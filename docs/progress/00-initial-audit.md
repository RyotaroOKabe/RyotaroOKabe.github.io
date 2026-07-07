---
title: Initial Repository Audit
date: 2026-07-06
type: progress
slug: 00-initial-audit
source: Local repository inspection
related: []
---

# Initial Repository Audit

## Context / Source
This audit was performed on the `RyotaroOKabe.github.io` repository on July 6, 2026, to identify the current structure, content, mismatches, and issues with the existing Academic Pages Jekyll setup.

## Summary
The repository is based on the **Minimal Mistakes** Jekyll theme adapted as **Academic Pages**. It contains portfolio/blog features, academic collections (publications, talks, teaching), and helper scripts. However, it currently relies on outdated placeholders, embeds a missing CV PDF, is missing recent high-impact publications, and does not support light/dark mode. Furthermore, local ruby dependency installation fails on Windows due to Dropbox file locks.

## Detailed Findings

### 1. Key Layouts & Templates
- **Entrypoints & Config**: `_config.yml` controls the overall site metadata. The author profile sidebar info is hardcoded under `author` in `_config.yml`, but `_data/authors.yml` still contains dummy template placeholders (`Name Name`, `Name2 Name2`).
- **Main Layouts (`_layouts/`)**:
  - `default.html`: The base HTML structure wrapper.
  - `single.html`: Layout for single pages (e.g., individual posts, publications).
  - `archive.html`: Base layout for list/archive pages.
  - `talk.html`: Custom layout for presentations.
- **Includes (`_includes/`)**:
  - `author-profile.html`: Generates the sidebar. Highly verbose and hardcoded with social media networks.
  - `head.html`: Pulls in page headers, Google Fonts (none are currently customized), and CSS.
  - `masthead.html`: Builds the top navigation.
  - `archive-single.html`: Previews articles/publications.

### 2. Styling System (`_sass/` & `assets/css/`)
- Main entry point is `assets/css/main.scss` which imports variables, resets, and layout files from `_sass/`.
- Styling is heavily coupled with SASS variables in `_sass/_variables.scss`.
- Currently **no dark/light mode support**; it uses static colors based on the default Minimal Mistakes theme.

### 3. Local Build Environment
- **Ruby version**: `ruby 3.4.6 [i386-mingw32]` is installed.
- **Dependencies**: Managed via `Gemfile` (using the `github-pages` gem).
- **Issue**: Running `bundle install` fails with `Bundler::DirectoryRemovalError` (Permission denied `@ dir_s_rmdir` or `strict_rm_rf` for `wdm` and `nokogiri` folders). This occurs because the workspace is located inside Dropbox (`MIT Dropbox`), which locks folders during syncing.
- **Workaround**: Temporarily pausing Dropbox syncing, or running the site build inside a local non-Dropbox folder, is required.

### 4. CV & Public Profile Content Extraction
From the latest untracked CV file (`files/2026-06-18_cv_RyotaroOKABE.pdf`), we extracted:
- **Name**: Ryotaro Okabe (岡部 遼太郎)
- **Email**: `rokabe [at] mit.edu`
- **Affiliation**: Ph.D. Candidate in Chemistry, Massachusetts Institute of Technology (MIT) (Sept 2021 – Sept 2026 expected)
- **Advisors**: Advised by Prof. Mingda Li (Quantum Measurement Group)
- **Education**:
  - M.S. in Engineering, Institute of Science Tokyo (formerly Tokyo Institute of Technology), Japan (Sept 2019 – Sept 2021)
  - B.S. in Engineering, Institute of Science Tokyo, Japan (Apr 2016 – Sept 2019) (Early Graduation)
- **Research Interests**: Structure–property relationships and inverse design of quantum materials, computational physics, machine learning, materials informatics.
- **Key Awards**:
  - MRS 2025 Spring Graduate Student Silver Award & Best Poster Award (Apr 2025)
  - IBM PhD Fellowship Award (Sept 2024 – Aug 2025)
  - NERSC GenAI Resource Allocation (Jul 2024)
- **Skills**: Python, CUDA, PyTorch, material simulation tools (VASP, Quantum Espresso, etc.), experimental characterization (solid-state NMR, XRD).

### 5. Content Mismatches
- **CV PDF File**: `_pages/cv.md` embeds `files/cv_RyotaroOKABE.pdf` which is deleted in the workspace. It needs to point to `files/2026-06-18_cv_RyotaroOKABE.pdf`.
- **Placeholder Authors**: `_data/authors.yml` contains dummy authors.
- **Missing/Outdated Publications**:
  - Five recent publications from 2025 and 2026 in the CV are completely missing from `publications.csv` and `_publications/`:
    1. *Universal Magnetic Structure Prediction...* (arXiv:2605.16230, 2026)
    2. *Quantum Theory of Functionally Graded Materials* (arXiv:2603.03424, 2026)
    3. *Artificial intelligence-driven approaches...* (Nature Materials 25, 174–190, 2026)
    4. *Are Quantum Materials Sustainable?* (Materials Today, 2025)
  - *Tuning Chiral Anomaly Signature...* is listed as an arXiv preprint in `publications.csv` but has since been published in *Nano Letters* (25, 17571, 2025).
- **Navigation Clutter**: commented items exist in `_data/navigation.yml` (Teaching, Portfolio). Active links include Publications, Talks, CV.

### 6. Technical Debt & Outdated Features
- **Leaflet / Talk Map**: The `talkmap/` folder uses an outdated Leaflet map generation workflow (`talkmap.py`, `talkmap.ipynb`) which generates `talkmap.html`. If the user does not want this, it adds clutter.
- **JS Bundler**: `package.json` relies on global/local configurations of `uglify-js` and `onchange` to compile `main.min.js`.
- **CSS Architecture**: SASS variables are hard-coded hex colors, which prevents fluid dark-mode transitions.

## Open Questions
- Should we completely clean out the `talkmap` feature if it is no longer required or if you prefer a simpler list of talks?
- Do you want to expose a "Teaching" section based on your teaching experience at MIT (Quantum Mechanics, General Chemistry) mentioned in your CV?

## Action Items
1. Switch local building to a non-syncing workspace or pause Dropbox to resolve Bundler lock errors.
2. Update `_data/navigation.yml` and `_config.yml` to clear out remaining placeholder metadata.
3. Synchronize publications by updating `markdown_generator/publications.csv` and running `publications.py` to rebuild `_publications/`.
4. Fix `_pages/cv.md` to point to the correct CV file name.
