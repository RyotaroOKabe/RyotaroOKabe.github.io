---
title: Design Directions
date: 2026-07-06
type: brainstorm
slug: 00-design-directions
source: Design direction ideation
related: []
---

# Design Directions

## Context / Source
This brainstorm details the design refreshes proposed for the `RyotaroOKabe.github.io` personal website, transitioning away from the default Academic Pages (Minimal Mistakes) templates toward a bespoke, premium look.

---

## Proposes Directions

### 1. Minimal Research Portfolio (Default Recommendation)
A clean, speed-optimized, content-first portfolio that highlights research impact, paper releases, and active links. It removes heavy sidebars and centers the content.

- **Layout**: Centered, single-column or off-center two-column layout without the overwhelming multi-layer sidebar. Generous whitespace (margins of 2rem-3rem). Sidebar replaced by a clean, lightweight floating or sticky mini-profile on desktop, and standard top header.
- **Typography**: Sans-serif pairing (e.g., *Inter* or *Outfit* for headings, *Inter* or *Roboto* for body text). Very readable hierarchy with strict line heights (1.6x for body, 1.25x for headings).
- **Homepage Structure**: 
  - Above the fold: A brief, high-impact intro statement ("Ph.D. Candidate at MIT working on AI for Materials Discovery").
  - Below the fold: A concise grid showing "Selected Publications" (with visual badges/graphics) and "Latest News/Talks".
- **Navigation**: Clean, simple horizontal header menu (Home, Publications, Talks, CV, Dark Mode Toggle).
- **Color System**: Curated slate/neutral base.
  - Light mode: Off-white background (`#f8fafc`), dark slate text (`#0f172a`), royal blue/indigo accents (`#2563eb`).
  - Dark mode: Matte obsidian background (`#0b0f19`), ice-white text (`#f8fafc`), electric blue accents (`#3b82f6`).
- **Dark/Light Mode**: Triggered by CSS variables using `prefers-color-scheme` with a manual JavaScript toggle saving the user preference to `localStorage`.
- **Implementation Difficulty**: **Medium**. Requires refactoring `_includes/head.html`, `_includes/masthead.html`, and `_sass/_navigation.scss`, then replacing colors with CSS variables.

---

### 2. Editorial Academic Profile
A magazine/journal-inspired layout that mimics the typography and spacing of modern science publications (like Nature or Science journals), but with a digital-first approach.

- **Layout**: Classical multi-column grids, asymmetrical page layouts, wide gutters, serif typography.
- **Typography**: Serif pairing for body (e.g., *Merriweather* or *Playfair Display*), clean geometric sans-serif for headings (e.g., *Montserrat* or *DM Sans*).
- **Homepage Structure**: 
  - Left column: Large typography greeting and a detailed academic biography.
  - Right column: Clean timeline of achievements, publications, and selected presentations.
- **Navigation**: Left-side vertical navigation bar on desktop, collapsing to a top hamburger menu on mobile.
- **Color System**: Warm/academic tone.
  - Light mode: Warm cream background (`#faf8f5`), charcoal text (`#1c1917`), forest green/burgundy accents (`#15803d` / `#991b1b`).
  - Dark mode: Dark bronze/coffee background (`#12100e`), ivory text (`#f5f5f4`), soft emerald accents (`#10b981`).
- **Dark/Light Mode**: Handled via CSS variables. Smooth fade transitions.
- **Implementation Difficulty**: **High**. Requires complete layout overhaul of layouts (`default.html`, `single.html`) and extensive rewriting of layouts' column wrappers.

---

### 3. Modern Personal Lab Notebook
A design that borrows aesthetics from developer dashboards, terminal outputs, and interactive labs. It focuses on showcasing repositories, live code snippets, and active calculations.

- **Layout**: Strict grid layout (CSS Grid), boxes with borders, subtle mono fonts, and code-block styled sections.
- **Typography**: Mono typeface pairing (e.g., *JetBrains Mono* or *Fira Code* for technical headings and figures) with clean sans-serif (e.g., *SF Pro* or *Geist* for body).
- **Homepage Structure**:
  - High-impact header showing "Active Status: Ph.D. Candidate @ MIT".
  - Code-like blocks containing "Bio", "Core Stack", "Selected Projects/Publications" (with Git stars/badges).
- **Navigation**: Top sticky grid bar with borders separating links.
- **Color System**: Highly tech-focused.
  - Light mode: Stark white background (`#ffffff`), dark gray text (`#1e293b`), bright amber/teal accents (`#0d9488`).
  - Dark mode: Jet black background (`#000000`), neon green/cyan accents (`#10b981` / `#06b6d4`), gray borders.
- **Dark/Light Mode**: Direct switch with no transitions for a retro-tech look.
- **Implementation Difficulty**: **Medium-High**. Requires custom styling of borders, margins, and custom card elements for publications.

---

## Recommendation
We recommend **Direction 1: Minimal Research Portfolio**. It aligns perfectly with a professional, elegant, and modern academic presence. It remains extremely fast, lightweight, accessible, and works seamlessly with Jekyll's collection outputs, while dramatically improving on the cluttered look of the default Academic Pages theme.
