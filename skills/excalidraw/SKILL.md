---
name: excalidraw
description: Draw a hand-sketched diagram of a concept or flow as an importable Excalidraw file with nodes, edges, and layout, triggered by "diagram this", "draw the flow", or "excalidraw"
---

# Excalidraw Diagram

Turn a concept, flow, or architecture into a hand-drawn style diagram saved as an importable Excalidraw spec.

## When to use
- You want to picture a funnel, a sequence, an org map, or a system flow before writing about it.
- A brief, SOP, case study, or content piece needs a diagram a reader can scan in five seconds.
- Someone hands you a list of steps and asks to "draw the flow" or "diagram this".

## Inputs
- The concept to draw: a flow, a tree, a funnel, a set of boxes and arrows, or a short description.
- Node labels and the edges between them (or enough context to infer them).
- Optional: a target file, the parent project or content slug, and a layout hint (left to right, top to bottom, or radial).
- Optional: brand colors from Company/brand for node fills and stroke.

## Process
1. Read Company/brand for color and tone. Read the source brief if a project or content slug was named (Projects/{slug}/brief.md or Content/{slug}-{date}/brief.md).
2. List the nodes. Give each a short label (three to six words), a stable id, and a shape (rectangle for a step, diamond for a decision, ellipse for a start or end).
3. List the edges. For each, name the source id, the target id, and an optional label on the arrow.
4. Pick a layout from the hint or the shape of the graph: left to right for a sequence, top to bottom for a hierarchy, radial for a hub. Assign x and y so nodes do not overlap and arrows do not cross where it can be helped.
5. Build the Excalidraw JSON: type "excalidraw", version 2, an elements array (rectangle, diamond, ellipse, text, and arrow objects with bound ids), and an appState with a neutral background. Use the hand-drawn roughness setting so it reads as sketched.
6. Apply brand colors to fills and strokes; keep text dark and legible.
7. Write the file. Solo and Team: Projects/{slug}/data/ or final/. Agency: Clients/{slug}/Projects/{project}/data/ for the active client only, marked confidential:true.
8. Note that this is a draft spec to import into excalidraw.com or the Obsidian Excalidraw plugin, never published or sent on its own.

## Outputs
- An importable diagram file: Projects/{slug}/final/{name}.excalidraw (Solo and Team) or Clients/{slug}/Projects/{project}/final/{name}.excalidraw (Agency).
- A short companion note listing nodes and edges in plain text next to the file, for review without the app.
- No KPI ledger row. If the diagram backs a project whose status moved, that change is logged by the owning skill, not here.

## Guardrails
- Draft only. The diagram is a working file to import and edit, never published, sent, or shown to a client by this skill.
- Provenance: label only what the source supports. Never invent a step, a metric, or a quote to fill the picture.
- Voice from Library/styles/brand-voice.md (agency: the client's). Labels stay terse: nouns and verbs, no filler.
- Firewall (agency): read and write the active client only; never read a sibling client; outputs confidential:true.
- excalidraw.com and the Obsidian plugin are optional connectors. The spec is plain JSON and renders offline; no credentials and no upload are required to produce it.

## References
- _system/connectors.md (optional Excalidraw connector)
- Company/brand (colors, tone)
- Library/styles/brand-voice.md (label voice)
