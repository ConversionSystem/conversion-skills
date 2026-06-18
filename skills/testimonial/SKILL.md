---
name: testimonial
description: Drafts a personalized testimonial or review request to a happy customer and assembles received testimonials into reusable social proof, triggered by "request a testimonial", "ask for a review", "collect social proof", or "add this testimonial to the swipe file"
---

# Testimonial

Turns proven results into a draft ask for proof, and turns received proof into a reusable, consent-flagged social-proof library — pulling the supporting numbers from the ledger, never inventing a quote.

## When to use
- A KPI ledger row shows a real, attributable win for a customer (a metric moved, a baseline beaten, a target hit) and you want to draft an ask for a testimonial or review.
- A customer has sent praise, a quote, a review, or a reference, and you want to file it as structured, reusable social proof.
- You are building a case study, landing page, proposal, or sales asset and need a vetted, consent-cleared quote bank to draw from.
- A renewal, milestone, or successful handoff is a natural moment to request proof.

## Inputs
- The customer/client identity and the slug for routing (`{slug}`).
- KPI ledger: `Memory/kpi-ledger.md` (Solo/Team) OR `Clients/{slug}/goals.md` (Agency) — for the result, baseline→current, source, and confidence backing the ask.
- Voice: `Library/styles/brand-voice.md` + `Company/brand.md` (Solo/Team) OR `Clients/{slug}/context/brand.md` (Agency, the client's voice).
- For assembly job: the raw received testimonial text (paste, email export, review screenshot transcript, or Inbox item) plus who said it, their role/company, and where it came from.
- Profile (Solo/Team vs Agency) and active client, to set routing and confidentiality.
- Optional: `_system/permissions.md` to confirm what external use is pre-cleared.

## Process
1. **Detect job and profile.** Decide whether this run is (1) a REQUEST draft, (2) an ASSEMBLE pass, or both. Read `_system/config.md` for the profile. For Agency, confirm the ACTIVE client and operate only inside `Clients/{slug}/` (firewall).
2. **Load voice.** Read the brand-voice and brand files for the correct owner. Solo/Team: the business's voice. Agency: the client's voice from `Clients/{slug}/context/brand.md`. Write everything in that voice.
3. **Pull the proof from the ledger (REQUEST job).** Open the ledger and find the most recent confirmed/reported row(s) for this customer. Capture the exact metric, baseline, current, target, source, and confidence. NEVER invent or round a number that is not in the ledger; if the only matching rows are `inferred` or `stale`, note that and soften the claim or ask the customer to confirm it in their own words.
4. **Draft the request (REQUEST job).** Write a short, personalized message that: thanks them, names the specific result in their context (e.g. the metric that moved), makes one clear ask (a quote, a star review on a named platform, or a short reference call), offers to draft a starter quote they can edit, and gives an easy out. Keep it human and on-voice. Set `status: draft`. Route to:
   - Solo/Team: `Operations/tasks.md` reference + the draft saved under `Operations/` (e.g. `Operations/testimonial-requests/{slug}-{date}.md`).
   - Agency: `Clients/{slug}/testimonial-request-{date}.md` with `confidential: true`.
   This is DRAFT-ONLY. Never send, email, or post it — a human ships it.
5. **Capture the received proof (ASSEMBLE job).** Take the verbatim quote exactly as the customer wrote it. Do not edit, embellish, or merge quotes. Record: who said it, role + company, date received, source/channel, and any result they cite. Cross-check any number they mention against the ledger; if it matches, cite the ledger row, if it does not, keep the quote as-is but flag the figure as customer-reported, not vault-verified.
6. **Set consent state (ASSEMBLE job).** Mark `consent: pending` until a human confirms the customer approved external use. Note the permission basis (e.g. "approved in email 2026-06-18" or "not yet asked"). Nothing here is cleared for publishing by this skill.
7. **Assemble into the library.** Append the structured entry:
   - Solo/Team (non-client): `Library/swipe/testimonials.md` — a running, reusable swipe bank, each entry with its quote, attribution, cited result + ledger source, and consent state.
   - Agency (client proof): `Clients/{slug}/testimonials.md` (or the client's context folder) with `confidential: true` and `consent: pending`.
8. **Update the ledger if a baseline/result is newly confirmed.** If the testimonial confirms or surfaces a metric not yet logged, APPEND a new row to the correct ledger (never edit prior rows) with `source` = the testimonial and an honest `confidence`.
9. **Flag next step for the human.** End the draft/entry with a one-line note on what a person must do before any external use: send the request, or obtain consent and verify the figure.

## Outputs
- **Request draft (Solo/Team):** `Operations/testimonial-requests/{slug}-{date}.md` (`status: draft`), plus a task line in `Operations/tasks.md`.
- **Request draft (Agency):** `Clients/{slug}/testimonial-request-{date}.md` (`status: draft`, `confidential: true`).
- **Social-proof entry (Solo/Team):** appended to `Library/swipe/testimonials.md` with attribution, cited result, ledger source, and `consent: pending` until cleared.
- **Social-proof entry (Agency):** appended to `Clients/{slug}/testimonials.md` (`confidential: true`, `consent: pending`).
- **Ledger row (optional):** one appended row in `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) only if the testimonial confirms or sets a metric — exact columns `| date | metric | baseline | current | target | source | confidence | note |`, never editing prior rows.
- Every file carries universal frontmatter: `type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated`.

## Guardrails
- DRAFT-ONLY: every request is `status: draft`. Never send, email, post, or submit a review on the customer's behalf. A human ships it.
- NEVER fabricate a quote, a name, an attribution, or a metric. Use the customer's exact words; pull figures only from the ledger or the customer's own statement, and label which.
- CONSENT FIRST: mark `consent: pending` on every assembled testimonial. Flag consent explicitly before any external use (landing page, ad, proposal, case study). This skill never marks consent cleared on its own.
- VOICE: load `Library/styles/brand-voice.md` + `Company/brand.md` (Solo/Team) or the client's `Clients/{slug}/context/brand.md` (Agency) before writing.
- FIREWALL (Agency): operate only within the active client's `Clients/{slug}/` workspace; never read a sibling client; all client outputs are `confidential: true`.
- PROVENANCE: cite the ledger row or channel behind any cited result; when a metric is confirmed or set, append a ledger row with source + confidence. Never edit or reorder prior ledger rows.
- Route outputs to canonical homes; kebab-case slugs; ISO dates.

## References
- `Memory/kpi-ledger.md` and `Clients/{slug}/goals.md` — supporting results and append-only logging.
- `Library/styles/brand-voice.md`, `Company/brand.md`, `Clients/{slug}/context/brand.md` — voice.
- `_system/permissions.md`, `_system/rules.md` — consent and external-use rules.
- `Operations/case-studies/` — downstream home for cleared, verified proof.
