# RSI Literature — bilingual reading site

A static reading site for **RSI, Feedback and Learning Dynamics**. English is the default; switching language keeps the current article. The reading map groups the literature into value, knowledge and learning mechanisms, with feedback as a connecting theme.

## Read locally

Open `dist/index.html` in a browser. Articles, search, styles and formulas work without a server or an internet connection. Original-paper links require an internet connection. The four review PDFs are in `dist/downloads/`.

The site supports keyboard navigation, `/` or `Ctrl/Cmd + K` for search, section navigation, mobile layouts and browser printing. Formulas are converted to native MathML at build time and displayed by current browsers; no remote math library or font download is needed.

## Upload to GitHub Pages

The **contents of this directory** are the repository root: `dist/`, `.github/`, `sources/`, `assets/` and the build scripts sit side by side. Do not place them inside an additional `site/` directory unless you also update the workflow path.

1. Create a GitHub repository and upload this directory, including `.github/workflows/pages.yml` and the complete `dist/` folder.
2. In **Settings → Pages → Build and deployment**, select **GitHub Actions**.
3. Push to `main`, or run **Publish literature site** from the Actions tab. The workflow publishes the already-built `dist/`; it does not require Python, Pandoc or source folders outside this repository.
4. GitHub provides the Pages URL after the workflow completes. Relative links support both a project URL such as `username.github.io/repository/` and a custom domain.

The target repository is [`PengYiJiang-john/rsi-literature`](https://github.com/PengYiJiang-john/rsi-literature). The GitHub Pages URL is https://pengyijiang-john.github.io/rsi-literature/. Confirm publication from the Actions result and the live Pages URL.

## Rebuild or maintain

Requirements: Python 3.10+ and Pandoc 3+. No Python or npm package installation is required. The prebuilt `dist/` needs neither tool.

```bash
python build_site.py
python validate_site.py
```

To build, validate and produce a self-contained upload ZIP:

```bash
python package_site.py
```

The archive includes its own content snapshot and all four PDFs; it does not rely on a parent directory. The provided archive has also been extracted and rebuilt in a separate directory to check this independence. Automated checks cover local links, paired language pages, search coverage and rendered formulas. A browser visual inspection has not been run in this environment.

`sources/` is a self-contained snapshot of the maintained Chinese and English Markdown, main review JSON and document registry. A standalone rebuild reads that snapshot. In the full research workspace, refresh the snapshot and rebuild with:

```bash
python site/build_site.py --source /absolute/path/to/rsi_literature
```

The builder copies these four PDFs from `sources/downloads/` to `dist/downloads/` on every build:

- `rsi-review-en-plain.pdf`
- `rsi-review-en-linked.pdf`
- `rsi-review-zh-plain.pdf`
- `rsi-review-zh-linked.pdf`

Refreshing from the full research workspace also refreshes the PDF snapshot from `exports/{en,zh}_{plain,linked}/review.pdf`. A missing PDF fails the build rather than leaving a broken download link.

Articles keep their stable slugs. Markdown cross-links resolve to local article pages in the current language; source-paper links remain external. Search data is an ordinary local script, so it also works when pages are opened with `file://`.

## Files

- `build_site.py`: content snapshot, bilingual HTML, search index and formula rendering.
- `validate_site.py`: local targets, fragments, language switches, formula output and downloads.
- `assets/`: shared CSS and interaction code.
- `sources/`: source snapshot for standalone rebuilding.
- `dist/`: complete upload-ready website.
- `.github/workflows/pages.yml`: GitHub Pages workflow, deploying `dist/`.

The build does not contact or update ChatGPT Pages, GitHub or any hosting service.
