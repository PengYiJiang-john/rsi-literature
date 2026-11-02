#!/usr/bin/env python3
"""Check the static site's local links, language pairs, formulas and downloads."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import json
import re
import sys

ROOT=Path(__file__).resolve().parent
DIST=ROOT/'dist'

class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids=set(); self.references=[];self.language_switch=None;self.math=0;self.unrendered=0;self.root=None;self.lang=None;self.links=[]
        self.feed(text)
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if a.get('id'):self.ids.add(a['id'])
        if tag=='html':self.lang=a.get('lang')
        if tag=='body':self.root=a.get('data-root')
        if tag=='math':self.math+=1
        if tag=='code' and a.get('class')=='language-math':self.unrendered+=1
        for name in ['href','src']:
            if a.get(name):self.references.append(a[name])
        if tag=='a':self.links.append(a)
        if 'language-switch' in a.get('class','').split():self.language_switch=a.get('href')

def main():
    errors=[];warnings=[];paths=sorted(DIST.rglob('*.html'))
    pages={p.resolve():Page(p.read_text()) for p in paths}
    registry=json.loads((ROOT/'sources/document_registry.json').read_text())
    docs=registry['documents']+registry.get('topics',[])
    checked=0
    for p,page in pages.items():
        for link in page.references:
            parsed=urlsplit(link)
            if parsed.scheme or parsed.netloc:continue
            checked+=1
            if parsed.path.startswith('/'):errors.append(f'Root-relative URL breaks project hosting: {p.name}: {link}')
            target=(p.parent/unquote(parsed.path)).resolve() if parsed.path else p
            if not target.is_relative_to(DIST.resolve()):errors.append(f'Escapes dist: {link}')
            if not target.exists():errors.append(f'Missing target: {p.relative_to(DIST)} → {link}');continue
            if parsed.fragment and target in pages and unquote(parsed.fragment) not in pages[target].ids:
                errors.append(f'Missing fragment: {p.relative_to(DIST)} → {link}')
        if p!= (DIST/'index.html').resolve():
            lang=p.relative_to(DIST).parts[0];other='zh' if lang=='en' else 'en'
            expected=(DIST/other/Path(*p.relative_to(DIST).parts[1:])).resolve()
            actual=(p.parent/(page.language_switch or '')).resolve()
            if actual!=expected:errors.append(f'Language switch loses article: {p}')
            if not (p.parent/(page.root or '')).resolve()==DIST.resolve():errors.append(f'Invalid relative root: {p}')
        if page.unrendered:errors.append(f'Raw math code block: {p}')
        text=p.read_text()
        if 'RSIMATHPLACEHOLDER' in text or '[[berk-nash|' in text:errors.append(f'Unresolved source markup: {p}')
    for lang in ['en','zh']:
        for d in docs:
            path=DIST/lang/'articles'/f'{d["slug"]}.html'
            if not path.exists():errors.append(f'Missing article: {path}')
            source=ROOT/'sources'/d['source_path'] if lang=='zh' else ROOT/'sources/translations/en'/d['source_path']
            expected=len(re.findall(r'^```math\s*$',source.read_text(),re.M))
            if path.exists() and pages[path.resolve()].math<expected:errors.append(f'Missing rendered equations: {path}')
        for variant in ['plain','linked']:
            p=DIST/'downloads'/f'rsi-review-{lang}-{variant}.pdf'
            if not p.exists() or not p.read_bytes().startswith(b'%PDF-'):errors.append(f'Missing or invalid PDF: {p}')
    if 'url=en/index.html' not in (DIST/'index.html').read_text():errors.append('Root does not default to English')
    search=(DIST/'assets/search-index.js').read_text()
    data=json.loads(search.removeprefix('window.RSI_SEARCH = ').rstrip(';\n'))
    if len(data)!=len(docs)*2:errors.append('Search index does not cover every translation')
    for lang in ['en','zh']:
        indexed={d['slug'] for d in data if d['lang']==lang}
        if indexed!={d['slug'] for d in docs}:errors.append(f'Incomplete search index: {lang}')
    app=(DIST/'assets/app.js').read_text()
    if re.search(r'\bfetch\s*\(|XMLHttpRequest',app):errors.append('Search depends on network/file fetch')
    stats={'html_pages':len(paths),'articles_per_language':len(docs),'local_references_checked':checked,'rendered_math_blocks':sum(p.math for p in pages.values()),'search_entries':len(data),'pdfs':4,'default_language':'en','relative_project_paths':True,'native_mathml':True,'browser_visual_qa':'not run; no supported browser preview available','errors':errors,'warnings':warnings}
    (ROOT/'validation.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(stats,ensure_ascii=False,indent=2))
    return bool(errors)

if __name__=='__main__':sys.exit(main())
