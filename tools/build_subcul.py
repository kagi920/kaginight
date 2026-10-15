# Direction C: art-pop subculture at 30% — Shiota-style red threads (web + thread medusae), red accent, light red grade.
# No new words. No Showa/underground poster devices. Hero jellyfish geometry, motion and sound untouched.
import pathlib,sys
src=pathlib.Path('/home/user/kaginight/index.html').read_text()
out=src
def rep(old,new,count=1):
    global out
    n=out.count(old); assert n==count,(old[:70],n); out=out.replace(old,new)
OUT=sys.argv[1] if len(sys.argv)>1 else '/home/user/kaginight/subcul/index.html'
rep('<meta name="robots" content="index,follow,max-image-preview:large">','<meta name="robots" content="noindex,nofollow">')
rep(':root{--bg:#07070b;--fg:#ece9e2;--muted:#9a9ea6;--rule:rgba(236,233,226,.14);--gold:#d9a84a;--red:#c8102e;--glass:rgba(12,12,18,.55);',
    ':root{--bg:#07070b;--fg:#ece9e2;--muted:#9a9ea6;--rule:rgba(236,233,226,.14);--gold:#d9a84a;--red:#c8102e;--glass:rgba(12,12,18,.55);--mix:.3;--sub:#e8432e;--sub-ink:#d7321f;')
css='''
/* ---- 赤い糸（塩田千春の参照）: 画面を渡る細い糸の網と結び目。UI の上には掛けない ---- */
.ui{z-index:2}
.web{position:fixed;inset:0;width:100%;height:100%;pointer-events:none;z-index:1;opacity:calc(var(--mix)*1.6)}
.web line{stroke:var(--sub);stroke-width:1;vector-effect:non-scaling-stroke;stroke-linecap:round}
.web circle{fill:var(--sub)}
.mark small{color:var(--sub)}
.snd[aria-pressed="true"]{border-color:var(--sub);color:var(--sub)}
.dock button[aria-expanded="true"]{background:var(--sub-ink);color:#fff}
.dial input{accent-color:var(--sub)}
.sheet{border-top:1px solid var(--sub)}
.sheet h2 small{color:var(--sub)}
.meta b{color:var(--sub)}
.bar{background:var(--sub-ink);color:#fff}
.bar.ghost{background:transparent;color:var(--fg);border:1px solid var(--fg)}
.steps i{color:var(--sub)}
.steps a{color:var(--sub);border-bottom-color:rgba(232,67,46,.5)}
.ver{color:var(--sub);opacity:.8}
@media (prefers-reduced-motion: reduce){.web{display:none}}
</style>'''
rep('@media (prefers-reduced-motion: reduce){.sheet{transition:none}}\n</style>','@media (prefers-reduced-motion: reduce){.sheet{transition:none}}'+css)
rep('<canvas id="gl"></canvas>','<canvas id="gl"></canvas>\n<svg class="web" id="web" aria-hidden="true"></svg>')
rep('<div class="ver" id="ver">v21</div>','<div class="ver" id="ver">v22 preview C · 30%</div>')
# --- vertex shader: thread mode (lines drawn in red, no point sprite)
rep("'varying vec3 vCol;varying float vAlpha;varying float vKind;',\n'float hash(float n){return fract(sin(n)*43758.5453);}',",
    "'varying vec3 vCol;varying float vAlpha;varying float vKind;varying float vThr;uniform float uThread;',\n'float hash(float n){return fract(sin(n)*43758.5453);}',")
rep("' float sz=aSize*uDpr*(2.6/dist)*(1.0+0.25*uCharge*body);if(k>2.5&&body<0.5)sz*=1.0+0.5*uHit;if(k>3.5&&k<4.5)sz*=1.0+0.8*pulse;gl_PointSize=sz;}'",
    "' vThr=uThread;if(uThread>0.5){vCol=vec3(0.96,0.14,0.12)*mix(1.0,1.5,uGlow);vAlpha=0.5*uDim*mix(0.25,1.0,fog)*mix(0.3,1.0,ie);}',\n"
    "' float sz=aSize*uDpr*(2.6/dist)*(1.0+0.25*uCharge*body);if(k>2.5&&body<0.5)sz*=1.0+0.5*uHit;if(k>3.5&&k<4.5)sz*=1.0+0.8*pulse;gl_PointSize=sz;}'")
