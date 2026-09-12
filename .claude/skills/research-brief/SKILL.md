---
name: research-brief
description: Interrogate the user with a mandatory human-in-the-loop interview to build a rigorous first-principles research brief, then install it as the canonical hyperresearch query and launch the run with the brief embedded verbatim in the final report. Use when the user wants to start a deep research run, sharpen a vague research question, write a research prompt or brief, apply first-principles deconstruction to a problem, or types /research-brief. Do NOT use for answering a question directly, for a single web lookup, or once a run is already in flight.
---

# Research Brief

Turns a half-formed research idea into a canonical, auditable prompt for the
hyperresearch pipeline. The user does the thinking; you do the interrogation,
structuring, and wiring.

**CLI path: `.venv/bin/hyperresearch`** (relative to the repo root). Referred to
below as `$HPR`. Append `-j` for structured output.

## Why this skill exists

hyperresearch treats the canonical query as **gospel** — every one of the 16
pipeline steps, and every subagent, inherits it verbatim. A vague prompt is not
recoverable downstream: it produces a fluent report that answers the wrong
question after 30+ minutes and real API spend. The brief is the single highest-
leverage artifact in the run, so it gets built deliberately and signed off
explicitly before anything is spawned.

---

## Hard rules

These are not stylistic preferences. Violating any of them defeats the skill.

1. **NEVER write the brief for the user.** You draft *candidate* answers to make
   responding cheap, but every phase requires the user to confirm, correct, or
   replace. Silence is not consent. An unanswered question is a blocker.
