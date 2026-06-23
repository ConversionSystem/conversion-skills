---
name: ads-audit
description: Audit a paid-ads account or set of campaigns for waste and lift from a CSV export or a described setup, producing a prioritized findings report · triggers on "audit my ads", "ads audit", "Google Ads audit", "Meta ads audit", "LinkedIn ads audit", "where am I wasting ad spend", "why is my ROAS low".
---

# Ads Audit

Audit a paid-ads account or set of campaigns (Google, Meta, or LinkedIn) for wasted spend and missed lift, then deliver a prioritized findings report a human can act on.

## When to use
- The user wants a paid-ads account or specific campaigns reviewed for waste and upside.
- A platform export (CSV) is available, or the user can describe how the account is set up.
- The user asks why ROAS is low, where spend is leaking, or whether their account structure, targeting, bidding, or creative is holding them back.
- Use before scaling spend, before a budget reallocation, or as a recurring health check.

## Inputs
- Platform name (google, meta, or linkedin). If unstated, ask before proceeding.
- One or more exports placed in the project's `data/` folder: campaign/ad-group/ad-level performance CSVs, search-terms report (Google), placement report (Meta), audience/demographic breakdowns, conversion-action export. If no export exists, a described setup: campaign list, budgets, targeting, bidding strategy, tracking method, and destination URLs.
- Date range of the data and the account's stated objective (leads, sales, ROAS target, CPA target).
- Company context: `Company/profile.md`, `Company/offers.md`, `Company/icp.md` for offer/audience fit, `Company/brand.md` for voice when judging creative.
- Agency profile: the active client's `Clients/{slug}/context/` files for the same context, used in place of `Company/`.
- Brand voice from `Library/styles/brand-voice.md` (Solo/Team) or `Clients/{slug}/context/brand.md` (Agency) when assessing creative messaging.

## Process
1. **Resolve profile and output home.** Read `_system/config.md` to determine profile.
   - Solo/Team: create `Projects/ads-audit-{platform}-{date}/` with `brief.md`, `data/`, and `final/`.
   - Agency: confirm the ACTIVE client, then work inside `Clients/{slug}/work/ads-audit-{platform}-{date}/`. Operate only within that client's workspace; never read a sibling client. All outputs are `confidential:true`.
2. **Load context and data.** Read the company/client profile, offers, ICP, and brand voice. Ingest every CSV in `data/`. If the user described the setup instead, capture it verbatim into `brief.md`. Record the date range, objective, and any CPA/ROAS targets. Cite the export filename or the user's description as `source` for every fact you use.
3. **Establish baselines.** From the data, compute account-level spend, conversions, CPA/CAC, ROAS (if revenue is present), CTR, and conversion rate for the period. If revenue or conversion values are missing, mark those metrics as unavailable rather than estimating. These become ledger baselines in step 11.
4. **Account structure.** Check campaign/ad-group organization, naming consistency, theme tightness, overlap or duplication across campaigns, and whether structure matches the stated objective. Flag single-keyword-stuffed ad groups, orphaned campaigns, and brand vs non-brand separation.
5. **Targeting.** Review audiences, geo, device, schedule, and (Google) match types and keyword intent; (Meta) audience size and overlap; (LinkedIn) job-title/seniority/company filters. Flag overly broad targeting, audience overlap, irrelevant geos/devices, and missing exclusions.
6. **Budget allocation.** Compare spend distribution against return by campaign/ad set. Flag budget concentrated in low-return campaigns, starved high-performers, and campaigns limited by budget. Quantify spend sitting in the bottom-performing segments.
7. **Bidding.** Assess bid strategy vs objective and data volume (e.g. value-based bidding without conversion values, target-CPA set far from actual CPA, manual bids on a thin account). Flag mismatches and bids that fight the stated target.
8. **Creative diversity and fatigue.** Count active ads/variants per ad group or ad set, check format coverage, and look for fatigue signals (rising frequency with falling CTR, flat or declining performance on aged creative). Flag thin variant counts, single-format reliance, and stale top spenders. Judge messaging against offer and brand voice.
9. **Conversion tracking.** Verify conversion actions exist and look sane: primary vs secondary actions, duplicate or double-counted conversions, missing values, attribution window, and obvious gaps (spend with zero tracked conversions). Flag any campaign spending with no measurable outcome.
10. **Landing-page match and wasted spend.** Check that ad destinations align with ad/keyword intent and the offer (message match, relevance, mobile fit where observable). Identify wasted spend: zero-conversion search terms or placements, irrelevant queries, converting-poorly segments, and spend on paused/irrelevant destinations. Sum estimated wasted spend with its basis.
11. **Score, prioritize, and write the report.** For each finding record: `issue · severity (high/medium/low) · evidence (with source) · fix · est. impact`. Sort by severity then estimated impact. Write `final/ads-audit-{platform}-{date}.md` with universal frontmatter (`status:draft`, `generated:true`), an executive summary, the baselines table, and the prioritized findings table. List the top fixes as a recommended action order. Never propose changes you would apply yourself · every fix is a human decision.
12. **Append the ledger.** Add APPEND-ONLY rows to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) for the baselines you established · e.g. `wasted-spend`, `cac`/`cpa`, `roas`, `ctr`, `conversion-rate` · one row each, using the exact columns and a `confidence` of `confirmed` (from export) or `reported` (from described setup). Never edit or reorder prior rows.

