---
name: youtube-scripting
description: Writes a full video script from an outline in the channel voice with spoken lines, on-screen notes, and b-roll cues, say "write the script" or "/youtube-scripting"
---

# YouTube Scripting

Turns an approved outline into a complete, shootable script in the channel's voice, with spoken lines, on-screen text, and b-roll cues.

## When to use
- An outline exists for a video and you want the full word-for-word script.
- A creator or client wants a draft they can read to camera or hand to an editor.
- You are extending a content piece from beat sheet to finished script before a shoot.

## Inputs
- The outline at `Content/{slug}-{date}/data/outline.md` (or a pasted outline if no file exists yet).
- The video brief at `Content/{slug}-{date}/brief.md` for goal, audience, length target, and call to action.
- Voice reference: `Library/styles/brand-voice.md` (Solo/Team). Agency: the client's voice file under `Clients/{slug}/` or the project brief.
- Optional: prior scripts in `Content/` to match cadence, recurring segments, and sign-off.

## Process
1. Read the brief and outline. Confirm the working title, the audience, the runtime target, and the one action the viewer should take at the end. If any of these are missing, note the gap at the top of the draft and proceed with a stated assumption.
2. Load the voice file. Pull 5 to 8 concrete markers: sentence length, contractions, recurring phrases, humor level, how the host opens and closes. Match these, do not invent a new voice.
3. Write a hook for the first 15 seconds. State the payoff in plain words and give the viewer a reason to stay. Keep it under 40 spoken words.
4. Expand each outline beat into spoken lines. Write the way the host talks, short sentences, one idea per line. Read it aloud in your head and cut any line that does not earn its place.
5. For every section, add an on-screen note (text, lower-third, or caption) and a b-roll cue (what the editor shows while the host speaks). Mark these clearly so they are easy to strip later.
6. Place a mid-roll retention beat near the one-third and two-third marks: an open loop, a question, or a pattern break that pulls the viewer forward.
7. Write the call to action from the brief. One ask, stated once, in the host's words. No stacking three asks at the end.
8. Add an end screen line: what to watch next and the sign-off the channel always uses.
9. Estimate runtime at roughly 130 to 150 spoken words per minute. Compare to the target and flag if the draft runs long or short.
10. Save the script to `Content/{slug}-{date}/final/script.md`. Mark it DRAFT at the top. Do not publish, upload, or schedule anything.

## Outputs
- `Content/{slug}-{date}/final/script.md`: the full script, each section showing SPOKEN lines, an ON-SCREEN note, and a B-ROLL cue, plus hook, retention beats, call to action, and sign-off. Marked DRAFT.
- A short header block in the same file: working title, runtime target vs estimate, audience, the one viewer action, and any assumptions made.
- A ledger row in `Memory/kpi-ledger.md` only if this script ships and a tracked metric (for example, planned video count or content output) moves. Append, never edit a prior row: `| date | metric | baseline | current | target | source | confidence | note |`.

## Guardrails
- Draft only. Never publish, upload, schedule, or send. The creator records and posts.
- Voice comes from the voice file. Agency work uses the client's voice, never the house voice, and the file is written `confidential: true`.
- Cite any stat, quote, or claim the host says on camera. Never invent numbers, studies, or testimonials. If a figure is unverified, mark it `[verify]` in the script.
- Agency firewall: read only the active client's folder, never a sibling client.
- Keep on-screen notes and b-roll cues visually distinct from spoken lines so an editor or host can scan the page fast.

## References
- `Content/{slug}-{date}/data/outline.md`
- `Content/{slug}-{date}/brief.md`
- `Library/styles/brand-voice.md`
