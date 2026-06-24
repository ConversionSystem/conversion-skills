---
name: redesign
description: Redesign a page or screen by auditing the current version then giving an improved direction with layout, type, color, and reasons, triggered by "redesign this page", "improve this screen", or "rework the UI"
---

# Redesign

Audit a page or screen as it stands today, then propose a stronger direction with specific calls on layout, type, color, and the reasoning behind each. Writes a draft to Projects/.

## When to use

- A landing page, signup screen, pricing table, or dashboard is underperforming or looks dated.
- You want a second read on hierarchy, readability, or visual weight before a rebuild.
- A stakeholder asks "make this look better" and you need a concrete, defensible plan.
- You have a screenshot, a URL, or raw markup and want a structured redo, not vibes.

## Inputs

- The current page: a URL, a screenshot, exported markup, or a written description.
- The page's job: one sentence on what a visitor should do or feel.
- Brand constraints from `Library/styles/brand-voice.md` and `Company/brand.md` (fonts, color, tone).
- Audience notes from `Company/icp.md` (who reads this, on what device).
- Any measured results so far (bounce, scroll depth, conversion) if they exist.

## Process

1. Read `Company/brand.md`, `Library/styles/brand-voice.md`, and `Company/icp.md`. Pull the locked fonts, color values, and voice so the redesign stays on brand.
2. Restate the page's one job in a single sentence. Everything below gets judged against it.
3. Audit the current version. Walk it top to bottom and note, for each: what the eye hits first, where attention leaks, what is unreadable, what is decoration with no job. Score four areas 1 to 5 with a one-line reason each: hierarchy, readability, color use, layout rhythm.
4. Name the three highest-cost problems. For each, write the symptom, the likely cause, and what it costs the page's one job.
5. Propose the new direction as four explicit calls, each with the reasoning:
   - Layout: the grid, the section order, what goes above the fold, what gets cut. Say why this order serves the one job.
   - Type: the scale (sizes for h1, h2, body, caption), line length target, and weight pairings. Tie every size back to hierarchy.
   - Color: the role of each value (background, text, one action color), contrast ratios for the action and body text, and what the action color points the eye toward.
   - Components: the hero, the proof block, the action block, and how each earns its place.
6. Write a before-to-after table: each fix, the old state, the new state, the reason.
7. List what you did not change and why, so the rebuild does not over-correct.
8. Write the draft to `Projects/{slug}/redesign-{date}.md`. If raw HTML or CSS is part of the direction, write it to `Projects/{slug}/data/` as a draft, never live.

## Outputs

- `Projects/{slug}/redesign-{date}.md`: the audit, the four-area scores, the three problems, the new direction with reasoning, and the before-to-after table.
- `Projects/{slug}/data/`: any draft HTML, CSS, or layout markup, marked DRAFT.
- One ledger row in `Memory/kpi-ledger.md` only if a baseline metric for this page exists, recording the metric and its source. Append only, never edit prior rows.

## Guardrails

- DRAFT-ONLY. Nothing here ships or publishes. The rebuild is a human decision.
- VOICE comes from `Library/styles/brand-voice.md`. Match it in every label and headline you propose.
- Stay inside brand fonts and color from `Company/brand.md`. If a call breaks brand, flag it and say why, do not silently override.
- PROVENANCE. Cite any metric you reference to its source. Never invent numbers to justify a change.
- FIREWALL. For client work, read and write only the active client's folder under `Clients/{slug}/`.
- Contrast every action color and body text against its background. State the ratio, do not guess.

## References

- `Company/brand.md`
- `Library/styles/brand-voice.md`
- `Company/icp.md`
- `Memory/kpi-ledger.md`
- `/a11y-audit` - run it on the redesigned page for a WCAG 2.1 AA accessibility pass; contrast and focus states are design decisions.
