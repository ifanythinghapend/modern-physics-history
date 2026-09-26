"""Build a complete static reading page, including SVG equations, from chapter sources."""
from html import escape
from html.parser import HTMLParser
from pathlib import Path
import hashlib
import json
import re
import subprocess
import markdown
from project import ROOT, DOCS, LINK, book, chapters, expanded, source, validate, generated_files, write, reference_records

class Plain(HTMLParser):
    def __init__(self): super().__init__(); self.parts=[]
    def handle_data(self, text): self.parts.append(text)

def plain(text):
    p=Plain(); p.feed(markdown.markdown(text,extensions=['tables'])); return ' '.join(p.parts)

def page_id(path):
    if path=='preface.md': return 'page-preface'
    return 'page-'+Path(path).stem

def reading_units():
    m=book()
    units=[{'path':m['preface'],'title':'导读','group':'阅读起点'}]
    for part in m['parts']:
        units += [dict(c,group=part['title']) for c in part['chapters']]
    units += [dict(a,group='附录') for a in m['appendices']]
    return units

def links_for_web(text,path):
    def replace(match):
        url=match[1]
        if re.match(r'[A-Za-z][A-Za-z0-9+.-]*:',url) or url.startswith('//'): return match[0]
        dest,_,anchor=url.partition('#')
        if anchor:return '](#'+anchor+')'
        target=(DOCS/Path(path).parent/dest).resolve().relative_to(DOCS.resolve()).as_posix()
        if target.endswith('.md'):return '](#'+page_id(target)+')'
        return '](docs/'+target+')'
    return LINK.sub(replace,text)

def graph_svg(raw):
    positions={'A':(150,50),'D':(420,50),'F':(690,50),'B':(150,170),'C':(420,170),
               'G':(690,170),'J':(150,290),'E':(420,290),'H':(420,410),'I':(420,530)}
    links={'A':2,'D':1,'F':3,'B':7,'C':4,'G':18,'J':15,'E':8,'H':8,'I':18}
    labels={}
    edges=[]
    for line in raw.splitlines()[1:]:
        line=line.strip()
        if not line:continue
        for node,label in re.findall(r'([A-Z])\["([^"]+)"\]',line):labels[node]=label
        simple=re.sub(r'\["[^"]+"\]','',line)
        m=re.fullmatch(r'([A-Z])\s*(-->|<-->)\s*([A-Z])',simple)
        if not m:raise ValueError('关系图语法需要检查：'+line)
        edges.append((m[1],m[3],m[2]=='<-->'))
    if set(labels)!=set(positions):raise ValueError('关系图节点已变化，请同步检查 SVG 布局。')
    parts=['<figure class="branch-map"><svg viewBox="0 0 840 590" role="img" aria-labelledby="map-title map-desc" xmlns="http://www.w3.org/2000/svg">',
    '<title id="map-title">物理分支之间的方法联系</title><desc id="map-desc">量子、统计与引力经多体、重整化、纠缠和黑洞问题相联系。箭头的端点和方向来自正文中的关系图。</desc>',
    '<defs><marker id="arrow-end" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8" fill="#788787"/></marker><marker id="arrow-start" markerWidth="8" markerHeight="8" refX="1" refY="4" orient="auto"><path d="M8,0 L0,4 L8,8" fill="#788787"/></marker></defs>']
    for a,b,both in edges:
        x1,y1=positions[a];x2,y2=positions[b]
        if y1==y2:
            path=f'M{x1+101},{y1} L{x2-103},{y2}'
        elif (a,b)==('J','I'):
            path=f'M{x1},{y1+25} C{x1},440 225,{y2} {x2-103},{y2}'
        elif (a,b)==('G','I'):
            path=f'M{x1},{y1+25} C{x1},410 620,{y2} {x2+103},{y2}'
        elif (a,b)==('D','E'):
            path=f'M{x1+101},{y1} C585,{y1} 585,{y2} {x2+103},{y2}'
        else:
            path=f'M{x1},{y1+25} C{x1},{y1+70} {x2},{y2-70} {x2},{y2-27}'
        parts.append(f'<path d="{path}" fill="none" stroke="#788787" stroke-width="1.6" marker-end="url(#arrow-end)"'+(' marker-start="url(#arrow-start)"' if both else '')+'/>')
    for node,(x,y) in positions.items():
        parts.append(f'<a href="#chapter-{links[node]}"><rect x="{x-100}" y="{y-24}" width="200" height="48" rx="5" fill="#f8f6f0" stroke="#b7c6c2"/><text x="{x}" y="{y+5}" text-anchor="middle" font-size="16" fill="#1c414a">{escape(labels[node])}</text></a>')
    parts.append('</svg><figcaption>点击节点可跳转到相应章节。</figcaption></figure>')
    return ''.join(parts)

