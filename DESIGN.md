# menzimuck.ro — DESIGN.md

## Brand extraction
- Who: Baier Solutions SRL, distribuitor oficial Menzi Muck AG (Rüthi, CH) pentru România. Excavatoare pășitoare only.
- Product truth: machines are red steel on black tyres, working on 45° slopes, riverbeds, forest. Swiss, 60 years (1966–2026).
- Buyer: owner of a construction / forestry / utilities firm in RO, 40–60, decides on numbers and on seeing the machine work. Not impressed by SaaS gloss.
- Voice: short, technical, confident. No superlatives we can't back with a spec.

## Aesthetic families remixed
1. Swiss technical catalogue (Müller-Brockmann grid, mono spec tables, numbers as the hero).
2. Alpine heavy-equipment poster (one machine, one black-and-red field, condensed uppercase type).

## Tokens
- Layout model: spacex.com — full-bleed photo/video panels, text bottom-left, thin uppercase nav, outlined white buttons, no cards, no icons.
- `--bg: #000` (pure black, dominant)
- `--ink: #fff`, `--ink-2: rgba(255,255,255,.72)`, `--line: rgba(255,255,255,.2)`
- `--red: #E7000D` — sampled from the official logo SVG. Used ONLY in the logo. The machines are yellow; the photos carry the colour, the UI stays black/white.
- Radius: 0. Shadows: none. Elevation by 1px lines and photo gradients.

## Type
- One family: Barlow 400/500/600. Headlines 600 uppercase, +0.02em tracking (SpaceX uses D-DIN; Barlow is the closest open DIN-style face).
- Nav/labels: 11–12px, 600, +0.14–0.22em tracking, uppercase.
- Spec tables: Barlow (tabular numerals via `font-variant-numeric: tabular-nums`).
- Banned: Inter, Roboto, Space Grotesk.

## Motion
- One staggered page-load reveal on the hero (eyebrow → H1 → sub → CTA, 80ms steps).
- Model rail: native horizontal scroll with snap; no carousel JS.
- `prefers-reduced-motion`: reveal disabled.

## Imagery
- All imagery is Menzi Muck AG's own (pulled from menzimuck.com with Chris's authorisation as distributor), resized to 1920px / q82. Hero film streamed from menzimuck.com until a 1080p cut arrives.
- Logo: `images/logo.svg` — the original vector from menzimuck.com, untouched.

## Layout
- Max width 1280. 12-col grid, 24px gutter. Section padding 96/64.
- Nav: logo left, 5 links, red "Cere ofertă" button.
- Pages: index, m5x, m4x, m2, a20-a25 (+ contact anchor). Footer with company data.
