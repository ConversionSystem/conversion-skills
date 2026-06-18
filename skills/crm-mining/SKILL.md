---
name: crm-mining
description: Mine the pipeline and CRM export for stalled deals, dormant accounts, upsell and expansion candidates, and cold prospects, then produce a prioritized revival action list — triggers on "mine the CRM", "find hidden opportunities", "revive stalled deals", "dormant accounts", "upsell candidates", "what deals went cold", "CRM cleanup"
---

# CRM Mining
Read the pipeline and a CRM export to surface hidden revenue — stalled deals to revive, dormant accounts to re-engage, expansion candidates, and prospects gone cold — as a prioritized action list with suggested plays.

## When to use
- The pipeline feels stale and you suspect winnable deals are sitting untouched.
- A fresh CRM export just landed in Inbox/ and needs to be turned into action.
- Before a pipeline review, QBR, or quarterly planning, to find recoverable revenue.
- A quiet sales week is a good moment to work re-engagement instead of only net-new.
- You want a ranked "who to chase first" list rather than a raw account dump.

## Inputs
- `Pipeline/accounts/` and `Pipeline/prospects/` — current account and prospect records (Solo/Team).
- `Pipeline/deals.md` — open deal list with stage, value, and last-activity dates.
- A provided CRM export (CSV/JSON) — typically dropped in `Inbox/`. Map its columns to: account, stage, amount, owner, close date, last activity/contact date, status, lost reason.
- `Company/icp.md` and `Company/offers.md` — to judge fit and frame expansion/upsell plays.
- `Memory/kpi-ledger.md` — for current pipeline baselines and revival targets.
- Agency profile: read only the ACTIVE client's `Clients/{slug}/` workspace (pipeline, `goals.md`, `context/`); never read a sibling client.

## Process
1. **Locate sources.** Identify the active profile. Solo/Team: read `Pipeline/accounts/`, `Pipeline/prospects/`, `Pipeline/deals.md`. Agency: read `Clients/{slug}/` pipeline records for the active client only. Locate the provided CRM export in `Inbox/` (or the path given). If no export exists, mine the vault pipeline alone and note the limitation.
2. **Normalize the export.** Parse the CRM file and map columns to the standard fields (account, stage, amount, owner, last activity date, close date, status, lost reason). Flag rows with missing owners or missing dates — these are themselves a finding (hygiene gaps). Never invent values for blank fields.
3. **Set thresholds.** Establish "stalled" / "dormant" / "cold" windows. Default: stalled = open deal with no activity in 30+ days; dormant account = no contact in 90+ days; cold prospect = engaged once then silent 60+ days. Use any thresholds defined in `_system/config.md` or `Company/strategy.md` if present; otherwise use defaults and state them.
4. **Detect signals.** Pass each record through four lenses:
   - *Stalled deals* — open, mid-stage, past the activity window, still ICP-fit and within reach.
   - *Dormant accounts* — past customers or late-stage accounts that went quiet; re-engagement candidates.
   - *Upsell / expansion* — current customers whose usage, segment, or stated need maps to an offer in `Company/offers.md` they don't yet have.
   - *Cold prospects* — qualified leads that engaged then stopped; worth a fresh touch.
5. **Score and prioritize.** Rank each opportunity by a simple, transparent score: deal/expansion value × ICP fit × recency-of-signal (warmer = higher), minus obvious blockers (hard "no", churned-for-cause, out of segment). Produce a single ordered list, highest-leverage first.
6. **Assign play and owner.** For each opportunity write: account · signal (why it surfaced) · suggested play (the concrete next move) · owner (from the record; flag "unassigned" where blank). Keep plays specific — e.g. "reference the stalled Q1 proposal, offer a scoped pilot" not "follow up".
7. **Draft outreach (optional, draft-only).** For the top opportunities, draft outreach in the business's voice. Load `Library/styles/brand-voice.md` + `Company/brand.md` first (Agency: `Clients/{slug}/context/brand.md`). Every draft carries `status:draft`. Never send, email, or contact anyone.
8. **Write the action list.** Save the prioritized list to the canonical home (see Outputs). Solo/Team route to `Pipeline/` or `Operations/reviews/`; Agency route to `Clients/{slug}/`.
9. **Update the ledger.** Append one row to the KPI ledger recording opportunities found and total revivable value, with the export as source and a confidence rating. Never edit or reorder prior rows.

## Outputs
- **Prioritized action list** — Solo/Team: `Operations/reviews/crm-mining-{date}.md` (or `Pipeline/crm-mining-{date}.md` if run as a pipeline task). Agency: `Clients/{slug}/reviews/crm-mining-{date}.md`. Full frontmatter; `generated:true`; a table of `account · signal · suggested play · owner` ordered by score, plus a short summary of counts and total revivable value by category.
- **Outreach drafts (optional)** — Solo/Team: `Pipeline/outreach/{account-slug}-{date}.md`. Agency: `Clients/{slug}/outreach/{account-slug}-{date}.md`. Each `status:draft`, `confidential:true` for agency outputs.
- **Ledger row** — appended to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), exact columns:
  `| date | metric | baseline | current | target | source | confidence | note |`
  Append two rows where data supports it — `opportunities-found` (count) and `revivable-value` (currency) — each citing the CRM export filename as source and a confidence in {confirmed, reported, inferred, stale}. Counts from a clean export = reported; value estimated from open deal amounts = inferred.

## Guardrails
- DRAFT-ONLY: produce drafts and lists only. Never publish, send, email, post, contact a customer, or change anything in the source CRM. A human ships every touch.
- FIREWALL (Agency): operate inside the ACTIVE client's `Clients/{slug}/` only; never read a sibling client; all client outputs are `confidential:true`.
- VOICE: write any outreach in the business's voice (Agency: the client's voice) — load brand-voice and brand files before drafting.
- PROVENANCE: cite the CRM export for every external fact; never invent metrics, dates, owners, or amounts. Treat blank fields as gaps to flag, not values to guess.
- LEDGER INTEGRITY: append-only; never edit or reorder prior rows; use only the locked columns and confidence vocabulary.
- State the stalled/dormant/cold thresholds used so the list is reproducible and auditable.

## References
- `_system/rules.md` and `_system/config.md` — profile, thresholds, routing.
- `Company/icp.md`, `Company/offers.md` — fit and expansion logic.
- `Library/styles/brand-voice.md`, `Company/brand.md` — voice for drafts.
