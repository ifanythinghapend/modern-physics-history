from pathlib import Path
import json
import re
import math
import os
import subprocess
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, Color
from reportlab.lib.units import mm

ROOT = Path(__file__).resolve().parents[1]
BUILD = ROOT / 'build'
BUILD.mkdir(exist_ok=True)
font_dir = os.environ.get('FANDOL_FONT_DIR')
if font_dir:
    FONTS = Path(font_dir).expanduser().resolve()
else:
    result = subprocess.run(['kpsewhich','FandolSong-Regular.otf'],capture_output=True,text=True,encoding='utf-8')
    if result.returncode or not result.stdout.strip():
        raise SystemExit('找不到 Fandol 中文字体。请安装 TeX Live 的中文语言包，或设置 FANDOL_FONT_DIR。')
    FONTS = Path(result.stdout.strip()).parent
for font_name in ['FandolSong-Regular.otf','FandolSong-Bold.otf','FandolHei-Regular.otf','FandolHei-Bold.otf','FandolKai-Regular.otf','FandolFang-Regular.otf']:
    if not (FONTS/font_name).is_file():
        raise SystemExit('缺少中文字体：'+font_name)
data = json.loads((BUILD / 'document.json').read_text(encoding='utf-8'))

# A vector cover plate. All typography is set by XeLaTeX.
c = canvas.Canvas(str(BUILD / 'cover_art.pdf'), pagesize=(176*mm,250*mm), pageCompression=1)
c.setTitle('Cover')
c.setAuthor('')
c.setFillColor(HexColor('#F7F5EF')); c.rect(0,0,176*mm,250*mm,fill=1,stroke=0)
c.setFillColor(HexColor('#193F4D')); c.rect(0,0,7*mm,250*mm,fill=1,stroke=0)
c.setStrokeColor(HexColor('#CFD7D3')); c.setLineWidth(.5)
for j in range(16):
    path=c.beginPath()
    for i in range(401):
        x=18+i*.43
        y=40+j*2.2+11*math.sin((x-18)/31+j*.065)*math.exp(-(x-84)**2/9000)
        (path.moveTo if i==0 else path.lineTo)(x*mm,y*mm)
    c.drawPath(path)
c.setStrokeColor(HexColor('#A07843')); c.setLineWidth(.8)
path=c.beginPath()
for i in range(401):
    x=18+i*.43; y=40+7*2.2+11*math.sin((x-18)/31+7*.065)*math.exp(-(x-84)**2/9000)
    (path.moveTo if i==0 else path.lineTo)(x*mm,y*mm)
c.drawPath(path)
for x in [40,77,121,153]:
    y=40+7*2.2+11*math.sin((x-18)/31+7*.065)*math.exp(-(x-84)**2/9000)
    c.setFillColor(HexColor('#A07843')); c.circle(x*mm,y*mm,1.1*mm,fill=1,stroke=0)
c.showPage(); c.save()

def esc(text):
    mapping = {'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_',
               '{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}',
               'Λ':r'\(\Lambda\)','β':r'\(\beta\)','α':r'\(\alpha\)','φ':r'\(\phi\)',
               '→':r'\(\to\)','≥':r'\(\ge\)','≤':r'\(\le\)', '−':'-'}
    return ''.join(mapping.get(ch,ch) for ch in text)

stats={'inline_math':0,'display_math':0,'tables':0,'links':0,'anchors':[],'chapters':0,'questions':0,'derivations':0,'diagrams':0}

def plain(inlines):
    out=''
    for item in inlines:
        t=item['t']; v=item.get('c')
        if t=='Str': out+=v
        elif t in ['Space','SoftBreak','LineBreak']:out+=' '
        elif t=='Math':out+=v[1]
        elif t=='Link':out+=plain(v[1])
        elif t in ['Emph','Strong','Span']:out+=plain(v[-1] if t=='Span' else v)
    return out

