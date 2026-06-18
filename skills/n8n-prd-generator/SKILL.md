---
name: n8n-prd-generator
description: Write a product requirements doc for one n8n automation covering the job, trigger, steps, data, guardrails, and success metric, saved as a draft brief when you say write an n8n PRD, spec an automation, plan an n8n workflow, or document this automation before I build it
---

# n8n PRD

Turn a rough automation idea into a build-ready product requirements doc for a single n8n workflow, written as a draft a human reviews before anyone wires up a node.

## When to use
- You want to automate a repetitive task and need the spec before touching n8n.
- A process in `Operations/processes/` keeps eating manual hours and should run on its own.
- You have a trigger in mind (a form, a schedule, a webhook, a new row) but the steps, data shape, and failure handling are still fuzzy.
- You want one clear doc to hand a builder, a contractor, or your future self so the automation gets built once, correctly.
- You are deciding whether an automation is worth building and need its success metric defined up front.

## Inputs
- The job, in one line: what the automation does and why it matters.
- The trigger: what kicks it off (schedule/cron, inbound webhook, form submit, new record, email received, manual run).
- Source and destination systems (e.g. a CRM, a sheet, an email tool, a Slack channel). Treat these as OPTIONAL connectors, registered in `_system/connectors.md`, never assumed live.
- Any sample data: a record shape, a payload, the fields that move through the flow.
- Context files: `Company/profile.md` and `Company/stack.md` for the existing tool set; `Operations/processes/` for the manual version being replaced.
- Optional: a slug for the project. If unspecified, derive a kebab-case slug from the job (e.g. `lead-routing-automation`).
- Agency: the ACTIVE client only. Read `Clients/{slug}/context/` and write client systems and data under the firewall; never mix clients.

## Process
1. Confirm scope: restate the job in one sentence and name the single workflow this PRD covers. One PRD equals one automation. If the idea spans several, split it and write this PRD for the first.
2. Resolve the slug and create `Projects/{slug}/` if it does not exist. The PRD is written to `Projects/{slug}/brief.md`.
3. Read context: `Company/stack.md` for tools already in use, `Company/profile.md` for the business, and the relevant `Operations/processes/` file if this automation replaces a manual process. Agency: read the active client's context instead.
4. Define the trigger precisely: type (cron, webhook, form, polling, manual), its exact firing condition (cron expression, event name, poll interval), and the expected volume per day or per run.
5. Map the steps as a numbered node sequence: each step names the node's purpose, its input, its output, and any branch or condition. Mark every external system as a connector reference, not a hard dependency.
6. Specify the data: the input schema (fields and types), each transformation, and the output schema. Use a sample payload to make field names concrete. Cite where the sample came from; never invent field values you have not seen.
7. Write the guardrails: rate limits, retry and timeout behavior, what happens on failure (alert where, fall back to what), idempotency so a re-run does not double-fire, and a DRAFT-ONLY or human-approval gate on any step that sends, publishes, or charges anything outbound.
8. Define one success metric: the number that proves the automation works (e.g. runs completed without error, hours saved per week, records processed per day, lead response time in minutes). State its baseline, its target, and exactly how it is measured.
9. Add a build checklist: credentials needed (named, stored outside the vault), the connectors to register in `_system/connectors.md`, a test plan with one happy-path and one failure-path case, and a rollback step.
10. Write `Projects/{slug}/brief.md` with the sections from Outputs. Flag anything assumed with a `[CHECK]` tag for the reviewer.

## Outputs
- `Projects/{slug}/brief.md`, an n8n PRD with these sections, in order:
  - Job: one line, plus why it matters.
  - Trigger: type, firing condition, expected volume.
  - Steps: numbered node sequence, each with input, output, and branches.
  - Data: input schema, transformations, output schema, sample payload.
  - Guardrails: rate limits, retries, failure handling, idempotency, the outbound human-approval gate.
  - Success metric: the one number, with baseline, target, and measurement method.
  - Build checklist: credentials, connectors to register, test plan, rollback.
  - Open questions: each `[CHECK]` item the reviewer must resolve before build.
- If the vault tracks this metric, append one row to `Memory/kpi-ledger.md` (Solo/Team) or `Clients/{slug}/goals.md` (Agency) using the exact columns `| date | metric | baseline | current | target | source | confidence | note |`. Append only; never edit a prior row. Skip this if the metric is not yet measured, and note it as a `[CHECK]`.

## Guardrails
- DRAFT-ONLY: the PRD is a draft for human review; no automation gets built or run from this skill.
- Any step that sends, publishes, charges, or otherwise acts outbound must carry a human-approval gate in the spec.
- PROVENANCE: cite where sample data and metrics came from. Never invent field values or numbers.
- Connectors are OPTIONAL. External systems are referenced via `_system/connectors.md`; credentials are named in the build checklist but stored outside the vault, never written into it.
- FIREWALL (agency): the active client only. Never reference another client's systems or data in this PRD.
- Ledger rows are append-only and use the exact eight columns.

## References
- `_system/connectors.md` for registered external systems.
- `Company/stack.md` and `Operations/processes/` for the current tools and the manual process being replaced.
