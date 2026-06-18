---
name: content-plan
description: Plans top-of-funnel marketing content from company truth and recent performance then scaffolds draft content briefs tied to measurable targets, triggered by "content plan", "plan our content", "what should we post", or "build a content calendar"
---

# Content Plan

Plan marketing content grounded in the company's strategy, ICP pains, and recent performance, then scaffold draft content briefs each tied to a measurable top-of-funnel target.

## When to use
- The user asks to "plan content", "build a content calendar", or "decide what to post" for the coming weeks or a campaign.
- A new offer, strategy shift, or ICP update means content should be re-anchored to fresh truth.
- A periodic content cadence (monthly/quarterly) is due and you want themes, formats, and cadence proposed from the ledger, not from vibes.

## Inputs
- `Company/strategy.md` — current go-to-market strategy and priorities.
- `Company/icp.md` — ICP pains, triggers, objections, and language.
- `Company/brand.md` — positioning, messaging pillars, do/don't.
- `Library/styles/brand-voice.md` — tone and voice constraints for any drafted copy.
- `Memory/kpi-ledger.md` — the top-of-funnel KPI history and any per-piece performance rows.
- Recent `Content/{slug}-{date}/` directories — past briefs and `data/` to read what worked and what did not.
- Optional user input: time window, channel focus, piece count, or campaign theme.

## Process
1. Load truth. Read `Company/strategy.md`, `Company/icp.md`, `Company/brand.md`, and `Library/styles/brand-voice.md`. Extract the active strategic priority, the top 3-5 ICP pains with their language, and the messaging pillars. If any file is missing or stale (frontmatter `reviewed` is old), note the gap and proceed with what exists; do not invent facts.
2. Read performance. Open `Memory/kpi-ledger.md` and identify the top-of-funnel KPI the plan should move (e.g., qualified visits, subscribers, leads) with its baseline, current, and target. Scan recent `Content/{slug}-{date}/` briefs and their `data/` for format and theme performance signals. Mark confidence per signal as confirmed/reported/inferred/stale.
3. Derive themes. Map 3-6 content themes directly to specific ICP pains and the strategic priority. For each theme, name the pain it answers, the angle, and why now. Reject any theme that does not trace to a pain or priority.
4. Choose formats and cadence. For each theme, pick a format (article, short video, carousel, email, etc.) justified by past performance signals and channel fit, then propose a cadence (e.g., 2 pieces/week for 4 weeks) sized to the user's window and capacity.
5. Set targets. Tie the whole plan to the one top-of-funnel KPI it should move, and give each piece a measurable target (e.g., reach, click-through, subscribes) plus exactly how it will be measured (which metric, which source). Targets must be concrete numbers, not adjectives.
6. Present plan for approval. Summarize themes, formats, cadence, the KPI, and per-piece targets. Get human confirmation on which pieces to scaffold before writing files.
7. Scaffold chosen pieces. For each approved piece, create `Content/{slug}-{date}/` with a kebab-case slug and ISO date, write `brief.md` (with universal frontmatter, `status:draft`, `generated:false`), write `data/baseline.json` capturing the starting metric values and measurement source, and create an empty `final/` directory for the eventual deliverable.
8. Log the plan. Append one summarizing row to `Memory/kpi-ledger.md` recording the target for the top-of-funnel KPI this plan is meant to move. Never edit or reorder prior rows.

## Outputs
- One directory per chosen piece under `Content/{slug}-{date}/`, each containing:
  - `Content/{slug}-{date}/brief.md` — the content brief with universal frontmatter (`type:content-brief`, `status:draft`, `owner`, `date`, `reviewed`, `tags` >=2, `confidential`, `source`, `generated:false`), the theme, the ICP pain it answers, format, target, and how it will be measured.
  - `Content/{slug}-{date}/data/baseline.json` — starting metric values and the measurement source for this piece.
  - `Content/{slug}-{date}/final/` — empty directory for the eventual draft deliverable.
- One appended row in `Memory/kpi-ledger.md` using the exact columns `| date | metric | baseline | current | target | source | confidence | note |`, recording the top-of-funnel KPI target for this plan, with `confidence` in {confirmed,reported,inferred,stale}.
- A plan summary returned to the user: themes, formats, cadence, KPI, and per-piece targets.

## Guardrails
- Draft-only. Never publish, schedule, or send any piece; all briefs are written `status:draft` and all deliverables stay in `final/` for human action.
- Truth-sourced only. Every theme must trace to an ICP pain or strategic priority; never invent pains, metrics, or performance signals. If truth files are missing, surface the gap rather than guessing.
- Human-approval gate before scaffolding files (Process step 6) and before any future publishing step.
- KPI ledger is append-only with the exact column order; never edit, reorder, or overwrite prior rows. Generated rollups carry `generated:true` and are not hand-edited.
- Route facts to canonical homes; use kebab-case slugs and ISO dates for all `Content/{slug}-{date}/` directories.
- Respect the Agency client firewall: never read sibling `Clients/{slug}/` directories; route anything ambiguous to `Inbox/`.

## References
none
