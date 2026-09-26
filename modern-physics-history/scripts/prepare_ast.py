from pathlib import Path
import json,re,subprocess

root=Path(__file__).resolve().parents[1]
(root/'build').mkdir(exist_ok=True)
source=(root/'manuscript.md').read_text(encoding='utf-8')
display=[]
def protect(m):
    display.append(m[1].strip())
    return '$$DISPLAYBLOCK'+str(len(display)-1).zfill(3)+'$$'
protected=re.sub(r'^\$\$\n(.*?)^\$\$',protect,source,flags=re.M|re.S)
p=subprocess.run(['pandoc','-f','markdown+tex_math_dollars+raw_html','-t','json'],input=protected,capture_output=True,text=True,encoding="utf-8",check=True)
doc=json.loads(p.stdout)
restored=[]
def walk(x):
    if isinstance(x,dict):
        if x.get('t')=='Math' and x['c'][0]['t']=='DisplayMath':
            index=int(x['c'][1].removeprefix('DISPLAYBLOCK'))
            x['c'][1]=display[index]
            restored.append(index)
        for v in x.values():walk(v)
    elif isinstance(x,list):
        for v in x:walk(v)
walk(doc)
assert restored==list(range(len(display)))
(root/'build/document.json').write_text(json.dumps(doc,ensure_ascii=False),encoding="utf-8")
print('Display equations protected and restored:',len(display))
