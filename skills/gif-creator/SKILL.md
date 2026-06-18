---
name: gif-creator
description: Build a short looping gif from a sequence of screens, frames, or a described animation, producing a storyboard plus either the rendered file via a connector or a precise render spec. Triggers on "make a gif", "looping gif", "animate these screens", "turn these frames into a gif".
---

# GIF Creator

Turn a sequence of screens, frames, or a described motion into a short looping gif. Draft a storyboard first, then render the file if a tool connector is registered, otherwise hand off a precise spec a renderer can run.

## When to use
- You have 2 or more screens, frames, or stills and want them stitched into a loop.
- You want a product flow, before/after, or step count shown as a moving demo.
- You have no frames yet but can describe the motion, and need a frame plan plus a render spec.
- You need a lightweight moving asset for a post, email, or case study without opening a video editor.

## Inputs
- Source frames: image files in `Projects/{slug}/data/` or `Content/{slug}-{date}/data/`, or a described animation in plain text.
- Intent: what the gif should show and where it runs (post, email, landing block, doc).
- Loop spec (optional): target seconds, frames per second, loop style (forward, ping-pong, hold-last), and max pixel width.
- Brand voice from `Library/styles/brand-voice.md` (agency: the active client's) for any on-frame captions.
- Connector status from `_system/connectors.md` (look for an image or video render tool).

## Process
1. Read the intent and confirm the one thing the gif must show. Write it as a single line.
2. Gather frames. If files exist, list them in order and note width, height, and count. If only a description exists, break the motion into 4 to 12 discrete frames, each one line.
3. Set the loop plan: frames per second, total seconds, loop style, pixel width, and a target file size ceiling (default 5 MB for email and post use). Keep total seconds at or under 6 for a clean loop.
4. Write the storyboard to `Projects/{slug}/data/gif-storyboard.md` (Solo and Team), or `Clients/{slug}/Projects/{slug}/data/gif-storyboard.md` (Agency, active client only). One row per frame: frame number, source file or drawn description, on-frame caption if any, hold time in milliseconds, and a transition note.
5. Caption check: any on-frame text follows brand voice, carries no blocklist words, and cites a source if it states a metric. Never invent a number for a frame.
6. Check `_system/connectors.md` for a registered render tool.
   - If present: pass the ordered frames and loop plan to the connector, save the returned file to `Projects/{slug}/final/{slug}.gif` (Agency: the client path), and record the actual frame count, dimensions, duration, and file size.
   - If absent: write a render spec to `Projects/{slug}/final/gif-spec.md` with the exact ordered frame list, per-frame durations, fps, loop style, output dimensions, color note, and a ready-to-run command line a person or a connector can execute later. Do not fabricate a rendered file.
7. Append a ledger row to `Memory/kpi-ledger.md` noting the asset was drafted (metric: gif drafted, source: this skill).
8. Stop at draft. Never post, send, or publish the gif or attach it to a live channel.

## Outputs
- `Projects/{slug}/data/gif-storyboard.md` (Agency: `Clients/{slug}/Projects/{slug}/data/gif-storyboard.md`): the frame-by-frame plan.
- One of: `Projects/{slug}/final/{slug}.gif` (when a render connector ran) or `Projects/{slug}/final/gif-spec.md` (the precise render spec).
- A render log line inside the storyboard recording final dimensions, duration, and file size when a file was produced.
- One appended row in `Memory/kpi-ledger.md` marking the draft.

## Guardrails
- Draft only. Never publish, send, post, or attach the gif to a client or a live channel.
- Agency: read and write the active client only, never a sibling client. Client outputs carry `confidential: true`.
- On-frame text uses brand voice and avoids blocklist words. No invented metrics or quotes; cite a source for any stated number and append a ledger row when a metric moves.
- A render tool is an optional connector registered in `_system/connectors.md`. With no connector, deliver the spec, never a faked file. Credentials stay out of the vault.
- Keep total loop length at or under 6 seconds and respect the file size ceiling so the asset stays usable in email and posts.

## References
- `Library/styles/brand-voice.md` for caption voice.
- `_system/connectors.md` for render tool status.
- `Memory/kpi-ledger.md` for the append-only draft log.
