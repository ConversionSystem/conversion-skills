---
name: lead-qualify
description: Score a lead or prospect against your ICP and return a qualified, not-qualified, or needs-info verdict with reasons, fit score, and the next human action when asked to qualify a lead, score a prospect, or check if a lead is a fit
---

# Lead Qualify

Score a single lead/prospect against `Company/icp.md`, produce a verdict with reasons mapped to ICP criteria, and recommend the next human action. Never contacts the lead.

## When to use
- A new lead/prospect arrived and you need a qualified / not-qualified / needs-info call before anyone spends time on it.
- You want a defensible fit score with reasons tied to explicit ICP criteria, not a gut feel.
- A prospect file in `Pipeline/` needs a recorded verdict before it moves to outreach or gets dropped.
- Triggers: "qualify this lead", "score this prospect", "is this lead a fit", "should we pursue this account".

## Inputs
- The lead/prospect: an existing file in `Pipeline/prospects/` or `Pipeline/accounts/`, OR raw details (name, company, role, size, industry, signals, source) pasted by the user.
- `Company/icp.md` — the ideal customer profile and its criteria (required; the scorecard is meaningless without it).
- `Company/offers.md` — to sanity-check fit against what is actually sold (optional but recommended).
- `_system/config.md` — to read the active profile (Solo/Team vs Agency) and the ledger location.
- Agency only: the ACTIVE client's `Clients/{slug}/context/icp.md` (use the client's ICP, not the agency's).

## Process
1. **Resolve profile and paths.** Read `_system/config.md` for the active profile. Solo/Team: score against `Company/icp.md`, write to `Pipeline/`, ledger at `Memory/kpi-ledger.md`. Agency: score against the ACTIVE client's `Clients/{slug}/context/icp.md`, write only into that client's `Clients/{slug}/` workspace, ledger at `Clients/{slug}/goals.md`. Never read a sibling client.
2. **Load the ICP.** Read the applicable `icp.md` and extract its criteria into a checklist: firmographics (industry, company size, geography, revenue), role/seniority of the contact, pain/trigger signals, budget/authority indicators, and any explicit disqualifiers. Optionally read `offers.md` to confirm the lead could plausibly buy.
3. **Locate or create the prospect file.** If the lead already exists, find it at `Pipeline/prospects/{slug}.md` (Solo/Team) or under the active client's workspace (Agency). If it is raw input, create `Pipeline/prospects/{slug}.md` with a kebab-case slug, universal frontmatter, and the supplied details. Do not invent missing facts.
4. **Score each criterion.** For every ICP criterion, mark met / not-met / unknown with one line of evidence and the source of that evidence. Cite the source for any external fact; never fabricate firmographics, revenue, or signals — mark them unknown instead.
5. **Compute the fit score.** Score 0–100 = (criteria met / total weighted criteria) expressed as a percentage; weight any criteria the ICP flags as must-haves higher, and treat an explicit disqualifier as an automatic cap. State the simple formula used so the number is reproducible.
6. **Decide the verdict.** `qualified` = all must-have criteria met and score above the ICP's bar; `not` = a disqualifier is hit or must-haves fail; `needs-info` = one or more must-have criteria are unknown and the gap is answerable. Map every reason back to a named ICP criterion.
7. **Recommend the next human action.** One concrete step: e.g. "human books a discovery call", "human sends to nurture", "human asks for headcount before deciding", "drop — out of ICP". Never contact the lead yourself; this is a recommendation for a person to execute.
8. **Update the prospect file.** Append a `## Qualification — {date}` section with the verdict, fit score, per-criterion reasons, and recommended next step; set `status:` in frontmatter to `qualified`, `not-qualified`, or `needs-info`, and update `reviewed` to today's date.
9. **Append the ledger row.** Add one APPEND-ONLY row to the KPI ledger recording the qualified-leads metric. Never edit or reorder prior rows.

## Outputs
- Updated prospect file (Solo/Team): `Pipeline/prospects/{slug}.md` — frontmatter `status` set to the verdict, `reviewed` set to today, plus a `## Qualification — {date}` block (verdict, fit score 0–100, per-criterion reasons mapped to ICP, recommended next human action). Agency: the same block written under `Clients/{slug}/` with `confidential: true`.
- One appended KPI ledger row (Solo/Team `Memory/kpi-ledger.md`; Agency `Clients/{slug}/goals.md`):
  `| {date} | qualified-leads | {baseline} | {current} | {target} | {prospect-file-path} | {confidence} | {verdict} {slug} fit {score} |`
  with `confidence` in {confirmed, reported, inferred, stale} reflecting how solid the lead's data is (confirmed sources → confirmed; unknowns filled by assumption → inferred).
- A short verdict summary returned to the user: verdict, fit score, top reasons, next human action.

## Guardrails
- DRAFT-ONLY: this produces a verdict and a recommendation only. NEVER contact, email, message, or otherwise reach out to the lead — a human takes the next step.
- PROVENANCE: cite a source for every external fact used in scoring; never invent metrics, firmographics, or signals. Unverifiable criteria are marked `unknown`, which pushes toward `needs-info`, not toward a guess.
- FIREWALL (Agency): read and write only the ACTIVE client's `Clients/{slug}/` workspace; never read a sibling client; mark all client outputs `confidential: true`.
- LEDGER: the KPI ledger is append-only with the exact columns `| date | metric | baseline | current | target | source | confidence | note |`. Never edit or reorder existing rows.
- VOICE: any human-facing note text follows `Library/styles/brand-voice.md` and `Company/brand.md` (Agency: the client's `Clients/{slug}/context/brand.md`).
- Keep slugs kebab-case and all dates ISO (YYYY-MM-DD). Route the prospect file and ledger row only to their canonical homes.

## References
- `Company/icp.md` (Agency: `Clients/{slug}/context/icp.md`) — ICP criteria source
- `Company/offers.md` — buyability sanity check
- `_system/config.md` — active profile and ledger location
- `Memory/kpi-ledger.md` / `Clients/{slug}/goals.md` — KPI ledger
