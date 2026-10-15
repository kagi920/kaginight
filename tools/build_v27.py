# v27 発見性（SEO／性能）: 字形サブセットの Web フォント、軽い OG 画像、構造化データ（WebSite / Person / MusicEvent）、preconnect。
# 見た目・言葉・振る舞いは変えない。hub（index.html）と BASE 差し込みの両方に掛ける。
# Usage: python3 -I tools/build_v27.py <hub_in> <hub_out> <insert_in> <insert_out>
import sys,pathlib,re,urllib.parse,json,datetime
hub_in,hub_out,ins_in,ins_out=sys.argv[1:5]
hub=pathlib.Path(hub_in).read_text(); ins=pathlib.Path(ins_in).read_text()
def rep(s,old,new,count=1):
    n=s.count(old); assert n==count,(old[:60],n); return s.replace(old,new)
# ---- font subset: every non-ASCII glyph used anywhere in either file + printable ASCII, so nothing falls back
glyphs=sorted(set(c for c in hub+ins if ord(c)>0x7f))+[chr(c) for c in range(0x20,0x7f)]
txt=urllib.parse.quote(''.join(glyphs),safe='')
OLD='https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=Noto+Serif+JP:wght@500;700&family=IBM+Plex+Mono:wght@400;500&display=swap'
LAT='https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600&family=IBM+Plex+Mono:wght@400;500&display=swap'
JP='https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@500;700&display=swap&text='+txt
# hub
hub=rep(hub,'<link rel="stylesheet" href="%s">'%OLD,
 '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link rel="stylesheet" href="%s">\n<link rel="stylesheet" href="%s">'%(LAT,JP))
hub=rep(hub,'<meta property="og:image" content="https://kagi920.github.io/kaginight/og.png">',
 '<meta property="og:image" content="https://kagi920.github.io/kaginight/og.jpg">\n<meta property="og:image:type" content="image/jpeg">\n<meta property="og:image:alt" content="KAGI NIGHT｜XR ドラマー 鍵山喬一">')
hub=rep(hub,'<meta name="twitter:image" content="https://kagi920.github.io/kaginight/og.png">',
 '<meta name="twitter:image" content="https://kagi920.github.io/kaginight/og.jpg">\n<meta name="twitter:image:alt" content="KAGI NIGHT｜XR ドラマー 鍵山喬一">')
# structured data: @graph with WebSite, Person (+image), MusicEvent (facts already on the page)
m=re.search(r'<script type="application/ld\+json">(.*?)</script>',hub,re.S); person=json.loads(m.group(1))
person['@id']='https://kagi920.github.io/kaginight/#person'; person['image']='https://kagi920.github.io/kaginight/og.jpg'
site={'@type':'WebSite','@id':'https://kagi920.github.io/kaginight/#website','url':'https://kagi920.github.io/kaginight/','name':'KAGI NIGHT','inLanguage':'ja','about':{'@id':person['@id']},'publisher':{'@id':person['@id']}}
ev={'@type':'MusicEvent','name':'KAGI NIGHT 2026 Vol.1「衝突の夜」','startDate':'2026-07-17','eventStatus':'https://schema.org/EventScheduled','eventAttendanceMode':'https://schema.org/MixedEventAttendanceMode',
 'location':{'@type':'Place','name':'unravel tokyo','address':{'@type':'PostalAddress','addressLocality':'六本木','addressRegion':'東京都','addressCountry':'JP'}},
 'performer':{'@id':person['@id']},'organizer':{'@id':person['@id']},'url':'https://kagi920.github.io/kaginight/#live','inLanguage':'ja'}
graph={'@context':'https://schema.org','@graph':[site,person,ev]}
hub=hub[:m.start()]+'<script type="application/ld+json">'+json.dumps(graph,ensure_ascii=False,separators=(',',':'))+'</script>'+hub[m.end():]
hub=rep(hub,'id="ver">v26<','id="ver">v27<')
pathlib.Path(hub_out).write_text(hub)
# BASE insert: the subset URL (about 3,200 chars) would push the theme over BASE's 150,000-character limit, so BASE keeps the standard font link.
ins=rep(ins,'id="kn-ver">v26<','id="kn-ver">v27<')
pathlib.Path(ins_out).write_text(ins)
# sitemap lastmod
sm=pathlib.Path(pathlib.Path(hub_out).parent/'sitemap.xml'); t=sm.read_text(); t=re.sub(r'<lastmod>[^<]*</lastmod>','<lastmod>%s</lastmod>'%datetime.date.today().isoformat(),t); sm.write_text(t)
print('built; glyphs',len(glyphs),'jp url len',len(JP))
