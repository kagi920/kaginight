# v28: 本文（KAGI NIGHT の説明 約 300 字）を LIVE の扉に、計測の受け口（Search Console タグの枠、GoatCounter／Cloudflare の差し替え表）、
# PROFILE に「X の最新の投稿」バー（差し替え表に URL を入れた時だけ出る）。見た目・既存の言葉・振る舞いは不変。hub と BASE 差し込みの両方。
# Usage: python3 -I tools/build_v28.py <hub_in> <hub_out> <insert_in> <insert_out>
import sys,pathlib,re,datetime
ABOUT=['KAGI NIGHT は、XR ドラマー 鍵山喬一が企画する夜。鍵山が実際に叩いた一打が、そのまま光と空間と人の動きになる。',
 '配信からは、スマホか PC のブラウザで参加する。現地では、会場で QR を読んで参加する。どちらも、見るだけでなく、叩く人として参加できる。',
 'これまでに、KAGI NIGHT 2022（渋谷 B.Y.G）、KAGI NIGHT 2026 Vol.1「衝突の夜」（六本木 unravel tokyo）を開催。',
 '鍵山喬一は埼玉県出身。1998 年ごろから都内のライブハウスで叩きはじめ、cocobat、JUDGEMENT、アーバンギャルドを経て、多くのアーティストのサポートドラマーとして活動している。']
def apply(src,pre):
    out=src
    def rep(old,new,count=1):
        nonlocal out
        n=out.count(old); assert n==count,(pre,old[:70],n); return_=out.replace(old,new); out=return_
    p=pre; semi=';' if pre else ''
    rep('id="%sver">v27<'%p,'id="%sver">v28<'%p)
    # about block CSS
    rm='@media (prefers-reduced-motion: reduce){.%ssheet{transition:none%s}}'%(p,semi)
    rep(rm,rm+'\n.%sabout{margin:1rem 0 0;padding-top:.8rem;border-top:1px solid var(--%srule);font-family:"Noto Sans JP",var(--%s);font-size:.84rem;line-height:1.9%s}\n.%sabout p{margin:0 0 .6rem%s}'%(p, 'kn-' if p else '', 'kn-jp' if p else 'f-jp', semi, p, semi))
    about='<div class="%sabout">'%p+''.join('<p>%s</p>'%t for t in ABOUT)+'</div>'
    rep('タップで参加する。</span></li><li><i>4</i><span>結果と録画を持ち帰る。</span></li></ol>',
        'タップで参加する。</span></li><li><i>4</i><span>結果と録画を持ち帰る。</span></li></ol>\n    '+about)
    # latest-post bar in PROFILE (hidden until LINKS.latest is set)
    rep('<a class="%sbar %sghost" href="https://www.instagram.com/kagi03/" target="_blank" rel="me noopener">Instagram（@kagi03）<span>›</span></a>'%(p,p),
        '<a class="%sbar %sghost" href="https://www.instagram.com/kagi03/" target="_blank" rel="me noopener">Instagram（@kagi03）<span>›</span></a>\n    <a class="%sbar %sghost" id="%slnk-latest" href="https://x.com/KAGI920" target="_blank" rel="noopener" hidden>X の最新の投稿<span>›</span></a>'%(p,p,p,p,p))
    # swap table: measurement + latest
    m=re.search(r"(const|var) (KN_)?LINKS=\{\n",out); assert m,(pre,'LINKS')
    out=out[:m.end()]+"  latest:'',   // X の最新の投稿の URL（入れると PROFILE に「X の最新の投稿」が出る。毎週差し替える）\n  goat:'',     // GoatCounter のコード（例 'kaginight'）。入れると訪問計測が動く\n  cf:'',       // Cloudflare Web Analytics の token。入れると訪問計測が動く\n"+out[m.end():]
    L='KN_LINKS' if p else 'LINKS'
    rep("set('%slnk-ks',%s.ks);"%(p,L),
        "set('%slnk-ks',%s.ks);"%(p,L)+"if(%s.latest){const la=document.getElementById('%slnk-latest');if(la){la.href=%s.latest;la.hidden=false;}}"%(L,p,L)+
        "if(%s.goat){const g=document.createElement('script');g.async=true;g.src='https://gc.zgo.at/count.js';g.setAttribute('data-goatcounter','https://'+%s.goat+'.goatcounter.com/count');document.head.appendChild(g);}"%(L,L)+
        "if(%s.cf){const c=document.createElement('script');c.defer=true;c.src='https://static.cloudflareinsights.com/beacon.min.js';c.setAttribute('data-cf-beacon',JSON.stringify({token:%s.cf}));document.head.appendChild(c);}"%(L,L))
    return out
hub_in,hub_out,ins_in,ins_out=sys.argv[1:5]
hub=apply(pathlib.Path(hub_in).read_text(),'')
hub=hub.replace('<link rel="canonical" href="https://kagi920.github.io/kaginight/">','<link rel="canonical" href="https://kagi920.github.io/kaginight/">\n<!-- Search Console の所有権確認: 鍵山が受け取った <meta name="google-site-verification" content="…"> をこの行の下に貼る -->',1)
pathlib.Path(hub_out).write_text(hub)
pathlib.Path(ins_out).write_text(apply(pathlib.Path(ins_in).read_text(),'kn-'))
sm=pathlib.Path(hub_out).parent/'sitemap.xml'; t=sm.read_text(); sm.write_text(re.sub(r'<lastmod>[^<]*</lastmod>','<lastmod>%s</lastmod>'%datetime.date.today().isoformat(),t))
print('built; about chars',sum(len(t) for t in ABOUT))