def inline(items):
    out=[]
    for item in items:
        t=item['t']; v=item.get('c')
        if t=='Str':out.append(esc(v))
        elif t in ['Space','SoftBreak']:out.append(' ')
        elif t=='LineBreak':out.append(r'\newline ')
        elif t=='Emph':out.append(r'\emph{'+inline(v)+'}')
        elif t=='Strong':out.append(r'\textbf{'+inline(v)+'}')
        elif t=='Math':
            if v[0]['t']=='DisplayMath':
                stats['display_math']+=1
                out.append('\n\\[\n'+re.sub(r'\n\s*\n', '\n', v[1])+'\n\\]\n')
            else:
                stats['inline_math']+=1
                out.append(r'\('+v[1]+r'\)')
        elif t=='Link':
            stats['links']+=1
            label=inline(v[1]); url=v[2][0]
            if url.startswith('#'):out.append(r'\hyperlink{'+url[1:]+'}{'+label+'}')
            else:out.append(r'\href{'+url.replace('%',r'\%').replace('#',r'\#')+'}{'+label+'}')
        elif t=='RawInline':
            if v[0]=='html':
                m=re.search(r'<a id="([^"]+)"',v[1])
                if m:
                    stats['anchors'].append(m[1]);out.append(r'\hypertarget{'+m[1]+'}{}')
            elif v[0]=='tex':out.append(v[1])
            else:raise ValueError(item)
        elif t=='Code':out.append(r'\texttt{'+esc(v[1])+'}')
        elif t=='Span':out.append(inline(v[1]))
        elif t=='Quoted':out.append('“'+inline(v[1])+'”')
        elif t=='Superscript':out.append(r'\textsuperscript{'+inline(v)+'}')
        elif t=='Subscript':out.append(r'\textsubscript{'+inline(v)+'}')
        else:raise ValueError(('inline',item))
    return ''.join(out)

def cell(blocks):
    return r'\par '.join(inline(b['c']) for b in blocks if b['t'] in ['Plain','Para'])

def table(block):
    stats['tables']+=1
    _,caption,specs,head,bodies,foot=block['c']
    headers=head[1][0][1]
    labels=[plain(c[-1][0]['c']) for c in headers]
    n=len(headers)
    if labels==['编号','资料','性质']:w=[.085,.755,.16]
    elif labels==['问题','对应文献编号','推导札记']:w=[.60,.27,.13]
    elif labels[0]=='篇章':w=[.23,.08,.34,.35]
    elif labels==['篇','章节导航']:w=[.09,.91]
    elif labels[0]=='年代':w=[.11,.21,.23,.31,.14]
    elif labels[0]=='方向' and n==5:w=[.12,.245,.235,.24,.16]
    elif labels[0]=='分支' and n==5:w=[.15,.21,.23,.26,.15]
    elif labels[0]=='方法' and n==5:w=[.14,.23,.20,.28,.15]
    elif n==5:w=[.17,.21,.23,.25,.14]
    elif n==4:w=[.18,.25,.28,.29]
    elif labels[0].startswith('误解') or (n==3 and labels[-1]=='正文与出处'):w=[.37,.48,.15]
    elif n==3 and labels[0]=='资料':w=[.32,.39,.29]
    elif n==3:w=[.27,.41,.32]
    else:w=[1/n]*n
    font='8.7'; leading='12.6'
    if labels[0]=='编号':font='9.1';leading='13.2'
    elif n==2:font='9.3';leading='13.8'
    cols='@{}'+''.join(r'>{\RaggedRight\arraybackslash}p{\dimexpr '+str(round(f,5))+r'\TableWidth\relax}' for f in w)+'@{}'
    rowhead=r'\rowcolor{TableHead} '+ ' & '.join(r'{\sffamily\bfseries\color{Ink} '+cell(c[-1])+'}' for c in headers)+r' \\'+'\n'+r'\midrule'+'\n'
    lines=[r'\par\begingroup',r'\setlength{\tabcolsep}{4pt}',r'\setlength{\TableWidth}{\dimexpr\linewidth-'+str(2*(n-1))+r'\tabcolsep\relax}',
           r'\fontsize{'+font+'}{'+leading+r'}\selectfont\setlength{\parskip}{0pt}\renewcommand{\arraystretch}{1.18}',
           r'\begin{longtable}{'+cols+'}',r'\toprule',rowhead,r'\endfirsthead',r'\toprule',rowhead,r'\endhead',
           r'\midrule\multicolumn{'+str(n)+r'}{r}{\scriptsize\color{Muted}续下页}\\',r'\endfoot',r'\bottomrule',r'\endlastfoot']
    count=0
    for body in bodies:
        for row in body[3]:
            count+=1
            if count%2==0:lines.append(r'\rowcolor{TableStripe}')
            lines.append(' & '.join(cell(c[-1]) for c in row[1])+r' \\'+'\n')
    lines += [r'\end{longtable}',r'\endgroup\par']
    return '\n'.join(lines)

