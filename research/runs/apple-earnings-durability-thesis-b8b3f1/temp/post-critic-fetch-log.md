# Step 13 — post-critic gap-fetch log

Reviewed all findings in `critic-findings-{dialectic,depth,width,instruction}.json` (40 findings total). Most width/depth/instruction findings named sources the vault **already has** (DOJ v. Apple filings, Epic-trial 78%/79.6% App Store margin testimony, the CEO-transition note cluster, TSMC's 20-F, the SSRN crowding papers, the iOS-27 supercycle Wedbush/JPMorgan note) — those are patcher work (step 14), not fetch gaps, and were left alone here.

Three findings named topics with genuinely thin or absent vault coverage (checked via `hyperresearch search --tag apple-earnings-durability-thesis-b8b3f1` plus direct grep of candidate notes before fetching). All three were fetched, within the 5-gap cap.

## Gap 1 — Vietnam manufacturing lead-time / capex (instruction-critic major #1, §7.5)

**Searched:** vault search turned up only passing Vietnam mentions inside the AEI supply-chain report (diversification landscape, no Apple-specific lead-time/capex figures). Web: JPMorgan/TechCrunch 2022 forecast, vietnam-briefing.com supplier reporting, AppleInsider 2020/2022 coverage, SCMP Nov 2023 Luxshare investment, smartanalyticsglobal.com Q1 2026 AirPods share data.

**Found:** 7 sources fetched (see agent report). Key result: Vietnam factory-shell *construction* is fast (5 months for a 30-hectare shell in 2020; 12–24 months for a 70-acre facility in 2023) — construction speed is not the binding constraint. What is slow: building a deep, multi-tier supplier ecosystem for complex products (iPhone, MacBook), and a 2020 labor-conditions rejection that kept a fully-built Vietnam facility from getting iPhone-assembly approval. JPMorgan's 2022 forecast gives the one quantified capex-to-share timeline: India iPhone share 5%→25% over ~2.5 years; Vietnam's non-iPhone targets (iPad/Watch/MacBook/AirPods) on a similar ~3-year horizon to 2025.

**Audited absence recorded:** iPhone final assembly has never moved to Vietnam as of Sept 2026 (checked across all 7 sources) — recorded as an explicit claim, not silently omitted.

**Status:** filled. Note IDs tagged `post-critic-fill`: `apple-holding-off-on-vietnam-iphone-assembly-over-workers-living-conditions-appl`, `apple-tests-production-of-apple-watch-macbook-pro-in-vietnam-appleinsider`, `apple-supplier-luxshare-to-invest-additional-us330-million-in-vietnam-plant-as-s`, `apples-production-strategy-in-vietnam`, `apple-suppliers-in-vietnam-where-why`, `apple-to-move-25-iphone-production-to-india-by-2025-20-ipad-and-apple-watch-to-v`, `sag-vietnam-led-global-apple-airpods-manufacturing-in-q1-2026-while-india-contin`.

## Gap 2 — EU alternative-marketplace adoption rate (width-critic + dialectic-critic, §4.3/§6.3/§7.1)

**Searched:** vault grep for percentage-bearing marketplace-adoption figures across all DMA-related notes returned zero hits. Web: European Commission DMA compliance decisions (address steering/interoperability, not usage stats), Sensor Tower/Appfigures (no indexed public report), Apple's own Nov 2025 Analysis-Group study (explicitly excludes alternative marketplaces), Epic's own Jan 2025 disclosure, AltStore/Setapp coverage.

**Found:** no published adoption-rate figure exists anywhere — official, academic, or analyst — after a genuine search. One WebSearch-synthesized "<3%" figure was checked, found unsourced, and explicitly rejected rather than cited. Built a synthesis note from the best available proxies instead: Epic Games Store reached only 29M installs globally against its own 100M target (5M EU-specific install attempts blocked by Apple's checks); zero of the top-100 highest-grossing mobile game developers list on EGS; Setapp Mobile shut down in Feb 2026 after 17 months citing non-viability. Both Apple and Epic have adversarial incentives to publish a favorable adoption number and neither has, ~2 years post-DMA — the defensible inference is that adoption-driven commission erosion is bounded as slow, not a step-function threat, but this is flagged explicitly as an inference from proxies, not a disclosed rate.

**Status:** filled as an audited absence + proxy bound (correct outcome — no real figure exists to fetch). New synthesis note: `audited-absence-eu-marketplace-adoption`. Supporting notes tagged `post-critic-fill`: `epic-games-store-adoption`, `move-over-apple`, `what-happens-to`.

## Gap 3 — Apple Pay revenue sizing (width-critic major, dialectic-critic reader-prior-II context, §6.3)

**Searched:** vault grep found only passing "Apple Pay" mentions inside 10-Ks/court docs, no dedicated revenue-sizing note. Web: chased the full aggregator citation chain back to source.

**Found:** Apple does not disclose Apple Pay revenue (confirmed on the record by an Apple spokesperson, Payments Dive Aug 2024). The only primary, methodologically transparent estimate is Loup Ventures (Gene Munster, Feb 2019): $988M (2019) → $4B forecast for 2023, built on a disclosed 0.15% issuer-fee take rate — now 7 years stale with no credible update found. Everything published since 2019 (Statista, grabon.com, electroiq.com, Capital One Shopping) is aggregator arithmetic re-extrapolating the same 2019 base, not independent analysis; current estimates span $3.0B–$5.6B for 2025 with no reconcilable methodology, i.e. Apple Pay/Card revenue is roughly 0.7–1.5% of total Apple revenue regardless of which estimate is used — small, not decisive on its own. Most load-bearing new fact for the report's "voidable arrangement" framing: Apple opened NFC/secure-element access to third-party wallets (PayPal, Shopify) across the EU, Australia, Brazil, Canada, Japan, New Zealand, UK and US in 2024, ending the on-device exclusivity Loup Ventures' 2019 model implicitly assumed would persist — a concrete, dated regulatory event.

**Status:** filled (with explicit staleness/divergence caveats — correct outcome, since a fresher precise figure genuinely does not exist). Note IDs tagged `post-critic-fill`: `report-sees-plenty-of-upside-for-apple-with-one-of-its-services-offerings-phonea`, `pymnts-apple-pays-business-model-blues`, `apple-services-revenue-rises-with-boost-from-payments-payments-dive`, `global-apple-pay-revenue-forecast-statista`, `apple-pay-statistics-2026-users-market-share-growth-rate`, `apple-pay-usage-statistics-in-2024`, `apple-pay-statistics-by-revenue-users-security-and-facts-2025`.

## Summary

3/3 gaps attempted, 3/3 filled (two as audited-absence + proxy/estimate rather than a clean disclosed figure — that is the correct, honest outcome given what actually exists in the public record, not a fetch failure). 55 claims extracted across 18 notes; curated selection appended to `evidence-digest.md` under "### Post-critic gap fill (step 13)". The patcher should cite the audited-absence framing explicitly rather than treat gaps 2 and 3 as resolved with point figures.
