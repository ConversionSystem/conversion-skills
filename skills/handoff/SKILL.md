---
name: handoff
description: Save the thread so the next session or a teammate picks up cleanly, captures the next goal and points at canonical vault files by path, triggers hand off, handoff, continue in a fresh session, save context for the next session, brief the next operator
---

# Handoff

## When to use
At the end of a working session, or when you are about to hand the task to a fresh session or another operator and you do not want them to lose the thread. Use it when context is about to reset (a new window, a different machine, a teammate taking over) and the next person needs to know the goal, what to read first, and what to run next. It complements `/memory` and `/daily`, it points at canonical homes, it does not store durable facts itself.

## Inputs
- The current task and its next goal, stated in a line or two.
- The canonical vault files the next session needs, named by path, not by content: `Company/strategy.md`, the active `Clients/{slug}/` folder, today's `Daily/` note, the relevant `Projects/{slug}/`.
- The open loops still in flight and the last decision that was made.
- The skills that would sensibly run next (for example `/daily`, then `/pipeline-review`).

## Process
1. STATE THE GOAL. Write the next goal in one or two lines, what the next session should accomplish first, so they start aimed instead of guessing.
2. POINT AT THE FILES. List the canonical files to read first by path only (for example `Company/strategy.md`, the active `Clients/{slug}/`, today's `Daily/` note, the relevant `Projects/{slug}/`). Link them, never paste their bodies. The brief is a map, not a copy.
3. NOTE THE LOOPS. List the open loops still in flight and the last decision made, so the next session knows what is unresolved and what is already settled.
4. SUGGEST THE SKILLS. Name the next skills to run, in order, with a word on why each (for example run `/daily` to set the day, then `/pipeline-review` to triage the deals).
5. REDACT. Scrub the brief before writing it. Never include a credential, token, API key, password, or personal contact detail. If a file holds secrets, point at the file by path and let the next session open it themselves.
6. WRITE THE BRIEF. Write the paste-able fresh-session brief to today's `Daily/` note under a `## Handoff` heading. If no daily note exists, write it to `Inbox/` as a dated handoff note instead.

## Outputs
- A short, paste-able fresh-session brief written under a `## Handoff` heading in today's `Daily/` note, or to `Inbox/` if no daily note exists, containing: the next goal, the canonical files to read first (paths only), the open loops and last decision, and the suggested next skills.
- A one-line confirmation in the reply naming where the brief was written and what the stated next goal is.

## Guardrails
- Read only on the vault. The single write is the brief itself (to `Daily/` or `Inbox/`); nothing else in the vault is changed.
- Link canonical files by path, never copy their bodies into the brief. The next session opens the source of truth itself.
- Agency firewall: never copy a confidential client body across the firewall. Point at the active `Clients/{slug}/` folder by path; do not reproduce its contents in a brief that may travel.
- Redact secrets and personal data: no credential, token, API key, password, or personal contact detail ever lands in the brief.
- Draft only. This skill writes a brief for a human or a next session to act on, it sends nothing and contacts no one.
- This is a pointer, not a store. Durable facts belong in `/memory`; the day's log belongs in `/daily`. The handoff only references their canonical homes.

## References
- `Daily/` for today's note, the default home for the handoff brief.
- `Inbox/` for the dated handoff note when no daily note exists.
- `Company/strategy.md` for the canonical strategy the next session reads first.
- The active `Clients/{slug}/` folder and the relevant `Projects/{slug}/` for the live work in flight.
- `/memory` for durable facts and `/daily` for the day's log, the skills this one complements.
