---
name: grill
description: Relentless one-question-at-a-time interrogation of a new plan before any spend, walks every branch to sharpen it then returns GO REWORK or STOP, triggers grill this plan, pressure test before we build, poke holes in this, sharpen this plan, interrogate this idea
---

# Grill

## When to use
Before you build or spend on a NEW plan: a campaign, a launch, an offer, a hire, a channel bet. Use it when the plan is still soft and you want every load-bearing branch made concrete before money moves. The defining rule is one question at a time, the highest-leverage open one, each carrying a recommended answer you can accept or override. This is not process-interviewer, which documents a process that already runs into an SOP. It is not doubt-check, which renders a final adversarial STOP or GO on a single decision after the plan is set. Grill is the pre-build sharpening loop between them. It recommends; the human answers and decides.

## Inputs
- The plan in one or two lines (what you intend to do, and roughly when).
- The outcome the plan assumes (the result that makes it worth doing), if the human has one. If not, the first branch grills for it.
- `Company/strategy.md` for the bet the plan must serve, and whether it fits.
- `Company/offers.md` for the real offer, price, and promise the plan rests on.
- `Company/icp.md` for who the plan must reach and what they already believe.
- `Memory/kpi-ledger.md` for the real baselines the success metric will be judged against.
- `Memory/lessons.md` for plans of this shape that already worked or failed here.

## Process
1. RESTATE. Read strategy, offers, icp, the ledger, and lessons. Write the plan in one line and the outcome it assumes in one line, each as a number where one exists, not a feeling. Read both back and let the human correct before you grill. Never invent the outcome; if none was given, the first question asks for it.
2. MAP. Lay out the decision tree: the branches that must each be answered for the plan to be real. The default branches are audience, offer, channel, budget, timing, success metric, owner, and fallback. Add any branch this specific plan needs and drop any that genuinely does not apply (mark it N/A with a reason, never silently). List each branch as resolved or open against what the context files already settle.
3. GRILL. Ask ONE question at a time, the highest-leverage unresolved branch first, the one where a wrong answer wastes the most spend. Each question carries your recommended answer and the one-line why, drawn from the context files and the ledger, so the human can accept or correct in a breath. Then STOP and wait for the human. Never batch questions. Never answer for the human. Never move to the next branch until this one has a real answer.
4. DRILL. If the answer is vague ("everyone", "soon", "more leads", "it'll pay off"), do not accept it. Ask the next sharper question on the same branch, again with a recommended answer, until the branch is concrete and testable. A branch is concrete when it names a specific audience, a number, a date, a named owner, or a measurable target, not an adjective.
5. TRACK. After each answer, mark the branch resolved and restate the running list of resolved versus open in one line so the human always sees what is left. Stop grilling when every load-bearing branch is concrete, or the human calls it, whichever comes first. A branch the human refuses to settle is recorded as an open assumption, not quietly closed.
6. SYNTHESIZE. Write the sharpened plan as it now stands, the assumptions it now rests on (each tagged solid, thin, or unproven), and the top two or three risks. Close with a verdict: GO if every load-bearing branch is concrete and the assumptions are solid, REWORK if a load-bearing branch is still thin and name it, STOP if the plan contradicts strategy or rests on an unproven assumption it cannot survive. State the one number that would prove the plan, the metric and the threshold that would say it worked.
7. HAND OFF. Optionally record the sharpened plan, its open assumptions, and the verdict to `Memory/decisions/YYYY-MM-DD-{slug}.md`. Append a row to `Memory/kpi-ledger.md` only if grilling set a real baseline or a target for the success metric. Then offer the final adversarial pass: hand the sharpened plan to doubt-check for the STOP or GO on whether to actually commit the spend.

## Outputs
- A live interrogation in the reply: one question at a time, each with a recommended answer, and after every answer the running resolved-versus-open branch list.
- A sharpened plan summary: the restated plan and outcome, every branch and its concrete answer, the assumptions tagged solid/thin/unproven, the top risks, and a GO/REWORK/STOP with the one number that would prove it.
- Optional `Memory/decisions/YYYY-MM-DD-{slug}.md` with the plan, branches, assumptions, open items, and verdict, status:draft.
- Optional appended row in `Memory/kpi-ledger.md` when a baseline or target was set: `| date | metric | baseline | current | target | source | confidence | note |`, append-only.

