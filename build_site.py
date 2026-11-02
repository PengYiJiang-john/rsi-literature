#!/usr/bin/env python3
"""Build a bilingual, offline-readable literature site from maintained sources."""
from __future__ import annotations
import argparse
import html
import json
import re
import shutil
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DIST = HERE / 'dist'
LANGS = ('en', 'zh')
CATEGORIES = {
 'value': {'en':'Value and evaluation', 'zh':'价值与评价'},
 'epistemic': {'en':'Knowledge and interaction', 'zh':'认识与交互'},
 'learning': {'en':'Learning mechanisms', 'zh':'学习机制'},
 'feedback': {'en':'Feedback and learning dynamics', 'zh':'反馈与学习动力学'},
}
DESCRIPTIONS = {
 'value': {'en':'What makes a change better? Goals, rewards and the decision to modify oneself.', 'zh':'凭什么判断修改更好？区分最终目标、训练奖励与自修改的决策。'},
 'epistemic': {'en':'How does evidence become usable? Information, representations, tools and world models.', 'zh':'怎样获得并理解证据？连接信息、表示、工具与世界模型。'},
 'learning': {'en':'How can learning improve later learning? Updates, memory, architecture and improvers.', 'zh':'怎样让下一轮更会学习？比较更新规则、记忆、架构与改进程序。'},
 'feedback': {'en':'Why can the same feedback loop support progress, sustain error or lose information?', 'zh':'为什么反馈闭环既能支持进步，也会维持错误或丢失信息？'},
}
LABELS = {
 'en': {'overview':'Review', 'library':'Reading map', 'search':'Search articles', 'search_hint':'Title, concept, or paper', 'toc':'On this page', 'related':'Continue reading', 'source':'Original paper', 'topic':'Cross-cutting topic', 'article':'Literature note', 'skip':'Skip to content', 'download':'Download the review', 'plain':'Plain PDF', 'linked':'Linked PDF', 'all':'All articles', 'results':'results', 'empty':'No matching articles. Try another term.', 'close':'Close', 'menu':'Contents', 'back':'Back to reading map', 'reading':'min read', 'footer':'RSI, Feedback and Learning Dynamics', 'intro':'A literature review connecting classic theory with modern systems that modify their goals, interaction, and learning mechanisms.', 'open':'Read the review', 'explore':'Explore the literature', 'theme':'One feedback problem, several mechanisms', 'theme_text':'Action selection shapes evidence; representations shape what evidence can correct; learning rules shape whether correction takes hold.', 'zh':'Chinese', 'en':'English'},
 'zh': {'overview':'主综述', 'library':'阅读地图', 'search':'搜索文章', 'search_hint':'标题、概念或文献', 'toc':'本文目录', 'related':'接着阅读', 'source':'原论文', 'topic':'贯通主题', 'article':'文献解读', 'skip':'跳到正文', 'download':'下载主综述', 'plain':'纯净版 PDF', 'linked':'链接版 PDF', 'all':'全部文章', 'results':'篇结果', 'empty':'没有匹配的文章，请尝试其他词。', 'close':'关闭', 'menu':'目录', 'back':'返回阅读地图', 'reading':'分钟', 'footer':'RSI、反馈与学习动力学', 'intro':'从经典理论到现代自修改系统，围绕价值、认识与学习机制，理解反馈为何支持进步，也可能维持错误。', 'open':'阅读主综述', 'explore':'查看文献地图', 'theme':'同一个反馈问题，不同的形成机制', 'theme_text':'行动决定接触哪些证据，表示决定能读出什么差别，学习规则决定这些差别能否带来纠正。', 'zh':'中文', 'en':'英文'},
}

def esc(x): return html.escape(str(x), quote=True)
def read_json(path): return json.loads(path.read_text(encoding='utf-8'))
def title_of(text): return re.search(r'^#\s+(.+)$', text, re.M).group(1).strip()
def plain(text):
    text = re.sub(r'```[\s\S]*?```', ' ', text)
    text = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return re.sub(r'[#*_`>|\n]+', ' ', text).strip()

