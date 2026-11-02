(() => {
  'use strict';
  const lang = document.body.dataset.lang;
  const root = document.body.dataset.root;
  const dialog = document.getElementById('search-dialog');
  const input = document.getElementById('search-input');
  const results = document.getElementById('search-results');
  const status = document.getElementById('search-count');
  const entries = (window.RSI_SEARCH || []).filter(item => item.lang === lang);
  const labels = lang === 'zh' ? {count:'篇结果', empty:'没有匹配的文章，请尝试其他词。', all:'篇文献解读'} : {count:'results', empty:'No matching articles. Try another term.', all:'literature notes'};
  let previousFocus;
  function renderResults() {
    const query = input.value.trim().toLocaleLowerCase();
    const terms = query.split(/\s+/).filter(Boolean);
    const matched = entries.map(entry => {
      const title = entry.title.toLocaleLowerCase();
      const text = `${entry.title} ${entry.paper} ${entry.text}`.toLocaleLowerCase();
      return {entry, score: terms.every(term => text.includes(term)) ? terms.reduce((score,term) => score + (title.includes(term) ? 8 : 1), 0) + 1 : 0};
    }).filter(x => x.score).sort((a,b) => b.score - a.score);
    status.textContent = matched.length ? `${matched.length} ${query ? labels.count : labels.all}` : labels.empty;
    results.replaceChildren();
    for (const {entry} of matched) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.href = `${root}${lang}/articles/${entry.slug}.html`;
      const title = document.createElement('span'); title.className='result-title'; title.textContent=entry.title;
      const category = document.createElement('span'); category.className='result-category'; category.textContent=entry.category;
      const excerpt = document.createElement('span'); excerpt.className='result-excerpt';
      const hit = terms.length ? Math.max(0, entry.text.toLocaleLowerCase().indexOf(terms[0]) - 55) : 0;
      excerpt.textContent = (hit ? '…' : '') + entry.text.slice(hit,hit+170) + '…';
      link.append(title,category,excerpt);item.append(link);results.append(item);
    }
  }
  function openSearch() {
    previousFocus = document.activeElement;
    renderResults(); dialog.showModal(); input.focus();
  }
  document.querySelector('.search-open').addEventListener('click',openSearch);
  input.addEventListener('input',renderResults);
  input.addEventListener('keydown',event => {
    if (event.key==='ArrowDown') {event.preventDefault();results.querySelector('a')?.focus();}
  });
  dialog.addEventListener('close',() => previousFocus?.focus());
  dialog.addEventListener('click',event => {if(event.target===dialog){const b=dialog.getBoundingClientRect();if(event.clientX<b.left||event.clientX>b.right||event.clientY<b.top||event.clientY>b.bottom)dialog.close();}});
  document.addEventListener('keydown',event => {
    const typing = /INPUT|TEXTAREA|SELECT/.test(document.activeElement?.tagName) || document.activeElement?.isContentEditable;
    if ((event.key==='/' && !typing) || ((event.ctrlKey||event.metaKey) && event.key.toLowerCase()==='k')) {event.preventDefault();if(!dialog.open)openSearch();}
  });
  const languageSwitch=document.querySelector('.language-switch');
  languageSwitch.addEventListener('click',() => {const target=new URL(languageSwitch.href);target.hash=location.hash;languageSwitch.href=target.href;});
  document.querySelectorAll('.mobile-toc a').forEach(link=>link.addEventListener('click',()=>link.closest('details').open=false));
  if ('IntersectionObserver' in window) {
    const links = [...document.querySelectorAll('.page-toc a')];
    const observer = new IntersectionObserver(changes => {
      for (const change of changes) if(change.isIntersecting)links.forEach(link=>link.classList.toggle('active',link.hash===`#${change.target.id}`));
    },{rootMargin:'-10% 0px -70% 0px'});
    document.querySelectorAll('.prose h2,.library-section').forEach(h=>observer.observe(h));
  }
})();
