---
title: 'The “exit penalty”: Why the DMA’s interoperability rules fail the reality
  test of platform migration | Internet Policy Review'
id: the-exit-penalty-why-the-dmas-interoperability-rules-fail-the-reality-test-of-pl
tags:
- apple-earnings-durability-thesis-b8b3f1
- locus-lockin-durability-preference-vs-ai-interface
- dma-interoperability
- platform-migration-case-study
- exit-penalty
created: '2026-09-13T11:29:03.250294Z'
updated: '2026-09-15T19:32:22.174335Z'
source: https://policyreview.info/articles/news/exit-penalty-platform-migration
source_domain: policyreview.info
fetched_at: '2026-09-13T11:29:03.231859Z'
fetch_provider: crawl4ai
status: review
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Independent-researcher case study (Internet Policy Review, published 20
  Feb 2026, author Teruki Yagi) documenting a single-author (n=1) real-world iOS-to-Android
  migration attempt in Japan in early 2026, used as evidence that DMA-style/DMA-mirrored
  interoperability compliance does not eliminate phone-level switching costs. Over
  5 days and 25+ hours, migrating ~120 accounts/services produced 34 documented friction
  points (11 requiring manual reconfiguration, 9 partial/failed data portability,
  6 hardware-dependent constraints). Concrete barriers found even where DMA-style
  portability formally exists: Suica transit card tied to Apple Pay could only be
  deregistered with the original iPhone hardware present (hardware lock-in); iMessage
  history has no meaningful export mechanism (data+social lock-in, network-effect
  amplified); Apple Keychain CSV export does not preserve 2FA settings, forcing manual
  reconstruction of credentials; Apple Watch loses core functionality entirely off
  iOS (hardware dependency). Argues DMA Article 6''s data-portability focus addresses
  ENTRY/daily-use but leaves an unaddressed ''exit penalty'' -- procedural, hardware,
  and identity-migration costs -- that keeps real switching costly even after formal
  compliance. Grounds the argument in Klemperer (1987) switching-cost theory, Farrell
  & Klemperer (2007), and the OECD''s 2021 ''Switching Costs and Consumer Policy in
  Digital Markets'' report. IMPORTANT CAVEAT for this locus: this is a Japan-based
  single-subject case study, not EU-market data, and is qualitative/anecdotal (n=1),
  not a switching-rate statistic -- it does NOT supply the phone-level EU switching-RATE
  dataset the query sought, but it is directly relevant qualitative evidence for why
  such rate data may stay low even post-DMA.'
---

