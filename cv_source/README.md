# CV source

- `cv_RyotaroOKABE.docx` — the Word master. Edit this.
- `RyotaroOkabe_bio.docx` — short bio text.
- `cv_pdf_archive/`, `archives_old/` — past versions (kept in Dropbox, ignored by git).

## Publishing a new CV

1. Edit `cv_RyotaroOKABE.docx` in Word.
2. File → Save As → PDF, saving **directly into `../files/`** as `YYYY-MM-DD_cv_RyotaroOKABE.pdf`.
3. Commit and push. The CV page (`_pages/cv.md`) links the newest dated PDF automatically
   and shows its month as "Last updated".
4. If positions, awards, or skills changed, mirror them in `_data/cv.yml`.

This folder is excluded from the Jekyll build (`exclude:` in `_config.yml`), so nothing
here is published; only PDFs placed in `files/` are.
