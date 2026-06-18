---
name: customer-onboarding
description: Builds a dated onboarding plan and checklist that gets a new customer or client to first value fast and sets the first success metric as a ledger target — triggered by "onboard this customer", "create an onboarding plan", "new client onboarding", "kickoff plan", or "get them to first value"
---

# Customer Onboarding

Turn a closed deal into a dated onboarding plan and checklist that drives a new customer or client to their first-value moment fast, with an owner and a success metric on every milestone.

## When to use
- A deal just closed and a new customer or client needs a structured path from kickoff to first value.
- A client engagement is starting and you want a repeatable kickoff plan instead of an ad-hoc email.
- An existing onboarding is stalling and you want to re-baseline milestones, owners, and the first-value moment.
- Do NOT use this to send the welcome message or kick off anything autonomously — this skill drafts the plan; a human runs it.

## Inputs
- What was purchased: `Company/offers.md` (the bought offer, deliverables, scope, promised outcome) — Solo/Team; or the active `Clients/{slug}/context/offers.md` if present (Agency).
- Who the customer is: `Company/icp.md` (Solo/Team) plus any account/deal record (`Pipeline/accounts/`, `Pipeline/deals.md`) — or `Clients/{slug}/context/` files (Agency).
- Voice: `Library/styles/brand-voice.md` + `Company/brand.md` (Solo/Team) OR `Clients/{slug}/context/brand.md` (Agency) — for any customer-facing message draft.
- The new customer/client name and a kebab-case slug; the engagement start date (defaults to today).
- Optional: the contracted outcome or SLA, named contacts and roles on both sides, and any existing kickoff SOP in `Operations/sops/`.

## Process
1. **Determine profile and subject.** Read `_system/config.md` to confirm Solo/Team vs Agency. For Agency, confirm the ACTIVE client slug; read and write ONLY inside that client's `Clients/{slug}/` workspace. Pick or confirm the customer slug (kebab-case) and the start date (ISO).
2. **Load what was bought.** Read `Company/offers.md` (or the client offers file) to capture the exact deliverables, scope, and the outcome the customer was promised. This anchors what "first value" means for them.
3. **Load who they are.** Read `Company/icp.md` and any account/deal record to understand their context, likely goals, and the friction that usually blocks this segment from reaching value. Solo/Team: pull from `Pipeline/accounts/` and `Pipeline/deals.md`. Agency: pull only from the active `Clients/{slug}/` workspace.
4. **Load voice.** Solo/Team: read `Library/styles/brand-voice.md` + `Company/brand.md`. Agency: read `Clients/{slug}/context/brand.md`. Any customer-facing copy is written in that voice.
5. **Define the first-value moment.** Name the single concrete moment the customer first experiences the promised outcome (the "aha" / first measurable result). State it in one line and make it the spine of the plan — every milestone should move toward it.
6. **Lay out milestones.** Break the path from kickoff to first value (and to the first renewal/expansion signal) into ordered milestones. For EACH milestone define: the action, the **owner** (a named person/role on your side or theirs), the target date (relative to start, ISO), and a **success metric** that proves the milestone is done. Mark the milestone that delivers the first-value moment explicitly.
7. **Build the checklist.** Convert the milestones into a runnable, checkbox checklist a human can work top-to-bottom. Each item is one concrete action with its owner and due date. Flag any item that depends on the customer (data, access, sign-off) so blockers surface early.
8. **Draft customer-facing copy as DRAFT-ONLY.** If a welcome/kickoff message or agenda is needed, write it in the loaded voice with `status:draft` and a clear `> SEND BY A HUMAN` marker. Never send, email, or schedule it.
9. **Set the success metric as a ledger target row.** Choose the headline success metric for the onboarding (the first-value metric) and append ONE target row to the KPI source: baseline = current/known starting value (or `—` if not yet known), target = the first-value threshold, source = this plan's path, confidence in {confirmed, reported, inferred, stale}. Append only; never edit prior rows.
10. **Write the plan.** Save the SOP-style onboarding plan to its canonical home (see Outputs) with full universal frontmatter and `status:draft`. Cite any external fact and never invent a metric.
11. **Hand off.** Tell the user where the plan lives, the first-value moment and its target date, the success metric now tracked in the ledger, any customer-dependent blockers, and that all customer-facing messages are drafts awaiting a human to send.

## Outputs
- **Solo/Team:** `Operations/sops/onboarding-{slug}.md` — the dated onboarding plan + checklist, `status:draft`, full frontmatter, `generated:true`. Body structure:
  - `# Onboarding — {Customer name}`
  - `**Start date:**` ISO · `**First-value moment:**` one line · `**Target date for first value:**` ISO
  - `## Milestones` — a table: `| milestone | owner | target date | success metric | first-value? |`
  - `## Checklist` — ordered checkboxes, each with owner + due date; customer-dependent items flagged.
  - `## Customer-facing drafts` — any welcome/kickoff copy at `status:draft`, voice-matched, marked `> SEND BY A HUMAN`.
- **Agency:** the same plan written inside the active client workspace as `Clients/{slug}/onboarding.md` (or `Clients/{slug}/operations/onboarding.md` if that structure exists) — `confidential:true`, firewall-safe (no other client named), `generated:true`.
- **Ledger target row appended** (APPEND-ONLY, exact columns) to:
  - Solo/Team → `Memory/kpi-ledger.md`
  - Agency → `Clients/{slug}/goals.md`
  - Example: `| {ISO date} | onboarding-first-value:{slug} | — | not-started | {first-value threshold} | {path to onboarding plan} | inferred | First-value target set at onboarding kickoff |`

## Guardrails
- DRAFT-ONLY: the plan and any customer-facing message carry `status:draft`. Never send, email, post, schedule, or contact the customer autonomously — a human runs the onboarding and sends every message.
- VOICE: load brand voice before writing any customer-facing copy; Solo/Team uses the business's voice, Agency uses the active CLIENT's voice.
- PROVENANCE: cite sources for any external fact; never invent a metric, date, or contact. The success metric and baseline must be real or marked `—` with `inferred`/`stale` confidence.
- LEDGER INTEGRITY: append exactly one target row; never edit, reorder, or delete prior rows. Confidence stays in {confirmed, reported, inferred, stale}.
- FIREWALL (Agency): read and write only inside the active `Clients/{slug}/` workspace; never read a sibling client; never name another client; outputs are `confidential:true`.
- Every milestone must have an owner, a target date, and a success metric — no orphan steps. The first-value moment is named explicitly and is the spine of the plan.
- Route outputs to canonical homes; kebab-case slugs; ISO dates.

## References
- `_system/config.md` for profile (Solo/Team vs Agency) and the escalation/approval contact.
- `Company/offers.md` (what was bought) and `Company/icp.md` (who the customer is).
- `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) for the append-only target row.
- `Operations/sops/` for any existing kickoff SOP to reuse.
