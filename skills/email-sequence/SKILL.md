---
name: email-sequence
description: Draft a 3-6 email outbound or nurture sequence from offers, ICP, and brand voice when asked to write an email sequence, cold outreach drip, or nurture flow
---

# Email Sequence

Draft a 3-6 email outbound or nurture sequence in the business's voice, each email with a goal, subject-line options, body, and a single CTA, saved as drafts a human sends from their own tool.

## When to use
- The user asks to "write an email sequence", "build a cold outreach drip", "create a nurture flow", "draft outbound emails", or "warm up these leads".
- A new offer in Company/offers.md needs a multi-touch sequence to a defined ICP segment.
- A list of prospects or signups exists and needs a structured, multi-email follow-up.
- Use the single-message companion skill instead when only one email is needed; use this when 3-6 connected touches are wanted.

## Inputs
- Company/offers.md (the offer, promise, proof, price posture, primary CTA).
- Company/icp.md (target segment, pains, triggers, objections, language).
- Library/styles/brand-voice.md and Company/brand.md (tone, banned phrases, reading level). Agency: Clients/{slug}/context/brand.md.
- Optional: a named segment, sequence type (cold outbound vs warm nurture), email count (default 4), and a list of prospects or accounts from Pipeline/.
- Optional: any prior baseline reply rate or booked-call rate (from Memory/kpi-ledger.md or Clients/{slug}/goals.md).

## Process
1. Confirm scope: ask the user for sequence type (outbound or nurture), email count (3-6, default 4), and the target segment if more than one ICP exists. Do not block — infer sensible defaults and state them.
2. Load voice first: read Library/styles/brand-voice.md + Company/brand.md (Agency: Clients/{slug}/context/brand.md). Capture tone rules and banned phrases. Every email is written in this voice.
3. Load substance: read Company/offers.md and Company/icp.md. Extract the offer promise, proof points, the single primary CTA, the segment's top 2-3 pains, buying triggers, and likely objections.
4. Design the arc across the chosen count. Each email advances one job: e.g. (1) relevance + hook, (2) problem/pain agitation, (3) proof/social proof, (4) objection handling, (5) direct ask, (6) breakup. Trim to the chosen count; never pad. One CTA per email, all pointing to the same conversion action (e.g. book a call).
5. Draft each email with: goal (one line), 2-3 subject-line options, a short plain-text body in brand voice, and exactly one CTA. Keep bodies skimmable; cold emails short. Cite any external fact and never invent metrics or case-study numbers — pull proof only from offers.md or approved sources.
6. Resolve the slug: kebab-case from sequence purpose (e.g. "cold-outbound-cfos"). Resolve the date as today in ISO (YYYY-MM-DD).
7. Choose the output home. Solo/Team: Content/{slug}-{date}/. Agency: the active client's Clients/{slug}/ workspace only (confidential:true) — never read or write a sibling client.
8. Write final/email-sequence.md with universal frontmatter and status:draft, containing all emails plus a measurement note (where this is tracked: reply rate and/or booked calls) and a suggested send cadence (e.g. day 0, 3, 6, 10).
9. Write final/brief.md (the sequence's goal, segment, arc, and the human send/measurement plan).
10. Ledger: if a prior baseline reply rate or booked-call rate exists, append one row per relevant metric to the ledger (set baseline, current = baseline, target from the user or a stated assumption, confidence per the source). If no baseline exists, do not invent one — note in the brief that the first send establishes the baseline.

## Outputs
- Solo/Team: `Content/{slug}-{date}/final/email-sequence.md` (status:draft, all emails + measurement note + cadence).
- Solo/Team: `Content/{slug}-{date}/final/brief.md` (goal, segment, arc, send + measurement plan).
- Agency: the same two files under `Clients/{slug}/` per that client's content path, confidential:true.
- Ledger row(s), only if a baseline exists — append-only, exact columns, never edit prior rows:
  - Solo/Team: `Memory/kpi-ledger.md`
  - Agency: `Clients/{slug}/goals.md`
  - Example: `| 2026-06-18 | email reply rate | 4% | 4% | 8% | prior campaign export | reported | baseline for cold-outbound-cfos sequence |`

## Guardrails
- DRAFT-ONLY: status:draft on every file. Never send, schedule, or connect to an email tool to dispatch. A human sends from their own platform.
- VOICE: brand-voice.md + brand.md loaded before writing; honor banned phrases and tone. Agency uses the client's voice.
- FIREWALL (Agency): write only into the active client's Clients/{slug}/ workspace; never read a sibling client; outputs confidential:true.
- PROVENANCE: cite sources for any external fact; never invent metrics, names, or results. Proof comes only from offers.md or cited sources.
- LEDGER: append-only with exact columns and confidence in {confirmed,reported,inferred,stale}; never edit or reorder prior rows; only add a row when a real baseline exists.
- Route to canonical homes; kebab-case slugs; ISO dates; universal frontmatter on every .md.

## References
- Company/offers.md, Company/icp.md
- Library/styles/brand-voice.md, Company/brand.md (Agency: Clients/{slug}/context/brand.md)
- Memory/kpi-ledger.md (Agency: Clients/{slug}/goals.md)
