# Assemble the BASE theme: original theme (untouched) + minified KAGI insert after <body … class="shop template"> + intro block after the first </header>.
# Then write the one-click copy page. BASE limits a theme to 150,000 characters, so the insert is minified (comments, indentation, blank lines).
# Usage: python3 -I tools/assemble_base.py <original> <insert> <below> <copy_template> <label_text> <out_full> <out_copy>
import sys,pathlib,re,html
from collections import Counter
orig,ins,below,cpt,label,out_full,out_copy=sys.argv[1:8]
o=pathlib.Path(orig).read_text(); i=pathlib.Path(ins).read_text(); b=pathlib.Path(below).read_text(); cp=pathlib.Path(cpt).read_text()
def minify(s):
    s=re.sub(r'<!--.*?-->','',s,flags=re.S)
    s=re.sub(r'/\*.*?\*/','',s,flags=re.S)            # no block comments inside quoted strings (checked)
    lines=[]
    for l in s.split('\n'):
        t=l.strip()
        if not t or t.startswith('//'): continue
        lines.append(t)
    return '\n'.join(lines)
im=minify(i)
tag='class="shop template">'; k=o.index(tag)+len(tag); full=o[:k]+'\n'+im+'\n'+o[k:]
j=full.index('</header>')+len('</header>'); full=full[:j]+'\n'+b+'\n'+full[j:]
co,cc=Counter(re.findall(r'\{block:([A-Za-z]+)\}',full)),Counter(re.findall(r'\{/block:([A-Za-z]+)\}',full))
assert all(co[x]==cc[x] for x in set(co)|set(cc)),'block tags unbalanced'
for req in ['{LogoTag}','{PageTitle}','{FaviconTag}','{CanonicalTag}']: assert req in full,req
assert len(full)<=148000,('too long',len(full))
pathlib.Path(out_full).write_text(full)
a=cp.index('<textarea id="t" readonly spellcheck="false">')+len('<textarea id="t" readonly spellcheck="false">'); e=cp.index('</textarea>',a)
cp2=cp[:a]+html.escape(full,quote=True)+cp[e:]; cp2=re.sub(r'v\d+（[^）]*）',label,cp2,count=1)
a2=cp2.index('<textarea id="t" readonly spellcheck="false">')+len('<textarea id="t" readonly spellcheck="false">'); e2=cp2.index('</textarea>',a2)
assert html.unescape(cp2[a2:e2])==full,'roundtrip'
pathlib.Path(out_copy).write_text(cp2)
print('full chars',len(full),'insert',len(i),'->',len(im),'copy ok')
