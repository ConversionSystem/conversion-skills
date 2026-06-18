---
name: taste
description: Critiques a UI or page against design principles, scores hierarchy spacing contrast type and rhythm, and lists the specific fixes that raise it. Triggers on "taste check", "critique this design", "score this page", "is this UI any good", "what would make this look better".
---

# Taste

Score a UI or page against five design principles, then hand back the exact changes that move each score up. Draft only, written to Projects/.

## When to use
- You have a screenshot, a live URL, or a built page in Projects/{slug}/ and want an honest read on how it looks.
- A draft from another skill (a landing page, an email, a one-pager) needs a design pass before it ships.
- You are choosing between two layouts and want a scored comparison, not a vibe.
- A page converts poorly and you suspect the look is the leak, not the copy.

## Inputs
- The artifact to critique: a screenshot path, an image, a URL, or a file in Projects/{slug}/.
- Optional: the page goal in one line (what the visitor should do next), so scoring weights the right things.
- Brand voice and visual rules from Library/styles/brand-voice.md and Company/brand.md, when they exist.
- Optional: a second variant to compare against.

## Process
1. Restate the goal of the page in one sentence. If none was given, infer it from the content and note the assumption.
2. Capture the artifact. For a URL or live page, use the browse skill to take a full screenshot at desktop and mobile widths. For a file, read it. Save reference shots to Projects/{slug}/data/.
3. Score each of the five principles 0 to 10, with a one-line reason per score:
   - Hierarchy: does the eye land on the most important thing first, then move in the intended order.
   - Spacing: is whitespace used to group and separate, or is everything cramped or floating.
   - Contrast: do foreground and background, active and inactive, primary and secondary read clearly. Check text legibility against WCAG AA as a floor.
   - Type: is the typographic scale consistent, are line lengths 45 to 90 characters, is line height comfortable, are there too many fonts or weights.
   - Rhythm: do margins, gaps, and component sizes follow a repeating scale, or do values look hand-picked and uneven.
4. Compute the overall score as the mean of the five, rounded to one decimal. Flag any principle under 6 as a blocker.
5. For every score under 9, write a specific fix: the element, the current value, the proposed value, and the principle it lifts. No vague advice. "Raise the H1 to 48px and drop the subhead to 18px to restore hierarchy", not "improve the hierarchy".
6. Rank the fixes by points gained per minute of effort, so the cheapest wins come first.
7. If a second variant was given, repeat steps 3 to 5 for it and add a short verdict on which wins and why.
8. Write the critique to Projects/{slug}/final/taste-{date}.md as a draft. Append one row to Memory/kpi-ledger.md recording the overall score so re-runs chart the trend.

## Outputs
- Projects/{slug}/final/taste-{date}.md, a draft holding: goal, the five scores with reasons, overall score, blockers, the ranked fix list, and the variant verdict if any.
- Reference screenshots in Projects/{slug}/data/.
- One appended row in Memory/kpi-ledger.md: | {date} | taste-score | {prior or blank} | {overall} | 9.0 | taste skill | {high or medium} | {slug}, {one-line note} |.

## Guardrails
- Draft only. Nothing here is published or pushed live. The fixes are recommendations, not edits to the source.
- Score against the stated goal, not personal preference. If the goal is unknown, say so rather than guess silently.
- Cite what you measured. Contrast ratios, pixel values, and character counts come from the artifact, never invented.
- Use brand rules from Library/styles/brand-voice.md when they exist. Brand consistency beats novelty.
- kpi-ledger.md is append-only. Add a row, never edit a prior one.
- Firewall: for a client artifact, read and write only inside the active Clients/{slug}/ tree.

## References
- Library/styles/brand-voice.md
- Company/brand.md
- Memory/kpi-ledger.md
- browse skill, for capturing live pages
