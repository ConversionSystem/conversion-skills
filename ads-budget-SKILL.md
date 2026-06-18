---
name: ads-budget
description: Allocate and pace ad budget across campaigns by return, find waste, shift spend to winners, and set a weekly pacing plan, run when asked to "allocate budget", "pace spend", "where is my ad budget leaking", or "rebalance campaigns"
---

# Ad Budget
Rank campaigns by return, move spend off losers onto winners, and write a weekly pacing plan you approve before any live change.

## When to use
- Spend is flat but results are not, and you want to know which campaigns to cut or feed.
- A new week or month starts and you need a pacing plan against a fixed budget.
- A metric moved (cac up, roas down) and you want the spend shift that answers it.
- You are reviewing a client account and need a defensible allocation, not a guess.

## Inputs
- A spend export per campaign: spend, conversions, revenue, and dates. Pull from the ad platform UI export, or from a connector listed in `_system/connectors.md` if one is registered.
- The total budget for the period and any per-campaign caps or floors.
- Target cac and target roas. Read from `Company/strategy.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency). If absent, ask once and record the answer.
- Prior baselines from `Memory/kpi-ledger.md` so you compare against last period, not zero.
- Voice from `Library/styles/brand-voice.md` (Agency: the client's voice).

## Process
1. Confirm scope. Solo/Team: write to `Projects/{slug}/`. Agency: confirm the active client, write to `Clients/{slug}/`, set `confidential: true`, and never read a sibling client.
2. Load the spend export and the targets. If a number is missing, mark it and lower confidence rather than inventing it.
3. Compute per campaign: spend, conversions, cac (spend / conversions), revenue, roas (revenue / spend). Carry the date range and the source for each row.
4. Rank campaigns by return against target. Sort into three buckets: winners (roas at or above target, cac at or below target), middle (one of two on target), losers (both off target).
5. Find waste. Flag every loser and every campaign spending above its cap for no return. Sum the dollars sitting in losers as the recoverable pool.
6. Propose the shift. Move the recoverable pool toward winners that have room to scale, respecting caps and floors. Keep a reserve line (default 10 percent) for tests so you do not starve learning.
7. Build the weekly pacing plan. Split the period budget into weekly targets per campaign, with a daily run-rate and a checkpoint date to re-pull and re-rank.
8. Write the allocation to `Projects/{slug}/final/ad-budget-{date}.md` (Agency: `Clients/{slug}/final/ad-budget-{date}.md`): the bucketed table, the proposed shift with dollar deltas, the weekly pacing plan, and the assumptions.
9. Append ledger rows for each metric that moved (spend, cac, roas) to `Memory/kpi-ledger.md`, one row per metric, with the export as source and a confidence value.
10. Stop at draft. List the exact changes for the operator to make by hand in the platform. Never touch a live budget or bid.

## Outputs
- `Projects/{slug}/final/ad-budget-{date}.md` (Agency: `Clients/{slug}/final/ad-budget-{date}.md`): bucketed campaign table, recoverable waste total, proposed shift with dollar deltas, weekly pacing plan with daily run-rate and a re-pull checkpoint, and the assumptions and gaps.
- Appended rows in `Memory/kpi-ledger.md` for spend, cac, and roas, one per metric, columns exactly: date, metric, baseline, current, target, source, confidence, note. Confidence in {confirmed, reported, inferred, stale}. Prior rows are never edited.
- A short operator checklist of manual platform changes to apply after approval.

## Guardrails
- DRAFT-ONLY. Never change a live budget, bid, or campaign state. Output is a plan the operator applies by hand.
- PROVENANCE. Cite the export or connector for every number. Never invent a metric. Append a ledger row whenever a metric moves.
- FIREWALL (Agency). Active client only. Never read a sibling client. Client outputs carry `confidential: true`.
- VOICE. Match `Library/styles/brand-voice.md` (Agency: the client's voice).
- CONNECTORS. Ad platforms and analytics are optional connectors in `_system/connectors.md`. Default to a provided export. Credentials never live in the vault.
- Keep a test reserve so a rebalance does not kill learning, and respect every cap and floor the operator set.

## References
- `_system/connectors.md`
- `Company/strategy.md`
- `Clients/{slug}/goals.md`
- `Memory/kpi-ledger.md`
- `Library/styles/brand-voice.md`
