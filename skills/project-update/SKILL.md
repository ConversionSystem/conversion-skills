---
name: project-update
description: Refreshes a project's brief status acceptance and baseline, logs progress, appends ledger rows for moved metrics, surfaces blockers and the next step, and hands off published work · invoked by "update project", "project update", "log project progress", or "refresh project status".
---

# Project Update

Refresh a `Projects/{slug}/` with current status, progress, and moved metrics, then surface the next concrete step.

## When to use
- A project has changed since the last touch: work shipped, numbers moved, a blocker appeared, or acceptance criteria were met.
- You finished a work session on a project and need to capture state before context is lost.
- The project published an asset (page, post, asset) that should flow into the content pipeline.
- A decision was made mid-project that future work depends on.

## Inputs
- `slug` · the kebab-case project folder under `Projects/{slug}/` (required).
- What changed since last update: progress notes, new metric readings, blockers, decisions, published assets (provided by the user or read from the working session).
- `Projects/{slug}/brief.md` · current status, acceptance criteria, owner.
- `Projects/{slug}/data/baseline.json` · current tracked numbers (created on first update if absent).
- `Memory/kpi-ledger.md` · append target for moved metrics.

## Process
1. **Locate and read.** Open `Projects/{slug}/brief.md`. If the folder does not exist, stop and route the request to `Inbox/` for triage rather than guessing the slug. Read existing `data/baseline.json` if present.
2. **Refresh the brief.** Update `status` in frontmatter (e.g. `active`, `blocked`, `review`, `done`) and bump `date` and `reviewed`. Revise the acceptance-criteria section to mark which criteria are now met and which remain open. Do not invent criteria; only edit what exists.
3. **Log progress.** Append a dated entry to the brief's progress/notes section (or `Projects/{slug}/notes.md` if the brief delegates there): one line per concrete change, newest first, ISO-dated. Omit the section entirely if there is nothing to log.
4. **Update baseline numbers.** Write current readings into `Projects/{slug}/data/baseline.json`, preserving prior keys and only overwriting values that actually changed. Keep it valid JSON; record the as-of date inside the file.
5. **Append ledger rows for moved metrics.** For every metric this project moved, append one APPEND-ONLY row to `Memory/kpi-ledger.md` using the exact columns `| date | metric | baseline | current | target | source | confidence | note |`. Set `confidence` to one of `confirmed`, `reported`, `inferred`, `stale` based on the source. Never edit or reorder existing rows. Skip any metric without a real source.
6. **Surface blockers and the next step.** In the brief, list open blockers plainly and write a single concrete next action (who does what next). If a blocker needs a human-approval gate (send, publish, pricing, permissions), mark the action `status:draft` and note the escalation contact from `_system/config.md`.
7. **Hand off published assets.** If the project published something, create `Content/{slug}-{date}/` with a `brief.md` capturing the asset, its source project, and where it lives in `final/`. Do not publish or send anything; record only.
8. **Record decisions.** For any decision made during the update, write `Memory/decisions/{date}-{topic}.md` with the decision, rationale, and owner, and reference it from the brief.

## Outputs
- `Projects/{slug}/brief.md` · updated frontmatter (`status`, `date`, `reviewed`), refreshed acceptance criteria, appended progress log, blockers, and next step.
- `Projects/{slug}/data/baseline.json` · current numbers with as-of date (created if absent).
- `Memory/kpi-ledger.md` · one appended row per moved metric, exact columns, confidence set.
- `Memory/decisions/{date}-{topic}.md` · one file per decision made (only if a decision occurred).
- `Content/{slug}-{date}/brief.md` · handoff record (only if the project published an asset).

## Guardrails
- Never autonomously send, publish, delete, contact clients, change pricing, or edit permissions; outbound or publish-bound work is written `status:draft` and escalated to the `_system/config.md` contact.
- KPI ledger is append-only: never edit, reorder, or delete prior rows; one row per moved metric only.
- No placeholder files and no empty sections · omit anything with no real content.
- Route facts to their canonical homes; if the project belongs to a client, respect the agency firewall and never read sibling `Clients/{slug}/` folders.
- Use kebab-case slugs and ISO dates. Keep folder context files within size budgets.
- Generated rollups are never hand-edited; only update files this workflow owns.

## References
- `Memory/kpi-ledger.md` (append-only ledger, exact columns)
- `_system/config.md` (escalation contact for approval gates)
- `Content/{slug}-{date}/` (content pipeline handoff)
- `Memory/decisions/` (decision log)
