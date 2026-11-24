#!/usr/bin/env bash
# Build the CV from LaTeX with Tectonic and publish it as a dated PDF in files/.
#   ./build_cv.sh              -> files/YYYY-MM-DD_cv_RyotaroOKABE.pdf (today's date)
#   ./build_cv.sh 2026-12-01   -> use a specific date in the file name
#   ./build_cv.sh --no-copy    -> compile only (cv_source/latex/cv.pdf)
set -euo pipefail
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
DATE="$(date +%F)"; COPY=1
for a in "$@"; do
  case "$a" in
    --no-copy) COPY=0 ;;
    [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]) DATE="$a" ;;
    *) echo "usage: $0 [YYYY-MM-DD] [--no-copy]" >&2; exit 2 ;;
  esac
done
command -v tectonic >/dev/null || { echo "tectonic not found: brew install tectonic" >&2; exit 1; }
cd "$HERE/latex"
tectonic --chatter minimal cv.tex 2>&1 | grep -v 'accessing absolute path' || true
[ -s cv.pdf ] || { echo "build failed: cv.pdf not produced" >&2; exit 1; }
echo "built: $HERE/latex/cv.pdf ($(pdfinfo cv.pdf 2>/dev/null | awk '/^Pages/{print $2}') pages)"
if [ "$COPY" = 1 ]; then
  OUT="$REPO/files/${DATE}_cv_RyotaroOKABE.pdf"
  cp cv.pdf "$OUT"
  echo "published: $OUT"
  echo "next: git add files/${DATE}_cv_RyotaroOKABE.pdf && git commit && git push (the CV page picks the newest dated PDF)"
fi
