# Corpus-critic results — apple-earnings-durability-thesis-b8b3f1

Seven gaps: one period-pinned (pp-1) from the orchestrator pre-flight and six
from the corpus critic (cc-1 to cc-6). Three fetch agents failed during this
step (two stalled at 600s with no progress; the first critic and pp-1 fetcher
were killed by an API session limit). Where an agent failed on a question that
reduced to a targeted extraction, the orchestrator ran it directly with the CLI
and verified every figure against the note body before recording it.

---

## cc-1 — critical, overturning — Apple's share of Alphabet distribution TAC

**Searched:** Alphabet FY2022 and FY2025 10-Ks (goog-20221231, goog-20251231),
targeted extraction of all TAC passages.

**Found:**
- Total TAC: $45,566M (2021), $48,955M (2022), $54,900M (2024), $59,926M (2025).
  FY2022→FY2025 CAGR ≈ 7.0%, consistent with the TAC investigator's 6.6%.
- AUDITED ABSENCE: Alphabet does not disclose the dollar split between
  distribution-partner TAC and Network-partner TAC in either filing.
- Qualitative, verbatim, FY2025 10-K: "The increase in TAC from 2024 to 2025 was
  largely due to an increase in TAC paid to distribution partners". The FY2022
  10-K credited "distribution partners and … Google Network partners" together.
- Both filings: Network TAC as a percentage of revenue is "significantly higher"
  than Search TAC, and the overall TAC rate "has been decreasing primarily due to
  a revenue mix".

**Effect:** OVERTURNING RISK NOT REALISED. The feared direction was that
Apple's share had fallen, shrinking TAC below $23–29B. The evidence points the
other way: growth has concentrated in distribution partners (where Apple sits)
while the high-TAC Network business shrinks as a share, so distribution TAC has
likely grown FASTER than the blended ~7% used for scaling. The $23–29B range is
if anything conservative. The constant-share assumption remains unverifiable in
dollar terms (no split disclosed), so the range stays a modeled band.
**TAC locus confidence: unchanged at medium; direction of residual error now
known to be upward.**

---

## cc-2 — critical, overturning — the one data point behind "AI query migration is already underway"

**Searched:** fetcher landed two notes before stalling:
`google-searches-in-apples-safari-fall-for-first-time-in-22-years` (Search
Engine Land, May 7 2025) and `stats-from-a-dying-web` (Platformer).

