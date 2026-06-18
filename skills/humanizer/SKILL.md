---
name: humanizer
description: Rewrite machine-sounding text into the business's own voice from Library/styles/brand-voice.md, cut the AI tells, keep every fact, and return a draft
---

# Humanizer

Take text that reads like a machine wrote it and rewrite it in the business's voice. Cut the tells, keep the facts, ship a draft.

## When to use
- A draft sounds generic, padded, or stiff and you want it to sound like the business.
- You pasted output from another tool and need it to match the house voice.
- Copy is heading outbound or to publish and must pass the brand rules first.
- Triggers: "humanize this", "make this sound like us", "rewrite in our voice", "de-AI this copy", "cut the AI tells".

## Inputs
- The text to rewrite (pasted in, or a path to a file under Inbox/, Content/, or Projects/).
- Library/styles/brand-voice.md, the voice source. If it is missing, say so and rewrite to the brand rules in CLAUDE.md only.
- Optional: the audience and the channel (email, page, post), so word choice and length fit.

## Process
1. Read Library/styles/brand-voice.md. Note the voice rules, the words the business uses, the words it bans, sentence length, and reading level.
2. Read CLAUDE.md and _system/rules for the hard brand rules, no em-dashes, no blocklist words, numbers not adjectives, verbs not nouns.
3. Read the input text. Mark the facts, the numbers, the claims, and the calls to action. These stay.
4. Mark the tells: padding, hedging, throat-clearing intros, stock transitions, repeated sentence shapes, vague adjectives, passive voice, words on the blocklist, em-dashes.
5. Rewrite. Keep every fact and number from step 3. Cut every tell from step 4. Match the voice from step 1. Replace each banned word with a plain one. Replace em-dashes with commas, periods, parentheses, or the middot.
6. Check sources. If the original cited a metric, keep the citation. Never invent a number to fill a gap.
7. Self-check the rewrite against the brand rules: scan for em-dashes, scan for each blocklist word, confirm the facts survived. Fix any miss before you return it.
8. Return the rewrite as a draft. Do not send it and do not publish it. If the input came from a file, write the rewrite next to it as a new draft and leave the original alone.

## Outputs
- The rewritten text, returned in chat as a draft.
- If the input was a file, a sibling draft written to the same folder, named `{original}-humanized.md` (for example Content/launch-2026-06-18/post-humanized.md). The original file is untouched.
- A short change list under the rewrite: tells cut, words swapped, facts kept.
- No ledger row. This skill does not touch Memory/kpi-ledger.md.

## Guardrails
- DRAFT-ONLY. Outbound and published copy stays a draft until a person approves it.
- VOICE comes from Library/styles/brand-voice.md, not from invention.
- PROVENANCE: keep every cited source, never add a metric that was not in the input.
- Zero em-dashes. Zero blocklist words. Run the self-check in step 7 every time.
- Keep the facts. If a rewrite would change a claim or a number, stop and flag it instead.
- FIREWALL: if the text belongs to a client, work only inside that client's folder and only when it is the active client.

## References
- Library/styles/brand-voice.md
- CLAUDE.md
- _system/rules
