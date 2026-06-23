---
name: business-review
description: Roll up a monthly or quarterly KPI scorecard with by-area movement, narrative, and next moves · run when someone says business review, monthly review, quarterly review, KPI rollup, or how are we tracking against targets.
---

# Business Review

Turn the KPI ledger into a period scorecard that makes the compounding visible: every metric baseline to current to target, what moved and why, an honest narrative, and the highest-leverage moves to run next.

## When to use
- The end of a month or quarter, or any time someone asks "how are we tracking against targets" or wants a KPI rollup.
- Before a planning session, board update, or strategy refresh that needs a single honest read on progress.
- On a recurring cadence to keep `Memory/kpi-ledger.md` momentum traced and the next review's diff baseline fresh.

## Inputs
- Period to cover (month or quarter). If not supplied, confirm it before reading anything.
- `Memory/kpi-ledger.md` · the whole file, every row (append-only source of truth).
- `Company/strategy.md` · current priorities and targets to score against.
- Recent `Memory/decisions/` entries relevant to the period (what was decided and why).
- Deliverables' `data/baseline.json` snapshots under `Projects/{slug}/` and `Content/{slug}-{date}/` (what each piece of work actually moved).
- The previous review's snapshot, `Operations/reviews/{prev-date}-business-review/data/baseline.json`, if one exists (for the trend lead).

## Process

### Phase 1 · LOAD
1. Confirm the period with the user (e.g. `2026-05` for a month or `2026-Q2` for a quarter). Do not proceed until it is fixed; this date drives every output path.
2. Read the entire `Memory/kpi-ledger.md`. Note every metric, its latest `current`, `target`, `source`, and `confidence`. Never skim · the rollup must trace to real rows.
3. Read `Company/strategy.md` for the active priorities and targets each metric is judged against.
4. Read the relevant `Memory/decisions/` entries for the period · these explain why numbers moved.
5. Read each deliverable's `data/baseline.json` under `Projects/` and `Content/` to attribute movement to specific work.
6. If a prior review snapshot exists, load its `data/baseline.json` so the report can lead with the trend versus last time.

### Phase 2 · ROLL-UP
7. Build the **SCORECARD**: one table, every metric, columns `metric | baseline | current | target | period delta | direction | source row`. Direction is `on-track`, `behind`, or `regressed`. Every value traces to a real ledger row · never invent a number. If a metric has no fresh row, mark it `stale` and say so; do not fabricate.
8. Write **BY-AREA** across acquisition, conversion, retention, content, and pipeline: for each area, what moved and why, citing the specific deliverable(s) (path-referenced) that drove it.
9. Write the **NARRATIVE**: exactly three evidence-linked wins (each tied to a metric and a deliverable), what stalled, and an honest read · lead with what is behind, not what looks good.
10. Write **DO-NEXT**: exactly three highest-leverage moves. Each names a measurable goal (a specific metric and target) and a concrete Conversion Skills skill to run to get there.
11. If a prior snapshot exists, open the report with the trend versus last review (which metrics improved, held, or regressed since the last snapshot) before the scorecard.
12. Write the report to `Operations/reviews/{date}-business-review/{date}-business-review.md` with `generated: true` in frontmatter. Write the snapshot `data/baseline.json` beside it as the artifact the next review diffs against.
13. Append a one-line entry to today's `Daily/YYYY-MM-DD.md` noting the review was generated and the headline read.

## Outputs
- `Operations/reviews/{date}-business-review/{date}-business-review.md` · the generated review (`generated: true`); sections in order: TREND (re-run only), SCORECARD, BY-AREA, NARRATIVE, DO-NEXT.
- `Operations/reviews/{date}-business-review/data/baseline.json` · the period snapshot the next review diffs against.
- One appended line in `Daily/YYYY-MM-DD.md` · Daily Activity entry: review generated + headline.
- No rows added to `Memory/kpi-ledger.md` · the ledger is read here, never written.

## Guardrails
- Reads only, with three exceptions: its own report file, its own `data/baseline.json`, and the one-line Daily Activity entry. Touch nothing else.
- Never edit, reorder, or append to `Memory/kpi-ledger.md`. Never hand-edit any `generated: true` rollup.
- Every scorecard number must trace to a real ledger row. If it cannot be traced, mark it `stale` and surface the gap · never invent or estimate a figure.
- Lead with what is behind. The honest read is the point; do not bury regressions under wins.
- Respect the Agency firewall · read only the active vault context; never read sibling `Clients/{slug}/` data into a shared review.
- Frontmatter on the report carries the universal keys with `generated: true`; the report is regenerated on re-run, never patched by hand.

## Red flags
- Writing a scorecard number that no `Memory/kpi-ledger.md` row supports, instead of marking the metric `stale`.
- Leading the NARRATIVE with wins while a regressed metric sits lower in the report, or quietly omitted.
- Attributing BY-AREA movement to a deliverable without a path-referenced `data/baseline.json` to cite.
- Producing more or fewer than three NARRATIVE wins, three DO-NEXT moves, or skipping a metric in the SCORECARD.
- A DO-NEXT move with no measurable goal (named metric + target) or no concrete Conversion Skills skill to run.
- Editing, reordering, or appending to `Memory/kpi-ledger.md`, or hand-patching a `generated: true` report on re-run.

## Verification
- [ ] Every SCORECARD row has a `source row` pointing at a real `Memory/kpi-ledger.md` entry; untraceable metrics are marked `stale`, not estimated.
- [ ] Each BY-AREA claim cites the specific deliverable path (`Projects/{slug}/...` or `Content/{slug}-{date}/...`) that drove the movement.
- [ ] NARRATIVE has exactly three evidence-linked wins, names what stalled, and leads with what is behind.
- [ ] DO-NEXT has exactly three moves, each with a named metric, a target, and a concrete skill to run.
- [ ] `Memory/kpi-ledger.md` is byte-for-byte unchanged; the only writes are the report, its `data/baseline.json`, and one Daily Activity line.
- [ ] If a prior snapshot exists, the report opens with the TREND versus last review before the SCORECARD.
- [ ] Report frontmatter carries `generated: true`; nothing was published or sent, the output is a draft review file.
- [ ] Agency firewall held: no sibling `Clients/{slug}/` data was read into a shared review.

## Rationalizations
| Rationalization | Reality |
|---|---|
| "The ledger row is missing but I know the number is roughly right." | Mark it `stale`. A guessed figure in a board read is a number someone will plan against and miss. |
| "Last month was rough, lead with the wins so it reads well." | Lead with what is behind. Burying the regression is how it compounds another period unnoticed. |
| "I'll just nudge this stale ledger row so the scorecard is clean." | Reads only. Touch the ledger and the next review's diff baseline is corrupted; the firewall is the whole point. |
| "Movement is obviously from that campaign, no need to cite the baseline." | Cite the `baseline.json` path. Uncited attribution is a story, and stories do not survive the next planning session. |
| "Four wins is better than three, more good news." | Exactly three. The fixed count forces a ranked, honest read instead of a padded highlight reel. |

## Orchestration
Run `agents/judge` on the scorecard claims before the review is shared; cut what it refutes. See `docs/orchestration.md`.

## References
- `Memory/kpi-ledger.md` (append-only KPI source, confidence in confirmed/reported/inferred/stale)
- `Company/strategy.md` (priorities and targets)
- `Memory/decisions/` (period rationale)
- `Projects/{slug}/data/baseline.json`, `Content/{slug}-{date}/data/baseline.json` (deliverable movement)
