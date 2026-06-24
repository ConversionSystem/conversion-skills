#!/usr/bin/env python3
"""Conversion Skills output-quality eval harness.

Commands:
  validate              check the fixture corpus is well formed and points at real skills (CI safe, deterministic).
  checklist <skill>     print the scoring sheet for a skill: the deterministic auto-checks plus the judge dimensions.
  score <skill> <file>  run the deterministic auto-checks on a recorded skill output, append a row to the scorecard.

The auto-checks catch structural quality drift for free. The judge dimensions are subjective and
are scored by a person or by the judge agent (_system/agents/judge.md). See docs/eval.md for the method.
"""
import json, glob, os, re, sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
FIX_DIR = "evals/fixtures"
SCORECARD = "evals/baselines/scorecard.md"

BANNED = ["partner", "journey", "unlock", "empower", "transformative", "holistic", "seamless",
          "synergize", "ecosystem", "best-in-class", "world-class", "cutting-edge", "scalable",
          "reimagined", "elevate", "solutions", "circle back", "touch base", "north star",
          "north-star", "10x", "thought leadership", "drive value"]

PLACEHOLDERS = ["tbd", "todo", "[check]", "lorem ipsum", "xxxx", "[your ", "[insert", "[company",
                "[name]", "placeholder", "fixme"]

AUTO_TYPES = {"min_links", "min_citations", "no_em_dash", "no_banned", "no_placeholders",
              "regex", "min_words", "max_words", "requires_sections", "appends_ledger"}


def load_fixtures():
    out = []
    for f in sorted(glob.glob(f"{FIX_DIR}/*.json")):
        with open(f) as fh:
            out.append((f, json.load(fh)))
    return out


def fixture_for(skill):
    for path, fx in load_fixtures():
        if fx.get("skill") == skill:
            return path, fx
    return None, None


# ---- deterministic checks -------------------------------------------------

def _links(text):
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def _citations(text):
    md = set(_links(text))
    bare = set(re.findall(r"https?://\S+", text))
    return md | bare


