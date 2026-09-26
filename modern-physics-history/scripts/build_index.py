"""Generate structured data, bibliography and merged Markdown."""
import argparse
from project import generated_files, read, write, validate

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true',help='Check generated files without modifying them')
    args=parser.parse_args()
    errors=validate()
    if errors: raise SystemExit('\n'.join(errors))
    stale=[]
    for path,text in generated_files().items():
        if args.check:
            if not path.exists() or read(path)!=text:stale.append(str(path))
        else:write(path,text)
    if stale: raise SystemExit('生成文件需要更新，请运行 python scripts/build_index.py：\n'+'\n'.join(stale))
    print('索引与合并正文检查通过。' if args.check else '已生成索引、BibTeX 与合并正文。')
if __name__=='__main__':main()
