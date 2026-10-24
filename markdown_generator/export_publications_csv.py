#!/usr/bin/env python3
"""Export markdown_generator/publications.csv from the _publications/*.md pages.

_publications/ is the source of truth for the website. This script keeps the
legacy CSV in sync (one direction only) so it can still be used for exports or
quick inspection. Run from the repository root:

    python3 markdown_generator/export_publications_csv.py
"""
import csv, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "markdown_generator", "publications.csv")
COLS = ["pub_date", "title", "venue", "excerpt", "citation", "url_slug", "paper_url",
        "media_url", "github_url", "data_url", "slides_url", "figure", "category"]

def fm_value(fm, key):
    m = re.search(rf"(?m)^{key}:\s*(.*)$", fm)
    if not m:
        return ""
    v = m.group(1).strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        v = v[1:-1].replace("''", "'") if v[0] == "'" else v[1:-1]
    return v

def classify_links(body):
    out = {"media_url": "", "github_url": "", "data_url": "", "slides_url": ""}
    for url, label in re.findall(r"<a href='([^']+)'(?![^>]*target=)[^>]*>([^<]+)</a>", body):
        lab = label.lower()
        if "github" in lab or "code" in lab:
            out["github_url"] = out["github_url"] or url
        elif "data" in lab:
            out["data_url"] = out["data_url"] or url
        elif "slide" in lab:
            out["slides_url"] = out["slides_url"] or url
        elif "news" in lab or "press" in lab or "briefing" in lab:
            out["media_url"] = out["media_url"] or url
    return out

rows = []
for p in sorted(glob.glob(os.path.join(ROOT, "_publications", "*.md")), reverse=True):
    s = open(p, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n(.*)$", s, re.S)
    if not m:
        print("skip (no front matter):", p, file=sys.stderr)
        continue
    fm, body = m.groups()
    name = os.path.basename(p)[:-3]
    date, slug = name[:10], name[11:]
    fig = re.search(r"images_pub/([^'\"]+)", body)
    row = {
        "pub_date": date,
        "title": fm_value(fm, "title"),
        "venue": fm_value(fm, "venue"),
        "excerpt": fm_value(fm, "excerpt"),
        "citation": fm_value(fm, "citation").replace("&amp;", "&"),
        "url_slug": slug,
        "paper_url": fm_value(fm, "paperurl"),
        "figure": fig.group(1) if fig else "",
        "category": fm_value(fm, "category"),
    }
    row.update(classify_links(body))
    rows.append(row)

with open(OUT, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=COLS, lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
print(f"wrote {len(rows)} rows to {os.path.relpath(OUT, ROOT)}")
