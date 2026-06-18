---
name: minimalist-ui
description: Draft a minimalist UI design spec with restraint rules, type scale, spacing, color set, and a sample layout, when you say design a clean UI, minimalist interface, or build a quiet UI spec
---

# Minimalist UI

Write a restraint-first UI design spec to Projects/ as a draft: the rules, type scale, spacing system, color set, and one sample layout.

## When to use
- You want a calm, editorial, document-style interface and need the rules written down before anyone builds it.
- A page or app feels noisy, and you want a spec that cuts decoration back to structure.
- You are starting a new project surface and want a small, fixed set of tokens so the build stays consistent.

## Inputs
- The surface to design (landing page, dashboard, settings, app shell). Ask if not stated.
- Brand voice from Library/styles/brand-voice.md, if present.
- Any existing tokens or screenshots the user points at. If none, draft from the defaults below.
- Target slug for the project folder. Default to the surface name in kebab-case.

## Process
1. Read Library/styles/brand-voice.md for tone, and Company/brand.md if it exists, so the spec matches the house voice.
2. Set the surface and one sentence of intent. Name what the page must do, nothing more.
3. Write the restraint rules. State the bans plainly:
   - No drop shadows beyond a near-invisible diffuse one (opacity under 0.05).
   - No gradients, no neon, no glassmorphism past a subtle navbar blur.
   - No pill shapes on large containers or primary buttons.
   - No bright color fills on large sections or hero areas.
   - One accent family only, used for meaning, never for decoration.
   - Body text is charcoal, never pure black. Secondary text is one muted gray.
   - Content column capped near 1024px so lines stay readable.
4. Define the type scale. Pick three roles and fixed sizes (rem):
   - Display serif for hero headings, tight tracking (-0.02em to -0.03em), line-height 1.1.
   - Sans for body and UI, line-height 1.6.
   - Mono for code, keys, and metadata.
   - Steps: 3.0 / 2.25 / 1.75 / 1.25 / 1.0 / 0.875 / 0.75, weights 400 and 600 only.
5. Define the spacing system on a 4px base: 4, 8, 12, 16, 24, 32, 48, 64, 96. Set section padding at 96 top and bottom, card padding at 24 to 40.
6. Define the color set as named tokens:
   - Canvas warm off-white, surface white, border one light gray.
   - Text charcoal for body, one muted gray for secondary.
   - One ink button (near-black background, white text).
   - One desaturated accent pair (a pale tint plus a readable text shade) for tags and inline marks.
7. Sketch one sample layout in words and a simple ASCII frame: header, hero, a small asymmetric card grid, and a footer. Map each region to the tokens above.
8. Add a short motion note: fade and rise on entry (translateY 12px, 600ms, ease-out), animate transform and opacity only.
9. Write the spec to Projects/{slug}/final/minimalist-ui-spec.md. Mark it DRAFT at the top.
10. Write a one-line brief to Projects/{slug}/brief.md noting the surface, the date, and the source of the brand voice.

## Outputs
- Projects/{slug}/final/minimalist-ui-spec.md (DRAFT) with restraint rules, type scale, spacing system, color tokens, sample layout, and motion note.
- Projects/{slug}/brief.md with the one-line brief.
- No KPI ledger row. This skill produces a spec, not a measured result.

## Guardrails
- DRAFT-ONLY. The spec is a draft for review, not a published page or shipped CSS.
- VOICE from Library/styles/brand-voice.md. Match it in every line of copy in the spec.
- PROVENANCE. If you cite a token from an existing file, name the file. Never invent brand colors the user has not set; mark any guess as a default.
- Write only inside Projects/{slug}/. Do not touch _system/, Memory/, or Clients/.
- Keep the token set small. If the spec needs more than nine spacing steps or more than one accent pair, cut back.

## References
- Library/styles/brand-voice.md
- Company/brand.md
