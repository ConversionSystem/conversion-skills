---
name: weekly-review
description: Roll up the past week into Daily/YYYY-Www-review.md leading with what is behind, then surface next-week Top 3 candidates and a follow-up nudge, when asked to run a weekly review or close out the week
---

# Weekly Review

Compose the week's rollup: lead with what is behind, then wins, drag patterns, metric movement, cadence check, and next-week Top 3 candidates.

## When to use
- End of a working week (or start of the next), to close out the prior week and set direction.
- When asked to "run the weekly review", "roll up the week", "close out the week", or "do the Www review".
- Before a monthly `/business-review`, to feed it a clean week-by-week trail.

## Inputs
- The week's `Daily/YYYY-MM-DD.md` notes (Monday through Sunday of the target ISO week).
- `Pipeline/deals.md` — current deal stages and movement (Solo and Team modes).
- Any client reports under `Clients/{slug}/` that the operator owns — respect the agency firewall; read only the operator's own clients, never sibling clients.
- `Memory/kpi-ledger.md` — metric baseline/current/target rows for movement analysis.
- `Operations/reviews/` and the prior `Daily/YYYY-W(ww-1)-review.md` (last week's review) for cadence and carried-over Top 3.
- Target ISO week (default: the week just ended). Confirm the week number and its date range before reading.

## Process
1. **Resolve the window.** Compute the target ISO week (`YYYY-Www`) and its Monday–Sunday date range. Default to the week that just ended. List the `Daily/YYYY-MM-DD.md` files that fall inside it.
2. **Read the week.** Load each daily note in range, `Pipeline/deals.md`, the operator's own `Clients/{slug}/` reports, and `Memory/kpi-ledger.md`. Load last week's review (`Daily/YYYY-W(ww-1)-review.md`) if it exists.
3. **Lead with what is behind.** Before anything else, identify what slipped: carried-over Top 3 that did not land, deals that stalled, stale context (`reviewed` dates past their cadence), missed cadence items. State it plainly at the top — this section opens the review.
4. **Collect wins.** Pull concrete wins from the daily notes and deal movement. Every win links to its evidence file (e.g. `[shipped landing page](../Projects/acme-relaunch/final/index.html)`). No win without a file reference.
5. **Name what dragged.** Identify the *pattern* behind the drag — a recurring cause (e.g. "discovery calls slipping to next day"), not a list of excuses. One pattern, stated honestly.
6. **Read metric movement.** From `Memory/kpi-ledger.md`, report each tracked metric's baseline → current → target and direction. Flag any row with `confidence: stale` as needing a refresh. Never edit or reorder ledger rows — read only.
7. **Cadence check.** Confirm whether the week's expected rituals ran (dailies written, reviews logged, pipeline touched). Note gaps.
8. **Next-week Top 3 candidates.** Propose three candidate priorities for the coming week, drawn from what is behind plus open deals and stale context. Mark as candidates, not commitments — the operator confirms.
9. **Compose the review.** Write `Daily/YYYY-Www-review.md` with full frontmatter (`generated: true`), in this section order: What's Behind → Wins → What Dragged → Metric Movement → Cadence Check → Next-Week Top 3 Candidates → Suggested Follow-up.
10. **Suggest a follow-up.** End with one concrete nudge: e.g. run `/business-review` if a month has closed, refresh the stale ledger rows flagged in step 6, or re-review context files past their cadence.

## Outputs
- `Daily/YYYY-Www-review.md` — the generated weekly rollup, frontmatter `generated: true`, `type: review`, `status: final`, sections in the order above. Never hand-edited after generation; re-run this skill to refresh it.
- No KPI ledger rows are written by this skill — it reads `Memory/kpi-ledger.md` only. If the review surfaces a new confirmed metric the operator wants tracked, that is a separate append by the operator to `Memory/kpi-ledger.md` (append-only, exact columns, never reorder prior rows).

## Guardrails
- Generated artifact: `Daily/YYYY-Www-review.md` carries `generated: true` and is never hand-edited — re-run to refresh.
- Append-only ledger: read `Memory/kpi-ledger.md` only; never edit, reorder, or rewrite existing rows. New rows are the operator's manual append.
- Agency firewall: read only the operator's own `Clients/{slug}/` reports; never read sibling clients. If ownership is ambiguous, route the question to `Inbox/` and skip that client.
- Human-approval gates: Top 3 are candidates, not commitments, and follow-up is a suggestion — never auto-send, publish, or contact clients. Any outbound stays `status: draft`; escalate to the contact in `_system/config.md`.
- Honesty over comfort: "What's Behind" and "What Dragged" lead and name patterns, not excuses. Do not soften or bury the lede.
- Size budget: keep the review within the context budget (<=150 lines); link to evidence files rather than inlining their content.

## References
- `Memory/kpi-ledger.md` (read-only source for metric movement)
- `Daily/YYYY-W(ww-1)-review.md` (prior week's review, for carry-over)
- `/business-review` (suggested monthly follow-up)
