---
name: pipeline-update
description: Refreshes the sales pipeline from CRM exports call notes or user input by moving deal stages updating values and next steps adding prospects recomputing pipeline value and surfacing stalled deals when you say update the pipeline log a won deal or refresh deals
---

# Pipeline Update

Refresh the sales pipeline from new inputs, recompute totals, log outcomes and ledger rows, and surface stalled deals with next actions.

## When to use
- After a CRM export, sales call, or pipeline review when deal data has changed.
- When a deal moves stages, changes value, or needs a new owner or next step.
- When a new prospect must be captured into the pipeline.
- When a deal is won or lost and the outcome must be recorded.
- When the user asks to "update the pipeline", "refresh deals", "log a closed deal", or "what's stalled".

## Inputs
- `Pipeline/deals.md` — the canonical deal register (read first).
- `Pipeline/accounts/` — account context files.
- `Pipeline/prospects/` — existing prospect files (`{slug}.md`).
- New info from one of: a CRM export (CSV/paste), call notes, or direct user input.
- `Memory/kpi-ledger.md` — for prior pipeline-value rows and trend context.
- `_system/config.md` — escalation contact for any outreach drafts.
- `_system/rules.md` — routing and frontmatter conventions.

## Process
1. **Load state.** Read `Pipeline/deals.md`, scan `Pipeline/accounts/` and `Pipeline/prospects/` for the deals and accounts referenced. Note current stage, value, owner, next-step, and last-touch date for each open deal.
2. **Ingest new info.** Accept the CRM export, call notes, or user input. Normalize each item to a deal: account, contact, stage, value, owner, next-step, expected-close, last-touch. If the source is ambiguous or unmappable, route the raw item to `Inbox/` rather than guessing.
3. **Reconcile deals.** For each existing deal, apply changes: move `stage`, update `value`, `owner`, `next-step`, and `last-touch`. Preserve deal history in-line (do not delete prior context). Use kebab-case slugs and ISO dates.
4. **Add new prospects.** For each new prospect not already tracked, create `Pipeline/prospects/{slug}.md` with universal frontmatter and fields: account, contact, source, stage, value, owner, next-step, last-touch. Link to or create the matching `Pipeline/accounts/{slug}.md` if an account file is warranted.
5. **Handle won/lost outcomes.** For each deal marked won or lost, write a decision note at `Memory/decisions/YYYY-MM-DD-{slug}.md` (frontmatter + outcome, value, reason, what-worked / what-failed, lessons). Mark the deal's `status` accordingly in `Pipeline/deals.md`.
6. **Recompute pipeline value.** Sum open-deal values into a total pipeline value; tally `deals-won` and `deals-lost` for the period. Tag each figure with its `source` (e.g. crm-export, call-notes, user-input) and a confidence level.
7. **Append ledger rows.** Append (never edit) rows to `Memory/kpi-ledger.md` for `pipeline-value`, and for `deals-won` / `deals-lost` when outcomes occurred, using the exact column order and a `confidence` from {confirmed, reported, inferred, stale}.
8. **Draft outreach only.** If any next-step implies contacting a prospect, write the message with `status: draft`, save it under the relevant prospect/account, and escalate to the contact in `_system/config.md`. NEVER send, email, or contact a prospect autonomously.
9. **Surface stalled + next actions.** Flag deals with no movement past the stall threshold (default: no `last-touch` update in 14 days, or stuck in-stage beyond its norm). List each stalled deal with its owner and a recommended next action, and present the period summary (new prospects, stage moves, won/lost, new pipeline value).

## Outputs
- Updated `Pipeline/deals.md` (stages, values, owners, next-steps, statuses).
- New prospect files at `Pipeline/prospects/{slug}.md` (one per new prospect).
- Updated/created account files at `Pipeline/accounts/{slug}.md` as needed.
- Decision notes at `Memory/decisions/YYYY-MM-DD-{slug}.md` (one per won/lost deal).
- Appended rows in `Memory/kpi-ledger.md`:
  - `| YYYY-MM-DD | pipeline-value | <baseline> | <current> | <target> | <source> | <confidence> | <note> |`
  - `| YYYY-MM-DD | deals-won | <baseline> | <current> | <target> | <source> | <confidence> | <note> |` (when applicable)
  - `| YYYY-MM-DD | deals-lost | <baseline> | <current> | <target> | <source> | <confidence> | <note> |` (when applicable)
- Any outreach saved as `status: draft` (never sent), with an escalation flag to the `_system/config.md` contact.
- A returned summary: stage moves, new prospects, won/lost outcomes, recomputed pipeline value, and the stalled-deal list with next actions.

## Guardrails
- Human-approval gate: NEVER autonomously send, publish, email, or contact a prospect. All outreach is `status: draft` and escalated to the `_system/config.md` contact.
- `Memory/kpi-ledger.md` is APPEND-ONLY — never edit or reorder prior rows; only append new ones with the exact column set.
- Generated rollups carry `generated: true` and are never hand-edited.
- Every `.md` written carries universal frontmatter (type, status, owner, date, reviewed, tags >=2, confidential, source, generated).
- Agency firewall: only read the active client's pipeline; never read sibling `Clients/{slug}/` data. If an input is ambiguous or unroutable, send it to `Inbox/` instead of guessing.
- Route facts to canonical homes; use kebab-case slugs and ISO dates throughout.
- Never change pricing, alter `_system/permissions.md`, or delete deal history as part of an update.

## References
- `_system/config.md` (escalation contact)
- `_system/rules.md` (routing + frontmatter)
- `Memory/kpi-ledger.md` (append-only ledger spec)
- `Pipeline/deals.md`, `Pipeline/accounts/`, `Pipeline/prospects/`
- `Memory/decisions/` (won/lost notes)
