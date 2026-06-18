---
name: video
description: Turn a script into a short video by producing the shot list, asset list, captions, and either an assembled cut from a connector or a build-ready package, written to Content/ as a draft. Triggers on "make a video", "cut this script", "video from script", "shot list", "video package".
---

# Video

Take a written script and produce everything a short video needs: a numbered shot list, the asset list to gather or generate, timed captions, and either an assembled cut (when a video connector is registered) or a build-ready package any editor can finish. Draft only.

## When to use

- You have a script (or a piece of content with a clear spoken track) and want a short video built from it.
- You want a shot-by-shot plan plus captions before anyone opens an editor.
- You want an asset checklist so footage, stills, and voiceover can be gathered or briefed.
- You want a cut assembled automatically if a connector allows it, and a clean handoff package if not.

## Inputs

- The script. A file path under `Content/{slug}-{date}/` or `Inbox/`, or pasted text. Required.
- Target length and aspect ratio (for example 60 seconds, 9:16). Default to 60 seconds and 9:16 if the script does not say.
- Voice reference from `Library/styles/brand-voice.md` (agency: the active client's voice file). Required for any on-screen or spoken copy.
- Brand cues from `Company/brand.md` (agency: the client's `Clients/{slug}/`): colors, fonts, logo path, lower-third style.
- Optional assets already on hand: footage, stills, logo, music, voiceover, listed by path.
- Optional video connector registered in `_system/connectors.md` (assembly, voiceover, or stock). Check before assuming any are present.

## Process

1. Resolve scope. Solo or Team writes to `Content/{slug}-{date}/`. Agency confirms the active client first, reads only that client's folder per the firewall, and marks outputs `confidential: true`. If no `{slug}-{date}` folder exists, create `Content/{slug}-{date}/` with `brief.md`, `data/`, and `final/`.
2. Read the script and the voice file. Pull the spoken track, the beats, and any callouts. If the script has no clear structure, segment it into a hook, body beats, and a close, and record that split in `brief.md`.
3. Lock the spec. Set length, aspect ratio, pacing (words per second from the script word count), and shot count. Write the spec to `brief.md`.
4. Build the shot list. For each beat, write one shot row: number, timecode in and out, spoken line, visual description, on-screen text, and a source tag (footage, still, screen-record, generated, b-roll). Save to `data/shot-list.md`.
5. Build the asset list. From the source tags, list every asset the cut needs: what it is, whether it is on hand or to gather, the path if on hand, and a one-line brief if it must be created. Flag anything that needs a connector (stock pull, generated still, voiceover). Save to `data/asset-list.md`.
6. Write captions. Produce timed captions in SRT format covering the full spoken track, line lengths kept short enough to read on a phone, in the resolved voice. Save to `data/captions.srt`. Also write a plain on-screen text list (`data/on-screen-text.md`) for any text that is not spoken.
7. Branch on connectors. If a video assembly connector is registered, assemble a draft cut from the shot list, available assets, and captions, and write it to `final/cut-draft.{ext}` with a `final/cut-notes.md` describing what was assembled and what is still a placeholder. If no connector is registered, write a build-ready package to `final/`: an edit decision list (`final/edit-decision-list.md` mapping each shot to its asset and timecode), the captions file, the on-screen text list, and `final/build-guide.md` with step-by-step assembly instructions for any editor.
8. Note gaps and provenance. Cite the script and any source files used. List missing assets, placeholders, and any metric or claim in the script that needs a source before publish. Never invent footage, quotes, or numbers.
9. Stop at draft. Do not publish, upload, or post. Hand back the paths and the open items.

## Outputs

- `Content/{slug}-{date}/brief.md` · spec, beat split, and open items.
- `Content/{slug}-{date}/data/shot-list.md` · numbered shots with timecodes, lines, visuals, on-screen text, source tags.
- `Content/{slug}-{date}/data/asset-list.md` · every asset, on-hand or to-gather, with paths or briefs.
- `Content/{slug}-{date}/data/captions.srt` · timed captions for the full spoken track.
- `Content/{slug}-{date}/data/on-screen-text.md` · non-spoken on-screen text.
- With a connector: `Content/{slug}-{date}/final/cut-draft.{ext}` plus `final/cut-notes.md`.
- Without a connector: `Content/{slug}-{date}/final/edit-decision-list.md` and `final/build-guide.md`, alongside the captions and on-screen text.
- Append a `Memory/kpi-ledger.md` row only if this run moves a tracked metric (for example a published-asset count); otherwise append no ledger row.

## Guardrails

- Draft only. Never publish, upload, post, schedule, or contact anyone.
- Voice comes from `Library/styles/brand-voice.md` (agency: the active client's voice file). On-screen and spoken copy must match it.
- Firewall (agency): read and write only the active client; never read a sibling client; outputs carry `confidential: true`.
- Provenance: cite the script and every source file. Never invent footage, stills, quotes, or metrics. Flag any claim that needs a source before publish.
- Connectors are optional and registered in `_system/connectors.md`. Credentials never live in the vault. With no connector, deliver the build-ready package and say so plainly.
- Keep assets the user provided as the first choice; only brief new assets when a beat has no source on hand.

## References

- `_system/connectors.md` · registered video, voiceover, and stock connectors.
- `Library/styles/brand-voice.md` · voice for on-screen and spoken copy.
- `Company/brand.md` · colors, fonts, logo, lower-third style (agency: the client's brand files).
