---
name: brutalist-ui
description: Draft a brutalist UI design spec with raw structure, monospace and heavy type, hard edges, high contrast, and a sample layout, triggered by "brutalist UI", "brutalist design", "raw UI spec", or "industrial layout"
---

# Brutalist UI

Draft a brutalist interface spec: raw structure, monospace plus heavy sans type, hard 90-degree edges, high contrast, and one worked sample layout. Written to Projects/ as a draft.

## When to use
- You want a landing page, dashboard, or microsite that reads as raw, mechanical, and high-density.
- You need a design source of truth before anyone writes HTML or CSS.
- A client brief asks for an industrial, terminal, or print-blueprint look.
- You want to set tokens (type, color, grid, borders) once and reuse them across a build.

## Inputs
- Surface: page type and one-line purpose (landing, dashboard, doc index).
- Mode: pick ONE. `print` (light substrate, heavy sans) or `terminal` (dark substrate, monospace). Never mix both in one interface.
- Brand pull from `Company/brand.md` and voice from `Library/styles/brand-voice.md`.
- Optional: copy blocks, target viewport widths, any fixed content the layout must hold.

## Process
1. Read `Company/brand.md` and `Library/styles/brand-voice.md`. If either is missing, note it and proceed with defaults.
2. Confirm the mode. `print` = matte off-white background (#F4F4F0), carbon ink text (#0A0A0A), one hazard-red accent (#E61919). `terminal` = near-black background (#0A0A0A, not pure black), phosphor text (#EAEAEA), same single red accent.
3. Set type. Macro headers use a heavy neo-grotesque (Archivo Black, Inter Black) at fluid scale `clamp(4rem, 10vw, 14rem)`, tracking -0.04em, line-height 0.9, uppercase. Micro data uses a monospace (JetBrains Mono, IBM Plex Mono) at 11-14px, tracking 0.06em, uppercase, for all metadata, nav, IDs, and units.
4. Set structure. CSS Grid only. Razor lines via `display: grid; gap: 1px;` with contrasting parent and child backgrounds. Borders are 1px or 2px solid. Border-radius is exactly 0 everywhere. Full-width rules segregate zones.
5. Set markers. Frame data with ASCII brackets (`[ STATUS ]`), directional glyphs (`>>>`, `///`), registration marks as geometric units, and short fixed strings (`REV 2.6`, `UNIT D-01`) to read as active machinery.
6. Set texture, optional. Terminal mode may add scanlines via `repeating-linear-gradient`. Either mode may add a low-opacity SVG grain on the root. Keep it subtle. No gradients, no soft shadows, no translucency.
7. Build one sample layout that uses every token: header band with oversized numeral, a 12-column grid, one dense monospace data block, one full-width rule, and a red accent on exactly one vital element.
8. Write the spec and the sample to `Projects/{slug}/` as drafts. Stamp DRAFT at the top.

## Outputs
- `Projects/{slug}/brief.md` · mode, tokens, and rationale in plain text.
- `Projects/{slug}/final/brutalist-ui-spec.md` · the full spec: color, type, grid, components, texture rules, marked DRAFT.
- `Projects/{slug}/final/sample-layout.html` · one static reference layout that applies the tokens, marked DRAFT in a comment.
- Append one row to `Memory/kpi-ledger.md` only if a real metric exists (for example a measured load time). Columns: | date | metric | baseline | current | target | source | confidence | note |. Never edit prior rows.

## Guardrails
- DRAFT-ONLY. Nothing here ships or publishes without human review.
- Pick ONE mode and ONE substrate per surface. No mixing light and dark, no mixing print and terminal.
- Red (#E61919) is the only accent. Use it on vital data, structural rules, or strike-throughs, nowhere else.
- No gradients, no rounded corners, no drop shadows, no translucency. Corners stay at 90 degrees.
- Voice follows `Library/styles/brand-voice.md`. Numbers over adjectives, verbs over nouns.
- PROVENANCE: cite any metric you record. Never invent numbers for the ledger.
- Code and design files are drafts in `Projects/`. Credentials and tools stay out of the vault.

## References
- `Company/brand.md`
- `Library/styles/brand-voice.md`
- `_system/rules`
