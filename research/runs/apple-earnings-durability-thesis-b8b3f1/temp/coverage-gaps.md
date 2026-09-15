# Coverage gaps — apple-earnings-durability-thesis-b8b3f1

## Wave 1 outcome

12 fetchers dispatched against 70 URLs. 7 completed; 5 terminated by an API
session limit (batches 4, 8, 9, 11, 12) — but fetchers write notes
incrementally, and all five had landed most of their work before dying.

Vault after wave 1: **86 notes, 84 substantive** after cleanup (target 55–80).

Cleanup performed:
- Deprecated 2 EDGAR navigation/index pages (not substantive).
- `united-states-district-court-2` is a second mirror of the same Doc. 1436
  remedies opinion as `united-states-district-court`. Tagged
  `duplicate-of-united-states-district-court`, NOT deprecated, so its extracted
  claims survive. Counted once.
- All three court opinions carried the identical useless title
  "UNITED STATES DISTRICT COURT"; disambiguated via summaries and
  `us-v-google-remedies` / `us-v-google-liability` tags, tier `ground_truth`.

Gaps were confirmed by probing the vault with full-body search, not assumed.
Hit counts on 10-K filings are inflated by boilerplate risk-factor language,
so near-zero results are the meaningful signal.

## Coverage by atomic item (after wave 1)

| Atomic item | Status | Independent sources | Notes |
|---|---|---|---|
| Q1 durability decomposition | well-covered | 10+ | 10-Ks FY22-25, 10-Qs FY26, 8-Ks, both court opinions, App Store notes |
| Q2 Google TAC remedy | well-covered | 8 | Both Mehta opinions (primary), KGI, Hughes Hubbard, TechPolicy, SEL, NTU, Quartz |
| Q3 late-follower AI | well-covered | 8 | 4 capex comparisons, 3 Siri-delay chronology, Gemini deal, Epoch AI inference cost |
| Q4 payment-rail disruption | well-covered | 7 | Stablecoin x5 (conflict-of-interest tagged), Visa/Mastercard CEO quotes, DOJ NFC claim |
| Q5 multiple earned vs passive | adequate | 5 | Inelastic markets, Koijen, passive investing, Bouchaud critique, GIV. **Factor crowding UNCOVERED** — both crowding notes are abstract-only stubs (141/152 words) |
| Q6 lock-in / DMA | adequate (weak form only) | 8 | Full EC decision, browser choice-screen evidence. **Strong form (actual phone switching) UNCOVERED** |
| Q7 required services CAGR | adequate | 5 | 8-Ks, 10-Qs, macrotrends, valuation notes |
| Q8 multiple vs fundamentals 2-5y | adequate | 3 | Ferreira & Santa-Clara, Blitz/Robeco. Audited absence: no horizon-specific breakdown exists in either |
| Q9 replacement cycle | well-covered | 5 | Cycle-length data, iPhone statistics, iOS 27 supercycle case |
| Q10 silicon margin attribution | **UNCOVERED** | 1 weak | Single aggregator hit only |
| Q11 falsification test | adequate | computed | Derived from filings + court figures; provisional sizing in orchestrator notes |
| Q12 supply chain / geopolitics | thin | 4 | India assembly share covered. **Tariff quantification and value-added vs assembly THIN** |
| Q13 regulatory beyond TAC | well-covered | 7 | DOJ v. Apple x3, Epic contempt order, EC decision, DMA analyses |
| Q14 buybacks | thin | filings only | Amounts from 10-Qs; **durability / pro-cyclicality evidence UNCOVERED** |
| Q15 discount-rate sensitivity | **UNCOVERED** | 0 real | 10-K hits are boilerplate; no rate series, no equity-duration evidence |

**No atomic item has zero candidate sources after wave 2 is dispatched.**

## Wave 2 — gap fill (4 fetchers, ~28 URLs)

| Batch | Gap | Sources |
|---|---|---|
| W2-A | Q6 strong-form lock-in + **CEO transition** | CIRP loyalty data (87% Q1 2026), CIRP carrier-loyalty and switcher analyses, Cook/Ternus succession coverage |
| W2-B | Q10 silicon margin | SemiAnalysis Apple–TSMC, Digits to Dollars margin attribution (incl. contrarian "not about money"), C2 modem displacing Qualcomm |
| W2-C | Q12 tariffs + value-added | Q2/Q3 FY26 earnings-call transcripts, AEI supply-chain report, CEPR iPhone value-added, iPhone 16 BOM teardown |
| W2-D | Q5 crowding, Q14 buybacks, Q15 duration | Lettau & Wachter JF 2007, NBER w34814, Floyd/Li/Skinner JFE 2015, Payout Policy review, arXiv crowding, MSCI crowding, FRED DGS10/DFII10 |

