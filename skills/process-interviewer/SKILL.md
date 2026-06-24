---
name: process-interviewer
description: Interview the user step by step to capture how a process actually runs, then hand a clean process to sop-create, triggered by "interview me on this process", "document my workflow", or "capture this process"
---

# Process Interviewer

Walk the user through a guided interview that pulls a process out of their head one step at a time, then write a clean, ordered process file that sop-create can turn into a finished SOP.

## When to use
- A process lives only in someone's head and needs to be written down before it can become an SOP.
- An existing process is messy, partial, or out of date and you want a clean capture by asking instead of guessing.
- You want sop-create to run against a verified, ordered set of steps rather than a rough brain dump.
- Onboarding a new hire and you need the experienced operator to narrate how the work really gets done.

## Inputs
- The process name or goal in one line (what finished looks like).
- The operator or owner who actually runs the process and can answer questions.
- Optional: any rough notes, checklists, or screenshots the user already has.
- Optional: the existing draft at Operations/processes/{slug}.md if this is a re-capture.

## Process
1. Confirm the one-line goal and who owns the process. Derive a kebab-case {slug} from the goal (for example "month-end-close").
2. Ask for the trigger: what event or signal starts this process, and how often it runs.
3. Ask for the end state: what exists or is true when the process is done, and who confirms it.
4. Walk the steps in order. For each step, ask four questions: what action is taken, who takes it, what tool or file it touches, and how you know the step is finished. Capture one step per answer, then ask "what happens next" until the user reaches the end state.
5. Confidence read. Ask only the single highest-leverage question at a time, the one that most reduces your uncertainty about the user's intent (what they actually want this process to achieve), not just the next surface fact. With each question, carry your current best-guess answer and a confidence percent about that underlying intent. Show both inline, for example "Best guess: this kicks off when the invoice lands in the shared inbox. Confidence in intent: 70 percent. Highest-leverage question: who is allowed to start it before that?" Update the percent after every answer so the user watches it climb.
6. Stop rule. Keep asking the one highest-leverage question until confidence about intent reaches about 95 percent or the user calls it ("good enough", "stop", "that's it"). Once you are confident, stop. Do not pad with low-value questions to look thorough; a low-leverage question that would not move the percent is a signal you are done. If the percent stalls and will not climb, say so and ask the user whether to push on or call it.
7. After each step, read it back in one sentence and ask the user to confirm or correct before moving on.
8. Probe the gaps: ask about decision points (if X then Y), handoffs between people, waiting periods, and the most common failure or rework point.
9. Collect inputs and outputs: every file, form, or piece of data the process needs to start, and every file or result it produces.
10. Ask for the time and frequency: rough minutes per step and how often the whole process runs, so the SOP can flag the slow parts.
11. Read the full ordered list back to the user. Mark any step the user was unsure about as "needs review" so it is not lost.
12. Write the captured process to Operations/processes/{slug}.md using the structure in Outputs.
13. Offer the handoff: tell the user the file is ready and ask whether to run sop-create against Operations/processes/{slug}.md now.

## Outputs
- Operations/processes/{slug}.md with: goal (one line), owner, trigger and frequency, end state, ordered steps (each with action, owner, tool or file, done-when), decision points, handoffs, inputs, outputs, and an open-questions list of anything marked "needs review".
- A one-line status to the user naming the file path, the count of steps captured, and the final confidence percent about intent (or "user called it at N percent" if they stopped early).
- No KPI ledger row. This skill captures a process, it does not move a metric.

## Guardrails
- Ask, do not assume. If the user does not know a step, write "needs review" rather than inventing the answer.
- One step at a time. Do not batch questions or jump ahead, and read each step back before moving on.
- Surface the running confidence percent with every question so the user can see when enough is enough. Stop at about 95 percent or when the user calls it; do not pad with low-value questions once you are confident.
- Capture the process as it actually runs today, not an idealized version. Note improvement ideas separately under open questions.
- Provenance: record who supplied each unclear step so it can be verified later. Never invent owners, tools, or timings.
- Write only to Operations/processes/{slug}.md. Do not create the SOP yourself; that is sop-create's job.
- If a draft already exists at that path, show the user a diff in plain language and confirm before overwriting.

## References
- sop-create (consumes Operations/processes/{slug}.md to produce the finished SOP)
- Operations/processes/ (where captured processes live)
- _system/rules (voice and draft-only guardrails)
