---
name: portfolio-watch
description: Owner-only agency roll-up that aggregates every client's health, trend, risk, and renewal into one portfolio board · run when the owner says portfolio watch, how's the whole book doing, client health board, which accounts are at risk across all clients, renewal radar, or give me the agency overview.

---

# Portfolio Watch

Aggregate the whole client book into a single owner-only health board · per-client status, metric trend, risk flags, renewal radar, and growth opportunities · by reading each client's profile, goals, and recent reports under explicit owner permission. This is the one legitimate cross-client roll-up; the output is an aggregate for the owner alone and never leaks one client's specifics into another.

## When to use
- On a recurring cadence (weekly or monthly) when the agency owner wants a single view of the entire book: who's healthy, who's slipping, what renews soon.
- Before a leadership review, board update, or capacity-planning session that needs portfolio-level numbers (active clients, at-risk value, portfolio MRR).
- After a rough stretch across several accounts, when the owner asks "how's the whole book doing", "which clients are at risk", or wants a renewal radar across all clients.
- Any time the owner asks for a portfolio watch, a client health board, or an agency overview.

## Inputs
- `_system/permissions.md` · REQUIRED gate. Confirm the requester is `owner` with `clients: all` before reading across clients. If not owner, refuse and stop.
- `Clients/{slug}/profile.md` for every client · name, status, plan, value/MRR, renewal date, owner-side lead.
- `Clients/{slug}/goals.md` for every client · the per-client append-only ledger; read each tracked metric's latest `current`, `target`, `source`, `confidence`, and the prior row to compute trend.
- `Clients/{slug}/` recent reports, especially the latest `Operations/reviews/{date}-churn-watch.md` written within that client's scope (if present) · to inherit risk signals rather than re-derive them.
- `Operations/reviews/{prev-date}-portfolio.md`, if one exists · the prior board, so the new one can lead with what changed.
- `_system/config.md` · firm context and the escalation contact.
- `_system/rules.md` · routing, frontmatter, and Solo/Team vs Agency conventions.

## Process

### Phase 1 · PERMISSION GATE
1. Read `_system/permissions.md`. Confirm the requesting principal has `role: owner` and `clients: all`. If the requester is a member or contractor, REFUSE · write nothing, return a one-line denial, and log the attempt to `_system/audit/`. This skill exists only for the owner.
2. Confirm profile is `agency`. On Solo/Team there is no client book to roll up; tell the user to use `pipeline-review` or `churn-watch` instead and stop.

### Phase 2 · LOAD (cross-client, aggregate-only)
3. Enumerate every `Clients/{slug}/` workspace. For each, read only `profile.md`, `goals.md`, and the most recent report(s) needed for status · nothing more than the roll-up requires.
4. From each `goals.md`, take the latest row per tracked metric plus its immediate prior row; derive a **trend** (`up`, `flat`, `down`, or `stale`) with the metric's `source` and `confidence`. Never edit any `goals.md`.
5. If a client has a recent `churn-watch` report, inherit its risk level and signals. Otherwise, infer a provisional risk read from goals (behind/regressed/stale metrics, missed targets) and mark those signals `inferred`.
6. If a prior `Operations/reviews/{prev-date}-portfolio.md` exists, load it to lead the new board with movement (improved, worsened, new client, churned).

### Phase 3 · AGGREGATE
7. Build the **per-client row**: client | status | headline metric + trend | risk flag (`high`/`medium`/`low`) | renewal date | one-line note. Keep each row to that client's own data only.
8. Build the **renewal radar**: every client with a renewal inside the window (default 90 days), sorted by date, flagged where metrics are weak going into it.
9. Build the **risk roster**: clients flagged `medium`/`high`, each tied to its source signal (inherited churn-watch path + date, or the specific behind/stale metric).
10. Build the **opportunities** list: clients beating targets, ripe for upsell/expansion/case-study, each pointing at the supporting metric.
11. Compute firm roll-ups, each tagged with `source` and `confidence`: `active-clients` (count of `status: active`), `at-risk-value` (sum of value/MRR for medium+high-risk clients), `portfolio-mrr` (sum of recurring value across active clients). Never invent a number; if a client's value is missing, exclude it and note the gap.

