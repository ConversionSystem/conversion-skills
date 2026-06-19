---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [router, memory]
confidential: false
source: Conversion Skills Setup
generated: false
---

# Memory/ · local rules
Purpose: the compounding layer. KPI ledger + decisions + lessons + glossary.

## Read
- `kpi-ledger.md`: scan from the BOTTOM for the latest row per metric.
- `decisions/`: check for prior/contradicting decisions before advising.

## Write
- `kpi-ledger.md` is APPEND-ONLY. One row per metric moved:
  `| date | metric | baseline | current | target | source | confidence | note |`
- New decision -> `decisions/YYYY-MM-DD-{slug}.md` with rationale + confidence.
- Durable insight -> append to `lessons.md`. New term -> `glossary.md`.

## Never
- Never edit, reorder, or delete prior ledger rows.
- Never record a metric without a `source`.
- Never exceed 60 lines in this file (Optimizer enforces).

## Hand-off
- Metric truth lives HERE; identity truth lives in `Company/`.
- On conflict: higher `confidence` + newer `date` wins; log to `lessons.md`.
