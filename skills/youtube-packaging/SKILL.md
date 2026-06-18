---
name: youtube-packaging
description: Package a video for the click with title options, a thumbnail concept, and a description, tied to a click-through metric, when you say package this video, write a YouTube title, or design a thumbnail concept
---

# YouTube Packaging

Turn a finished or planned video into a package built for the click. Title options, one thumbnail concept, and a description, all pointed at a click-through metric. Draft only.

## When to use
- A video is scripted, edited, or planned and needs a title, thumbnail, and description before publish.
- An older video underperforms on click-through rate and you want a repackage to test.
- You are batching packaging for several videos and want each one tied to a measurable click target.

## Inputs
- Topic, working title, and the core promise of the video (the one thing a viewer gets).
- Target viewer, from `Company/icp.md`.
- Brand voice, from `Library/styles/brand-voice.md` (agency: the active client's voice).
- The channel's recent click-through rate, if known, for a baseline. Solo/Team: `Memory/kpi-ledger.md`. Agency: `Clients/{slug}/Memory/kpi-ledger.md` or the client brief.
- Optional: thumbnail face or product shot as a provided file, plus any series naming rules.

## Process
1. Read the inputs above. If the channel has a recent click-through rate, record it as the baseline. If not, mark the baseline `unknown` and proceed.
2. Name the promise in one sentence. Every title and the thumbnail must point at this one promise, not three.
3. Draft 6 to 10 title options across distinct angles (curiosity gap, number or result, contrarian take, question, plain how-to). Keep each under 60 characters so it survives truncation. No clickbait the video cannot pay off.
4. Score each title 1 to 5 on promise match, specificity, and scroll-stopping pull. Mark the top pick and one backup for an A/B test.
5. Write one thumbnail concept as a brief: focal subject, 3 to 5 words of overlay text, foreground and background split, color contrast, facial expression or product framing, and what to cut so it reads at phone size. Note that title and thumbnail must not repeat the same words.
6. Write the description: first 2 lines carry the hook and the promise (visible before the fold), then a 2 to 4 sentence summary, then chapters or key points, then 1 call to action, then links. Fold in target search terms naturally, no keyword stuffing.
7. Set the click target. State the current click-through rate as the baseline and the target lift you expect (for example, 4.0% to 5.0%). If the baseline is `unknown`, set a target range to confirm after launch.
8. Write the deliverable to the draft path below. Append one ledger row recording the click-through baseline and target. Do not publish, upload, or schedule anything.

## Outputs
- Solo/Team: `Content/{slug}-{date}/final/youtube-package.md` with title options and scores, the thumbnail brief, the description, and the click target. Working notes in `Content/{slug}-{date}/data/`.
- Agency: `Clients/{slug}/Projects/{project-slug}/final/youtube-package.md`, set `confidential: true` in frontmatter.
- Ledger row appended to `Memory/kpi-ledger.md` (agency: `Clients/{slug}/Memory/kpi-ledger.md`):
  `| {date} | youtube-ctr | {baseline or unknown} | {baseline or unknown} | {target} | {channel or video id} | inferred | packaging draft, pre-launch |`

## Guardrails
- Draft only. Never publish, upload, schedule, or send.
- Voice comes from `Library/styles/brand-voice.md` (agency: the active client's voice).
- Agency firewall: read and write the active client only, never a sibling client. Client outputs carry `confidential: true`.
- Provenance: cite the source for any baseline rate. Never invent metrics or view counts. When a metric moves post-launch, append a new ledger row, never edit a prior one.
- A thumbnail face, product shot, or rendering tool is an optional connector registered in `_system/connectors.md`. Default to a provided file or a precise written brief. Credentials never live in the vault.

## References
- `Company/icp.md`, `Library/styles/brand-voice.md`, `Memory/kpi-ledger.md`, `_system/connectors.md`