## Outputs
- `Projects/ads-audit-{platform}-{date}/brief.md` (Solo/Team) or `Clients/{slug}/work/ads-audit-{platform}-{date}/brief.md` (Agency) · scope, date range, objective, inputs, sources.
- `…/final/ads-audit-{platform}-{date}.md` · the prioritized findings report (executive summary, baselines table, findings table of issue · severity · evidence · fix · est. impact, recommended action order), `status:draft`, `generated:true`, `confidential:true` for Agency.
- Raw exports retained under `…/data/`.
- Ledger rows appended to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency): one APPEND-ONLY row per established baseline (e.g. wasted-spend, cac/cpa, roas, ctr, conversion-rate) with `source` and `confidence`.

## Guardrails
- DRAFT-ONLY: this skill diagnoses and recommends. Never change budgets, bids, targeting, creative, or campaign status, and never connect to a platform to push changes. A human applies every fix.
- PROVENANCE: cite the export filename or the described-setup note for every finding. Never invent metrics · if revenue, conversion values, or a field are missing, label the metric unavailable rather than estimating. Estimated impact must state its basis.
- VOICE: load brand voice before judging creative; assess messaging in the business's voice (Agency: the client's voice).
- FIREWALL (Agency): operate only within the active client's `Clients/{slug}/` workspace; never read a sibling client; mark all outputs `confidential:true`.
- CONNECTORS: ad-platform connectors are OPTIONAL. Default to provided exports or a described setup. Only use a connector if one is registered in `_system/connectors.md` and the user has enabled it, and even then only to READ.
- LEDGER: append-only with the exact columns; confidence in {confirmed, reported, inferred, stale}; never edit or reorder prior rows.

## Red flags
- Scoring account structure, targeting, or bidding as a problem with no campaign name, search term, or CSV row cited as evidence.
- Quoting a CPA, ROAS, or wasted-spend number that no `data/` export actually contains (estimating a missing metric instead of marking it unavailable).
- Writing "est. impact" on a finding without stating the basis (which segment, which spend, what math).
- Judging ad creative or messaging before brand voice is loaded, or judging it against generic ad rules instead of the offer.
- Severity inflation: most findings tagged "high" with no ranking that separates a six-figure leak from a naming nit.
- Recommending a specific bid, budget, or status change as if you will apply it, instead of leaving it as a human decision.

## Verification
- [ ] Every finding cites a `source`: the export filename or the described-setup note in `brief.md`.
- [ ] Baselines table is built only from present fields; missing revenue/conversion values are labeled unavailable, not estimated.
- [ ] Each finding row carries issue, severity, evidence-with-source, fix, and est. impact (with its basis).
- [ ] Findings are sorted by severity then estimated impact, and a recommended action order is listed.
- [ ] Report frontmatter is `status:draft` and `generated:true` (and `confidential:true` for Agency); nothing was pushed to any ad platform.
- [ ] Brand voice was loaded before any creative or messaging judgment.
- [ ] APPEND-ONLY ledger rows were added for each baseline (wasted-spend, cac/cpa, roas, ctr, conversion-rate) with `source` and `confidence` in {confirmed, reported, inferred, stale}; no prior row edited or reordered.
- [ ] Agency: work stayed inside the active client's `Clients/{slug}/` workspace; no sibling client was read.

## Rationalizations
| Rationalization | Reality |
|---|---|
| "Revenue isn't in the export, I'll estimate ROAS so the table looks complete." | Mark it unavailable. A made-up ROAS gets acted on as fact and sends real budget the wrong way. |
| "The leak is obvious, I don't need to pull the exact search term or row." | No cited row, no finding. Uncited "obvious" waste is the line that gets challenged and kills the whole report's credibility. |
| "This bid is clearly wrong, I'll just set the right target-CPA." | DRAFT-ONLY. You diagnose; a human applies. Pushing a bid change is the one move that can torch spend before anyone reviews it. |
| "I'll skip loading brand voice, bad creative is bad creative." | Voice is the offer's, not yours. Off-voice judgments flag winning ads and miss the ones that actually clash. |
| "I'll tag everything high severity so nothing important gets missed." | All-high is no ranking. The operator fixes the naming convention first and the six-figure budget leak sits another month. |

## References
none
