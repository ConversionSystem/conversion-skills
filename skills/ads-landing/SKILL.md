---
name: ads-landing
description: Critique or draft the page an ad points to for message match, one action, proof, and friction, tied to a conversion metric and written as a draft you ship yourself · triggers on /ads-landing, "review my ad landing page", "ad destination page", "does my landing page match the ad", "post-click page", "message match", "improve ad conversion rate"
---

# Ad Landing

Critiques or drafts the landing page an ad points to, judged on the four things that move post-click conversion: headline match to the ad, one single action, real proof, and removed friction. Tied to a named conversion metric. DRAFT-ONLY: a human ships it.

## When to use

- An ad is running (or about to) and you want the destination page to match the ad and convert the click.
- Click-through is fine but the page converts poorly, and you want the post-click experience diagnosed.
- You are about to scale ad spend and want the destination page checked before more traffic hits it.
- You have ad copy plus a page (or a URL) and want a focused critique of message match, the single action, proof, and friction.
- NOT a full landing page from a blank page for organic or email traffic · that is the landing-page skill. This one is ad-destination focused: it starts from the ad and judges the page against it. NOT an account-level paid audit · that is the ads-audit skill. To draft the page itself from scratch, hand off to landing-page; to fix the ad side, hand off to ads-audit.

## Inputs

- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md`. Agency profile: the CLIENT's `Clients/{slug}/context/brand.md` instead.
- **The ad it points from:** the ad headline, primary text, and the promise/offer the click was sold on, plus the keyword or audience the ad targets · from the user, from an export in the project `data/` folder, or from `Company/offers.md` (Agency: `Clients/{slug}/context/offers.md`). This is the thing the page must match.
- **The page itself:** the live URL, or a page draft in `data/`, or a prior `landing-page` deliverable under `Content/` (Agency: `Clients/{slug}/work/`). If only a URL is given and no crawler connector is registered, ask the user to paste the page copy or save an export to `data/`.
- **The reader:** `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) · who the ad targets, their problem, their objections, the words they use.
- **Proof (real only):** `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) for any cited result; `Operations/case-studies/` for case studies; `Library/swipe/` and `Memory/lessons.md` for angles that worked. Cite proof; never invent it.
- **The conversion metric baseline:** the same ledger file, to read the current post-click conversion rate (or CPA/cost-per-lead) if a baseline exists.
- **From the user (ask only for genuine gaps):** the single action the page should drive and its destination, whether you are critiquing an existing page or drafting one, the traffic source/platform, and any non-negotiable claims or constraints.

## Process

1. **Resolve profile and write location.** Read `_system/config.md` for the profile. Solo/Team: write to `Content/ads-landing-{slug}-{date}/final/`, ledger is `Memory/kpi-ledger.md`. Agency: confirm the ACTIVE client, obey the FIREWALL (read only that client's `Clients/{slug}/`), write to `Clients/{slug}/work/ads-landing-{slug}-{date}/final/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. Use a kebab-case slug and an ISO date. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill.
2. **Load voice, then the ad, then the page.** Read the voice files first, then capture the ad's headline, promise, and target term/audience, then read the page copy. Confirm in one line what you found ("Ad promise: 14-day audit, $0 to start; page headline: 'Grow your agency'; action: book a call; mode: critique") and ask only for genuine gaps (the single action, the page copy if only a URL was given).
3. **Pick the mode.** CRITIQUE if a page exists · score it and prescribe fixes. DRAFT if no page exists and the user wants one · build it ad-first, then hand the full-page build to the landing-page skill. State the mode in the brief.
4. **Name the ONE conversion goal and metric.** One page = one primary action = one metric. Name the single action the click should complete (book a call, start trial, request the audit, buy) and the post-click metric it maps to: post-click conversion rate = action completions / ad clicks (or landing-page sessions from that source). State exactly how and where it is read (form/checkout completions, the UTM on the inbound ad traffic, or a connector in `_system/connectors.md`), plus cost-per-lead/CPA if the ad spend is known. Everything on the page serves this one action.
5. **Score the four levers.** Judge the page against the ad on exactly these, each rated and evidenced:
   - **Headline match** · does the page's headline (and hero) echo the ad's promise and the searched term/audience in the reader's words? A mismatch between the ad clicked and the page seen is the top reason clicks bounce. Flag every gap between ad promise and page headline.
   - **The single action** · is there exactly one primary call to the named action, repeated, with no competing asks above the fold (no nav maze, no second offer, no "learn more" that leaks away)? Flag every competing action.
   - **Proof** · does the page back the promise with real, specific proof near the action (results, a case study, a testimonial, named numbers) rather than adjectives? Flag thin or generic proof; cite only real proof from the ledger or `Operations/case-studies/`.
   - **Friction** · what stands between the click and the action: form length, asking for more than needed, unclear next step, slow or heavy hero, mobile fit, surprise price, missing trust cues at the point of action. Flag each friction point and the cheapest removal.
