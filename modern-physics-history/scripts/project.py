"""Shared source assembly and structural checks. No network or third-party imports."""
from pathlib import Path
import json
import os
import re
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / 'docs'
ANCHOR = re.compile(r'<a\s+id="([^"]+)"\s*></a>')
LINK = re.compile(r'\]\(([^\s()]*(?:\([^\s()]*\)[^\s()]*)*)\)')
INCLUDE = re.compile(r'^<!-- include-derivation: ([^\n]+) -->\n.*?^<!-- /include-derivation -->[ \t]*$', re.M | re.S)


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding='utf-8')


def book():
    return json.loads(read(ROOT / 'data/book.json'))


def chapters(meta=None):
    return [c for p in (meta or book())['parts'] for c in p['chapters']]


def source_paths(meta=None):
    m = meta or book()
    return [m['preface']] + [c['path'] for c in chapters(m)] + [a['path'] for a in m['appendices']] + [d['path'] for d in m['derivations']]


def source(path):
    p = (DOCS / path).resolve()
    if not p.is_relative_to(DOCS.resolve()):
        raise ValueError(f'正文路径超出 docs：{path}')
    if not p.is_file():
        raise ValueError(f'正文文件不存在：{path}')
    return read(p)


def relative(target, origin):
    return os.path.relpath(target, Path(origin).parent).replace(os.sep, '/')


def rebase_links(text, origin, target):
    def replace(m):
        url = m[1]
        if urlsplit(url).scheme or url.startswith('//'):
            return m[0]
        path, sep, anchor = url.partition('#')
        absolute = (DOCS / Path(origin).parent / path).resolve() if path else (DOCS / origin).resolve()
        if not absolute.is_relative_to(DOCS.resolve()):
            raise ValueError(f'链接超出 docs：{origin}: {url}')
        dest = absolute.relative_to(DOCS.resolve()).as_posix()
        prefix = '' if dest == target else relative(dest, target)
        return '](' + prefix + (sep + anchor if sep else '') + ')'
    return LINK.sub(replace, text)


def expanded(path, view='web'):
    text = source(path)
    if view == 'book':
        shift = 2 if path.startswith('chapters/') else 1 if path.startswith('appendices/') else 0
        if shift:
            text = re.sub(r'^(#{1,2}) ', lambda m: '#' * (len(m[1]) + shift) + ' ', text, flags=re.M)
    known = {d['path'] for d in book()['derivations']}
    def include(m):
        item = m[1].strip()
        if item not in known:
            raise ValueError(f'未登记的推导：{item}')
        frag = source(item)
        if INCLUDE.search(frag):
            raise ValueError(f'推导不允许嵌套包含：{item}')
        frag = rebase_links(frag, item, path)
        return re.sub(r'^# ', '##### ' if view == 'book' else '### ', frag, count=1).rstrip()
    text = INCLUDE.sub(include, text)
    if view == 'book':
        text = LINK.sub(lambda m: '](#' + m[1].split('#', 1)[1] + ')' if '#' in m[1] and not urlsplit(m[1]).scheme else m[0], text)
    return text.strip()


def assemble():
    m = book()
    fields = [('title', m['title']), ('date', m['date']), ('version', m['edition'])]
    front = '---\n' + '\n'.join(k + ': ' + json.dumps(v, ensure_ascii=False) for k, v in fields) + '\n---\n\n'
    blocks = [expanded(m['preface'], 'book')]
    for part in m['parts']:
        blocks.append('## ' + part['title'])
        blocks += [expanded(c['path'], 'book') for c in part['chapters']]
    blocks += [expanded(a['path'], 'book') for a in m['appendices']]
    return front + '\n\n'.join(blocks) + '\n'


