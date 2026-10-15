# v24「三つ叩くと夜が変わる」: 3 taps on the key → the night holds its breath, then turns into the サブカル 120% skin
# (red threads, hanging door keys, thread medusae, red grade). 3 taps again → back. Plus the one-minute absence (v22).
# Hero geometry/colour/sound untouched. Same replacements for the hub ('' prefix) and the BASE insert ('kn-' prefix).
# Usage: python3 -I tools/build_v24.py <hub_in> <hub_out> <insert_in> <insert_out>
import re,sys,pathlib
LABEL='v24'
def apply(src,pre):
    out=src
    def rep(old,new,count=1):
        nonlocal out
        n=out.count(old); assert n==count,(pre,old[:70],n); out=out.replace(old,new)
    p=pre; semi=';' if pre else ''; pos='absolute' if pre else 'fixed'
    rep('id="%sver">v21<'%p,'id="%sver">%s<'%(p,LABEL))
    rm='@media (prefers-reduced-motion: reduce){.%ssheet{transition:none%s}}'%(p,semi)
    css=rm+'''
/* ---- 三つ叩くと夜が変わる: スキン（赤い糸・吊るした鍵）。html.skin のときだけ効く。主役には掛けない ---- */
html.known .{p}hit{box-shadow:0 0 0 6px rgba(7,7,11,.65),0 0 0 7px rgba(217,168,74,.6);}
.{p}ui{z-index:2;}
.{p}web{position:{pos};inset:0;width:100%;height:100%;pointer-events:none;z-index:1;opacity:0;transition:opacity 2.4s ease;}
html.skin .{p}web{opacity:1;}
.{p}web line{stroke:#e8432e;stroke-width:1.3;vector-effect:non-scaling-stroke;stroke-linecap:round;}
.{p}web circle{fill:#e8432e;}
.{p}web .key{fill:none;stroke:#d9a84a;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;transform-box:fill-box;transform-origin:50% 0;animation:knsway 4.2s ease-in-out infinite alternate;}
.{p}web .key.b{stroke:#fff1e8;stroke-width:1.6;}
.{p}web .hang{stroke:#e8432e;stroke-width:1;}
@keyframes knsway{from{transform:rotate(-6deg);}to{transform:rotate(6deg);}}
html.skin .{p}mark small,html.skin .{p}ver,html.skin .{p}sheet h2 small,html.skin .{p}meta b,html.skin .{p}steps i{color:#e8432e;}
html.skin .{p}sheet{border-top:1px solid #e8432e;}
html.skin .{p}bar{background:#d7321f;color:#fff !important;}
html.skin .{p}bar.{p}ghost{background:transparent;color:#ece9e2 !important;}
html.skin .{p}dock button[aria-expanded="true"]{background:#d7321f;color:#fff;}
html.skin .{p}snd[aria-pressed="true"]{border-color:#e8432e;color:#e8432e;}
html.skin .{p}dial input{accent-color:#e8432e;}
@media (prefers-reduced-motion: reduce){.{p}web{display:none;}.{p}web .key{animation:none;}}'''.replace('{p}',p).replace('{pos}',pos)
    rep(rm,css)
    rep('<canvas id="%sgl"></canvas>'%p,'<canvas id="%sgl"></canvas>\n<svg class="%sweb" id="%sweb" aria-hidden="true"></svg>'%(p,p,p))
    # ---- engine: thread mode for lines
    rep("'varying vec3 vCol;varying float vAlpha;varying float vKind;',","'varying vec3 vCol;varying float vAlpha;varying float vKind;varying float vThr;uniform float uThread;',")
    rep("' float sz=aSize*uDpr*(2.6/dist)*(1.0+0.25*uCharge*body);if(k>2.5&&body<0.5)sz*=1.0+0.5*uHit;if(k>3.5&&k<4.5)sz*=1.0+0.8*pulse;gl_PointSize=sz;}'",
        "' vThr=uThread;if(uThread>0.5){vCol=vec3(0.96,0.14,0.12)*mix(1.0,1.5,uGlow);vAlpha=0.5*uDim*mix(0.25,1.0,fog)*mix(0.3,1.0,ie);}',\n' float sz=aSize*uDpr*(2.6/dist)*(1.0+0.25*uCharge*body);if(k>2.5&&body<0.5)sz*=1.0+0.5*uHit;if(k>3.5&&k<4.5)sz*=1.0+0.8*pulse;gl_PointSize=sz;}'")
    rep("'varying vec3 vCol;varying float vAlpha;varying float vKind;uniform float uTimeF;',","'varying vec3 vCol;varying float vAlpha;varying float vKind;varying float vThr;uniform float uTimeF;',")
    rep("'void main(){vec2 q=gl_PointCoord-0.5;float d=length(q);float a;',","'void main(){if(vThr>0.5){gl_FragColor=vec4(vCol,vAlpha);return;}vec2 q=gl_PointCoord-0.5;float d=length(q);float a;',")
    rep("['uProj','uView','uTime','uTimeF','uPhase','uSplit','uHit','uDpr','uGlow','uIntro','uModel','uDim','uCharge']","['uProj','uView','uTime','uTimeF','uPhase','uSplit','uHit','uDpr','uGlow','uIntro','uModel','uDim','uCharge','uThread']")
    rep("var N=kind.length, NL=160+880+NPL, NB=N-NL;","var N=kind.length, NL=160+880+NPL, NB=N-NL;var OT=NS+NI, OA=NS+NI+TN*TL+MR;")
    # ---- composite: red grade on the dark water only
    rep("var compfs=['precision mediump float;varying vec2 vUv;uniform sampler2D uScene;uniform sampler2D uBloom;uniform float uStr;uniform vec3 uMask;',",
        "var compfs=['precision mediump float;varying vec2 vUv;uniform sampler2D uScene;uniform sampler2D uBloom;uniform float uStr;uniform vec3 uMask;uniform float uMix;',")
    rep("'void main(){vec3 s=texture2D(uScene,vUv).rgb;vec3 b=texture2D(uBloom,vUv).rgb;vec3 c=s+b*uStr*uMask;gl_FragColor=vec4(aces(c*1.0),1.0);}'].join('\\n');",
        "'void main(){vec3 s=texture2D(uScene,vUv).rgb;vec3 b=texture2D(uBloom,vUv).rgb;vec3 c=aces(s+b*uStr*uMask);',\n' float l=dot(c,vec3(0.299,0.587,0.114));vec3 tone=mix(vec3(0.04,0.02,0.035),vec3(0.93,0.26,0.18),smoothstep(0.0,0.62,l));tone=mix(tone,vec3(0.99,0.95,0.88),smoothstep(0.62,1.0,l));',\n' float keep=1.0-smoothstep(0.22,0.55,l);gl_FragColor=vec4(mix(c,tone,uMix*0.7*keep),1.0);}'].join('\\n');")
    rep("uStr:gl.getUniformLocation(compp,'uStr'),uMask:gl.getUniformLocation(compp,'uMask'),a:gl.getAttribLocation(compp,'aXY')};",
        "uStr:gl.getUniformLocation(compp,'uStr'),uMask:gl.getUniformLocation(compp,'uMask'),uMix:gl.getUniformLocation(compp,'uMix'),a:gl.getAttribLocation(compp,'aXY')};")
    rep("gl.uniform1f(CP.uStr,0.42);gl.uniform3f(CP.uMask,1.0-ch*0.5,1.0-ch*0.6,1.0);quad(compp,CP.a);",
        "gl.uniform1f(CP.uStr,0.42);gl.uniform3f(CP.uMask,1.0-ch*0.5,1.0-ch*0.6,1.0);gl.uniform1f(CP.uMix,window.KN_MIX||0.0);quad(compp,CP.a);")
    # ---- state: absence (v22), 3-tap knock, breath, skin toggle
    rep("var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;",
        "var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;\n"
        "/* 一分の不在: 90 秒見た人にだけ一度、主役が塵に解けて消え、戻る */\n"
        "var gone=0,goneT=-1,goneDone=false,seenT=0,GONE_AFTER=(function(){var g=parseFloat(new URLSearchParams(location.search).get('gone'));return g>0?g:90;})();\n"
        "/* 合図: 金の鍵を 3 回続けて叩く（間隔 140〜900 ms、ほぼ均等）。夜が息を止め、スキンが切り替わる */\n"
        "var taps=[];function knock(now){taps.push(now);if(taps.length>3)taps.shift();if(taps.length<3)return false;var a=taps[1]-taps[0],b=taps[2]-taps[1];if(a<140||a>900||b<140||b>900)return false;var r=a/b;if(r<0.5||r>2.0)return false;taps=[];return true;}\n"
        "var ansT=-1,breath=0;function answer(){ansT=performance.now();document.documentElement.classList.add('known');try{localStorage.setItem('kn_known','1');}catch(e){}}\n"
        "function answerNow(){var ph0=(2.1*0.2)%1;for(var i=0;i<med.length;i++){var m=med[i];m.off=((ph0-simT*0.2)%1+1)%1;m.charge=1;}simT=2.1;lastCycle=Math.floor(simT*0.2-0.875);lensV+=7.0;echoA=1;hit=1;if(window.KN_AUDIO){KN_AUDIO.kick();KN_AUDIO.hit();}if(window.KN_SKIN)KN_SKIN.toggle();}\n"
        "try{if(localStorage.getItem('kn_known'))document.documentElement.classList.add('known');}catch(e){}\n"
        "window.KN_TEST={knock:function(ts){taps=[];var r=false;for(var i=0;i<ts.length;i++)r=knock(ts[i])||r;return r;},gone:function(){return gone;},taps:function(){return taps.length;},breath:function(){return breath;}};")
    rep("function strike(){hit=1;simT=2.1;med[0].charge=1;lensV+=3.2;echoA=1;if(window.KN_AUDIO)KN_AUDIO.hit();lastCycle=Math.floor(simT*0.2-0.875);}",
        "function strike(){if(gone>0.5||ansT>=0)return;hit=1;simT=2.1;med[0].charge=1;lensV+=3.2;echoA=1;if(window.KN_AUDIO)KN_AUDIO.hit();lastCycle=Math.floor(simT*0.2-0.875);if(knock(performance.now()))answer();}")
    rep("intro=reduce?1:Math.min(1,(now-introT0)/3400);if(intro>=1&&!introDone){introDone=true;strike();}",
        "intro=reduce?1:Math.min(1,(now-introT0)/3400);if(intro>=1&&!introDone){introDone=true;strike();}\n"
        "  if(visible&&introDone&&!reduce)seenT+=dt;if(!goneDone&&goneT<0&&seenT>GONE_AFTER){goneT=now;}\n"
        "  if(goneT>=0){var ge=(now-goneT)/1000;if(ge<2.5)gone=ge/2.5;else if(ge<30.5)gone=1;else if(ge<33.9)gone=1-(ge-30.5)/3.4;else{gone=0;goneT=-1;goneDone=true;strike();}}\n"
        "  if(ansT>=0){var ae=(now-ansT)/1000;if(ae<0.55){breath=Math.max(0,Math.min(1,ae/0.12));}else{breath=0;ansT=-1;answerNow();}}else{breath=0;}")
    rep("if(m.hero){var cyc=Math.floor(simT*0.2-0.875);if(cyc>lastCycle){lastCycle=cyc;if(window.KN_AUDIO)KN_AUDIO.kick();}}",
        "if(m.hero){var cyc=Math.floor(simT*0.2-0.875);if(cyc>lastCycle){lastCycle=cyc;if(window.KN_AUDIO&&gone<0.5&&ansT<0)KN_AUDIO.kick();}}")
    rep("for(var mi=0;mi<INST;mi++){var m={x:0,y:0,z:0,sc:1,off:0,seed:7,yaw:0,hero:mi===0,charge:0};if(mi>0)spawn(m,true);med.push(m);}",
        "for(var mi=0;mi<INST;mi++){var m={x:0,y:0,z:0,sc:1,off:0,seed:7,yaw:0,hero:mi===0,charge:0,thread:false};if(mi>0)spawn(m,true);med.push(m);}")
    rep("if(mm.hero&&echoA>0.02&&tier===0){","if(mm.hero&&echoA>0.02&&tier===0&&gone<0.01){")
    rep("    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,mm.hero?1.0:0.55);gl.uniform1f(U.uCharge,mm.charge);\n    gl.uniform1f(U.uGlow,1.0);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);gl.drawArrays(gl.POINTS,0,NB);",
        "    gl.uniform1f(U.uIntro,mm.hero?Math.min(intro,1-gone):intro);\n"
        "    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,(mm.hero?1.0:0.55)*(1.0-0.88*breath));gl.uniform1f(U.uCharge,mm.charge);\n"
        "    if(!mm.hero&&window.KN_MIX>0.05){gl.uniform1f(U.uThread,1.0);gl.uniform1f(U.uGlow,1.0);gl.uniform1f(U.uDim,Math.min(1,window.KN_MIX)*(1.0-0.88*breath));gl.blendFunc(gl.SRC_ALPHA,gl.ONE);\n"
        "      gl.drawArrays(gl.LINE_STRIP,0,420);for(var tk=0;tk<TN;tk++)gl.drawArrays(gl.LINE_STRIP,OT+tk*TL,TL);for(var ak=0;ak<4;ak++)gl.drawArrays(gl.LINE_STRIP,OA+ak*AR,160);\n"
        "      gl.uniform1f(U.uThread,0.0);gl.uniform1f(U.uDim,0.55*(1.0-Math.min(1,window.KN_MIX))*(1.0-0.88*breath)+0.06);gl.uniform1f(U.uGlow,0.4);gl.drawArrays(gl.POINTS,0,NB);continue;}\n"
        "    gl.uniform1f(U.uGlow,1.0);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);gl.drawArrays(gl.POINTS,0,NB);")
    # ---- skin controller + red-thread web with door keys (outside the engine, prefix baked in)
    kn_call="KN({ pre:'%s', stage:%s, canvas:'%sgl' });"%(p,("'kn-stage'" if p else 'null'),p)
    ctrl=r"""(function(){
/* スキン制御: KN_SKIN.toggle() で 120%% と 0 を切り替える。?skin=on で最初からオン。 */
var LEVEL=1.2,cur=0,target=(/[?&]skin=on/.test(location.search))?LEVEL:0,lastTick=performance.now();window.KN_MIX=0;window.KN_OVER=0;
var ver=document.getElementById('%(p)sver'),root=document.documentElement,base=ver?ver.textContent:'';
setInterval(function(){var nw=performance.now(),dt=Math.min(0.5,(nw-lastTick)/1000);lastTick=nw;cur+=(target-cur)*(1-Math.exp(-dt/1.2));if(Math.abs(target-cur)<0.004)cur=target;window.KN_MIX=Math.min(1,cur);window.KN_OVER=Math.max(0,cur-1);var on=target>0;if(on!==root.classList.contains('skin'))root.classList.toggle('skin',on);if(ver)ver.textContent=on?base+' · 120%%':base;},50);
window.KN_SKIN={on:function(){return target>0;},set:function(v){target=v?LEVEL:0;},toggle:function(){target=target>0?0:LEVEL;}};
/* 赤い糸の網と、糸から吊るしたドアの鍵（鍵山のアイコン） */
var svg=document.getElementById('%(p)sweb');if(!svg)return;var sd=7;function r(){sd=(sd*9301+49297)%%233280;return sd/233280;}
var KEY='M0 0a6 6 0 1 0 0.01 0M0 6v30M0 26h7M0 32h5M0 36h8';
function draw(){var W=svg.clientWidth||innerWidth,H=svg.clientHeight||innerHeight;svg.setAttribute('viewBox','0 0 '+W+' '+H);var n=Math.round(LEVEL*62),s='',knots=[];sd=7;
  function edge(){var e=r();return e<0.25?[r()*W,0]:e<0.5?[W,r()*H]:e<0.75?[r()*W,H]:[0,r()*H];}
  for(var i=0;i<n;i++){var a=edge(),b=(r()<0.55)?edge():[W*(0.5+(r()-0.5)*0.5),H*(0.52+(r()-0.5)*0.4)];s+='<line x1="'+a[0].toFixed(0)+'" y1="'+a[1].toFixed(0)+'" x2="'+b[0].toFixed(0)+'" y2="'+b[1].toFixed(0)+'" stroke-opacity="'+(0.3+r()*0.4).toFixed(2)+'"/>';
    if(i%%6===2){var t=0.25+r()*0.5;knots.push([a[0]+(b[0]-a[0])*t,a[1]+(b[1]-a[1])*t]);}}
  for(var k=0;k<knots.length;k++){var kx=knots[k][0],ky=knots[k][1];if(ky>H*0.78||ky<H*0.08||kx<W*0.06||kx>W*0.94)continue;var len=18+r()*40,sc=(0.8+r()*0.6)*(W<640?0.85:1);
    s+='<circle cx="'+kx.toFixed(0)+'" cy="'+ky.toFixed(0)+'" r="2.4"/><line class="hang" x1="'+kx.toFixed(0)+'" y1="'+ky.toFixed(0)+'" x2="'+kx.toFixed(0)+'" y2="'+(ky+len).toFixed(0)+'"/>';
    s+='<g transform="translate('+kx.toFixed(0)+' '+(ky+len).toFixed(0)+') scale('+sc.toFixed(2)+')"><g class="key'+(k%%3===1?' b':'')+'" style="animation-delay:-'+(r()*4).toFixed(1)+'s"><path d="'+KEY+'"/></g></g>';}
  svg.innerHTML=s;}
draw();addEventListener('resize',draw);})();
""" % {'p':p}
    rep(kn_call,ctrl+kn_call)
    return out
hub_in,hub_out,ins_in,ins_out=sys.argv[1:5]
pathlib.Path(hub_out).write_text(apply(pathlib.Path(hub_in).read_text(),''))
pathlib.Path(ins_out).write_text(apply(pathlib.Path(ins_in).read_text(),'kn-'))
print('built')
