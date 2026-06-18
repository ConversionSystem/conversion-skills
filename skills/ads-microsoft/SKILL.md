---
name: ads-microsoft
description: Build or optimize Microsoft (Bing) Ads by importing from Google, structuring search campaigns, and setting audience targeting, when you say import to Microsoft Ads, set up Bing Ads, or run Microsoft search
---

# Microsoft Ads

Draft a Microsoft Advertising build or optimization: import from Google as a starting point, then restructure search, fix the platform differences that break a straight copy, and layer audience targeting. Draft only.

## When to use
- You run Google Ads and want to extend reach onto Bing, Yahoo, AOL, and the Microsoft Search Network with minimal rework.
- You imported once, it underperformed, and you want a Microsoft-native rebuild rather than a stale mirror of Google.
- You want a search structure (campaigns, ad groups, keywords, match types, negatives) sized for lower volume and older, higher-intent audiences.
- You need audience targeting set up: in-market, LinkedIn profile targeting, remarketing, and custom audiences.

## Inputs
- `Company/profile.md`, `Company/offers.md`, `Company/icp.md` for who you sell to and what you sell.
- An existing Google Ads export or account access (campaign names, ad groups, keywords, ads, budgets) if importing. A CSV or screenshot export is enough.
- `Library/styles/brand-voice.md` for ad copy tone (agency: the active client's voice).
- Target geographies, daily budget, and conversion goals.
- `_system/connectors.md` to check whether a Microsoft Advertising connector or Google export is registered. None required; describe the manual path if absent.

## Process
1. Read `Company/profile.md`, `Company/offers.md`, and `Company/icp.md`. Note the offer, price points, and who buys. Microsoft skews older, higher household income, and more desktop and B2B than Google, so flag which offers fit that audience best.
2. Decide the path: fresh build or import. If a Google export exists, treat it as a draft, not a final. The import copies campaigns, ad groups, keywords, and ads, but it carries over assumptions that do not hold on Microsoft.
3. Map the import differences that matter, and write each as a fix:
   - Bids and budgets: Microsoft volume runs lower, so a copied budget over-allocates. Recommend starting at 30 to 50 percent of the Google daily budget and reading actuals before scaling.
   - Match types: keyword behavior differs slightly and search volume is thinner, so broad match pulls less and needs tighter negatives. Keep exact and phrase for the proven terms.
   - Audience network: Microsoft serves on a syndicated search network (third-party sites beyond Bing). Recommend a separate setting or campaign so you can read Bing-only performance against syndicated traffic and cut what wastes spend.
   - Final URLs and tracking: confirm UTM and tracking templates point to the right place and that the source reads as Microsoft, not a leftover Google value.
   - Unsupported features: some Google asset types and automated rules do not map. List what dropped in the import so nothing silently goes missing.
4. Structure search. Group ad groups by intent and offer, 1 theme per ad group, 5 to 15 keywords each. Write exact and phrase for proven terms, broad only where you have negatives to contain it. Draft a starter negative keyword list and a shared negative list to reuse across campaigns.
5. Draft ads. Write 3 responsive search ads per ad group: 12 to 15 headlines, 4 descriptions, pinned where a claim or brand name must hold position. Pull tone and claims from `Library/styles/brand-voice.md`. Add sitelink, callout, and structured snippet assets. Cite any metric used in copy.
6. Layer audiences. Set in-market and custom audiences as targeting or observation. Add remarketing lists if a tag or list exists. Note LinkedIn profile targeting (company, industry, job function) as a Microsoft-only lever worth using for B2B offers, and mark it as a setup step, not a default-on change.
7. Set geo, schedule, and device bid adjustments from the inputs. Default to observation mode on new audiences so you gather data before you restrict.
8. Write the draft to the output location below. Flag every item that needs a human to push it live in the platform. Change nothing in any live account.

Solo and Team write to `Projects/{slug}/`. Agency writes to `Clients/{slug}/Projects/{slug}/` for the active client only, with `confidential: true` in the front matter.

## Outputs
- `Projects/{slug}/brief.md` (Agency: `Clients/{slug}/Projects/{slug}/brief.md`): the plan, import-vs-build decision, and the difference fixes from step 3.
- `Projects/{slug}/final/microsoft-search-structure.md`: campaigns, ad groups, keywords with match types, negative lists.
- `Projects/{slug}/final/microsoft-ads-copy.md`: responsive search ads and assets, ready to paste into the editor.
- `Projects/{slug}/final/microsoft-audiences.md`: audience targeting plan and the LinkedIn profile setup steps.
- `Projects/{slug}/data/import-diff.md`: what the Google import carried over, changed, or dropped.
- Append 1 row to `Memory/kpi-ledger.md` only when a real metric moves (for example a first cost-per-conversion reads back from the platform). Use the exact columns: | date | metric | baseline | current | target | source | confidence | note |. Set confidence to `inferred` for projections and `confirmed` only for platform-reported numbers. Never edit a prior row.

## Guardrails
- DRAFT-ONLY. Never publish, launch, pause, change a bid or budget, or touch a live account. Every output is a draft a human reviews and pushes.
- VOICE from `Library/styles/brand-voice.md` (agency: the client's voice).
- FIREWALL (agency): the active client only. Never read a sibling client. Mark client outputs `confidential: true`.
- PROVENANCE: cite sources for any claim or metric in copy. Never invent numbers. Append a ledger row when a metric moves.
- The Microsoft Advertising connector is OPTIONAL. With no connector, default to a Google export or a described manual setup. Credentials never live in the vault.

## References
- `_system/connectors.md` for the Microsoft Advertising and Google Ads connector status.
- `Library/playbooks/` for any saved search-structure or negative-list patterns.
