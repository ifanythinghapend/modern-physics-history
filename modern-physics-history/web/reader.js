(() => {
  const pages=[...document.querySelectorAll('.reading-page')];
  const sidebar=document.getElementById('sidebar');
  const toggle=document.getElementById('menu-toggle');
  const input=document.getElementById('search');
  const panel=document.getElementById('search-panel');
  const results=document.getElementById('search-results');
  const rows=JSON.parse(document.getElementById('book-index').textContent);
  const normalized=rows.map(row => (row[1]+' '+row[2]).normalize('NFKC').toLowerCase());
  const closeMenu=()=>{document.body.classList.remove('nav-open');toggle.setAttribute('aria-expanded','false');};
  function navigate(){
    let id;
    try{id=decodeURIComponent(location.hash.slice(1))||'start';}catch{id='start';}
    const target=document.getElementById(id)||document.getElementById('start');
    const current=target.closest('.reading-page')||document.getElementById('start');
    pages.forEach(page=>{const active=page===current;page.classList.toggle('is-current',active);page.hidden=!active;});
    const heading=current.querySelector('h1');
    document.title=current.id==='start'?'现代物理学史 · 问题、人物与分支':heading.textContent+' · 现代物理学史';
    sidebar.querySelectorAll('a').forEach(link=>{
      const exact=link.hash==='#'+id;
      const named=document.getElementById(link.hash.slice(1));
      const active=exact || (!id.startsWith('derivation-') && named && named.closest('.reading-page')===current && /^#(chapter-|appendix-)/.test(link.hash));
      link.classList.toggle('active',!!active);
      if(active){link.setAttribute('aria-current','page');const group=link.closest('details');if(group)group.open=true;}
      else link.removeAttribute('aria-current');
    });
    closeMenu();panel.hidden=true;
    requestAnimationFrame(()=>{
      if(target===current || target.id==='start')window.scrollTo(0,0);
      else target.scrollIntoView({block:'start'});
    });
  }
  toggle.addEventListener('click',()=>{const open=document.body.classList.toggle('nav-open');toggle.setAttribute('aria-expanded',String(open));});
  document.querySelector('.scrim').addEventListener('click',closeMenu);
  window.addEventListener('hashchange',navigate);
  document.addEventListener('click',event=>{
    const link=event.target.closest('a[href^="#"]');
    if(link && link.getAttribute('href')==='#main'){event.preventDefault();document.getElementById('main').focus();return;}
    if(link && link.getAttribute('href')===location.hash)navigate();
  });
  document.getElementById('back-top').addEventListener('click',()=>window.scrollTo({top:0,behavior:'auto'}));
  const hideSearch=()=>{panel.hidden=true;input.value='';input.focus();};
  document.getElementById('close-search').addEventListener('click',hideSearch);
  document.addEventListener('keydown',event=>{if(event.key==='Escape'){panel.hidden=true;closeMenu();}});
  input.addEventListener('input',()=>{
    const query=input.value.normalize('NFKC').toLowerCase().trim();
    if(!query){panel.hidden=true;return;}
    const terms=query.split(/\s+/);const matches=[];
    normalized.forEach((text,i)=>{if(terms.every(term=>text.includes(term)))matches.push(i);});
    const rank=i=>10*Number(rows[i][1].toLowerCase().includes(query))+(/^q-/.test(rows[i][0])?3:/^derivation-/.test(rows[i][0])?2:/^ref-/.test(rows[i][0])?1:0);
    matches.sort((a,b)=>rank(b)-rank(a));
    results.replaceChildren();panel.hidden=false;
    document.getElementById('search-count').textContent=`找到 ${matches.length} 项`+(matches.length>24?'，显示前 24 项':'');
    for(const i of matches.slice(0,24)){
      const row=rows[i];const link=document.createElement('a');link.href='#'+row[0];link.className='search-result';
      const title=document.createElement('strong');title.textContent=row[1];
      const excerpt=document.createElement('span');const pos=row[2].toLowerCase().indexOf(terms[0]);const start=Math.max(0,pos-30);
      excerpt.textContent=(start?'…':'')+row[2].slice(start,start+125)+(row[2].length>start+125?'…':'');
      link.append(title,excerpt);results.append(link);
    }
    if(!matches.length){const empty=document.createElement('p');empty.className='search-empty';empty.textContent='没有找到。可以换用人名、章节主题或更短的关键词。';results.append(empty);}
  });
  // Repository links are derived only when viewed on the standard GitHub Pages domain.
  if(location.hostname.endsWith('.github.io')){
    const owner=location.hostname.slice(0,-10);const parts=location.pathname.split('/').filter(Boolean);
    const name=parts.length && parts[0]!=='index.html'?parts[0]:location.hostname;
    if(/^[A-Za-z0-9_.-]+$/.test(owner)&&/^[A-Za-z0-9_.-]+$/.test(name)){
      const repo='https://github.com/'+owner+'/'+name;document.body.classList.add('online');
      document.querySelectorAll('.repo-link').forEach(link=>link.href=repo);
      document.querySelectorAll('.issue-link').forEach(link=>link.href=repo+'/issues/new/choose');
    }
  }
  navigate();
})();
