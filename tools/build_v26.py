# v26「クラゲが変わる」(3 taps each: 赤い糸 → 緑の糸の鍵 → 塵 → 元)
# v25「クラゲが変わる」: 3 taps on the key → the night holds its breath → the HERO MEDUSA is re-made of another matter.
#   state 1: 糸のクラゲ — the same bell/tentacles/arms re-woven as thread (line strips in the medusa's own colours)
#   state 2: 鍵のクラゲ — every point becomes a small door key (SDF sprite), the medusa's own colours
#   state 0: back. Nothing is pasted on the screen. No new colours. The flock, the UI, the sound are unchanged.
# Plus the one-minute absence (v22). Same replacements for the hub ('' prefix) and the BASE insert ('kn-' prefix).
# Usage: python3 -I tools/build_v25.py <hub_in> <hub_out> <insert_in> <insert_out>
import sys,pathlib
LABEL='v26'
def apply(src,pre):
    out=src
    def rep(old,new,count=1):
        nonlocal out
        n=out.count(old); assert n==count,(pre,old[:70],n); out=out.replace(old,new)
    p=pre; semi=';' if pre else ''
    rep('id="%sver">v21<'%p,'id="%sver">%s<'%(p,LABEL))
    rm='@media (prefers-reduced-motion: reduce){.%ssheet{transition:none%s}}'%(p,semi)
    rep(rm,rm+'\nhtml.known .%shit{box-shadow:0 0 0 6px rgba(7,7,11,.65),0 0 0 7px rgba(217,168,74,.6)%s}'%(p,semi))
    rep("'varying vec3 vCol;varying float vAlpha;varying float vKind;',","'varying vec3 vCol;varying float vAlpha;varying float vKind;varying float vThr;varying float vH;uniform float uThread;uniform float uKey;',")
    rep("' float sz=aSize*uDpr*(2.6/dist)*(1.0+0.25*uCharge*body);if(k>2.5&&body<0.5)sz*=1.0+0.5*uHit;if(k>3.5&&k<4.5)sz*=1.0+0.8*pulse;gl_PointSize=sz;}'",
        "' vThr=uThread;vH=h1;if(uThread>0.5){vCol=vec3(0.95,0.12,0.16)*mix(1.0,1.45,uGlow);vAlpha=0.46*uDim*mix(0.25,1.0,fog)*mix(0.3,1.0,ie);}',\n"
        "' float sz=aSize*uDpr*(2.6/dist)*(1.0+0.25*uCharge*body);if(k>2.5&&body<0.5)sz*=1.0+0.5*uHit;if(k>3.5&&k<4.5)sz*=1.0+0.8*pulse;if(uKey>0.5&&body>0.5){sz*=4.6;vAlpha*=0.5;}gl_PointSize=sz;}'")
    rep("'varying vec3 vCol;varying float vAlpha;varying float vKind;uniform float uTimeF;',","'varying vec3 vCol;varying float vAlpha;varying float vKind;varying float vThr;varying float vH;uniform float uTimeF;uniform float uKeyF;',")
    rep("'void main(){vec2 q=gl_PointCoord-0.5;float d=length(q);float a;',",
        "'void main(){if(vThr>0.5){gl_FragColor=vec4(vCol,vAlpha);return;}vec2 q=gl_PointCoord-0.5;float d=length(q);float a;',\n"
        "' if(uKeyF>0.5&&(vKind<2.5||(vKind>4.5&&vKind<8.5))){float an=(vH-0.5)*0.9+0.12*sin(uTimeF*1.3+vH*12.0);float cs=cos(an),sn=sin(an);vec2 r=vec2(cs*q.x-sn*q.y,sn*q.x+cs*q.y);',\n"
        "'   r.x+=0.014*sin(r.y*38.0+vH*21.0);float ring=1.0-smoothstep(0.016,0.036,abs(length(r-vec2(0.0,-0.27))-0.15));float shaft=(1.0-smoothstep(0.014,0.032,abs(r.x)))*step(-0.14,r.y)*step(r.y,0.46);',\n"
        "'   float bit1=(1.0-smoothstep(0.012,0.028,abs(r.y-0.29)))*step(0.0,r.x)*step(r.x,0.17);float bit2=(1.0-smoothstep(0.012,0.028,abs(r.y-0.41)))*step(0.0,r.x)*step(r.x,0.13);',\n"
        "'   a=max(max(ring,shaft),max(bit1,bit2));if(a<0.02)discard;gl_FragColor=vec4(vec3(0.42,1.0,0.58)*1.1,a*vAlpha);return;}',")
    rep("['uProj','uView','uTime','uTimeF','uPhase','uSplit','uHit','uDpr','uGlow','uIntro','uModel','uDim','uCharge']","['uProj','uView','uTime','uTimeF','uPhase','uSplit','uHit','uDpr','uGlow','uIntro','uModel','uDim','uCharge','uThread','uKey','uKeyF']")
    rep("var N=kind.length, NL=160+880+NPL, NB=N-NL;","var N=kind.length, NL=160+880+NPL, NB=N-NL;var OT=NS+NI, OA=NS+NI+TN*TL+MR;")
    rep("var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;",
        "var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;\n"
        "/* 一分の不在: 90 秒見た人にだけ一度、主役が塵に解けて消え、戻る */\n"
        "var gone=0,goneT=-1,goneDone=false,seenT=0,GONE_AFTER=(function(){var g=parseFloat(new URLSearchParams(location.search).get('gone'));return g>0?g:90;})();\n"
        "/* 合図: 金の鍵を 3 回続けて叩く（間隔 140〜900 ms、ほぼ均等）。夜が息を止め、主役の素材が変わる: 0 元 → 1 赤い糸 → 2 緑の糸の鍵 → 3 塵 → 0 */\n"
        "var taps=[];function knock(now){taps.push(now);if(taps.length>3)taps.shift();if(taps.length<3)return false;var a=taps[1]-taps[0],b=taps[2]-taps[1];if(a<140||a>900||b<140||b>900)return false;var r=a/b;if(r<0.5||r>2.0)return false;taps=[];return true;}\n"
        "var MAT=(function(){var s=new URLSearchParams(location.search).get('mat');return s==='thread'?1:s==='key'?2:s==='dust'?3:0;})(),matT=0,dustT=0,ansT=-1,breath=0;\n"
        "var verEl=document.getElementById(pre+'ver'),verBase=verEl?verEl.textContent:'';function showMat(){if(verEl)verEl.textContent=verBase+(MAT===1?' · 糸':MAT===2?' · 鍵':MAT===3?' · 塵':'');}showMat();\n"
        "function answer(){ansT=performance.now();document.documentElement.classList.add('known');try{localStorage.setItem('kn_known','1');}catch(e){}}\n"
        "function answerNow(){var ph0=(2.1*0.2)%1;for(var i=0;i<med.length;i++){var m=med[i];m.off=((ph0-simT*0.2)%1+1)%1;m.charge=1;}simT=2.1;lastCycle=Math.floor(simT*0.2-0.875);lensV+=7.0;echoA=1;hit=1;if(window.KN_AUDIO){KN_AUDIO.kick();KN_AUDIO.hit();}MAT=(MAT+1)%4;showMat();}\n"
        "try{if(localStorage.getItem('kn_known'))document.documentElement.classList.add('known');}catch(e){}\n"
        "window.KN_TEST={knock:function(ts){taps=[];var r=false;for(var i=0;i<ts.length;i++)r=knock(ts[i])||r;return r;},gone:function(){return gone;},taps:function(){return taps.length;},breath:function(){return breath;},mat:function(){return MAT;}};")
    rep("function strike(){hit=1;simT=2.1;med[0].charge=1;lensV+=3.2;echoA=1;if(window.KN_AUDIO)KN_AUDIO.hit();lastCycle=Math.floor(simT*0.2-0.875);}",
        "function strike(){if(gone>0.5||ansT>=0)return;hit=1;simT=2.1;med[0].charge=1;lensV+=3.2;echoA=1;if(window.KN_AUDIO)KN_AUDIO.hit();lastCycle=Math.floor(simT*0.2-0.875);if(knock(performance.now()))answer();}")
    rep("intro=reduce?1:Math.min(1,(now-introT0)/3400);if(intro>=1&&!introDone){introDone=true;strike();}",
        "intro=reduce?1:Math.min(1,(now-introT0)/3400);if(intro>=1&&!introDone){introDone=true;strike();}\n"
        "  if(visible&&introDone&&!reduce)seenT+=dt;if(!goneDone&&goneT<0&&seenT>GONE_AFTER){goneT=now;}\n"
        "  if(goneT>=0){var ge=(now-goneT)/1000;if(ge<2.5)gone=ge/2.5;else if(ge<30.5)gone=1;else if(ge<33.9)gone=1-(ge-30.5)/3.4;else{gone=0;goneT=-1;goneDone=true;strike();}}\n"
        "  if(ansT>=0){var ae=(now-ansT)/1000;if(ae<0.55){breath=Math.max(0,Math.min(1,ae/0.12));}else{breath=0;ansT=-1;answerNow();}}else{breath=0;}\n"
        "  matT+=((MAT===1?1:0)-matT)*(1-Math.exp(-dt/0.6));dustT+=((MAT===3?1:0)-dustT)*(1-Math.exp(-dt/1.4));")
    rep("if(m.hero){var cyc=Math.floor(simT*0.2-0.875);if(cyc>lastCycle){lastCycle=cyc;if(window.KN_AUDIO)KN_AUDIO.kick();}}",
        "if(m.hero){var cyc=Math.floor(simT*0.2-0.875);if(cyc>lastCycle){lastCycle=cyc;if(window.KN_AUDIO&&gone<0.5&&ansT<0)KN_AUDIO.kick();}}")
    rep("if(mm.hero&&echoA>0.02&&tier===0){","if(mm.hero&&echoA>0.02&&tier===0&&gone<0.01){")
    rep("    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,mm.hero?1.0:0.55);gl.uniform1f(U.uCharge,mm.charge);\n    gl.uniform1f(U.uGlow,1.0);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);gl.drawArrays(gl.POINTS,0,NB);",
        "    gl.uniform1f(U.uIntro,mm.hero?Math.min(intro,1-gone,1-0.72*dustT):intro);var isKey=mm.hero&&MAT===2;gl.uniform1f(U.uKey,isKey?1.0:0.0);gl.uniform1f(U.uKeyF,isKey?1.0:0.0);\n"
        "    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,(mm.hero?1.0:0.55)*(1.0-0.88*breath));gl.uniform1f(U.uCharge,mm.charge);\n"
        "    if(mm.hero&&matT>0.02){gl.uniform1f(U.uThread,1.0);gl.uniform1f(U.uGlow,1.0);gl.uniform1f(U.uDim,matT*(1.0-0.88*breath));gl.blendFunc(gl.SRC_ALPHA,gl.ONE);\n"
        "      gl.drawArrays(gl.LINE_STRIP,0,900);for(var tk=0;tk<TN;tk++)gl.drawArrays(gl.LINE_STRIP,OT+tk*TL,TL);for(var ak=0;ak<4;ak++)gl.drawArrays(gl.LINE_STRIP,OA+ak*AR,130);\n"
        "      gl.uniform1f(U.uThread,0.0);gl.uniform1f(U.uDim,(1.0-0.9*matT)*(1.0-0.88*breath));}\n"
        "    gl.uniform1f(U.uGlow,1.0);gl.blendFunc(gl.SRC_ALPHA,gl.ONE_MINUS_SRC_ALPHA);if(isKey){gl.drawArrays(gl.POINTS,0,Math.floor(NS/4));gl.drawArrays(gl.POINTS,NS,NB-NS);}else{gl.drawArrays(gl.POINTS,0,NB);}")
    rep("    gl.uniform1f(U.uGlow,mm.hero?0.28:0.18);gl.blendFunc(gl.SRC_ALPHA,gl.ONE);gl.drawArrays(gl.POINTS,0,NB);\n    if(mm.hero){gl.uniform1f(U.uGlow,1.0);gl.drawArrays(gl.POINTS,NB,NL);}}",
        "    gl.uniform1f(U.uGlow,isKey?0.1:(mm.hero?0.28:0.18));gl.blendFunc(gl.SRC_ALPHA,gl.ONE);if(isKey){gl.drawArrays(gl.POINTS,0,Math.floor(NS/4));gl.drawArrays(gl.POINTS,NS,NB-NS);}else{gl.drawArrays(gl.POINTS,0,NB);}\n    if(mm.hero){gl.uniform1f(U.uKey,0.0);gl.uniform1f(U.uKeyF,0.0);gl.uniform1f(U.uGlow,1.0);gl.drawArrays(gl.POINTS,NB,NL);}}")
    return out
hub_in,hub_out,ins_in,ins_out=sys.argv[1:5]
pathlib.Path(hub_out).write_text(apply(pathlib.Path(hub_in).read_text(),''))
pathlib.Path(ins_out).write_text(apply(pathlib.Path(ins_in).read_text(),'kn-'))
print('built')
