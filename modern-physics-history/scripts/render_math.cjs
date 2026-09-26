/* Pre-render TeX to self-contained SVG. No browser-side MathJax is needed. */
const fs = require('fs');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');
const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: AllPackages.filter(p => !['autoload','require'].includes(p)),
  formatError: (jax, error) => { throw error; }});
const svg = new SVG({fontCache: 'local'});
const doc = mathjax.document('', {InputJax: tex, OutputJax: svg});
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
try {
  const html = input.map((item, i) => {
    try {
      const node = doc.convert(item.tex, {display:item.display, em:16, ex:8, containerWidth:1000});
      const result = adaptor.outerHTML(node);
      if (result.includes('data-mml-node="merror"')) throw new Error('MathJax returned an error node');
      return result;
    } catch (error) { throw new Error(`Formula ${i + 1}: ${error.message}\n${item.tex}`); }
  });
  process.stdout.write(JSON.stringify({html, css:adaptor.textContent(svg.styleSheet(doc))}));
} catch (error) { console.error(error.message); process.exit(1); }
