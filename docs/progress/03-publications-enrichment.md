---
title: Publications Enrichment and Housekeeping
date: 2026-10-24
type: progress
slug: 03-publications-enrichment
source: chore/housekeeping branch
related: [02-argonne-update]
---

# Publications Enrichment and Housekeeping

- All 26 publication pages now carry a specific two-sentence excerpt written
  from the paper abstract (sources: local PDFs under `resources/publications_RO/`,
  Crossref, arXiv, Semantic Scholar).
- Figures added to five first/co-first-author pages (Isogawa 2026, Landry 2026,
  Cheng 2026 review, Han 2025 review, Okabe 2023); the figure on the
  second-author Hung 2024 page was removed. Rule: figures only for first or
  co-first-author papers.
- `_publications/` is now the documented source of truth;
  `markdown_generator/export_publications_csv.py` regenerates the legacy CSV.
- Housekeeping: June 2026 CV PDF archived; LF line endings enforced via
  `.gitattributes`; July 2026 diagnosis note committed.
