---
type: kpi-ledger
status: active
owner: jordan
tags: [memory, ledger]
confidential: false
source: multiple
generated: false
---

# KPI Ledger · append-only

Rules: one row per metric moved. NEVER edit or reorder prior rows. Scan from the
bottom for the latest value. `confidence` ∈ {confirmed, reported, inferred, stale}.

| date | metric | baseline | current | target | source | confidence | note |
|------|--------|----------|---------|--------|--------|------------|------|
| 2026-05-01 | mrr | 12000 | 12000 | 20000 | stripe export | confirmed | Q3 baseline set |
| 2026-05-01 | newsletter-subs | 1800 | 1800 | 3000 | beehiiv | confirmed | baseline |
| 2026-05-01 | qualified-calls-per-wk | 0.5 | 0.5 | 2 | manual count | reported | baseline |
| 2026-06-01 | newsletter-subs | 1800 | 2140 | 3000 | beehiiv | confirmed | +340 in May |
| 2026-06-18 | mrr | 12000 | 14500 | 20000 | stripe export | confirmed | landed 1 retainer |
| 2026-06-18 | qualified-calls-per-wk | 0.5 | 1.2 | 2 | calendar | reported | newsletter CTA working |