diagram=r'''
\begin{center}
\resizebox{.96\linewidth}{!}{%
\begin{tikzpicture}[>=Stealth, node distance=1cm,
  box/.style={draw=Rule,fill=Paper,rounded corners=2pt,line width=.55pt,minimum height=.8cm,text width=2.5cm,align=center,font=\sffamily\small,inner sep=5pt},
  arr/.style={->,draw=Ink!65,line width=.7pt}]
\node[box] (D) at (-4,0) {热力学与统计};
\node[box] (A) at (0,0) {量子力学};
\node[box] (F) at (4,0) {广义相对论};
\node[box] (B) at (-4,-2) {多体与凝聚态};
\node[box] (C) at (0,-2) {量子场论};
\node[box] (E) at (-2.8,-4) {临界与重整化};
\node[box] (G) at (4,-4) {黑洞热力学};
\node[box] (H) at (-1.6,-6) {共形场论};
\node[box] (J) at (-5.2,-6) {纠缠与量子信息};
\node[box,fill=TableHead,draw=Ink!50] (I) at (1.2,-8.2) {全息对偶};
\draw[arr] (A) -- (B);
\draw[arr] (A) -- (C);
\draw[arr] (D) -- (B);
\draw[arr] (D.east) .. controls (-1.5,-.3) and (-1.2,-2.8) .. (E.north east);
\draw[arr] (B) -- (E);
\draw[<->,draw=Ink!65,line width=.7pt] (C) -- (E);
\draw[arr] (F) -- (G);
\draw[arr] (C) -- (G);
\draw[arr] (E) -- (H);
\draw[arr] (H) -- (I);
\draw[arr] (G) -- (I);
\draw[arr] (B.south west) .. controls (-5.3,-3.1) and (-5.4,-4.2) .. (J.north);
\draw[arr] (J.south) .. controls (-5.2,-8.4) and (-1.1,-8.3) .. (I.west);
\end{tikzpicture}}
\end{center}
'''

