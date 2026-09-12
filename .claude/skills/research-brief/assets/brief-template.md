# Research Brief Template

Fill from Gates 0–4. The filled result is the **entire** contents of
`research/prompt.txt` — it is the canonical research query, gospel for every
pipeline step.

## Rules for filling it

- **Only the user's content.** Every claim traces to something they said. Where
  they were unsure, write the uncertainty down — do not resolve it for them.
- **Drop empty sections.** A skipped gate's section is removed, and the omission
  is recorded on the `Method` line. Never leave a heading with placeholder text.
- **Research questions are the payload.** Every `unsure`, `unknown`, and
  `needs evidence` item from Gates 1–4 becomes a numbered question. This is what
  the pipeline actually goes and answers.
- **No pipeline instructions here.** Save paths, citation style, tier, and
  section requirements are wrapper concerns and belong in the scaffold or
  `wrapper_contract.json`. The query is the research question only.
- **Keep the German phase labels.** They are the canonical names and they anchor
  the brief to the framework the user works in.

---

```markdown
# <One-line research question — the thing that must be answered>

Method: first-principles deconstruction (Gates 0–4)<, omitting: ...>
Audience: <who reads the report and what decision it informs>

## AUSGANGSSITUATION

<Confirmed problem statement from Gate 0. What is happening, what has been
tried, what "solved" looks like, which constraints are non-negotiable.>

## Fundamentale Wahrheiten (Phase 1 — Dekonstruktion)

Objectively true, independent of convention:
- <component or law>
- <component or law>

Necessary vs. conventional:
| Element | Verdict | Rationale |
|---|---|---|
| <element> | necessity / convention / unsure | <one line> |

## Arbiträre Annahmen (Phase 2 — Annahmen-Check)

| Assumption | Verdict | What would settle it |
|---|---|---|
| Costs X because ... | arbitrary / load-bearing / unknown | <evidence needed> |
| Takes Y because ... | arbitrary / load-bearing / unknown | <evidence needed> |
| Works this way because ... | arbitrary / load-bearing / unknown | <evidence needed> |

## Neuaufbau von Null (Phase 3)

Solution shape derived only from Phase 1 truths:
<description>

Minimum necessary: <resources> | <process> | <time>

Radical divergences from the current solution:
- <divergence, and which standard component it drops, and why that is safe>

## Implementierung (Phase 4)

Barriers, classified:
| Barrier | Real or "immer so gemacht" | Notes |
|---|---|---|
| <barrier> | real / convention | <one line> |

Cheapest prototype test: <description>
Disruptive case if followed through: <description>

## Research questions

Every question the deconstruction could not settle from the user's own
knowledge, most decision-critical first:

1. <question>
2. <question>
3. <question>

## Scope boundaries

In scope: <what the report must cover>
Out of scope: <what it must not spend sources on>
Known non-negotiables: <constraints that survive regardless of findings>

## What a good answer looks like

<How the user will judge the report: the decision it must support, the level of
evidence that would change their mind, what would make it useless.>
```

---

## Appendix rendering

The final report must end with the appendix declared in
`wrapper_contract.json`. Expected shape:

````markdown
## Appendix A — Research Brief

The verbatim canonical query that drove this run, as approved before launch.

```markdown
<exact contents of research/prompt.txt>
```

Brief approved <UTC timestamp> · archived at `research/briefs/<timestamp>.md`
````

The fenced block is a byte-for-byte copy. Any drift between it and
`research/prompt.txt` is a transparency failure and must be reported as one.