## Guardrails
- One question at a time. This is the rule the skill is built on. Never batch, never send a numbered list of questions, never race ahead while a branch is still open.
- Recommend, never decide. Every question carries your recommended answer and why, but the human answers and the human owns the call. Never invent the human's answer to keep moving.
- Draft only. Grill writes drafts and recommendations. It never sends, publishes, posts, launches, changes a live ad or site, spends, or contacts anyone.
- Cite the context. A recommendation leans on a named file or a ledger row, or it is marked a guess. Never present a guessed number as if it came from the ledger.
- Agency firewall. If the plan belongs to one client, read only that `Clients/{slug}/` folder, never a sibling client.
- Mark gaps honestly. A branch with no real answer is "open" or "unproven", never a bracket placeholder and never quietly filled.
- Stay in lane. Grill sharpens before the build; it does not render the final commit verdict (that is doubt-check) and does not document an existing process (that is process-interviewer).

## Red flags
- Sending more than one question in a turn, or a numbered batch, instead of the single highest-leverage one.
- Accepting a vague answer ("everyone", "soon", "grow the business") and moving on without drilling it to a number, a name, or a date.
- Writing the human's answer for them to keep the loop moving, instead of stopping and waiting.
- Asking a low-leverage question (font, button color) while the audience, offer, or budget branch is still open.
- A recommended answer that cites no file and no ledger row, presented as if it were grounded.
- Calling the plan GO while a load-bearing branch (who, what offer, what metric) is still an adjective, not a fact.
- Declaring a success metric with no baseline pulled from the ledger to judge it against.
- Drifting into the final commit verdict or into documenting an existing process, instead of sharpening the new plan.

## Verification
- [ ] The plan and the outcome it assumes were each restated in one line and confirmed by the human before grilling began.
- [ ] The decision tree was mapped; every default branch (audience, offer, channel, budget, timing, success metric, owner, fallback) is resolved or explicitly marked N/A with a reason.
- [ ] Questions were asked one at a time, never batched, each carrying a recommended answer and a one-line why.
- [ ] Every vague answer was drilled to something concrete (a named audience, a number, a date, an owner, or a measurable target).
- [ ] The running resolved-versus-open list was restated after each answer, and no load-bearing branch was closed without a real answer.
- [ ] The synthesis tags each assumption solid, thin, or unproven, names the top risks, and states the one number that would prove the plan.
- [ ] The verdict is GO, REWORK, or STOP, and a REWORK or STOP names the exact branch or assumption that blocks it.
- [ ] No answer was invented for the human; open branches are recorded as open, not filled.
- [ ] Nothing was sent, launched, published, or spent; any decision file or ledger row is status:draft and append-only.
- [ ] Agency run: read only the active client's `Clients/{slug}/` folder, never a sibling.

## Rationalizations
| Excuse | Reality |
|---|---|
| "I'll send all the questions at once to save the human time." | One question at a time is the whole point. A batch lets vague answers slide and skips the drill. Ask the highest-leverage one and wait. |
| "The human didn't say, so I'll assume the audience is everyone." | "Everyone" is not an audience, it is a skipped branch. Drill to a named segment or record it open; never invent it. |
| "The plan feels strong, I'll call it GO without finishing the branches." | A GO with an open load-bearing branch is a guess dressed as a verdict. Finish the branches or return REWORK and name the gap. |
| "Close enough, 'more leads' is the success metric." | An adjective is not a metric. Drill to a number and a date, then pull the baseline from the ledger to judge it against. |
| "I'll just give the recommended answer and move on." | A recommendation is not an answer. The human decides each branch; you stop and wait, you do not decide for them. |
| "This plan is basically a decision, I'll render the final STOP or GO myself." | That is doubt-check's job. Grill sharpens, then hands off. Rendering the commit verdict here skips the adversarial pass. |

## References
- `Company/strategy.md`, `Company/offers.md`, `Company/icp.md` for the bet, the offer, and the audience the plan must serve.
- `Memory/kpi-ledger.md` for the baselines the success metric is judged against, append-only.
- `Memory/lessons.md` for plans of this shape that already worked or failed.
- `Memory/decisions/` for where the sharpened plan and verdict are recorded.
- doubt-check for the final adversarial STOP or GO before the spend actually commits.
- process-interviewer for documenting a process that already runs (not a new plan).
