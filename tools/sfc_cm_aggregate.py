#!/usr/bin/env python3
"""SFC CM フレーム分類の集計。

入力（MEASUREMENT_DIR 内）:
  corpus.tsv            sfc_cm_sampler.py の出力（no, id, dur_s, stratum, query, channel, title）
  coding_part*.tsv      1回目分類（縮小シート・題名あり）。12列・ヘッダなし
  pass2_part*.tsv       2回目分類（原寸・題名なし）。15列・ヘッダなし
  exclusions.tsv        任意。「no<TAB>理由」。集計から外す投稿（別商品との連結など）
  title_aliases.tsv     任意。「別表記<TAB>正規の題名」。同じCMの題名ゆれを束ねる
  overrides.tsv         任意。pass2 と同じ15列。pass2 を上書き

出力: MEASUREMENT_DIR/results.json と results.md

数え方:
- 集計単位は「正規化したゲームタイトル × 尺区分（15秒/30秒）」。単位の重みは 1。
  同じ単位に属する複数の投稿は、各投稿に 1/投稿数 の重みを与えて束ねる。
- 「3点の並び」と「型」は投稿ごとに決め、上の重みで足す（同数の扱いに依存しない）。
- 標本点は各動画の 3 つの瞬間（約 25/50/75% 地点とされる）だけで、その間も前後も観測していない。
- 2回目分類の live フラグは人形・模型（P）にも立つ。人物・風景の実写だけを見るときは主分類 L を使う。
- フラグの 'Y?' は Y、'N?' は N として数える。1回目の C（実写とゲームの合成）は一致度の計算から外す。

使い方: python3 tools/sfc_cm_aggregate.py MEASUREMENT_DIR
"""
import collections
import csv
import glob
import json
import random
import re
import sys
import unicodedata
from pathlib import Path

P1_COLS = "no include reason game_title publisher year platform f1 f2 f3 endcard_info notes".split()
P2_COLS = ("no f1 f1_live f1_game f1_super f2 f2_live f2_game f2_super "
           "f3 f3_live f3_game f3_super readable_text notes").split()
CODES = ["L", "P", "G", "A", "E", "X"]
POS = ["f1", "f2", "f3"]
TYPES = ["実写主体・ゲーム画面なし", "実写まじり・ゲーム画面なし", "人形・模型主体・ゲーム画面なし",
         "実写系＋ゲーム画面", "絵・カード＋ゲーム画面", "ゲーム画面主体", "絵・カードのみ"]
ROMAN = {"viii": "8", "vii": "7", "vi": "6", "iv": "4", "iii": "3", "ii": "2", "v": "5", "i": "1"}
ROMAN_CHARS = {"ⅷ": "viii", "ⅶ": "vii", "ⅵ": "vi", "ⅴ": "v", "ⅳ": "iv", "ⅲ": "iii", "ⅱ": "ii", "ⅰ": "i"}


def read_tsv(pattern, cols):
    rows, bad = {}, 0
    for path in sorted(glob.glob(pattern)):
        for line in open(path, encoding="utf8"):
            f = line.rstrip("\n").split("\t")
            if len(f) != len(cols) or not f[0].lstrip("#").isdigit():
                bad += 1
                continue
            r = dict(zip(cols, f))
            r["no"] = r["no"].lstrip("#")
            rows[r["no"]] = r
    return rows, bad


def read_pairs(path):
    if not Path(path).exists():
        return {}
    out = {}
    for line in open(path, encoding="utf8"):
        if line.strip() and not line.startswith("#"):
            a, b = line.rstrip("\n").split("\t", 1)
            out[a.strip()] = b.strip()
    return out


def length_class(d):
    if 13 <= d <= 17:
        return "15s"
    if 28 <= d <= 33:
        return "30s"
    return None


def norm_title(t):
    """表記ゆれを吸収する。NFKC、括弧書きの除去、独立したローマ数字の算用数字化、記号の除去。"""
    for a, b in ROMAN_CHARS.items():  # NFKC はローマ数字を大文字の英字に分解するので先に置換する
        t = t.replace(a, b).replace(a.upper(), b)
    t = unicodedata.normalize("NFKC", t).lower()
    t = re.sub(r"\(.*?\)", "", t)
    t = re.sub(r"(?<![a-z])(viii|vii|vi|iv|iii|ii|v|i)(?![a-z])", lambda m: ROMAN[m.group(1)], t)
    return re.sub(r"[\s・\-‐―ー~〜:：!！?？'’\"“”.,、。/／&＆+＋…]", "", t)


