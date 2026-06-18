---
name: pipeline-review
description: Diagnose sales pipeline health (coverage, conversion, aging, weighted forecast, concentration, source mix) and recommend the highest-leverage actions when you ask to review the pipeline, check pipeline health, forecast the quarter, or find where deals are stalling.
---

# Pipeline Review

Assess the HEALTH of the pipeline (not just its data) and produce a forecast plus the three highest-leverage actions to move the number. This is the diagnosis pass; the refresh pass lives in pipeline-update.

## When to use
- You want a periodic (weekly/monthly/quarter-end) read on whether the pipeline will hit target.
- A deal slipped, a quarter is closing, or coverage feels thin and you need a forecast you can trust.
- You want to know where the leak is: which stage converts poorly, which deals are aging, where revenue is concentrated, and which sources are actually producing.
- Run pipeline-update first if the data is stale; this skill reads, it does not refresh.

## Inputs
- `Pipeline/deals.md` · the deal list with stage, value, owner, source, and dates (the spine of the analysis).
- `Pipeline/accounts/` · per-account context for the deals behind each claim.
- `Pipeline/prospects/` · top-of-funnel context for source-mix and coverage reasoning.
- `Memory/kpi-ledger.md` (Solo/Team) · prior pipeline-value, weighted-forecast, and win-rate rows for trend and baselines. Agency: read the ACTIVE client's `Clients/{slug}/goals.md` instead.
- `Company/strategy.md` · the revenue target / quota to measure coverage against.
- `Company/offers.md` · deal-size norms and expected sales-cycle length to judge aging and stalls.
- `_system/config.md` · profile (Solo/Team vs Agency) and the active client when Agency.

## Process
1. **Resolve profile and target.** Read `_system/config.md`. If Agency, confirm the ACTIVE client and operate only inside `Clients/{slug}/`; never read a sibling client. Pull the revenue target / quota for the period from `Company/strategy.md` (Agency: `Clients/{slug}/context/strategy.md`). If no target is recorded, state that coverage cannot be scored and flag it as a finding.
2. **Load the deals.** Read `Pipeline/deals.md` and the relevant `Pipeline/accounts/` files (Agency: `Clients/{slug}/pipeline/`). Build the working set: for each open deal capture stage, value, owner, source, created date, last-activity date, and expected close date. Note any deal missing a field · do not guess values; mark it "incomplete" and exclude from quantitative claims while listing it as a data-quality gap.
3. **Coverage vs target.** Sum open pipeline value and compute coverage ratio (open pipeline ÷ remaining target for the period). Compare against a healthy band (state the band you use, e.g. 3x). Call out whether there is enough pipeline to credibly hit the number.
4. **Stage-by-stage conversion.** Count deals and value by stage. Where the ledger holds prior win-rate and stage history, compute stage-to-stage conversion and identify the worst-converting step. If history is thin, say so and report current stage distribution only, marked confidence:inferred.
5. **Aging and stalls.** Flag deals whose time-in-stage or days-since-last-activity exceeds the expected sales-cycle norm from `Company/offers.md` (state the threshold). List the specific stalled deals by name with their idle days and owner.
6. **Weighted forecast.** Apply stage probabilities to each deal's value (use ledger-derived stage win-rates if available, else a stated default ladder marked inferred) to produce a weighted forecast for the period. Show best-case (open total), weighted, and commit (late-stage only) so the range is explicit.
7. **Concentration risk.** Identify how much of the weighted forecast sits in the top 1–3 deals, the top account, and any single owner. Flag if the number depends on one deal closing.
8. **Source mix.** Group open pipeline and (where ledger history allows) won deals by source. Identify which sources produce volume vs which produce closed value, and where the pipeline is over-reliant on one channel.
9. **Synthesize the three highest-leverage actions.** From the findings, pick the three moves that most change the forecast (e.g. unstick the two biggest stalled deals, add coverage to a thin stage, fix the worst-converting step). Each action names the specific deals/accounts behind it and the expected effect. Keep to three.
10. **Write the review** to `Operations/reviews/{date}-pipeline-review.md` (Agency: `Clients/{slug}/operations/reviews/{date}-pipeline-review.md`) with full frontmatter, `generated:true`, and `confidential:true` for Agency. Cite the deal names/accounts behind every quantitative claim.
11. **Append ledger rows.** Add APPEND-ONLY rows to `Memory/kpi-ledger.md` (Agency: `Clients/{slug}/goals.md`) for `pipeline-value`, `weighted-forecast`, and `win-rate`, each with `source: {date}-pipeline-review.md` and a confidence value. Never edit or reorder existing rows.

## Outputs
- `Operations/reviews/{date}-pipeline-review.md` (Agency: `Clients/{slug}/operations/reviews/{date}-pipeline-review.md`) · `type: review`, `generated:true`, containing: coverage vs target, stage-by-stage conversion, aging/stalls list, weighted forecast (best-case / weighted / commit), concentration risk, source mix, and the three highest-leverage actions · each claim citing the deals behind it.
- Ledger rows appended to `Memory/kpi-ledger.md` (Agency: `Clients/{slug}/goals.md`), exact columns `| date | metric | baseline | current | target | source | confidence | note |`:
  - `pipeline-value` · total open pipeline, current vs target, confidence per data completeness.
  - `weighted-forecast` · probability-weighted forecast for the period.
  - `win-rate` · observed close rate used in the forecast (confidence:inferred when history is thin).

## Guardrails
- DIAGNOSIS, NOT MUTATION: read-only on pipeline data. Never edit `Pipeline/deals.md`, change a deal's stage, contact a prospect, or send anything. The output is a draft review for a human.
- PROVENANCE: every metric traces to named deals/accounts in the vault. Never invent deal values, stages, win-rates, or sources. If a number rests on incomplete data, mark its confidence and list the gap rather than filling it.
- LEDGER IS APPEND-ONLY: add new rows only; never edit or reorder prior rows. Use confidence in {confirmed, reported, inferred, stale}; default forecast probabilities are inferred until ledger history confirms them.
- FIREWALL (Agency): operate only within the ACTIVE client's `Clients/{slug}/`; never read or compare a sibling client; mark client outputs `confidential:true`.
- VOICE: load `Library/styles/brand-voice.md` and `Company/brand.md` first (Agency: `Clients/{slug}/context/brand.md`) and write the review in the business's voice.
- DATES & ROUTING: ISO dates, kebab-case slugs, canonical homes only.

## References
- pipeline-update (run first to refresh the data this skill reads)
- business-review (consumes this review for the periodic roll-up)
