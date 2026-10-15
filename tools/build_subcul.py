import re,sys,pathlib
src=pathlib.Path('/home/user/kaginight/index.html').read_text()
out=src
def rep(old,new,count=1):
    global out
    n=out.count(old)
    assert n==count,(old[:60],n)
    out=out.replace(old,new)

# 0. preview: noindex, title
rep('<meta name="robots" content="index,follow,max-image-preview:large">','<meta name="robots" content="noindex,nofollow">')
# 1. fonts: add Shippori Mincho B1 (retro mincho) + DotGothic16 (bitmap)
rep('family=IBM+Plex+Mono:wght@400;500&display=swap','family=IBM+Plex+Mono:wght@400;500&family=Shippori+Mincho+B1:wght@700;800&family=DotGothic16&display=swap')
# 2. tokens: 60/30/10 → 30% = 朱 + retro type + screen tone. --mix is the layer strength (0..1), default .3
rep(':root{--bg:#07070b;--fg:#ece9e2;--muted:#9a9ea6;--rule:rgba(236,233,226,.14);--gold:#d9a84a;--red:#c8102e;--glass:rgba(12,12,18,.55);',
    ':root{--bg:#07070b;--fg:#ece9e2;--muted:#9a9ea6;--rule:rgba(236,233,226,.14);--gold:#d9a84a;--red:#c8102e;--glass:rgba(12,12,18,.55);--mix:.3;--sub:#e8432e;--sub-ink:#d7321f;--f-sub:"Shippori Mincho B1","Noto Serif JP",serif;--f-dot:"DotGothic16","IBM Plex Mono",monospace;')
# 3. CSS additions (appended before </style>): texture layers, seal, vertical strip, type swaps
css='''
/* ---- サブカル層（30%）: 網点と粒子はキャンバスにだけ掛かる（UI は上） */
.ui{z-index:2}
/* : 朱・レトロ明朝・ドット書体・網点・判子・縦書き。クラゲの形と動きは触らない ---- */
.tone{position:fixed;inset:0;pointer-events:none;z-index:1;background-image:radial-gradient(circle,rgba(255,236,220,.55) 0 .55px,transparent .95px);background-size:3px 3px;opacity:calc(var(--mix)*.42);mix-blend-mode:overlay}
.grain{position:fixed;inset:0;pointer-events:none;z-index:1;opacity:calc(var(--mix)*.22);background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='160' height='160'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1 0 0 0 0 .93 0 0 0 0 .86 0 0 0 .5 0'/></filter><rect width='160' height='160' filter='url(%23n)'/></svg>");background-size:160px 160px;mix-blend-mode:screen}
.mark{font-family:var(--f-sub);font-weight:800;letter-spacing:.12em}
.mark small{font-family:var(--f-sub);font-weight:700;color:var(--sub);letter-spacing:.3em}
.seal{position:absolute;left:22px;top:calc(120px + env(safe-area-inset-top,0px));width:46px;height:46px;border:2px solid var(--sub);border-radius:50%;color:var(--sub);font-family:var(--f-sub);font-weight:800;font-size:1.25rem;display:flex;align-items:center;justify-content:center;transform:rotate(-9deg);opacity:calc(.55 + var(--mix));pointer-events:none;box-shadow:inset 0 0 0 1px rgba(232,67,46,.35)}
.tate{position:absolute;right:16px;top:calc(96px + env(safe-area-inset-top,0px));writing-mode:vertical-rl;font-family:var(--f-sub);font-weight:700;font-size:.82rem;letter-spacing:.34em;color:var(--sub);opacity:calc(.5 + var(--mix));pointer-events:none;text-shadow:0 0 12px rgba(232,67,46,.35)}
.hint{top:calc(26px + env(safe-area-inset-top,0px));font-family:var(--f-dot);letter-spacing:.12em;font-size:.7rem}
.snd,.dial span,.ver{font-family:var(--f-dot);letter-spacing:.12em}
.snd{font-size:.72rem;border-radius:3px}
.snd[aria-pressed="true"]{border-color:var(--sub);color:var(--sub)}
.ver{font-size:.66rem;opacity:.75;color:var(--sub)}
.dock{border-radius:6px;border-color:rgba(232,67,46,.45)}
.dock button,.dock a{border-radius:3px}
.dock button[aria-expanded="true"]{background:var(--sub-ink);color:#fff}
.hit{border-color:var(--sub);background:radial-gradient(circle,rgba(232,67,46,.42),rgba(217,168,74,.05) 70%)}
.hit::after{background:#fff1e8}
.dial input{accent-color:var(--sub)}
.sheet{border-radius:4px 4px 0 0;border-top:3px solid var(--sub)}
.sheet h2{font-family:var(--f-sub);font-weight:800;letter-spacing:.14em}
.sheet h2 small{font-family:var(--f-sub);color:var(--sub);letter-spacing:.26em}
.meta b{color:var(--sub)}
.bar{background:var(--sub-ink);color:#fff;border:1px solid var(--sub-ink)}
.bar.ghost{background:transparent;color:var(--fg);border:1px solid var(--fg)}
.steps i{font-family:var(--f-sub);font-weight:800;color:var(--sub)}
.steps a{color:var(--sub);border-bottom-color:rgba(232,67,46,.5)}
@media (max-width:640px){.tate{font-size:.74rem;top:calc(90px + env(safe-area-inset-top,0px));right:12px}.seal{width:40px;height:40px;font-size:1.05rem}}
@media (max-width:380px){.tate{display:none}}
@media (prefers-reduced-motion: reduce){.tone,.grain{display:none}}
</style>'''
rep('@media (prefers-reduced-motion: reduce){.sheet{transition:none}}\n</style>','@media (prefers-reduced-motion: reduce){.sheet{transition:none}}'+css)
# 4. markup: texture layers + seal + vertical strip; version stamp
rep('<canvas id="gl"></canvas>','<canvas id="gl"></canvas>\n<div class="tone" aria-hidden="true"></div><div class="grain" aria-hidden="true"></div>')
rep('<div class="hint">DRAG · ROTATE<br>PINCH · ZOOM<br>TAP · HIT</div>','<div class="hint">DRAG · ROTATE<br>PINCH · ZOOM<br>TAP · HIT</div>\n  <div class="seal" aria-hidden="true">夜</div>\n  <div class="tate" aria-hidden="true">叩く人として参加できる夜</div>')
rep('<div class="ver" id="ver">v21</div>','<div class="ver" id="ver">v22 preview · 30%</div>')
# 5. composite shader: risograph two-ink (朱 + 墨) with 45° halftone and slight off-register, mixed in by uMix
rep("var compfs=['precision mediump float;varying vec2 vUv;uniform sampler2D uScene;uniform sampler2D uBloom;uniform float uStr;uniform vec3 uMask;',",
    "var compfs=['precision mediump float;varying vec2 vUv;uniform sampler2D uScene;uniform sampler2D uBloom;uniform float uStr;uniform vec3 uMask;uniform float uMix;uniform float uDprC;',")
