---
name: ads-youtube
description: Plan YouTube video ad campaigns with in-stream, in-feed, and Shorts formats, targeting, a five-second hook, and an ad sequence, draft only. Triggers on "YouTube ads", "video ad plan", "in-stream ads", "Shorts ads".
---

# YouTube Ads

Plan a YouTube video ad campaign before a single dollar is spent. Pick formats, set targeting, write the five-second hook, and lay out an ad sequence. Draft only, nothing is published.

## When to use
- You want to launch video ads on YouTube and need a campaign plan you can hand to a media buyer.
- You have a product, an offer, and a budget range, and you need format choices and targeting mapped to a goal.
- You are scripting video creative and need a hook that survives the first five seconds.
- You want a sequence that walks a cold viewer from a teaser to a direct-response ask across several exposures.

## Inputs
- Company/offers and Company/icp for the product, the price, and who you are selling to.
- Company/strategy and Memory/kpi-ledger.md for the campaign goal and the current cost-per-acquisition baseline.
- Library/styles/brand-voice.md for ad copy voice (agency: the client's voice file under Clients/{slug}/).
- A stated budget range, a flight window, and a primary goal (awareness, consideration, action).
- Optional: existing video assets, a landing page URL, and any export from a prior campaign.
- Optional connectors registered in _system/connectors.md (an ad platform export, an analytics export). Default to a provided export or a described manual setup. No credentials in the vault.

## Process
1. Read the inputs above. If offer, ICP, goal, or budget is missing, ask once, then proceed with stated assumptions and label them.
2. Set the goal and the metric. Map the primary goal to one measured outcome (view rate, cost per view, leads, cost per acquisition) and record the baseline from Memory/kpi-ledger.md. Note the target.
3. Choose campaign types. Pick from the three and say why each fits the goal:
   - In-stream (skippable): plays before or during other videos, viewer can skip after five seconds, you pay on a watched view or an action. Best for reach plus direct response.
   - In-feed (discovery): shows as a thumbnail and headline in search results, the watch feed, and the home feed, the click starts the watch. Best for high intent and consideration.
   - Shorts: vertical, sound-on, fast, served between Shorts. Best for cheap reach and a young mobile audience.
4. Set targeting. For each campaign type list audience signals (life events, in-market, custom segments built from search terms and visited sites), demographics, placements or topics, and exclusions (kids content, sensitive categories, brand-unsafe channels). Keep cold and warm audiences in separate campaigns so you can read the numbers.
5. Write the five-second hook. Draft three openers that name the viewer, the problem, or the payoff inside the first five seconds, before the skip button matters. Each hook states what the viewer gets if they stay. Pull voice from the brand-voice file. No invented claims, no metrics you cannot cite.
6. Build the sequence. Order the ads as a sequence a single viewer sees across exposures:
   - Ad 1, teaser: name the problem, earn the next view.
   - Ad 2, proof: show the product working, cite one real result or a customer quote.
   - Ad 3, ask: a direct-response close with one call to action and the landing page.
   Set the rule that moves a viewer to the next ad (watched, skipped, clicked) and a frequency cap.
7. Draft the call to action and the landing destination. One ask per ad, matched to the page it points to. Note any tracking the media buyer must set up as a described step, not a credential.
8. Write the budget split and flight. Divide the budget across campaign types, set a daily pace, name the flight window, and define a read date to judge results.
9. Assemble the plan file. Solo or Team: write to Projects/{slug}/. Agency: write to Clients/{slug}/Projects/{slug}/ with confidential:true and only the active client in context.
10. If a target metric is named, append one row to Memory/kpi-ledger.md with confidence inferred. Never edit a prior row.

## Outputs
- Solo or Team: Projects/{slug}/brief.md, the campaign plan (formats, targeting, three hooks, the sequence, budget split, flight, read date).
- Agency: Clients/{slug}/Projects/{slug}/brief.md with confidential:true, scoped to the active client only.
- A new appended row in Memory/kpi-ledger.md when a target metric is set, columns | date | metric | baseline | current | target | source | confidence | note |, confidence inferred.
- Draft ad scripts and hooks live under Projects/{slug}/data/ as named drafts. Nothing is published.

## Guardrails
- DRAFT-ONLY. Never publish, launch, fund, or change a bid or a budget on any platform. Never contact a client.
- VOICE from Library/styles/brand-voice.md (agency: the client's voice file).
- FIREWALL (agency): only the active client, never read a sibling client, all client outputs confidential:true.
- PROVENANCE: cite every source, never invent a metric or a result, append a ledger row when a metric moves.
- External ad platforms, crawlers, and analytics are OPTIONAL connectors in _system/connectors.md. Default to a provided export or a described setup. Credentials never live in the vault.

## References
- Company/offers, Company/icp, Company/strategy
- Memory/kpi-ledger.md
- Library/styles/brand-voice.md
- _system/connectors.md
