# CV source

- `latex/cv.tex` — **the CV master (LaTeX)**. Edit this (or ask the agent to).
- `build_cv.sh` — compiles with Tectonic and copies the PDF to `../files/YYYY-MM-DD_cv_RyotaroOKABE.pdf`.
- `cv_RyotaroOKABE.docx` — the former Word master, kept untouched as a fallback (last used for the 2026-10-24 PDF).
- `RyotaroOkabe_bio.docx` — short bio text.
- `cv_pdf_archive/`, `archives_old/` — past versions (kept in Dropbox, ignored by git). Never delete.

## Publishing a new CV

1. Edit `latex/cv.tex`.
2. Run `./build_cv.sh` (needs `brew install tectonic`; first run downloads TeX packages).
   It writes `latex/cv.pdf` and copies it to `../files/<today>_cv_RyotaroOKABE.pdf`.
3. Commit the new PDF (and `cv.tex`) and push. The CV page (`_pages/cv.md`) links the
   newest dated PDF automatically and shows its month as "Last updated".
4. If positions, awards, or skills changed, mirror them in `_data/cv.yml`.

Fonts: Times New Roman from macOS (`/System/Library/Fonts/Supplemental`), loaded via fontspec.
Build artifacts (`latex/cv.pdf`, `*.aux`, ...) are gitignored; only `cv.tex` is tracked.

This folder is excluded from the Jekyll build, so nothing here is published; only PDFs in `files/` are.
