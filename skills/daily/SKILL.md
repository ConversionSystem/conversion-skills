---
name: daily
description: Runs your operating rhythm for resume morning triage evening and save flows reading and writing Daily notes when you say start my day standup what next plan today empty the inbox wrap up or save this session
---

# Daily

The operating rhythm of Conversion Skills. One intent-routed entry point for resuming context, composing the day, clearing the inbox, closing the day, and logging a session · all reading and writing `Daily/`.

## When to use

- You sit down and want a standup of where things stand ("resume", "what next", "where was I").
- You want to compose today's plan ("plan my day", "start my day", "morning").
- The `Inbox/` has piled up and needs routing ("empty the inbox", "triage").
- You want to close the day against the morning plan ("wrap up", "evening review", "end of day").
- You want to log what just happened in this working session ("save this session", "log this").
- Default when intent is unclear: run MORNING.

## Inputs

- Intent phrase from the user (RESUME / MORNING / TRIAGE / EVENING / SAVE). Default = MORNING.
- Root router: `CLAUDE.md`.
- Company context: `Company/profile.md`, `Company/strategy.md`.
- Recent days: 2-3 most recent `Daily/YYYY-MM-DD.md`.
- Open loops: `Operations/tasks.md`, `Pipeline/deals.md`, `Pipeline/accounts/`, `Clients/{slug}/` (per access; respect agency firewall).
- Latest KPI: most recent rows of `Memory/kpi-ledger.md`.
- Lessons log: `Memory/lessons.md`.
- Today's note (existing or to-be-created): `Daily/YYYY-MM-DD.md`.

## Process

1. **Route the intent.** Read the user's phrase and select one flow: RESUME, MORNING, TRIAGE, EVENING, or SAVE. If none is clear, run MORNING. State which flow is running in one line.

2. **RESUME · standup, max 10 lines.**
   1. Read `CLAUDE.md`, `Company/profile.md`, and the 2-3 most recent `Daily/YYYY-MM-DD.md`.
   2. Pull open loops from `Operations/tasks.md`, `Pipeline/deals.md`, and accessible accounts/clients (skip any sibling `Clients/{slug}/` outside access).
   3. Collect deadlines surfacing in the next 1-2 days.
   4. Output: one-line context, top open loops, nearest deadlines, and one suggested first move. No file write. Read-only.

3. **MORNING · compose today's note.**
   1. Read yesterday's `Daily/YYYY-MM-DD.md`, `Operations/tasks.md`, `Company/strategy.md` priorities, and the latest `Memory/kpi-ledger.md` row.
   2. Argue a **Top 3** for today (each with a one-line why it beats the alternatives), shape the calendar into named work blocks, list carried-forward open loops, and name one watch item.
   3. Write `Daily/YYYY-MM-DD.md` with universal frontmatter (`type: daily`, `status: active`, `owner`, `date`, `reviewed`, `tags` (>=2), `confidential`, `source`, `generated: false`).

4. **TRIAGE · empty the inbox.**
   1. Read each item in `Inbox/`.
   2. Route each to its canonical home per the root router map (facts to Company/Memory, deal items to Pipeline, client items to the correct `Clients/{slug}/`, project/content artifacts to their folders). Ambiguous items go to `Inbox/` notes for human decision, never guessed into a client folder.
   3. After a successful filing, delete the original inbox item. Items that are not filings (actions) become entries on `Operations/tasks.md`.
   4. Report a move-ledger: one line per item · `from -> to` (or `-> task`), with reason.

5. **EVENING · close the day.**
   1. Read today's `Daily/YYYY-MM-DD.md` Top 3 and compare against actual: mark each **done / moved / dropped**.
   2. Tick completed items in `Operations/tasks.md`; carry unfinished open loops forward (note them for tomorrow).
   3. Capture exactly one lesson to `Memory/lessons.md` (append).
   4. Append the day's outcome summary to today's note.

6. **SAVE · log this session.**
   1. Append a session-log block to today's `Daily/YYYY-MM-DD.md`: topics discussed, decisions made, files changed, and open loops opened/closed.
   2. Route durable facts to their canonical homes (e.g., a confirmed metric to the ledger, a strategy shift to `Company/strategy.md`, a lesson to `Memory/lessons.md`).
   3. Emit one line per write so the user can audit what moved where.

7. **Ledger on metrics.** In any flow, whenever a concrete metric surfaces (a number with a source), append a row to `Memory/kpi-ledger.md` using the exact columns. Append-only; never edit or reorder prior rows.

8. **Respect gates.** Never autonomously send, publish, delete client data, contact clients, change pricing, or edit permissions. Deletion is limited to filed `Inbox/` originals after a successful route. Drafted outbound stays `status: draft`.

## Outputs

- **MORNING:** `Daily/YYYY-MM-DD.md` created/updated with Top 3, work blocks, open loops, and watch item (`generated: false`).
- **EVENING:** outcome summary appended to `Daily/YYYY-MM-DD.md`; ticked items in `Operations/tasks.md`; one appended lesson in `Memory/lessons.md`; carried-forward loops noted.
- **TRIAGE:** routed files written to their canonical homes; non-filings added to `Operations/tasks.md`; filed originals removed from `Inbox/`; move-ledger reported in chat.
- **SAVE:** session-log block appended to `Daily/YYYY-MM-DD.md`; durable facts routed to homes; one line per write reported.
- **RESUME:** standup printed to chat only · no file writes.
- **Any flow:** appended row(s) in `Memory/kpi-ledger.md` when a metric surfaces · columns `| date | metric | baseline | current | target | source | confidence | note |`, confidence in {confirmed, reported, inferred, stale}.

## Guardrails

- Default flow is MORNING when intent is ambiguous.
- RESUME is strictly read-only.
- KPI ledger is append-only: never edit, reorder, or overwrite existing rows; new rows use the exact columns and a confidence value in {confirmed, reported, inferred, stale}.
- Generated rollups carry `generated: true` and are never hand-edited; daily notes authored here are `generated: false`.
- Agency firewall: never read a sibling `Clients/{slug}/` outside granted access; ambiguous inbox items route to `Inbox/` for human decision, never guessed into a client folder.
- Human-approval gates: never autonomously send, publish, delete (beyond filed inbox originals), contact clients, change pricing, or edit permissions; outbound stays `status: draft` and escalates to the contact in `_system/config.md`.
- Every `.md` written carries universal frontmatter (type, status, owner, date, reviewed, tags >=2, confidential, source, generated).
- Keep within size budgets: daily note context stays lean; root `CLAUDE.md` <=150 lines, folder routers <=60, context files <=150.
- Use kebab-case slugs and ISO dates throughout.

## References

- Root router: `CLAUDE.md`
- `_system/config.md` (escalation contact), `_system/rules.md`
- `Operations/tasks.md`, `Memory/kpi-ledger.md`, `Memory/lessons.md`, `Company/strategy.md`, `Company/profile.md`
- `Inbox/`
