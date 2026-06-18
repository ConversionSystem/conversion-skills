---
name: ads-tiktok
description: Build or improve TikTok Ads with native creative angles, targeting, Spark Ads, and a strong first-three-seconds hook, all draft only, triggered by "tiktok ads", "spark ad", or "make a tiktok ad".
---

# TikTok Ads

Draft native TikTok creative angles, hooks, targeting, and Spark Ad setup, then score an existing account against a creative-first checklist. Drafts only, never publishes.

## When to use
- You want fresh creative angles or hooks for a TikTok campaign.
- An existing TikTok account is underperforming and you need a scored review.
- You are launching a new offer and need a native-feeling ad plan, not a polished corporate spot.
- You want to test Spark Ads against standard in-feed ads.

## Inputs
- Offer and ICP from `Company/offers.md` and `Company/icp.md`.
- Brand voice from `Library/styles/brand-voice.md` (Agency: the active client's voice).
- Optional TikTok Ads Manager export (CSV of ad groups, spend, CTR, watch time, conversions).
- Optional Pixel and Events API status (installed, firing, ttclid passback yes or no).
- Goal: lead volume, cost per result, ROAS, or app installs.
- Daily budget and target cost per result.

## Process
1. Confirm scope: new creative, account review, or both. If Agency, confirm the active client and read only that client's folder under `Clients/{slug}/`.
2. Load context. Read `Company/offers.md`, `Company/icp.md`, and `Library/styles/brand-voice.md` (Agency: the client's voice file). Pull any prior decisions from `Memory/decisions/`.
3. If an export exists, score the account on five weighted areas: creative (30), tracking (25), bid and budget (20), structure (15), results (10). Mark each check pass, watch, or fail.
   - Creative: 6 or more videos per ad group, all 9:16 at 1080x1920, native and not corporate, hook in the first 1 to 3 seconds, sound-on with trending audio, custom CTA, text and logo inside the safe zone.
   - Tracking: Pixel firing on every page, Events API and ttclid passback live, standard events set (view content, add to cart, purchase, registration).
   - Bid and budget: bid type fits the goal, daily budget at least 50x target cost per result, 50 or more conversions per 7 days per ad group, no edits mid-learning.
   - Structure: prospecting separated from retargeting, search toggle on, placements reviewed, dayparting set to active hours.
   - Results: in-feed CTR at or above 1.0 percent, cost per result inside target with a 3x kill rule, average watch time 6 seconds or more.
4. Draft 3 to 5 native creative angles tied to the offer. For each angle write: the angle in one line, a first-three-seconds hook (spoken and on-screen text), the body beat, and the CTA. Keep it sound-on and UGC in feel.
5. Draft targeting: 1 broad prospecting audience, 1 interest or behavior set, 1 retargeting set (site visitors, video viewers, engagers). Note that broad plus strong creative usually beats narrow targeting here.
6. Draft the Spark Ads plan: which organic posts or creator handles to boost, the standard-versus-Spark test (Spark CTR near 3 percent versus 2 percent standard), and the authorization code step the user runs manually.
7. Write a 5 to 7 day test plan: 3 to 5 hooks per concept, rotate every 5 to 7 days, kill a creative after 3 days under 0.5 percent CTR, scale a winner by duplicating rather than raising budget on the same ad.
8. Write the output file. Solo or Team: `Projects/{slug}/final/tiktok-ads.md`. Agency: `Clients/{slug}/Projects/{slug}/final/tiktok-ads.md` with `confidential: true` in the frontmatter.
9. If a metric moved versus a prior run, append one row to `Memory/kpi-ledger.md` with the source and a confidence value.

## Outputs
- `Projects/{slug}/final/tiktok-ads.md` (Agency: `Clients/{slug}/Projects/{slug}/final/tiktok-ads.md`), containing: health score by area (if an export was given), 3 to 5 creative angles with hooks and CTAs, targeting sets, Spark Ads plan, and the 5 to 7 day test plan.
- A creative scorecard per ad: hook strength, safe-zone check, native feel, sound-on.
- Quick wins sorted by impact at the top of the file.
- One appended row in `Memory/kpi-ledger.md` when a tracked metric moves, columns: date, metric, baseline, current, target, source, confidence, note.

## Guardrails
- DRAFT-ONLY. Never publish, boost, launch, pause, or change budgets or bids inside Ads Manager. The user runs every live action, including the Spark authorization code.
- VOICE from `Library/styles/brand-voice.md` (Agency: the client's voice).
- FIREWALL (Agency): read and write only the active client. Never read a sibling client. Client outputs carry `confidential: true`.
- PROVENANCE: cite the export or source for every metric. Never invent CTR, watch time, or ROAS. When a metric moves, append a ledger row.
- TikTok Ads Manager, the Pixel, and the Events API are optional connectors registered in `_system/connectors.md`. Default to a provided export or a described setup. Credentials never live in the vault.
- Keep all critical text, logos, and CTAs inside the safe zone (clear of the top status area, the bottom caption strip, and the right-side action rail).

## References
- `Company/offers.md`, `Company/icp.md`
- `Library/styles/brand-voice.md`
- `_system/connectors.md`
- `Memory/kpi-ledger.md`, `Memory/decisions/`
