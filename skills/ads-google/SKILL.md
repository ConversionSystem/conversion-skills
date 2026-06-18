---
name: ads-google
description: Build or optimize a Google Ads account from an export or described setup, structuring Search and Performance Max, keywords, negatives, match types, asset coverage, and conversion tracking into prioritized draft recommendations
---

# Google Ads

Audit and restructure a Google Ads account from an export or a described setup, then hand back a prioritized list of draft changes that you apply by hand. Never touches the live account.

## When to use
- A new Google Ads account or campaign is being stood up and you want the structure right before spend starts.
- An existing account is leaking budget and you need to find the cause: thin ad groups, missing negatives, loose match types, weak assets, broken tracking.
- You exported account data (Editor share, UI report, CSV) and want a read on what to fix first.
- You are about to brief a Performance Max campaign and need an asset and signal checklist.

## Inputs
- An account export or described setup: campaigns, ad groups, keywords with match types, negatives, Responsive Search Ads, Performance Max asset groups, budgets, bid strategies. CSV, Google Ads Editor share, or pasted UI report all work.
- Conversion tracking state: which actions are tracked, primary vs secondary, attribution model, and whether values are passed. A Google Tag or GA4 export helps if available.
- `Company/offers.md` and `Company/icp.md` for the offers and audience the account should serve.
- `Company/strategy.md` for the target cost per acquisition or return target, if recorded.
- Voice from `Library/styles/brand-voice.md` (Agency: the active client's voice file) for any ad copy drafted.
- Optional connector: the Google Ads export tooling registered in `_system/connectors.md`. Default to a provided export or a described setup; never read credentials from the vault.

## Process
1. Confirm scope. Read `_system/rules` and `_system/permissions`. Agency: confirm the active client, stay inside `Clients/{slug}/`, and never read a sibling client. Solo or Team: work under `Projects/{slug}/`.
2. Load context. Pull the offers, ICP, and target cost or return from `Company/`. If the account export is a file, place the raw export under the project `data/` folder unchanged so the read is reproducible.
3. Map the account. List every campaign with its type (Search, Performance Max, Shopping, Display, other), budget, bid strategy, and status. Flag campaigns with overlapping themes that compete for the same queries.
4. Grade Search structure. For each Search campaign, check ad group tightness (one theme per group), keyword count per group, and match type spread. Flag single keyword groups bloated past their theme, broad match running without a tight negative list, and duplicate keywords across groups.
5. Check match types and search terms. If a search terms export is present, sort by spend and by conversions. Flag spend on terms with zero conversions, terms that signal the wrong intent, and queries that deserve their own keyword or their own negative.
6. Build the negative list. Draft account level and campaign level negative keyword lists from the search terms read and from the offers (exclude jobs, free, DIY, competitor brand terms where the offer does not serve them). Note which list each negative belongs to and the match type to add it as.
7. Audit assets. For each Responsive Search Ad, count headlines and descriptions against the maximum and rate variety (benefit, offer, proof, call to action). For each Performance Max asset group, check coverage across headlines, long headlines, descriptions, images, logos, video, and audience signals. List exact gaps to fill.
8. Verify conversion tracking. Confirm a primary conversion action exists, is counted correctly (one per click for leads, every for sales), carries a value where the business has one, and is not double counting. Flag secondary actions promoted to primary by mistake and any campaign optimizing toward a broken or empty action.
9. Read bids and budget. Note the bid strategy on each campaign against the recorded target, whether the conversion volume supports a value based strategy yet, and budgets that cap a profitable campaign or feed a losing one.
10. Prioritize. Sort every finding into Fix now (bleeding money or broken tracking), Fix this week (structure and coverage), and Watch (needs more data). Each line states the change, the exact location in the account, the reason, and the expected effect.
11. Draft, never apply. Write a numbered change list a person can execute step by step in Google Ads Editor or the UI. Mark it draft only. Append a KPI ledger row when a tracked metric (cost per acquisition, conversion rate, wasted spend) is measured at audit time so re-audits chart against it.

## Outputs
- `Projects/{slug}/final/ads-google-audit.md` (Agency: `Clients/{slug}/final/ads-google-audit.md`, `confidential: true`): account map, graded findings, and the prioritized change list marked draft only.
- `Projects/{slug}/final/negatives-list.md` (Agency: under the client): drafted negative keyword lists with target list and match type per line.
- `Projects/{slug}/final/asset-gaps.md` (Agency: under the client): per ad and per asset group coverage gaps with exact counts.
- `Projects/{slug}/data/` holds the raw export unchanged for reproducibility.
- A `Memory/kpi-ledger.md` row per metric measured at audit time, append only, columns: | date | metric | baseline | current | target | source | confidence | note |.

## Guardrails
- Draft only. Never publish, pause, enable, edit budgets or bids, or change anything in the live account. Every output is a recommendation a person applies by hand.
- Provenance. Cite the export or report each finding rests on. Never invent metrics. If a number is not in the export, mark it unknown and say what to pull. Append a ledger row when a metric moves.
- Firewall (Agency). Work the active client only, never read a sibling client, write client outputs with `confidential: true`.
- Voice. Any ad copy drafted follows `Library/styles/brand-voice.md` (Agency: the client's voice file). Stay inside Google Ads character limits.
- Connectors. The Google Ads export tooling is an optional connector in `_system/connectors.md`. Default to a provided export or a described setup. Credentials never live in the vault.
- Confidence. Tag each measured metric confirmed, reported, inferred, or stale by how it was sourced.

## References
- `_system/rules`, `_system/permissions`, `_system/connectors.md`
- `Company/offers.md`, `Company/icp.md`, `Company/strategy.md`
- `Library/styles/brand-voice.md`
- `Memory/kpi-ledger.md`