def reference_records():
    text = source('appendices/references.md')
    out = []
    group = ''
    row = re.compile(r'^\| <a id="ref-(\d+)"[^>]*></a>(\d+) \| \[(.*?)\]\((https?://.+)\) \| (.*?) \|$')
    for line in text.splitlines():
        if line.startswith('## 资料组：'):
            group = line[len('## 资料组：'):].strip()
        m = row.match(line)
        if 'id="ref-' in line and not m:
            raise ValueError('文献行格式错误：' + line)
        if m:
            if m[1] != m[2]:
                raise ValueError(f'文献锚点与显示编号不一致：{m[1]} / {m[2]}')
            out.append({'id': m[1], 'label': m[3], 'url': m[4], 'kind': m[5], 'group': group})
    return out


def table_rows(text):
    for line in text.splitlines():
        if not line.startswith('|') or re.fullmatch(r'[|\s:\-]+', line):
            continue
        yield [c.strip() for c in re.split(r'(?<!\\)\|', line.strip().strip('|'))]


def timeline_records():
    out = []
    for row in table_rows(source('appendices/timeline.md')):
        if row[0] == '年代':
            continue
        if len(row) != 5:
            raise ValueError('时间轴行应有五列：' + repr(row))
        out.append(dict(zip(['period', 'researchers', 'milestone', 'question', 'source_links_markdown'], row)))
        out[-1]['question_anchors'] = re.findall(r'#(q-\d+-\d+)', row[-1])
    return out


def question_records():
    units = {}
    for c in chapters():
        raw = source(c['path'])
        full = expanded(c['path'])
        sections = list(re.finditer(r'^## (\d+\.\d+) (.+)$', full, re.M))
        raw_sections = list(re.finditer(r'^## (\d+\.\d+) (.+)$', raw, re.M))
        for i, h in enumerate(sections):
            text = full[h.end():sections[i+1].start() if i+1<len(sections) else len(full)]
            rh = raw_sections[i]
            rtext = raw[rh.end():raw_sections[i+1].start() if i+1<len(raw_sections) else len(raw)]
            units[h[1]] = {'id':h[1], 'title':h[2], 'chapter':c['number'], 'source_file':c['path'], 'anchor':'q-'+h[1].replace('.', '-'),
                          'urls':list(dict.fromkeys(m[1] for m in LINK.finditer(text) if m[1].startswith(('https://','http://')))),
                          'derivations':[m[1].strip() for m in INCLUDE.finditer(rtext)]}
    out = []
    for row in table_rows(source('appendices/question-index.md')):
        if row[0] == '问题':
            continue
        q = re.search(r'\[§(\d+\.\d+) (.*?)\]\([^\n]*#(q-\d+-\d+)\)', row[0])
        if not q or q[1] not in units:
            raise ValueError('问题索引指向不存在的小节：' + row[0])
        item = dict(units[q[1]])
        item['index_label'] = q[2]
        item['references'] = re.findall(r'#ref-(\d+)', row[1])
        item['derivation_note'] = row[2]
        out.append(item)
    if set(units) - {q['id'] for q in out} != {q['id'] for q in units.values() if q['chapter'] > 19}:
        raise ValueError('附录 E 未覆盖全部第 1—19 章问题')
    return out


def validate_registry(refs):
    errors = []
    ids, urls = set(), set()
    for r in refs:
        if r['id'] in ids: errors.append('文献编号重复：' + r['id'])
        if r['url'] in urls: errors.append('文献网址重复：' + r['url'])
        ids.add(r['id']); urls.add(r['url'])
        parsed = urlsplit(r['url'])
        if parsed.scheme not in ('http','https') or not parsed.netloc:
            errors.append('文献网址格式错误：' + r['id'])
    return errors


def validate_documents(documents):
    """Check actual file targets and explicit anchors, with duplicate anchor detection."""
    errors, owners = [], {}
    for path, text in documents.items():
        for a in ANCHOR.findall(text):
            if a in owners: errors.append('锚点重复：' + a)
            owners[a] = path
    for origin, text in documents.items():
        for m in LINK.finditer(text):
            url = m[1]
            if urlsplit(url).scheme or url.startswith('//'): continue
            target, _, anchor = url.partition('#')
            dest = (DOCS / Path(origin).parent / unquote(target)).resolve() if target else (DOCS / origin).resolve()
            if not dest.is_relative_to(DOCS.resolve()):
                errors.append(f'链接超出 docs：{origin}: {url}'); continue
            key = dest.relative_to(DOCS.resolve()).as_posix()
            if key not in documents:
                errors.append(f'链接文件不存在：{origin}: {url}')
            elif anchor and owners.get(unquote(anchor)) != key:
                errors.append(f'链接锚点不存在或位于别的文件：{origin}: {url}')
    return errors