[ Skip to main content ](https://policyreview.info/articles/news/exit-penalty-platform-migration#main-content)
#  The “exit penalty”: Why the DMA’s interoperability rules fail the reality test of platform migration
[Teruki Yagi](https://policyreview.info/users/teruki-yagi), _Independent researcher_ , _Japan_ PUBLISHED ON: 20 Feb 2026
## Introduction: The DMA and the myth of easy switching
The EU’s Digital Markets Act (DMA) (EU, 2022) has been hailed as a landmark in regulating platform monopolies, mandating interoperability and data portability to enhance consumer choice. Apple and Google, the dominant players in mobile ecosystems, publicly frame these provisions as evidence that users can now “switch” platforms without friction, as stated in [Google’s official blog on complying with the DMA.](https://blog.google/around-the-globe/google-europe/complying-with-the-digital-markets-act/)
Yet, the reality of a full platform migration remains deeply challenging. While basic data such as photos and contacts are transferable, many core layers of users’ digital lives remain tightly locked within their original ecosystems. This “exit penalty” architecture effectively deters migration despite formal compliance with Article 6 of the DMA.
## Methodology: A real-world migration experiment
In early 2026, I conducted a full migration from Apple’s iOS ecosystem to Google’s Android in Japan – a market characterised by dense integration of mobile payments, transit cards (e.g., Suica), and device-dependent identity systems. According to consumer adoption research, by December 2024 more than 40% of respondents in Japan reported using mobile payments as their primary cashless payment method, indicating significant penetration of mobile payment technologies in everyday transactions. According to a [Dentsu Cashless Project survey conducted in December 2024](https://dentsu-ho.com/en/articles/9460), mobile payments had become the most frequently used cashless payment method in Japan.
The migration process involved systematically transferring all personal data, communication histories, payment methods, and device-linked services. This empirical approach allowed direct observation of technical, regulatory, and user experience barriers. Detailed logs and verification notes document the step-by-step challenges encountered, highlighting gaps between the DMA’s legal framework and practical exit feasibility.  
Table 1: The main services migrated, their expected portability under DMA principles, the observed barriers, the required workarounds, and the resulting exit cost types.  
| **Category**  | **Service / Component**  | **Expected portability under DMA principles**  | **Observed barrier**  | **Required workaround**  | **Exit cost type**  |  
| --- | --- | --- | --- | --- | --- |  
| Payments / Transit  | Suica (Apple Pay)  | Account/device independence  | Deregistration requires original iPhone hardware  | Physical device retention and manual removal  | Procedural + hardware lock-in  |  
| Messaging  |  iMessage history  | Data exportability  | No meaningful export or full history transfer  |  Archive loss or screenshot/manual saving  | Data + social lock-in  |  
| Identity / Security  |  Apple Keychain passwords  | Structured credential portability  | CSV export incomplete; 2FA not preserved  | Manual reconfiguration per account  | Identity reconstruction cost  |  
| Devices  | Apple Watch  | Cross-platform functionality  | Core features unavailable on Android  | Device replacement required  | Hardware dependency  |  
| Accounts / Services  | App-specific logins (multiple)  | Standardised reauthentication  | Repeated manual login and verification  | Individual resets and SMS verification  | Time + cognitive cost  |  
This experiment is informed by established theories of switching costs and platform lock-in in industrial organisation and platform economics, including Paul Klemperer’s [Markets with Consumer Switching Costs](https://www.jstor.org/stable/1885065) (1987), Farrell and Klemperer’s [Coordination and Lock-In: Competition with Switching Costs and Network Effects](https://doi.org/10.1016/S1573-448X\(06\)03031-7) (2007), the European Commission report [Competition Policy for the Digital Era](https://ec.europa.eu/competition/publications/reports/kd0419345enn.pdf) (2019), and the OECD report [Switching Costs and Consumer Policy in Digital Markets](https://www.oecd.org/daf/competition/switching-costs-and-consumer-policy-in-digital-markets.htm) (2021).
Methodologically, it follows a qualitative case-study approach as outlined in Robert K. Yin’s [Case Study Research and Applications](https://us.sagepub.com/en-us/nam/case-study-research-and-applications/book250150) (2018), combined with structured migration logs documenting each transfer step, failure point, procedural requirement, and user-side workaround. These observations allow an assessment not only of technical portability, but also of procedural, social, and hardware-based frictions that shape the real cost of exit.
### Quantitative scope of the migration
The migration covered approximately 120 user accounts and digital services across communication, finance, identity management, and hardware ecosystems. The figure refers to accounts and digital services I personally migrated and verified, primarily my own, with several family or administrative accounts managed directly by me. The process was conducted over five consecutive days and involved more than 25 hours of active transfer and verification work. During this process, 34 distinct friction or failure points were documented, including 11 cases requiring manual reconfiguration, 9 cases involving partial or failed data portability, and 6 instances of hardware-dependent constraints. These quantitative observations complement the qualitative logs and provide a structured estimate of the practical costs associated with platform exit.
## Case study 1: Financial and infrastructural lock-in (Suica and Apple Pay)
A prominent example is Japan’s Suica transit card, widely linked to Apple Pay. Despite Apple’s public messaging about portability, deregistering Suica from Apple Pay requires physical access to the original iPhone hardware. This procedural requirement forces users to retain Apple devices as a condition for exit, contradicting the premise of ecosystem independence.
This “hardware possession prerequisite” exemplifies how payment and transit infrastructures create layered lock-ins. Such design not only complicates switching but also raises concerns about consumer autonomy and market contestability. Moreover, this barrier is not addressed by the DMA’s current interoperability rules, which primarily focus on data access rather than procedural or device-based constraints.
## Case study 2: Digital identity, network effects, and social graph barriers
Messaging is another critical domain where exit penalties manifest. Apple’s iMessage histories cannot be meaningfully exported or migrated, effectively stranding years of personal communication within Apple’s ecosystem. This loss is not just technical; it entails significant social and economic consequences amplified by strong network effects – where the value of a communication platform grows with the number of users.
Many users rely on historical message archives for personal memory, business contacts, and proof of agreements or transactions. The sudden loss or fragmentation of these archives imposes psychological barriers and economic risks, making switching prohibitively costly beyond mere inconvenience.
Similarly, passwords and credentials stored in Apple Keychain lack seamless and secure end-to-end export mechanisms. While some basic export functions exist (e.g., CSV), these do not reliably preserve two-factor authentication (2FA) settings or maintain consistent formatting. This forces users into manual, error-prone reconstructions of their digital identities across hundreds of accounts, jeopardising account security and user experience.
These frictions highlight how “data portability” in the DMA remains narrowly defined and insufficient in addressing real-world identity migration. According to Article 6 of the EU Digital Markets Act (Regulation (EU) 2022/1925), designated gatekeepers must ensure effective interoperability and data portability sufficient to enable real-world platform switching.
## Case study 3: Hardware dependencies and sustainability implications
Beyond software and data, hardware dependencies further deepen exit penalties. Devices like Apple Watch lose core functionalities outside their native ecosystems without technical necessity, forcing users to abandon or replace expensive hardware prematurely.
This forced obsolescence leads to increased electronic waste (e-waste), raising sustainability concerns aligned with the EU’s broader environmental and sustainability regulatory agenda.
The incompatibility of such hardware contradicts the DMA’s broader goals of fair competition and consumer protection. Addressing platform lock-in must therefore extend to environmental impacts, ensuring that ecosystem exit does not translate into increased e-waste and resource depletion.
## The regulatory gap in DMA Article 6
Article 6 of the DMA emphasises interoperability and data portability as keys to unlocking platform monopolies. However, current provisions concentrate predominantly on facilitating entry and daily usage rather than enabling seamless and cost-free exit.
This asymmetry creates a regulatory blind spot. Platforms can comply with the letter of the law while embedding architectural and procedural exit barriers. These exit penalties undermine the DMA’s intent to foster consumer sovereignty, competition, and innovation. An expanded policy focus is needed – one that addresses procedural exit costs, identity portability in full context, and hardware dependencies to ensure genuinely reversible platform participation.
## Conclusion and policy recommendations
The Japanese migration experience provides a detailed, real-world perspective on exit penalties concealed within the EU’s current regulatory framework. Prior research on platform lock-in and switching costs has long shown that formal data portability often fails to translate into practical exit, reinforcing the structural nature of these barriers beyond individual user experience.
This case can be read as a preview for the EU: as digital identity and payment systems become more tightly integrated into hardware ecosystems, similar forms of exit friction are likely to emerge beyond Japan.
Effective digital sovereignty requires users to switch ecosystems without systemic loss or punitive costs.
To close this gap, EU policymakers should:
• Expand interoperability definitions beyond data formats to include procedural and hardware considerations;
• Mandate comprehensive portability of digital identity and communication histories;
• Integrate environmental sustainability into platform governance to address hardware obsolescence and e-waste;
• Develop enforcement mechanisms that penalise hidden exit barriers, ensuring genuine consumer autonomy.
Only by addressing these hidden walls can the DMA fulfill its promise of empowering users and preserving open, contestable digital markets.
Further information:
Contact: natsumikan163@gmail.com
