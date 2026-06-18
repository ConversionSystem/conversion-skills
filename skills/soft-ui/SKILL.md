---
name: soft-ui
description: Draft a soft UI design spec with gentle depth, rounded forms, calm color, and a sample layout when you say make it soft, soften the UI, or neumorphic design
---

# Soft UI

A design spec for calm interfaces: gentle depth, rounded forms, restrained color, generous breathing room, and a worked sample layout.

## When to use
- You want a screen or component set that feels quiet and tactile instead of loud and flat.
- You need a written reference (tokens, shadows, spacing) before anyone builds.
- You want a sample layout to react to, not a finished product.

## Inputs
- Surface to design (dashboard, settings panel, card grid, form, mobile screen).
- Brand color from `Company/brand.md`, or one accent hue if none is set.
- Light or dark base preference (default: light).
- Density preference: airy or compact (default: airy).

## Process
1. Read `Company/brand.md` for accent color and tone. Read `Library/styles/brand-voice.md` so any UI copy in the sample matches voice. If neither exists, pick one calm accent and note the assumption.
2. Set the base surface. Light mode: a near-white tinted gray, not pure white. Dark mode: a soft charcoal, not pure black. Record the hex.
3. Build the color set: one accent, two neutrals (text and muted text), one success and one warning. Keep saturation low. Record hex values and contrast ratios against the surface (target 4.5:1 for body text).
4. Define depth. Two shadow recipes per element: a lighter highlight from the top-left and a softer cast to the bottom-right, both low-opacity and wide-blur. Give raised, flat, and inset variants. No hard 1px borders; let shadow do the separation.
5. Set the corner scale: small 8px, medium 16px, large 24px, pill 999px. Apply the medium radius as the default for cards and inputs.
6. Set spacing on an 8px step (8, 16, 24, 32, 48, 64). Set component padding to 24px and section gaps to 48px so the layout breathes.
7. Set type: one calm sans, four sizes (13, 15, 20, 28), line height 1.5 for body. Weight 400 for text, 600 for headings.
8. Define motion: 200ms ease for hover, press states that deepen the inset shadow, no bounce.
9. Compose one sample layout for the chosen surface. Show header, a 2 by 2 card grid, one primary button, one input, and one toggle, each annotated with the tokens it uses.
10. Write the spec and a paste-ready token block to `Projects/{slug}/final/soft-ui-spec.md`, and the sample layout notes to `Projects/{slug}/final/soft-ui-sample.md`. Mark both DRAFT at the top.

## Outputs
- `Projects/{slug}/brief.md` (one paragraph: surface, base mode, accent, density).
- `Projects/{slug}/final/soft-ui-spec.md` (DRAFT: color set, shadow recipes, radii, spacing, type, motion, token block).
- `Projects/{slug}/final/soft-ui-sample.md` (DRAFT: annotated sample layout).
- No ledger rows. This skill writes drafts only.

## Guardrails
- DRAFT-ONLY. Design files are drafts for review, never shipped from here.
- VOICE: any UI copy in the sample comes from `Library/styles/brand-voice.md`.
- PROVENANCE: state every assumption (accent, mode, density) at the top of the spec. Do not invent brand colors; if none exist, say so.
- Keep contrast at 4.5:1 or better for body text. Soft does not mean unreadable.
- Restraint over decoration: one accent, low saturation, wide soft shadows. Drop any effect that fights legibility.

## References
- `Company/brand.md`
- `Library/styles/brand-voice.md`