**Found:**
- NO SECOND DATA POINT. The Search Engine Land note reports the SAME May 2025
  Cue testimony ("Searches on Apple's Safari browser declined for the first
  time last month… 'That has never happened in 22 years'"). It corroborates
  what was said, not what happened.
- ADVOCACY CONTEXT (Platformer): Cue's "primary objective was to convince the
  judge that the search market is already so competitive that he should allow
  Google to continue paying it $20 billion a year." Apple had a direct
  financial interest in portraying search as disrupted by AI, in the very
  proceeding where the testimony was given.
- CONTRARY AGGREGATE DATA (Platformer, citing SparkToro/Fishkin): Google
  searches grew roughly 20% in 2024, and Google handles 373 times as many
  searches as OpenAI's chatbot. Google's CEO says AI Overviews are increasing
  search usage.
- Complicating, not contradicting: Google's AI Overviews reportedly cut
  click-through to source pages by 70–80%, and ~60% of searches end without a
  click (Bain) — the interface is changing INSIDE Google, not only away from it.

**Effect:** WEAKENS Tension 1. "Already underway" rests on a single data point,
from a witness with an incentive to make exactly that claim, and aggregate
Google search volume contradicts platform-wide migration. The claim survives in
a narrower form that is still relevant to TAC: Safari-originated queries — the
base TAC is paid on — can fall even as total Google search grows, because
queries can move to the Google app, AI Overviews, or chatbots. But the report
must NOT present AI query migration as an established, underway trend.
**Tension 1 confidence DOWNGRADED from medium to low-medium.** Leading
indicator unchanged: a second measured year of Safari search volume.

---

## cc-3 — high, overturning — is FY2026 iPhone growth price-led or unit-led?

**Searched:** orchestrator web search, then direct CLI fetch of three sources
(`apple-tops-smartphone-market-in-q1-as-overall-shipments-drop-9to5mac`,
`apple-tops-global-smartphone-market-for-first-time-in-a-q1-macrumors`,
`apples-smartphone-shipment-share-hits-first-ever-20-for-a-q2-as-memory-crisis-sp`).

**Found (verified verbatim in note bodies):**

| Calendar quarter | Apple units YoY | Apple iPhone revenue YoY (fiscal) | Implied price/mix |
|---|---|---|---|
| Q4 2025 | +4.9% (IDC) | +23.3% | ~18pp |
| Q1 2026 | +5% (Counterpoint); +4.4% (IDC, via search summary) | +21.7% | ~17pp |
| Q2 2026 | **+3% (Counterpoint) vs +15.3% (IDC)** | +21.7% | ~19pp vs ~6pp |

- Q1 2026 (Counterpoint, verbatim): Apple "achieving 21% market share and 5% YoY
  growth in Q1 2026" while Samsung fell 6% and Xiaomi 19%.
- Q2 2026 (XenoSpectrum, verbatim): Counterpoint put Apple's growth at 3% with
  the market down 11%; "IDC estimates that Apple's shipments grew 15.3%" with
  the market down 6.7% — "a substantial gap compared to Counterpoint's figures".
  Both firms put Apple's share at a record ~20%.

**Orchestrator error caught and corrected:** the web search's AI summary
reported "Counterpoint +13% in Q2 2026". Verification against the source body
shows Counterpoint's figure is +3%; the +13% was an artefact of the search
summary. It was briefly relayed to the user before verification and has been
corrected. Only verified figures are used here.

**Effect:** NOT OVERTURNED — CONTESTED. Price/mix-led growth is confirmed for two
of three quarters by both firms. The latest quarter is a genuine
12-point measurement dispute between the two leading trackers that cannot be
adjudicated from the corpus (differing sell-in estimation methods). What BOTH
firms agree on is newly material: Apple reached a record ~20% share while the
market contracted, i.e. it is TAKING UNIT SHARE from Android vendors squeezed
harder by the memory shock (consistent with IDC's forecast of iOS −1.3% vs
Android −24.3%). **Hardware locus confidence unchanged at medium**, with two
refinements: (1) the Q2 2026 unit picture is disputed; (2) the memory shock
helps Apple through share gain, not only through price pass-through — which is
somewhat higher-quality growth than "pure cost pass-through" implied.

---

## cc-4 — high, overturning — what fee survives the cost-based remand?

**Searched:** orchestrator web search; CLI fetch of
`apple-proposes-commissions-of-up-to-15-for-off-app-store-purchases-in-the-us-9to`
(9to5Mac, Aug 13 2026) and
`apples-fight-over-commissions-for-linked-out-app-store-purchases-continues-in-fe`
(Courthouse News).

**Found (verified verbatim):** Apple's remand submission proposes link-out
commissions of **15% for standard apps** (vs the 30% IAP rate), **10%** for the
Video, News and Mini Apps partner programs and subscription renewals, and
**5% for Small Business Program apps**. Apple cites Google Play's linked-out
rates (20% standard, 15% program, 10% subscription) and says "Epic agreed to
those rates" — a real comparator supporting a nonzero fee.

**Orchestrator error caught and corrected:** the web search's AI summary stated
that "Apple admitted" it would charge 0% under the Ninth Circuit's
necessary-costs standard. The source body attributes that statement to
**Epic's post on X** ("Apple's filing is in, and Apple admitted that under the
Ninth Circuit's definition of 'necessary costs' they would charge 0%…") — an
adversary's characterisation of Apple's filing, not Apple's own words. It must
never be reported as an Apple admission.

**Effect:** App Store erosion claim REFINED — direction confirmed, magnitude
open. Even Apple's own requested rates are half its prior 27% link-out fee and
half its IAP rates; the realistic remand range runs from ~0% (Epic's reading
of the cost standard) to 15% (Apple's ask). Erosion is durable in direction; the
remand decides whether it is near-total or partial. App Store locus confidence
unchanged (medium).

## cc-5 — high, independent-verification — commission revenue

**Searched:** orchestrator web search for court-filing, expert-testimony or
congressional figures.

**Found:** every result traces back to Appfigures ($10.1B US / $27.39B global,
2024) or Apple's own commissioned $149B digital-billings figure.
**AUDITED ABSENCE, confirmed:** no court-surfaced, expert or government
estimate of App Store commission revenue exists in accessible sources. The
$22–31B range remains vendor-estimate-based; the draft must say so.

## pp-1 — critical, period-pinned primary — US v. Apple record

**Searched:** justice.gov, CourtListener, law.justia.com (escalation #9),
congress.gov CRS report LSB11154 (bot wall, queued as escalation #16).

**Found:** only a 219-word DOJ press release on additional states joining the
suit. **UNFINDABLE via the headless lane:** both primary routes are bot-walled.
The operative substance (surviving claims including NFC/tap-to-pay access,
monopoly-power pleading at 65%/70% share, no trial date as of May 2026) is
covered by the Mintz analysis and 9to5Mac. The draft must cite DOJ v. Apple
facts to those secondary sources and label them as such.

## cc-6 — second independent TAC estimate

The cc-1/cc-6 fetcher stalled before finding one. AUDITED ABSENCE at this
point: no second independent (non-Morgan-Stanley) current estimate is in the
corpus. cc-1's finding that distribution TAC is growing faster than blended TAC
partly substitutes, since it bounds the error direction. Draft must state the
current-TAC figure is a scaled court figure cross-checked against ONE analyst.
