---
title: The EU’s Digital Markets Act Meets The Mobile OS, Round Two
id: the-eus-digital-markets-act-meets-the-mobile-os-round-two
tags:
- apple-earnings-durability-thesis-b8b3f1
- locus-lockin-durability-preference-vs-ai-interface
- dma-article-6-7
- ai-assistant-os-access
created: '2026-09-13T11:29:21.126233Z'
updated: '2026-09-15T19:32:22.177838Z'
source: https://www.forrester.com/blogs/the-eus-digital-markets-act-meets-the-mobile-os-round-2-can-the-push-for-a-fair-fight-go-too-far/
source_domain: www.forrester.com
fetched_at: '2026-09-13T11:29:21.106177Z'
fetch_provider: crawl4ai
status: review
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'Forrester analyst blog (Paddy Harrington) on DMA Article 6(7)''s requirement
  that third-party virtual/AI assistants get the same OS-level access as Apple''s
  and Google''s native assistants. Content is entirely about SECURITY risk of this
  mandate (malware/spyware already found in Apple App Store and Google Play; only
  ~40% of enterprise mobile environments use mobile antivirus and ~35% use mobile
  threat defense per Forrester''s 2026 Security Survey) -- it contains NO switching-rate
  data, no EU/DMA usage statistics, and no phone-level OS-migration figures. Relevance
  to this locus is narrow: it documents that DMA Article 6(7) is the specific legal
  hook forcing OS-level access parity for third-party AI assistants, which is tangentially
  related to the ''AI relocates the interface'' scenario (a third-party AI assistant
  with native-level OS access could theoretically compete for interface primacy on
  an iPhone without requiring a full OS switch) but does not address brand-preference
  durability or switching evidence directly.'
---

