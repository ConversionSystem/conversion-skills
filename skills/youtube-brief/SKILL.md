---
name: youtube-brief
description: Drafts one YouTube video brief locking the single idea, the audience, the hook, the goal metric, and the call to action, written to Content as a draft - triggers on /youtube-brief, "write a video brief", "brief this YouTube video", "what's the hook for this video", "plan a YouTube video", "video brief", "youtube brief"
---

# YouTube Brief

Drafts one tight video brief that locks the single idea, who it is for, the hook, the one goal metric, and the call to action before anyone writes a script or films. DRAFT-ONLY: a human approves it.

## When to use

- You have a video topic and want it pinned down to one idea, one audience, one hook, and one goal before scripting or filming.
- You want a shared brief the script, the thumbnail, and the title all answer to, so the video stays on one promise.
- NOT for the full script or outline (that is a later step), and NOT for a written blog post (use the blog-post skill). Pairs with content-plan (a slot feeds the brief) and repurpose (turn the shipped video into posts and an email).

## Inputs

- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md`. Agency profile: the CLIENT's `Clients/{slug}/context/brand.md` instead.
- **Audience:** `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) · who the video is for and the job they want done.
- **The one CTA:** `Company/offers.md` (Agency: `Clients/{slug}/context/offers.md`) · the offer the single call to action points to.
- **Source signal (if any):** a `content-plan` slot, a strong post or teardown in `Content/`, a lesson in `Memory/lessons.md`, or a case study in `Operations/case-studies/` the video can be built on.
- **The metric baseline:** `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) · to read any current views, watch-time, or subscriber baseline.
- **From the user (ask only for genuine gaps):** the topic or angle, the goal of this one video (views, watch-time, leads, subscribers), and which offer the CTA points to.

## Process

1. **Resolve profile and write location.** Solo/Team: write to `Content/{slug}-{date}/`, ledger is `Memory/kpi-ledger.md`. Agency: resolve the active client, obey the FIREWALL (read only that client's `Clients/{slug}/`), write to `Clients/{slug}/work/{slug}-{date}/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill.
2. **Load voice, then context.** Read the voice files first, then ICP, offers, and any source signal. Confirm in one line what you found ("Voice: plain, numbers over adjectives; viewer: ops leads at 20-100-person agencies; goal: leads; CTA: the free audit") and ask only for what is absent (the topic, the goal, the offer).
3. **Lock the ONE idea.** One video, one idea, stated in a single sentence a viewer could repeat. If two ideas compete, cut one or hold it for a separate brief.
4. **Name the audience and the job.** State exactly who this video is for, grounded in `Company/icp.md`, and the one job they came to get done. A video for everyone is a video for no one.
5. **Write the hook.** Draft 3 hook options for the first 15 seconds, each naming the viewer's problem or the payoff fast, no warm-up. Mark the recommended one and say in a line why it earns the watch.
6. **Set the one goal metric.** Pick the single metric this video is built to move (views, average view duration or watch-time, subscribers, or leads to the offer), with a benchmark band and the one decision the result drives. One video, one goal.
7. **Write the call to action.** One CTA tied to `Company/offers.md` (Agency: the client's offers), placed where the viewer has earned the ask. Never bolt an audit or report CTA onto the video; the CTA is the user's own offer.
8. **Persist as a draft.** Write the brief with `status:draft` and full universal frontmatter, write the data intermediates, and append the ledger row (see Outputs). Close with the next action (a human approves, then the outline or script step runs).

## Outputs

- **Brief** → `Content/{slug}-{date}/brief.md` (Solo/Team) or `Clients/{slug}/work/{slug}-{date}/brief.md` (Agency), `status:draft`, with: the one idea (single sentence) · the audience and the job · 3 hook options with the recommended one marked · the one goal metric with its benchmark band · one offer-tied CTA · acceptance criteria. Universal frontmatter on the file (type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated). `type: youtube-brief`; Agency files are `confidential:true`.
- **Intermediate data** → same folder `data/`: `baseline.json` (the one goal metric and its current baseline if known) and `inputs.json` (the context snapshot drafted from).
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - Brief-written row, e.g. `| 2026-06-18 | video-briefs | 4 | 5 | 12 | Content/{slug}-2026-06-18/ | confirmed | brief: the onboarding teardown |`.
  - **Goal metric:** if a baseline for the chosen metric (views, watch-time, subscribers, leads) exists, append the current value with `confidence` in {confirmed, reported, inferred, stale} and its source. If none exists, SEED a first row (baseline = current = the user-confirmed number, or `inferred` if estimated) and FLAG it for the user to confirm · never invent a baseline.
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY.** Produce `status:draft`. Never publish, upload, schedule, or post the video or brief autonomously · a human approves it.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` before writing (Agency: the CLIENT's `Clients/{slug}/context/brand.md`). If the voice file is thin, ask for one real sample rather than improvising a voice.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Every number is real and traceable to `goals.md`/`Memory/`/a user-named source; cite external facts; invent no views, watch-time, or results. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- One video, one idea, one goal metric, one CTA. A brief for everyone serves no one.
- Content ships clean: the CTA is the user's own offer · never append an audit or report CTA into the brief.
- A delivery run without its ledger row is unfinished.
- Original expression only; no lifted hooks, titles, or competitor copy.

## References

- `Company/icp.md`, `Company/brand.md`, `Library/styles/brand-voice.md`, `Company/offers.md` (Agency: `Clients/{slug}/context/icp.md`, `Clients/{slug}/context/brand.md`, `Clients/{slug}/context/offers.md`)
- `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency)
- `_system/connectors.md` · OPTIONAL YouTube analytics or upload connectors (real view/watch-time benchmarks, draft upload); zero-infra default needs none.
