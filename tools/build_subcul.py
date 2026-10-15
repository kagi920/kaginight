# Direction D 「沈黙と合図」: behaviour only. No added words, colours, motifs. Hero geometry/colour/sound untouched.
import pathlib,sys
src=pathlib.Path('/home/user/kaginight/index.html').read_text(); out=src
def rep(old,new,count=1):
    global out
    n=out.count(old); assert n==count,(old[:70],n); out=out.replace(old,new)
OUT=sys.argv[1] if len(sys.argv)>1 else '/home/user/kaginight/subcul/index.html'
rep('<meta name="robots" content="index,follow,max-image-preview:large">','<meta name="robots" content="noindex,nofollow">')
rep('<div class="ver" id="ver">v21</div>','<div class="ver" id="ver">v22 preview D</div>')
# a faint second ring on the key for those who have knocked (no text)
rep('@media (prefers-reduced-motion: reduce){.sheet{transition:none}}\n</style>',
    '@media (prefers-reduced-motion: reduce){.sheet{transition:none}}\nhtml.known .hit{box-shadow:0 0 0 7px rgba(217,168,74,.10),0 0 0 8px rgba(217,168,74,.18)}\n</style>')
# knock pattern lives next to LINKS (swap table). Intervals as ratios: tap (1) tap (0.5) tap (0.5) tap
rep("const LINKS={","const KNOCK=[1,0.5,0.5];   // 合図のリズム（叩く間隔の比。鍵山のリズムに差し替える）\nconst LINKS={")
# state: gone (absence) + knock buffer
rep("var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;",
    "var FOV0=0.95,lens=0,lensV=0,echoA=0,parX=0,parY=0,ema=16.7,hiN=0,loN=0,tier=0,NE=MOB?2:3;\n"
    "/* 一分の不在: 90 秒見た人にだけ一度、主役が塵に解けて消え、戻る（intro の組み上がりを逆に使う） */\n"
    "var gone=0,goneT=-1,goneDone=false,seenT=0,GONE_AFTER=(function(){var g=parseFloat(new URLSearchParams(location.search).get('gone'));return g>0?g:90;})();\n"
    "/* 合図: 金の鍵を KNOCK の比で叩くと、夜が応える */\n"
    "var taps=[];function knock(now){taps.push(now);if(taps.length>KNOCK.length+1)taps.shift();if(taps.length<KNOCK.length+1)return false;var iv=[];for(var i=1;i<taps.length;i++)iv.push(taps[i]-taps[i-1]);var base=iv[0]/KNOCK[0];if(base<220||base>1400)return false;for(var j=0;j<iv.length;j++){if(Math.abs(iv[j]/base-KNOCK[j])>0.28*Math.max(1,KNOCK[j]))return false;}taps=[];return true;}\n"
    "function answer(){var ph0=(2.1*0.2)%1;for(var i=0;i<med.length;i++){var m=med[i];m.off=((ph0-simT*0.2)%1+1)%1;m.charge=1;}lensV+=5.5;echoA=1;hit=1;document.documentElement.classList.add('known');try{localStorage.setItem('kn_known','1');}catch(e){}}\n"
    "try{if(localStorage.getItem('kn_known'))document.documentElement.classList.add('known');}catch(e){}")
# strike: feed the knock detector
rep("function strike(){hit=1;simT=2.1;med[0].charge=1;lensV+=3.2;echoA=1;if(window.KN_AUDIO)KN_AUDIO.hit();lastCycle=Math.floor(simT*0.2-0.875);}",
    "function strike(){if(gone>0.5)return;hit=1;simT=2.1;med[0].charge=1;lensV+=3.2;echoA=1;if(window.KN_AUDIO)KN_AUDIO.hit();lastCycle=Math.floor(simT*0.2-0.875);if(knock(performance.now()))answer();}")
# absence schedule in frame: fade out 2.5 s, dust 28 s, reassemble 3.4 s, then a strike
rep("  intro=reduce?1:Math.min(1,(now-introT0)/3400);if(intro>=1&&!introDone){introDone=true;strike();}",
    "  intro=reduce?1:Math.min(1,(now-introT0)/3400);if(intro>=1&&!introDone){introDone=true;strike();}\n"
    "  if(visible&&introDone&&!reduce)seenT+=dt;if(!goneDone&&goneT<0&&seenT>GONE_AFTER){goneT=now;}\n"
    "  if(goneT>=0){var ge=(now-goneT)/1000;if(ge<2.5)gone=ge/2.5;else if(ge<30.5)gone=1;else if(ge<33.9)gone=1-(ge-30.5)/3.4;else{gone=0;goneT=-1;goneDone=true;strike();}}")
# hero draw uses uIntro = 1-gone (dust), kick muted while gone
rep("    if(m.hero){var cyc=Math.floor(simT*0.2-0.875);if(cyc>lastCycle){lastCycle=cyc;if(window.KN_AUDIO)KN_AUDIO.kick();}}",
    "    if(m.hero){var cyc=Math.floor(simT*0.2-0.875);if(cyc>lastCycle){lastCycle=cyc;if(window.KN_AUDIO&&gone<0.5)KN_AUDIO.kick();}}")
rep("    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,mm.hero?1.0:0.55);gl.uniform1f(U.uCharge,mm.charge);",
    "    gl.uniform1f(U.uIntro,mm.hero?Math.min(intro,1-gone):intro);\n"
    "    gl.uniformMatrix4fv(U.uModel,false,mm.mat);gl.uniform1f(U.uPhase,mm.ph);gl.uniform1f(U.uDim,mm.hero?1.0:0.55);gl.uniform1f(U.uCharge,mm.charge);")
# echoes of a gone hero should not draw
rep("    if(mm.hero&&echoA>0.02&&tier===0){","    if(mm.hero&&echoA>0.02&&tier===0&&gone<0.01){")
# expose for tests
rep("try{if(localStorage.getItem('kn_known'))document.documentElement.classList.add('known');}catch(e){}","try{if(localStorage.getItem('kn_known'))document.documentElement.classList.add('known');}catch(e){}\nwindow.KN_TEST={knock:function(ts){taps=[];var r=false;for(var i=0;i<ts.length;i++)r=knock(ts[i])||r;return r;},gone:function(){return gone;}};")
pathlib.Path(OUT).write_text(out); print('ok',len(out))