### Phase 4 · WRITE (owner-only)
12. Write the board to `Operations/reviews/{date}-portfolio.md` with `generated: true`, `confidential: true`, owner-only. Universal frontmatter. Sections in order: CHANGE-SINCE-LAST (re-run only), PORTFOLIO ROLL-UP (the three firm numbers), PER-CLIENT BOARD (one table), RENEWAL RADAR, RISK ROSTER, OPPORTUNITIES.
13. Append firm-level rows to `Memory/kpi-ledger.md` for `active-clients`, `at-risk-value`, and `portfolio-mrr`, in the exact column order with a `confidence` from {confirmed, reported, inferred, stale}. Append only · never edit or reorder prior rows. (These are firm metrics, so they live in `Memory/kpi-ledger.md`, NOT in any client's `goals.md`.)
14. Append a one-line entry to today's `Daily/YYYY-MM-DD.md`: portfolio watch ran, active-clients / at-risk-value / portfolio-mrr, and the high-risk client count.
15. Return the board headline to the owner: the three firm numbers, the high-risk clients, and the next renewals.

## Outputs
- `Operations/reviews/{date}-portfolio.md` · the generated, owner-only board (`generated: true`, `confidential: true`); sections in order: CHANGE-SINCE-LAST (re-run only), PORTFOLIO ROLL-UP, PER-CLIENT BOARD, RENEWAL RADAR, RISK ROSTER, OPPORTUNITIES.
- Appended rows in `Memory/kpi-ledger.md` (firm ledger):
  - `| YYYY-MM-DD | active-clients | <baseline> | <current> | <target> | <source> | <confidence> | <note> |`
  - `| YYYY-MM-DD | at-risk-value | <baseline> | <current> | <target> | <source> | <confidence> | <note> |`
  - `| YYYY-MM-DD | portfolio-mrr | <baseline> | <current> | <target> | <source> | <confidence> | <note> |`
- One appended line in `Daily/YYYY-MM-DD.md` · watch ran, the three firm numbers, high-risk client count.
- A returned summary: the three firm numbers, high-risk clients, and upcoming renewals.

## Guardrails
- OWNER-ONLY: this is the single legitimate cross-client exception. Read `_system/permissions.md` FIRST; proceed only if the requester is `owner` with `clients: all`. Any non-owner request is refused and logged to `_system/audit/`.
- AGGREGATE-ONLY, NEVER LEAK: the board is a roll-up for the owner. NEVER write one client's specifics into another client's folder, and NEVER expose one client's data to a non-owner. The report lives in `Operations/reviews/` (firm space), is `confidential: true`, and is never placed inside any `Clients/{slug}/`.
- DRAFT-ONLY: this skill observes and reports. NEVER contact a client, send, post, change a renewal, or take any account action autonomously · a human runs every play.
- Reads only, with three write exceptions: its own report file, the three appended firm ledger rows, and the one-line Daily entry. Touch nothing under any `Clients/{slug}/`.
- `Memory/kpi-ledger.md` is APPEND-ONLY · never edit, reorder, or hand-edit a prior row; only append the three new firm rows with the exact column set. Firm metrics go here, never into a client's `goals.md`.
- PROVENANCE: every status, trend, risk flag, and firm number traces to a real file (path + date) or ledger row. Never invent a metric or a risk reason; if evidence is thin, mark it `inferred` and surface the gap. Exclude clients with missing values from the sums and note it.
- Every `.md` written carries universal frontmatter (type, status, owner, date, reviewed, tags >=2, confidential, source, generated); the report is `generated: true` and `confidential: true`, regenerated on re-run, never patched by hand.
- Route outputs to canonical homes; kebab-case slugs and ISO dates throughout.

## References
- `_system/permissions.md` (owner gate · required; role/clients check)
- `_system/config.md` (firm context, escalation contact)
- `_system/rules.md` (routing + frontmatter, Solo/Team vs Agency)
- `Clients/{slug}/profile.md` and `Clients/{slug}/goals.md` (per-client status, value, renewal, metric trend)
- `Clients/{slug}/Operations/reviews/{date}-churn-watch.md` (inherited per-client risk signals, where present)
- `Memory/kpi-ledger.md` (firm append-only ledger; confidence in confirmed/reported/inferred/stale)
- `Operations/reviews/{prev-date}-portfolio.md` (prior board, for change-since-last)
