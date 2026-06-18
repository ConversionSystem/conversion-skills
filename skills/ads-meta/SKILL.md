---
name: ads-meta
description: Build or optimize Meta Ads with campaign structure, audience choices, creative formats, Advantage+ notes, and pixel or CAPI tracking checks, when you say "build Meta ads", "optimize Facebook ads", or "check my Meta tracking"
---

# Meta Ads

Draft a Meta Ads build or optimization brief: campaign structure, audience approach, creative formats, Advantage+ notes, and tracking checks, all as files you review before anything goes live.

## When to use
- You are launching a new Meta (Facebook and Instagram) campaign and want a structure plus creative brief before touching Ads Manager.
- An existing campaign is under target and you want a written read on what to change.
- You want a tracking check before spend: pixel firing, CAPI status, event match quality, and conversion event mapping.
- You need a creative format plan (static, video, carousel) tied to one offer and one audience.

## Inputs
- Offer and goal from `Company/offers/` and the active goal (Solo/Team: the campaign goal in the project brief; Agency: `Clients/{slug}/goals.md`).
- ICP and audience notes from `Company/icp/`.
- Voice from `Library/styles/brand-voice.md` (Agency: the active client's voice file).
- Current account export if optimizing: campaign, ad set, and ad level numbers (spend, CPM, CTR, CPA, ROAS) as a CSV or pasted table. No login required.
- Tracking facts: pixel ID present yes/no, CAPI configured yes/no, event match quality score if known, primary conversion event name. Register any Meta connector in `_system/connectors.md`; never store credentials in the vault.
- Baseline metrics from `Memory/kpi-ledger.md` if a prior run exists.

## Process
1. Read the offer, goal, ICP, and voice. Confirm one offer and one primary conversion event. If either is unclear, write the open question into the brief and continue with a stated assumption.
2. Set the campaign objective. Map the goal to a Meta objective (Sales, Leads, Traffic, Awareness, App). Note budget level: campaign budget (Advantage campaign budget) for consolidated learning, or ad set budget when you need control per audience.
3. Lay out structure. Recommend a consolidated build: few ad sets, several ads each, so the system exits the learning phase. Record the target of roughly 50 conversion events per ad set per week as the signal floor, and flag ad sets that cannot reach it.
4. Choose the audience approach for each ad set:
   - Broad: age, gender, country, language only, system finds buyers. Default for accounts with clean conversion signal.
   - Detailed targeting: interests or behaviors, narrower, for thin signal or a sharp niche. Note that Advantage detailed targeting expansion can widen this.
   - Custom and lookalike: from a provided customer list export or site visitors via the pixel. Note retargeting as a separate ad set or campaign.
   Write which approach fits this account and why, in one or two lines each.
5. Note Advantage+ options plainly: Advantage+ Sales (formerly the shopping campaign) for catalog or repeat purchase accounts, Advantage+ creative enhancements (set on or off and why), Advantage+ audience as the broad default with an audience suggestion. State what each one does and when to leave it off.
6. Plan creative formats. For the one offer, draft 3 to 5 ad concepts across formats (single image, short video, carousel), each with a hook line, primary text, headline, and a stated visual direction. Keep copy in voice. Mark any creative that needs a designer or video as a dependency, not a finished asset.
7. Run the tracking check. Confirm pixel present and firing the primary event, CAPI configured for server-side backup, event match quality acceptable, and the conversion event chosen in the ad set matches the offer. List each as pass, gap, or unknown with the fix for every gap.
8. If optimizing, read the export. Diagnose at the right level: creative (low CTR), audience or bid (high CPM, low volume), or landing and offer (clicks but no conversions). Tie each recommendation to a number from the export, never to a guess.
9. Write the brief and, if a tracked metric moved versus a prior run, append one row to the KPI ledger. Keep everything draft. Never publish, never change live budgets or bids, never contact a client.

## Outputs
- Solo/Team: `Projects/{slug}/final/meta-ads-brief.md` with the campaign structure, per ad set audience approach, Advantage+ notes, creative concepts, and the tracking check table. Supporting export goes in `Projects/{slug}/data/`.
- Agency: `Clients/{slug}/Projects/{slug}/final/meta-ads-brief.md`, marked `confidential: true`, scoped to the active client only.
- KPI ledger: when a metric moves, one appended row in `Memory/kpi-ledger.md` using the exact columns | date | metric | baseline | current | target | source | confidence | note |. Never edit a prior row.
- Open questions and assumptions listed at the top of the brief.

## Guardrails
- DRAFT-ONLY. This skill writes files. It never launches a campaign, edits a live budget or bid, publishes an ad, or contacts a client.
- VOICE from `Library/styles/brand-voice.md` (Agency: the client's voice).
- FIREWALL (Agency): read and write only the active client. Never read a sibling client. Client outputs carry `confidential: true`.
- PROVENANCE: cite the export or source for every number. Never invent a metric, a match quality score, or a result. Mark unknowns as unknown.
- External tools (Meta Ads Manager, the pixel, CAPI, a customer list) are optional connectors in `_system/connectors.md`. Default to a provided export or a described setup. Credentials never live in the vault.

## References
- `Company/offers/`, `Company/icp/`, `Library/styles/brand-voice.md`
- `Memory/kpi-ledger.md`
- `_system/connectors.md`