2. **NEVER skip a gate**, including when the user is terse, impatient, or says
   "just do it". If they want fewer phases, they must say which ones to drop —
   see [Escape hatches](#escape-hatches). Record what was skipped.
3. **NEVER launch the pipeline before explicit approval** of the assembled brief
   at Gate 5. Approval means the user affirms the final text, not that they
   stopped objecting.
4. **The approved text is immutable.** After Gate 5, do not "improve" wording,
   fix typos, or reformat. It is copied byte-for-byte into `research/prompt.txt`
   and into the report appendix. If it needs a change, reopen Gate 5.
5. **Interview in the user's language.** If they write German, ask in German.
   The phase labels below stay as-is; they are the canonical names.
6. **One phase per message.** Do not dump all four phases at once — that
   produces skimmed, low-quality answers and defeats the interrogation.

---

## Workflow

Track progress with the task tools so the user can see where they are. Seven
gates: 0 → 1 → 2 → 3 → 4 → 5 (approval) → 6 (launch).

### Gate 0 — AUSGANGSSITUATION

Ask for a thorough description of the problem. Prompt for what a stranger would
need to know: what is happening, what they have tried, what "solved" looks like,
what constraints are non-negotiable, who the audience for the answer is.

Then reflect back a 3–5 sentence restatement and ask: *"Is this the problem, or
have I drifted?"* Do not proceed until they confirm or correct it.

**Deliverable:** a confirmed problem statement.

### Gate 1 — DEKONSTRUKTION

> Was ist fundamental wahr — nicht was ist üblich?

Work through these three with the user, drafting candidates for each:

1. **Fundamental components.** What is objectively, factually true about this
   problem? Explicitly set aside "best practices", "so macht man das", and
   industry standards. What is physically, factually, or logically necessary?
2. **Invariant laws.** Which unchangeable truths govern this? Consider physical
   laws, psychological principles (how people actually learn and behave),
   economic fundamentals (supply/demand, where value is actually created), and
   pure logical necessities.
3. **Necessary vs. conventional.** Separate genuine requirements from
   convention. For each item, ask: is this tradition or necessity?

Present your candidates as a table with a `necessity | convention | unsure`
column and have the user adjudicate each row. The `unsure` rows are the
interesting ones — they usually become research sub-questions.

### Gate 2 — ANNAHMEN-CHECK

> Which assumptions of the current solution are actually arbitrary?

Push on the three "why" questions. Do not accept the first answer:

- **Why does it cost X?** Which costs are genuinely unavoidable?
- **Why does it take Y?** What is physically necessary time vs. process overhead?
- **Why does it work this way?** Which steps are logically compelled?

For each assumption the user names, ask them to rate it `arbitrary`,
`load-bearing`, or `unknown`. Every `unknown` is a candidate research question —
these are frequently the highest-value part of the whole brief.

### Gate 3 — NEUAUFBAU

> Starting from zero, using only the Phase 1 truths.

1. **What would the solution look like** with no regard for how it is currently
   done — based only on what must logically, physically, or psychologically
   happen?
2. **Which components are genuinely required?** Minimum necessary resources,
   minimum necessary process, minimum necessary time.
3. **What is radically different** from the current solution? Where does the
   first-principles approach diverge sharply? Which "standard components" are
   absent — and why are they not necessary?

Where the user cannot answer without evidence, capture it as a research question
rather than letting them guess. That is the point of the exercise: the gaps
become the research scope.

### Gate 4 — IMPLEMENTIERUNG

1. **Which barriers** sit between the first-principles solution and reality? For
   each, force the call: real barrier, or "das haben wir immer so gemacht"?
2. **How could it be prototyped** and tested cheaply?
3. **What is the disruptive innovation** if the first-principles logic is
   followed all the way through?

### Gate 5 — Assembly and approval (MANDATORY)

Read `assets/brief-template.md` and fill it from Gates 0–4. Then:

1. Present the **complete** brief in a fenced block. Never a summary or a diff —
   the user must approve the exact bytes that will drive the run.
2. State plainly what happens next and what it costs: *"This launches a run at
   the `<gear>` gear, roughly `<time estimate>`. The brief below is gospel for
   every step. Approve, or tell me what to change."*
3. Then ask for a decision with `AskUserQuestion`, offering: **Approve and
   launch** / **Revise a phase** (which one?) / **Save the brief without
   running**.
4. On revision, return to that gate and come back to Gate 5. Loop until
   approved. There is no iteration limit.

Get the gear and time estimate from `$HPR profile list -j` — read the entry with
`current_gear: true`. Do not hardcode them; the installed gear changes.

### Gate 6 — Install and launch

Only after explicit approval.

1. **Write the canonical query.** The brief text goes to `research/prompt.txt`,
   byte-for-byte. The router reads this file first and treats it as GOSPEL,
   overriding any wrapping instructions.

2. **Write the transparency contract** to `research/wrapper_contract.json`:

   ```json
   {
     "required_terminal_sections": ["## Appendix A — Research Brief"],
     "source": "research-brief skill"
   }
   ```

   `hyperresearch lint` reads `required_terminal_sections` and raises a
   `wrapper-report` **error** when a declared heading is missing from the final
   report. That check is what makes the transparency requirement binding rather
   than aspirational.

   **Heading collision warning:** the heading must not begin with
   `## User Prompt (VERBATIM` — that string is in `SCAFFOLD_ONLY_SECTION_HEADERS`
   and lint errors if it appears in a report body. Matching is plain substring,
   so keep the appendix heading exactly as written above.

3. **Preserve an immutable copy** at `research/briefs/<UTC-timestamp>.md`, so the
   brief survives a later run overwriting `research/prompt.txt`.

   Write it **without YAML frontmatter**. Vault sync walks `research/**.md` and
   indexes anything carrying frontmatter; a brief with frontmatter would be
   ingested as a research note and distort source counts. No frontmatter means
   sync skips it as a scratch artifact, which is what we want.

4. **Launch** by invoking the `hyperresearch` skill via the `Skill` tool. It
   reads `research/prompt.txt` on its own — do not paste the brief into the
   invocation, which would create a second, divergent copy of the query.

5. **Tell the synthesizer where the appendix comes from.** After the run mints
   its `vault_tag`, append to `research/runs/<vault_tag>/scaffold.md`:

   ```markdown
   ## Wrapper requirement — brief appendix
   The final report MUST end with `## Appendix A — Research Brief`, containing
   the full verbatim contents of `research/prompt.txt` in a fenced block, plus
   the one-line provenance footer. Do not paraphrase, summarize, or reformat it.
   ```

   Wrapper requirements belong in the scaffold, not in the query — the query is
   the research question only.

### After the run

Verify the transparency requirement actually held:

```bash
$HPR lint -j          # wrapper-report rule: appendix present?
$HPR run verify -j    # headings, length, citation density, cite-check
```

If lint reports a missing appendix, the report is incomplete. Fix it with a
surgical `Edit` appending the appendix — never regenerate the report.

Then confirm the copy is faithful:

```bash
diff <(sed -n '/^## Appendix A — Research Brief/,$p' \
        research/notes/final_report_<vault_tag>.md | sed -n '/^```/,/^```/p' \
        | sed '1d;$d') research/prompt.txt
```

Report the outcome plainly. A drifted appendix is a transparency failure and
must be reported as one, not quietly corrected.

---

## Escape hatches

The gates are mandatory by default, but the user governs their own process.

- **"Skip the first-principles phases"** — allowed. Run Gates 0 and 5 only.
  Note the omission in the brief's `Method` line so the report records that the
  deconstruction was not performed.
- **"I already have a prompt"** — do not discard it. Run it through Gate 5 as-is
  and offer, once, to strengthen it. If they decline, install it verbatim.
- **"Just research X"** with no appetite for an interview — say in one sentence
  that the brief materially improves the result, then respect their answer. Do
  not ask twice.

Record any skipped gate in the brief. An undocumented shortcut is the one
outcome this skill must never produce.

## Failure modes to avoid

| Symptom | Why it is wrong |
|---|---|
| Filling gaps with your own plausible answers | The brief stops being the user's, and the run researches your assumptions |
| Compressing all phases into one question | Produces skimmed answers; the deconstruction adds nothing |
| Launching on "sounds good" to a summary | They approved your summary, not the actual query bytes |
| Editing the brief after approval | Breaks the audit trail between `prompt.txt` and the appendix |
| Pasting the brief into the skill invocation | Creates a second query copy that can silently diverge |
| Treating `unsure` / `unknown` items as noise | Those are the research questions; they are the yield of the exercise |
