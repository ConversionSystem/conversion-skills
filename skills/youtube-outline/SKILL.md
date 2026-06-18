---
name: youtube-outline
description: Structure a video outline from a brief with the hook, beats, retention turns, payoff, and call to action, triggered by /youtube-outline, "outline this video", or "structure my YouTube video". Draft only.
---

# YouTube Outline

Turn a video brief into a filmable outline: the hook, the beats, the retention turns, the payoff, the call to action. Draft only.

## When to use
- You have a brief (from a content brief skill or written by hand) and need a section by section plan before scripting.
- You want to lock pacing, demo placement, and on screen visuals before you write a word of script.
- You are deciding where retention turns go so viewers stay past the first 30 seconds.

## Inputs
- A video brief: the main outcome, the points to cover, the proof or demos available. From `Content/{slug}-{date}/brief.md` if it exists, or pasted by the user.
- `Company/icp.md` for audience context (pacing, depth, what they already know).
- `Company/strategy.md` for format preferences and the channel's typical structure.
- `Library/styles/brand-voice.md` for tone on transitions and the call to action (agency: the active client's voice file).
- Optional: a target length and a video type (tutorial, essay, list, case study, contrarian take).

## Process
1. Read the brief. Pull the one sentence outcome, the ordered points, and every piece of proof or demo named. If no brief exists, ask for one or build a 5 line version with the user before continuing.
2. Read `Company/icp.md` and `Company/strategy.md`. Set pacing and complexity to the audience. Note the channel's default structure so the outline matches what works.
3. Name the video type and a target length. Map points to a rough minute budget so the total lands near the target.
4. Draft the hook. Write 3 options in under 15 seconds each: a promise hook (what the viewer leaves with), a story open, a contrarian open. State the promise the rest of the video pays off.
5. Lay out the beats. Propose a section by section structure, each with a name, its purpose, the points it covers (mapped from the brief), and an estimated duration. Show the running total.
6. Place the retention turns. For each section boundary, write the line or move that pulls the viewer forward: an open loop, a payoff tease, a pattern break, a "but here is the catch." Mark where attention tends to drop.
7. Detail each section. For every beat, note the talking points, the demo or proof shown (cited from the brief, never invented), the transition into the next beat, and what is on screen (face cam, screen recording, diagram slide, B roll).
8. List the visual needs. Collect every diagram, slide, or visual aid: what it shows, where it appears, a complexity estimate. This feeds a visual or diagram skill later.
9. Mark the demo and example checklist. For each section, call out which points need a live demo, a use case, or a resource, so nothing is vague before scripting.
10. Write the payoff and the call to action. State the resolution that closes the promise from the hook. Draft one call to action in the brand voice, tied to one next step. Draft only, never publish or post.
11. Write the outline to `Content/{slug}-{date}/final/outline.md` (Solo and Team). Agency: write to `Clients/{slug}/Content/{date}/final/outline.md` with `confidential: true`, and read only the active client.

## Outputs
- `Content/{slug}-{date}/final/outline.md` (Solo and Team), or `Clients/{slug}/Content/{date}/final/outline.md` (Agency): hook options, beat structure with durations, retention turns, on screen plan, visual needs list, demo and example checklist, payoff, and call to action.
- A frontmatter `status: draft` on the outline file.
- If this outline sets or revises a target view or watch time number, append one row to `Memory/kpi-ledger.md` with the exact columns; never edit a prior row.

## Guardrails
- DRAFT-ONLY. Never publish, schedule, post, or contact anyone.
- VOICE from `Library/styles/brand-voice.md` (agency: the client's voice file).
- FIREWALL (agency): only the active client, never read a sibling, outputs carry `confidential: true`.
- PROVENANCE: every demo, stat, or quote in the outline traces to the brief or a cited source. Never invent metrics or proof. If a number moves, append a ledger row.
- No em-dashes in any drafted copy. Numbers over adjectives, verbs over nouns.

## References
- `Company/icp.md`, `Company/strategy.md`, `Library/styles/brand-voice.md`
- `Memory/kpi-ledger.md` (append-only)
