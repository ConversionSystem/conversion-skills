---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [router, brain]
confidential: false
source: Conversion OS Setup
generated: false
---

# Conversion OS — Root Router
Product: Conversion OS by Conversion System. Profile: solo.
This file is the brain. Read it fully at the start of every session.

## 1. Startup read-routine
1. Read this file.
2. Read `_system/config.md` (budgets, signature, escalation contact).
3. Read `_system/rules.md` (and, on team/agency, `_system/permissions.md`).
4. Read today's `Daily/YYYY-MM-DD.md` if it exists, else the most recent one.
5. Load the folder `CLAUDE.md` for whatever folder the task touches.
6. Load `Memory/kpi-ledger.md` latest state before any metric work.

## 2. Routing map (canonical home per info type)
| Info type                     | Canonical home                         |
|-------------------------------|----------------------------------------|
| Company identity/brand/offer  | `Company/`                             |
| Metric that moved             | `Memory/kpi-ledger.md` (append)        |
| A decision + rationale        | `Memory/decisions/`                    |
| Reusable lesson               | `Memory/lessons.md`                    |
| Sales account/prospect/deal   | `Pipeline/`                            |
| Internal initiative           | `Projects/{slug}/`                     |
| Published marketing           | `Content/{slug}-{date}/`               |
| Meeting note                  | `Operations/meetings/`                 |
| SOP / process                 | `Operations/sops/`, `processes/`       |
| Daily log / weekly review     | `Daily/`                               |
| Reusable prompt/template      | `Library/`                             |
| Unsorted capture              | `Inbox/` (triage daily)                |

## 3. Memory-retrieval rules
- Before stating a metric, read the LATEST row for it in `kpi-ledger.md`.
- Prefer rows with higher `confidence` and a named `source`.
- Before a decision, check `Memory/decisions/` for prior/contradicting ones.

## 4. Writing rules
- Every file starts with the universal frontmatter schema.
- One concept per file; kebab-case slugs; ISO dates.
- Append to `kpi-ledger.md`; NEVER edit or reorder prior rows.
- Never hand-edit files marked `generated: true`.

## 5. Update rules
- New fact -> route to its canonical home (section 2), don't duplicate.
- Changed company truth -> update `Company/*` and bump `reviewed:`.
- Every workflow that moves a metric MUST append a ledger row.

## 6. Naming rules
- kebab-case; `YYYY-MM-DD`; weeks `YYYY-Www`; decisions `YYYY-MM-DD-{slug}.md`.

## 7. Source-of-truth rules
- `Company/` = identity truth. `Memory/kpi-ledger.md` = metric truth.
- `_system/` = config/permission truth. Rollups are generated, not authored.

## 8. Conflict-resolution rules
- If two files disagree: newer `reviewed:`/`date:` wins; higher `confidence` wins.
- Log the contradiction to `Memory/lessons.md` and flag for Optimizer merge.

## 9. Token-efficiency / size budgets
- Root CLAUDE.md <=150 lines; folder CLAUDE.md <=60; context docs <=150.
- Load only the folder(s) the task needs. Summarize, don't paste, long files.

## 10. Security / confidentiality rules
- `confidential: true` => never read across contexts.
- Keep credentials out of `Company/stack.md`; they live in a secret manager.
- Log external reads/writes to `_system/audit/`.

## 11. Human-approval rules
- Ask a human before: sending external messages, deleting files, publishing
  content, changing pricing/offers, editing permissions, contacting clients.
- Operator escalates decisions to the contact in `_system/config.md`.

## 12. Voice rules
- Use `Library/styles/brand-voice.md`. Specific, plain, no hype. No emojis.

## 13. Anti-patterns (never do)
- Don't dump everything in one note. Don't overwrite the ledger.
- Don't invent metrics without a `source`. Don't hand-edit generated rollups.
- Don't exceed size budgets silently.