preamble=r'''
\documentclass[11pt,oneside,openany]{book}
\usepackage[paperwidth=176mm,paperheight=250mm,left=20mm,right=18mm,top=21mm,bottom=20mm,headheight=22pt,headsep=7mm,footskip=10mm]{geometry}
\usepackage{fontspec}
\usepackage{xeCJK}
\setmainfont{Latin Modern Roman}
\setsansfont{Latin Modern Sans}
\setmonofont{Latin Modern Mono}[Scale=.87]
\setCJKmainfont{FandolSong-Regular.otf}[Path=FONTDIR/,Script=Default,BoldFont=FandolSong-Bold.otf,ItalicFont=FandolKai-Regular.otf]
\setCJKsansfont{FandolHei-Regular.otf}[Path=FONTDIR/,Script=Default,BoldFont=FandolHei-Bold.otf]
\setCJKmonofont{FandolFang-Regular.otf}[Path=FONTDIR/,Script=Default]
\xeCJKsetup{PunctStyle=quanjiao,CJKecglue={\hskip .07em plus .04em minus .03em}}
\usepackage{amsmath,amssymb}
\usepackage{unicode-math}
\setmathfont{Latin Modern Math}
\usepackage[table]{xcolor}
\definecolor{Ink}{HTML}{193F4D}
\definecolor{Gold}{HTML}{A07843}
\definecolor{Muted}{HTML}{677779}
\definecolor{Rule}{HTML}{C7D1CE}
\definecolor{Paper}{HTML}{F7F5EF}
\definecolor{TableHead}{HTML}{E8EFEC}
\definecolor{TableStripe}{HTML}{F5F7F5}
\usepackage{graphicx,tikz,eso-pic}
\usetikzlibrary{arrows.meta,positioning,calc}
\usepackage{longtable,booktabs,array,ragged2e}
\usepackage{needspace,enumitem}
\usepackage[most]{tcolorbox}
\usepackage{titlesec,tocloft,fancyhdr}
\usepackage[unicode,colorlinks=true,linkcolor=Ink,urlcolor=Ink,bookmarksopen=true,bookmarksopenlevel=1,bookmarksdepth=1,pdfborder={0 0 0},pdfdisplaydoctitle=true]{hyperref}
\usepackage{bookmark}
\hypersetup{pdftitle={现代物理学史：问题、人物与分支},pdfauthor={},pdfsubject={现代物理学史},pdfkeywords={物理学史,量子理论,相对论,统计物理},pdfcreator={XeLaTeX}}
\setlength{\parindent}{0pt}
\setlength{\parskip}{5pt plus .5pt minus .5pt}
\raggedbottom
\setlength{\emergencystretch}{2em}
\tolerance=1800
\hyphenpenalty=400
\widowpenalty=9000
\clubpenalty=9000
\displaywidowpenalty=9000
\allowdisplaybreaks[2]
\setlength{\abovedisplayskip}{9pt plus 2pt minus 2pt}
\setlength{\belowdisplayskip}{9pt plus 2pt minus 2pt}
\setlist{topsep=4pt,itemsep=3pt,parsep=0pt,leftmargin=1.6em}
\newlength{\TableWidth}
\setlength{\LTpre}{6pt}
\setlength{\LTpost}{8pt}
\setlength{\heavyrulewidth}{.55pt}
\arrayrulecolor{Rule}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\sffamily\fontsize{8}{10}\selectfont\color{Muted}现代物理学史}
\fancyhead[R]{\sffamily\fontsize{8}{10}\selectfont\color{Muted}\leftmark}
\fancyfoot[R]{\sffamily\fontsize{9}{11}\selectfont\color{Ink}\thepage}
\renewcommand{\headrulewidth}{.35pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{Rule}\leaders\hrule height\headrulewidth\hfill}}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[R]{\sffamily\color{Ink}\thepage}\renewcommand{\headrulewidth}{0pt}}
\renewcommand{\contentsname}{目录}
\titleformat{\chapter}[display]{\sffamily\bfseries\color{Ink}\fontsize{23}{29}\selectfont}{}{0pt}{}
\titlespacing*{\chapter}{0pt}{0pt}{18pt}
\renewcommand{\cftpartfont}{\sffamily\bfseries\color{Ink}}
\renewcommand{\cftpartpagefont}{\sffamily\color{Ink}}
\renewcommand{\cftchapfont}{\normalfont}
\renewcommand{\cftchappagefont}{\normalfont}
\renewcommand{\cftchapleader}{\cftdotfill{\cftdotsep}}
\setlength{\cftbeforepartskip}{10pt}
\setlength{\cftbeforechapskip}{4.5pt}
\setlength{\cftchapindent}{1em}
\setcounter{tocdepth}{0}
\setcounter{secnumdepth}{-2}
\newif\ifafterpart
\newcommand{\PartBand}[1]{\clearpage\thispagestyle{plain}\phantomsection\addcontentsline{toc}{part}{#1}%
  {\sffamily\bfseries\color{Gold}\fontsize{11}{16}\selectfont #1\par}\vspace{3pt}{\color{Rule}\hrule}\vspace{17pt}\global\afterparttrue}
\newcommand{\Chapter}[4]{\ifafterpart\global\afterpartfalse\else\clearpage\fi\thispagestyle{plain}%
  \phantomsection#4\addcontentsline{toc}{chapter}{#1. #2}\markboth{#1\quad #3}{}%
  \noindent\begin{minipage}[t]{14mm}\vspace{0pt}{\sffamily\color{Gold}\fontsize{34}{39}\selectfont #1}\end{minipage}%
  \hfill\begin{minipage}[t]{\dimexpr\linewidth-18mm\relax}\vspace{0pt}{\sffamily\bfseries\color{Ink}\fontsize{18}{26}\selectfont #2\par}\end{minipage}\par\vspace{15pt}}
\newcommand{\Major}[3]{\clearpage\thispagestyle{plain}\phantomsection#3\addcontentsline{toc}{chapter}{#1}\markboth{#2}{}%
  {\sffamily\bfseries\color{Ink}\fontsize{21}{29}\selectfont #1\par}\vspace{5pt}{\color{Rule}\hrule}\vspace{13pt}}
\newcommand{\BookQuestion}[4]{\par\Needspace{6\baselineskip}\vspace{8pt}\phantomsection#3%
  \addcontentsline{toc}{section}{\texorpdfstring{#1\quad #2}{#1 #4}}%
  {\sffamily\bfseries\color{Ink}\fontsize{12.3}{18}\selectfont #1\quad #2\par}\nobreak\vspace{2pt}\nobreak}
\newcommand{\Minor}[2]{\par\Needspace{8\baselineskip}\vspace{7pt}\phantomsection#2%
  {\sffamily\bfseries\color{Ink}\fontsize{12}{17}\selectfont #1\par}\nobreak\vspace{2pt}\nobreak}
\newtcolorbox{derivation}[1]{enhanced,breakable,colback=Paper,colframe=Rule,boxrule=.35pt,arc=1pt,
  borderline west={1.6pt}{0pt}{Gold},left=9pt,right=9pt,top=7pt,bottom=7pt,
  before skip=12pt,after skip=10pt,pad at break*=5pt,
  fontupper=\fontsize{10.4}{16.7}\selectfont,
  title={#1},fonttitle=\sffamily\bfseries\fontsize{10.5}{16}\selectfont,
  coltitle=Ink,colbacktitle=Paper,detach title,before upper={\setlength{\parskip}{5pt}\tcbtitle\par\smallskip}}
\begin{document}
\pagenumbering{gobble}
\begin{titlepage}
\AddToShipoutPictureBG*{\AtPageLowerLeft{\includegraphics[width=\paperwidth,height=\paperheight]{cover_art.pdf}}}
\vspace*{29mm}
{\sffamily\color{Muted}\fontsize{9}{13}\selectfont HISTORY OF MODERN PHYSICS\par}
\vspace{10mm}
{\sffamily\bfseries\color{Ink}\fontsize{32}{44}\selectfont 现代物理学史\par}
\vspace{4mm}
{\sffamily\color{Ink}\fontsize{15}{22}\selectfont 问题、人物与分支\par}
\vspace{13mm}
{\color{Gold}\rule{20mm}{.9pt}\par}
\vspace{5mm}
{\color{Muted}\fontsize{10.5}{18}\selectfont 从场与量子，到物态、宇宙与信息\par}
\vfill
{\sffamily\color{Muted}\fontsize{9}{14}\selectfont 公开讨论稿\hfill 2026.09\par}
\end{titlepage}
\clearpage\pagenumbering{roman}\markboth{目录}{}
{\fontsize{10.3}{15.5}\selectfont\tableofcontents}
\clearpage\pagenumbering{arabic}
\fontsize{11}{17.6}\selectfont
\Major{导读}{导读}{}
'''.replace('FONTDIR',FONTS.as_posix())

