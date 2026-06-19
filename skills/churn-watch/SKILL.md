---
name: churn-watch
description: Scans customers and accounts for churn-risk signals and produces a ranked save list with recommended plays · run when someone says churn watch, who's at risk, retention check, which accounts might cancel, renewal risk, or which clients are slipping.
---

# Churn Watch

Sweep the active book of accounts for early warning signs of churn · usage drops, silence, missed goals, open escalations, weak metrics into a renewal · and turn them into a ranked risk list with a recommended save play per account, escalating the worst before they slip.

## When to use
- On a recurring cadence (weekly or monthly) to catch at-risk accounts before they quietly cancel.
- Before a renewal cycle, QBR, or retention push, to know which relationships need a save play first.
- After a rough delivery period, a missed goal, or an unresolved escalation, when someone asks "who's at risk", "which clients are slipping", or wants a retention read.
- Any time someone asks for a churn watch, a save list, or "which accounts might cancel".

## Inputs
- Solo/Team: `Pipeline/accounts/` · every account file (status, value, renewal date, last-touch, owner).
- Agency: the ACTIVE client only · `Clients/{slug}/` (context, goals, meetings); never a sibling client.
- KPI source: `Memory/kpi-ledger.md` (Solo/Team) OR `Clients/{slug}/goals.md` (Agency) · for missed goals, stale metrics, and current-vs-target gaps.
- Recent `Operations/meetings/` notes (Solo/Team) or `Clients/{slug}/` meeting notes (Agency) · for last meaningful contact and open escalations.
- `Operations/reviews/{prev-date}-churn-watch.md`, if one exists · the prior risk list, to show what changed since last watch.
- `_system/config.md` · the escalation contact for high-risk accounts.
- `_system/rules.md` · routing, frontmatter, and Solo/Team vs Agency conventions.

## Process

### Phase 1 · LOAD
1. Determine profile and scope. Solo/Team: enumerate every file in `Pipeline/accounts/`. Agency: confirm the ACTIVE client slug, then operate only inside `Clients/{slug}/` · never read a sibling client.
2. Read the ledger source for the scope: `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency). Note each tracked metric's latest `current`, `target`, `source`, and `confidence`. Never edit it.
3. Read recent meeting notes for the scope (`Operations/meetings/` or `Clients/{slug}/`). Record each account's last meaningful contact date and any open or unresolved escalation.
4. If a prior `Operations/reviews/{prev-date}-churn-watch.md` exists, load it so the new report can lead with what changed (newly at-risk, recovered, worsened).

### Phase 2 · SCORE
5. For each account, evaluate the churn signals and cite the evidence (path + date) behind each:
   - **Engagement drop** · usage or activity declining versus its own baseline.
   - **Contact gap** · no meaningful touch past the silence threshold (default: no contact in 30 days).
   - **Missed goals** · a ledger/goals metric `behind` or `regressed` against target, or marked `stale`.
   - **Open escalation** · an unresolved complaint, bug, or dissatisfaction in the notes.
   - **Renewal risk** · renewal approaching (default: within 60 days) with weak or behind metrics.
6. Assign a **risk level** per account · `high`, `medium`, or `low` · driven by signal count and severity (an approaching renewal with weak metrics or an open escalation lifts an account toward `high`). Never invent a metric to justify a level; if evidence is thin, mark the signal `inferred` and say so.
7. For each at-risk account, write a **recommended save play**: the concrete next move (check-in, value recap, goal reset, escalation fix, renewal conversation) named to a specific Conversion Skills skill or owner action where it fits. Save plays are recommendations only · never executed here.
8. Compute the roll-up: `at-risk-count` (high + medium) and `at-risk-value` (sum of those accounts' values), each tagged with its `source` and a `confidence`.

### Phase 3 · WRITE + ESCALATE
9. Write the report to `Operations/reviews/{date}-churn-watch.md` with `generated: true` and universal frontmatter. Sections in order: CHANGE-SINCE-LAST (re-run only), RISK LIST (one table: `account | risk level | signals/evidence | recommended save play`), then HIGH-RISK CALLOUTS.
10. Append rows to the ledger source (`Memory/kpi-ledger.md` Solo/Team, or `Clients/{slug}/goals.md` Agency) for `at-risk-count` and `at-risk-value`, using the exact column order and a `confidence` from {confirmed, reported, inferred, stale}. Append only · never edit or reorder prior rows.
11. Escalate every `high`-risk account to the contact in `_system/config.md`: surface the account, its signals, and the recommended save play as a flagged callout. Do not contact the customer.
12. Append a one-line entry to today's `Daily/YYYY-MM-DD.md` noting the watch ran, the at-risk count/value, and the high-risk names.

## Outputs
- `Operations/reviews/{date}-churn-watch.md` · the generated risk list (`generated: true`); sections in order: CHANGE-SINCE-LAST (re-run only), RISK LIST, HIGH-RISK CALLOUTS.
- Appended rows in the ledger source (`Memory/kpi-ledger.md` Solo/Team OR `Clients/{slug}/goals.md` Agency):
  - `| YYYY-MM-DD | at-risk-count | <baseline> | <current> | <target> | <source> | <confidence> | <note> |`
  - `| YYYY-MM-DD | at-risk-value | <baseline> | <current> | <target> | <source> | <confidence> | <note> |`
- A high-risk escalation flagged to the `_system/config.md` contact (one callout per high-risk account; never customer-facing).
- One appended line in `Daily/YYYY-MM-DD.md` · watch ran, at-risk count/value, high-risk names.
- A returned summary: risk list headline, at-risk count and value, and the high-risk accounts with their save plays.

## Guardrails
- DRAFT-ONLY: save plays are recommendations. NEVER contact a customer, send, email, post, change a renewal, or take any account action autonomously · a human runs the play.
- Reads only, with three write exceptions: its own report file, the two appended ledger rows, and the one-line Daily entry. Touch nothing else.
- `Memory/kpi-ledger.md` / `Clients/{slug}/goals.md` is APPEND-ONLY · never edit, reorder, or hand-edit a prior row; only append the two new rows with the exact column set.
- PROVENANCE: every signal and risk level traces to a real file (path + date) or ledger row. Never invent a metric or a churn reason; if evidence is thin, mark it `inferred` and surface the gap.
- Agency FIREWALL: operate inside the ACTIVE client's `Clients/{slug}/` only; never read a sibling client; the report is `confidential: true`. Solo/Team writes to `Operations/reviews/`.
- Escalate high risk to the `_system/config.md` contact, not to the customer.
- Every `.md` written carries universal frontmatter (type, status, owner, date, reviewed, tags >=2, confidential, source, generated); the report is `generated: true` and regenerated on re-run, never patched by hand.
- Route outputs to canonical homes; kebab-case slugs and ISO dates throughout.

## References
- `_system/config.md` (escalation contact)
- `_system/rules.md` (routing + frontmatter, Solo/Team vs Agency)
- `Memory/kpi-ledger.md` / `Clients/{slug}/goals.md` (append-only ledger source, confidence in confirmed/reported/inferred/stale)
- `Pipeline/accounts/` (Solo/Team account files) or `Clients/{slug}/` (Agency, active client only)
- `Operations/meetings/` / `Clients/{slug}/` meeting notes (last contact, open escalations)
- `Operations/reviews/{prev-date}-churn-watch.md` (prior watch, for change-since-last)
