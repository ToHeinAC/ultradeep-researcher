## Coverage Matrix — query phrase → atomic item mapping

Pass 2 (after fixing three gaps found in pass 1 — see bottom).

| Query phrase (verbatim) | Mapped atomic item(s) | Scope check | Gap? |
|---|---|---|---|
| "fraction of Apple's earnings is contingent on arrangements a court or regulator can void" | Sub-Q1 (durability decomposition); Sub-Q13 (regulatory exposure beyond TAC) | OK — covers both "court" (litigation) and "regulator" (DMA/EC), not just litigation | No |
| "2–5 year holding view" | time_horizons: 2-5y forward; scope_conditions: equity-holder, no trade | OK | No |
| "informed technical investor forming a view, not executing a trade" | levers.register=analyze; scope_conditions (no buy/sell/hold) | OK | No |
| "fundamentals and valuation" | Sub-Q1, Sub-Q5, Sub-Q7, Sub-Q8, Sub-Q15; headings 1–3 | OK | No |
| "product and AI strategy" | Sub-Q3, Sub-Q9, Sub-Q10; entity Apple Intelligence, Apple Silicon; heading 5 | OK | No |
| "regulatory and legal exposure" | Sub-Q2, Sub-Q6, Sub-Q13; entities DMA, DOJ, Epic; heading 4 | OK — broadened beyond TAC alone | No |
| "supply chain and geopolitics" | Sub-Q12; entities China, India/Vietnam; heading 7 | OK — has a dedicated heading | No |
| "argue both bull and bear cases competently" | response_format=argumentative; heading 8 (Verdikt) | OK | No |
| "A share is a claim on future cash flows" | Sub-Q1 framing; Sub-Q15 (discount-rate sensitivity) | OK | No |
| "total return decomposes exactly into fundamental growth + multiple change + shareholder returns" | Sub-Q8 (multiple vs fundamentals); Sub-Q14 (buybacks/capital returns) | OK — all three identity terms covered | No |
| "Buybacks raise EPS with no revenue growth" | Sub-Q14 | OK | No |
| "Higher discount rates compress long-duration cash flows" | Sub-Q15 | OK | No |
| "~$3–4T company cannot compound at small-cap rates" | Sub-Q7 (required services CAGR); Sub-Q8 | OK | No |
| "Apple is a hardware company" (convention) | Sub-Q1 (durability not segment); scope_conditions (segment frame rejected) | OK | No |
| "P/E vs. its own history is the valuation anchor" (convention) | Sub-Q5; Sub-Q11 (falsification test) | OK | No |
| "The iPhone cycle drives the stock" (convention) | Sub-Q9; entity iPhone | OK | No |
| "AI capability is existential for Apple" (convention) | Sub-Q3 | OK | No |
| "passive/index flows mechanically support the multiple" | Sub-Q5 | OK | No |
| "Quality factor crowding" | Sub-Q5 | OK | No |
| "Antitrust remedies and appeals run multi-year" | Sub-Q2; time_periods (US v. Google, US v. Apple) | OK | No |
| "Manufacturing diversification is physically slow" | Sub-Q12 (capex-to-output lead times) | OK | No |
| "AI product cycles resolve inside the window" | Sub-Q3, Sub-Q9 | OK | No |
| "A multiple re-rating needs years" (arbitrary) | Sub-Q8 | OK | No |
| "Ecosystem lock-in is structural, not switching-cost inertia" | Sub-Q6; entity DMA | OK | No |
| "Owning silicon is load-bearing for margin" | Sub-Q10; entity Apple Silicon | OK | No |
| "Services growth can offset hardware maturity" | Sub-Q7; entity Services segment | OK | No |
| "Late-follower status in AI is currently an ADVANTAGE" (reader prior 1) | Sub-Q3; heading 5 (dedicated) | OK — dedicated section, framed as test not restatement | No |
| "payments business ... faces near-term disruption from crypto/AI payment rails" (reader prior 2) | Sub-Q4; entity crypto/AI payment rails; heading 6 (dedicated) | OK | No |
| "the Google search-placement fee (TAC) is NOT a payment service" | scope_conditions (explicit separation clause); headings 4 and 6 are separate sections | OK — enforced structurally by separate headings | No |
| "Annuity-like / Cyclical / Contingent / Binary" | Four durability-class entities; heading 1 | OK — each is its own entity with required_fields | No |
| "Earnings decomposed by durability class, not product segment" | required_formats item 1; heading 1 | OK | No |
| "The multiple decomposed into earned vs. passive-flow/factor artefact" | required_formats item 2; heading 3 | OK | No |
| "Binary events listed explicitly with magnitude and timing" | required_formats item 3; heading 4 | OK | No |
| "Required services CAGR to hold total growth flat" | required_formats item 4; Sub-Q7 | OK | No |
| "observe the EU DMA natural experiment" | Sub-Q6; time_periods (DMA March 2024 onward) | OK | No |
| "DOJ–Google discovery put figures on the record" | Sub-Q2; time_periods (US v. Google remedies) | OK — drives court-record sourcing | No |
| "Show a range and its assumptions, not a point estimate" | required_formats items 1, 2 | OK | No |
| "Remedy DESIGN is analysable even when the ruling is not predictable" | Sub-Q2 (remedy design + timetable + worth per design) | OK | No |
| "prefer filings and court records over commentary" | levers.domain_notes; scope_conditions | OK | No |
| "Cheapest prototype test ... blended multiple diverges materially from the headline P/E" | Sub-Q11; required_formats item 5; heading 2 (dedicated) | OK — dedicated heading, sequenced before forecasting sections | No |
| "Run this falsification BEFORE any forecasting" | Heading order: 2 precedes 3–8 | OK — enforced by heading sequence | No |
| "price targets" (out of scope) | scope_conditions | OK | No |
| "quarterly earnings estimates" (out of scope) | scope_conditions | OK | No |
| "peer-multiple comparison as a valuation anchor" (out of scope) | scope_conditions | OK | No |
| "personalised investment advice" (out of scope) | scope_conditions | OK | No |
| "Report language: GERMAN" | scope_conditions; required_section_headings are German literals | OK | No |
| "Sources: any language" | scope_conditions | OK | No |
| "Quotations translated into German, with the English original alongside" | scope_conditions | OK | No |
| "inline `[N]` markers plus a `## Sources` section" | citation_style=inline | OK | No |
| "Register: informed technical investor" | levers.register=analyze; scope_conditions | OK | No |
| "Length: whatever the evidence supports" | response_format=argumentative (5000-10000w guidance, not a hard cap) | OK | No |
| "Structure: earnings decomposition → multiple decomposition → binary events → two tested priors → verdict" | required_section_headings 1→8 preserve this order | OK — headings 2 and 7 inserted without breaking the mandated sequence | No |

### Gaps found in pass 1 and fixed

1. **"supply chain and geopolitics" had no home.** It is named as one of four in-scope angles in AUSGANGSSITUATION but appears in none of the ten numbered research questions. Added Sub-Q12 and dedicated heading 7. Without this the width sweep would have under-searched China/India/tariffs entirely.
2. **"regulatory and legal exposure" was narrowed to Google TAC.** Pass 1 mapped it only to Sub-Q2. The phrase's natural scope covers DOJ v. Apple, EU DMA and App Store rulings as well. Added Sub-Q13 and broadened heading 4.
3. **The return identity's third term was unmapped.** "shareholder returns" appears in the Phase 1 truths and in the buyback claim, but pass 1 had no atomic item for the buyback/capital-return contribution to 2-5y return. Added Sub-Q14. Also added Sub-Q15 for discount-rate sensitivity, which Phase 1 asserts but no numbered question tested.

**Zero `Gap? = YES` rows remain.**
