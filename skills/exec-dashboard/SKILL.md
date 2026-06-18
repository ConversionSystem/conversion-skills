---
name: exec-dashboard
description: Build a self-contained brand HTML executive dashboard snapshot from the vault when you say generate exec dashboard, executive snapshot, KPI dashboard, or show me the numbers
---

# Executive Dashboard

Render one self-contained, plugin-free HTML snapshot of where the business stands. KPIs as receipts, pipeline, recent decisions and meetings, today's Top 3. Read-only. Point-in-time. Conversion System brand.

## When to use
- You want one shareable HTML view of the numbers right now.
- Before a weekly review, a board update, or a client check-in.
- After a batch of ledger updates, to see current against target at a glance.
- Triggers: "generate exec dashboard", "executive snapshot", "KPI dashboard", "show me the numbers".

## Inputs
- `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency): the latest row per metric, with `source` and `date`.
- `Pipeline/deals.md`, recent `Memory/decisions/`, recent `Operations/meetings/`, today's `Daily/YYYY-MM-DD.md` (Top 3).
- `_system/config.md`: the business name and escalation contact.
- `assets/brand-tokens.css`: the six colors and the two font stacks. The brand is fixed. Do not read colors from the vault.

## Process
1. Resolve profile and business name from `_system/config.md`. Agency: operate inside the active client only. Mark the file confidential if any source is.
2. Read the latest row per metric (scan the ledger from the bottom). Read pipeline, recent decisions and meetings, and today's Top 3. Read only. Never write a source file.
3. Compose ONE HTML document, all CSS inline in a `<style>` block. No external stylesheet, no script, no CDN. Inline the brand tokens:
   - colors: Paper `#ffffff`, Ink `#0a0a0a`, Indigo `#1a0f6a`, Orange `#ff5a1f`, Solar `#ffd91a`, Cobalt `#1f4cff`, Paper-2 `#f4f4f0`, Mute `#8a8a8a`.
   - fonts: `font-family:'Inter Tight',system-ui,sans-serif` for everything, `'JetBrains Mono',ui-monospace,monospace` for every number. Brand fonts first, system fallback, so it stays self-contained.
4. Header: an Indigo bar carrying the wordmark `CONVERSION / SYSTEM` (slash in Orange, the rest Paper), the descriptor `an AI agency` in small caps, the business name, and the snapshot date in JetBrains Mono.
5. Receipts band (Ink background): the 3 or 4 headline KPIs as receipts. A receipt is a big JetBrains Mono number, a one-line verb-context, and the named source with its date (the ledger row `source` and `date`). Names or it did not happen. Show current against target.
6. KPI grid: every metric as a Paper-2 card. Big Mono number (current), target and direction under it, source and date as a Mono caption. Where a metric has no ledger row, print "no data". Never a guess.
7. Panels: Pipeline (deal, stage, value), Recent decisions, Recent meetings, today's Top 3. Numbers in Mono. Links in Cobalt.
8. Orange discipline: use Orange at most twice on the whole page. Spend it on the single most important number against target, and the one primary action. Everything else is Ink, Indigo, Mute.
9. Snapshot banner: state in the page that this is a point-in-time view generated on the snapshot date, and that numbers reflect the ledger at generation time. Never present it as live.
10. Write to `Operations/reviews/dashboard-{YYYY-MM-DD}.html`. Lead the file with an HTML comment carrying `generated: true`, the source files read, and the generation date.

## Outputs
- `Operations/reviews/dashboard-{YYYY-MM-DD}.html`: a self-contained brand dashboard, provenance in a leading HTML comment (`generated: true`, sources, date). Agency: confidential if any source is.
- Optional `Operations/reviews/dashboard-{YYYY-MM-DD}.md` companion with universal frontmatter (`generated: true`, `type: dashboard-snapshot`, `source` list), under the 60-line folder budget.
- No ledger writes. This skill reads.

## Guardrails
- Read-only of the vault. The only writes are the dashboard HTML and its optional companion.
- Snapshot only. Never present the dashboard as live.
- Self-contained. Inline CSS only, no CDN, no script required to read it.
- Brand is fixed. Six colors, two faces, the wordmark with the Orange slash. Orange at most twice. No em-dashes in any rendered copy.
- Never invent a number. Print "no data" where a metric has no ledger row.
- Respect `confidential`. The HTML inherits the sensitivity of its sources.

## References
- `assets/brand-tokens.css` (the six colors, the two font stacks, the wordmark snippet)
- `BRAND.md` (the brand source of truth)
