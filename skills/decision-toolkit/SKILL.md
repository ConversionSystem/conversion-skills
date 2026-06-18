---
name: decision-toolkit
description: Run a structured decision (frame, options, criteria, trade-offs, recommendation) and record it to Memory/decisions with a confidence, triggered by /decision, "help me decide", "decision toolkit", or "should I".
---
# Decision Toolkit
Work a significant choice through frame, options, criteria, trade-offs, and a recommendation, then write the verdict to the decision log with a confidence score.

## When to use
- A choice has more than one real option and the stakes (time, money, focus, reputation) are high enough to think on paper.
- You want a record of why a call was made, so future-you (or a teammate) can audit the reasoning.
- Trigger phrases: /decision, "help me decide", "decision toolkit", "should I", "weigh these options", "make a call on this".
- Not for: trivial or reversible choices, emergencies, or cases where you only need a fact (use a research skill instead).

## Inputs
- The decision in one sentence (what is actually being chosen).
- The options on the table (2 to 6 named choices, including "do nothing" if it applies).
- What is at stake and the deadline.
- Any constraints, context, or relevant numbers from `Company/` or `Memory/kpi-ledger.md`.
- Optional: a source document (a brief, a transcript, a thread) to pull the above from.

## Process
1. Read `_system/rules` and `Library/styles/brand-voice.md` so the writeup matches house voice. If a client is in scope, read `_system/permissions` and stay inside the active client firewall.
2. Frame the decision in one sentence. State what counts as a win and what the deadline is. If the user gave a document, extract the frame, options, and stakes from it and confirm them back.
3. List the options, 2 to 6 of them, each with a short plain label. Add "do nothing" or "wait" as an explicit option when it is real.
4. Set the criteria that decide this. Pick 3 to 6 (for example: cost, time to result, reversibility, fit with strategy, risk). Weight each one high, medium, or low so the heavy factors are visible.
5. Score each option against each criterion in a markdown table. Use plain marks (strong, ok, weak) or 1 to 5, not invented precision. Cite any number you use and its source; never fabricate a metric (see PROVENANCE).
6. Name the trade-offs. For the leading two options, write what you give up by choosing it and what has to be true for it to work.
7. Run a bias pass. Check the call against: sunk cost, fear of missing out, recency, confirmation, and over-optimism. Note any that apply in one line each.
8. Pre-mortem the front-runner. Assume it failed six months out and write the top 3 reasons, then mark which are inside your control and which are early warning signs to watch.
9. Write the recommendation: the chosen option, the one-paragraph reason, the first action, and a confidence from 0 to 100 percent with a one-line basis for that number.
10. Record the decision to `Memory/decisions/YYYY-MM-DD-{slug}.md` using today's date and a short slug of the frame. Keep it inside `Clients/{slug}/` instead when the decision belongs to an active client.

## Outputs
- `Memory/decisions/YYYY-MM-DD-{slug}.md` with sections: Frame, Options, Criteria and weights, Scoring table, Trade-offs, Bias pass, Pre-mortem, Recommendation, Confidence, First action, Sources. (Client decisions write to `Clients/{slug}/decisions/YYYY-MM-DD-{slug}.md`.)
- If the decision sets or moves a tracked number, append one row to `Memory/kpi-ledger.md` with the exact columns | date | metric | baseline | current | target | source | confidence | note |. Never edit a prior row.
- A short summary in chat: the recommendation, the confidence, and the first action.

## Guardrails
- DRAFT-ONLY: this skill records a decision, it does not act on it. Anything outbound or published that follows stays a draft until a human approves it.
- PROVENANCE: cite every source and number. If a figure is unknown, mark it unknown rather than guessing.
- The decision log entry is a record, not a rewrite. Append new decisions as new files; do not overwrite or quietly edit a past entry. To change a call, write a new dated entry that supersedes the old one and link back.
- FIREWALL: for client decisions, read and write only the active client folder.
- VOICE: pull tone from `Library/styles/brand-voice.md`. Numbers over adjectives, verbs over nouns.

## References
- `_system/rules`, `_system/permissions`
- `Library/styles/brand-voice.md`
- `Company/strategy`, `Company/offers`, `Memory/kpi-ledger.md`
