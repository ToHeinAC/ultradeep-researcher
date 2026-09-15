# Synthesis conflicts — verified against source bodies

## Conflict 1: Counterpoint calendar-Q1 2026 Apple unit growth
- Draft B says: MacRumors reports Counterpoint +9% at 21% share; "other reports" +5%.
- Draft A / C say: Counterpoint +5% at 21% share.
- Source check: `apple-tops-smartphone-market-in-q1-as-overall-shipments-drop-9to5mac` — "achieving 21% market share and 5% YoY growth". The MacRumors note (`apple-tops-global-smartphone-market-for-first-time-in-a-q1-macrumors`) contains NO "9%" figure.
- **Verdict:** +5% (Counterpoint, via 9to5Mac). Drop the +9% claim entirely.

## Conflict 2: IDC 2026 smartphone forecast vintage
- Draft A says: IDC −16.7% shipments, iOS −1.3%, Android −24.3%, iOS share record 23.6%.
- Evidence digest (older Axis-Intel aggregator) says: IDC −13.9%, iOS −5.2%, share 22%.
- Source check: `idc-smartphone-shipments-to-drop-167-in-2026-as-memory-crisis-bites` (IDC's own blog, Aug 26 2026) confirms −16.7%, −24.3%, −1.3%, 23.6%.
- **Verdict:** use the Aug 26 2026 IDC figures (latest, primary). The −13.9% figure is an earlier forecast vintage; do not use it.

## Conflict 3: Google search growth 2024
- Draft A "~22%"; Drafts B/C "21.6%"; digest "~20%".
- Source check: `stats-from-a-dying-web` — "Google searches rose 21.6…" (SparkToro data via Platformer).
- **Verdict:** 21.6% (2024 vs 2023), attributed to SparkToro via Platformer.

## Conflict 4: Card-network volume denominator for the stablecoin ratio
- Draft A: ~$23.7T Visa+Mastercard → ~1:1,300. Draft B: Visa $17T + Mastercard $11T → ~1:1,500. Draft C: $23.7T → <0.1%.
- Source check: $23.7T appears only in `mastercard-and-visa-building-crypto-rails-…` (Spark.money, stablecoin vendor, conflict of interest). $17T/$11T is in `visa-and-mastercard-arent-buying-the-stablecoin-hype-…` (CoinDesk, citing Glassnode).
- **Verdict:** state the conclusion robustly: ~$18B annualised stablecoin-card spend is **under 0.1%** of Visa+Mastercard volume on either denominator ($23.7T vendor figure; $28T CoinDesk figure). Prefer CoinDesk's $17T/$11T as the named figure.

## Conflict 5: Name spelling
- Drafts spell Visa's CEO "McInerny" (as in the CoinDesk text) and Mastercard's "Miebach"/"Mierbach".
- **Verdict:** Ryan McInerney (Visa), Michael Miebach (Mastercard). Quote text verbatim, but name them correctly in prose.

## Conflict 6: Alphabet stock move on the remedies ruling
- Draft A: +8.5% (Apple +2.8%). Draft B: "nearly 8%".
- Source check: Quartz note says "about 8.5%" and Apple 2.8%; NTU note says "nearly 8%".
- **Verdict:** "rund 8–8,5 %", cite the Quartz note for 8.5%/2.8%.

## Conflict 7: Silicon margin contribution
- Draft A: SemiAnalysis annual chip savings >$7B (Intel ~$5B, Qualcomm ~$1.2B, Broadcom ~$0.7B); Mac GM 28.5–29% → 39.5%.
- Draft B: Digits to Dollars, M1 switch GM effect 0.3pp ("almost rounding error").
- Draft C: Digits to Dollars rough model ~$3.5B / 1.7pp, ~$1B after design costs; authors "100% certain that some of our numbers are wildly off".
- Source check: all three figures are verbatim in their notes. They measure different things: SemiAnalysis = gross avoided vendor spend (paywalled preview, no netting of design cost); Digits to Dollars = net of design costs, self-declared rough.
- **Verdict:** not a factual contradiction — a method range. Commit: COGS savings are real but small relative to the exposed Services streams (≤ ~$7B gross ≈ ≤3.6% of FY2025 GP; net of design cost far smaller); the load-bearing value of owned silicon is pricing power/differentiation, not unit cost. The modem net gain is unquantified in any source.

## Conflict 8: Differentiated haircuts (judgment, not fact)
- A: TAC 15–25%, commissions 40–60% → −1.8 to −4.1 turns.
- B: TAC 15–25%, commissions 30–50% → −1.5 to −3.6 turns.
- C: TAC 10–20%, commissions 35–55% → −1.4 to −3.6 turns (GP basis); −5.3 on OI basis.
- **Verdict:** use TAC 10–25% and commissions 30–60% as the span, central TAC 20% / commissions 45% → central ≈ −2.5 to −3 turns; state the band as ~1.5–4 turns on GP basis, up to ~5 on an operating-income basis. All haircuts are labelled assumptions.

## Conflict 9: Services Q4 FY2026 "below 10%"
- A attributes "below 10% year-over-year as reported" to an analyst on the Q3 call; B/C say guidance implies <10% reported on ~2.5pp FX headwind.
- Source check: consistent — the analyst framed it, Parekh cited FX (~2.5pp) and a prior-year film effect, plus App Store changes, without quantifying the split.
- **Verdict:** present as guidance-implied (~<10% reported, FX-driven in part); attribute the phrase to the analyst question. Filed Q3 Services growth is +12.1% (Tradingpedia's "below 10%" for Q3 contradicts the filing).

## Conflict 10: Market cap / 28x three-year average
- A: ~$4.9–5T; B: >$5T. The 28x three-year average appears only in Tradingpedia (`apple-valuation-faces-scrutiny-as-services-growth-cools`), a low-authority source that also misreported Q3 Services growth.
- **Verdict:** "rund 5 Bio. $" (Alpha Spread $4.9T at $332.61, Sept 11 2026). Use 34.6x/28x with explicit attribution to Tradingpedia and flag it as a secondary figure; the argument must not hinge on the exact 28x.
