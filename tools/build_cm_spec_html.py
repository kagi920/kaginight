#!/usr/bin/env python3
"""Markdown の仕様書を、インクリメンタル検索つきの単一 HTML に変換する。

使い方: python3 tools/build_cm_spec_html.py INPUT.md OUTPUT.html
依存: pip install markdown

検索欄に文字を入れるたびに、該当しない節（h2 単位）を隠し、該当箇所を強調する。
空白で区切ると AND 検索。全角・半角と大文字・小文字は区別しない。
節の該当判定は節全体の文字で行い、強調は語が装飾の境目をまたがない箇所にだけ付く。
絞り込み中に目次の項目を押すと、絞り込みを解除してその節へ移動する。外部ファイルや外部通信は使わない。
"""
import html
import re
import sys
from pathlib import Path

import markdown

CSS = """
:root{--bg:#fbfaf7;--fg:#1c1b19;--muted:#6b6862;--line:#dcd8cf;--accent:#8a5a00;--mark:#ffe08a;--card:#fff;--code:#f1eee7}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#14151a;--fg:#e6e3dc;--muted:#9a968d;--line:#33343c;--accent:#e2b866;--mark:#6b5200;--card:#1b1c22;--code:#22232a}}
:root[data-theme="dark"]{--bg:#14151a;--fg:#e6e3dc;--muted:#9a968d;--line:#33343c;--accent:#e2b866;--mark:#6b5200;--card:#1b1c22;--code:#22232a}
*{box-sizing:border-box}
html{scroll-padding-top:5rem}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.85 "Hiragino Sans","Noto Sans JP","Yu Gothic",Meiryo,sans-serif}
header.bar{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:.6rem 16px}
header.bar .in{max-width:1080px;margin:0 auto;display:flex;gap:.75rem;align-items:center;flex-wrap:wrap}
#q{flex:1 1 16rem;min-width:0;font:inherit;padding:.45rem .7rem;border:1px solid var(--line);border-radius:6px;background:var(--card);color:var(--fg)}
#q:focus{outline:2px solid var(--accent);outline-offset:1px}
#count{color:var(--muted);font-size:.85rem;white-space:nowrap}
main{max-width:1080px;margin:0 auto;padding:1.5rem 16px 6rem}
h1{font-size:1.6rem;line-height:1.4;margin:.5rem 0 1rem}
h2{font-size:1.3rem;margin:2.6rem 0 .8rem;padding-top:.8rem;border-top:2px solid var(--line)}
h3{font-size:1.1rem;margin:1.8rem 0 .5rem}
h4{font-size:1rem;margin:1.3rem 0 .4rem}
a{color:var(--accent);overflow-wrap:anywhere}
p,li{overflow-wrap:anywhere}
nav.toc{border:1px solid var(--line);border-radius:8px;background:var(--card);padding:.6rem 1rem;margin:1rem 0 1.5rem}
nav.toc summary{cursor:pointer;font-weight:600}
nav.toc ul{margin:.4rem 0;padding-left:1.2rem}
nav.toc li{margin:.15rem 0}
.tw{overflow-x:auto;margin:1rem 0;border:1px solid var(--line);border-radius:8px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:.9rem;line-height:1.6}
th,td{padding:.45rem .65rem;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}
th{background:var(--code);white-space:nowrap}
tr:last-child td{border-bottom:0}
code{background:var(--code);padding:.1em .35em;border-radius:4px;font-size:.9em}
pre{background:var(--code);padding:.9rem;border-radius:8px;overflow-x:auto;line-height:1.5}
pre code{background:none;padding:0}
blockquote{margin:1rem 0;padding:.2rem 1rem;border-left:4px solid var(--accent);background:var(--card)}
mark{background:var(--mark);color:inherit;padding:0 .1em;border-radius:2px}
section.hide{display:none}
#none{display:none;color:var(--muted);padding:2rem 0}
"""

