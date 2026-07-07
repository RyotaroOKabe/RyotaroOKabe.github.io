# CLAUDE.md - Ryotaro Okabe Personal Website Refactor

This repository contains the personal/academic website of Ryotaro Okabe, hosted on GitHub Pages. The goal of this project is to maintain a simple, elegant, modern academic portfolio, keeping it accessible and up-to-date with publications, presentations, and CV changes.

## Repository Architecture
- `_config.yml`: Core Jekyll configurations.
- `_pages/`: Base static markdown pages (about, CV, publications, talks).
- `_publications/`: Generated markdown entries for academic papers.
- `_talks/`: Generated markdown entries for presentations/talks.
- `_data/navigation.yml`: Header navigation links.
- `_sass/`: SCSS styling components.
- `assets/`: Custom assets (CSS, JS, fonts).
- `files/`: Statically served files (like PDFs of papers and the CV).
- `markdown_generator/`: Python scripts and source CSV/BibTeX files for automating publication list additions.

## Build and Test Commands
- Local Jekyll build: `bundle exec jekyll build`
- Local Jekyll dev server: `bundle exec jekyll serve`
  *Note: Local building inside Dropbox may require pausing Dropbox sync to avoid `Permission Denied` folder lock errors.*

## Style & Design Principles
- **Modern Minimalist**: Rely on generous white space, clean grids, and strong typography.
- **Color Scheme**: Slate/neutral base with a high-contrast dark/light mode toggle. Accent color: royal blue (`#2563eb` in light) / electric blue (`#3b82f6` in dark).
- **Responsive**: Mobile-first design using fluid CSS layouts. No hardcoded pixel widths for structural wrappers.
- **Typography**: Inter (sans-serif) for body and headers.
- **Static Compatibility**: Avoid using server-side frameworks or plugins not supported by GitHub Pages (stay compatible with `github-pages` gem).

## Content Source of Truth
- **Profile details**: `_config.yml` (author configuration) and `_pages/about.md`.
- **CV File**: `files/2026-06-18_cv_RyotaroOKABE.pdf` (referenced by `_pages/cv.md`).
- **Publications database**: `markdown_generator/publications.csv` (source) -> generates `_publications/` pages via `markdown_generator/publications.py`.

## Safety Rules
- **Do not commit directly to master**: Always work on a separate branch (like `refresh/site-redesign`) and create snapshots/backups before structural modifications.
- **Do not delete original content**: Keep the core content structure and historical pages intact.
- **Do not expose private metadata**: Maintain privacy of email addresses and phone numbers unless they are public academic contact details.

## Publication/CV Update Workflow
1. If the CV PDF is updated, rename the file using `YYYY-MM-DD_cv_RyotaroOKABE.pdf` format and copy it to `files/`.
2. Update the link inside `_pages/cv.md` to point to the new path.
3. If new publications are added:
   - Add a row in `markdown_generator/publications.csv`.
   - Run `python markdown_generator/publications.py` to regenerate the individual publication markdown files under `_publications/`.