SSRN deliberately avoided in wave 2 — it bot-walls the headless fetcher.
Journal DOIs, NBER and arXiv used instead.

## New first-order facts surfaced by gap searches (not in the brief)

1. **CEO transition.** Tim Cook stepped down Aug 31 2026; John Ternus (SVP
   Hardware Engineering) CEO from Sept 1 2026; Cook becomes executive chairman.
   Announced Apr 20 2026. A hardware engineer as CEO bears on both the AI
   strategy prior and the hardware/services mix.
2. **Valuation ~$5T**, not the brief's "~$3–4T". Strengthens the growth-decay
   argument in Phase 1.
3. **Q3 FY26 gross margin 50.1% includes ~2pp of non-recurring tariff refunds.**
   Q4 guidance 47–48% includes ~1pp more. Underlying margin is lower than
   headline and may contract as refunds lapse. Earlier orchestrator note
   claiming +680bp expansion overstates the underlying trend.
4. **China's value-added share of an iPhone is small and method-dependent.**
   ~$38.89 per iPhone 16 against a **$563.73 total landed cost** (Contractor/
   Rutgers) ≈ 7%; ~$104 of a **$409.25 BOM** for the iPhone X (Xing/CEPR,
   peer-reviewed) ≈ 25%. CORRECTED: an earlier version of this line paired
   $38.89 with the separate $416 TD Cowen iPhone 16 BOM — those are different
   quantities from different sources and must not be combined. Assembly share
   and value-added share are different quantities; the India shift moves
   low-value assembly.

## Escalations queued for step 2.8

SSRN bot-blocks (#4–#7), calawyers.org login wall (#8), law.justia.com
Cloudflare challenge on the D.N.J. DOJ v. Apple opinion (#9). Drain after
wave 2.

## Long sources for source-analyst delegation (cap 6)

| Note | Words | Why load-bearing |
|---|---|---|
| `united-states-district-court-3` | 89,290 | Liability opinion — $20B testimony, Alice-in-Wonderland bidder analysis |
| `united-states-district-court` | 74,310 | Remedies opinion — operative injunction, 6-year term |
| `european-commission` | 34,798 | Full DMA decision — steering obligations |
| `support-for-this-study-was-provided-by-apple` | 8,265 | Analysis Group — commissionable base methodology |

## Step 2.8 — escalation queue: NOT drained (deliberate)

10 items queued. Assessed individually:

| # | Item | Status | Marginal value |
|---|---|---|---|
| 1 | SSRN 3220842 Active World of Passive Investing | full text already in vault via another route | none |
| 4 | SSRN 5159811 Blitz decomposition | substituted (Robeco PDF) | low |
| 7 | SSRN 1363941 Ferreira & Santa-Clara | substituted (NBER full PDF) | none |
| 5 | SSRN 6087626 mega-cap archetypes | zero independent footprint | low, quality-flagged |
| 6 | SSRN 6730804 "BSVM™" terminal value | vanity/practitioner signature | low, quality-flagged |
| 8 | calawyers.org remedies commentary | redundant with Doc. 1436 + source-analysis | low |
| 10 | stockanalysis Qualcomm Q3 transcript | Qualcomm 8-K substitutes | low |
| 2 | SSRN 5023380 Dynamics of Factor Crowding | abstract only | **moderate** |
| 3 | SSRN 3803954 Crowding and Factor Returns | abstract only | **moderate** |
| 9 | D.N.J. DOJ v. Apple opinion (justia) | Mintz covers substance | **moderate** |

Rationale for not draining: the browser-fetcher drives the user's REAL Chrome
session. Only three items carry moderate value and none is decision-critical —
factor crowding is already flagged as thinly evidenced, and the DOJ v. Apple
opinion's operative findings are covered by the Mintz analysis. The cost of
taking over the user's browser is not justified by the expected gain.

Drain later if wanted: `hyperresearch escalation list --status queued -j`,
then spawn one hyperresearch-browser-fetcher.

## Step 2 exit criterion — MET

- Source count: 128 substantive (minimum 45, target 55–80) ✓
- No `uncovered` atomic items after wave 2 ✓ (Q5 crowding and Q6 weak-form
  lock-in thin but ≥2 independent sources)
- coverage-gaps.md written ✓
- redundancy-audit.md written ✓
- Ranking signals persisted: 512 claims ingested, 5 DOIs backfilled,
  0 retracted, 145 notes graph-ranked ✓
