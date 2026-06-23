---
name: client
description: Manage firewalled per-client agency workspaces under Clients/{slug}/ · onboard a new client, pull a strategist brief, log a client meeting, draft a deliverable, build a client report, run a health check, or archive and offboard. Triggers on phrases like onboard client, new client, client brief, log client meeting, draft for client, client report, client health, offboard client, archive client.
---

# Conversion Client OS
Run firewalled per-client workspaces under Clients/{slug}/ for agency delivery · onboarding, briefing, meeting logs, deliverables, reporting, health, and clean offboarding.

## When to use
- "Onboard {name} as a client" / "set up a new client" -> NEW (flow 1).
- "Give me the brief on {client}" / "what's the state of {client}" -> BRIEF (flow 2).
- "Log the {client} call" / "capture this client meeting" -> LOG (flow 3).
- "Draft the {deliverable} for {client}" -> DRAFT (flow 4).
- "Build the weekly/monthly report for {client}" -> REPORT (flow 5).
- "How healthy is {client}" / "any at-risk accounts" -> HEALTH (flow 6).
- "Offboard {client}" / "archive {client}" -> ARCHIVE (flow 7).
- Skip this skill for non-client work (Solo/Team Pipeline, Projects, Content) · those route elsewhere.

## Inputs
- The active client (name or slug). If absent or ambiguous across existing slugs, ask once; never guess.
- Per-flow payload: interview answers (NEW), raw meeting notes/transcript (LOG), deliverable type + spec (DRAFT), period (REPORT).
- Read context: the active `Clients/{slug}/` tree only, plus shared `Library/playbooks/`, `Library/templates/`, `Library/prompts/`, and `_system/config.md` (escalation contact, operator budgets).
- Profile gate: Agency profile only (per `_system/config.md`). If profile != Agency, stop and explain.

## Process
Resolve the active client first. Match the requested name to exactly one existing `Clients/{slug}/`; on no match propose NEW; on multiple matches or ambiguity, ask once, else file the request to `Inbox/` and stop. Once resolved, treat that slug as the ONLY client folder you may open this turn.

1. NEW · onboard a client
   1. Derive a kebab-case `{slug}` from the legal/brand name (ISO-safe, lowercase). If `Clients/{slug}/` or `Clients/_archive/{slug}/` already exists, refuse as a duplicate and offer the existing folder.
   2. Run a short interview (ask only for gaps): who they are; mandate + the single success metric; their ICP; key people (names, roles, contact channel); commercials (scope, term, cadence); brand voice/constraints.
   3. Scaffold the workspace, every file `confidential:true` with universal frontmatter:
      - `Clients/{slug}/CLAUDE.md` · firewall router: states "read/write only this folder; never open a sibling Clients/*", canonical map of the subtree, escalation contact.
      - `Clients/{slug}/profile.md` · who/mandate/commercials/voice.
      - `Clients/{slug}/goals.md` · per-client KPI ledger (append-only, exact columns below) seeded with the success metric as the first target row.
      - `Clients/{slug}/context/` · `brand.md`, `stack.md`, `people.md`.
      - `Clients/{slug}/meetings/`, `work/`, `reports/`, `inbox/` (created as needed) and `Clients/{slug}/decisions.md`.
   4. Emit a one-screen report card: what was created, the mandate/metric, and the top 3 open questions.
2. BRIEF · strategist context
   1. Read `profile.md`, the last 5–8 rows of `goals.md`, the 2–3 most recent `meetings/`, open actions, and `decisions.md`.
   2. Output one screen: mandate + success metric, latest numbers vs target (with confidence), recent decisions, what we owe vs what we're waiting on, and the next best action. No files written.
