"""Check that a checkout contains a complete reading edition with working local links."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
import json
import re
from project import ROOT, ANCHOR, LINK, assemble, generated_files, read, source_paths, source, validate

class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids=[];self.links=[];self.assets=[];self.math=[];self.errors=[];self.svgs=0
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if attrs.get('id'):self.ids.append(attrs['id'])
        for name in ('href','xlink:href'):
            if name in attrs:self.links.append(attrs[name])
        if tag in ('img','script','iframe','audio','video','source') and attrs.get('src'):self.assets.append(attrs['src'])
        if tag=='link' and attrs.get('href'):self.assets.append(attrs['href'])
        if tag=='svg':self.svgs+=1
        if attrs.get('role')=='math':self.math.append((tag,attrs.get('aria-label','')))
        if attrs.get('data-mml-node')=='merror':self.errors.append('公式含 MathJax 错误节点')

def inspect_html(text,root=ROOT):
    page=Page();page.feed(text);errors=list(page.errors)
    ids=set(page.ids)
    errors += ['网页 ID 重复：'+i for i,n in Counter(page.ids).items() if n>1]
    for url in page.links+page.assets:
        parts=urlsplit(url)
        if parts.scheme or url.startswith('//'):continue
        if not parts.path:
            if parts.fragment and unquote(parts.fragment) not in ids:errors.append('网页锚点不存在：'+url)
        else:
            p=(root/unquote(parts.path)).resolve()
            if not p.is_relative_to(root.resolve()) or not p.is_file():errors.append('网页本地文件不存在：'+url)
    errors += ['阅读依赖外部资源：'+u for u in page.assets if urlsplit(u).scheme in ('http','https') or u.startswith('//')]
    return page,errors

def check():
    errors=validate()
    for path,text in generated_files().items():
        if not path.is_file() or read(path)!=text:errors.append('生成快照需要更新：'+str(path.relative_to(ROOT)))
    html=read(ROOT/'index.html')
    page,html_errors=inspect_html(html);errors+=html_errors
    source_anchors=set(a for path in source_paths() for a in ANCHOR.findall(source(path)))
    errors += ['源稿锚点未进入网页：'+a for a in sorted(source_anchors-set(page.ids))]
    if len(page.math)==0 or page.svgs<len(page.math):errors.append('网页公式没有完整排成 SVG')
    # Compare actual math payloads against the complete Markdown, independent of page layout.
    manuscript=assemble()
    blocks=re.findall(r'^\$\$\n(.*?)^\$\$',manuscript,re.M|re.S)
    without_blocks=re.sub(r'^\$\$\n.*?^\$\$','',manuscript,flags=re.M|re.S)
    inlines=re.findall(r'(?<![\\$])\$(?!\$)(.+?)(?<!\\)\$(?!\$)',without_blocks,re.S)
    expected=Counter([('div',s.strip()) for s in blocks]+[('span',s.strip()) for s in inlines])
    if Counter(page.math)!=expected:errors.append('网页中的 TeX 公式内容或数量与完整稿不一致')
    guides = sorted(ROOT.glob('*.md')) + sorted((ROOT/'handbook').rglob('*.md')) + [ROOT/'docs/outline.md']
    for path in guides:
        for link in LINK.finditer(read(path)):
            url=urlsplit(link[1])
            if url.scheme or link[1].startswith('//') or not url.path:continue
            target=(path.parent/unquote(url.path)).resolve()
            if not target.is_relative_to(ROOT.resolve()) or not (target.is_file() or target.is_dir()):errors.append('说明文件链接不存在：'+str(path.relative_to(ROOT))+': '+link[1])
    for required in ['.nojekyll','.gitignore','.github/workflows/checks.yml','.github/workflows/pdf.yml','pdf/modern-physics-history.pdf']:
        if not (ROOT/required).is_file():errors.append('缺少发布文件：'+required)
    return errors,{'source_anchors':len(source_anchors),'math_svg':len(page.math),'external_reading_assets':len([u for u in page.assets if urlsplit(u).scheme in ('http','https')])}

if __name__=='__main__':
    errors,stats=check()
    if errors:raise SystemExit('\n'.join(errors))
    print('可发布文件检查通过：'+json.dumps(stats,ensure_ascii=False))
