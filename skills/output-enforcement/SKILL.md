---
name: output-enforcement
description: Check a design or content output against a written standard and pass or fail each rule with the exact fix, triggers on "enforce the brand", "QA this output", "check against spec", "does this pass"
---

# Output Enforcement

Hold a produced output to a written standard, brand, spec, or accessibility bar, and return pass or fail per rule with the exact fix for every miss.

## When to use
- A draft (page, post, email, design, copy) is done and you want it checked before it ships.
- You have a written standard to check against: a brand guide, a spec, an accessibility bar, a house style.
- You want a repeatable QA gate, not a vibe read. Every rule gets a verdict and, on a fail, the precise change.
- Someone says "enforce the brand", "QA this output", "check this against the spec", or "does this pass".

## Inputs
- The output to check. A file path under `Projects/`, `Content/`, or `Operations/`, or pasted text or markup.
- The standard to check against. One or more of:
  - `Company/brand.md` and `Library/styles/brand-voice.md` for voice and brand rules.
  - A spec file in the relevant `Projects/{slug}/brief.md` or a named standard.
  - An accessibility bar (state which: contrast, alt text, heading order, focus, labels).
- Optional: the rule set to apply, if narrower than the full standard.

## Process
1. Resolve the output. Read the target file, or take the pasted content. Note its path and type (copy, page, email, design markup).
2. Resolve the standard. Read `Company/brand.md`, `Library/styles/brand-voice.md`, and any named spec or `Projects/{slug}/brief.md`. List every checkable rule as a flat checklist. If a rule is vague, write down how you will test it before you test it.
3. Load the hard brand rules from `_system/rules`: no em-dashes, no blocklist words, voice from `Library/styles/brand-voice.md`, draft-only on outbound work, cite sources and never invent metrics.
4. Check each rule against the output. For every rule, record:
   - rule id and one-line statement,
   - verdict: PASS or FAIL,
   - on a fail: the exact location (line, selector, or quoted phrase), what is wrong, and the exact fix to apply.
5. Run the mechanical scans every time: em-dash characters, each blocklist word, banned phrases, voice misses (adjectives doing a number's job, nouns doing a verb's job).
6. For accessibility checks, test each named bar concretely: color contrast ratios with the numbers, alt text presence and quality, heading order, link and button labels, focus order. Quote the offending element.
7. Score the result. Count rules, passes, fails. Mark the output BLOCKED if any hard brand rule or any stated must-pass rule fails. Otherwise mark it CLEAR or CLEAR WITH FIXES.
8. Write the report. Put it next to the work it judges:
   - work produced for a project goes to `Projects/{slug}/final/enforcement-{date}.md`,
   - standalone or recurring QA goes to `Operations/reviews/enforcement-{slug}-{date}.md`.
9. Do not edit the output. This skill reports and prescribes. Hand the fixes back so the author or the relevant build skill applies them.

## Outputs
- A report at `Projects/{slug}/final/enforcement-{date}.md` or `Operations/reviews/enforcement-{slug}-{date}.md` containing:
  - header: output path, standard checked, date, verdict (BLOCKED, CLEAR, or CLEAR WITH FIXES), score (passes of total),
  - a table with columns: rule, verdict, location, fix,
  - a fix list: every failing rule restated as a one-line instruction the author can act on.
- No change to the checked output. No ledger row by default. If this run is tracking a recurring quality metric, append one row to `Memory/kpi-ledger.md` with the exact columns: | date | metric | baseline | current | target | source | confidence | note |.

## Guardrails
- Report only. Never edit the output under review. Prescribe the fix, do not apply it.
- Every fail needs a location and a concrete fix. No "tighten this up" without the replacement text or the exact change.
- Cite the rule. Each verdict points to the line in the standard it came from. Never invent a rule the standard does not state.
- One miss on a hard brand rule blocks the output. Em-dashes and blocklist words are automatic fails.
- Provenance: if the output claims a metric, check it has a source. An unsourced metric is a fail.
- The ledger is append-only. Never edit a prior row.

## References
- `Company/brand.md`, `Library/styles/brand-voice.md`
- `_system/rules`
- `Projects/{slug}/brief.md` for project-specific specs
