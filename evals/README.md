# Evals

Output-quality eval harness for Conversion Skills. It catches quality drift that the brand,
budget, and section gates cannot see: a skill that still passes every gate but quietly produces
thinner, vaguer, or less-cited work than it used to.

Skills are prose contracts that Claude runs, so output is not deterministic. The harness has two
layers:

- A deterministic layer (`scripts/eval.py`), which validates the fixture corpus and scores a
  recorded output against machine-checkable quality rules. This runs free in CI.
- A judge layer, a set of subjective dimensions scored 0 to 5 by a person or by the judge agent
  (`_system/agents/judge.md`). This is manual by default, run it when you change a heavy skill.

See `docs/eval.md` for the full method.

## Layout

```
evals/
  fixtures/<skill>.json     one fixture file per skill under eval
  baselines/scorecard.md    append-only record of every scored run
```

## Fixture schema

```json
{
  "skill": "seo-audit",
  "cases": [
    {
      "id": "unique-case-id",
      "input": "the scenario or prompt to run the skill on",
      "must": ["human-readable quality requirement", "..."],
      "auto_checks": [
        { "id": "cites_evidence", "type": "min_citations", "min": 5 }
      ],
      "dimensions": [
        { "name": "specificity", "desc": "what a strong output looks like on this axis" }
      ]
    }
  ]
}
```

- `skill` must match a real `skills/<skill>/` directory.
- `must` is the plain-language bar, what a good output has to do. It guides the judge.
- `auto_checks` are the deterministic rules. Supported `type` values: `min_links`, `min_citations`,
  `no_em_dash`, `no_banned`, `no_placeholders`, `regex` (needs `pattern`, optional `flags: "i"`),
  `min_words` (`min`), `max_words` (`max`), `requires_sections` (`sections`, matched case-insensitively),
  `appends_ledger`.
- `dimensions` are the subjective axes the judge scores 0 to 5.

## Use

```
scripts/eval.py validate              # CI runs this, checks the corpus is well formed
scripts/eval.py checklist seo-audit   # print the scoring sheet for a skill
scripts/eval.py score seo-audit out.md [case-id]   # auto-score a recorded output, append to the scorecard
```

To add a skill to the harness, drop a `<skill>.json` fixture in `fixtures/` that follows the schema
and run `scripts/eval.py validate`.
