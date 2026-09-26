"""Assemble chapter sources and build the PDF. Run from any working directory."""
from pathlib import Path
import importlib.util
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'
OUTPUT = ROOT / 'pdf/modern-physics-history.pdf'


def main():
    if sys.version_info < (3, 10):
        raise SystemExit('需要 Python 3.10 或更新版本。')
    for command in ['pandoc', 'xelatex', 'kpsewhich']:
        if shutil.which(command) is None:
            raise SystemExit(f'找不到 {command}。安装方法见 handbook/BUILD.md。')
    if importlib.util.find_spec('reportlab') is None:
        raise SystemExit('请先运行：python -m pip install -r requirements.txt')
    version = subprocess.run(['pandoc', '--version'], capture_output=True,
                             text=True, encoding='utf-8', check=True).stdout.splitlines()[0]
    if not re.match(r'pandoc 3\.', version):
        raise SystemExit('此排版脚本使用 Pandoc 3 的文档结构；请安装 Pandoc 3.x。')
    BUILD.mkdir(exist_ok=True)
    for script in ['build_index.py', 'prepare_ast.py', 'render_latex.py']:
        subprocess.run([sys.executable, str(ROOT / 'scripts' / script)],
                       cwd=ROOT, check=True)
    for n in range(1, 4):
        print(f'XeLaTeX {n}/3', flush=True)
        result = subprocess.run(
            ['xelatex', '-interaction=nonstopmode', '-halt-on-error',
             '-file-line-error', 'book.tex'], cwd=BUILD,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, encoding='utf-8', errors='replace')
        log = BUILD / f'xelatex-{n}.log'
        log.write_text(result.stdout, encoding='utf-8')
        if result.returncode:
            print(result.stdout[-3000:])
            raise SystemExit(f'编译未完成，请查看 {log}。已有 PDF 未被覆盖。')
    log_text = (BUILD / 'book.log').read_text(encoding='utf-8', errors='replace')
    if 'Missing character:' in log_text:
        raise SystemExit('编译日志发现缺字，请检查字体。已有 PDF 未被覆盖。')
    OUTPUT.parent.mkdir(exist_ok=True)
    shutil.copyfile(BUILD / 'book.pdf', OUTPUT)
    if 'Overfull' in log_text:
        print('有内容越界提示，请检查 build/book.log 和对应页面。')
    print(f'已生成：{OUTPUT}')
    print('请查看改动处的公式、表格与分页，再提交新版 PDF。')


if __name__ == '__main__':
    main()
