---
type: context
status: active
owner: system
reviewed: 2026-06-18
tags: [router, operations]
confidential: false
source: Conversion OS Setup
generated: false
---

# Operations/ · local rules
Purpose: how the company runs. SOPs, processes, meetings, reviews, tasks.

## Read
- `tasks.md` (the board), `sops/`, `processes/`, recent `meetings/`, `reviews/`.

## Write
- Meeting -> `meetings/YYYY-MM-DD-{topic}.md`; extract decisions+actions.
- New SOP -> `sops/{slug}.md`. Review -> `reviews/{date}-{kind}.md` (generated).

## Never
- Never hand-edit files marked `generated: true` (e.g. rollups).

## Hand-off
- Decisions -> `Memory/decisions/`. Actions -> `tasks.md`. Metrics -> ledger.
