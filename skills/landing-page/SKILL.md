---
name: landing-page
description: Draft a conversion landing page in brand voice from offers and ICP with hero, problem, offer, how-it-works, proof, objections, and one primary CTA, written to Content as a draft you publish yourself - triggers on /landing-page, "write a landing page", "draft a landing page", "build a sales page", "landing page copy", "offer page", "create a landing page for this offer"
---

# Landing Page

Drafts one conversion-focused landing page around a single offer and one primary CTA, written in the business's voice and grounded in real material from the vault. Delivers full section copy plus a section outline. DRAFT-ONLY: a human publishes it.

## When to use

- You have an offer and want a single page built to convert one audience toward one action.
- You are launching, running ads, or sending traffic somewhere and need a dedicated page rather than the homepage.
- You want copy grounded in your real positioning, proof, and objections - not a generic template.
- NOT for blog posts, ungated articles, or multi-offer pages. One page, one offer, one primary CTA. For an email push to the same offer, pair with the email-sequence skill; to drive traffic to the page, pair with the social-post skill.

## Inputs

- **Voice (load first):** `Library/styles/brand-voice.md` + `Company/brand.md`. Agency profile: the CLIENT's `Clients/{slug}/context/brand.md` instead.
- **The offer:** `Company/offers.md` (Agency: `Clients/{slug}/context/offers.md`) - the promise, the deliverable, the price/terms, the guarantee, and the single action the page drives toward.
- **The reader:** `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) - who this is for, their problem, their objections, the words they use.
- **Proof (real only):** `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) for any cited result; `Operations/case-studies/` for case studies; `Library/swipe/` and `Memory/lessons.md` for past angles that worked. Cite proof; never invent it.
- **The conversion metric baseline:** the same ledger file, to read the current conversion-rate or signups baseline if one exists.
- **From the user (ask only for genuine gaps):** which offer, the primary CTA action and its destination/URL, the traffic source if known, and any non-negotiable claims or constraints.

## Process

1. **Resolve profile and write location.** Solo/Team: write to `Content/landing-{slug}-{date}/final/`, ledger is `Memory/kpi-ledger.md`. Agency: resolve the active client, obey the FIREWALL (read only that client's `Clients/{slug}/`), write to `Clients/{slug}/work/landing-{slug}-{date}/final/`, ledger is `Clients/{slug}/goals.md`, set `confidential:true`. Use a kebab-case offer slug and an ISO date. If no root `CLAUDE.md` exists, stop and tell the user to run the setup skill.
2. **Load voice, then context.** Read the voice files first, then the offer, ICP, and proof sources. Confirm in one line what you found ("Voice: plain, direct, numbers over adjectives; reader: ops leads at 20-100-person agencies; offer: the 14-day audit sprint; CTA: book a call") and ask only for what is genuinely missing (the CTA action/URL, the price if not in offers).
3. **Define the ONE conversion goal.** One page = one primary CTA = one metric. Name the single action (book a call, start trial, request the audit, buy) and the conversion metric it maps to (e.g. landing-page conversion rate = primary-CTA completions / unique visitors). State exactly how it is measured and where (form/checkout completions, UTM on the inbound traffic, or a connector in `_system/connectors.md`). Everything on the page serves this one action.
4. **Mine the offer and ICP into raw material.** Pull the core promise, the reader's problem in their own words, the offer's mechanism and deliverables, the proof you can legitimately cite, and the top 3-5 objections to disarm. Keep every external fact and every metric traceable to its source; tag anything assumed with `[CHECK]`.
5. **Outline first, confirm, then write.** Produce the section outline in this order and confirm it before drafting full copy:
   - **Hero** - the promise: one headline (the core outcome), a subhead that says who it's for and how, and the primary CTA above the fold.
   - **Problem** - name the reader's pain in their language; agitate honestly, no fear-mongering.
   - **The offer** - what it is, what's included, the terms; the promise made concrete.
   - **How it works** - the mechanism in 3-4 plain steps so the outcome feels believable.
   - **Proof** - cite real results from the ledger, a case study from `Operations/case-studies/`, or testimonials; if none exist, use a placeholder block and FLAG it - never fabricate proof.
   - **Objections** - answer the top 3-5 reasons a fit reader hesitates (price, time, risk, trust, "will it work for me").
   - **Primary CTA** - one final, unambiguous call to the same single action, with the offer/guarantee restated.
6. **Draft in voice.** Write the full copy for every section in the business's voice (Agency: the CLIENT's voice). One headline, one offer, one primary CTA repeated - no competing secondary asks above the fold. Concrete over generic; every number real and traceable; original expression only.
7. **Instrument.** Add a `## How this is measured` block: the named conversion metric, its definition (CTA completions / visitors), where it's read (form/checkout analytics, UTM, or a `_system/connectors.md` connector), a sensible benchmark band, and the one decision the result drives.
8. **Persist as a draft.** Write the deliverable with `status:draft` and full universal frontmatter, write the section outline and data intermediates, and append the ledger row (see Outputs). Close with the next action (a human builds/publishes the page; pair with social-post or email-sequence to drive traffic). Never publish to the live site.

