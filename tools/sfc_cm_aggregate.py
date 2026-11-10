#!/usr/bin/env python3
"""SFC CM フレーム分類の集計。

入力（MEASUREMENT_DIR 内）:
  corpus.tsv            sfc_cm_sampler.py の出力（no, id, dur_s, stratum, query, channel, title）
  coding_part*.tsv      1回目分類（縮小シート・題名あり）。12列・ヘッダなし
  pass2_part*.tsv       2回目分類（原寸・題名なし・独立）。15列・ヘッダなし
  overrides.tsv         任意。原寸で人が読んで確定した行（pass2 と同じ15列）。pass2 を上書き

出力: MEASUREMENT_DIR/results.json と results.md

集計単位は「正規化したゲームタイトル × 尺区分（15秒/30秒）」。同じ単位に属する
複数の投稿は標本点として束ね、単位ごとの重みは 1 とする。
標本点は各動画の約 25/50/75% 地点の 3 点だけなので、冒頭と末尾（各およそ 1/8）は
観測していない。エンドカードの比率は過小に出る。

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


def length_class(d):
    if 13 <= d <= 17:
        return "15s"
    if 28 <= d <= 33:
        return "30s"
    return None


ROMAN = [("ⅷ", "8"), ("ⅶ", "7"), ("ⅵ", "6"), ("ⅴ", "5"), ("ⅳ", "4"), ("ⅲ", "3"), ("ⅱ", "2"), ("ⅰ", "1")]


def norm_title(t):
    """表記ゆれを吸収するタイトル正規化（NFKC・記号除去・末尾ローマ数字の算用数字化）。"""
    t = t.lower()
    for a, b in ROMAN:  # NFKC はローマ数字を英字に分解するので先に置換する
        t = t.replace(a, b)
    t = unicodedata.normalize("NFKC", t)
    t = re.sub(r"\(.*?\)", "", t)
    t = re.sub(r"[\s・\-‐―ー~〜:：!！?？'’\"“”.,、。/／&＆+＋]", "", t)
    for a, b in (("viii", "8"), ("vii", "7"), ("vi", "6"), ("iv", "4"), ("iii", "3"), ("ii", "2")):
        t = re.sub(a + r"$", b, t)
    t = re.sub(r"(?<![a-z])v$", "5", t)
    return t


def clean(code):
    """'A?' → ('A', True)。1回目の C（実写とゲームの合成）は L として扱い flags で補う。"""
    unsure = code.endswith("?")
    c = code.rstrip("?").strip().upper()
    return (c if c in CODES + ["C"] else "X"), unsure


def kappa(pairs, cats):
    n = len(pairs)
    if not n:
        return None, 0
    po = sum(a == b for a, b in pairs) / n
    ca = collections.Counter(a for a, _ in pairs)
    cb = collections.Counter(b for _, b in pairs)
    pe = sum(ca[c] * cb[c] for c in cats) / (n * n)
    return ((po - pe) / (1 - pe) if pe < 1 else 1.0), po


def mean(xs):
    return sum(xs) / len(xs) if xs else float("nan")


def boot_ci(values, reps=2000, seed=1):
    if len(values) < 2:
        return [None, None]
    rnd = random.Random(seed)
    ms = sorted(mean([rnd.choice(values) for _ in values]) for _ in range(reps))
    return [round(ms[int(0.025 * reps)], 4), round(ms[int(0.975 * reps)], 4)]


def main(mdir):
    m = Path(mdir)
    corpus = {r["no"]: r for r in csv.DictReader(open(m / "corpus.tsv", encoding="utf8"), delimiter="\t")}
    p1, bad1 = read_tsv(str(m / "coding_part*.tsv"), P1_COLS)
    p2, bad2 = read_tsv(str(m / "pass2_part*.tsv"), P2_COLS)
    ov, _ = read_tsv(str(m / "overrides.tsv"), P2_COLS)

    # --- 対象の絞り込み -------------------------------------------------
    funnel = collections.Counter()
    eligible = []
    for no, r in p1.items():
        funnel["coded"] += 1
        if r["include"] != "Y":
            funnel["excluded_" + (r["include"] == "U" and "unknown_platform" or (r["reason"] or "N"))] += 1
            continue
        lc = length_class(int(corpus[no]["dur_s"]))
        if not lc:
            funnel["excluded_length_not_15_or_30"] += 1
            continue
        if "multi_spot" in r["notes"] or "crt_reshoot" in r["notes"]:
            funnel["excluded_multispot_or_reshoot"] += 1
            continue
        funnel["eligible"] += 1
        eligible.append(no)

    # --- 採用コード（override > pass2 > pass1）と一致度 ------------------
    def final(no):
        src = ov.get(no) or p2.get(no)
        if src:
            out = {"source": "override" if no in ov else "pass2"}
            for p in POS:
                c, unsure = clean(src[p])
                out[p] = {"code": c, "unsure": unsure, "live": src[p + "_live"].upper() == "Y",
                          "game": src[p + "_game"].upper() == "Y", "super": src[p + "_super"].upper() == "Y"}
            out["text"] = src["readable_text"]
            return out
        r = p1[no]
        out = {"source": "pass1", "text": r["endcard_info"]}
        for p in POS:
            c, unsure = clean(r[p])
            comp = c == "C"
            c = "L" if comp else c
            out[p] = {"code": c, "unsure": unsure, "live": c in "LP", "game": c == "G" or comp, "super": None}
        return out

    pairs, disagree = [], collections.Counter()
    for no in eligible:
        if no not in p2:
            continue
        for p in POS:
            a, _ = clean(p1[no][p])
            b, _ = clean(p2[no][p])
            if a == "C":  # 2回目には C が無いので比較から外す
                continue
            pairs.append((a, b))
            if a != b:
                disagree[f"{a}->{b}"] += 1
    k, po = kappa(pairs, CODES)
    lp = lambda c: "LP" if c in "LP" else c  # 実写と人形・模型を束ねた場合
    k2, po2 = kappa([(lp(a), lp(b)) for a, b in pairs], ["LP", "G", "A", "E", "X"])

    # --- 単位（タイトル×尺）に束ねる ------------------------------------
    units = collections.defaultdict(list)
    for no in eligible:
        r = p1[no]
        key = (norm_title(r["game_title"]) or "untitled_" + no, length_class(int(corpus[no]["dur_s"])))
        units[key].append(no)

    def unit_profile(nos):
        prof = {p: collections.Counter() for p in POS}
        flags = {p: collections.Counter() for p in POS}
        for no in nos:
            f = final(no)
            for p in POS:
                prof[p][f[p]["code"]] += 1
                flags[p]["live"] += f[p]["live"]
                flags[p]["game"] += f[p]["game"]
                if f[p]["super"] is not None:
                    flags[p]["super"] += f[p]["super"]
                    flags[p]["super_n"] += 1
        n = len(nos)
        share = {p: {c: prof[p][c] / n for c in CODES} for p in POS}
        fl = {p: {"live": flags[p]["live"] / n, "game": flags[p]["game"] / n,
                  "super": (flags[p]["super"] / flags[p]["super_n"]) if flags[p]["super_n"] else None} for p in POS}
        return share, fl

    profiles = {}
    for key, nos in units.items():
        share, fl = unit_profile(nos)
        r0 = p1[nos[0]]
        years = [p1[n]["year"] for n in nos if re.fullmatch(r"19\d\d", p1[n]["year"])]
        pubs = [p1[n]["publisher"] for n in nos if p1[n]["publisher"]]
        texts = ";".join(final(n)["text"] for n in nos)
        any_live = any(fl[p]["live"] > 0 for p in POS)
        any_game = any(fl[p]["game"] > 0 for p in POS)
        any_art = any(share[p]["A"] > 0 for p in POS)
        pattern = ("live+game" if any_live and any_game else "live_only" if any_live
                   else "game(+art)" if any_game else "art_only" if any_art else "card_only")
        profiles[key] = {
            "title": r0["game_title"], "length": key[1], "uploads": len(nos), "nos": nos,
            "year": collections.Counter(years).most_common(1)[0][0] if years else "",
            "publisher": collections.Counter(pubs).most_common(1)[0][0] if pubs else "",
            "stratum_generic": any(corpus[n]["stratum"] == "generic" for n in nos),
            "share": share, "flags": fl, "pattern": pattern, "text": texts,
            "live_share3": mean([share[p]["L"] + share[p]["P"] for p in POS]),
            "game_share3": mean([share[p]["G"] for p in POS]),
            "art_share3": mean([share[p]["A"] for p in POS]),
            "card_share3": mean([share[p]["E"] for p in POS]),
        }

    def summarise(keys):
        ps = [profiles[k] for k in keys]
        if not ps:
            return None
        out = {"units": len(ps), "uploads": sum(p["uploads"] for p in ps), "by_position": {}}
        for p in POS:
            out["by_position"][p] = {c: round(mean([x["share"][p][c] for x in ps]), 4) for c in CODES}
            out["by_position"][p]["live_present"] = round(mean([x["flags"][p]["live"] for x in ps]), 4)
            out["by_position"][p]["game_present"] = round(mean([x["flags"][p]["game"] for x in ps]), 4)
            sup = [x["flags"][p]["super"] for x in ps if x["flags"][p]["super"] is not None]
            out["by_position"][p]["super_present"] = round(mean(sup), 4) if sup else None
        for name in ("live_share3", "game_share3", "art_share3", "card_share3"):
            vals = [x[name] for x in ps]
            out[name] = {"mean": round(mean(vals), 4), "ci95": boot_ci(vals)}
        out["patterns"] = dict(collections.Counter(x["pattern"] for x in ps))
        ls = sorted(x["live_share3"] for x in ps)
        out["live_share3_distribution"] = {
            "0": sum(v == 0 for v in ls), "0<v<=1/3": sum(0 < v <= 1 / 3 + 1e-9 for v in ls),
            "1/3<v<=2/3": sum(1 / 3 + 1e-9 < v <= 2 / 3 + 1e-9 for v in ls), ">2/3": sum(v > 2 / 3 + 1e-9 for v in ls)}
        tags = collections.Counter()
        for x in ps:
            t = x["text"]
            for tag in ("price", "date", "mega", "disclaimer", "sfclogo", "publogo", "status", "credit", "copy"):
                tags[tag] += (tag + ":" in t) or (tag in ("sfclogo", "publogo") and tag in t)
        out["readable_text_units"] = {k: v for k, v in tags.items()}
        return out

    keys = list(profiles)
    results = {
        "inputs": {"corpus": len(corpus), "pass1_rows": len(p1), "pass2_rows": len(p2), "override_rows": len(ov),
                   "malformed_lines_skipped": {"pass1": bad1, "pass2": bad2}},
        "funnel": dict(funnel),
        "duration_all_uploads": dict(collections.Counter(
            length_class(int(r["dur_s"])) or ("58-63s" if 58 <= int(r["dur_s"]) <= 63 else "other")
            for r in corpus.values())),
        "duration_eligible": dict(collections.Counter(length_class(int(corpus[n]["dur_s"])) for n in eligible)),
        "reliability": {"frames_compared": len(pairs), "agreement": round(po, 4) if pairs else None,
                        "kappa_6class": round(k, 4) if k is not None else None,
                        "agreement_LP_merged": round(po2, 4) if pairs else None,
                        "kappa_LP_merged": round(k2, 4) if k2 is not None else None,
                        "top_disagreements": disagree.most_common(12)},
        "final_code_source": dict(collections.Counter(final(n)["source"] for n in eligible)),
        "all": summarise(keys),
        "by_length": {lc: summarise([k for k in keys if k[1] == lc]) for lc in ("15s", "30s")},
        "by_stratum": {"generic": summarise([k for k in keys if profiles[k]["stratum_generic"]]),
                       "title_only": summarise([k for k in keys if not profiles[k]["stratum_generic"]])},
        "by_year": {y: summarise([k for k in keys if profiles[k]["year"] == y])
                    for y in sorted({p["year"] for p in profiles.values() if p["year"]})},
        "units": [{k2_: v for k2_, v in p.items() if k2_ not in ("share", "flags")} |
                  {"codes": {pos: max(p["share"][pos], key=p["share"][pos].get) for pos in POS}}
                  for p in sorted(profiles.values(), key=lambda p: (p["title"], p["length"]))],
    }
    (m / "results.json").write_text(json.dumps(results, ensure_ascii=False, indent=1), encoding="utf8")

    # --- 人が読む用の要約 ----------------------------------------------
    pct = lambda v: "—" if v is None else f"{100 * v:.0f}%"
    L = ["# SFC CM フレーム分類 集計結果（自動生成）", "",
         f"- コーパス {len(corpus)} 本 → 1回目分類 {len(p1)} 行 → 集計対象 {len(eligible)} 投稿 → {len(keys)} 単位（タイトル×尺）",
         f"- 2回目分類 {len(p2)} 行、上書き {len(ov)} 行。採用元: {results['final_code_source']}",
         f"- 一致度（1回目 vs 2回目、{len(pairs)} フレーム）: 一致率 {pct(po) if pairs else '—'}、κ={results['reliability']['kappa_6class']}"
         f"（実写と人形・模型を束ねると 一致率 {pct(po2) if pairs else '—'}、κ={results['reliability']['kappa_LP_merged']}）", ""]

    def table(title, s):
        if not s:
            return
        L.extend([f"## {title}（{s['units']} 単位 / {s['uploads']} 投稿）", "",
                  "| 地点 | 実写 L | 人形・模型 P | ゲーム画面 G | アニメ・CG・絵 A | カード E | 不明 X | 実写が画面内 | ゲーム画面が画面内 |",
                  "|---|---:|---:|---:|---:|---:|---:|---:|---:|"])
        for p, lab in zip(POS, ("約25%", "約50%", "約75%")):
            b = s["by_position"][p]
            L.append(f"| {lab} | " + " | ".join(pct(b[c]) for c in CODES) + f" | {pct(b['live_present'])} | {pct(b['game_present'])} |")
        L.extend(["", f"- 3点平均: 実写系(L+P) {pct(s['live_share3']['mean'])}（95%CI {s['live_share3']['ci95']}）、"
                      f"ゲーム画面 {pct(s['game_share3']['mean'])}（{s['game_share3']['ci95']}）、"
                      f"アニメ・CG・絵 {pct(s['art_share3']['mean'])}、カード {pct(s['card_share3']['mean'])}",
                  f"- 構成パターン: {s['patterns']}", f"- 実写系3点平均の分布: {s['live_share3_distribution']}",
                  f"- 読み取れたテロップ（単位数、下限値）: {s['readable_text_units']}", ""])

    table("全体", results["all"])
    for lc in ("15s", "30s"):
        table(f"尺 {lc}", results["by_length"][lc])
    table("対照層（年・機種のみの検索で見つかった単位）", results["by_stratum"]["generic"])
    table("指名層のみ（タイトル指名検索でのみ見つかった単位）", results["by_stratum"]["title_only"])
    for y, s in results["by_year"].items():
        table(f"{y}年（題名に年がある単位のみ）", s)
    (m / "results.md").write_text("\n".join(L) + "\n", encoding="utf8")
    print(f"eligible={len(eligible)} units={len(keys)} pass2={len(p2)} kappa={results['reliability']['kappa_6class']}")


if __name__ == "__main__":
    main(sys.argv[1])
