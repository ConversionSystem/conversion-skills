---
name: meeting-capture
description: Process a meeting transcript or notes into the vault — files the meeting record, routes decisions, actions, metrics, people and signals to their canonical homes, and logs to Daily — triggered by "capture meeting", "process this transcript", "log meeting notes", or "file these meeting notes"
---

# Meeting Capture

Turn a raw meeting (pasted transcript, typed notes, or uploaded file) into a filed meeting record plus routed decisions, actions, metrics, and signals. Manual counterpart to the Operator, with the same routing discipline.

## When to use
- You have a transcript, recap, or rough notes from a call, standup, sales conversation, or internal meeting and want it captured and routed.
- You want decisions, action items, and mentioned metrics pulled out and filed where they belong, not left buried in notes.
- You are not running the automated Operator and need to do the same routing by hand.

## Inputs
- The meeting content: pasted transcript, typed notes, or an uploaded file (paste the contents into the conversation).
- Meeting topic (short phrase, used in the slug).
- Meeting date (defaults to today, ISO `YYYY-MM-DD`).
- Context: is this an internal meeting or a client meeting, and on which mode (Solo, Team, or Agency)?
- For client meetings on Agency mode: the client `{slug}`.

## Process
1. Confirm scope. Establish date, topic (kebab-case it for the slug), internal-vs-client, mode, and client `{slug}` if client-facing. If the meeting clearly belongs to a client but the `{slug}` is ambiguous, write the record to `Inbox/` and stop for clarification rather than guessing.
2. Choose the destination folder:
   - Internal meeting: `Operations/meetings/YYYY-MM-DD-{topic}.md`.
   - Client meeting on Agency mode: `Clients/{slug}/meetings/YYYY-MM-DD-{topic}.md`. Stay firewalled — only read and write within this one client folder; never read sibling `Clients/` folders.
3. Read the meeting template from `Library/templates/` (meeting template) if present; otherwise use the standard meeting sections (Summary, Attendees, Discussion, Decisions, Actions, Metrics, Next steps). Write the meeting record with universal frontmatter: `type: meeting`, `status`, `owner`, `date` (the meeting date), `reviewed`, `tags` (>=2), `confidential` (true for client meetings), `source` (e.g. "transcript" or "notes"), `generated: false`.
4. Extract decisions. For each decision made, write a dated entry to `Memory/decisions/YYYY-MM-DD-{decision-slug}.md` with frontmatter and a stated confidence in {confirmed, reported, inferred, stale}. Note what was decided, who owns it, and the rationale. Link back to the meeting record.
5. Extract actions to `Operations/tasks.md` (or `Clients/{slug}/tasks.md` equivalent home on Agency):
   - OUR actions: one task line each with owner and due date (ISO).
   - THEIR actions (client/partner commitments): one line each flagged `waiting-on` with the responsible party.
6. Extract metrics. For every metric or number mentioned, append one row per metric to `Memory/kpi-ledger.md` using the exact columns `| date | metric | baseline | current | target | source | confidence |  note |`. APPEND-ONLY — never edit or reorder prior rows. Set `source` to this meeting record and `confidence` to {confirmed, reported, inferred, stale} based on how the number was stated.
7. Route people and signals. New people, account intel, competitor mentions, or strategy signals go to their canonical homes — `Pipeline/accounts/`, `Pipeline/prospects/`, `Company/competitors/`, `Company/market.md`, `Memory/lessons.md`, or the relevant `Clients/{slug}/` file on Agency. If a fact has no clear home, drop a note in `Inbox/`.
8. Log to Daily. Append a one-line entry to `Daily/YYYY-MM-DD.md` (today's note) summarizing the meeting and linking the meeting record.
9. Respect approval gates. Any outbound follow-up drafted from the meeting (emails, client messages) is written as `status: draft` only — never sent, published, or shared. Escalate sends to the contact in `_system/config.md`.

## Outputs
- Meeting record: `Operations/meetings/YYYY-MM-DD-{topic}.md` (internal) or `Clients/{slug}/meetings/YYYY-MM-DD-{topic}.md` (Agency, confidential).
- Decision files: `Memory/decisions/YYYY-MM-DD-{decision-slug}.md`, one per decision, with confidence.
- Action lines appended to `Operations/tasks.md`: OUR actions with owner + due, THEIR actions flagged `waiting-on`.
- Ledger rows appended to `Memory/kpi-ledger.md`, one per mentioned metric, with `source` set to the meeting record.
- Routed facts/signals written to their canonical context files (e.g. `Pipeline/accounts/`, `Company/competitors/`, `Memory/lessons.md`) or `Inbox/` when ambiguous.
- One-line entry appended to `Daily/YYYY-MM-DD.md` linking the meeting record.

## Guardrails
- Human-approval gates: never autonomously send, publish, delete, contact clients, change pricing, or edit permissions. Any drafted outbound is `status: draft`; escalate to the contact in `_system/config.md`.
- Agency firewall: when handling a client meeting, read and write only within that one `Clients/{slug}/` folder. Never read sibling client folders.
- Route every fact to its canonical home; when the home is ambiguous, write to `Inbox/` rather than guessing.
- KPI ledger is APPEND-ONLY with fixed columns — never edit or reorder prior rows; mark confidence honestly ({confirmed, reported, inferred, stale}).
- Universal frontmatter on every file written, with >=2 tags and `confidential: true` for client material. Keep within size budgets (context files <=150 lines).
- Use kebab-case slugs and ISO dates throughout.

## References
- `Library/templates/` (meeting template)
- `Memory/kpi-ledger.md` (append-only ledger and column spec)
- `_system/config.md` (escalation contact for approval gates)
- `_system/rules.md`, `_system/permissions.md` (routing and access rules)
