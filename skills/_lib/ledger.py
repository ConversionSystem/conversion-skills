"""Shared ledger parsing for Conversion Skills bundled engines. Standard library only."""
import re

COLS = ["date", "metric", "baseline", "current", "target", "source", "confidence", "note"]


def parse_ledger(path):
    """Parse an append-only kpi-ledger.md markdown table into a list of row dicts."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line.startswith("|"):
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 8:
                continue
            if cells[0].lower() == "date" or set(cells[0]) <= set("-: "):
                continue  # header or separator row
            rows.append(dict(zip(COLS, cells[:8])))
    return rows


def _num(v):
    try:
        return float(re.sub(r"[^0-9.\-]", "", v))
    except (ValueError, TypeError):
        return None


def latest_per_metric(rows):
    """The most recent row per metric. The ledger is chronological append-only, so later wins."""
    out = {}
    for r in rows:
        out[r["metric"]] = r
    return out


def first_per_metric(rows):
    """The first row per metric, used as the baseline when no snapshot is supplied."""
    out = {}
    for r in rows:
        out.setdefault(r["metric"], r)
    return out


def scorecard(rows, baseline=None):
    """Build a scorecard: per metric, baseline, current, target, delta, direction, vs_target."""
    latest = latest_per_metric(rows)
    first = first_per_metric(rows)
    cards = []
    for metric, r in latest.items():
        base = (baseline or {}).get(metric)
        if base is None:
            base = first[metric]["baseline"] or first[metric]["current"]
        cur, tgt = r["current"], r["target"]
        bn, cn, tn = _num(base), _num(cur), _num(tgt)
        delta = None if (bn is None or cn is None) else round(cn - bn, 4)
        direction = "flat"
        if delta is not None:
            direction = "up" if delta > 0 else ("down" if delta < 0 else "flat")
        vs_target = None
        if None not in (bn, cn, tn) and tn != bn:
            vs_target = "on-track" if (cn - bn) / (tn - bn) >= 0.5 else "behind"
        cards.append({
            "metric": metric, "baseline": base, "current": cur, "target": tgt,
            "delta": delta, "direction": direction, "vs_target": vs_target,
            "source": r["source"], "confidence": r["confidence"], "date": r["date"],
        })
    return cards
