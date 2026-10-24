---
title: Master Ship & Dark-Toggle Diagnosis
date: 2026-07-07
type: progress
slug: 02-master-ship-and-toggle-diagnosis
source: Session resuming refresh/site-redesign after Phase 1-2
related: [01-phase1-summary, 02-phase1-implementation-plan]
---

# Master Ship & Dark-Toggle Diagnosis

Session goals: resume the redesign, publish it to the live site, and
investigate a reported day/night toggle problem. All three done; no open
code defects. One optional polish patch is proposed but not yet started.

## 1. Working-tree recovery (before anything else)

On resume, the branch state contradicted the prior session's note (which
claimed `HEAD = 7b3e9c2 / Patch 12`, clean):

- Actual `HEAD` was `b45c6ea` (Patch 11); `7b3e9c2` never existed.
- The working tree was **dirty with the destructive `publications.py`
  output**: 25 `_publications/*.md` pages had their hand-authored bodies
  replaced by the generic template and their co-first-author `†` corrupted
  to `�`. An uncommitted `.gitattributes` edit (unlanded Patch 12) was also
  present.
- No committed damage — `HEAD` and `origin` were intact.

Action: `git restore .` (owner-approved) discarded all 26 dirty files back
to a clean `b45c6ea`. Verified the tetris page regained `<strong>`/`†`/rich
body. **Reminder still stands: never run `markdown_generator/publications.py`.**

## 2. Shipped Phase 1-2 to master (LIVE)

Owner approved publishing after a 4-page headless-Chrome visual check
(top / publications / CV / talks — all intact, `†` and figures correct).

- `git merge --no-ff refresh/site-redesign` → merge commit **`f0905f9`**
  ("Merge site redesign (Phase 1-2) into master"), 17 commits, 94 files.
- `git push origin master` (`82ef7f6..f0905f9`) → GitHub Pages rebuilt; the
  redesign is **live** at https://ryotarookabe.github.io/.
- Also pushed the branch backup: `origin/refresh/site-redesign` → `b45c6ea`.
- Rollback if ever needed: `git revert -m 1 f0905f9` then push.

### Side-effect fixed: `.bundle/config` removed on checkout

The merge deleted `.bundle/config` (it was tracked on master; the branch
untracked it). Returning to `refresh/site-redesign` physically removed the
file, so `bundle exec jekyll` lost `BUNDLE_PATH` and failed with
`command not found: jekyll`. Recreated it (untracked, gitignored):

```
BUNDLE_PATH: "C:/Users/rokabe/AppData/Local/ruby-bundle"
```

Local `serve` works again. See [[local-dev-environment]].

## 3. Day/night toggle — reported "clicking does nothing"

**Root cause: post-deploy browser caching, not a code bug.**

Evidence gathered:

- Toggle mechanism verified working end-to-end with puppeteer-core driving
  real clicks on system Chrome: click flips `data-theme` + all CSS vars
  (`--background-color` `#faf9f7`⇄`#12100e`), choice persists via
  `localStorage`, OS `prefers-color-scheme` auto-follow works, and the
  toggle is visible/functional on mobile (390px).
- The live HTML carries the correct toggle button + inline handler, and the
  live `main.css` serves the `html[data-theme="dark"]` token block.
- **`main.css` is served with `Cache-Control: max-age=600` (10 min).**
  Within that window the browser reuses the *old* pre-redesign stylesheet
  (no dark tokens) without revalidating. Result: the new HTML shows the
  button, but the stale CSS has no dark rules, so clicking changes
  `data-theme` with no visual effect — exactly the reported symptom.

Resolution (no code change possible for a client cache): **hard reload
(Ctrl+Shift+R)** or wait out the ~10-minute cache. Self-resolving; will
recur for ~10 min after any future deploy.

## 4. Open item — optional dark-mode polish patch (proposed, not started)

Dark screenshots surfaced two cosmetic issues (separate from the toggle):

1. CV page embedded PDF renders as a large empty block — jarring in dark.
2. Selected-publication thumbnails keep white figure backgrounds and float
   on the dark cards.

Proposed one small patch: frame/size the PDF embed (or swap for a
thumbnail+link), give thumbnails a subtle background + radius, and add a
dark-aware `theme-color` meta / pre-paint background for FOUC. To run
through the normal propose → approve → build/serve → screenshot →
pre-commit review cycle on request.

## State at end of session

- Branch `refresh/site-redesign` @ `b45c6ea`, working tree clean.
- `master` @ `f0905f9` == `origin/master` — redesign is live.
- No uncommitted tracked changes; recreated `.bundle/config` is gitignored.
