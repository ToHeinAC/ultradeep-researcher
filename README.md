# ultradeep-researcher

An agent-driven deep research workspace. It exists to make one thing hard to get
wrong: **the question you actually asked.**

Research pipelines fail quietly. Given a vague prompt they return a fluent,
well-cited report that answers something adjacent — after 30+ minutes and real
API spend. There is no error to catch, because nothing errored. So this
workspace splits the work into two stages and puts a human gate between them.

```
   Stage 1                         Stage 2
   /research-brief                 /hyperresearch
   ─────────────────────────       ──────────────────────────────
   First-principles interview      16-step adversarial pipeline
   You answer, Claude structures   Search → fetch → analyse →
            ↓                      draft → critique → patch → polish
   You approve the exact text               ↓
            ↓                      Detailed report in your language
   research/prompt.txt (gospel) ──▶ with the brief attached verbatim
```

Stage 1 is deliberately slow and interrogative. Stage 2 is fully automatic. The
gate between them is the point: nothing is spawned until you have signed off on
the literal bytes of the query.

---

## Stage 1 — Build the brief

```
/research-brief
```

Eight gates. One phase per message. Claude drafts candidate answers so replying
is cheap, but never answers on your behalf.

| Gate | Name | Produces |
|---|---|---|
| 0 | AUSGANGSSITUATION | Confirmed problem statement |
| 1 | DEKONSTRUKTION | Fundamental truths, separated from convention |
| 2 | ANNAHMEN-CHECK | Assumptions rated arbitrary / load-bearing / unknown |
| 3 | NEUAUFBAU | The solution rebuilt from zero |
| 4 | IMPLEMENTIERUNG | Barriers, prototype, disruptive case |
| 4.5 | AUSGABE | Language, register, length, citation style |
| 5 | **Approval** | You approve the exact text, or send it back |
| 6 | Launch | Brief installed, pipeline started |

The yield of the deconstruction is the *gaps*. Everything you mark `unsure` or
`unknown` becomes a numbered research question — those are what Stage 2 goes and
answers. A brief with no unknowns means you did not need research.

Gates are skippable if you say so, but a skipped gate is recorded in the brief.
Undocumented shortcuts are the one outcome the skill will not produce.

## Stage 2 — Run the research

Launching is automatic at Gate 6. The approved brief lands in
`research/prompt.txt`, which the pipeline treats as **gospel** — inherited
verbatim by all 16 steps and every subagent.

Step 1 classifies the query into a tier, and the pipeline scales itself:

| Tier | Steps | Time |
|---|---|---|
| `light` | 5 — single draft, no critics | ~30–40 min |
| `full` | 17 — triple draft, four critics, patcher, cite-check | longer |

The installed **gear** sets the source budget on top of that. This workspace
ships at the `fast` gear (15–25 sources). Check and change it with:

```bash
.venv/bin/hyperresearch profile list -j
.venv/bin/hyperresearch profile use <gear>
```

Output lands at `research/notes/final_report_<vault_tag>.md`.

### Language

The report is written in whatever language the brief specifies; sources are read
in **any** language. That split is deliberate — restricting the search to the
report's language throws away most of the evidence.

There is no language setting to configure. hyperresearch's levers are only
`register`, `inference_depth`, and `domain_notes`, so the language requirement
travels inside the query itself. Gate 4.5 exists to make sure it is in there. If
you bypass the brief and prompt the pipeline directly, say the language in your
prompt or you will get English.

### Transparency

Every report carries the brief that produced it, at
`## Appendix A — Research Brief`, byte-for-byte. This is enforced, not
requested: `research/wrapper_contract.json` declares the heading, and
`hyperresearch lint` raises an error if it is missing.

```bash
.venv/bin/hyperresearch lint -j          # appendix present?
.venv/bin/hyperresearch run verify -j    # headings, length, citations, cite-check
```

---

## Setup

Requires [uv](https://docs.astral.sh/uv/) and Python 3.11–3.13.

```bash
uv sync
uv run python scripts/patch_edgar_ua.py   # required — see Known issues
```

Create `.env` for credentials (gitignored):

```bash
HYPERRESEARCH_CONTACT_EMAIL=you@example.com   # SEC EDGAR + polite-pool access
FRED_API_KEY=...                              # optional, economic time series
CORE_API_KEY=...                              # optional, open-access full text
```

The CLI reads the process environment and does **not** load `.env` itself:

```bash
set -a; . ./.env; set +a
```

For Claude Code sessions, mirror the same values into the `env` block of
`.claude/settings.local.json` (also gitignored) so tool calls inherit them.

### Scholarly sources

| Source | Covers | Needs |
|---|---|---|
| OpenAlex | ~250M works, all fields, incl. books | — |
| Crossref | DOI registry, ~160M works | — |
| DOAB | Open-access scholarly books | — |
| ClinicalTrials.gov | Trial registrations | — |
| SEC EDGAR | US filings since 2001 | contact email |
| FRED | Economic time series | `FRED_API_KEY` |
| CORE | OA full text, ~30k repositories | `CORE_API_KEY` |
| RePEc | Economics working papers | unavailable — no search API exists |

Academic sources are queried **before** web search. They return citation-ranked
canonical work; web search returns commentary about it.

## Known issues

**SEC EDGAR requires a local patch.** The SEC rejects any User-Agent containing
a URL, and hyperresearch hardcodes its GitHub URL into every request. EDGAR then
returns zero results while still reporting itself available — a silent failure.
`scripts/patch_edgar_ua.py` fixes it and is idempotent. Re-run it after any
package upgrade or environment rebuild. Full diagnosis:
[docs/edgar-ua-patch.md](docs/edgar-ua-patch.md).

## Layout

```
.claude/skills/research-brief/   Stage 1 — the HITL brief builder
.claude/skills/hyperresearch*/   Stage 2 — router + 18 step skills
.claude/agents/                  16 pipeline subagents
research/prompt.txt              Canonical query (gospel)
research/briefs/                 Immutable brief archive
research/notes/                  Final reports
research/runs/<vault_tag>/       Per-run workspace and manifest
docs/                            Component documentation
scripts/                         Maintenance scripts
```

Collaboration rules for AI coding tools live in [AGENTS.md](AGENTS.md);
[CLAUDE.md](CLAUDE.md) imports them and adds Claude Code specifics.

## License

Apache-2.0. `hyperresearch` is MIT.
