---
title: Phase 1 Completion Summary
date: 2026-07-07
type: progress
slug: 01-phase1-summary
source: Phase 1 patch series on refresh/site-redesign
related: [01-design-brief, 02-phase1-implementation-plan]
---

# Phase 1 Completion Summary

Phase 1 (visual system redesign) is complete on the `refresh/site-redesign`
branch. The site moved from the default Academic Pages template to the
approved "Minimal Research Portfolio" design (warm stone palette, royal blue
accent, serif display headings, single-column layout, dark mode).

## Patch series

| Patch | Commit | Scope |
|---|---|---|
| 0 | `1055b16` | Baseline snapshot (publication sync, planning docs, CV update) |
| env | `8040ce0` | Windows dev fixes: disable wdm/hawkins, add tzinfo-data, untrack .bundle/config |
| fix | `6ec348a` | UTF-8 re-encoding of 4 publication pages; Jekyll excludes (archives/docs/resources/.claude/markdown_generator) |
| 1 | `7915d6a` | Design tokens (`_sass/_tokens.scss`): palette X, fonts, spacing, radii, focus ring |
| 2 | `b389c70` | Light/dark toggle: OS auto-follow, explicit-choice persistence, a11y |
| 3 | `e7b5d31` | Header/footer refresh, Source Serif 4 for display headings, academic footer links, greedy-nav recursion fix |
| 4 | `f56e1d6` | Sidebar removal, centered single-column layout (42rem prose / 64rem lists) |
| 5 | `678a497` | Homepage hero + research theme cards (`_data/profile.yml`, `_data/research_themes.yml`) |
| 6 | `fe7255a` | Selected publications + recent highlights (`_data/selected_publications.yml`, `_data/news.yml`) |
| 7a | `98a6281` | Content restoration: publication rich bodies/figures/links from git history, duplicate citation fix, talks synced with CV (added 5 entries, removed 3 dummies) |
| 7b | (this) | Thumbnail optimization, WCAG contrast verification, full-site sweep |

## Verification status (Patch 7b)

- Contrast: all 14 token pairs (light/dark x text/muted/accent/link-hover on
  bg/card/footer) pass WCAG AA for normal text (lowest: 4.91:1).
- Homepage publication thumbnails reduced from ~2.8 MB to ~241 KB
  (320px PNGs; originals preserved in `images_pub/`).
- Sweep: 7 page types x HTTP 200, no horizontal scroll (desktop + 375px),
  footer/toggle present everywhere, dark mode persists across navigation,
  52 internal links OK, no JS console errors.

## How to edit content (for the site owner)

- Hero text/tagline/buttons: `_data/profile.yml`
- Research themes: `_data/research_themes.yml`
- Selected publications: `_data/selected_publications.yml`
- News: `_data/news.yml`
- Publications database: `markdown_generator/publications.csv`
  (WARNING: do not regenerate pages until the generator is fixed —
  see Technical Debt in `docs/plan/02-phase1-implementation-plan.md`)

## Deferred to Phase 2

- Publications page redesign (P3 hybrid: selected cards + year-grouped list
  with venue badges and external link buttons)
- CV page: HTML summary + PDF download button (current PDF embed is weak on
  mobile)
- Content decisions: cheng2025ai vs cheng2026ai duplicate, arXiv/journal
  categorization on the publications list
- `_config.yml` cleanup (staticman/comments/social placeholders)

## Deferred to Phase 3

- Rebuild `main.min.js` from source via the npm/uglify pipeline
  (minified file was patched directly for the greedy-nav fix)
- `.gitattributes` line-ending policy
- Lighthouse-style performance audit; possible webfont self-hosting