# --- fragment shader: thread branch
rep("'#ifdef GL_FRAGMENT_PRECISION_HIGH','precision highp float;','#else','precision mediump float;','#endif','varying vec3 vCol;varying float vAlpha;varying float vKind;uniform float uTimeF;',\n'void main(){vec2 q=gl_PointCoord-0.5;float d=length(q);float a;',",
    "'#ifdef GL_FRAGMENT_PRECISION_HIGH','precision highp float;','#else','precision mediump float;','#endif','varying vec3 vCol;varying float vAlpha;varying float vKind;varying float vThr;uniform float uTimeF;',\n'void main(){if(vThr>0.5){gl_FragColor=vec4(vCol,vAlpha);return;}vec2 q=gl_PointCoord-0.5;float d=length(q);float a;',")
# --- uniforms list
rep("['uProj','uView','uTime','uTimeF','uPhase','uSplit','uHit','uDpr','uGlow','uIntro','uModel','uDim','uCharge']","['uProj','uView','uTime','uTimeF','uPhase','uSplit','uHit','uDpr','uGlow','uIntro','uModel','uDim','uCharge','uThread']")
# --- geometry offsets for line strips (tentacles are contiguous, ordered along the strand)
rep("var N=kind.length, NL=160+880+NPL, NB=N-NL;","var N=kind.length, NL=160+880+NPL, NB=N-NL;var OT=NS+NI, OA=NS+NI+TN*TL+MR;")
# --- thread medusae: every other non-hero (indices 1 and 3) swims as red thread
rep("for(var mi=0;mi<INST;mi++){var m={x:0,y:0,z:0,sc:1,off:0,seed:7,yaw:0,hero:mi===0,charge:0};if(mi>0)spawn(m,true);med.push(m);}",
    "for(var mi=0;mi<INST;mi++){var m={x:0,y:0,z:0,sc:1,off:0,seed:7,yaw:0,hero:mi===0,charge:0,thread:(mi===1||mi===3)};if(mi>0)spawn(m,true);med.push(m);}")
# --- draw: thread medusa = line strips (bell chords, 20 tentacle strands, 4 oral-arm ribbons) + dim points
rep("    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,mm.hero?1.0:0.55);gl.uniform1f(U.uCharge,mm.charge);\n    gl.uniform1f(U.uGlow,1.0);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);gl.drawArrays(gl.POINTS,0,NB);",
    "    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,mm.hero?1.0:0.55);gl.uniform1f(U.uCharge,mm.charge);\n"
    "    if(mm.thread&&window.KN_MIX>0.001){gl.uniform1f(U.uThread,1.0);gl.uniform1f(U.uGlow,1.0);gl.uniform1f(U.uDim,Math.min(1,window.KN_MIX*3.0));gl.blendFunc(gl.SRC_ALPHA,gl.ONE);\n"
    "      gl.drawArrays(gl.LINE_STRIP,0,420);for(var tk=0;tk<TN;tk++)gl.drawArrays(gl.LINE_STRIP,OT+tk*TL,TL);for(var ak=0;ak<4;ak++)gl.drawArrays(gl.LINE_STRIP,OA+ak*AR,160);\n"
    "      gl.uniform1f(U.uThread,0.0);gl.uniform1f(U.uDim,0.12);gl.uniform1f(U.uGlow,0.4);gl.drawArrays(gl.POINTS,0,NB);continue;}\n"
    "    gl.uniform1f(U.uGlow,1.0);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);gl.drawArrays(gl.POINTS,0,NB);")
# --- composite: light red grade (duotone without dots), mixed by uMix*0.6
rep("var compfs=['precision mediump float;varying vec2 vUv;uniform sampler2D uScene;uniform sampler2D uBloom;uniform float uStr;uniform vec3 uMask;',",
    "var compfs=['precision mediump float;varying vec2 vUv;uniform sampler2D uScene;uniform sampler2D uBloom;uniform float uStr;uniform vec3 uMask;uniform float uMix;',")