## Outputs

- **Deliverable** → `Content/landing-{slug}-{date}/final/landing-page.md` (Solo/Team) or `Clients/{slug}/work/landing-{slug}-{date}/final/landing-page.md` (Agency), `status:draft`, containing: full section copy in order (hero · problem · offer · how it works · proof · objections · primary CTA) and a `## How this is measured` block. Universal frontmatter on the file (type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated). Agency files are `confidential:true`.
- **Section outline** → same folder `final/outline.md`: the section skeleton with the one-line purpose and CTA placement for each section, so a designer/builder can lay it out fast.
- **Brief** → same folder `brief.md`: the offer, the audience, the one primary CTA + destination, the traffic source, the conversion metric, and acceptance criteria.
- **Intermediate data** → same folder `data/baseline.json`: the named conversion metric, its current baseline (or `null` if none), the target, and the proof points cited.
- **Ledger row** (APPEND-ONLY, never edit or reorder prior rows) → `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency), EXACT columns: `| date | metric | baseline | current | target | source | confidence | note |`.
  - **Conversion metric:** if a baseline row exists, append the current value with `confidence` in {confirmed,reported,inferred,stale} and its source. If none exists, SEED the metric with a first row (baseline = current = the user-confirmed number, or `inferred` if estimated) and FLAG it for the user to confirm - never invent a baseline.
  - Example: `| 2026-06-18 | landing-conversion-rate | 0 | 0 | 4% | Content/landing-audit-sprint-2026-06-18/ | inferred | new page drafted, target set; baseline once live |`.
- **Activity** → one line to today's `Daily/` note under `## Activity`.

## Guardrails

- **DRAFT-ONLY.** Produce `status:draft`. Never publish, push to the live site, change a CMS, or point traffic at the page autonomously - a human builds and ships it.
- **VOICE.** Load `Library/styles/brand-voice.md` + `Company/brand.md` before writing (Agency: the CLIENT's `Clients/{slug}/context/brand.md`). If the voice file is thin, ask for one real sample rather than improvising a voice.
- **FIREWALL (Agency).** Read and write only the active client's `Clients/{slug}/`; never read a sibling client. Client outputs are `confidential:true`.
- **PROVENANCE.** Every result, testimonial, and case-study claim is real and traceable to `kpi-ledger.md`/`goals.md`, `Operations/case-studies/`, or a user-named source; cite external facts; invent no metrics or proof. Use placeholder-and-FLAG when proof is missing. When a metric moves or a baseline is set, append a ledger row with source + confidence.
- One page, one offer, one primary CTA. No competing asks above the fold.
- A delivery run without its ledger row is unfinished.
- Original expression only; no lifted competitor copy or swiped headlines.

## References

- `references/structure.md` - landing-page section skeletons (lead-gen, sales/checkout, webinar/event, free-audit) and headline patterns.
- `Operations/case-studies/`, `Memory/kpi-ledger.md`, `Clients/{slug}/goals.md` - proof and the conversion baseline.
- `_system/connectors.md` - OPTIONAL analytics/CMS connectors (real conversion benchmarks, draft push); zero-infra default needs none.
