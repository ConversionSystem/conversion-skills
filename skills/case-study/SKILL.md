---
name: case-study
description: Turns a real measured win into a draft case study by pulling outcome numbers from the KPI ledger and structuring situation, what we did, outcome, and a quote placeholder · triggered by "write a case study", "turn this result into a case study", or "draft a case study from the ledger"
---

# Case Study

Turn a confirmed result into a draft case study, sourcing every number from the ledger so nothing is invented.

## When to use
- A metric in the ledger has moved meaningfully (baseline -> current) and the win is worth documenting.
- You want a repeatable proof asset for sales, the site, or a pitch deck · built only from numbers you can stand behind.
- A client or project engagement has reached a milestone with a measurable outcome.
- Do NOT use this to fabricate or estimate results · if there is no ledger row, stop and ask for the data.

## Inputs
- The KPI source for the subject:
  - Solo/Team: `Memory/kpi-ledger.md`
  - Agency: `Clients/{slug}/goals.md` (active client only)
- `Library/styles/brand-voice.md` and `Company/brand.md` (Solo/Team voice) OR `Clients/{slug}/context/brand.md` (Agency, client voice).
- Context on the engagement: `Projects/{slug}/brief.md` or `Content/{slug}-{date}/brief.md` (Solo/Team) OR `Clients/{slug}/` workspace files (Agency).
- Optional: relevant `Operations/sops/` or `Memory/decisions/` notes describing what was actually done.
- The metric name(s) or row(s) to feature, if the user specified them.

## Process
1. **Determine profile and subject.** Read `_system/config.md` to confirm Solo/Team vs Agency. For Agency, confirm the ACTIVE client slug; you will read and write ONLY inside that client's `Clients/{slug}/` workspace.
2. **Load voice.** Solo/Team: read `Library/styles/brand-voice.md` + `Company/brand.md`. Agency: read `Clients/{slug}/context/brand.md`. Write the entire case study in that voice.
3. **Pull the numbers from the ledger · never invent.** Open the KPI source (`Memory/kpi-ledger.md` for Solo/Team, `Clients/{slug}/goals.md` for Agency). Identify the row(s) for the featured metric: capture `date`, `metric`, `baseline`, `current`, `target`, `source`, `confidence`, `note`. If no matching row exists, STOP and ask the user to set a baseline / record the result first. Do not estimate or round beyond what the ledger states.
4. **Check confidence.** If the featured row's `confidence` is `inferred` or `stale`, flag it inline in the draft (e.g. `> NOTE: outcome confidence is "inferred" · verify before publishing`). Prefer `confirmed`/`reported` rows for headline claims.
5. **Reconstruct the story.** From the brief/SOP/decision notes, write the engagement as: SITUATION (where they started, the problem) -> WHAT WE DID (the specific intervention, no fluff) -> MEASURED OUTCOME (cite the ledger: baseline -> current vs target, with `source`).
6. **Cite every external fact and metric.** Inline-reference the ledger row and any external source. Never state a number that is not traceable to the ledger or a cited source.
7. **Insert a quote placeholder.** Add a clearly marked placeholder for a client/customer testimonial, e.g. `> "{TESTIMONIAL · pending from {name/role}}"`. Do not write a fake quote.
8. **Agency anonymization + consent.** For Agency client material, default to anonymizing identifying details (use role/industry/size instead of name unless consent is on file) and set `consent: pending` in frontmatter. Reference NO other client anywhere in the file (firewall).
9. **Write to the canonical home** (see Outputs) with `status:draft` and full universal frontmatter. This is a candidate draft only.
10. **Append a ledger row** recording that the result was packaged into a case-study draft (provenance), without editing or reordering any prior row.
11. **Hand off.** Tell the user the draft is ready, which metric/row it cites, any confidence or consent flags, and that publishing requires a human (and, for Agency, client consent).

## Outputs
- **Solo/Team:** `Content/{slug}-{date}/final/case-study.md` · `status:draft`, full frontmatter, `confidential:false` (unless sensitive), `generated:true`. Save supporting figures under `Content/{slug}-{date}/data/` if any.
- **Agency:** `Operations/case-studies/{slug}.md` · `status:draft`, `confidential:true`, `consent: pending`, anonymized, firewall-safe (no other client named), `generated:true`.
- **Ledger row appended** (APPEND-ONLY, exact columns) to the same KPI source the numbers came from:
  - Solo/Team -> `Memory/kpi-ledger.md`
  - Agency -> `Clients/{slug}/goals.md`
  - Example: `| {ISO date} | case-study-draft:{slug} | · | drafted | published | {path to case-study file} | inferred | Packaged confirmed outcome into case-study draft; awaiting human sign-off |`

## Guardrails
- DRAFT-ONLY: every output carries `status:draft`. Never publish, post, send, or email the case study. A human ships it; Agency also requires client consent.
- PROVENANCE: every metric traces to a ledger row or a cited external source. Never invent, estimate, or inflate a number. No ledger row -> no claim.
- LEDGER INTEGRITY: append rows only; never edit, reorder, or delete prior rows. Confidence stays in {confirmed, reported, inferred, stale}.
- VOICE: write in the business's voice (Solo/Team) or the CLIENT's voice (Agency), loaded before drafting.
- FIREWALL (Agency): read and write only inside the active `Clients/{slug}/` workspace and `Operations/case-studies/{slug}.md`; never read a sibling client; never name another client; client outputs are `confidential:true`.
- CONSENT (Agency): set `consent: pending`, anonymize identifying details by default, and do not present the draft as approved for external use until consent is confirmed.
- Quote stays a placeholder until a real, attributed testimonial is supplied · never fabricate quotes.

## Orchestration
Run `agents/judge` on every claimed number against its ledger row before the case study ships; cut what it refutes. See `docs/orchestration.md`.

## References
none
