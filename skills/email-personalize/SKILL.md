---
name: email-personalize
description: Personalize one outbound email to a single prospect from their Pipeline profile, research, offers, and brand voice when asked to personalize an email, write a one-to-one cold email, or tailor outreach to a specific person
---

# Email Personalize

Personalize a single outbound email to ONE named prospect, producing 1-2 variants with an earned opener tied to a real signal about them, one relevant value line, and one CTA, saved as a draft a human sends.

## When to use
- The user asks to "personalize this email", "write a one-to-one cold email", "tailor outreach to [person]", "warm up this specific prospect", or "make this email about them".
- A prospect in Pipeline/prospects/ or Pipeline/accounts/ is ready for first-touch or a follow-up and warrants a hand-tuned, not templated, message.
- Fresh research or enrichment exists on one person (a post, a hire, a launch, a funding round, a podcast, a job change) that can anchor a genuine opener.
- Use the multi-touch companion skill instead when 3-6 connected emails to a segment are wanted; use this when exactly one message to one named person is needed.

## Inputs
- The prospect's Pipeline file: Pipeline/prospects/{slug}.md or the contact inside Pipeline/accounts/{slug}.md (name, role, company, status, prior touches, known pains).
- Any research/enrichment on this person: notes in the prospect file, an enrichment block, Inbox/ exports, or a URL/text the user provides (post, article, announcement, profile).
- Company/offers.md (the offer, promise, proof, single primary CTA).
- Company/icp.md (to confirm fit and pull the segment's language and triggers).
- Library/styles/brand-voice.md and Company/brand.md (tone, banned phrases, reading level). Agency: Clients/{slug}/context/brand.md.
- Optional: email type (first-touch vs follow-up), the desired CTA (default: book a short call), and any prior reply-rate baseline from Memory/kpi-ledger.md or Clients/{slug}/goals.md.

## Process
1. Identify the one prospect. Resolve their Pipeline file by slug; if it does not exist, ask the user to name the prospect or paste their details — never personalize a generic placeholder. State the email type (first-touch or follow-up); default to first-touch.
2. Load voice first: read Library/styles/brand-voice.md + Company/brand.md (Agency: Clients/{slug}/context/brand.md). Capture tone rules and banned phrases. Both variants are written in this voice.
3. Find the signal. Read the prospect file plus any provided research/enrichment and pull ONE specific, real, recent fact about this person or their company (a post they wrote, a role change, a launch, a hire, a funding event, a stated initiative). Record the exact source. If no genuine signal exists, say so and offer to run enrichment/research first — never fabricate a signal or write a fake compliment ("love what you're doing").
4. Load substance: read Company/offers.md and Company/icp.md. Confirm this prospect fits the ICP, and extract the offer promise, the one proof point most relevant to their signal, and the single primary CTA.
5. Build the structure: (a) an earned opener that names the real signal and connects it to a relevant tension or opportunity — not flattery; (b) one value line that bridges the signal to the offer's promise, carrying at most one proof point; (c) exactly one CTA (default: a short, low-friction ask such as a brief call or a single yes/no question).
6. Draft 1-2 variants (default 2: one shorter/sharper, one slightly warmer). Each gets 2-3 subject-line options. Keep bodies short and skimmable — cold emails tight. Cite any external fact; never invent metrics, names, or case-study numbers — proof comes only from offers.md or a cited source.
7. Resolve date as today in ISO (YYYY-MM-DD). Choose the output home: write the draft into the prospect's Pipeline file (preferred when it exists), OR to Content/{slug}-{date}/final/email-personalize.md when the user wants a standalone artifact. Agency: write only inside the active client's Clients/{slug}/ workspace (confidential:true) — never read or write a sibling client.
8. When writing into the Pipeline file, append a dated "Personalized draft" section with status:draft and the signal cited inline; do not overwrite prior touches or history. When writing a standalone file, use universal frontmatter with status:draft.
9. Record the signal and source explicitly next to the draft (one line: what the personalization is built on and where it came from) so the human can verify before sending.
10. Ledger: if a prior reply-rate baseline for this prospect's segment exists, you may append one row (baseline, current = baseline, target from the user or a stated assumption, confidence per the source). If no baseline exists, do not invent one — note that the first send establishes it.

## Outputs
- Pipeline-home (preferred): an appended, dated `status:draft` "Personalized draft" section in `Pipeline/prospects/{slug}.md` (or the contact block in `Pipeline/accounts/{slug}.md`) containing 1-2 variants, subject-line options, and the cited signal. Agency: the equivalent file under `Clients/{slug}/`, confidential:true.
- Standalone option: `Content/{slug}-{date}/final/email-personalize.md` (status:draft, variants + subject lines + the cited signal + send note). Agency: the same under `Clients/{slug}/` per that client's content path, confidential:true.
- Ledger row, only if a baseline exists — append-only, exact columns, never edit prior rows:
  - Solo/Team: `Memory/kpi-ledger.md`
  - Agency: `Clients/{slug}/goals.md`
  - Example: `| 2026-06-18 | email reply rate | 6% | 6% | 12% | prior 1:1 outreach log | reported | baseline for personalized first-touch |`

## Guardrails
- DRAFT-ONLY: status:draft on every output. Never send, schedule, or connect to an email tool to dispatch, and never contact the prospect autonomously. A human sends from their own platform.
- EARNED OPENER: the personalization must be built on a real, cited signal about this prospect. Never write a fake compliment or invent a fact; if no genuine signal exists, stop and offer enrichment/research instead.
- VOICE: brand-voice.md + brand.md loaded before writing; honor banned phrases and tone. Agency uses the client's voice from Clients/{slug}/context/brand.md.
- FIREWALL (Agency): operate only inside the active client's Clients/{slug}/ workspace; never read a sibling client; outputs confidential:true.
- PROVENANCE: cite the signal's source and any external fact; never invent metrics, names, or results. Proof comes only from offers.md or a cited source.
- LEDGER: append-only with exact columns and confidence in {confirmed,reported,inferred,stale}; never edit or reorder prior rows; only add a row when a real baseline exists.
- Route to canonical homes; kebab-case slugs; ISO dates; universal frontmatter on every .md.

## References
- Pipeline/prospects/{slug}.md, Pipeline/accounts/{slug}.md
- Company/offers.md, Company/icp.md
- Library/styles/brand-voice.md, Company/brand.md (Agency: Clients/{slug}/context/brand.md)
- Memory/kpi-ledger.md (Agency: Clients/{slug}/goals.md)