[Skip to content](https://www.forrester.com/blogs/the-eus-digital-markets-act-meets-the-mobile-os-round-2-can-the-push-for-a-fair-fight-go-too-far/#main)
[Home](https://www.forrester.com) > [ Featured Blogs ](https://www.forrester.com/blogs/) > The EU’s Digital Markets Act Meets The Mobile OS, Round Two 
# The EU’s Digital Markets Act Meets The Mobile OS, Round Two
Share
Currently, there is some contention between the leading mobile OS providers, Apple and Google, and the EU Commission with regards to the [Digital Markets Act (DMA)](https://digital-markets-act.ec.europa.eu/index_en), and it’s put me in a bit of a dilemma. Consumers should be able to do what they want with devices they purchase. But is there an obligation for OS developers, no matter the underlying platform (desktop, mobile, IoT, or OT), to protect the user from themselves? Let me explain.
A quick perusal of the DMA shows that it’s about ensuring fairness and competition when it comes to what they call “gatekeepers”; large digital platforms, like Amazon, Apple, Alphabet (Google), Meta, or Microsoft that provide core services like search and app stores. For Apple and Google, “gatekeepers” for mobile devices means these providers aren’t just offering an OS, but a plethora of services that have direct ties into the OS: app store, virtual assistant, search capabilities, browsers, and email, to name a few.
When it comes to mobile apps, Google has been transparent about fairness and interoperability, as Android allows using other apps’ stores, sideloading of apps, and switching the default of any Google-provided app to a third party. Apple has, until rather recently, been more closed and has made many structural changes to allow third parties access to the same functions. These changes only directly impact EU-resident (and now Japan) users of [Apple](https://www.apple.com/legal/dma/) — which comes across as a slight to non-EU customers and developers, as they should open the platforms for all customers globally, but that’s a different issue. Where things get heated is when we turn to AI and the [DMA’s Article 6(7)](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.L_.2022.265.01.0001.01.ENG#006.007). Yes, six-seven. The meme has become something real.
There is nothing specific in the DMA with regards to artificial intelligence, only to virtual assistants and that the same level of access given to native virtual assistants should apply to any third-party assistant that the phone’s owner wants to use. Because the current assistants shipped by Apple and Google are using AI, however, some of the arguments now concern whether the AI brought in through third-party virtual assistants have the same level of access as Apple and Google’s assistants. This is where things can quickly go off the rails and brings us to that crossroads.
Malware on smartphones is a serious problem, and we’re not just talking about apps that are sideloaded or downloaded from third-party stores; both [Apple](https://macdailynews.com/2025/02/06/researchers-find-photo-scanning-malware-on-apples-app-store-for-the-first-time/) and [Google](https://www.forbes.com/sites/daveywinder/2025/03/18/60-million-malicious-google-play-downloads-as-331-apps-bypass-security/) have had malware/spyware/trojans within apps hosted on their maintained app stores. These apps steal data, hijack identities, or possibly allow an attacker to compromise other apps and damage the user.
Because of how mobile OSes are designed, it’s rare for mobile malware to gain access the OS core and fully compromise the device. But by forcing open this door into the area where mobile virtual assistants play — interacting with the user for their input and retrieving and submitting information into any app that’s requested by the user, along with the changing settings within the OS, accessing the sensors, and, in the case of Google, accessing the searches that the user has done through their account — the EU Commissioners are playing with fire.
Virtual assistants directly interact with your applications, have read/write access to system configurations, stay resident on the system, and again, in the context of Google, have access to all other components, including search history, from your Google account, etc. If that assistant is malicious, not only would local device data be compromised, but your account data, data from other apps on the device, or even data from websites you accessed through that assistant could be compromised.
We also have to consider AI agents as virtual assistants. AI agents act on your behalf, but they are not you. They have their own identity, and when interacting with various layers on an endpoint or enterprise, they will take all necessary actions to complete their tasks. There have been occurrences where an agent took malicious actions, even when [prompted not to](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database). In the case of a smartphone, an AI-based virtual assistant could easily — either prompted by an attacker or simply by hallucination — prompt a user to take an [inappropriate action](https://www.theguardian.com/technology/2026/mar/20/meta-ai-agents-instruction-causes-large-sensitive-data-leak-to-employees) and expose themselves, or their business, to compromise.
The drive for fairness by the EU Commissioners and those who want control of the devices they own, and the data associated with them, is legitimate — so long as they acknowledge that if they do something silly with those devices, like downloading a random AI-powered virtual assistant and installing it on their smartphone, they should be responsible for the consequences of their actions. But is your average user, consumer or corporate, computer- and cybersecurity-savvy enough to know how to avoid unsavory apps and agents? What about business leaders? And defaulting to “our endpoint security solution will pick up any malicious actions” is invalid, because data from Forrester’s Security Survey, 2026 reveals that only about 40% of environments are using mobile antivirus and 35% are using mobile threat defense — the equivalent of endpoint detection and response for mobile.
So unless more security leaders begin deploying [mobile threat defense (MTD)](https://www.forrester.com/report/the-forrester-wave-tm-mobile-threat-defense-solutions-q3-2024/RES181072) solutions, they’re not going to have much insight into whether their users are using their mobile devices safely. And if they’re not deploying MTD on the BYO devices that connect to company resources, they end up with a compromised mobile device containing a rogue virtual assistant that could pilfer data or spread malware within their organization.
Forrester clients interested in this topic should connect with me to discuss via an inquiry or guidance session.
Share
###### Related Links
  * [The Digital Markets Act](https://digital-markets-act.ec.europa.eu/index_en)
  * [European Digital Markets Act (DMA) [Apple]](https://www.apple.com/legal/dma/)
  * [Researchers find photo-scanning malware on Apple’s App Store for the first time](https://macdailynews.com/2025/02/06/researchers-find-photo-scanning-malware-on-apples-app-store-for-the-first-time/)
  * [Google Play Warning—331 Dangerous Phone Apps Bypass Security Controls](https://www.forbes.com/sites/daveywinder/2025/03/18/60-million-malicious-google-play-downloads-as-331-apps-bypass-security/)
  * [Claude-powered AI agent’s confession after deleting a firm’s entire database: ‘I violated every principle I was given’](https://www.theguardian.com/technology/2026/apr/29/claude-ai-deletes-firm-database)
  * [Meta AI agent’s instruction causes large sensitive data leak to employees](https://www.theguardian.com/technology/2026/mar/20/meta-ai-agents-instruction-causes-large-sensitive-data-leak-to-employees)


###### Related Forrester Content
  * [The Forrester Wave™: Mobile Threat Defense Solutions, Q3 2024](https://www.forrester.com/report/the-forrester-wave-tm-mobile-threat-defense-solutions-q3-2024/RES181072)


###### Categories


###### See Paddy Harrington at:
Security & Risk Forum
November 9-10, 2026,  Washington DC 
[ Learn more and register ](https://www.forrester.com/event/security-risk/)
### Get The Insights At Work Newsletter
### Thanks for signing up.
Stay tuned for updates from the Forrester blogs.
### Get Trusted Advice — In Seconds
#### AI Access puts Forrester’s trusted insights at your fingertips. Validate your strategy, align your team, and get instant advice grounded in proprietary research — no digging, no delays. It’s like having a Forrester analyst by your side, 24/7.
[ Explore AI Access ](https://www.forrester.com/research/ai-access/)
Blog
##  [ The Information Security Leader’s Guide To Security & Risk Forum 2026 ](https://www.forrester.com/blogs/the-information-security-leaders-guide-to-security-risk-forum-2026/)
2 days ago 
From securing AI and modernizing identity to strengthening governance and resilience, security leaders face a rapidly expanding mandate. See how Security & Risk Forum 2026 can help you stay ahead of emerging challenges. 
[ Read More  ](https://www.forrester.com/blogs/the-information-security-leaders-guide-to-security-risk-forum-2026/)
Blog
##  [ OT Security’s Next Chapter Starts When Asset Discovery Stops Being The Goal ](https://www.forrester.com/blogs/ot-securitys-next-chapter-starts-when-asset-discovery-stops-being-the-goal/)
3 days ago 
OT security has moved beyond simply identifying connected devices. Learn why leading organizations are shifting their focus toward reducing operational risk, strengthening resilience, and enabling safer IT and OT security collaboration. 
[ Read More  ](https://www.forrester.com/blogs/ot-securitys-next-chapter-starts-when-asset-discovery-stops-being-the-goal/)
## Get The Insights At Work Newsletter
### Thanks for signing up.
Stay tuned for updates from the Forrester blogs.
