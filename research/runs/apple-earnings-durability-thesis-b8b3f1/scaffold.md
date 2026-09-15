# Scaffold — apple-earnings-durability-thesis-b8b3f1

WORKSPACE ARTIFACT. Must not appear anywhere in the final report.

## Canonical research query source

`research/prompt.txt` (wrapped run, produced by the `research-brief` skill).
GOSPEL. Persisted verbatim at
`research/runs/apple-earnings-durability-thesis-b8b3f1/query.md`.

## Run config

| Field | Value |
|---|---|
| vault_tag | `apple-earnings-durability-thesis-b8b3f1` |
| query_file_path | `research/runs/apple-earnings-durability-thesis-b8b3f1/query.md` |
| profile / gear | `full` (55–80 sources, ~1.5–2.5 h) |
| modality | synthesize (secondary flavor: forecast) |
| budget | none set |

## Modality classification rationale

**synthesize.** The query asks for a defended thesis with evidence chains — a
quantified durability decomposition leading to a committed verdict on whether
the headline multiple is misleading. It is not enumerative (collect), and the
comparison it makes is between earnings *classes* inside one company, not
between entities (compare).

Secondary flavor **forecast**: the 2–5 year horizon requires predictive claims
about remedy timelines, replacement cycles and services growth, grounded in
present evidence with an explicit time horizon.

## Tier rationale

**`full` + `argumentative` + `inline`.**

Full tier is unambiguous here: the query demands a defended thesis over
contested evidence, explicitly names an even-handed survey as a *failed*
report, and requires the pipeline to adjudicate and commit where sources
disagree. That is the argumentative case the adversarial steps exist for.

`inference_depth: deep` rather than standard, because the central question
requires inference over absences. Apple does not disclose Google TAC or App
Store commission revenue as separate lines, so the durability decomposition
cannot be read off a filing — it has to be reconstructed from court-surfaced
discovery figures, regulatory findings and gray literature, with stated
estimation methods and ranges.

`register: analyze` at high confidence. The query is evaluation-shaped ("knows
which the evidence actually favours"), but stops short of `advocate`: it
forbids a buy/sell/hold recommendation and attaches no course of action.

Coverage-matrix pass 1 found three gaps, now fixed: supply chain/geopolitics
had no atomic item despite being one of four named in-scope angles;
"regulatory and legal exposure" had been narrowed to Google TAC alone; and the
return identity's third term (shareholder returns/buybacks) was unmapped.

## Session wrapper requirements

Binding, but NOT part of the research query:

1. **Terminal section (lint-enforced).** `research/wrapper_contract.json`
   declares `required_terminal_sections: ["## Appendix A — Research Brief"]`.
   `hyperresearch lint` raises a `wrapper-report` error if it is missing.
   The final report MUST end with `## Appendix A — Research Brief`, containing
   the full verbatim contents of `research/prompt.txt` in a fenced block, plus
   a one-line provenance footer. Do not paraphrase, summarize, reformat — and
   do NOT translate the appendix, even though the report body is German.

   Heading collision warning: the heading must NOT begin with
   `## User Prompt (VERBATIM` — that string is in
   `SCAFFOLD_ONLY_SECTION_HEADERS` and lint errors if it reaches a report body.

2. **Output language: GERMAN.** The entire report body is written in German.
   Technical/financial terms stay in English where the German equivalent is
   unusual (Traffic Acquisition Cost, Free Cash Flow, Services Revenue, Gross
   Margin). Sources are read in ANY language — do not restrict the search to
   German, which would discard nearly all the evidence. Quotations are
   translated into German with the English original alongside.

   hyperresearch has no output-language lever (levers are only register /
   inference_depth / domain_notes), so the requirement travels in the query.
   Every subagent receives it via the verbatim query. Restated here because
   the scaffold is what the synthesizer reads while writing.

3. **Citation style:** inline `[N]` markers plus a `## Sources` section
   (`citation_style: inline`).

4. **Save path:** `research/notes/final_report_apple-earnings-durability-thesis-b8b3f1.md`

5. **Structure:** follow the durability frame — earnings decomposition →
   multiple decomposition → binary events → the reader's two tested priors →
   verdict. NOT a conventional product-segment walkthrough.

6. **Register:** informed technical investor. No basic explanations.

7. **Length:** whatever the evidence supports.

## Sourcing posture (from the query's Phase 4)

Prefer PRIMARY sources — 10-K/10-Q filings (SEC EDGAR), court records,
regulatory documents — over analyst commentary, which imports the
product-segment frame the query explicitly rejects. EDGAR is live and verified
this session.

## Two reader priors that MUST be tested, not accommodated

1. Late-follower status in AI is currently an ADVANTAGE (capital-allocation
   efficiency vs. the capex arms race).
2. Apple's payments business (Apple Pay, App Store commissions) faces
   near-term disruption from crypto/AI payment rails.

**Critical distinction the report must preserve:** the Google search-placement
fee (TAC) is NOT a payment service. Payment-rail disruption does not touch it.
Conflating the two is named in the query as a failure condition.

## Orchestrator notes

- No TodoWrite/Task tools in this session. The run manifest
  (`hyperresearch run step <tag> <N> --status running|done -j`) is the durable
  memory and the primary recovery path.
- `archive-run` at bootstrap 0.5 MOVED `research/wrapper_contract.json` into
  `research/runs/archive-20260912T155154Z/` before bootstrap step 1 could read
  it. Restored to the research root. Ordering flaw worth fixing in the
  `research-brief` skill (it stages the contract at a path a later run's
  archive-run will sweep).