def run_auto_check(check, text):
    t = check["type"]
    if t == "min_links":
        n = len(_links(text)); return n >= check["min"], f"{n} markdown links (min {check['min']})"
    if t == "min_citations":
        n = len(_citations(text)); return n >= check["min"], f"{n} citations (min {check['min']})"
    if t == "no_em_dash":
        n = text.count("\u2014"); return n == 0, f"{n} em-dashes"
    if t == "no_banned":
        hits = [w for w in BANNED if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", text, re.I)]
        return not hits, ("none" if not hits else f"banned: {hits}")
    if t == "no_placeholders":
        low = text.lower(); hits = [p for p in PLACEHOLDERS if p in low]
        return not hits, ("none" if not hits else f"placeholders: {hits}")
    if t == "regex":
        flags = re.I if "i" in check.get("flags", "") else 0
        ok = re.search(check["pattern"], text, flags) is not None
        return ok, ("matched" if ok else f"missing pattern {check['pattern']!r}")
    if t == "min_words":
        n = len(text.split()); return n >= check["min"], f"{n} words (min {check['min']})"
    if t == "max_words":
        n = len(text.split()); return n <= check["max"], f"{n} words (max {check['max']})"
    if t == "requires_sections":
        low = text.lower(); missing = [s for s in check["sections"] if s.lower() not in low]
        return not missing, ("all present" if not missing else f"missing: {missing}")
    if t == "appends_ledger":
        ok = re.search(r"\|.*\d{4}-\d{2}-\d{2}.*\|.*\|.*\|.*\|", text) is not None
        return ok, ("ledger row found" if ok else "no append-only ledger row")
    return False, f"unknown check type {t}"


# ---- commands -------------------------------------------------------------

def cmd_validate():
    fixtures = load_fixtures()
    if not fixtures:
        print("EVAL FAIL: no fixtures in evals/fixtures/"); return 1
    bad = 0
    seen_ids = {}
    cases_total = 0
    for path, fx in fixtures:
        skill = fx.get("skill")
        if not isinstance(skill, str) or not skill:
            print(f"EVAL FAIL: {path} missing 'skill'"); bad += 1; continue
        if not os.path.isfile(f"skills/{skill}/SKILL.md"):
            print(f"EVAL FAIL: {path} targets skills/{skill}/ which does not exist"); bad += 1
        cases = fx.get("cases")
        if not isinstance(cases, list) or not cases:
            print(f"EVAL FAIL: {path} has no cases"); bad += 1; continue
        for c in cases:
            cases_total += 1
            cid = c.get("id")
            if not cid:
                print(f"EVAL FAIL: {path} a case is missing 'id'"); bad += 1; continue
            if cid in seen_ids:
                print(f"EVAL FAIL: duplicate case id '{cid}' in {path} and {seen_ids[cid]}"); bad += 1
            seen_ids[cid] = path
            for key in ("input", "must", "auto_checks", "dimensions"):
                if key not in c:
                    print(f"EVAL FAIL: case '{cid}' missing '{key}'"); bad += 1
            for ch in c.get("auto_checks", []):
                if ch.get("type") not in AUTO_TYPES:
                    print(f"EVAL FAIL: case '{cid}' bad auto-check type {ch.get('type')!r}"); bad += 1
                    continue
                need = {"min_links": ["min"], "min_citations": ["min"], "regex": ["pattern"],
                        "min_words": ["min"], "max_words": ["max"], "requires_sections": ["sections"]}
                for p in need.get(ch["type"], []):
                    if p not in ch:
                        print(f"EVAL FAIL: case '{cid}' auto-check {ch['type']} missing '{p}'"); bad += 1
            for d in c.get("dimensions", []):
                if "name" not in d or "desc" not in d:
                    print(f"EVAL FAIL: case '{cid}' a dimension is missing name/desc"); bad += 1
    if bad:
        print(f"Eval corpus check FAILED ({bad})."); return 1
    print(f"Eval corpus check passed: {len(fixtures)} fixtures, {cases_total} cases, all point at real skills.")
    return 0


def cmd_checklist(skill):
    path, fx = fixture_for(skill)
    if not fx:
        print(f"no fixture for {skill}"); return 1
    for c in fx["cases"]:
        print(f"\n## {c['id']}")
        print(f"input: {c['input']}\n")
        print("MUST (pass or fail):")
        for m in c["must"]:
            print(f"  [ ] {m}")
        print("\nAUTO-CHECKS (run: scripts/eval.py score):")
        for ch in c["auto_checks"]:
            print(f"  - {ch['id']} ({ch['type']})")
        print("\nJUDGE DIMENSIONS (score 0 to 5 each, by a person or the judge agent):")
        for d in c["dimensions"]:
            print(f"  [ _ ] {d['name']}: {d['desc']}")
    return 0


def cmd_score(skill, output_path, case_id=None):
    path, fx = fixture_for(skill)
    if not fx:
        print(f"no fixture for {skill}"); return 1
    case = next((c for c in fx["cases"] if c["id"] == case_id), None) if case_id else fx["cases"][0]
    if not case:
        print(f"no case {case_id} for {skill}"); return 1
    if not os.path.isfile(output_path):
        print(f"output file not found: {output_path}"); return 1
    text = open(output_path).read()
    passed = 0
    rows = []
    for ch in case["auto_checks"]:
        ok, detail = run_auto_check(ch, text)
        passed += 1 if ok else 0
        rows.append((ch["id"], "PASS" if ok else "FAIL", detail))
    total = len(case["auto_checks"])
    print(f"\nauto-score {skill} / {case['id']}: {passed}/{total}")
    for cid, verdict, detail in rows:
        print(f"  {verdict:4} {cid}: {detail}")
    print("\nJudge dimensions still to score (0 to 5, manual):")
    for d in case["dimensions"]:
        print(f"  - {d['name']}")
    # append to the scorecard
    os.makedirs(os.path.dirname(SCORECARD), exist_ok=True)
    line = f"| {date.today().isoformat()} | {skill} | {case['id']} | {passed}/{total} | {output_path} |\n"
    if not os.path.isfile(SCORECARD):
        with open(SCORECARD, "w") as fh:
            fh.write("# Eval scorecard\n\n")
            fh.write("Auto-check pass rate per recorded run. Judge dimension scores are tracked alongside, by hand. Append-only.\n\n")
            fh.write("| date | skill | case | auto-checks | output |\n")
            fh.write("|------|-------|------|-------------|--------|\n")
    with open(SCORECARD, "a") as fh:
        fh.write(line)
    print(f"\nappended to {SCORECARD}")
    return 0


def main():
    args = sys.argv[1:]
    cmd = args[0] if args else "validate"
    if cmd == "validate":
        return cmd_validate()
    if cmd == "checklist" and len(args) >= 2:
        return cmd_checklist(args[1])
    if cmd == "score" and len(args) >= 3:
        case_id = args[3] if len(args) >= 4 else None
        return cmd_score(args[1], args[2], case_id)
    print(__doc__); return 1


if __name__ == "__main__":
    sys.exit(main())
