---
name: stitch
description: Assemble a full page from sections and components in the right order with consistent transitions and a system that holds them together, run it when you say stitch the page, assemble the page, or put the sections together
---

# Stitch

Take a pile of approved sections and components and assemble them into one coherent page: the order they appear, the transitions between them, and the shared system (spacing, type, color, motion) that makes them read as one thing instead of a stack of parts.

## When to use

- You have individual sections drafted (hero, proof, offer, FAQ, close) and need them combined into a single page.
- A page reads like disconnected blocks: spacing jumps, headings change size for no reason, buttons look different section to section.
- You are moving from a section library to a finished layout and want the order and rhythm decided once, on purpose.
- You want a repeatable page skeleton you can reuse across offers without redrawing every block.

## Inputs

- The sections to assemble, as files in `Projects/{slug}/data/sections/` or pasted in line.
- `Company/brand.md` for type scale, color tokens, and spacing rules.
- `Library/styles/brand-voice.md` for headline and microcopy voice.
- `Company/offers/` for the offer this page sells, so the order serves one ask.
- Optional: an existing page in `Projects/{slug}/final/` to match or extend.

## Process

1. Read `Company/brand.md` and `Library/styles/brand-voice.md`. Pull the type scale, the spacing unit, the color tokens, and the motion rules into a short system block you will apply to every section.
2. List the sections you were given. Tag each one by job: open, prove, explain, ask, reassure, close.
3. Decide the order. One page, one ask. Lead with the open, build proof before the ask, place objection handling right before the close. Write the order as a numbered outline before you assemble anything.
4. Set the spacing rhythm. Pick one vertical spacing unit from the brand file and apply it between every section so the gaps are even. Note where a larger gap signals a new movement.
5. Normalize the shared elements. Make headings follow one type scale, buttons share one style and label voice, and links share one color. Resolve any section that fought the system.
6. Define the transitions. For each seam between sections, state how the reader moves: a connecting line of copy, a shift in background, a repeated visual marker. No hard cuts that drop the reader.
7. Assemble the full page in order, section by section, with the system applied and the transitions written in.
8. Walk the page top to bottom once as a reader. Mark any spot where the rhythm breaks, a style drifts, or the next section does not follow. Fix each, then walk it again.
9. Write the assembled page and an assembly map to `Projects/{slug}/final/`. Keep it a draft.

## Outputs

- `Projects/{slug}/final/page.md` · the full assembled page, in order, marked DRAFT.
- `Projects/{slug}/final/assembly-map.md` · the section order, the job tag per section, the spacing unit, and the transition note for each seam.
- `Projects/{slug}/data/system-block.md` · the type scale, color tokens, spacing unit, and motion rules applied, so a re-run reuses the same system.

## Guardrails

- DRAFT-ONLY. The page is outbound, so it ships as a draft for a human to approve before it goes live.
- VOICE from `Library/styles/brand-voice.md`. Headlines and microcopy follow it, no exceptions added during assembly.
- One page, one ask. If the sections push two different asks, stop and flag it rather than stitching a page that splits attention.
- PROVENANCE. Every metric or claim inside a section keeps its source. Do not invent proof to fill a gap in the order.
- Do not rewrite a section's substance during assembly. Stitch adjusts order, spacing, transitions, and shared style only. Content changes go back to the section that owns them.
- Write only inside `Projects/{slug}/`. Read brand and voice files, never edit them here.

## References

- `Company/brand.md`
- `Library/styles/brand-voice.md`
- `Company/offers/`
