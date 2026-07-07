---
title: Initial Antigravity Prompt
date: 2026-07-06
type: prompt
slug: 00-initial-antigravity-prompt
source: Session bootstrapping
related: []
---

# Initial Antigravity Prompt

## Context / Source
This document serves as a transition/bootstrapping prompt for subsequent agent sessions to continue the site refresh implementation.

---

## Agent Bootstrapping Prompt

You are tasked with implementing Phase 1 (Visual System Redesign) and Phase 2 (Content Sync) of the personal website refresh for Ryotaro Okabe (`RyotaroOKabe.github.io`).

### Context
- The codebase is a Jekyll project built on the **Minimal Mistakes** (Academic Pages) template.
- A thorough repository audit and plan have been drafted in:
  - `docs/progress/00-initial-audit.md` (mismatches, site structure)
  - `docs/plan/00-site-refresh-master-plan.md` (work stages)
  - `docs/brainstorm/00-design-directions.md` (recommended layout/typography)
- The target design is a **Minimal Research Portfolio** with:
  - Integrated dark/light mode using CSS variables.
  - Centered or lightweight layout replacing the heavy default sidebar.
  - Generous whitespace and clean modern typography (*Inter*).

### Instructions for Next Agent Session
1. **Pausing Dropbox Sync**: Advise the user to temporarily pause Dropbox sync or copy the folder out of Dropbox before running `bundle install` to avoid file-locking permissions errors.
2. **Phase 1 (Theme Refresh)**:
   - Create a CSS variables token file `_sass/_tokens.scss`.
   - Update `assets/css/main.scss` to import `_tokens.scss`.
   - Implement `prefers-color-scheme` media queries and add a manual dark mode toggle in the header.
   - Refactor `_includes/author-profile.html` to simplify the sidebar, removing excessive unused icons and making it feel premium.
3. **Phase 2 (Content Sync)**:
   - Synchronize missing publications (details in `docs/progress/00-initial-audit.md`) by modifying `markdown_generator/publications.csv` and running Python scripts.
   - Update the CV link in `_pages/cv.md` to point to the new CV `files/2026-06-18_cv_RyotaroOKABE.pdf`.
4. **Safety**: Do not delete existing articles or write code that breaks static hosting on GitHub Pages. Work on the `refresh/site-redesign` branch.