3. LOG · capture a meeting
   1. Write `Clients/{slug}/meetings/YYYY-MM-DD-{kind}.md` (kind ∈ {call, kickoff, review, qbr, async}) with attendees, summary, raw notes.
   2. Extract decisions -> append to `decisions.md` (each with `source` + `confidence`). Extract our actions -> client task list; their commitments -> a "waiting-on" list. Extract any metrics -> append rows to `goals.md`.
   3. Surface follow-ups; any outbound (recap email/DM) is drafted `status:draft`, never sent.
4. DRAFT · a deliverable
   1. Create `Clients/{slug}/work/{deliverable-slug}/drafts/{name}-vN.md`, `status:draft`, `generated:true`, `confidential:true`.
   2. Compose from the active client's context + relevant `Library/playbooks/` and `Library/templates/` only. No facts, names, or assets from any other client.
   3. Note open questions/assumptions inline; leave publishing/sending to a human gate.
5. REPORT · period report
   1. Write `Clients/{slug}/reports/YYYY-Www.md` (weekly) or `YYYY-MM.md` (monthly), `generated:true`.
   2. Lead with numbers pulled from `goals.md` (current vs target, confidence). Then wins, work shipped, decisions, next period's plan.
   3. Flag every goal lacking a fresh ledger row (stale/no data) rather than inventing progress. Client-facing send stays a human gate.
6. HEALTH · risk check
   1. Score risk signals: stale metrics, missed/over-running deadlines, unanswered "waiting-on", flat/negative KPI trend, sentiment from recent `meetings/`, low touch cadence.
   2. Write/refresh `Clients/{slug}/reports/health.md` (`generated:true`) with a RAG status + top risks + recommended interventions.
   3. Regenerate Ops rollups (pipeline/revenue) as `generated:true` aggregates; emit anonymized figures only · never expose one client's data inside another's view.
7. ARCHIVE · offboard
   1. Run an offboarding checklist: outstanding deliverables, final report, access/credential handover, data export.
   2. Produce an ownership/export bundle so the client OS survives the agency: a portable copy of `Clients/{slug}/` plus an `EXPORT.md` explaining the structure and that the files are theirs to keep.
   3. Harvest anonymized lessons -> `Memory/lessons.md`; create a consent-flagged case-study candidate (`generated:true`, `status:draft`, requires client sign-off before any use).
   4. Set every file `status:archived`, move the tree to `Clients/_archive/{slug}/`, and fix inbound links from Ops/Memory to the new path.

## Outputs
- NEW: `Clients/{slug}/CLAUDE.md`, `profile.md`, `goals.md` (seeded target row), `context/{brand,stack,people}.md`, `decisions.md`, empty `meetings/`, `work/`, `reports/`, `inbox/`; plus a report card (chat only).
- BRIEF: no files (one-screen summary in chat).
- LOG: `Clients/{slug}/meetings/YYYY-MM-DD-{kind}.md`; appended rows in `decisions.md` and `goals.md`; draft recap if requested (`status:draft`).
- DRAFT: `Clients/{slug}/work/{deliverable-slug}/drafts/{name}-vN.md` (`status:draft`).
- REPORT: `Clients/{slug}/reports/YYYY-Www.md` or `YYYY-MM.md` (`generated:true`).
- HEALTH: `Clients/{slug}/reports/health.md` and regenerated Ops pipeline/revenue rollups (`generated:true`).
- ARCHIVE: `Clients/_archive/{slug}/` (all `status:archived`), `Clients/_archive/{slug}/EXPORT.md`, appended `Memory/lessons.md`, case-study candidate (`status:draft`).
- Per-client ledger columns (append-only, never edit/reorder/delete prior rows):
  `| date | metric | baseline | current | target | source | confidence | note |` with confidence ∈ {confirmed, reported, inferred, stale}.