def snapshot(source):
    target = HERE / 'sources'
    if source.resolve() == target.resolve(): return target
    target.mkdir(exist_ok=True)
    for name in ('document_registry.json','content.json','content.en.json'):
        shutil.copy2(source/name, target/name)
    for name in ('cards','topics','translations/en/cards','translations/en/topics'):
        src, dest = source/name, target/name
        dest.mkdir(parents=True, exist_ok=True)
        for p in src.glob('*.md'): shutil.copy2(p,dest/p.name)
    (target/'downloads').mkdir(exist_ok=True)
    for lang in LANGS:
        for variant in ('plain','linked'):
            pdf=source/'exports'/f'{lang}_{variant}'/'review.pdf'
            if pdf.exists():shutil.copy2(pdf,target/'downloads'/f'rsi-review-{lang}-{variant}.pdf')
    return target

def source_documents(source):
    registry = read_json(source/'document_registry.json')
    docs = registry['documents'] + registry.get('topics',[])
    by_slug = {}
    for d in docs:
        entry = dict(d); entry['body']={}; entry['titles']={}
        for lang in LANGS:
            path = source/d['source_path'] if lang=='zh' else source/'translations/en'/d['source_path']
            if not path.exists(): raise RuntimeError(f'Missing translation: {path}')
            body = path.read_text(encoding='utf-8')
            entry['body'][lang]=body; entry['titles'][lang]=title_of(body)
        by_slug[d['slug']]=entry
    return by_slug

def local_links(text, lang, prefix, docs):
    def custom(m):
        slug,label=m.group(1),m.group(2)
        if slug not in docs: raise RuntimeError(f'Unknown document {slug}')
        return f'[{label}]({prefix}{lang}/articles/{slug}.html)'
    text=re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]',custom,text)
    def md(m):
        label,path=m.group(1),m.group(2)
        if path.startswith(('https:','http:','mailto:','#')):return m.group(0)
        target,_,fragment=path.partition('#')
        if target.endswith('.md'):
            slug=Path(target).stem
            if slug not in docs:raise RuntimeError(f'Unknown markdown link: {path}')
            return f'[{label}]({prefix}{lang}/articles/{slug}.html'+(f'#{fragment}' if fragment else '')+')'
        return m.group(0)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)',md,text)

def render_markdown(text, lang, prefix, docs):
    text=local_links(text,lang,prefix,docs)
    formulas=[]
    def mathblock(m):
        tex=m.group(1).strip(); i=len(formulas);formulas.append(tex)
        return f'\n\nRSIMATHPLACEHOLDER{i}END\n\n'
    text=re.sub(r'```math\s*\n([\s\S]*?)\n```',mathblock,text)
    result=subprocess.run(['pandoc','--from=markdown','--to=html5','--wrap=none','--mathml'],input=text,text=True,capture_output=True,check=True).stdout
    for i,tex in enumerate(formulas):
        result=result.replace(f'<p>RSIMATHPLACEHOLDER{i}END</p>',render_math(tex))
    # Stable, language-independent heading anchors preserve position on language switch.
    counter=[0];toc=[]
    def headings(m):
        counter[0]+=1; ident=f'section-{counter[0]}'
        label=re.sub('<[^>]+>','',m.group(1))
        toc.append((ident,html.unescape(label)))
        return f'<h2 id="{ident}">{m.group(1)}</h2>'
    result=re.sub(r'<h2(?:\s+[^>]*)?>(.*?)</h2>',headings,result)
    result=re.sub(r'<a href="(https?://[^"]+)"',r'<a rel="noopener noreferrer" href="\1"',result)
    result=result.replace('<table>','<div class="table-wrap"><table>').replace('</table>','</table></div>')
    return result,toc

MATH_CACHE={}
def render_math(tex):
    if tex in MATH_CACHE:return MATH_CACHE[tex]
    result=subprocess.run(['pandoc','--from=markdown','--to=html5','--mathml'],input='$$\n'+tex+'\n$$',text=True,capture_output=True,check=True).stdout
    if '<math' not in result:raise RuntimeError(f'Could not render math: {tex}')
    value='<div class="equation">'+result+'</div>'
    MATH_CACHE[tex]=value;return value