def clean(code):
    """'A?' → ('A', True)。"""
    unsure = code.strip().endswith("?")
    c = code.strip().rstrip("?").upper()
    return (c if c in CODES + ["C"] else "X"), unsure


def yes(v):
    return v.strip().upper().startswith("Y")


def kappa(pairs, cats):
    n = len(pairs)
    if not n:
        return None, None
    po = sum(a == b for a, b in pairs) / n
    ca = collections.Counter(a for a, _ in pairs)
    cb = collections.Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in cats) / (n * n)
    return round((po - pe) / (1 - pe) if pe < 1 else 1.0, 4), round(po, 4)


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def boot_ci(values, reps=2000, seed=1):
    if len(values) < 2:
        return [None, None]
    rnd = random.Random(seed)
    ms = sorted(mean([rnd.choice(values) for _ in values]) for _ in range(reps))
    return [round(ms[int(0.025 * reps)], 4), round(ms[int(0.975 * reps)], 4)]


def tags_at(text, pos):
    """readable_text から、その地点（f1/f2/f3）のタグ種別の集合を取り出す。"""
    out = set()
    for item in text.split(";"):
        m = re.match(r"\s*(f[123]):([a-z_]+)", item)
        if m and m.group(1) == pos:
            out.add(m.group(2))
    return out


def upload_type(fr):
    """1投稿の3フレームから型を決める。fr[p] = {code, live, game, ...}"""
    n = collections.Counter(fr[p]["code"] for p in POS)
    game = sum(fr[p]["game"] for p in POS)
    lp = n["L"] + n["P"]
    if n["G"] >= 2:
        return "ゲーム画面主体"
    if game and lp:
        return "実写系＋ゲーム画面"
    if game:
        return "絵・カード＋ゲーム画面"
    if n["P"] >= 2:
        return "人形・模型主体・ゲーム画面なし"
    if lp >= 2:
        return "実写主体・ゲーム画面なし"
    if lp == 1:
        return "実写まじり・ゲーム画面なし"
    return "絵・カードのみ"