JS = r"""
(function(){
  var q=document.getElementById('q'),count=document.getElementById('count'),none=document.getElementById('none');
  var secs=[].slice.call(document.querySelectorAll('main section'));
  function nk(s){return s.normalize('NFKC').toLowerCase();}
  var texts=secs.map(function(s){return nk(s.textContent);});
  function clear(){
    [].slice.call(document.querySelectorAll('main mark')).forEach(function(m){
      var p=m.parentNode;p.replaceChild(document.createTextNode(m.textContent),m);p.normalize();
    });
  }
  function esc(s){return s.replace(/[.*+?^${}()|[\]\\]/g,'\\$&');}
  function mark(root,re){
    var w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null),nodes=[],n;
    while((n=w.nextNode())){if(n.nodeValue.trim()&&!/^(SCRIPT|STYLE)$/.test(n.parentNode.nodeName))nodes.push(n);}
    var hits=0;
    nodes.forEach(function(t){
      var s=t.nodeValue,last=0,m,frag=null;re.lastIndex=0;
      while((m=re.exec(s))){
        if(m[0]===''){re.lastIndex++;continue;}
        frag=frag||document.createDocumentFragment();
        frag.appendChild(document.createTextNode(s.slice(last,m.index)));
        var k=document.createElement('mark');k.textContent=m[0];frag.appendChild(k);
        last=m.index+m[0].length;hits++;
      }
      if(frag){frag.appendChild(document.createTextNode(s.slice(last)));t.parentNode.replaceChild(frag,t);}
    });
    return hits;
  }
  function run(){
    clear();
    var terms=nk(q.value).split(/\s+/).filter(Boolean);
    if(!terms.length){secs.forEach(function(s){s.classList.remove('hide');});count.textContent='';none.style.display='none';return;}
    var shown=0,hits=0,re=new RegExp(terms.map(esc).join('|'),'gi');
    secs.forEach(function(s,i){
      var ok=terms.every(function(t){return texts[i].indexOf(t)>=0;});
      s.classList.toggle('hide',!ok);
      if(ok){shown++;hits+=mark(s,re);}
    });
    count.textContent=shown+' 節が該当'+(hits?'（強調 '+hits+' か所）':'');
    none.style.display=shown?'none':'block';
  }
  document.querySelector('nav.toc').addEventListener('click',function(e){
    if(e.target.closest('a')&&q.value){q.value='';run();}
  });
  var timer;
  q.addEventListener('input',function(){clearTimeout(timer);timer=setTimeout(run,80);});
  document.addEventListener('keydown',function(e){
    if(e.key==='/'&&document.activeElement!==q){e.preventDefault();q.focus();}
    if(e.key==='Escape'&&document.activeElement===q){q.value='';run();}
  });
})();
"""


def build(src, dst):
    text = Path(src).read_text(encoding="utf8")
    md = markdown.Markdown(extensions=["tables", "fenced_code", "toc", "sane_lists"],
                           extension_configs={"toc": {"toc_depth": "2-3"}})
    body = md.convert(text)
    m = re.search(r"<h1[^>]*>(.*?)</h1>", body, re.S)
    title = re.sub(r"<[^>]+>", "", m.group(1)).strip() if m else Path(src).stem
    body = body.replace("<table>", '<div class="tw"><table>').replace("</table>", "</table></div>")
    # h2 ごとに section で包む（検索の表示単位）。最初の h2 より前は前文として 1 節にする
    parts = re.split(r"(?=<h2[ >])", body)
    sections = "\n".join(f"<section>\n{p}\n</section>" for p in parts if p.strip())
    page = f"""<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head>
<body>
<header class="bar"><div class="in">
<input id="q" type="search" placeholder="検索（入力するたびに絞り込み。空白区切りで AND。/ でここへ移動）" aria-label="文書内検索" autocomplete="off">
<span id="count" aria-live="polite"></span>
</div></header>
<main>
<nav class="toc"><details><summary>目次</summary>{md.toc}</details></nav>
{sections}
<p id="none">該当する節がない。</p>
</main>
<script>{JS}</script>
</body>
</html>
"""
    Path(dst).write_text(page, encoding="utf8")
    print(f"{dst}: {len(page)} bytes, {len(parts)} sections")


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
