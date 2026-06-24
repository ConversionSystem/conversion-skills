---
name: decision-map
description: Build and drive a stateful map for a complex engagement or strategic question that needs more than one work session, decompose it into typed investigation tickets with dependencies and work them one at a time to a decision, triggers decision map, map this decision, multi-session plan, investigation plan, sequence these open questions
---

# Decision Map

## When to use
For a complex engagement or strategic question that will not close in one sitting and has several open investigations running at once: a new client engagement with unknowns, a market-entry call, a pricing overhaul, a build-or-buy that needs evidence gathered over days. Use it when the work spans more than one session and the path to the answer is itself unclear. It complements three single-pass skills and fills the gap between them. decision-toolkit resolves ONE decision in one pass. grill sharpens ONE plan. doubt-check renders a STOP or GO verdict on ONE decision. decision-map is the multi-session, many-open-questions case that feeds work into those. It recommends and tracks; a human makes the final call.

## Inputs
- The overarching question or goal in one or two lines, and the decision it leads to.
- The open investigations already on your mind, however rough, to seed the first tickets.
- `Company/strategy.md` for the bet this question must serve.
- `Company/offers.md` and `Company/icp.md` for the offer and audience the question touches.
- `Memory/kpi-ledger.md` for the real numbers any ticket will be judged against.
- `Memory/lessons.md` for prior maps or bets of this shape that already paid off or failed.
- The existing `decision-map.md` if one is already open for this engagement, so you continue it instead of starting over.

## Process
1. FRAME. Write the overarching question or goal in one or two lines and the decision it leads to in one line. State the decision as a real commitment ("sign this engagement at this scope", "raise the floor price"), not a vague aim. Read it back and let the human correct before you decompose.
2. DECOMPOSE. Break the question into numbered investigation tickets. Type each one: Research (find something out), Build (make a small thing to learn from it), or Discuss (a call a human must make). Size each ticket to a single work session. For each, write the one thing that would resolve it, the specific finding, artifact, or decision that closes the ticket. A ticket with no clear resolver is too big; split it.
3. SEQUENCE. Map blocked-by dependencies between tickets so the order is explicit. Ticket 4 blocked-by 2 means 2 must resolve first. Mark each ticket open, blocked, or resolved. A ticket with no unresolved blockers is ready. State the critical path, the chain of blocked-by links that gates the final decision.
4. DRIVE. Work one ticket at a time. Pick the next ready ticket, the highest-leverage one whose blockers are all resolved. Work it (run the research, build the small thing, or put the call to the human). Record the outcome in one or two lines on the ticket, then mark it resolved and unblock its dependents. Never open a second ticket while the chosen one is still in flight.
5. UPDATE. Keep the map stateful. Each session, update ticket states and append outcomes; never rewrite or erase resolved tickets or their findings, the history is the record of how the answer was reached. Link assets and prior files by path (`Projects/{slug}/research/...`, `Memory/decisions/...`), never paste their bodies into the map. If new questions surface, add them as new numbered tickets with their dependencies, do not silently fold them into old ones.
6. CONVERGE. When every load-bearing ticket is resolved, write the resulting decision in one or two lines with the findings that back it, each cited to the ticket and the linked asset that produced it. If the decision is a real commitment, record it to `Memory/decisions/YYYY-MM-DD-{slug}.md` and hand off to doubt-check for the adversarial STOP or GO pass before anyone acts on it.

## Outputs
- A stateful `decision-map.md` at its home path containing: the framed question and the decision it leads to, the numbered tickets each tagged Research/Build/Discuss with its resolver and state (open/blocked/resolved), the blocked-by dependencies and critical path, and the recorded outcome on every resolved ticket with linked asset paths.
- On convergence, the resulting decision written into the map with its backing findings, and for a real commitment a `Memory/decisions/YYYY-MM-DD-{slug}.md` record, status:draft, handed to doubt-check.
- A short status line in the reply each session: which ticket was worked, its outcome, what it unblocked, and the next ready ticket.

## Guardrails
- Stateful, not disposable. Update the map, never erase a resolved ticket or its finding. The history of how the answer was reached is part of the output.
- One ticket at a time. Pick the next ready ticket, work it to an outcome, then move on. Never run several tickets in parallel or skip a ticket whose blockers are still open.
- Link, never inline. Reference assets and prior files by path; do not paste their bodies into the map.
- Draft only. decision-map plans, tracks, and recommends. It never sends, publishes, posts, launches, spends, or contacts anyone.
- Agency firewall. If the engagement belongs to one client, read and write only that `Clients/{slug}/` folder, never a sibling client.
- The human makes the final call. The map drives the investigation and proposes the decision; a person signs off, and doubt-check runs the adversarial pass before any commitment.
- Stay in lane. decision-map is the multi-session driver. It does not resolve a single decision in one pass (decision-toolkit), sharpen one plan (grill), or render the final commit verdict (doubt-check); it routes work to them.

## References
- `Projects/{slug}/decision-map.md` for an engagement, or `Memory/decisions/` for an internal strategic map (the two homes).
- `Memory/decisions/` for prior calls and the final committed records.
- `Memory/kpi-ledger.md` for the real numbers any ticket is judged against, append-only.
- `Memory/lessons.md` for maps and bets of this shape that already taught something.
- `Company/strategy.md`, `Company/offers.md`, `Company/icp.md` for the bet, offer, and audience the question touches.
- doubt-check for the adversarial STOP or GO pass on the resulting decision; decision-toolkit, grill for single-pass work a ticket may route to.
