# v22/v23「沈黙と合図」: behaviour-only additions applied to the hub (index.html) and the BASE insert (kn- prefix).
# Usage: python3 -I tools/build_v22.py <hub_in> <hub_out> <insert_in> <insert_out>
import re,sys,pathlib
def apply(src,pre,label):
    out=src
    def rep(old,new,count=1):
        nonlocal out
        n=out.count(old); assert n==count,(pre,old[:70],n); out=out.replace(old,new)
    semi=';' if pre else ''
    # version stamp
    rep('id="%sver">v21<'%pre,'id="%sver">%s<'%(pre,label))
    # faint second ring on the key for those who have knocked (no text)
    rm='@media (prefers-reduced-motion: reduce){.%ssheet{transition:none%s}}'%(pre,semi)
    rep(rm,rm+'\nhtml.known .%shit{box-shadow:0 0 0 6px rgba(7,7,11,.65),0 0 0 7px rgba(217,168,74,.6)%s}'%(pre,semi))
    # knock pattern next to LINKS (swap table)
    m=re.search(r'(const|var) (KN_)?LINKS=\{',out); assert m,(pre,'LINKS')
    out=out[:m.start()]+"const KNOCK=[1,0.5,0.5];   // 合図のリズム（叩く間隔の比。鍵山のリズムに差し替える）\n"+out[m.start():]
    rep("var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;",
        "var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;\n"
        "/* 一分の不在: 90 秒見た人にだけ一度、主役が塵に解けて消え、戻る（intro の組み上がりを逆に使う） */\n"
        "var gone=0,goneT=-1,goneDone=false,seenT=0,GONE_AFTER=(function(){var g=parseFloat(new URLSearchParams(location.search).get('gone'));return g>0?g:90;})();\n"
        "/* 合図: 金の鍵を KNOCK の比で叩くと、夜が応える */\n"
        "var taps=[],KDBG=/[?&]knock=1/.test(location.search);function knock(now){taps.push(now);if(taps.length>KNOCK.length+1)taps.shift();if(taps.length<KNOCK.length+1)return false;var iv=[],num=0,den=0;for(var i=1;i<taps.length;i++)iv.push(taps[i]-taps[i-1]);for(var q=0;q<iv.length;q++){num+=iv[q]*KNOCK[q];den+=KNOCK[q]*KNOCK[q];}var base=num/den;var ok=base>=200&&base<=1600;var worst=0;for(var j=0;j<iv.length;j++){var e=Math.abs(iv[j]/base-KNOCK[j])/Math.max(0.5,KNOCK[j]);if(e>worst)worst=e;}if(worst>0.35)ok=false;if(KDBG){var v=document.getElementById(pre+'ver');if(v)v.textContent=iv.map(function(x){return (x/base).toFixed(2);}).join(' ')+(ok?' ok':' x');}if(!ok)return false;taps=[];return true;}\n"
        "var ansT=-1,breath=0;function answer(){ansT=performance.now();document.documentElement.classList.add('known');try{localStorage.setItem('kn_known','1');}catch(e){}}\n"
        "function answerNow(){var ph0=(2.1*0.2)%1;for(var i=0;i<med.length;i++){var m=med[i];m.off=((ph0-simT*0.2)%1+1)%1;m.charge=1;}simT=2.1;lastCycle=Math.floor(simT*0.2-0.875);lensV+=7.0;echoA=1;hit=1;if(window.KN_AUDIO){KN_AUDIO.kick();KN_AUDIO.hit();}}\n"
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
    rep("gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,mm.hero?1.0:0.55);gl.uniform1f(U.uCharge,mm.charge);",
        "gl.uniform1f(U.uIntro,mm.hero?Math.min(intro,1-gone):intro);\n"
        "    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,(mm.hero?1.0:0.55)*(1.0-0.88*breath));gl.uniform1f(U.uCharge,mm.charge);")
    rep("if(mm.hero&&echoA>0.02&&tier===0){","if(mm.hero&&echoA>0.02&&tier===0&&gone<0.01){")
    return out
hub_in,hub_out,ins_in,ins_out=sys.argv[1:5]
pathlib.Path(hub_out).write_text(apply(pathlib.Path(hub_in).read_text(),'','v23'))
pathlib.Path(ins_out).write_text(apply(pathlib.Path(ins_in).read_text(),'kn-','v23'))
print('built')
