---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [router, pipeline]
confidential: false
source: Conversion OS Setup
generated: false
---

# Pipeline/ — local rules
Purpose: sales/CRM context. Accounts, prospects, and the live deal board.

## Read
- `deals.md` for stages/owners/next-steps. `accounts/`, `prospects/` for context.

## Write
- New prospect -> `prospects/{slug}.md`. New account -> `accounts/{slug}.md`.
- Stage change or value change -> update `deals.md` AND append a ledger row
  (e.g. `pipeline-value`, `deals-won`) with a `source`.

## Never
- Never email a prospect autonomously; draft and escalate for a human to send.
- Never invent deal values; cite the source (CRM export, call note).

## Hand-off
- Won/lost outcomes -> a `Memory/decisions/` note + a `kpi-ledger.md` row.
