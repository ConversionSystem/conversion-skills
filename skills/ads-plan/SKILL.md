---
name: ads-plan
description: Plans a paid-ads campaign from your offers, ICP, and strategy with objective, channel, account structure, budget split, targeting, and three creative angles, triggered by /ads-plan, "plan an ad campaign", "build a paid media plan", or "set up ads"
---

# Ads Plan

Turn Company files into a ready-to-build paid-ads campaign plan: one objective, the right channel, a clean account structure, a budget split, targeting, and three creative angles. Draft only.

## When to use
- You want to run paid ads and need a plan before touching any ad account.
- A new offer or launch needs a media plan grounded in your ICP and strategy.
- You are pitching a paid-ads engagement and need a defensible starting structure.
- Not for editing live campaigns, changing bids or budgets, or anything that publishes. This writes a file you review first.

## Inputs
- `Company/offers.md` (or `Company/offers/`): the offer, price, margin, and the action you want buyers to take.
- `Company/icp.md`: who you target, their pains, where they spend attention, objections.
- `Company/strategy.md`: goals, positioning, and any stated growth targets.
- `Company/brand/` and `Library/styles/brand-voice.md`: voice and claims rules the creative must respect (Agency: the client's voice).
- Optional `Memory/kpi-ledger.md`: current cost per lead, conversion rate, or revenue to set realistic targets.
- Optional ad-platform exports or `_system/connectors.md` entries for benchmark costs. If none exist, state assumptions in the plan.
- From the operator: total monthly budget, geography, and any channel you must use or avoid. If a budget is missing, propose a test budget and mark it as an assumption.

## Process
1. Read `Company/offers.md`, `Company/icp.md`, and `Company/strategy.md`. If any is missing, list what is missing in the plan and proceed with stated assumptions rather than inventing facts.
2. Set ONE objective tied to the buyer action in the offer (lead, booked call, purchase, install). Map it to a measurable target using `Memory/kpi-ledger.md` if a baseline exists, otherwise mark the target as inferred.
3. Choose the channel from where the ICP actually spends attention and how the offer converts: search for active demand, social feeds for created demand, video for reach and warming. Name the primary channel and at most one secondary, with one sentence each on why.
4. Draft the account structure: campaigns by objective or funnel stage, ad sets or ad groups by audience or theme, and the naming convention (for example `{channel}-{objective}-{audience}-{date}`).
5. Split the budget across the structure as percentages and as currency from the supplied total. Reserve 15 to 25 percent for testing. Note the minimum daily spend each ad set needs to exit the learning phase.
6. Define targeting per ad set: audiences, geography, exclusions (existing customers, current pipeline), and any device or schedule limits drawn from the ICP.
7. Write three creative angles, each as a distinct message tied to a specific ICP pain: angle name, hook line, primary text direction, and the offer-aligned call to action. Keep claims inside brand rules and cite the offer for any number used.
8. Add a measurement plan: the one primary metric, two guardrail metrics, the conversion event to optimize toward, and a check-in cadence (for example day 3, day 7, day 14).
9. List launch prerequisites the operator owns: tracking or pixel in place, payment method, landing page live, and any connector setup. Mark each as a to-do, never as done.
10. Assemble the plan and write it. Solo/Team: `Projects/ads-plan-{date}/brief.md`. Agency: the active client workspace at `Clients/{slug}/Projects/ads-plan-{date}/brief.md` with `confidential: true` in the frontmatter. Agency firewall: read only the active client, never a sibling.
11. If a target metric is set or revised from a known baseline, append one row to `Memory/kpi-ledger.md` recording the target. Never edit a prior row.

## Outputs
- `Projects/ads-plan-{date}/brief.md` (Solo/Team) or `Clients/{slug}/Projects/ads-plan-{date}/brief.md` (Agency, `confidential: true`), containing: objective and target, channel choice, account structure with naming convention, budget split (percent and currency), targeting per ad set, three creative angles, measurement plan, and launch prerequisites.
- Supporting notes or supplied benchmark exports saved to `Projects/ads-plan-{date}/data/` (Agency: under the client workspace).
- One appended row in `Memory/kpi-ledger.md` when a target is set from a baseline, columns `| date | metric | baseline | current | target | source | confidence | note |`.

## Guardrails
- DRAFT-ONLY: write the plan file only. Never create or edit campaigns, set bids or budgets in any tool, publish, or contact a client.
- VOICE: creative angles follow `Library/styles/brand-voice.md` (Agency: the client's voice).
- FIREWALL (Agency): work the active client only, never read a sibling client, outputs carry `confidential: true`.
- PROVENANCE: cite the offer and ICP for every claim and number. Never invent costs or conversion rates; mark unknowns as assumptions and label targets `inferred` when no baseline exists.
- CONNECTORS: ad platforms, crawlers, and analytics are optional connectors registered in `_system/connectors.md`. Default to a supplied export or a described setup. Credentials never live in the vault.

## References
- `_system/rules.md` and `_system/connectors.md`
- `Company/offers.md`, `Company/icp.md`, `Company/strategy.md`
- `Library/styles/brand-voice.md`
- `Memory/kpi-ledger.md`
