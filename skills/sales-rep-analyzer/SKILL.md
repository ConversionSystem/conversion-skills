---
name: sales-rep-analyzer
description: Analyze sales performance from Pipeline and a CRM export to surface conversion by stage and rep, cycle time, win rate, and coaching points when you ask to review sales reps, analyze the pipeline, or score rep performance
---

# Sales Rep Analyzer

Turn Pipeline data and a CRM export into a sourced read on who is closing, where deals stall, and what to coach.

## When to use
- You want win rate, cycle time, and stage conversion broken out by rep.
- A quarter or month closed and you need a performance review backed by the actual deals.
- A rep is underperforming and you want concrete coaching points, not a gut call.
- You are prepping a one-on-one or a forecast and need to know where the pipeline leaks.

## Inputs
- `Pipeline/` deal files (Solo and Team profiles), one record per deal with owner, stage, amount, open date, close date, and outcome.
- A CRM export dropped in `Inbox/` (CSV or markdown table) with the same fields. Used to fill gaps and reconcile against `Pipeline/`.
- `Company/strategy.md` and `Company/offers.md` for target win rate, target cycle time, and deal size context.
- `Memory/kpi-ledger.md` for the prior win-rate baseline.
- Agency profile: read only the active client under `Clients/{slug}/`, never a sibling. Use that client's `goals.md` for their targets.

## Process
1. Resolve scope. Solo and Team read `Pipeline/`. Agency reads only `Clients/{slug}/Pipeline/` for the active client. Confirm the date window (default: trailing 90 days by close date).
2. Load deals from `Pipeline/` and the CRM export in `Inbox/`. Match records by deal id or by company name plus owner. Where the two disagree, prefer the source with the later timestamp and note the conflict.
3. Normalize fields per deal: owner (rep), stage, amount, open date, close date, outcome (won, lost, open). Drop deals missing an owner or a stage and list them as excluded.
4. Compute stage conversion. For each stage, count deals that entered versus advanced, and report the advance rate. Do this overall and per rep.
5. Compute win rate per rep: won divided by (won plus lost) over the window. Compute the team win rate the same way. Cite the deal ids behind each numerator and denominator.
6. Compute cycle time per rep: median days from open date to close date for won deals. Flag reps whose median runs more than 30 percent over the team median.
7. Find the leak. Identify the stage with the steepest drop in advance rate per rep, and name two or three deals that died there as evidence.
8. Write coaching points. For each rep, write two or three concrete actions tied to a number and a named deal (for example, "first-call to demo conversion is 22 percent versus 41 percent team; rework discovery on Acme and Borealis").
9. Compare to targets from `Company/strategy.md` (or the client's `goals.md`). Mark each metric against target as ahead, on, or behind.
10. Write the analysis to `Operations/reviews/{date}-sales-analysis.md` with front matter `generated: true`. Agency: write to `Clients/{slug}/Operations/reviews/{date}-sales-analysis.md` with `confidential: true`.
11. Append win-rate rows to `Memory/kpi-ledger.md`, one for the team and one per rep, using the exact columns. Never edit prior rows.

## Outputs
- `Operations/reviews/{date}-sales-analysis.md` (`generated: true`), containing: scope and date window, excluded deals, stage conversion table (overall and per rep), win rate per rep with cited deal ids, cycle time per rep, the leak with named deals, per-rep coaching points, and a metric-versus-target line. Agency path: `Clients/{slug}/Operations/reviews/{date}-sales-analysis.md` (`confidential: true`).
- Appended rows in `Memory/kpi-ledger.md`, append-only, exact columns `| date | metric | baseline | current | target | source | confidence | note |`. One row for `team win rate` and one per rep (metric `win rate {rep}`). `source` cites the report path and the deal ids; `confidence` is `confirmed` when both `Pipeline/` and the CRM export agree, `reported` when only one source has it, `inferred` when reconstructed from partial data, `stale` when the export predates the window.

## Guardrails
- Draft only. Never message a rep, update the CRM, or change a deal record.
- Cite the deals behind every claim. Every win rate, cycle time, and leak names the deal ids it rests on. Never invent a deal, a metric, or a quote.
- Append a ledger row whenever a win rate moves; never overwrite a prior row.
- Agency firewall: read only the active client's `Pipeline/`, never a sibling. All client outputs carry `confidential: true`.
- When sources conflict or a field is missing, say so in the report and lower the confidence rating rather than guessing.
- Numbers come from the deals on file. If the window has too few closed deals to be meaningful (fewer than five), say so instead of reporting a noisy rate.

## References
- `_system/rules` for vault-wide guardrails and confidence definitions.
- `Memory/kpi-ledger.md` for the append-only ledger contract.
- `Company/strategy.md`, `Company/offers.md`, and (agency) `Clients/{slug}/goals.md` for targets.