6. **Mine the offer and ICP into raw material.** Pull the ad-matched promise, the reader's problem in their words, the proof you can legitimately cite, and the top 3-5 objections a fit reader has after clicking. Keep every external fact and every metric traceable to its source; tag anything assumed with `[CHECK]`.
7. **Critique or draft.**
   - CRITIQUE: record each finding as `lever · issue · severity (high/medium/low) · evidence · fix · est. impact on the conversion metric`, sorted by severity then impact. Lead with the headline-match gaps. Give the rewritten hero (headline + subhead) that matches the ad, the single-action treatment, where proof goes, and the friction to cut.
   - DRAFT: write an ad-matched hero (headline echoing the ad promise, subhead naming who it is for and the action), one primary CTA, a tight proof block near the action, and an objection-handling beat for the top 3-5 post-click objections. Keep it to the page the ad needs; hand a full multi-section build to the landing-page skill.
8. **Instrument.** Add a `## How this is measured` block: the named post-click conversion metric, its definition (action completions / ad clicks or source sessions), where it is read (form/checkout analytics, the inbound UTM, or a `_system/connectors.md` connector), a sensible benchmark band, and the one decision the result drives (keep, fix, or pull the ad).
9. **Persist as a draft.** Write the deliverable with `status:draft` and full universal frontmatter, write the brief and data intermediates, and append the ledger row (see Outputs). Close with the next action (a human ships the change; hand off to landing-page for a full build or ads-audit for the ad side). Never publish to the live site or touch the ad.

## Outputs

- **Deliverable** → `Content/ads-landing-{slug}-{date}/final/ads-landing.md` (Solo/Team) or `Clients/{slug}/work/ads-landing-{slug}-{date}/final/ads-landing.md` (Agency), `status:draft`, `generated:true`, containing: the mode, the ad-to-page match summary, the four-lever scorecard (headline match · single action · proof · friction) as a findings table of `lever · issue · severity · evidence · fix · est. impact` for CRITIQUE or the ad-matched hero/CTA/proof/objection copy for DRAFT, and a `## How this is measured` block. Universal frontmatter (type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated). Agency files are `confidential:true`.
- **Brief** → same folder `brief.md`: the ad promise and target term/audience, the page under review (URL or source), the one primary action + destination, the traffic source/platform, the conversion metric, the mode, and acceptance criteria.
- **Intermediate data** → same folder `data/baseline.json`: the named conversion metric, its current baseline (or `null` if none), the target, the four-lever scores, and the proof points cited. Any raw ad/page export retained under `data/`.
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - **Conversion metric:** if a baseline row exists, append the current value with `confidence` in {confirmed,reported,inferred,stale} and its source. If none exists, SEED the metric with a first row (baseline = current = the user-confirmed number, or `inferred` if estimated) and FLAG it for the user to confirm · never invent a baseline.
  - Example: `| 2026-06-18 | post-click-conversion-rate | 3% | 3% | 6% | Content/ads-landing-audit-sprint-2026-06-18/ | reported | message-match fixes drafted; target set, re-read once live |`.
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY.** Produce `status:draft`. Never publish, push to the live site, change a CMS, or edit/pause/repoint the ad · a human ships every change.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` before writing (Agency: the CLIENT's `Clients/{slug}/context/brand.md`). If the voice file is thin, ask for one real sample rather than improvising a voice.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Every result, testimonial, and case-study claim is real and traceable to `kpi-ledger.md`/`goals.md`, `Operations/case-studies/`, or a user-named source; cite external facts; invent no metrics or proof. Use placeholder-and-FLAG when proof is missing. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- One page, one action, one metric. The headline must match the ad; no competing asks above the fold.
- **CONNECTORS.** A crawler or analytics connector is OPTIONAL and READ-only; default to a pasted page or a saved export. Use a connector only if it is registered in `_system/connectors.md` and the user enabled it.
- A delivery run without its ledger row is unfinished.
- Original expression only; no lifted competitor copy or swiped headlines.

## References

- `references/match-checklist.md` · the four-lever checklist (headline match · single action · proof · friction) with severity cues and message-match patterns by ad type (search, paid social, retargeting).
- `Content/` / `Clients/{slug}/work/` prior `landing-page` deliverables · the page to critique or extend.
- `Operations/case-studies/`, `Memory/kpi-ledger.md`, `Clients/{slug}/goals.md` · proof and the post-click conversion baseline.
- `_system/connectors.md` · OPTIONAL crawler/analytics connectors (page fetch, real conversion benchmarks); zero-infra default needs none.
