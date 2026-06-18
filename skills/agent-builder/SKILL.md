---
name: agent-builder
description: Design an AI agent from a job description with its role, reads, writes, budget, escalation contact, and guardrails, written as an agent brief plus a config skeleton when you say build an agent or design a sub-agent
---

# Agent Builder

Turn a job into a runnable agent: what it does, what it touches, what it costs, who it answers to, and where it stops.

## When to use
- You keep doing the same task by hand and want an agent to own it.
- You want a sub-agent for one job (lead research, daily digest, draft replies) with a tight scope.
- You need a written brief and a config file before you wire any tool to a folder.
- A reviewer wants to see an agent's reads, writes, and limits on one page before it runs.

## Inputs
- The job in one line: what the agent is for and what "done" looks like.
- Trigger: on command, on a schedule, or on a file landing in `Inbox/`.
- Read scope: which vault paths the agent may read.
- Write scope: which vault paths the agent may write, and whether output is draft or live.
- Budget: a per-run cost or token ceiling, plus a daily cap.
- Escalation contact: a name and channel for when the agent is unsure or blocked.
- Optional connectors the agent needs, by name only (see `_system/connectors.md`).

## Process
1. Read `Company/profile.md`, `Company/strategy.md`, and `_system/rules.md` to ground the agent in the business and the house rules.
2. Read `Library/styles/brand-voice.md` so any text the agent drafts inherits the voice.
3. Name the agent from its job. Slugify it (lowercase, hyphens) as `{agent-slug}`.
4. Write the role: one sentence on purpose, then the 3 to 6 steps the agent runs each time.
5. Set the trigger (command, schedule, or inbox) and the success test (what a finished run produces).
6. List read paths and write paths explicitly. Default every write to draft. Mark any path that needs human approval before it goes out.
7. Set the budget: per-run ceiling, daily cap, and the action on breach (stop and escalate).
8. Name the escalation contact and the channel, and list the conditions that trigger escalation (low confidence, missing data, budget breach, anything outbound).
9. Write guardrails: firewall scope if it touches `Clients/`, provenance rule (cite sources, never invent metrics), and the draft-only rule on anything published or sent.
10. Write the agent brief to `Library/agents/{agent-slug}.md` for a reusable agent, or to `Projects/{project-slug}/agents/{agent-slug}.md` for a project-scoped one.
11. Write the config skeleton to the same folder as `{agent-slug}.config.md` with the fields filled from the brief.
12. Append one row to `Memory/kpi-ledger.md` recording the agent created and its budget cap, so spend has a baseline to chart against.

## Outputs
- `Library/agents/{agent-slug}.md` or `Projects/{project-slug}/agents/{agent-slug}.md`: the agent brief (role, trigger, reads, writes, budget, escalation, guardrails).
- `Library/agents/{agent-slug}.config.md` or the project equivalent: the config skeleton with these fields:
  - `name`, `role`, `trigger`, `reads` (list), `writes` (list, each marked draft or live), `budget` (per-run, daily, on-breach), `escalation` (contact, channel, conditions), `connectors` (names only), `guardrails` (list).
- One appended row in `Memory/kpi-ledger.md`: `| date | metric | baseline | current | target | source | confidence | note |` with metric set to the agent's budget cap and note naming the agent.

## Guardrails
- Draft only. Every write defaults to draft, and anything outbound or published stays a draft until a human approves it.
- Credentials never enter the vault. Connectors are named in the config and configured in `_system/connectors.md` only.
- Firewall. If the agent reads or writes under `Clients/`, it is scoped to the active client and no other.
- Provenance. The agent cites its sources and never invents a metric. Numbers come from files or named connectors.
- Budget is a hard stop. On breach the agent halts and escalates rather than continuing.
- No new ledger edits. The ledger row is appended, never an edit to a prior row.

## References
- `_system/rules.md`
- `_system/connectors.md`
- `Library/styles/brand-voice.md`
- `Memory/kpi-ledger.md`