rep("'void main(){vec3 s=texture2D(uScene,vUv).rgb;vec3 b=texture2D(uBloom,vUv).rgb;vec3 c=s+b*uStr*uMask;gl_FragColor=vec4(aces(c*1.0),1.0);}'].join('\\n');",
    "'void main(){vec3 s=texture2D(uScene,vUv).rgb;vec3 b=texture2D(uBloom,vUv).rgb;vec3 c=aces(s+b*uStr*uMask);',\n"
    "' /* 赤の階調（網点なし）: 影を赤黒へ、中間を朱へ寄せる。uMix*0.6 で混ぜる */',\n"
    "' float l=dot(c,vec3(0.299,0.587,0.114));vec3 tone=mix(vec3(0.04,0.02,0.035),vec3(0.93,0.26,0.18),smoothstep(0.0,0.62,l));tone=mix(tone,vec3(0.99,0.95,0.88),smoothstep(0.62,1.0,l));',\n"
    "' gl_FragColor=vec4(mix(c,tone,uMix*0.6),1.0);}'].join('\\n');")
rep("uStr:gl.getUniformLocation(compp,'uStr'),uMask:gl.getUniformLocation(compp,'uMask'),a:gl.getAttribLocation(compp,'aXY')};",
    "uStr:gl.getUniformLocation(compp,'uStr'),uMask:gl.getUniformLocation(compp,'uMask'),uMix:gl.getUniformLocation(compp,'uMix'),a:gl.getAttribLocation(compp,'aXY')};")
rep("gl.uniform1f(CP.uStr,0.42);gl.uniform3f(CP.uMask,1.0-ch*0.5,1.0-ch*0.6,1.0);quad(compp,CP.a);",
    "gl.uniform1f(CP.uStr,0.42);gl.uniform3f(CP.uMask,1.0-ch*0.5,1.0-ch*0.6,1.0);gl.uniform1f(CP.uMix,window.KN_MIX||0.0);quad(compp,CP.a);")
# --- mix from URL + red-thread web (seeded, redrawn on resize)
rep("KN({ pre:'', stage:null, canvas:'gl' });",
    """(function(){var m=parseFloat(new URLSearchParams(location.search).get('mix'));if(!(m>=0&&m<=1))m=0.3;window.KN_MIX=m;document.documentElement.style.setProperty('--mix',m);var v=document.getElementById('ver');if(v)v.textContent='v22 preview C · '+Math.round(m*100)+'%';
/* 赤い糸の網: 画面の縁から中央付近へ渡る糸。線の数は mix に比例（0.3 で 22 本）。結び目は糸の上に 3 つ */
var svg=document.getElementById('web');if(!svg)return;var sd=7;function r(){sd=(sd*9301+49297)%233280;return sd/233280;}
function draw(){var W=innerWidth,H=innerHeight;svg.setAttribute('viewBox','0 0 '+W+' '+H);var n=Math.round(m*74),s='';sd=7;
  function edge(){var e=r();return e<0.25?[r()*W,0]:e<0.5?[W,r()*H]:e<0.75?[r()*W,H]:[0,r()*H];}
  for(var i=0;i<n;i++){var a=edge(),b=(r()<0.55)?edge():[W*(0.5+(r()-0.5)*0.5),H*(0.52+(r()-0.5)*0.4)];s+='<line x1="'+a[0].toFixed(0)+'" y1="'+a[1].toFixed(0)+'" x2="'+b[0].toFixed(0)+'" y2="'+b[1].toFixed(0)+'" stroke-opacity="'+(0.25+r()*0.35).toFixed(2)+'"/>';
    if(i%7===3){var t=0.3+r()*0.4;s+='<circle cx="'+(a[0]+(b[0]-a[0])*t).toFixed(0)+'" cy="'+(a[1]+(b[1]-a[1])*t).toFixed(0)+'" r="'+(2+r()*2).toFixed(1)+'"/>';}}
  svg.innerHTML=s;}
draw();addEventListener('resize',draw);})();
KN({ pre:'', stage:null, canvas:'gl' });""")
pathlib.Path(OUT).parent.mkdir(exist_ok=True,parents=True)
pathlib.Path(OUT).write_text(out)
print('ok',len(out))