preamble=preamble.replace('2026.09',esc(plain(data['meta']['date']['c'])[:7].replace('-','.')))
preamble=preamble.replace('公开讨论稿',esc(plain(data['meta']['version']['c'])))

body=[]
pending=[]
in_derivation=False
appendix=''

def anchors_tex():
    global pending
    value=''.join(r'\hypertarget{'+a+'}{}' for a in pending)
    pending=[]
    return value

def end_derivation():
    global in_derivation
    if in_derivation:
        body.append(r'\end{derivation}')
        in_derivation=False

for b in data['blocks']:
    t=b['t'];v=b.get('c')
    if t=='Header':
        end_derivation()
        level,attributes,items=v
        title=plain(items)
        if level==1:continue
        if level==2 and re.match(r'第[一二三四五六七]篇',title):
            body.append(r'\PartBand{'+inline(items)+'}'+anchors_tex())
        elif level==3 and re.match(r'\d+\.',title):
            m=re.match(r'(\d+)\.\s*(.*)',title)
            stats['chapters']+=1
            body.append(r'\Chapter{'+m[1]+'}{'+esc(m[2])+'}{'+esc(m[2].split('：')[0])+'}{'+anchors_tex()+'}')
        elif level==2 and title.startswith('附录'):
            appendix=title[2]
            body.append(r'\bookmarksetup{startatroot}')
            body.append(r'\Major{'+inline(items)+'}{附录 '+appendix+'}{'+anchors_tex()+'}')
        elif level==4:
            m=re.match(r'(\d+\.\d+)\s+(.*)',title)
            stats['questions']+=1
            if m[1] in ['5.5','17.5']:
                body.append(r'\clearpage')
            pdf_title=m[2].replace('&',r'\&').replace('%',r'\%').replace('_',r'\_')
            body.append(r'\BookQuestion{'+m[1]+'}{'+esc(m[2])+'}{'+anchors_tex()+'}{'+pdf_title+'}')
        elif level==5:
            stats['derivations']+=1
            body.append(r'\par\Needspace{6\baselineskip}'+anchors_tex()+r'\begin{derivation}{'+inline(items)+'}')
            in_derivation=True
        else:
            # Appendix source headings remain compact; page breaks are controlled by Needspace.
            body.append(r'\Minor{'+inline(items)+'}{'+anchors_tex()+'}')
    elif t in ['Para','Plain']:
        if all(i['t']=='RawInline' and i['c'][0]=='html' for i in v):
            for item in v:
                m=re.search(r'<a id="([^"]+)"',item['c'][1])
                if m:
                    stats['anchors'].append(m[1]);pending.append(m[1])
            continue
        body.append(anchors_tex()+inline(v)+'\n\n')
    elif t=='Table':
        body.append(anchors_tex()+table(b))
    elif t=='CodeBlock':
        assert 'mermaid' in v[0][1]
        expected_diagram = 'flowchart TD\n    A["量子力学"] --> B["多体与凝聚态"]\n    A --> C["量子场论"]\n    D["热力学与统计"] --> B\n    D --> E["临界与重整化"]\n    B --> E\n    C <--> E\n    F["广义相对论"] --> G["黑洞热力学"]\n    C --> G\n    E --> H["共形场论"]\n    H --> I["全息对偶"]\n    G --> I\n    B --> J["纠缠与量子信息"]\n    J --> I\n'
        if v[1].strip() != expected_diagram.strip():
            raise ValueError('分支图已修改，请同步更新 scripts/render_latex.py 中的 TikZ 图，再生成 PDF。')
        stats['diagrams']+=1
        body.append(diagram)
    elif t=='OrderedList':
        body.append(r'\begin{enumerate}')
        for item in v[1]:body.append(r'\item '+cell(item))
        body.append(r'\end{enumerate}')
    elif t=='BulletList':
        body.append(r'\begin{itemize}')
        for item in v:body.append(r'\item '+cell(item))
        body.append(r'\end{itemize}')
    elif t=='HorizontalRule':body.append(r'\par\medskip{\color{Rule}\hrule}\medskip')
    else:raise ValueError(('block',t))
end_derivation()
assert not pending
assert len(stats['anchors'])==len(set(stats['anchors'])), '出现重复的内部锚点'
(BUILD/'book.tex').write_text(preamble+'\n'.join(body)+'\n\\end{document}\n',encoding='utf-8')
(BUILD/'conversion_report.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:(len(v) if k=='anchors' else v) for k,v in stats.items()},ensure_ascii=False))
