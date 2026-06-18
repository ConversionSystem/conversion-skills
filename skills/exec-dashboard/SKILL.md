---
name: exec-dashboard
description: Build a self-contained brand-colored HTML executive dashboard snapshot from the vault when you say generate exec dashboard, executive snapshot, KPI dashboard, or show me the numbers
---

# Executive Dashboard

Generate one self-contained, plugin-free HTML dashboard from the vault as a read-only point-in-time snapshot of KPIs, pipeline, recent decisions and meetings, and today's open Top 3.

## When to use
- You want a single shareable HTML view of where the business stands right now.
- Before a weekly review, board update, or stakeholder check-in.
- After a batch of KPI ledger updates, to see current vs target at a glance.
- Triggers: "generate exec dashboard", "executive snapshot", "KPI dashboard", "show me the numbers", "build the dashboard".

## Inputs
- `Memory/kpi-ledger.md` — the append-only KPI ledger (required source for KPI cards).
- `Pipeline/deals.md` — pipeline summary (Solo and Team modes; absent in Agency-only vaults).
- `Memory/decisions/*.md` — recent decision records.
- `Operations/meetings/*.md` — recent meeting notes.
- `Daily/YYYY-MM-DD.md` — today's Daily note, for the open Top 3.
- `_system/config.md` — brand colors (read for theming) and the escalation contact.
- `Company/brand.md` — brand name and palette fallback if `_system/config.md` lacks colors.

## Process
1. Resolve today's date as ISO `YYYY-MM-DD` from the environment. This is the snapshot date used in the filename, the header, and the "as of" stamp.
2. Read brand colors from `_system/config.md` (fallback `Company/brand.md`); if none found, default to a neutral palette (primary `#1f2937`, accent `#2563eb`, ok `#16a34a`, warn `#d97706`, bad `#dc2626`). Never invent a brand name; use the configured one or "Conversion OS".
3. KPI cards — read `Memory/kpi-ledger.md`. For each distinct `metric`, select the latest row by `date` (last matching row wins; never reorder or edit the ledger). For each metric build a card with: metric name, current, target, source, confidence badge, and a direction indicator computed only from `baseline` vs `current` (up/down/flat). If a metric has no ledger row, render its card as "no data". Never compute or fabricate values not present in the ledger.
4. Pipeline summary — if `Pipeline/deals.md` exists, summarize counts and total value by stage (and any explicit totals already in the file). If the file is absent or empty, render the pipeline panel as "no data". Do not estimate amounts.
5. Recent activity — list the most recent 3-5 entries from `Memory/decisions/` and the most recent 3-5 from `Operations/meetings/`, by file date. Show title, date, and one-line summary pulled from each file's frontmatter or first line. If a folder is empty, show "no recent items".
6. Top 3 — open `Daily/{snapshot-date}.md` and extract the open Top 3 priorities. If today's Daily note is missing or has no Top 3, render "no Top 3 set for today" and note the missing file.
7. Compose ONE HTML document with all CSS inline in a `<style>` block — no external stylesheets, fonts, scripts, or CDN links. Brand-color the header and accents. Lay out KPI cards as a responsive grid, then panels for Pipeline, Recent Decisions, Recent Meetings, and Top 3. Put a prominent banner stating this is a read-only point-in-time snapshot generated on the snapshot date, and that numbers reflect the ledger at generation time.
8. Write the file to `Operations/reviews/dashboard-{snapshot-date}.html`. Mark provenance: embed an HTML comment header with `generated: true`, the source files read, and the generation timestamp.
9. Optionally write a companion `Operations/reviews/dashboard-{snapshot-date}.md` with full universal frontmatter (`generated: true`) recording provenance, since the HTML itself cannot carry frontmatter. Keep it under the 60-line folder budget.
10. Tell the user the snapshot is read-only and offer to refresh it by re-running the skill (which overwrites that date's file).

## Outputs
- `Operations/reviews/dashboard-{YYYY-MM-DD}.html` — self-contained brand-colored dashboard; provenance in a leading HTML comment with `generated: true`, source list, and timestamp.
- `Operations/reviews/dashboard-{YYYY-MM-DD}.md` (optional companion) — universal frontmatter with `generated: true`, `type: dashboard-snapshot`, `source` listing the files read, and a one-line note that the HTML is the artifact.
- No KPI ledger rows are written. This skill is read-only of the vault and appends nothing to `Memory/kpi-ledger.md`.

## Guardrails
- Read-only of the vault: never edit, reorder, or append to `Memory/kpi-ledger.md` or any source file; the only writes are the dashboard HTML and its optional companion `.md`.
- Never invent numbers. Render "no data" for any metric without a ledger row, and "no data" for absent Pipeline/Daily/decisions/meetings sources.
- Snapshot only: state clearly in the HTML and to the user that the dashboard is a point-in-time view; never present it as live.
- Self-contained and plugin-free: inline CSS only, no external dependencies, no network calls, no JavaScript required to read it.
- Agency firewall: include only the current scope's data; never read sibling `Clients/{slug}/` folders. If a source is ambiguous, skip it and note the gap rather than guessing; route genuinely unfiled facts to `Inbox/`.
- Do not auto-send, publish, or share the dashboard. Sharing is a human-approval action; escalate to the contact in `_system/config.md` if distribution is requested.
- Respect `confidential` data: the HTML inherits the sensitivity of its sources; flag it as confidential if any source is.

## References
- `Memory/kpi-ledger.md` (append-only ledger; latest row per metric)
- `Pipeline/deals.md`
- `Memory/decisions/`, `Operations/meetings/`
- `Daily/YYYY-MM-DD.md`
- `_system/config.md` (brand colors, escalation contact)
