---
name: doubt-check
description: Adversarial check on a hard-to-reverse decision before you commit, extract and challenge every assumption then STOP or GO, triggers doubt check, stress test this decision, should we really do this, sanity check before launch
---

# Doubt Check

## When to use
Before a high-stakes, hard-to-reverse call: a price change, a discount, a launch, a large spend, dropping a feature. Use it when the cost of being wrong is high and you cannot quietly walk it back. Skip it for small, reversible bets. This skill recommends; a human makes the decision.

## Inputs
- The decision, stated plainly (what you intend to do, by when).
- The outcome the decision assumes (the payoff that makes it worth doing).
- The real numbers: relevant rows from `Memory/kpi-ledger.md` and any baseline in `Memory/`.
- `Company/strategy.md`, `Company/offers.md`, and `Company/icp.md` for context on what the decision touches.
- Past calls in `Memory/decisions/` and `Memory/lessons.md` for prior bets that went the same way.

## Process
1. CLAIM. Write the decision in one sentence and the outcome it assumes in one sentence. Example: "Raise the plan price 20 percent" assumes "revenue rises because fewer than 1 in 6 buyers leave." State the assumed payoff as a number, not a feeling.
2. EXTRACT. List every assumption the claim rests on, the ones that must all hold for the payoff to land. Cover demand (will buyers stay), supply (can you deliver), timing (is now right), and second order effects (what breaks downstream). Number them. A claim with zero listed assumptions is not done; dig until you have at least four.
3. DOUBT. For each assumption, write the one question that would break it if the answer goes the wrong way, and name the evidence that would settle the question. Mark each assumption shakiest, shaky, or solid based on how thin the evidence is.
4. JUDGE. Take the two or three shakiest assumptions and call the judge agent (`_system/agents/judge.md`) to refute each one: have it argue the assumption is false and state what it would take to be sure. Record what it found. If the judge breaks an assumption the whole claim needs, that is your answer.
5. RECONCILE. Pull the real numbers. For every assumption, write what the ledger and the baseline actually say versus what the claim hoped. Flag each gap. Cite the source row; never fill a gap with a guessed number, mark it unknown and treat unknown as a risk.
6. VERDICT. Weigh it. STOP if a load-bearing assumption is shaky or unknown and the decision is hard to reverse. GO if the load-bearing assumptions are solid and the downside of being wrong is survivable. Set a confidence in {confirmed, reported, inferred, stale} and write the one number or test that would flip the verdict.
7. RECORD. Write the decision, the assumptions, the doubts, the reconciliation, and the verdict to `Memory/decisions/YYYY-MM-DD-{slug}.md`. Append a row to `Memory/kpi-ledger.md` only if the check produced a measurable baseline or target.

## Outputs
- `Memory/decisions/YYYY-MM-DD-{slug}.md` containing: the claim, the numbered assumptions, the doubts and their settling evidence, the judge findings, the reconciliation against the ledger, and a STOP or GO with a confidence and the flip condition.
- An optional appended row in `Memory/kpi-ledger.md` when a baseline or target was set: `| date | metric | baseline | current | target | source | confidence | note |`.
- A short verdict summary in the reply: STOP or GO, the confidence, the shakiest assumption, and the one thing that would change the call.

## Guardrails
- Draft only. This skill recommends; it never executes the decision, never sends, publishes, posts, or contacts anyone.
- Never invent a metric. An assumption with no evidence is marked unknown and counts as a risk, not a pass.
- Cite every number to its ledger row or source file.
- Agency firewall: if the decision belongs to a client, read only the active client folder, never a sibling.
- A confident GO does not override a human. The decision file is a recommendation; a person signs off.
- Bias toward STOP when the decision is hard to reverse and the evidence is thin. Reversible bets do not need this skill.

## References
- `Memory/kpi-ledger.md` for the real numbers, append-only.
- `Memory/decisions/` for prior calls and how they aged.
- `Memory/lessons.md` for bets that taught something.
- `_system/agents/judge.md` for the refutation pass.
- `Company/strategy.md`, `Company/offers.md`, `Company/icp.md` for context.
