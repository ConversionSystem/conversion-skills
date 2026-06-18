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

# Conversion OS · Root Router
Product: Conversion OS by Conversion System. Profile: team.
Read this file fully at the start of every session.

## 1. Startup read-routine
1. Read this file, `_system/config.md`, `_system/rules.md`, `_system/permissions.md`.
2. Read the acting person's `Team/{slug}/access.md` to scope what to load.
3. Read today's `Daily/YYYY-MM-DD.md`; load `Memory/kpi-ledger.md` latest state.

## 2. Routing map (canonical home per info type)
| Info type                   | Canonical home                          |
|-----------------------------|-----------------------------------------|
| Company identity/brand/offer| `Company/`                              |
| Department charter/SOPs     | `Company/departments/{name}/`           |
| Metric that moved           | `Memory/kpi-ledger.md` (append)         |
| A decision + rationale      | `Memory/decisions/`                     |
| Sales account/prospect/deal | `Pipeline/`                             |
| Internal initiative         | `Projects/{slug}/`                      |
| Meeting / SOP               | `Operations/meetings/`, `sops/`         |
| Person / role / permission  | `Team/{person}/`, `_system/permissions` |
| Daily log / weekly review   | `Daily/`                                |
| Reusable asset              | `Library/`                              |
| Unsorted capture            | `Inbox/` (triage daily)                 |

## 3. Memory & writing rules
- Before a metric, read its latest `kpi-ledger.md` row (higher confidence wins).
- Universal frontmatter on every file. One concept per file. kebab-case, ISO dates.
- Ledgers append-only; never edit prior rows. Generated rollups never hand-edited.

## 4. Source-of-truth & conflict rules
- `Company/` = identity. `Memory/kpi-ledger.md` = metric truth.
- `_system/permissions.md` = access. Newer + higher-confidence wins on conflict.

## 5. Size budgets
- Root CLAUDE.md <=150; folder CLAUDE.md <=60; context docs <=150.

## 6. Security / permissions
- Load only what the acting person's `access.md` grants. Log external I/O to `_system/audit/`.
- AI-scoping is paired with storage-layer ACLs; it is not encryption.

## 7. Human-approval rules
- Ask before sending external messages, deleting files, publishing, changing
  pricing/offers, or editing permissions. Outbound is `status: draft` + escalated.

## 8. Voice & anti-patterns
- Use `Library/styles/brand-voice.md`. No placeholders. Don't exceed budgets silently.