def navigation():
    m=book()
    out=['<a class="nav-start" href="#start">开始阅读</a><a href="#page-preface">导读</a>']
    for part in m['parts']:
        out.append('<details><summary>'+escape(part['title'])+'</summary>')
        for c in part['chapters']:out.append(f'<a href="#chapter-{c["number"]}">{escape(c.get("nav_title",c["title"]))}</a>')
        out.append('</details>')
    out.append('<details><summary>推导札记</summary>')
    for d in m['derivations']:out.append(f'<a href="#derivation-{d["id"]}">{d["id"]:02d} · {escape(d.get("nav_title",d["title"]))}</a>')
    out.append('</details><details><summary>附录与资料</summary>')
    for a in m['appendices']:out.append(f'<a href="#appendix-{a["letter"].lower()}">{escape(a["title"])}</a>')
    out.append('</details><a href="#participate">参与修改</a>')
    return ''.join(out)

def landing():
    m=book()
    rows=[]
    for part in m['parts']:
        links=''.join(f'<a href="#chapter-{c["number"]}">{escape(c.get("nav_title",c["title"]))}<span aria-hidden="true">↗</span></a>' for c in part['chapters'])
        rows.append('<div class="part-row"><h3>'+escape(part['title'])+'</h3><div>'+links+'</div></div>')
    return '''<article id="start" class="reading-page is-current landing">
<div class="hero"><div><p class="eyebrow">公开讨论稿 · 主要历史节点截至 2025 年</p>
<h1>现代物理学史<span>问题、人物与分支</span></h1>
<p class="lead">光是什么，原子为什么稳定，大量粒子怎样形成新的物态，时空又如何演化？从具体问题出发，读研究者怎样提出、检验和修正物理理论。</p>
<p class="edition-stats">七篇 · 二十一章 · 二十则推导札记</p>
<div class="actions"><a class="button primary" href="#page-preface">从导读开始 <span aria-hidden="true">→</span></a><a class="button" href="pdf/modern-physics-history.pdf">阅读 PDF</a></div></div>
<img class="cover" src="docs/assets/images/cover.png" width="220" height="312" alt="现代物理学史讲义封面"></div>
<div class="entry-grid"><a href="#appendix-e"><small>从问题进入</small><strong>94 个问题与出处</strong><span>研究者、成果与可查证的资料</span></a>
<a href="#appendix-a"><small>循时间回看</small><strong>关键发展时间轴</strong><span>人物与事件怎样改变研究方向</span></a>
<a href="#chapter-20"><small>在分支间比较</small><strong>物理学的分支地图</strong><span>对象、方法与反复出现的结构</span></a></div>
<h2 class="contents-heading">全文目录</h2>'''+''.join(rows)+'''
<div class="note"><h2>怎样使用这份讲义</h2><p>可以按顺序读，也可以用左侧目录或全文搜索进入具体问题。推导保留在所属章节中，并提供单独的入口。文献集中列在附录 D，问题与出处的对应关系列在附录 E。</p><p>这是一份可持续修订的讨论稿。引用方便追查依据，不能代替阅读原文；发现问题时，请写明位置、原句和参考资料。</p></div></article>'''

