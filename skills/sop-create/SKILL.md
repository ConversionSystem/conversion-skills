---
name: sop-create
description: Turn a described or observed process into a reusable runnable SOP saved under Operations/sops/ when you say create an SOP, document this process, write a standard operating procedure, or turn this workflow into an SOP
---

# SOP Create

Capture a process once and turn it into a clear, runnable SOP that someone new can follow without you in the room.

## When to use
- You just did something repeatable (onboarding a client, publishing a post, sending a report) and want it written down once.
- A teammate keeps asking how to do the same task and you want a single canonical answer.
- You are observing or describing a process out loud and want it captured as a procedure, not buried in chat.
- You want to surface which steps are ripe for automation before you scale the process.

## Inputs
- A described or observed process: paste a transcript, a chat log, a recording summary, or just talk through the steps.
- Optional source material: an existing checklist, email thread, or a `Daily/YYYY-MM-DD.md` entry where the process happened.
- The owner of the process (a person, or a `Team/{person}/` if Team or Agency).
- The trigger that should start this SOP (an event, a schedule, or a request).
- The folder this SOP belongs to (which department or workflow it serves).

## Process
1. Gather the raw process. If a transcript, chat log, or file path is provided, read it. Otherwise interview the user: ask for the trigger, the step-by-step actions in order, the tools or files touched, the decision points, and the final output plus where it gets filed. Stop and ask when a step is vague rather than guessing.
2. Pick a slug. Derive a short kebab-case name from the process (for example `client-kickoff`, `weekly-report-send`, `blog-post-publish`). Confirm it does not collide with an existing file in `Operations/sops/`.
3. Normalize the steps. Rewrite the raw process into discrete, ordered, imperative steps. Each step is one concrete action. Name exact file paths (canonical homes like `Pipeline/deals.md`, `Clients/{slug}/`, `Content/{slug}-{date}/final/`) and exact tools or connectors. Remove ambiguity; a new hire should be able to follow it cold.
4. Mark automation candidates. For each step, judge whether it is a good fit for an Operator routine (repetitive, rule-based, runs on a schedule) or a connector (touches an external system). Flag those steps inline with `automation: operator` or `automation: connector` and a one-line reason. Do not build the automation here; just flag it.
5. Identify the output and its filed home. State exactly what the SOP produces and the canonical path it is written to. If the SOP produces a metric, note that it should be logged to `Memory/kpi-ledger.md` via the ledger's append-only flow.
6. Write the SOP file to `Operations/sops/{slug}.md` using the template in Outputs. Apply universal frontmatter. Set `generated: false` (a human owns and maintains this SOP).
7. Cross-link it. Add a one-line link to the new SOP from the most relevant folder router (the owning department's `CLAUDE.md` or `README.md`, or `Operations/CLAUDE.md`). If no router exists, note the gap in `Inbox/` rather than guessing.
8. Review for runnability. Re-read the SOP as if you were new. Confirm every step has an actor, an action, and a destination. Fix gaps or escalate open questions to the contact in `_system/config.md`.

## Outputs
- `Operations/sops/{slug}.md` — the SOP, with frontmatter and this body structure:
  - `# {SOP display name}`
  - `**Trigger:**` one line — the event, schedule, or request that starts it.
  - `**Owner:**` the responsible person or `Team/{person}/`.
  - `## Inputs` — files, data, and tools needed before starting.
  - `## Steps` — numbered, imperative, each with exact paths and tools; automation candidates flagged inline.
  - `## Output` — what it produces and the exact canonical path it is filed to.
  - Frontmatter keys: `type: sop` · `status` · `owner` · `date` · `reviewed` · `tags` (>=2) · `confidential` · `source` · `generated: false`.
- A one-line cross-link added to the owning folder's `CLAUDE.md` or `README.md` pointing at the new SOP.
- If the SOP emits a metric: a note in its `## Output` that the metric is appended to `Memory/kpi-ledger.md` (append-only; never edit prior rows).
- If no suitable router exists for the cross-link: a short note dropped in `Inbox/` flagging the missing link.

## Guardrails
- Never autonomously execute the process you are documenting — this skill writes the SOP, it does not run it.
- Steps that send, publish, delete, contact clients, change pricing, or edit permissions must be written with a human-approval gate; outbound artifacts are drafted at `status: draft` and escalated to the contact in `_system/config.md`.
- Agency firewall: when documenting a client process, never read sibling `Clients/{slug}/` folders; keep the SOP inside the owning client's scope or in `Operations/sops/` with no cross-client detail.
- Route facts to canonical homes; do not duplicate company or client facts into the SOP — link to them.
- Use kebab-case slugs and ISO dates. Keep the SOP under the 150-line context budget.
- Flag automation candidates only; do not create Operator routines or connectors from this skill.

## References
- `Library/templates/` for an existing SOP template, if present.
- `_system/config.md` for the escalation contact and approval gates.
- `Memory/kpi-ledger.md` for the append-only metric logging flow.
