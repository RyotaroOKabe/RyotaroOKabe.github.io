---
title: Phase 1 Implementation Plan
date: 2026-07-06
type: plan
slug: 02-phase1-implementation-plan
source: Design Brief v2
related: [01-design-brief, 00-site-refresh-master-plan]
---

# Phase 1 Implementation Plan (Patch-Based)

## Working Rules (agreed with site owner)
Every patch follows this cycle:

1. Propose the patch: purpose / files to edit / expected visual change / rollback method.
2. Owner approves.
3. Edit files.
4. Run `bundle _2.6.8_ exec jekyll build` to confirm the build passes.
5. Restart `bundle _2.6.8_ exec jekyll serve --no-watch` and verify the actual
   rendering at `http://localhost:4000/`.
   - Because of `--no-watch`, every change requires a rebuild + serve restart.
   - Review via `localhost` (not `127.0.0.1`): built URLs are localhost-based,
     so a different origin blocks icon fonts via CORS.
   - Note: `jekyll serve` rebuilds with `site.url` overridden to localhost;
     serving a plain `jekyll build` output would load CSS from the production
     site (absolute URLs) and mask local changes.
6. Present `git diff --stat` and a summary of the changes.
7. Propose a local commit message; commit if approved.
8. Move to the next patch.

Constraints:
- **No push to GitHub until explicitly requested.**
- No large sweeping edits; keep patches small and reviewable.
- Rollback baseline: after Patch 0, any patch can be reverted with `git restore <file>` (or `git revert <commit>` once committed).
- Dropbox folder locks can break `bundle`; pause Dropbox sync during builds if needed, per `.claude/CLAUDE.md`.

## Patch List

### Patch 0: Baseline snapshot commit
- **Purpose**: Commit all current uncommitted work (publication sync, planning docs, new CV, partial styling work) as a rollback baseline before structural changes.
- **Files**: commit only; no edits.
- **Visual change**: none.
- **Pre-commit review**: present `git status --short`, `git diff --stat`, change summary, file list, and commit message for owner approval BEFORE committing.

### Patch 1: Design tokens & CSS variables
- **Purpose**: Define the full token system (colors, spacing, typography scale, radii) as CSS custom properties.
- **Files**: `_sass/_tokens.scss` (existing untracked file — review current contents first), `assets/css/main.scss` (import order).
- **Visual change**: little to none (foundation only).
- **Rollback**: `git restore assets/css/main.scss`; revert `_sass/_tokens.scss`.

### Patch 2: Light/dark theme foundation + toggle
- **Purpose**: `prefers-color-scheme` auto-follow, manual toggle with `localStorage`, early inline script in head to prevent FOUC.
- **Files**: `_includes/head.html`, inline JS, `_sass/_tokens.scss`.
- **Visual change**: base background/text colors become variable-driven; theme switchable.
- **Rollback**: `git restore` the touched files.

### Patch 3: Header / navigation / footer refresh
- **Purpose**: Minimal top nav (Home, Publications, Talks, CV, theme toggle); footer reduced to the academic five links (Email / Scholar / GitHub / LinkedIn / ORCID).
- **Files**: `_includes/masthead.html`, `_includes/footer.html`, `_sass/_masthead.scss`, `_sass/_navigation.scss`, `_sass/_footer.scss`.
- **Visual change**: new header and footer across all pages.
- **Rollback**: `git restore` the touched files.

### Patch 4: Sidebar removal & base layout refresh
- **Purpose**: Disable `author_profile` sidebar site-wide; single-column content-first layout; adjust content widths (prose ~42rem, grids ~64rem).
- **Files**: `_config.yml` (defaults), `_layouts/` wrappers as needed, `_sass/_sidebar.scss`, `_sass/_archive.scss`.
- **Visual change**: **largest visual change of Phase 1** — all pages become single-column.
- **Rollback**: `git restore` the touched files.

### Patch 5: New hero + Research Themes (homepage top half)
- **Purpose**: Left-aligned hero (name, affiliation, tagline, 3–5 sentence bio, primary link buttons; photo right) + 4 Research Themes cards.
- **Files**: `_pages/about.md`, new `_includes/hero.html` (and/or `research-themes.html`), token additions.
- **Visual change**: homepage top half reaches final form.
- **Rollback**: `git restore _pages/about.md`; delete new includes.

### Patch 6: Selected Publications + News sections (homepage bottom half)
- **Purpose**: Selected publication cards (max 5) and Recent Highlights list on the homepage.
- **Files**: new `_data/news.yml`, new `_data/selected_publications.yml`, new includes, `_pages/about.md`.
- **Content**: use the approved drafts in Design Brief v2 §9 (factual tone; year-only dates where month unverified).
- **Visual change**: homepage complete.
- **Rollback**: `git restore _pages/about.md`; delete new data files/includes.

### Patch 7: Final polish & verification
- **Purpose**: Mobile/responsive fixes, typography and contrast tuning, font loading optimization, final build check.
- **Files**: minor SCSS adjustments.
- **Visual change**: detail refinements only.
- **Rollback**: `git restore` the touched files.

## Deferred to Phase 2
- Publications page redesign (P3 hybrid: Selected cards + year-grouped list with external links).
- CV page: HTML summary + PDF download button.
- **Talks reconciliation**: cross-check CV Presentations (~18) vs `_talks/` (17 files; 3 are 2012–2014 template dummies → 14 real entries); only the dummies are deletion candidates; no real data will be deleted.
- Content fixes: `about.md` typo (`prooperties`), LinkedIn `https://` missing, `_config.yml` cleanup (staticman/comments/social placeholders).
- `_data/news.yml` ongoing curation.

## Phase 3 (unchanged)
- Local build verification outside Dropbox, mobile checks, contrast/performance audit.

## Technical Debt
- `assets/js/main.min.js` was patched directly (greedy-nav infinite-recursion
  guard) because no JS bundling environment is set up. The same fix is applied
  to the source (`assets/js/plugins/jquery.greedy-navigation.js`), so a future
  rebuild via the npm/uglify pipeline (`package.json`) will preserve it. In
  Phase 3, set up the bundling pipeline and regenerate `main.min.js` from
  source instead of editing the minified file.
- CRLF/LF warnings on git operations: consider adding `.gitattributes` with an
  explicit line-ending policy (Phase 3 or a dedicated patch).
