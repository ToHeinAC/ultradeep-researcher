# Redundancy audit — apple-earnings-durability-thesis-b8b3f1

## Method

111 claims files, 512 ingested claims. Clustered by shared SUBSTANTIVE figures
in `claim` + `quoted_support` text: currency amounts, percentages, decimals.
Bare years and small integers excluded — a first pass without that filter
produced 64 spurious pairs driven by "2025"/"2026" (e.g. stablecoin notes
"matching" CEO-succession coverage). After filtering: 9 pairs at ≥2 shared
figures and ≥50% overlap. Each pair then adjudicated by reading summaries.

Derivatives are TAGGED, not deprecated, so their claims survive and remain
citable. They are discounted in independent-source counts only.

## Adjudicated pairs

| Pair | Shared | Verdict | Action |
|---|---|---|---|
| Mozilla "six million selections" ~ active-choice-interventions study | 113%, 12% | **Derivative.** One upstream study; Mozilla (interested party) restates it | `derivative-dma-choice-study`, `interested-party` |
| IBTimes "90% escape commission" ~ Apple newsroom $1.4T ecosystem | $1.1T, $1.4T, 90% | **Derivative** of the Apple-funded Analysis Group study | `derivative-of-support-for-this-study-was-provided-by-apple` |
| MacRumors 3Q results ~ Six Colors Q3 transcript | 8 figures | **Derivative.** Both restate Apple's Q3 disclosure; 8-K + transcript are upstream | `derivative-of-aapl-8k-q3fy2026` |
| "Big Tech $700B buildout" ~ Quartz Google ruling | $25B, 95% | **Derivative.** Both cite ONE Morgan Stanley (Woodring) TAC estimate | `derivative-ms-tac-estimate` |
| AAF DOJ v. Apple primer ~ Mintz DOJ ruling | 65%, 70% | **Derivative.** Both cite DOJ complaint share figures; Mintz is later and procedural | `derivative-of-judge-allows-…-mintz` |
| Xing RePEc citation page ~ Xing CEPR column | 25%, 45% | **Derivative.** Citation-index page of the working paper behind the column | `derivative-xing-cepr` |
| CNBC live ~ BigGo App Store admission | 6%, 9% | Same upstream Sensor Tower spend estimate | noted, not tagged |
| FRED DGS10 ~ FRED DFII10 | 4.95% | **Distinct.** Nominal vs real series; real note cites nominal for breakeven | keep both |
| Apple FY25 10-K ~ AAF primer | 10%, 23% | **Coincidental** | none |

Previously handled: `united-states-district-court-2` tagged as a duplicate
mirror of Doc. 1436.

## What the audit changes — evidence is thinner in three places than raw counts suggest

1. **DMA weak-form lock-in rests on ONE study.** The headline "Firefox usage
   113% above counterfactual" has a single upstream, amplified by an
   interested party. Independent evidence on browser switching is ~2 sources
   (the study; early TechCrunch data), not the 6 notes the vault holds.
   Combined with the confirmed absence of any EU phone-switching data, the
   natural experiment the brief relies on is weakly evidenced on BOTH forms.

2. **The ">$25B TAC at 95% margin" figure is one analyst estimate.** Two
   notes, one Morgan Stanley model. The court's **~$20B (2022, worldwide)** is
   the independent, higher-authority figure and must anchor the sizing. Use
   the MS figure only as a labelled estimate bounding the range above.

3. **App Store commission erosion rests on two commercial estimators**
   (Appfigures, Sensor Tower), restated across many outlets. Management's
   oral admission on the Q3 FY26 call is the only independent confirmation of
   direction; no filing quantifies it.

## Conceptual clusters (not caught by figure overlap, adjudicated from fetcher reports)

- **Google remedies commentary** (Hughes Hubbard, KGI, TechPolicy, SEL, NTU,
  Quartz) all derive from Doc. 1436. Factually derivative — cite the opinion
  and its source-analysis. BUT they carry genuinely independent ANALYTICAL
  positions (the "toothless remedy" vs "structural erosion" split), so they
  remain valuable as commentary.
- **India assembly share** (National Herald, Gulf News, AppleInsider,
  Technology Magazine) likely share one commercial upstream. Independent
  corroboration comes from AEI and Xing/CEPR instead.
- **Stablecoin adoption** (Spark ×2, insights4vc, Chainalysis) — interested
  parties sharing a few upstream reports. Visa and Mastercard CEO statements
  (CoinDesk) are the independent evidence.
- **AI capex** (725B, 660B, 700B, Fast Company) all restate hyperscaler
  guidance. Company 10-Qs and earnings calls are upstream.
- **Factor crowding**: two MSCI posts count as ONE interested source;
  Barroso/Edelen/Karehnke (JFQA 2022) is the independent peer-reviewed one;
  arXiv 2512.11913 is a self-withdrawn preprint and does not count.

## Wave 3 decision: NOT required

No atomic item drops below 2 independent sources after discounting:

| Item | Independent sources after discount |
|---|---|
| Q5 factor crowding | 2 (MSCI; Barroso et al.) — borderline, flagged thin |
| Q6 weak-form lock-in | 2 (choice-screen study; early TechCrunch data) — flagged thin |
| Q10 silicon margin | 4 (SemiAnalysis; Digits to Dollars; Qualcomm 10-K; TSMC 20-F) |
| Q12 supply chain | ≥3 (AEI; Xing/CEPR; India share upstream) |
| Q2 TAC | ≥3 (liability opinion; remedies opinion; Apple 10-Q risk factors) |

Q5 crowding and Q6 weak-form lock-in are thin but not below the threshold. The
drafters must present both as weakly evidenced, not as settled.
