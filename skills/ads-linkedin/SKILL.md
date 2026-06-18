---
name: ads-linkedin
description: Build or optimize LinkedIn Ads for account-based marketing with title and seniority and company targeting, ad formats, bids, and lead-gen forms, drafts only when you say build LinkedIn ads, optimize LinkedIn campaigns, or set up ABM on LinkedIn
---

# LinkedIn Ads

Draft and tune LinkedIn Ads campaigns for B2B and account-based marketing. Targets by title, seniority, and company, picks formats and bids, and builds lead-gen forms. Drafts only, you launch.

## When to use
- You want a new LinkedIn campaign drafted from an offer and an ICP.
- You run LinkedIn Ads now and want a targeting, creative, bid, or lead-form review.
- You are starting account-based marketing and need a tiered company list plan.
- You want a single ad format or audience compared against another before you commit budget.

## Inputs
- Company/offers and Company/icp for the offer, audience, and account tiers.
- Library/styles/brand-voice.md for ad copy voice (agency: the active client's voice).
- A Campaign Manager export (CSV) or a described setup if you are optimizing an existing account.
- Optional: a target-account list (company names or domains) for ABM, and Insight Tag plus Conversions API status.
- _system/connectors.md to see if a LinkedIn export or analytics connector is registered. Default to a provided export when no connector exists.

## Process
1. Read the offer, ICP, and account tiers. Confirm the campaign objective by funnel stage (awareness, lead capture, or pipeline). State it in one line.
2. Build the audience. Use specific job titles, not just functions, plus seniority and company size that match the ICP. Add matched audiences (site retargeting, contact lists) where data exists. Keep audience expansion off for precision and on only for reach. Note minimum audience size of 500 for delivery.
3. For ABM, segment the target-account list into tiers (1, 2, 3) and draft messaging per tier. Note that company-list targeting supports large uploads, so flag any list that is too small to deliver.
4. Pick formats. Default to two or more for a test (single-image, document, video, and a personal-post format for B2B reach). Recommend a budget share for personal-post ads when the offer suits credibility-led reach.
5. Draft ad copy and headlines in the brand voice. Numbers over adjectives, verbs over nouns, one claim per ad. Every metric cited gets a source.
6. Draft the lead-gen form: five fields or fewer, a clear privacy line, and a thank-you action. Note the CRM sync to set up (a connector task, not done here).
7. Set bids and budgets as a draft. Match bid strategy to objective (cost-per-send for message formats, max delivery or manual for content), and set a daily budget that clears the format minimum.
8. Define measurement: conversion events, click and view attribution windows, and a monthly demographics check. List the LinkedIn benchmarks you will read results against (click-through rate, cost per click, lead-form conversion rate).
9. Write the campaign draft, the targeting and bid plan, and a short test plan. If you are optimizing, write a findings list scored pass, watch, or fix, with the highest-impact changes first.
10. If a metric in an export moves a tracked KPI, append one row to Memory/kpi-ledger.md. Never edit a prior row.

Solo and Team write to Projects/{slug}/ . Agency writes to Clients/{slug}/Projects/{slug}/ for the active client only, with confidential:true on every output.

## Outputs
- Projects/{slug}/final/linkedin-campaign.md (or Clients/{slug}/Projects/{slug}/final/linkedin-campaign.md): objective, audience, formats, ad copy, lead-form spec, bids, and budget, marked DRAFT.
- Projects/{slug}/final/linkedin-targeting.md: title, seniority, company, and ABM tier breakdown.
- Projects/{slug}/data/linkedin-findings.md (optimization runs only): checks scored pass, watch, or fix, with a ranked action list.
- A test plan block inside the campaign file: what varies, success metric, and read date.
- One appended row in Memory/kpi-ledger.md when a tracked metric moves, with source and confidence.

## Guardrails
- DRAFT-ONLY. Never launch, publish, change bids or budgets in any live account, or contact a target account. You hand back files.
- VOICE from Library/styles/brand-voice.md. Agency uses the active client's voice.
- FIREWALL (agency): read and write the active client only, never a sibling. All client outputs carry confidential:true.
- PROVENANCE: cite every benchmark and metric to its source. Never invent a number. When a metric moves, append a ledger row.
- Credentials never live in the vault. Ad-platform access is an optional connector in _system/connectors.md. Default to a provided export or a described setup.

## References
- _system/connectors.md (LinkedIn export or analytics connector, if registered)
- Library/styles/brand-voice.md (ad copy voice)
- Memory/kpi-ledger.md (append-only metric log)