def validate():
    errors = []
    paths = source_paths()
    if len(paths) != len(set(paths)): errors.append('目录清单包含重复路径')
    docs = {p: source(p) for p in paths}
    errors += validate_documents(docs)
    for c in chapters():
        actual = re.search(r'^# (.+)$',docs[c['path']],re.M)
        if not actual or actual[1] != c['title']: errors.append('章节标题与 book.json 不一致：'+c['path'])
    includes = [m[1].strip() for c in chapters() for m in INCLUDE.finditer(docs[c['path']])]
    known = [d['path'] for d in book()['derivations']]
    if sorted(includes) != sorted(known): errors.append('每则推导必须在正文中恰好包含一次')
    refs = reference_records()
    errors += validate_registry(refs)
    url_ids = {r['url']:r['id'] for r in refs}
    ref_ids = {r['id'] for r in refs}
    for q in question_records():
        if len(q['references']) != len(set(q['references'])): errors.append(q['id']+' 的文献编号重复')
        missing = set(q['references']) - ref_ids
        if missing: errors.append(q['id']+' 引用了未登记编号：'+str(sorted(missing)))
        unknown = set(q['urls']) - set(url_ids)
        if unknown: errors.append(q['id']+' 有未收入附录 D 的资料链接：'+str(sorted(unknown)))
        actual = {url_ids[u] for u in q['urls'] if u in url_ids}
        if actual != set(q['references']): errors.append(q['id']+' 的正文引文与附录 E 不一致')
        if bool(q['derivations']) != q['derivation_note'].startswith('有'): errors.append(q['id']+' 的推导标记与正文不一致')
    for row in timeline_records():
        if not row['question_anchors']: errors.append('时间轴缺少出处：'+row['period'])
    full = assemble()
    displays = re.findall(r'^\$\$\n(.*?)^\$\$', full, re.M|re.S)
    if full.count('$$') != 2*len(displays): errors.append('显示公式的 $$ 分隔符不成对')
    return errors


def bib_escape(text):
    replacements = {'\\':r'\textbackslash{}', '{':r'\{', '}':r'\}', '&':r'\&',
                    '%':r'\%', '#':r'\#', '_':r'\_', '$':r'\$', '~':r'\textasciitilde{}',
                    '^':r'\textasciicircum{}'}
    return ''.join(replacements.get(char, char) for char in text)


def generated_files():
    refs, qs, timeline = reference_records(), question_records(), timeline_records()
    outputs = {}
    for name, data in [('references',refs),('questions',qs),('timeline',timeline)]:
        outputs[ROOT / 'data' / (name+'.json')] = json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    bib = ['% Generated from docs/appendices/references.md. Do not edit.', '% Minimal records: howpublished preserves the source label; no author/year/title is guessed.\n']
    for r in refs:
        bib.append('@misc{ref'+r['id']+',\n  howpublished = {'+bib_escape(r['label'])+'},\n  url = {'+r['url']+'},\n  note = {'+bib_escape(r['kind'])+'}\n}\n')
    outputs[DOCS/'assets/references.bib']='\n'.join(bib)
    outputs[ROOT/'manuscript.md']=assemble()
    index=['# 推导札记\n','推导在所属章节中保留原来的位置，也可在这里单独阅读。\n','| 推导 | 所属章节 |','| --- | --- |']
    for d in book()['derivations']:
        c=next(c for c in chapters() if c['number']==d['chapter'])
        index.append(f"| [{d['title']}]({Path(d['path']).name}) | [{c['title']}]({relative(c['path'],'derivations/index.md')}) |")
    outputs[DOCS/'derivations/index.md']='\n'.join(index)+'\n'
    return outputs
