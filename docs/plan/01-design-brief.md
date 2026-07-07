---
title: Design Brief v2
date: 2026-07-06
type: plan
slug: 01-design-brief
source: Design discovery sessions (Round 1 & 2) with site owner
related: [00-site-refresh-master-plan, 00-design-directions, 02-phase1-implementation-plan]
---

# Design Brief v2 (Approved Direction)

## 1. Purpose & Target Audience
A researcher portfolio where research topics, publications, and themes are communicated as fast as possible. Priority order of readers:

1. Collaborators and researchers in the same field
2. Academic search/selection committees (faculty positions, postdoc, fellowships)
3. Industry research recruiters

This is a "research-first" site, not a resume site.

## 2. Desired First Impression
- Base: "a refined, trustworthy researcher" — quiet, polished, readable.
- Accent: cutting-edge AI x quantum materials, expressed through a royal blue accent color.
- Warmth: serif display headings and warm neutral tones for an approachable, editorial feel.
- Achievements speak through Selected Publications / Awards / Recent Highlights — factual, no overstating.
- No flashy animations. Whitespace, typography, and readability are the top priorities.

## 3. Homepage Structure (Wireframe B: left-aligned hero + photo right)
1. **Hero**: name (with 岡部 遼太郎), affiliation, one-line tagline, short bio (3–5 sentences integrated into hero), primary link buttons (CV / Publications / Google Scholar / GitHub / Email); profile photo on the right.
2. **Research Themes**: 4 cards (2x2 grid on desktop).
3. **Selected Publications**: up to 5 highlighted papers as cards (with images where available).
4. **Recent Highlights / News**: ~5 dated one-line items, driven by `_data/news.yml`, manually updated.
5. **Contact / Footer**: academic links restated.

## 4. Navigation
`Home | Publications | Talks | CV` + dark mode toggle.

- Teaching / Portfolio / Guide / talkmap: hidden from navigation but files preserved (archive treatment, no deletion).

## 5. Visual System

### Palette X: Warm Stone x Royal Blue
| Token | Light | Dark |
|---|---|---|
| Background | `#faf9f7` | `#12100e` |
| Body text | `#1c1917` | `#f5f5f4` |
| Secondary text | `#57534e` | `#a8a29e` |
| Accent | `#2563eb` | `#60a5fa` |
| Card border | `#e7e5e4` | `#292524` |

### Typography T2: limited serif + Inter
- Serif (planned: *Source Serif 4*) **only** for: name, h1, and section titles (h2).
- *Inter* for everything else: body, UI, navigation, card contents.
- Body 16–18px, line-height ~1.65.

### Layout
- Max width: ~42rem for prose, ~64rem for grid sections.
- Section spacing: 4–6rem.
- Cards: 1px border, 8px radius, hover = border color change only (minimal shadow, no lift).

### Light/Dark Mode
- CSS variables; auto-follow `prefers-color-scheme`; manual toggle persisted in `localStorage`; early inline script in `<head>` to prevent flash of wrong theme (FOUC).

## 6. Publications Page Strategy (P3 hybrid)
- Top: "Selected" section — 4–6 representative papers as cards with images.
- Below: all publications grouped by year (newest first). Each entry: title / authors (Okabe emphasized) / venue badge / external link buttons (DOI, arXiv, Code, Media).
- **Individual publication pages are preserved** (URLs kept, room for future enrichment), but the primary links from the list go directly to external resources (DOI/arXiv/publisher/PDF/code). Do not funnel visitors into thin internal pages.

## 7. CV / Profile Integration
- CV page (Phase 2): HTML summary (Education / Experience / Awards / Skills) + prominent "Download full CV (PDF)" button at top. PDF embed only as a desktop-side supplement.
- Current CV file: `files/2026-06-18_cv_RyotaroOKABE.pdf`.
- Profile source of truth: `author` in `_config.yml`; hero and footer both read from it.
- Links shown in main UI (academic five only): **Email / Google Scholar / GitHub / LinkedIn / ORCID**.
- Facebook / Instagram / X / YouTube: may remain in config files, but removed from all primary UI.

## 8. What to Remove from the Academic Pages Template
- **Remove from UI**: left author-profile sidebar, breadcrumbs, share buttons, comments, read-time indicator, the large social icon list.
- **Hide from nav (preserve files)**: talkmap, Portfolio, Teaching, Guide.
- **Phase 2 data cleanup**:
  - Dummy template talks in `_talks/` (3 files dated 2012–2014) — deletion candidates only; no real data is deleted.
  - Talks reconciliation: cross-check CV Presentations (~18 items) vs `_talks/` actual entries (17 files incl. 3 dummies → 14 real) and determine the correct list to publish.
  - Unused `_config.yml` settings (staticman, comments providers, placeholder socials).
  - Typo in `_pages/about.md` (`prooperties` → `properties`); LinkedIn link missing `https://`.
- **Preserve**: Jekyll collections structure, `markdown_generator/publications.py` workflow, existing permalinks.

## 9. Approved Initial Content Drafts

### Selected Publications (max 5 on homepage; factual, concise presentation)
1. Structural Constraint Integration in a Generative Model for the Discovery of Quantum Materials — *Nature Materials*, 2025
2. Virtual Node Graph Neural Network for Full Phonon Prediction — *Nature Computational Science*, 2024
3. Tetris-Inspired Detector with Neural Network for Radiation Mapping — *Nature Communications*, 2024
4. Large Language Model-Guided Prediction Toward Quantum Materials Synthesis — arXiv, 2024
5. Artificial intelligence-driven approaches for materials design and discovery — *Nature Materials*, 2026

(Alternate candidate: Universal Magnetic Structure Prediction from Atomic Coordinates — arXiv, 2026.)

### Research Themes (4 cards; descriptions limited to 1–2 sentences each)
1. **Generative Models for Quantum Materials**
2. **Graph Neural Networks for Materials Properties**
3. **LLMs for Materials Synthesis**
4. **AI-Assisted Detection and Scientific Instrumentation**

### Recent Highlights / News (initial items; year-only dates where the month is not confirmed by CV or repository data)
- **2026** — Review "Artificial intelligence-driven approaches for materials design and discovery" published in *Nature Materials*
- **2026-05** — Preprint "Universal Magnetic Structure Prediction from Atomic Coordinates with Near-Experimental Accuracy" posted to arXiv
- **2025** — "Structural Constraint Integration in a Generative Model for the Discovery of Quantum Materials" published in *Nature Materials* and featured by MIT News
- **2025-04** — Received MRS Spring Graduate Student Silver Award and Best Poster Award
- **2024-09** — Selected for the IBM PhD Fellowship

Date policy: use `YYYY-MM` only when the month is verifiable from the CV or repository data; otherwise use year only.

## 10. Technical Constraints
- Stay compatible with the `github-pages` gem (no unsupported plugins).
- Keep Jekyll collections and permalinks intact; the refresh is a presentation-layer change.
- Local builds may require pausing Dropbox sync (known folder-lock issue).