## Guardrails
- Firewall (core invariant): read/write ONLY the active `Clients/{slug}/`. NEVER open a sibling `Clients/{other}/`. Every client file `confidential:true`. Ops/Memory cross-client outputs must be anonymized aggregates only.
- Ambiguity: if the client can't be resolved to exactly one slug, ask once; otherwise file to `Inbox/` and stop. Never guess the client.
- Human-approval gates: never send external messages/email/DM, publish a deliverable, contact the client, change pricing/commercials, edit permissions, or delete files autonomously. Outbound is `status:draft` and escalated to the contact in `_system/config.md`.
- Append-only ledger: `goals.md` and `decisions.md` grow by appending; never rewrite history. `source` + `confidence` required on every ledger row and decision.
- Frontmatter: universal keys on every file (`type · status · owner · date · reviewed · tags(>=2) · confidential · source · generated`); `confidential:true` across the client subtree.
- Slugs/homes: kebab-case slug, ISO dates, one concept per file. Refuse duplicate slugs at onboarding.
- Budgets: respect operator read/write/transcript/email/dm/housekeeping caps in `_system/config.md`; stop cleanly when a cap is hit.

## Red flags
- You are about to open a second `Clients/{slug}/` folder in one turn, or you pulled a fact, name, or asset from a client other than the active one.
- You started a flow without resolving the active client to exactly one slug, or you guessed the slug instead of asking once.
- A REPORT or BRIEF states progress against a KPI with no fresh `goals.md` row behind it, or omits the confidence value.
- You appended a decision or metric row without a `source`, or you edited/reordered a prior `goals.md` or `decisions.md` row instead of appending.
- A recap email, DM, or deliverable is heading out without a `status:draft` flag and a human gate, or you are about to change pricing, permissions, or send anything client-facing.
- An Ops or Memory rollup carries a single client's raw figures instead of an anonymized aggregate, or a new client file is missing `confidential:true`.

## Verification
- [ ] Active client resolved to exactly one existing slug (or NEW proposed); on ambiguity, asked once or filed to `Inbox/` and stopped.
- [ ] Only the active `Clients/{slug}/` was read or written this turn; no sibling client folder was opened.
- [ ] Every metric or claim cites its `source`, carries a `confidence` value, and goals with no fresh row are flagged stale, not invented.
- [ ] `goals.md` and `decisions.md` were appended only, with the full column set; no prior row edited, reordered, or deleted.
- [ ] Every file written carries universal frontmatter and `confidential:true`; outbound items are `status:draft`, nothing sent or published.
- [ ] Cross-client Ops/Memory outputs are anonymized aggregates; no single client's raw data appears in another's view.
- [ ] Profile gate checked (Agency only); operator budgets respected and the run stopped cleanly if a cap was hit.
- [ ] On ARCHIVE: export bundle plus `EXPORT.md` produced, inbound links repointed, all files set `status:archived`, case-study candidate left `status:draft` pending sign-off.

## Rationalizations
| Rationalization | Reality |
|---|---|
| "I remember this number from their last review, no need to open `goals.md`." | Numbers come from a cited ledger row or they are stale. Memory is not a source; label it `inferred` and flag it. |
| "Just this once I'll peek at the sibling client to compare results." | The firewall is the whole product. One peek leaks confidential data and breaks the contract. Use anonymized Ops aggregates instead. |
| "Two clients match but they clearly meant this one, I'll proceed." | Clearly to you, not to the file tree. Wrong slug writes to the wrong account. Ask once, then act. |
| "The recap is obvious, I'll just send it to keep things moving." | Sending is a human gate, always. Draft it `status:draft` and escalate to the contact in `_system/config.md`. The cost of one wrong send is the account. |
| "The report reads better with steady progress, I'll smooth the gap." | A goal without a fresh row is stale, not progressing. Inventing a number is the one failure that ends the relationship. Flag it. |

## References
- `_system/config.md` (Agency profile flag, escalation contact, operator budgets), `_system/permissions.md`, `_system/rules.md`.
- `Library/playbooks/`, `Library/templates/`, `Library/prompts/` (shared, non-client assets for DRAFT).
- `Memory/lessons.md` (archive harvest target), root `CLAUDE.md` router (canonical homes for inbound-link fixes).