def header(lang,prefix,page_path):
    L=LABELS[lang];other='zh' if lang=='en' else 'en'
    return f'''<a class="skip-link" href="#main">{L['skip']}</a>
<header class="site-header"><a class="brand" href="{prefix}{lang}/index.html"><span class="brand-mark" aria-hidden="true">R</span><span>RSI <span class="brand-detail">/ Literature</span></span></a>
<nav class="top-nav" aria-label="{'Primary navigation' if lang=='en' else '主导航'}"><a href="{prefix}{lang}/review.html">{L['overview']}</a><a href="{prefix}{lang}/library.html">{L['library']}</a></nav>
<div class="header-actions"><button class="search-open" type="button" aria-label="{L['search']}" aria-haspopup="dialog" aria-controls="search-dialog"><svg viewBox="0 0 24 24" width="19" height="19" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><circle cx="10.5" cy="10.5" r="6.5"/><path d="m16 16 5 5"/></svg><span>{L['search']}</span><kbd>/</kbd></button><a class="language-switch" lang="{other}" hreflang="{other}" href="{prefix}{other}/{page_path}">{'中文' if other=='zh' else 'EN'}</a></div></header>'''

def downloads(lang,prefix):
    L=LABELS[lang]
    links=''.join(f'<a href="{prefix}downloads/rsi-review-{code}-{variant}.pdf" download><span>{L[code]} · {L[variant]}</span><span aria-hidden="true">↓</span></a>' for code in LANGS for variant in ('plain','linked'))
    return f'<section class="downloads" id="downloads"><h2>{L["download"]}</h2><div class="download-grid">{links}</div></section>'

def shell(lang,prefix,page_path,title,body,toc=None):
    L=LABELS[lang]
    toc_html=''
    if toc:
        toc_html=f'<aside class="page-toc"><nav aria-label="{L["toc"]}"><span class="toc-label">{L["toc"]}</span>'+''.join(f'<a href="#{ident}">{esc(label)}</a>' for ident,label in toc)+'</nav></aside>'
    mobile_toc=f'<details class="mobile-toc"><summary>{L["toc"]}</summary>'+''.join(f'<a href="#{i}">{esc(t)}</a>' for i,t in toc or [])+'</details>' if toc else ''
    return f'''<!doctype html><html lang="{'zh-CN' if lang=='zh' else 'en'}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light"><title>{esc(title)} · RSI Literature</title><meta name="description" content="{esc(L['intro'])}"><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/styles.css"><script src="{prefix}assets/search-index.js" defer></script><script src="{prefix}assets/app.js" defer></script></head>
<body data-lang="{lang}" data-root="{prefix}">{header(lang,prefix,page_path)}<div class="page-layout {'with-toc' if toc else ''}"><main id="main">{mobile_toc}{body}</main>{toc_html}</div>
<footer class="site-footer"><span>{L['footer']}</span><span><a href="{prefix}{lang}/library.html">{L['library']}</a><span class="footer-dot">·</span><a href="{prefix}{lang}/index.html#downloads">PDF</a></span></footer>
<dialog id="search-dialog" aria-labelledby="search-title"><form method="dialog" class="search-heading"><h2 id="search-title">{L['search']}</h2><button aria-label="{L['close']}">×</button></form><label class="sr-only" for="search-input">{L['search']}</label><input id="search-input" type="search" autocomplete="off" placeholder="{L['search_hint']}"><p id="search-count" role="status" aria-live="polite"></p><ul id="search-results"></ul></dialog></body></html>'''

def article_list(docs,lang,prefix,category=None):
    entries=[d for d in docs.values() if not category or d['category']==category]
    if category=='feedback': entries.sort(key=lambda d:(d['slug']!='feedback',d.get('ref_id',0)))
    return '<ul class="article-list">'+''.join(f'<li><a href="{prefix}{lang}/articles/{d["slug"]}.html"><span>{esc(d["titles"][lang])}</span><span class="arrow" aria-hidden="true">↗</span></a><p>{esc(d.get("paper_title",LABELS[lang]["topic"]))}</p></li>' for d in entries)+'</ul>'