def build():
    errors=validate()
    if errors:raise ValueError('\n'.join(errors))
    for path,text in generated_files().items():write(path,text)
    m=book();units=reading_units();formulas=[];bodies=[];search=[]
    for unit in units:
        path=unit['path'];text=expanded(path)
        for d in m['derivations']:
            if d['chapter']==unit.get('number'):
                text=text.replace('### '+d['title'],f'<a id="derivation-{d["id"]}"></a>\n\n### '+d['title'],1)
        # Search complete question text, chapter text, each derivation, and references.
        search.append([page_id(path),unit['title'],plain(text)])
        question_matches=list(re.finditer(r'^## (\d+\.\d+) (.+)$',text,re.M))
        for i,q in enumerate(question_matches):
            section=text[q.end():question_matches[i+1].start() if i+1<len(question_matches) else len(text)]
            search.append(['q-'+q[1].replace('.','-'),q[1]+' '+q[2],plain(section)])
        text=links_for_web(text,path)
        text=re.sub(r'```mermaid\n(.*?)\n```',lambda x:graph_svg(x[1]),text,flags=re.S)
        def math_token(tex,display):
            index=len(formulas);formulas.append({'tex':tex.strip(),'display':display})
            tag='div' if display else 'span'
            return f'<{tag} data-math="{index}"></{tag}>'
        text=re.sub(r'^\$\$\n(.*?)^\$\$',lambda x:math_token(x[1],True),text,flags=re.M|re.S)
        text=re.sub(r'(?<![\\$])\$(?!\$)(.+?)(?<!\\)\$(?!\$)',lambda x:math_token(x[1],False),text,flags=re.S)
        html=markdown.markdown(text,extensions=['tables','fenced_code','md_in_html'])
        bodies.append((unit,html))
    for d in m['derivations']:
        search.append(['derivation-'+str(d['id']),d['title'],plain(source(d['path']))])
    for r in reference_records():search.append(['ref-'+r['id'],r['label'],r['group']+' '+r['kind']+' '+r['url']])
    result=subprocess.run(['node',str(ROOT/'scripts/render_math.cjs')],input=json.dumps(formulas),capture_output=True,text=True,encoding='utf-8',cwd=ROOT)
    if result.returncode:raise RuntimeError(result.stderr)
    rendered=json.loads(result.stdout)
    if len(rendered['html'])!=len(formulas):raise ValueError('公式数量不一致')
    articles=[landing()]
    order=[{'id':'start','title':'开始阅读'}]+[{'id':page_id(u['path']),'title':u.get('nav_title',u['title'])} for u in units]
    for i,(unit,body) in enumerate(bodies,1):
        def insert_formula(match):
            index=int(match[2]);tag=match[1]
            return f'<{tag} class="'+('equation' if formulas[index]['display'] else 'math-inline')+'" role="math" aria-label="'+escape(formulas[index]['tex'],quote=True)+'">'+rendered['html'][index]+f'</{tag}>'
        body=re.sub(r'<(div|span) data-math="(\d+)"></\1>',insert_formula,body)
        body=re.sub(r'(<table>.*?</table>)',r'<div class="table-scroll">\1</div>',body,flags=re.S)
        body=re.sub(r'<h([123])>',r'<h\1 tabindex="-1">',body)
        prev=order[i-1]
        nav=f'<a href="#{prev["id"]}"><small>上一节</small>{escape(prev["title"])}</a>'
        if i+1<len(order):
            nxt=order[i+1];nav+=f'<a href="#{nxt["id"]}"><small>下一节</small>{escape(nxt["title"])}</a>'
        articles.append(f'<article id="{page_id(unit["path"])}" class="reading-page"><p class="eyebrow">{escape(unit["group"])}</p>'+body+f'<nav class="page-turn" aria-label="前后章节">{nav}</nav></article>')
    articles.append('''<article id="participate" class="reading-page"><p class="eyebrow">共同修订</p><h1>参与修改</h1><p>发现错误或想补充内容时，请记录章节、小节、原句、修改建议，以及支持建议的文献。若使用 PDF 页码，也请注明版本。</p><h2>四种参与方式</h2><ul><li>内容勘误：指出史实、公式、归因或表述的问题。</li><li>文献建议：说明一项资料支持哪条论断，尽量附 DOI、链接或页码。</li><li>新增内容：先说明要回答的问题及其与现有章节的关系。</li><li>推导补充：指出看不懂或缺失的步骤、结论位置和期望深度。</li></ul><p class="online-only"><a class="button primary issue-link" href="README.md">到仓库提出建议</a></p><p>已有具体修改时，可编辑相应的 Markdown 文件并提交 Pull request。正文在 <code>docs/chapters/</code>，推导在 <code>docs/derivations/</code>，资料索引在 <code>docs/appendices/</code>。</p><h2>核对与讨论</h2><p>项目纲领、逐章编审大纲及审阅指南见仓库首页。黑体辐射试点已经记录证据位置与计算条件，仍待独立专业审阅；其余章节保留公开讨论稿状态。</p><p>补充推导要交代变量、假设、边界条件和近似。发现、发表、观测和获奖可能对应不同日期，不能互相替代。讨论围绕证据与论证，避免公开未经同意披露的私人信息。</p><p>项目尚未选定正文与自编代码的开放许可证；第三方资料按各自条件使用。</p></article>''')
    css=(ROOT/'web/reader.css').read_text(encoding='utf-8')+'\n'+rendered['css']
    js=(ROOT/'web/reader.js').read_text(encoding='utf-8')
    template=(ROOT/'web/template.html').read_text(encoding='utf-8')
    output=template.replace('@@CSS@@',css).replace('@@NAV@@',navigation()).replace('@@CONTENT@@','\n'.join(articles)).replace('@@INDEX@@',json.dumps(search,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')).replace('@@JS@@',js).replace('@@DATE@@',escape(m['date'])).replace('@@EDITION@@',escape(m['edition']))
    if re.search(r'@@[A-Z]+@@',output):raise ValueError('模板变量未替换')
    write(ROOT/'index.html',output)
    audit={'chapters':len(chapters()),'derivations':len(m['derivations']),'references':len(reference_records()),'formulas':len(formulas),'display_formulas':sum(f['display'] for f in formulas),'inline_formulas':sum(not f['display'] for f in formulas),'source_sha256':hashlib.sha256((ROOT/'manuscript.md').read_bytes()).hexdigest()}
    write(ROOT/'build/web-report.json',json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(audit,ensure_ascii=False));print('Generated index.html: ready to open locally or publish with GitHub Pages.')

if __name__=='__main__':
    try:build()
    except (ValueError,RuntimeError,OSError) as error:raise SystemExit(str(error))