rep("'void main(){vec3 s=texture2D(uScene,vUv).rgb;vec3 b=texture2D(uBloom,vUv).rgb;vec3 c=s+b*uStr*uMask;gl_FragColor=vec4(aces(c*1.0),1.0);}'].join('\\n');",
    "'void main(){vec3 s=texture2D(uScene,vUv).rgb;vec3 b=texture2D(uBloom,vUv).rgb;vec3 c=aces(s+b*uStr*uMask);',\n"
    "' /* サブカル層: リソグラフ風 2 色刷り（朱＋墨）、45 度の網点、版ずれ。uMix で混ぜる。形と動きは不変 */',\n"
    "' float l=dot(c,vec3(0.299,0.587,0.114));vec3 s2=texture2D(uScene,vUv+vec2(0.0035,0.0012)*uMix).rgb+texture2D(uBloom,vUv+vec2(0.0035,0.0012)*uMix).rgb*uStr*uMask;float l2=dot(aces(s2),vec3(0.299,0.587,0.114));',\n"
    "' vec3 sumi=vec3(0.03,0.02,0.035);vec3 shu=vec3(0.91,0.27,0.18);vec3 kami=vec3(0.99,0.95,0.87);',\n"
    "' vec2 p=gl_FragCoord.xy/(uDprC*4.5);vec2 g=fract(mat2(0.7071,-0.7071,0.7071,0.7071)*p)-0.5;float r=length(g);',\n"
    "' float dotA=smoothstep(0.52*sqrt(l2)+0.09,0.52*sqrt(l2)-0.09,r);float dotB=smoothstep(0.5*l*l+0.07,0.5*l*l-0.07,r);',\n"
    "' vec3 tone=mix(sumi,shu,dotA);tone=mix(tone,kami,dotB*smoothstep(0.45,0.95,l));',\n"
    "' gl_FragColor=vec4(mix(c,tone,uMix),1.0);}'].join('\\n');")
rep("uStr:gl.getUniformLocation(compp,'uStr'),uMask:gl.getUniformLocation(compp,'uMask'),a:gl.getAttribLocation(compp,'aXY')};",
    "uStr:gl.getUniformLocation(compp,'uStr'),uMask:gl.getUniformLocation(compp,'uMask'),uMix:gl.getUniformLocation(compp,'uMix'),uDprC:gl.getUniformLocation(compp,'uDprC'),a:gl.getAttribLocation(compp,'aXY')};")
rep("gl.uniform1f(CP.uStr,0.42);gl.uniform3f(CP.uMask,1.0-ch*0.5,1.0-ch*0.6,1.0);quad(compp,CP.a);",
    "gl.uniform1f(CP.uStr,0.42);gl.uniform3f(CP.uMask,1.0-ch*0.5,1.0-ch*0.6,1.0);gl.uniform1f(CP.uMix,window.KN_MIX||0.0);gl.uniform1f(CP.uDprC,dpr);quad(compp,CP.a);")
# 6. mix control from URL (?mix=0.3) → CSS var + shader uniform. Owner compares strengths by URL only.
rep("KN({ pre:'', stage:null, canvas:'gl' });",
    "(function(){var m=parseFloat(new URLSearchParams(location.search).get('mix'));if(!(m>=0&&m<=1))m=0.3;window.KN_MIX=m;document.documentElement.style.setProperty('--mix',m);var v=document.getElementById('ver');if(v)v.textContent='v22 preview · '+Math.round(m*100)+'%';})();\nKN({ pre:'', stage:null, canvas:'gl' });")
pathlib.Path('/home/user/kaginight/subcul').mkdir(exist_ok=True)
pathlib.Path('/home/user/kaginight/subcul/index.html').write_text(out)
print('ok',len(out))