def make_home(docs,lang):
    L=LABELS[lang];prefix='../'
    cards=''.join(f'<a class="category-card" href="library.html#{cat}"><span class="category-number">0{i+1}</span><h2>{CATEGORIES[cat][lang]}</h2><p>{DESCRIPTIONS[cat][lang]}</p><span class="category-cta" aria-hidden="true">↗</span></a>' for i,cat in enumerate(('value','epistemic','learning')))
    title='RSI, Feedback and Learning Dynamics' if lang=='en' else 'RSI、反馈与学习动力学'
    headline='How does a system<br>learn to improve itself?' if lang=='en' else '系统如何学会<br>改进自身？'
    body=f'''<section class="hero"><p class="eyebrow">LITERATURE REVIEW · 2026</p><h1>{headline}</h1><p class="hero-description">{L['intro']}</p><div class="hero-actions"><a class="button-primary" href="review.html">{L['open']} <span aria-hidden="true">→</span></a><a class="text-action" href="library.html">{L['explore']}</a></div></section><section class="category-grid" aria-label="{'Three perspectives' if lang=='en' else '三类研究'}">{cards}</section><section class="theme-band"><div><p class="eyebrow">{'CONNECTING THE THREE PERSPECTIVES' if lang=='en' else '贯通三类研究'}</p><h2>{L['theme']}</h2><p>{L['theme_text']}</p></div><a href="articles/feedback.html">{esc(docs['feedback']['titles'][lang])}<span aria-hidden="true">→</span></a></section>{downloads(lang,prefix)}'''
    return shell(lang,prefix,'index.html',title,body)

def make_library(docs,lang):
    L=LABELS[lang];toc=[(cat,CATEGORIES[cat][lang]) for cat in CATEGORIES]
    sections=''.join(f'<section class="library-section" id="{cat}"><div class="section-heading"><span class="section-number">{i+1:02}</span><div><h2>{CATEGORIES[cat][lang]}</h2><p>{DESCRIPTIONS[cat][lang]}</p></div></div>{article_list(docs,lang,"../",cat)}</section>' for i,cat in enumerate(CATEGORIES))
    body=f'<header class="reading-header"><p class="eyebrow">LITERATURE MAP</p><h1>{L["library"]}</h1><p class="standfirst">{L["intro"]}</p></header>{sections}'
    return shell(lang,'../','library.html',L['library'],body,toc)

def make_article(d,docs,lang):
    prefix='../../';L=LABELS[lang]
    markdown=re.sub(r'^#\s+.+\n','',d['body'][lang],count=1)
    rendered,toc=render_markdown(markdown,lang,prefix,docs)
    count=len(plain(markdown)) if lang=='zh' else len(plain(markdown).split())
    minutes=max(1,round(count/(480 if lang=='zh' else 210)))
    source=f'<a class="source-link" href="{esc(d["paper_url"])}" rel="noopener noreferrer">{L["source"]} ↗</a>' if d.get('paper_url') else ''
    related=[s for s in d.get('related',[]) if s in docs]
    related_html=f'<section class="related-reading"><h2>{L["related"]}</h2><div>'+''.join(f'<a href="{s}.html">{esc(docs[s]["titles"][lang])}<span aria-hidden="true">→</span></a>' for s in related)+'</div></section>' if related else ''
    body=f'<a class="back-link" href="../library.html#{d["category"]}">← {L["back"]}</a><article><header class="reading-header"><p class="eyebrow">{CATEGORIES[d["category"]][lang]}</p><h1>{esc(d["titles"][lang])}</h1><div class="article-meta"><span>{L["topic"] if d["slug"]=="feedback" else L["article"]}</span><span>{minutes} {L["reading"]}</span>{source}</div></header><div class="prose">{rendered}</div>{related_html}</article>'
    return shell(lang,prefix,f'articles/{d["slug"]}.html',d['titles'][lang],body,toc)

