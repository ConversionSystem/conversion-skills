---
name: audio-transcriber
description: Transcribe an audio or video file into clean text then route it, sending a meeting to Operations/meetings/ with decisions, actions, and metrics pulled out, when asked to transcribe a recording, turn audio into notes, or write up a meeting
---

# Audio Transcriber

Turn a recording into clean, readable text, then route it to its canonical home. A meeting becomes a structured note in Operations/meetings/ with decisions, actions, and any metrics extracted. Draft only.

## When to use
- The user asks to "transcribe this recording", "turn this audio into text", "write up this meeting", "get notes from this call", or "clean up this transcript".
- A meeting, interview, voice memo, or call recording exists as a file (or a raw transcript) and needs to become usable, routed text.
- Use this when the source is spoken audio or video. For a written rough draft that just needs polishing, use a content or editing skill instead.

## Inputs
- The source: an audio or video file path, OR a provided transcript file (raw text or .vtt/.srt). One is required.
- A transcription connector registered in _system/connectors.md (status: active) if no transcript is provided and the file still needs transcribing. Credentials live in a secret manager, never in the vault.
- Optional: the recording type (meeting, interview, voice memo, content raw), so routing is exact. If unstated, infer from content and state the inference.
- Optional: for a meeting, the attendee names, date, and topic. For a known speaker, a name to label their turns.
- Optional: Library/styles/brand-voice.md and Company/brand.md, used only to clean filler and tidy phrasing, never to change meaning or invent words. Agency: Clients/{slug}/context/brand.md.

## Process
1. Confirm the source. If a transcript was provided, skip transcription and go to step 3. If only a media file exists, go to step 2.
2. Transcribe. Read _system/connectors.md for an active transcription connector. If one exists, transcribe the file through it and log the external read to _system/audit/. If none exists, stop and ask the user to either register a connector or paste a transcript. Never fabricate a transcript from a filename or guess at audio you cannot read.
3. Clean the text. Remove filler ("um", "uh", false starts), fix obvious mis-hearings only when context makes them certain, add paragraph breaks, and label speakers if names are known. Keep every claim, number, and quote exactly as spoken. Mark anything unclear as [inaudible] rather than guessing. Note the source and that this is a machine or provided transcript (accuracy is not certified).
4. Classify the recording. Decide the type (meeting, interview, voice memo, content raw) from content or the user's input, and state the choice.
5. Resolve slug and date. Kebab-case slug from the topic or attendees (e.g. "q3-pipeline-sync"). Date as the recording date if known, else today in ISO (YYYY-MM-DD).
6. Route by type:
   - Meeting: write the structured meeting note to Operations/meetings/ (Solo/Team) or Clients/{slug}/operations/meetings/ (Agency, confidential:true). Extract three sections: Decisions (what was decided + by whom), Actions (owner, task, due date if stated), and Metrics mentioned (figure, what it measures, source = this meeting, confidence: reported). Keep the cleaned full transcript below the summary.
   - Interview, voice memo, or content raw: write the cleaned transcript to Inbox/ for triage (Solo/Team) or the active client's Inbox path (Agency), with a one-line note on the suggested canonical home.
7. Extract actions and metrics conservatively. Only list an action if an owner or task is stated; only list a metric if a number was actually spoken. Do not infer targets or assign owners that were not named.
8. Ledger: if the meeting stated a real metric movement (a baseline and a current, or a current against a known prior), append one row per metric to the ledger. If a number was mentioned with no comparison point, record it in the note's Metrics section but do not invent a ledger baseline.

## Outputs
- Meeting, Solo/Team: `Operations/meetings/{date}-{slug}.md` (status:draft; Decisions, Actions, Metrics, then cleaned transcript).
- Meeting, Agency: `Clients/{slug}/operations/meetings/{date}-{slug}.md` (same structure, confidential:true).
- Interview / voice memo / content raw: `Inbox/{date}-{slug}-transcript.md` (Solo/Team) or the active client's Inbox path (Agency, confidential:true), with a suggested canonical home.
- Ledger row(s), only when a meeting stated a real metric movement, append-only, exact columns, never edit prior rows:
  - Solo/Team: `Memory/kpi-ledger.md`
  - Agency: `Clients/{slug}/goals.md`
  - Example: `| 2026-06-18 | trial signups | 120 | 145 | 200 | q3-pipeline-sync meeting | reported | figure cited by ops lead, not yet confirmed in analytics |`
- Audit line in `_system/audit/` for any external transcription call.

## Guardrails
- DRAFT-ONLY: status:draft on every file. Never publish, send, post, or contact anyone. A human reviews before any of it is shared.
- PROVENANCE: keep every quote, name, and number exactly as spoken; mark gaps as [inaudible]; never invent words, attendees, or figures. State that the transcript is machine or provided and unverified.
- CONNECTOR: transcription runs only through an active connector registered in _system/connectors.md; credentials stay in a secret manager; log the external read to _system/audit/. If no connector and no transcript, stop and ask.
- FIREWALL (Agency): read and write only the active client's workspace; never read a sibling; outputs confidential:true.
- LEDGER: append-only with exact columns and confidence in {confirmed,reported,inferred,stale}; never edit or reorder prior rows; add a row only when a real metric movement was stated.
- VOICE: brand voice is used only to remove filler and tidy phrasing, never to alter meaning. Route to canonical homes; kebab-case slugs; ISO dates; universal frontmatter on every .md.

## References
- _system/connectors.md, _system/audit/
- Operations/meetings/, Inbox/ (Agency: Clients/{slug}/operations/meetings/, Clients/{slug}/ Inbox path)
- Memory/kpi-ledger.md (Agency: Clients/{slug}/goals.md)
- Library/styles/brand-voice.md, Company/brand.md (Agency: Clients/{slug}/context/brand.md)
