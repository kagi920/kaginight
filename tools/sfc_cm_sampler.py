#!/usr/bin/env python3
"""90年代スーパーファミコンCMの標本採取。

YouTube の検索結果ページから個別CM動画（10〜65秒）の題名・尺を集め、
各動画の公開自動サムネイル 3 枚（hq1/hq2/hq3.jpg。動画のおよそ 25/50/75% 地点と
されるが公式仕様としては未確認）を取得し、目視分類用のコンタクトシートを作る。

使い方:
    python3 tools/sfc_cm_sampler.py QUERIES.tsv OUTDIR

QUERIES.tsv は「層<TAB>検索語」を 1 行 1 件。層は title（タイトル指名）か
generic（年・機種のみの検索語。名作への偏りを下げるための対照層）。
出力: OUTDIR/corpus.tsv, OUTDIR/thumbs/<id>_<n>.jpg, OUTDIR/sheets/sheet_NN.jpg
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
FONT = "/usr/share/fonts/opentype/ipafont-gothic/ipag.ttf"
MIN_S, MAX_S = 10, 65
PER_SHEET = 10


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ja"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()


def seconds(text):
    parts = [int(p) for p in text.split(":")]
    return sum(p * 60 ** i for i, p in enumerate(reversed(parts)))


def search(query):
    html = fetch("https://www.youtube.com/results?search_query=" + urllib.parse.quote(query)).decode("utf8", "ignore")
    m = re.search(r"var ytInitialData = (\{.*?\});</script>", html, re.S)
    if not m:
        return []
    found = []

    def walk(o):
        if isinstance(o, dict):
            v = o.get("videoRenderer")
            if v and v.get("lengthText"):
                found.append({
                    "id": v["videoId"],
                    "title": "".join(r.get("text", "") for r in v.get("title", {}).get("runs", [])),
                    "dur": seconds(v["lengthText"]["simpleText"]),
                    "channel": "".join(r.get("text", "") for r in v.get("ownerText", {}).get("runs", [])),
                })
            for x in o.values():
                walk(x)
        elif isinstance(o, list):
            for x in o:
                walk(x)

    walk(json.loads(m.group(1)))
    return found


def is_cm(title):
    t = title.lower()
    return any(k in t for k in ("cm", "ｃｍ", "コマーシャル", "commercial"))


def main(queries_path, outdir):
    out = Path(outdir)
    (out / "thumbs").mkdir(parents=True, exist_ok=True)
    (out / "sheets").mkdir(exist_ok=True)
    corpus = {}
    for line in Path(queries_path).read_text(encoding="utf8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        stratum, query = line.split("\t", 1)
        try:
            results = search(query)
        except Exception as e:  # ネットワーク失敗は記録して続行
            print(f"SEARCH-FAIL\t{query}\t{e}", file=sys.stderr)
            continue
        kept = 0
        for v in results:
            if not (MIN_S <= v["dur"] <= MAX_S) or not is_cm(v["title"]) or v["id"] in corpus:
                continue
            corpus[v["id"]] = {**v, "stratum": stratum, "query": query}
            kept += 1
        print(f"{stratum}\t{query}\t{len(results)} hits\t{kept} new", file=sys.stderr)
        time.sleep(1.0)

    rows = []
    for vid, v in corpus.items():
        ok = True
        for n in (1, 2, 3):
            p = out / "thumbs" / f"{vid}_{n}.jpg"
            if not p.exists():
                try:
                    p.write_bytes(fetch(f"https://i.ytimg.com/vi/{vid}/hq{n}.jpg"))
                except Exception:
                    ok = False
        if ok:
            rows.append(v)

    with open(out / "corpus.tsv", "w", encoding="utf8") as f:
        f.write("no\tid\tdur_s\tstratum\tquery\tchannel\ttitle\n")
        for i, v in enumerate(rows, 1):
            title = v["title"].replace("\t", " ")
            f.write(f"{i}\t{v['id']}\t{v['dur']}\t{v['stratum']}\t{v['query']}\t{v['channel']}\t{title}\n")

    font = ImageFont.truetype(FONT, 18)
    tw, th, label_h = 320, 240, 26
    for s in range(0, len(rows), PER_SHEET):
        chunk = rows[s:s + PER_SHEET]
        sheet = Image.new("RGB", (tw * 3, (th + label_h) * len(chunk)), "white")
        d = ImageDraw.Draw(sheet)
        for r, v in enumerate(chunk):
            y = r * (th + label_h)
            d.text((4, y + 3), f"#{s + r + 1} [{v['dur']}s] {v['title'][:60]}", fill="black", font=font)
            for n in (1, 2, 3):
                im = Image.open(out / "thumbs" / f"{v['id']}_{n}.jpg").convert("RGB").resize((tw, th))
                sheet.paste(im, ((n - 1) * tw, y + label_h))
        sheet.save(out / "sheets" / f"sheet_{s // PER_SHEET + 1:02d}.jpg", quality=80)
    print(f"corpus={len(rows)} sheets={(len(rows) + PER_SHEET - 1) // PER_SHEET}", file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
