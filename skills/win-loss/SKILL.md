---
name: win-loss
description: Analyze why deals were won or lost to find win-rate patterns and lift conversion when you run win-loss, ask why we lose deals, review closed deals, or want a win-loss report
---

# Win/Loss Analysis

Read closed deals and the conversations behind them, surface the patterns that decide outcomes, and turn them into concrete plays that lift win-rate.

## When to use
- A reporting period closed and you want to know why deals were won or lost.
- Win-rate is slipping, stuck, or you suspect a recurring objection, competitor, or price wall.
- Before pricing, positioning, or sales-process changes · to ground the decision in real outcomes.
- After a string of losses (or wins) you want explained instead of guessed.
- Triggers: "win-loss", "why are we losing deals", "review closed deals", "win-loss report", "what's killing our close rate".

## Inputs
- `Pipeline/deals.md` · the deal log with outcomes (won/lost), value, segment, source, competitor, close date. (Agency: `Clients/{slug}/pipeline/deals.md` or the client's deal export.)
- `Pipeline/accounts/` · per-account context for the deals being analyzed.
- `Operations/meetings/` · call notes and discovery/objection records tied to those deals.
- `Memory/decisions/` · prior calls on pricing, positioning, and ICP that shaped these outcomes.
- `Company/icp.md`, `Company/offers.md`, `Company/competitors.md` · to read patterns against your stated target, pricing, and rivals.
- `Memory/kpi-ledger.md` · the current win-rate baseline (Agency: `Clients/{slug}/goals.md`).
- Optional: the period to scope (default: last full quarter) and a minimum deal count for a pattern to count as real.

## Process
1. **Scope.** Confirm the analysis window and profile. Solo/Team writes to `Operations/`; Agency operates inside the ACTIVE client's `Clients/{slug}/` workspace only · never read a sibling client.
2. **Pull the closed set.** From `Pipeline/deals.md`, collect every deal that closed (won or lost) inside the window. Record deal id/name, outcome, value, segment, source, competitor, and close date. Skip still-open deals. Note the raw count of won vs lost.
3. **Compute win-rate.** win-rate = won / (won + lost) for the window, with the row counts shown. If sub-segments have enough volume, compute per segment too. Never extrapolate from a handful of deals · flag thin samples explicitly.
4. **Gather the evidence.** For each closed deal, read its `Pipeline/accounts/` entry and any matching `Operations/meetings/` notes for the stated objection, competitor, and decision driver. Pull relevant `Memory/decisions/` that bear on the outcome. Cite the deal id behind every fact · do not infer reasons that aren't in the record.
5. **Cluster the patterns.** Group outcomes across five lenses and keep only patterns backed by 2+ cited deals:
   - **Segment** · which ICP slices win or lose disproportionately.
   - **Objection** · the recurring reasons lost deals gave (price, timing, trust, fit, no-decision).
   - **Competitor** · who you lose to and what they win on.
   - **Price** · where value/discount mismatches outcomes.
   - **Source** · which lead sources convert vs leak.
6. **Contrast won vs lost.** For the top patterns, name what the won deals did differently (faster follow-up, the right champion, a specific proof point). This is where the recommendations come from.
7. **Write recommendations.** For each pattern, write one concrete, testable action to lift win-rate · pricing tweak, objection-handling script, source reallocation, ICP tightening · each tied to its citing deals and ranked by expected impact.
8. **Name the next play.** Recommend the single highest-leverage next action and the exact Conversion Skills skill to run it (e.g. `case-study` to convert a winning proof point, `pipeline-update` to re-stage at-risk deals, `email-sequence` to script an objection rebuttal, `business-review` to fold findings into strategy).
9. **Write the report.** Solo/Team: `Operations/reviews/{date}-win-loss.md` with `generated:true`. Agency: `Clients/{slug}/reviews/{date}-win-loss.md`, `confidential:true`, in the client's voice. Include universal frontmatter and a sources list of every deal id cited.
10. **Append the ledger row.** Add one APPEND-ONLY win-rate row to the KPI ledger (path per profile). Never edit or reorder prior rows.

## Outputs
- **Report** · `Operations/reviews/{date}-win-loss.md` (Solo/Team, `generated:true`) OR `Clients/{slug}/reviews/{date}-win-loss.md` (Agency, `confidential:true`). Sections: window + win-rate math, patterns (each with cited deal ids), won-vs-lost contrast, ranked recommendations, next play + skill to run, sources list.
- **Ledger row** · one appended line to `Memory/kpi-ledger.md` (Solo/Team) OR `Clients/{slug}/goals.md` (Agency), exact columns:
  `| {date} | win-rate | {baseline} | {current} | {target} | Pipeline/deals.md ({window}) | {confidence} | {note} |`
  with `confidence` in {confirmed,reported,inferred,stale} based on data completeness.

## Guardrails
- DRAFT-ONLY: this is analysis and recommendations. Never contact a prospect, re-stage a deal in a live CRM, change pricing, or send anything · a human acts on the report.
- PROVENANCE: cite the deal id behind every pattern and number. Never invent metrics, reasons, or outcomes; if the record is silent, say so. Win-rate comes only from counted rows in `deals.md`.
- VOICE: load `Library/styles/brand-voice.md` + `Company/brand.md` first (Agency: `Clients/{slug}/context/brand.md`) and write in that voice.
- FIREWALL (Agency): operate only within the ACTIVE client's `Clients/{slug}/` workspace; never read a sibling client; mark all outputs `confidential:true`.
- LEDGER: the win-rate row is APPEND-ONLY with the exact columns; never edit or reorder prior rows.
- THIN DATA: if won+lost is too small for a stable rate or a pattern rests on a single deal, label it inferred/stale and recommend collecting more before acting.

## References
- `Pipeline/deals.md`, `Pipeline/accounts/`, `Operations/meetings/`, `Memory/decisions/`
- `Company/icp.md`, `Company/offers.md`, `Company/competitors.md`
- KPI ledger: `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency)
- Next-play skills: `case-study`, `pipeline-update`, `email-sequence`, `business-review`
