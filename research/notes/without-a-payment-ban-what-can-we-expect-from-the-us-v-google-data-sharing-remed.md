---
title: Without a Payment Ban, What Can We Expect from the US v. Google Data Sharing
  Remedies? – Knight-Georgetown Institute
id: without-a-payment-ban-what-can-we-expect-from-the-us-v-google-data-sharing-remed
tags:
- apple-earnings-durability-thesis-b8b3f1
- google-tac
- antitrust-remedy
created: '2026-09-12T17:24:47.952400Z'
updated: '2026-09-15T19:32:21.990842Z'
source: https://kgi.georgetown.edu/research-and-commentary/without-a-payment-ban-what-can-we-expect-from-the-us-v-google-data-sharing-remedies/
source_domain: kgi.georgetown.edu
fetched_at: '2026-09-12T17:24:47.930916Z'
fetch_provider: crawl4ai
status: review
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'KGI/Georgetown analysis (Alissa Cooper) of Judge Mehta''s Sept 2, 2025 US
  v. Google remedies opinion: default payments to Apple/Samsung/Mozilla ("tens of
  billions of dollars per year") are NOT banned; only exclusive distribution deals
  are barred. Mehta expects gen-AI competitive pressure and fears distributors would
  suffer without Google payments; he retains authority to revisit a payment ban later
  if competition doesn''t materialize, on an undefined timeline tied to appeals. Also
  critiques watered-down data-sharing remedies (one-time web-index snapshot instead
  of periodic; user-side query data capped at ''at least two'' transfers instead of
  periodic) as likely ineffective at eroding Google''s scale advantage (90% of queries
  overall, 95% mobile; 13 months of Google user data = 17 years of Bing data; 93%
  of queries seen only by Google vs 5% Bing-only). Links directly to the CourtListener
  PDF of the Sept 2 opinion and to the 2024 liability opinion PDF, and references
  KGI''s later related pieces ''Pay for Half'' and an amicus brief on appeal.'
utility_score: 16.0
---

#### Written by
[Alissa Cooper](https://kgi.georgetown.edu/people/alissa-cooper/)
_This commentary was originally published in[Tech Policy Press](https://www.techpolicy.press/without-a-payment-ban-what-can-we-expect-from-the-us-v-google-data-sharing-remedies/)._
On September 2, US District Court Judge Amit Mehta issued an [opinion](https://storage.courtlistener.com/recap/gov.uscourts.dcd.223205/gov.uscourts.dcd.223205.1436.0_5.pdf) that many in the tech industry had been waiting on for more than 15 years: a ruling about how to rectify Google’s maintenance of its illegal monopoly in online search. The most consequential aspect of the opinion is that the remedies will not meaningfully address the conduct at the center of the case: Google paying distributors like Apple, Samsung, and Mozilla tens of billions of dollars per year to lock in Google Search as the default on nearly every mobile phone and across much of the desktop browser market. The judge has allowed these default payments to continue based on his expectation that generative AI companies will exert competitive pressure on Google Search in the future, and out of concern that Google’s search distributors would suffer without default payments from the monopolist, while barring Google from striking exclusive distribution deals. 
[Many](https://www.nytimes.com/2025/09/07/opinion/google-ruling-antirust.html?smid=nytcore-ios-share&referringSource=articleShare) [have](https://www.techpolicy.press/decision-in-us-vs-google-gets-it-wrong-on-generative-ai/) [decried](https://www.thebignewsletter.com/p/a-judge-lets-google-get-away-with) the judge’s reasoning, raised concerns about Google’s ability to consistently win default contracts by using monopoly profits to outbid its competitors, and identified how much of a departure the remedy conclusions appear to be from the meticulously argued [liability opinion](https://files.lbr.cloud/public/2024-08/045110819896.pdf?VersionId=mHMw8uSvPbFCwl.7.yAY8wRXM0.UCmrD) issued in the case just one year prior. Judge Mehta notes that his court is prepared to revisit the idea of a default payment ban (or [other payment-related solutions](https://www.michiganstatelawreview.org/forum20242025/2025/2/26/nohvgtr4ci6rseqy9ghye05ubtjf6o), perhaps) if competition is not substantially restored through the other remedies. The timeline for revisiting the payment ban decision is uncertain given likely appeals in the case and to-be-determined conditions for reopening the payments question. 
While that question can’t be revisited soon enough, the intervening years provide time to try to understand how the other remedies might work and whether they can be expected to open the search market to competitors.
#### **Data sharing remedies**
Judge Mehta acknowledges that the legal precedent governing his court requires his ruling to, among other things, “deny to the defendant the fruits of its statutory violation.” He identifies Google’s scale achieved through illegal monopoly maintenance as one such “fruit,” and considers data sharing and syndication remedies as reasonable methods of addressing the scale advantage that Google gained via its illegal conduct. He also explains that these remedies would “help promote more competition” among search engines. In principle, including these remedies in the package sets an important precedent about the legitimacy of the remedial value of these approaches in technology markets. 
At the Knight-Georgetown Institute (KGI), we have worked with scholars and experts to [document in detail](https://kgi.georgetown.edu/research-and-commentary/considerations-for-effective-search-competition-remedies/) what it would take for search remedies to be effective. On the basis of that work, the more technical remedies included in the judge’s opinion create cause for concern.
In specifying the remedies related to data sharing (and syndication, although we do not discuss it further here), the court’s approach seems to take inspiration from the Plaintiffs’ proposals while paring them down significantly to meet some additional objectives the judge found to be important. Unfortunately in complex technology markets, the watering down can render what was a good idea to be an ineffectual one. This seems to be the case for both index data sharing and user-side data sharing.
#### **Web index data**
No search engine can operate without access to an index of the pages on the web, and Google’s index [appears](https://assets.publishing.service.gov.uk/media/68598b13eaa6f6419fade67b/Proposed_decision.pdf) to be at least an order of magnitude larger than its next closest rival. The Plaintiffs had proposed that Google be required to provide to qualified competitors at marginal cost the list of URLs in its index, along with metadata about each URL indicating its popularity, quality/authoritativeness, the last time Google crawled the page, and a few other data fields. Under the Plaintiffs’ proposal, Google would have been required to share this data on a periodic basis.
The judge pared down this proposal in several ways, including: the popularity and quality signals are not to be shared, and competitors can receive the data from Google one time only. The court claims that “[r]eceipt of this narrowed dataset will still enable rivals to overcome the scale gap by allowing them to more quickly build a competitive search index—one that is robust in volume, freshness, and utility.” The narrowing of the remedy calls this claim about future effectiveness into question.
Both phases of the trial saw significant testimony about the expense of building and maintaining a large search index, and it is widely understood that cost is a key reason why Google’s index is so much larger than even its closest competitor, Microsoft. Obtaining the list of URLs in the index is not the bulk of the expense, though. Deciding which pages to crawl, and then actually crawling and indexing them, is where Google’s scale advantage lies. The volume of signals that Google receives about which pages may have been updated recently and which pages are most important to index or re-crawl far outpaces any competitor. (Microsoft has organized an [entire industry initiative](https://www.indexnow.org/) to try to more systemically crowdsource freshness data from web sites directly, likely due to this scale disadvantage.) 
Having eliminated signals that might indicate popularity or freshness from the data set, competitors will be left with the time that the page was last crawled by Google. The court notes:
> The court … limited the Search Index data disclosure to one time, because Qualified Competitors with access to a one-time snapshot of Google’s Search Index will be able to use it to develop their own. … the court believes that, with the Search Index data, a Qualified Competitor will receive information about websites that Google crawls with greater frequency. With that knowledge, a Qualified Competitor can maintain a fresh search index on its own accord.
Here the court seems to confuse recency – which is what time-of-last-crawl indicates – with frequency. While some pages crawled recently might be crawled frequently (e.g., news site home pages), others may not (e.g., low-ranking or infrequently changing sites). When combined with other data that competitors may have, time-of-last-crawl might help differentiate obscure pages from those that are more often returned in search results. But since competitors will only be able to obtain one snapshot of this data at a single point in time, what they can learn from time-of-last-crawl will be somewhat ambiguous, because they will not have any additional snapshot to compare it with. 
The utility of the time-of-last-crawl field will obviously also fade over time. This appears to be by design, as the court notes that “successive disclosures would grant a Qualified Competitor fresher Search Index data.” 
In short, rivals who choose to buy this data from Google may find out about URLs that exist on the web that they otherwise would not know about based on their own, more limited web crawling and data acquisition deals. But in watering down the remedy, the court has reduced both the likelihood that rivals will be able to use this data to guide their own cost-efficient crawling and indexing and the time period over which this data might help them close the gap with Google. 
#### **User-side data**
Google’s scale advantages in both data and queries are massive. As explained in the liability opinion, Google receives about 90% of total queries (95% on mobile) compared to 6% for Bing (1% on mobile), its next closest competitor. The user-side click and query data that Google collects in 13 months is equivalent to 17 years’ worth of Bing user data. Google claims to see about [5 trillion searches per year](https://blog.google/products/ads-commerce/ai-personalization-and-the-future-of-shopping/), or about 14-16 billion searches per day, while [industry analysis](https://sparktoro.com/blog/new-research-google-search-grew-20-in-2024-receives-373x-more-searches-than-chatgpt/) conducted earlier this year estimated that ChatGPT sees about 38 million search-like prompts per day (out of about 2.5 billion prompts per day total [claimed](https://www.theverge.com/news/710867/openai-chatgpt-daily-prompts-2-billion) by OpenAI). Those are the scale advantages the user-side data sharing remedy is supposed to address. 
The Plaintiffs proposed that Google be required to make available to qualified competitors on a periodic basis three user-side data sets (with privacy and security safeguards applied): query-related data that Google uses to build and operate two separate models that influence the search engine results page, as well as user-side data Google uses to train its generative AI models used in search (presumably for AI Overviews and AI Mode) or generative AI products that access search.
Judge Mehta narrowed this proposal to exclude user-side data that Google uses to train search-related gen AI models. This is somewhat surprising given that much of the opinion is focused on the threat that generative AI poses or may pose in the future to search. By including the user-side data sets oriented towards traditional search but not AI-enabled features such as AI Overviews, the court appears to be picking some parts of the product to open to competitors and not others. Display of organic web results is presumed to have continued relevance for these rivals, but not AI summarization. The differential treatment of the user-side data sets is particularly puzzling given that the opinion finds that “AI Overviews has potentially strengthened Google’s position in the [general search engine] market.”
While the remaining two data sets could be expected to have utility for rivals to understand search behavior that they currently cannot see, the court may have undercut the utility of these data sets by constraining the frequency of rivals’ access. Judge Mehta changed the frequency of user-side data sharing from “periodic basis” to “at least twice,” with a to-be-defined cap on the total number of data transfers per competitor. The opinion does not state what period of time each of the two data transfers must cover.
Google has said that [15% of all queries are new](https://blog.google/products/search/search-language-understanding-bert/), never-before-seen each day. The Plaintiffs’ expert [examined a query log sample](https://files.lbr.cloud/public/2024-08/045110819896.pdf?VersionId=mHMw8uSvPbFCwl.7.yAY8wRXM0.UCmrD) and found that 93% of the queries were seen only by Google, whereas about 5% were seen only by Bing. Citing evidence from both trials, the remedy opinion itself states that “Google’s scale advantage is particularly pronounced with respect to [uncommon] long-tail, local, and fresh queries.” 
If the point of this remedy is to put rivals in a better position to compete with Google on quality, an occasional window into what they are missing by virtue of Google’s dominance does not seem designed to fit the bill. A similar remedy is available under the Digital Markets Act (DMA) in the European Union, where even quarterly disclosures have been [criticized](https://spreadprivacy.com/investigate-google-dma/) [as useless](https://legalblogs.wolterskluwer.com/competition-blog/alphabets-second-dma-compliance-workshop-a-self-reported-engaged-gatekeeper/) and few competitors are known to be buying the data from Google under those terms. Perhaps the court and the to-be-formed Technical Committee required under the ruling “to assist Plaintiffs and the court in implementing and enforcing the final judgment” will establish a more frequent basis for data sharing, but, if not, the utility of this remedy will be questionable.
#### **Moving forward**
Looking ahead, all eyes will be on the appeals process, the formation of the Technical Committee, and how rivals experiment with data sharing and other remedies. If concerns raised about the inadequacy of the remedy are demonstrated through the failure of competition to take hold, the manner and timeliness for Judge Mehta’s willingness to reopen and review the default payment issues will become critical. 
In KGI’s synthesis of [considerations for effective remedies](https://kgi.georgetown.edu/research-and-commentary/considerations-for-effective-search-competition-remedies/), we noted that both transparency from Google about its compliance plans and the establishment of performance-based benchmarks that base the court’s future action on actual market conditions will be key. Even with a pared down remit, the Technical Committee will have a varied set of responsibilities, requiring it to be established with sound governance and sufficient resources to handle the intricacies of these remedies. Time will tell whether the data sharing requirements and the remedies as a whole ultimately open the search market to new competitors, or if the court needs to reconsider the decision not to limit Google’s payments for search and generative AI default positions.
Share this content


###  _Related_ Work
[US v. Google Amicus Brief: How Better Remedies Can Restore Competition](https://kgi.georgetown.edu/research-and-commentary/us-v-google-amicus-brief-how-better-remedies-can-restore-competition/)
Brief / August 11, 2026
#### US v. Google Amicus Brief: How Better Remedies Can Restore Competition
The appeals in the United States v. Google search case hinge on a fundamental question: do the District Court’s remedies address the anticompetitive conduct that maintained Google’s search monopoly, or do they leave the market largely unchanged? Eight leading economists, legal experts, and technologists argue in an amicus brief that better remedies exist to help restore meaningful competition.
[Pay for Half: A Better Remedy for Google Search](https://kgi.georgetown.edu/research-and-commentary/pay-for-half-a-better-remedy-for-google-search/)
Commentary / July 15, 2026
#### Pay for Half: A Better Remedy for Google Search
The appeals of the United States v. Google search antitrust case turn in part on whether the remedies ordered address Google’s illegal monopoly in search – or whether, by declining to ban the payments Google makes for search defaults, the District Court has left the conduct at the heart of the case largely intact. In Pay for Half, KGI’s Alissa Cooper joins leading economists and competition experts in showing how the court can reasonably cap those payments rather than ban them, opening at least half of the market to rivals, including emerging AI-powered entrants, while preserving revenue for distribution partners.
[Designing Europe’s Search Data Sharing Rules for Competition in the AI Era](https://kgi.georgetown.edu/research-and-commentary/designing-europes-search-data-sharing-rules-for-competition-in-the-ai-era/)
Commentary / June 18, 2026
#### Designing Europe’s Search Data Sharing Rules for Competition in the AI Era
As the European Commission advances efforts under the Digital Markets Act to require Google to share its search data with competitors, lessons from historic antitrust remedies underscore how data access could be transformational in the AI-powered search market. While the Commission’s proposals represent a novel and comprehensive approach, key improvements to data scope and sharing frequency, privacy protections, and dispute resolution are needed. US courts and enforcers charged with implementing similar provisions should take note.
[Alissa Cooper](https://kgi.georgetown.edu/people/alissa-cooper/), [Zander Arnao](https://kgi.georgetown.edu/people/zander-arnao/)
  * Issues 
#### [Platform Governance](https://kgi.georgetown.edu/topics/platform-governance/)
    * [Platform Design in Policy and Industry](https://kgi.georgetown.edu/topics/platform-governance/platform-design-in-policy-and-industry/)
    * [Litigating Technology Design](https://kgi.georgetown.edu/topics/platform-governance/litigating-technology-design)
#### [Competition Policy](https://kgi.georgetown.edu/topics/competition-policy/)
#### [Artificial Intelligence](https://kgi.georgetown.edu/topics/artificial-intelligence/)
    * [Litigating Technology Design](https://kgi.georgetown.edu/topics/platform-governance/litigating-technology-design/)
    * [Agentic Information Future](https://kgi.georgetown.edu/topics/artificial-intelligence/agentic-information-future/)
[Learn more about the issues KGI works on here](https://kgi.georgetown.edu/issues/)
  * Research & Commentary 
    * [Artificial Intelligence](https://kgi.georgetown.edu/research-and-commentary/?topic_tax%5B%5D=117)
[Learn about our issues](http://kgi.georgetown.edu/issues/)
  * About 
    * [Expert Working Groups](https://kgi.georgetown.edu/expert-working-groups/)
[Learn more about us](http://kgi.georgetown.edu/about/)


## This site uses cookies.
We use cookies to enhance your browsing experience and analyze our traffic. To accept the use of cookies and close this dialogue, click the Accept button. To reject the use of cookies and close this dialogue, click the Reject button. View our [privacy policy](https://www.georgetown.edu/privacy-policy/).
AcceptReject
Manage Preferences
Notifications
