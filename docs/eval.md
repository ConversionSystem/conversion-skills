# Eval method

The gates (clean-room, budgets, secrets, firewall, brand, sections) prove a skill is well formed.
They do not prove its output is any good. A skill can pass every gate and still drift: shorter
findings, fewer citations, vaguer fixes, a missing baseline. The eval harness exists to catch that
drift before a client sees it.

## How it works

Each skill under eval has a fixture in `evals/fixtures/<skill>.json`. A fixture holds one or more
cases. Each case has a fixed input, a plain-language `must` list, a set of deterministic
`auto_checks`, and a set of subjective `dimensions`. See `evals/README.md` for the schema.

There are two scoring layers.

1. Deterministic auto-checks. `scripts/eval.py score <skill> <output-file>` reads a recorded output
   and runs the case auto-checks against it: does it cite enough sources, does it have the required
   sections, is it long enough to be real work, is it free of em-dashes, banned words, and
   placeholder stubs. It prints a pass count and appends one row to `evals/baselines/scorecard.md`.
   This is fast, free, and repeatable, so it runs in CI through `scripts/eval.py validate` (which
   checks the corpus is well formed) and by hand on real outputs.

2. Judge dimensions. The subjective axes (specificity, prioritization, evidence, actionability,
   coverage, and the like) are scored 0 to 5 by a person or by the judge agent at
   `_system/agents/judge.md`. This is manual by default. Run it when you change a heavy skill or
   before a release, not on every commit.

## Running an eval

1. Pick a skill with a fixture, for example seo-audit.
2. Print the sheet: `scripts/eval.py checklist seo-audit`.
3. Run the skill on the case input and save its output to a file, for example `out.md`.
4. Auto-score it: `scripts/eval.py score seo-audit out.md`. Read the pass or fail per check.
5. Score the judge dimensions 0 to 5, by reading the output yourself or by handing the output and
   the dimension list to the judge agent.
6. Record the run. The auto-score row is appended for you. Note the dimension scores next to it so
   the next run has a baseline to beat.

## Reading drift

The scorecard is append-only and oldest first. Compare a fresh run for a skill against its prior
rows. A drop in the auto-check pass rate, or a falling dimension score, is the signal: the skill
got worse even though the gates still pass. Investigate the skill prose, not the harness.

## Adding a skill

Write `evals/fixtures/<skill>.json` to the schema in `evals/README.md`, point it at a real skill,
give it at least one case with a fixed input, a `must` list, deterministic `auto_checks`, and judge
`dimensions`. Run `scripts/eval.py validate`. CI keeps the corpus honest from then on.

## What not to do

Do not chase a perfect auto-score by gaming the checks (stuffing links to clear `min_citations`).
The auto-checks are a floor, not the goal. The judge dimensions and the `must` list are what a real
output has to earn. Do not commit recorded outputs that contain client data, the scorecard records
the path and the score, not the body.
