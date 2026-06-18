---
name: youtube-ideation
description: Generates a batch of video ideas for one channel from its niche, audience, and goal, each with its angle, its promise, and why it earns the click, written to Content as a draft - triggers on /youtube-ideation, "video ideas", "ideas for my channel", "what should I make a video about", "YouTube ideation", "brainstorm YouTube videos"
---

# YouTube Ideation

Generates a ranked batch of video ideas for one channel, grounded in its niche, its viewer, and one channel goal, each idea carrying its angle, its one-line promise, and the reason a viewer clicks. DRAFT-ONLY: a human picks which ones get made.

## When to use

- You run (or run a client's) YouTube channel and want a batch of concrete video ideas tied to the audience and a goal, not a generic topic dump.
- You are filling a content calendar, planning the next 10-20 uploads, or breaking a dry spell and want ideas with an angle and a click reason already attached.
- NOT for writing the title and thumbnail of one chosen idea (use the youtube-packaging skill) and NOT for outlining or scripting a video (use the youtube-outline and youtube-scripting skills). This skill ends at "here are the ideas worth making."

## Inputs

- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md`. Agency profile: the CLIENT's `Clients/{slug}/context/brand.md` instead.
- **Channel niche and goal:** `Company/strategy.md` and `Company/profile.md` (Agency: `Clients/{slug}/context/`) · what the channel is about and the one goal this batch serves (subscribers, watch time, leads to an offer, authority on a topic).
- **The viewer:** `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) · who watches, what they already know, and the job they hire a video to do.
- **The offer (if the goal is leads):** `Company/offers.md` (Agency: `Clients/{slug}/context/offers.md`) · what an idea can route a viewer toward.
- **What already exists:** prior YouTube briefs, outlines, or idea batches in `Content/`, plus the channel's past topics, so the batch avoids repeats and spots gaps.
- **The metric baseline:** `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) · current subscriber, view, or watch-time baseline if one is recorded.
- **From the user (ask only for genuine gaps):** the channel niche, the one goal for this batch, and how many ideas they want (default 15).

## Process

1. **Resolve profile and write location.** Solo/Team: write to `Content/youtube-ideas-{date}/`, ledger is `Memory/kpi-ledger.md`. Agency: resolve the active client, obey the FIREWALL (read only that client's `Clients/{slug}/`), write to `Clients/{slug}/work/youtube-ideas-{date}/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill.
2. **Load voice, then context.** Read the voice files first, then niche, the channel goal, the viewer, the offer (if goal is leads), and the list of past topics. Confirm in one line what you found ("Voice: blunt, builder-to-builder; viewer: solo founders pre-revenue; goal this batch: subscribers; 15 ideas; avoid the 6 topics already covered") and ask only for what is absent (the niche, the one goal, the count).
3. **Fix the goal and the viewer's job.** State the single goal this batch serves and the job the viewer hires a video to do, grounded in `Company/icp.md`. An idea that does not move the goal or do the viewer's job does not make the list.
4. **Map the territory.** List the topic clusters the niche covers, mark which the channel already owns (from past topics), and name the gaps and adjacent territory worth a video. This is where ideas come from · proven clusters with a fresh take, plus the open gaps.
5. **Generate ideas against angle frames.** Draft the requested count (default 15), each from a distinct angle frame so the batch is varied, not 15 versions of one idea. Frames to draw from: the contrarian take, the specific number or result, the costly mistake, the head-to-head comparison, the behind-the-scenes teardown, the beginner's first step, the "I tried X for N days," the myth correction. Reject ideas that only restate a topic the channel already covered.
6. **Give each idea its angle, promise, and click reason.** For every idea write: the working idea (one line), the **angle** (the specific take that makes it not generic), the **promise** (the one thing the viewer walks away with), the **click reason** (why this viewer stops scrolling for it), the format and rough length, and the goal it serves. Keep every claim real · cite a source for any stat referenced and invent no view counts or results.
7. **Rank the batch.** Order the ideas by a stated call on click pull against effort-to-produce, so the user reads the strongest-for-the-goal first. State the ranking basis in one line; do not fabricate a predicted view number.
8. **Instrument.** Add a `## Metrics to track` block tied to the batch goal: which idea ships, its views or watch time or subscriber lift against the channel's current baseline band, and the one decision the result drives (make more of this angle, or drop it).
9. **Persist as a draft.** Write the deliverable with `status:draft` and full universal frontmatter, write the brief and data intermediates, and append the ledger row (see Outputs). Close with the next action (a human picks the ideas to make; pair with the youtube-packaging skill to title and thumbnail a chosen idea).

## Outputs

- **Deliverable** → `Content/youtube-ideas-{date}/final/ideas.md` (Solo/Team) or `Clients/{slug}/work/youtube-ideas-{date}/final/ideas.md` (Agency), `status:draft`, with: the stated goal and viewer job · the territory map (owned clusters and gaps) · the ranked idea list, each idea carrying its angle, promise, click reason, format and length, and the goal it serves · the ranking basis · `## Metrics to track` · sources. Universal frontmatter on the file (type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated). `type: youtube-ideation`; Agency files are `confidential:true`.
- **Brief** → same folder `brief.md`: the niche, the one goal, the viewer and their job, the count requested, topics to avoid, and acceptance criteria.
- **Intermediate data** → same folder `data/`: `baseline.json` (the goal, the KPI being moved, and current channel baseline if known) and `inputs.json` (the context snapshot drafted from, including the past-topics list used to avoid repeats).
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - `metric` = the channel goal this batch serves (e.g. `youtube subscribers` or `youtube watch-time minutes`); `baseline`/`current` = known value or `unset`; `target` = the goal for the batch if the user set one, else `unset`; `source` = the channel analytics source or `inferred`; `confidence` in {confirmed, reported, inferred, stale}; `note` = the ideas-batch slug + that this is a draft idea set, not a published video.
  - If no baseline exists, SEED a first row (baseline = current = the user-confirmed number, or `inferred` if estimated) and FLAG it for the user to confirm · never invent a baseline.
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY.** Produce `status:draft`. Never publish, upload, schedule, or post a video · this skill produces ideas a human chooses from. A connector may only push a DRAFT, never go live.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` before writing (Agency: the CLIENT's `Clients/{slug}/context/brand.md`). If the voice file is thin, ask for one real sample rather than improvising a voice.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Every number is real and traceable to `goals.md`/`Memory/`/a user-named source; cite external facts with their source URL; invent no view counts, subscriber numbers, or results. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- Every idea earns its place against the one goal and the viewer's job; an idea with no angle and no click reason is cut.
- The batch is varied by angle frame, not the same idea restated; ideas that repeat a topic the channel already owns are dropped unless the angle is genuinely new.
- No required database or paid vendor; work from the vault and user-provided channel context. Treat any keyword tool, analytics API, or platform connector as an OPTIONAL upgrade only if registered in `_system/connectors.md`.
- A delivery run without its ledger row is unfinished.
- Original expression only; no lifted titles or competitor copy.

## References

- `Company/icp.md`, `Company/brand.md`, `Company/strategy.md`, `Company/profile.md`, `Company/offers.md`, `Library/styles/brand-voice.md` (Agency: the matching files under `Clients/{slug}/context/`)
- `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency)
- `_system/connectors.md` · OPTIONAL keyword, analytics, and platform draft-push connectors; zero-infra default needs none.