def main(mdir):
    m = Path(mdir)
    corpus = {r["no"]: r for r in csv.DictReader(open(m / "corpus.tsv", encoding="utf8"), delimiter="\t")}
    p1, bad1 = read_tsv(str(m / "coding_part*.tsv"), P1_COLS)
    p2, bad2 = read_tsv(str(m / "pass2_part*.tsv"), P2_COLS)
    ov, _ = read_tsv(str(m / "overrides.tsv"), P2_COLS)
    excl = read_pairs(m / "exclusions.tsv")
    alias = {norm_title(a): b for a, b in read_pairs(m / "title_aliases.tsv").items()}

    # --- 対象の絞り込み -------------------------------------------------
    funnel = collections.Counter()
    eligible = []
    for no, r in p1.items():
        funnel["coded"] += 1
        if r["include"] != "Y":
            funnel["excluded_" + ("unknown_platform" if r["include"] == "U" else (r["reason"] or "N"))] += 1
            continue
        funnel["judged_sfc_japan_cm"] += 1
        if not length_class(int(corpus[no]["dur_s"])):
            funnel["excluded_length_not_15_or_30"] += 1
        elif "multi_spot" in r["notes"] or "crt_reshoot" in r["notes"]:
            funnel["excluded_multispot_or_reshoot_note"] += 1
        elif no in excl:
            funnel["excluded_by_exclusions_tsv"] += 1
        else:
            funnel["eligible"] += 1
            eligible.append(no)

    # --- 採用コード（override > pass2）。pass2 が無い行だけ pass1 ----------
    def frames(no, use_pass2=True):
        src = (ov.get(no) or p2.get(no)) if use_pass2 else None
        out = {}
        if src:
            for p in POS:
                c, unsure = clean(src[p])
                out[p] = {"code": c, "unsure": unsure, "live": yes(src[p + "_live"]), "game": yes(src[p + "_game"]),
                          "super": yes(src[p + "_super"]), "tags": tags_at(src["readable_text"], p)}
            out["source"] = "override" if no in ov else "pass2"
        else:
            for p in POS:
                c, unsure = clean(p1[no][p])
                comp = c == "C"
                c = "L" if comp else c
                out[p] = {"code": c, "unsure": unsure, "live": c in "LP", "game": c == "G" or comp,
                          "super": None, "tags": set()}
            out["source"] = "pass1"
        return out

    # --- 一致度（1回目 vs 2回目） ----------------------------------------
    pairs, firm, unsure_pairs, disagree = [], [], [], collections.Counter()
    for no in eligible:
        if no not in p2:
            continue
        for p in POS:
            a, ua = clean(p1[no][p])
            b, _ = clean(p2[no][p])
            if a == "C":
                continue
            pairs.append((a, b))
            (unsure_pairs if ua else firm).append((a, b))
            if a != b:
                disagree[f"{a}->{b}"] += 1
    k_all, po_all = kappa(pairs, CODES)
    k_firm, po_firm = kappa(firm, CODES)
    k_uns, po_uns = kappa(unsure_pairs, CODES)
    lp = lambda c: "LP" if c in "LP" else c
    k_lp, po_lp = kappa([(lp(a), lp(b)) for a, b in pairs], ["LP", "G", "A", "E", "X"])

    # --- 単位（タイトル×尺） ---------------------------------------------
    units = collections.defaultdict(list)
    display = {}
    for no in eligible:
        raw = p1[no]["game_title"].strip()
        key_t = norm_title(raw)
        if key_t in alias:
            raw = alias[key_t]
            key_t = norm_title(raw)
        if not key_t:
            raw, key_t = f"（題名不明 #{no}）", f"untitled_{no}"
        key = (key_t, length_class(int(corpus[no]["dur_s"])))
        units[key].append(no)
        display.setdefault(key, re.sub(r"\s*\(.*?\)\s*$", "", raw))

    def profile(nos, use_pass2=True):
        w = 1 / len(nos)
        share = {p: collections.Counter() for p in POS}
        flag = {p: collections.Counter() for p in POS}
        seq, typ, game_pos = collections.Counter(), collections.Counter(), collections.Counter()
        uploads_with_game = 0
        for no in nos:
            fr = frames(no, use_pass2)
            for p in POS:
                f = fr[p]
                share[p][f["code"]] += w
                flag[p]["live"] += w * f["live"]
                flag[p]["game"] += w * f["game"]
                flag[p]["P_unsure"] += w * (f["code"] == "P" and f["unsure"])
                flag[p]["card_live"] += w * (f["code"] == "E" and f["live"])
                if f["super"] is not None:
                    flag[p]["super"] += w * f["super"]
                    flag[p]["notice"] += w * bool(f["tags"] & {"date", "status", "price"})
                    flag[p]["notice_or_title"] += w * bool(f["tags"] & {"date", "status", "price", "title"})
            seq["-".join(fr[p]["code"] for p in POS)] += w
            typ[upload_type(fr)] += w
            g = [fr[p]["game"] for p in POS]
            if any(g):
                uploads_with_game += 1
                game_pos["mid_only" if g == [False, True, False]
                         else "two_or_more" if sum(g) >= 2 else "first_or_last_only"] += w
        return {"share": share, "flag": flag, "seq": seq, "type": typ, "game_pos": game_pos,
                "no_game": 1 - sum(game_pos.values()), "uploads_with_game": uploads_with_game}

    profiles = {}
    for key, nos in units.items():
        pr = profile(nos)
        years = [p1[n]["year"] for n in nos if re.fullmatch(r"19\d\d", p1[n]["year"])]
        pubs = [p1[n]["publisher"] for n in nos if p1[n]["publisher"]]
        sh = pr["share"]
        pr.update({
            "title": display[key], "length": key[1], "uploads": len(nos), "nos": nos,
            "year": collections.Counter(years).most_common(1)[0][0] if years else "",
            "publisher": collections.Counter(pubs).most_common(1)[0][0] if pubs else "",
            "generic_only": all(corpus[n]["stratum"] == "generic" for n in nos),
            "live_share3": mean([sh[p]["L"] + sh[p]["P"] for p in POS]),
            "L_share3": mean([sh[p]["L"] for p in POS]),
            "P_share3": mean([sh[p]["P"] for p in POS]),
            "P_unsure_share3": mean([pr["flag"][p]["P_unsure"] for p in POS]),
            "game_share3": mean([sh[p]["G"] for p in POS]),
            "art_share3": mean([sh[p]["A"] for p in POS]),
            "card_share3": mean([sh[p]["E"] for p in POS]),
        })
        profiles[key] = pr

    def summarise(keys):
        ps = [profiles[k] for k in keys]
        if not ps:
            return None
        out = {"units": len(ps), "uploads": sum(p["uploads"] for p in ps), "by_position": {}}
        for p in POS:
            b = {c: round(mean([x["share"][p][c] for x in ps]), 6) for c in CODES}
            for name in ("live", "game", "card_live", "super", "notice", "notice_or_title"):
                b[name] = round(mean([x["flag"][p][name] for x in ps]), 6)
            out["by_position"][p] = b
        for name in ("live_share3", "L_share3", "P_share3", "P_unsure_share3", "game_share3", "art_share3", "card_share3"):
            vals = [x[name] for x in ps]
            out[name] = {"mean": round(mean(vals), 6), "ci95": boot_ci(vals)}
        out["live_share3_excluding_unsure_P"] = round(out["live_share3"]["mean"] - out["P_unsure_share3"]["mean"], 6)
        ls = [x["live_share3"] for x in ps]
        e = 1e-9
        out["live_share3_distribution_units"] = {
            "0": sum(v < e for v in ls), "0<v<=1/3": sum(e <= v <= 1 / 3 + e for v in ls),
            "1/3<v<=2/3": sum(1 / 3 + e < v <= 2 / 3 + e for v in ls), ">2/3": sum(v > 2 / 3 + e for v in ls)}
        out["units_with_any_L_frame"] = sum(x["L_share3"] > e for x in ps)
        out["units_with_any_live_or_model_flag"] = sum(any(x["flag"][p]["live"] > e for p in POS) for x in ps)
        tsum, ssum, gsum = collections.Counter(), collections.Counter(), collections.Counter()
        for x in ps:
            tsum.update(x["type"])
            ssum.update(x["seq"])
            gsum.update(x["game_pos"])
        out["types_unit_weighted"] = {t: round(tsum[t], 2) for t in TYPES}
        out["sequences_unit_weighted_top"] = [(s, round(v, 2)) for s, v in ssum.most_common(14)]
        out["no_game_unit_weighted"] = round(mean([x["no_game"] for x in ps]), 6)
        out["units_no_game_in_any_upload"] = sum(x["uploads_with_game"] == 0 for x in ps)
        out["game_position_unit_weighted"] = {k: round(v, 2) for k, v in gsum.items()}
        return out

    def upload_level(nos):
        seq, typ, gp = collections.Counter(), collections.Counter(), collections.Counter()
        for no in nos:
            fr = frames(no)
            seq["-".join(fr[p]["code"] for p in POS)] += 1
            typ[upload_type(fr)] += 1
            g = [fr[p]["game"] for p in POS]
            gp["none" if not any(g) else "mid_only" if g == [False, True, False]
               else "two_or_more" if sum(g) >= 2 else "first_or_last_only"] += 1
        return {"uploads": len(nos), "sequences_top": seq.most_common(14), "types": {t: typ[t] for t in TYPES},
                "game_position": dict(gp)}

    keys = list(profiles)
    sens = collections.defaultdict(list)  # 感度: 1回目分類だけで同じ集計をした場合
    for nos in units.values():
        sh = profile(nos, use_pass2=False)["share"]
        sens["live"].append(mean([sh[p]["L"] + sh[p]["P"] for p in POS]))
        sens["game"].append(mean([sh[p]["G"] for p in POS]))
        sens["art"].append(mean([sh[p]["A"] for p in POS]))
        sens["card"].append(mean([sh[p]["E"] for p in POS]))

    def text_units(tag):  # その種別の文字が、どの投稿のどの地点でも一度でも読めた単位の数（下限）
        return sum(any(tag in frames(n)[p]["tags"] for n in profiles[k]["nos"] for p in POS) for k in keys)

    titles = {k[0] for k in keys}
    both = sum(1 for t in titles if (t, "15s") in profiles and (t, "30s") in profiles)
    pubs = collections.Counter(profiles[k]["publisher"] for k in keys)
    results = {
        "inputs": {"corpus": len(corpus), "pass1_rows": len(p1), "pass2_rows": len(p2), "override_rows": len(ov),
                   "exclusions": len(excl), "aliases": len(alias),
                   "malformed_lines_skipped": {"pass1": bad1, "pass2": bad2}},
        "funnel": dict(funnel),
        "counts": {"eligible_uploads": len(eligible), "units": len(keys), "titles": len(titles),
                   "titles_with_both_lengths": both,
                   "eligible_by_length": dict(collections.Counter(length_class(int(corpus[n]["dur_s"])) for n in eligible)),
                   "final_code_source": dict(collections.Counter(frames(n)["source"] for n in eligible))},
        "reliability": {"note": "2回目は1回目が採用した投稿だけを分類した。採否・機種・題名・発売元・年は1回だけの判定で、κは主分類コードだけを対象とする",
                        "frames_compared": len(pairs), "agreement": po_all, "kappa_6class": k_all,
                        "agreement_LP_merged": po_lp, "kappa_LP_merged": k_lp,
                        "pass1_firm_frames": {"n": len(firm), "agreement": po_firm, "kappa": k_firm},
                        "pass1_unsure_frames": {"n": len(unsure_pairs), "agreement": po_uns, "kappa": k_uns},
                        "top_disagreements_pass1_to_pass2": disagree.most_common(12)},
        "sensitivity_pass1_only_share3": {k_: round(mean(v), 6) for k_, v in sens.items()},
        "readable_text_units_lower_bound": {t: text_units(t) for t in
                                            ("date", "status", "price", "title", "mega", "disclaimer", "sfclogo", "publogo", "credit", "copy")},
        "all": summarise(keys),
        "all_upload_level": upload_level(eligible),
        "by_length": {lc: summarise([k for k in keys if k[1] == lc]) for lc in ("15s", "30s")},
        "by_stratum": {"generic_only": summarise([k for k in keys if profiles[k]["generic_only"]]),
                       "found_by_title_query": summarise([k for k in keys if not profiles[k]["generic_only"]])},
        "by_publisher": {pb: summarise([k for k in keys if profiles[k]["publisher"] == pb])
                         for pb, n in pubs.most_common() if pb and n >= 6},
        "by_year": {y: summarise([k for k in keys if profiles[k]["year"] == y])
                    for y in sorted({p["year"] for p in profiles.values() if p["year"]})},
        "units": [{"title": p["title"], "length": p["length"], "uploads": p["uploads"], "nos": p["nos"],
                   "year": p["year"], "publisher": p["publisher"], "generic_only": p["generic_only"],
                   "live_share3": round(p["live_share3"], 4), "L_share3": round(p["L_share3"], 4),
                   "P_share3": round(p["P_share3"], 4), "game_share3": round(p["game_share3"], 4),
                   "art_share3": round(p["art_share3"], 4), "card_share3": round(p["card_share3"], 4),
                   "upload_sequences": {s: round(v * p["uploads"]) for s, v in p["seq"].items()},
                   "upload_types": {t: round(v * p["uploads"]) for t, v in p["type"].items()}}
                  for p in sorted(profiles.values(), key=lambda p: (p["title"], p["length"]))],
    }
    (m / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf8")

    # --- 人が読む用の要約 ----------------------------------------------
    pct = lambda v: "—" if v is None else f"{100 * v:.0f}%"
    pc1 = lambda v: "—" if v is None else f"{100 * v:.1f}%"
    R = results["reliability"]
    C = results["counts"]
    L = ["# SFC CM フレーム分類 集計結果（自動生成）", "",
         f"- 絞り込み: コーパス {len(corpus)} → SFC・日本向けCMと判定 {funnel['judged_sfc_japan_cm']} → 集計対象 {C['eligible_uploads']} 投稿"
         f"（15秒級 {C['eligible_by_length'].get('15s', 0)}、30秒級 {C['eligible_by_length'].get('30s', 0)}）"
         f" → {C['units']} 単位 / {C['titles']} タイトル（15秒と30秒の両方がある題名 {C['titles_with_both_lengths']}）",
         f"- 除外の内訳: {dict(funnel)}",
         f"- 採用コードの出所: {C['final_code_source']}",
         f"- 一致度（1回目 vs 2回目、主分類コード、{R['frames_compared']} フレーム）: 一致率 {pc1(R['agreement'])}、κ={R['kappa_6class']}。"
         f"1回目が確信ありとしたフレーム（{R['pass1_firm_frames']['n']}）: {pc1(R['pass1_firm_frames']['agreement'])}／κ={R['pass1_firm_frames']['kappa']}。"
         f"1回目が「?」を付けたフレーム（{R['pass1_unsure_frames']['n']}）: {pc1(R['pass1_unsure_frames']['agreement'])}／κ={R['pass1_unsure_frames']['kappa']}",
         f"- 注意: {R['note']}",
         f"- 不一致の内訳（1回目→2回目、上位）: {R['top_disagreements_pass1_to_pass2']}",
         f"- 感度（1回目分類だけで集計した3点平均）: { {k_: pc1(v) for k_, v in results['sensitivity_pass1_only_share3'].items()} }",
         f"- 文字が一度でも読めた単位の数（下限）: {results['readable_text_units_lower_bound']}", ""]

    def table(title, s, up=None):
        if not s:
            return
        L.extend([f"## {title}（{s['units']} 単位 / {s['uploads']} 投稿）", "",
                  "| 地点 | 実写 L | 人形・模型 P | ゲーム画面 G | アニメ・CG・絵 A | カード E | 不明 X | 実写か人形・模型が画面内 | ゲーム画面が画面内 | 文字あり（種類を問わず） | 発売日・発売状況・価格が読めた | 左に題名を加えた場合 | 実写を背景にしたカード |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|"])
        for p, lab in zip(POS, ("約25%", "約50%", "約75%")):
            b = s["by_position"][p]
            L.append(f"| {lab} | " + " | ".join(pct(b[c]) for c in CODES) +
                     f" | {pct(b['live'])} | {pct(b['game'])} | {pct(b['super'])} | {pct(b['notice'])} | {pct(b['notice_or_title'])} | {pct(b['card_live'])} |")
        L.extend(["",
                  f"- 3点平均: 実写系(L+P) {pc1(s['live_share3']['mean'])}（95%CI {s['live_share3']['ci95']}）＝ 実写 L {pc1(s['L_share3']['mean'])} ＋ 人形・模型 P {pc1(s['P_share3']['mean'])}。"
                  f"P のうち「CGかもしれない」保留付きを除くと実写系 {pc1(s['live_share3_excluding_unsure_P'])}",
                  f"- 3点平均: ゲーム画面 {pc1(s['game_share3']['mean'])}（{s['game_share3']['ci95']}）、アニメ・CG・絵 {pc1(s['art_share3']['mean'])}、カード {pc1(s['card_share3']['mean'])}",
                  f"- 単位ごとの実写系3点平均の分布: {s['live_share3_distribution_units']}",
                  f"- 主分類が実写 L のフレームを1つ以上持つ単位: {s['units_with_any_L_frame']}。実写か人形・模型のフラグを1つ以上持つ単位: {s['units_with_any_live_or_model_flag']}",
                  f"- ゲーム画面が3点のどこにも無い: 単位重み {pc1(s['no_game_unit_weighted'])}。どの投稿にも無い単位 {s['units_no_game_in_any_upload']}",
                  f"- ゲーム画面がある場合の位置（単位重み）: {s['game_position_unit_weighted']}",
                  f"- 型（単位重み。投稿ごとに決めて 1/投稿数 で足す）: {s['types_unit_weighted']}",
                  f"- 3点の並び（単位重み、上位）: {s['sequences_unit_weighted_top']}"])
        if up:
            L.extend([f"- 投稿単位（重みなし、{up['uploads']} 投稿）の型: {up['types']}",
                      f"- 投稿単位の並び（上位）: {up['sequences_top']}", f"- 投稿単位のゲーム画面の位置: {up['game_position']}"])
        L.append("")

    table("全体", results["all"], results["all_upload_level"])
    for lc in ("15s", "30s"):
        table(f"尺 {lc}", results["by_length"][lc])
    table("年・機種だけの検索でしか見つからなかった単位（偏りの対照）", results["by_stratum"]["generic_only"])
    table("タイトル指名の検索で見つかった投稿を含む単位", results["by_stratum"]["found_by_title_query"])
    L.extend(["## 発売元別（6単位以上。発売元名は1回目分類で記入されたもので、空欄の単位は含まない）", "",
              "| 発売元 | 単位数 | 実写系(L+P) | うち実写 L | ゲーム画面 | アニメ・CG・絵 | カード |", "|---|---:|---:|---:|---:|---:|---:|"])
    for pb, sm in results["by_publisher"].items():
        L.append(f"| {pb} | {sm['units']} | {pc1(sm['live_share3']['mean'])} | {pc1(sm['L_share3']['mean'])} | "
                 f"{pc1(sm['game_share3']['mean'])} | {pc1(sm['art_share3']['mean'])} | {pc1(sm['card_share3']['mean'])} |")
    L.append("")
    for y, s in results["by_year"].items():
        table(f"{y}年（投稿の題名などから年が分かる単位のみ。年は投稿者の記載に依存）", s)
    (m / "results.md").write_text("\n".join(L) + "\n", encoding="utf8")
    a = results["all"]
    print(f"eligible={len(eligible)} units={len(keys)} titles={len(titles)} kappa={k_all} "
          f"live={a['live_share3']['mean']:.4f} L={a['L_share3']['mean']:.4f} game={a['game_share3']['mean']:.4f}")


if __name__ == "__main__":
    main(sys.argv[1])
