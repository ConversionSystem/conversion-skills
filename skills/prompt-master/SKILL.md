---
name: prompt-master
description: Write or sharpen a reusable prompt for any task with role, context, constraints, output shape, and a test case, saved to your library. Use when you say write me a prompt, improve this prompt, or make a reusable prompt.
---

# Prompt Master
Turn a fuzzy ask into a tight, reusable prompt: role, context, constraints, output shape, and a worked test case. Saves to Library/prompts/ so you run it again instead of rewriting it.

## When to use
- You keep retyping the same request and want one prompt you trust.
- A prompt you have is vague, drifts, or returns the wrong shape.
- You are handing a repeatable task to a teammate or to a scheduled run.

## Inputs
- The task in one sentence (what good output looks like).
- Optional: a draft prompt to improve.
- Optional: 1 or 2 real examples of the input and the ideal output.
- Voice reference: Library/styles/brand-voice.md.
- Context, if the prompt should know your business: Company/profile.md, Company/offers.md, Company/icp.md.

## Process
1. Read Library/styles/brand-voice.md so the prompt and its outputs match house voice.
2. Restate the task in one sentence. If the goal is unclear, ask one question, then proceed.
3. If improving an existing prompt, read it and name 3 concrete weaknesses (vague role, missing context, no output shape, no failure handling).
4. Draft the prompt in five blocks, in this order:
   - Role: who the model is and the bar it holds.
   - Context: the facts it needs, plus which vault files to pull from at run time.
   - Task: the exact job, as a numbered set of steps when order matters.
   - Constraints: length, voice, what to avoid, what to never invent, when to ask before guessing.
   - Output shape: the literal format (headings, fields, table columns, or a fenced example block).
5. Write one test case: a sample input and the exact ideal output it should produce. This is the prompt's spec.
6. Add a one-line "fails if" note: the single mistake that means the prompt is wrong (wrong format, invented numbers, off voice).
7. Slugify the task name. Save to Library/prompts/{slug}.md with the prompt, the test case, and a short "how to run" line.
8. If a near-identical slug exists, read it, fold in the improvement, and keep one file rather than two.

## Outputs
- Library/prompts/{slug}.md, holding: the five-block prompt, one test case (input plus ideal output), a "fails if" line, and a one-line run note.
- If you revised an existing prompt, the same path, updated in place, with a dated one-line changelog at the bottom.

## Guardrails
- DRAFT-ONLY. This writes a prompt to your library, it does not send or publish anything.
- VOICE comes from Library/styles/brand-voice.md. No em-dashes, no filler.
- PROVENANCE. Prompts that touch metrics must instruct the model to cite the source and never invent a number.
- The prompt names the vault files to read at run time rather than baking in stale facts.
- Keep one prompt per task. Merge duplicates, do not fork them.

## References
- Library/styles/brand-voice.md
- Company/profile.md, Company/offers.md, Company/icp.md
