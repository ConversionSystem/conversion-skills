---
name: infographic
description: Designs an infographic from one idea and cited data points then either renders it through a registered image connector or writes a build-ready spec, triggered by "make an infographic", "design an infographic", "turn this into a graphic", or "visualize this data"
---

# Infographic

Design one infographic: name the single idea, gather cited data points, structure the visual flow, and set the visual direction, then render it if an image connector is registered or output a build-ready spec when it is not.

## When to use
- The user asks to "make an infographic", "design an infographic", or "turn this into a graphic" from a topic, a report, or a set of numbers.
- A piece of content, case study, or KPI movement has a clear single idea that a visual would carry better than prose.
- You want a structured, cited visual brief that a designer or an image tool can build from without inventing data.

## Inputs
- `Library/styles/brand-voice.md` · tone, voice, and any naming constraints for on-graphic copy. For Agency runs, use the active client's voice file under `Clients/{slug}/`.
- `Company/brand.md` · positioning, color and type direction, do/don't, logo and usage rules. For Agency runs, read the client's brand file instead.
- `_system/connectors.md` · whether an image connector is registered, its name, and its inputs.
- Source material for every data point: a `Content/{slug}-{date}/data/` file, `Memory/kpi-ledger.md` rows, `Operations/case-studies/`, `Company/` truth files, or a user-provided document or URL.
- Optional user input: the one idea, target channel and aspect ratio, piece count of data points, and any required brand assets.

## Process
1. Lock the one idea. State the single takeaway the infographic must land in one sentence. If the user gave a topic but no idea, propose 2-3 candidate ideas and get one confirmed before going further. One graphic carries one idea; reject scope creep into a second.
2. Gather and cite data points. Pull 3-7 data points that prove the idea, each with a source. Read from `Content/{slug}-{date}/data/`, `Memory/kpi-ledger.md`, `Operations/case-studies/`, `Company/` files, or the user-supplied document. Record each point as value plus source plus confidence in {confirmed,reported,inferred,stale}. Never invent a number, a quote, or a trend; if a point has no source, drop it or mark the gap.
3. Structure the flow. Order the points into a reading path: headline (the one idea), 3-7 supporting blocks, and a closing line or call to read. Pick the chart or motif per point (single big number, bar, trend line, ratio, map, step sequence) based on what the data shape supports, not decoration.
4. Set visual direction. From `Company/brand.md` (or the client's brand for Agency), specify palette, type, layout grid, aspect ratio for the target channel, iconography style, and on-graphic copy written to `brand-voice.md`. Keep copy terse: numbers over adjectives, verbs over nouns.
5. Check the connector. Read `_system/connectors.md`. If an image connector is registered, prepare its inputs (prompt or layout payload, dimensions, brand assets) and render to `Content/{slug}-{date}/final/`. If none is registered, write the build-ready spec only and name the connector the user could register to render it.
6. Write the deliverable. Create or reuse `Content/{slug}-{date}/` with a kebab-case slug and ISO date. Write `brief.md` (the one idea, the cited data table, the structure, the visual direction) and `data/sources.json` (each data point with value, source, confidence). Place any rendered image or the build-ready `spec.md` in `final/`.
7. Log any moved metric. If the infographic states a KPI that changed, append one row to `Memory/kpi-ledger.md`. Never edit prior rows.

## Outputs
- `Content/{slug}-{date}/brief.md` · the infographic brief with universal frontmatter (`type:content-brief`, `status:draft`, `owner`, `date`, `reviewed`, `tags` >=2, `confidential`, `source`, `generated:false`), the one idea, the cited data table, the structure, and the visual direction. For Agency runs set `confidential:true`.
- `Content/{slug}-{date}/data/sources.json` · every data point with its value, source, and confidence in {confirmed,reported,inferred,stale}.
- `Content/{slug}-{date}/final/` · the rendered image when an image connector ran, or `spec.md`, a build-ready specification (layout, dimensions, palette, type, per-block chart and copy) when no connector is registered.
- One appended row in `Memory/kpi-ledger.md` using the exact columns `| date | metric | baseline | current | target | source | confidence | note |`, only when the graphic states a metric that moved.

## Guardrails
- Draft-only. Never publish, post, or send the infographic; it stays `status:draft` in `final/` for human action.
- Cited data only. Every number, quote, and trend traces to a named source; never invent or estimate a data point. Drop or flag any point that has no source.
- Voice from `Library/styles/brand-voice.md` (Agency: the active client's). On-graphic copy obeys it.
- Connector boundary. Render only through an image connector registered in `_system/connectors.md`; credentials never live in the vault. With no connector, output the spec and stop.
- KPI ledger is append-only with the exact column order; never edit, reorder, or overwrite prior rows.
- Respect the Agency client firewall: read only the active `Clients/{slug}/`, never a sibling; mark client outputs `confidential:true`; route anything ambiguous to `Inbox/`.

## References
none