def make_review(source,docs,lang):
    content=read_json(source/('content.json' if lang=='zh' else 'content.en.json'))
    chunks=[]
    for page in content['pages']:
        # The PDF's reference index is replaced by the site's complete reading map.
        if any(b['type']=='references' for b in page['blocks']):continue
        if page.get('title'):chunks.append('## '+page['title'])
        for b in page['blocks']:
            if b['type']=='heading':chunks.append(('### ' if page.get('title') else '## ')+b['text'])
            elif b['type'] in ('p','note'):chunks.append(b['text'])
            elif b['type']=='equation':
                if 'tex' in b:tex=b['tex']
                elif 'nodes' in b:tex=''.join(equation_node(n) for n in b['nodes'])
                else:raise RuntimeError('Review equation requires structured nodes or a tex field.')
                chunks.append('```math\n'+tex+'\n```')
            elif b['type']=='table':
                chunks.append('| '+' | '.join(b['headers'])+' |\n| '+' | '.join(['---']*len(b['headers']))+' |\n'+'\n'.join('| '+' | '.join(row)+' |' for row in b['rows']))
    rendered,toc=render_markdown('\n\n'.join(chunks),lang,'../',docs)
    L=LABELS[lang]
    body=f'<article><header class="reading-header"><p class="eyebrow">LITERATURE REVIEW</p><h1>{esc(content["title"])}</h1><p class="standfirst">{esc(content["subtitle"])}</p></header><div class="prose">{rendered}</div></article>{downloads(lang,"../")}'
    return shell(lang,'../','review.html',content['title'],body,toc)

def equation_node(node):
    """Translate the review's editable equation tree without duplicating formulas."""
    if isinstance(node,str):
        symbols={'𝒱':r'\mathcal{V}','Θ':r'\Theta ','ρ':r'\rho ','θ':r'\theta ','∈':r'\in ','∼':r'\sim ','∥':r'\Vert ','·':r'\cdot ','−':'-','|':r'\mid '}
        names={'argmax':r'\operatorname*{argmax}','argmin':r'\operatorname*{argmin}','inf':r'\inf','log':r'\log','KL':r'\mathrm{KL}','E':r'\mathbb{E}'}
        text=''.join(symbols.get(c,c) for c in node)
        return re.sub(r'\b(argmax|argmin|inf|log|KL|E)\b',lambda m:names[m.group(1)],text)
    for key,op in [('sub','_'),('sup','^')]:
        if key in node:
            base,index=node[key]
            return '{'+equation_node(base)+'}'+op+'{'+equation_node(index)+'}'
    raise RuntimeError(f'Unsupported equation node: {node}')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,help='Maintained project root; snapshots sources for future standalone builds.');args=parser.parse_args()
    source=args.source or (HERE/'sources' if (HERE/'sources/document_registry.json').exists() else HERE.parent)
    source=snapshot(source)
    docs=source_documents(source)
    DIST.mkdir(exist_ok=True);(DIST/'downloads').mkdir(exist_ok=True)
    shutil.copytree(HERE/'assets',DIST/'assets',dirs_exist_ok=True)
    for lang in LANGS:
        for variant in ('plain','linked'):
            name=f'rsi-review-{lang}-{variant}.pdf';pdf=source/'downloads'/name
            if not pdf.exists():raise RuntimeError(f'Missing PDF in source snapshot: {pdf}')
            shutil.copy2(pdf,DIST/'downloads'/name)
    search=[]
    for lang in LANGS:
        base=DIST/lang;(base/'articles').mkdir(parents=True,exist_ok=True)
        (base/'index.html').write_text(make_home(docs,lang),encoding='utf-8')
        (base/'library.html').write_text(make_library(docs,lang),encoding='utf-8')
        (base/'review.html').write_text(make_review(source,docs,lang),encoding='utf-8')
        for d in docs.values():
            (base/'articles'/f'{d["slug"]}.html').write_text(make_article(d,docs,lang),encoding='utf-8')
            search.append({'lang':lang,'slug':d['slug'],'title':d['titles'][lang],'category':CATEGORIES[d['category']][lang],'text':plain(d['body'][lang]),'paper':d.get('paper_title','')})
    (DIST/'assets/search-index.js').write_text('window.RSI_SEARCH = '+json.dumps(search,ensure_ascii=False).replace('</','<\\/')+';\n',encoding='utf-8')
    (DIST/'index.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta http-equiv="refresh" content="0;url=en/index.html"><title>RSI Literature</title></head><body><a href="en/index.html">Read the literature review in English</a> · <a href="zh/index.html">中文</a></body></html>',encoding='utf-8')
    (DIST/'.nojekyll').write_text('')
    print(f'Built {len(docs)} articles × 2 languages; 73 HTML pages. Math: native MathML. Four PDFs copied from sources/downloads.')

if __name__=='__main__':main()
