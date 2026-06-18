---
type: context
status: active
owner: system
reviewed: {{YYYY-MM-DD}}
tags: [router, brain]
confidential: false
source: Conversion OS Setup
generated: false
---

# Conversion OS — Root Router
Product: Conversion OS by Conversion System. Profile: {{solo|team|agency}}.
Read this file fully at the start of every session. Keep it <=150 lines.

## 1. Startup read-routine
1. Read this file, `_system/config.md`, `_system/rules.md` (team/agency also `_system/permissions.md`).
2. (Agency) If the task is about ONE client, read `Clients/{slug}/CLAUDE.md` FIRST and load only that client.
3. Read today's `Daily/YYYY-MM-DD.md`; load `Memory/kpi-ledger.md` latest state before any metric work.

## 2. Routing map (canonical home per info type)
<!-- one row per info type -> its single canonical home. Profile-specific rows:
     Solo/Team: Pipeline/ for sales. Agency: Clients/{slug}/ (firewalled) for client work. -->
| Info type | Canonical home |
|-----------|----------------|
| Company identity/brand/offer | `Company/` |
| Metric that moved | `Memory/kpi-ledger.md` (append) |
| Decision + rationale | `Memory/decisions/` |
| Daily log / weekly review | `Daily/` |
| Reusable asset | `Library/` |
| Unsorted capture | `Inbox/` (triage daily) |

## 3. Memory & writing rules
- Before a metric, read its latest `kpi-ledger.md` row (higher `confidence` + named `source` wins).
- Universal frontmatter on every file. One concept per file. kebab-case, ISO dates.
- Ledgers are append-only; never edit/reorder prior rows. Generated rollups never hand-edited.

## 4. Source-of-truth & conflict rules
- `Company/` = identity truth. `Memory/kpi-ledger.md` = metric truth. `_system/` = config/permission truth.
- On conflict: newer `reviewed:`/`date:` + higher `confidence` wins; log to `Memory/lessons.md`.

## 5. Size budgets
- Root CLAUDE.md <=150 lines; folder CLAUDE.md <=60; context docs <=150. Load only what the task needs.

## 6. Security / confidentiality
- `confidential: true` => never read across contexts. (Agency) never read a sibling `Clients/{slug}/`.
- Keep credentials out of `Company/stack.md`. Log external reads/writes to `_system/audit/`.

## 7. Human-approval rules
- Ask before: sending external messages, deleting files, publishing, changing pricing/offers,
  editing permissions, contacting clients. Outbound is `status: draft` + escalated to `_system/config.md` contact.

## 8. Voice & anti-patterns
- Use `Library/styles/brand-voice.md`. No placeholders. No hand-editing generated rollups.
