---
name: operator
description: Daily autonomous operator that reads the OS, pulls enabled connectors within budget, synthesizes the day into the Daily note, routes durable facts to canonical homes, and escalates human decisions — triggers include run the operator, daily run, sync my day, catch me up, and schedule the operator.
---

# Conversion Operator

The daily autonomous operator that keeps the OS current: read, pull, synthesize, route, escalate, draft.

## When to use
- A scheduled or manual cadence run ("run the operator", "daily run", "sync my day", "catch me up", "process today").
- After meetings or a workday to fold transcripts, Slack, email, calendar, CRM, and PM activity into the OS.
- One-time setup to generate the operator's own run-prompt and (optionally) wire a cron schedule ("schedule the operator", "set up the daily run").

## Inputs
- Today's date (ISO `YYYY-MM-DD`) and cadence label (e.g. daily, twice-daily).
- Root router `CLAUDE.md` and `_system/config.md` (budgets, signature, escalation contact, active profile).
- `_system/rules.md`, `_system/connectors.md` (which connectors are ENABLED), `references/connectors.md`.
- Latest `Daily/` note and current state of `Memory/kpi-ledger.md`.
- Optional setup flag: generate-run-prompt and/or schedule-cron.

## Process
Phase 0 — Setup sub-flow (only when invoked for setup):
1. Read `_system/config.md` for cadence, signature, and escalation contact. Compose the operator run-prompt (a self-contained instruction to "run the operator for {date} at {cadence}") and write it to `Library/prompts/operator-run.md` (status:draft, generated:true).
2. If a scheduler is available, schedule the run-prompt on the configured cron cadence and record the schedule in `_system/state/operator-schedule.md`. If no scheduler exists, OUTPUT the cron expression + run-prompt verbatim for the user to wire manually and note this in the Daily synthesis. Do not assume a scheduler.

Phase 1 — Startup read-routine:
3. Read root `CLAUDE.md` to load the router map. Read `_system/config.md` for the per-category budgets (reads/writes/transcripts/emails/dms/housekeeping), the signature, and the single escalation contact. Read `_system/rules.md` for active guardrails and the current profile (Solo/Team/Agency).
4. Read the latest `Daily/YYYY-MM-DD.md` and the tail of `Memory/kpi-ledger.md` to establish yesterday's state and avoid duplicate work.

Phase 2 — Pull from ENABLED connectors only, within budget:
5. From `_system/connectors.md`, take only connectors marked enabled. Pull each category — meetings/transcripts, Slack, email, calendar, CRM, PM — strictly within its budget cap in `_system/config.md`.
6. When a category cap is hit, STOP that category cleanly and record `ran out of budget on {category}` in the synthesis. Never exceed a cap to "finish." Agency profile: never read across into a sibling `Clients/{slug}/`.

Phase 3 — Synthesize the day:
7. Append a synthesis section to today's `Daily/YYYY-MM-DD.md` (create it with universal frontmatter if absent): what happened, what changed, open loops, budget notes. Stamp the section with the signature from `_system/config.md`.

Phase 4 — Route durable facts to canonical homes (never dump in the Daily):
8. Decisions → `Memory/decisions/{slug}.md` (with `source` + `confidence`). Metric movements → APPEND rows to `Memory/kpi-ledger.md` using the exact columns and a `confidence` of {confirmed, reported, inferred, stale}. Meeting notes → `Operations/meetings/{slug}-{date}.md`. Tasks → `Operations/tasks.md` or the owning `Team/{person}/tasks.md`. Pipeline movement → `Pipeline/` (Solo/Team only). Ambiguous entities → `Inbox/`, never guess.

Phase 5 — Escalate the few human decisions:
9. Collect only items that need a human (approvals, blockers, pricing/offer/permission changes). Escalate them to the ONE escalation contact in `_system/config.md`. Dedupe against prior escalations so the same issue never re-pings; record escalated items in `_system/state/escalations.md`.

Phase 6 — Draft-only for outbound:
10. Anything outbound (emails, DMs, posts, replies) is written `status:draft` into the relevant file and surfaced to the escalation contact. Never send, publish, delete, change pricing/offers/permissions, or contact clients autonomously.

## Outputs
- `Daily/YYYY-MM-DD.md` — synthesis section appended, signed (created with universal frontmatter if new).
- `Memory/decisions/{slug}.md` — one decision per file, with `source` + `confidence`.
- `Memory/kpi-ledger.md` — APPEND-ONLY rows: `| date | metric | baseline | current | target | source | confidence | note |`.
- `Operations/meetings/{slug}-{date}.md` — routed meeting notes.
- `Operations/tasks.md` / `Team/{person}/tasks.md` — routed action items.
- `Inbox/` — ambiguous-entity captures.
- Outbound drafts written `status:draft` in their owning files.
- `_system/state/escalations.md` — deduped escalation log; `_system/state/operator-schedule.md` — schedule record (setup).
- `Library/prompts/operator-run.md` — the operator's run-prompt (setup, status:draft, generated:true).

## Guardrails
- Human-approval gates: never autonomously send messages/email/DM, publish, delete files, change pricing/offers, edit permissions, or contact clients — draft and escalate to the ONE contact in `_system/config.md`.
- Operator budgets in `_system/config.md` are hard caps per category; stop cleanly and note `ran out of budget on {category}`.
- KPI ledger is APPEND-ONLY: never edit, reorder, or delete prior rows; `source` + `confidence` required on every row and on every decision file.
- Firewall (Agency): never read a sibling `Clients/{slug}/`; every client file `confidential:true`; route ambiguous entities to `Inbox/`.
- Every written `.md` carries universal frontmatter (type, status, owner, date, reviewed, tags≥2, confidential, source, generated). Route facts to canonical homes; one concept per file; kebab-case slugs, ISO dates.
- Dedupe escalations against `_system/state/escalations.md` so the same issue never re-pings.

## References
- `references/connectors.md` — per-connector pull recipes, auth, and category budget mapping.
- `_system/connectors.md` — which connectors are ENABLED in this vault.
- `_system/config.md` — budgets, signature, escalation contact, cadence.
