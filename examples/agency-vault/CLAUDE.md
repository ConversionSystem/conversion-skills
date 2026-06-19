---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [router, brain]
confidential: false
source: Conversion Skills Setup
generated: false
---

# Conversion Skills · Root Router
Product: Conversion Skills by Conversion System. Profile: agency.
Read this file fully at the start of every session.

## 1. Startup read-routine
1. Read this file.
2. Read `_system/config.md`, `_system/rules.md`, `_system/permissions.md`.
3. If the task is about ONE client, read `Clients/{slug}/CLAUDE.md` FIRST and
   load only that client's folder. Never open a sibling client.
4. Read today's `Daily/YYYY-MM-DD.md`; load `Memory/kpi-ledger.md` latest state.

## 2. Routing map (canonical home per info type)
| Info type                    | Canonical home                          |
|------------------------------|-----------------------------------------|
| Our firm's identity          | `Company/`                              |
| A firm metric that moved     | `Memory/kpi-ledger.md` (append)         |
| A firm decision              | `Memory/decisions/`                     |
| CLIENT work / context        | `Clients/{slug}/` (firewalled)          |
| A client metric              | `Clients/{slug}/goals.md` (append)      |
| Person / role / permission   | `Team/{person}/`, `_system/permissions` |
| Daily log / weekly review    | `Daily/`                                |
| Reusable, non-client asset   | `Library/`                              |
| Unsorted capture             | `Inbox/` (triage daily)                 |

## 3. Memory-retrieval rules
- Firm metrics: latest row in `Memory/kpi-ledger.md`. Client metrics: that
  client's `goals.md`. Prefer higher `confidence` + named `source`.

## 4. Writing rules
- Universal frontmatter on every file. One concept per file. kebab-case, ISO dates.
- Ledgers are append-only; never edit or reorder prior rows.
- Client files are `confidential: true` and live ONLY under their workspace.

## 5. Source-of-truth rules
- `Company/` = firm identity. Each `Clients/{slug}/profile.md` = that client.
- `_system/permissions.md` = who may access what.

## 6. Conflict-resolution rules
- Newer `reviewed:`/`date:` + higher `confidence` wins; log to `Memory/lessons.md`.

## 7. Token-efficiency / size budgets
- Root CLAUDE.md <=150; folder CLAUDE.md <=60; context docs <=150.
- Load only the one client/folder the task needs.

## 8. Security / confidentiality (FIREWALL)
- Read and write ONLY the active client's `Clients/{slug}/` folder.
- NEVER open a sibling `Clients/{slug}/`. Every client file is `confidential: true`.
- Ambiguous entity -> file to `Inbox/`, never guess the client.
- Keep credentials out of any `stack.md`. Log external I/O to `_system/audit/`.

## 9. Human-approval rules
- Ask before: sending client messages, deleting files, publishing, changing
  pricing/scope, editing permissions. Outbound is `status: draft` + escalated.

## 10. Voice & anti-patterns
- Use `Library/styles/brand-voice.md`. No cross-client references. No placeholders.
