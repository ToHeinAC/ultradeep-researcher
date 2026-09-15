---
title: Crowd Control, Momentum and Concentrated Markets | MSCI
id: crowd-control-momentum-and-concentrated-markets-msci
tags:
- apple-earnings-durability-thesis-b8b3f1
- factor-crowding
- msci
- interested-party
created: '2026-09-13T06:16:31.193837Z'
updated: '2026-09-15T19:32:22.149172Z'
source: https://www.msci.com/research-and-insights/blog-post/crowd-control-momentum-and-concentrated-markets
source_domain: www.msci.com
fetched_at: '2026-09-13T06:16:31.176486Z'
fetch_provider: crawl4ai
status: review
type: note
tier: unknown
content_type: unknown
deprecated: false
summary: 'MSCI Research blog (Sze, Doole, Kumar; Dec 6, 2024). PROVENANCE: MSCI sells
  the underlying Security Crowding Model and Global Equity Factor Trading Model to
  institutional clients -- an interested party promoting its own crowding analytics;
  treat findings as vendor-marketing-adjacent, though the underlying methodology description
  and long-run backtest statistics are still informative.\n\nMethodology: the MSCI
  integrated crowding SCORE measures stocks on valuation (P/E and/or P/B), short interest,
  momentum, liquidity, and residual volatility, BOTH cross-sectionally (vs other stocks)
  and time-series (vs own history); exact weights are in the MSCI Security Crowding
  Model Factsheet. A related crowding FACTOR is built for the equity risk model by
  neutralizing the score against standard factors -- in practice this mostly strips
  out momentum exposure, isolating a mean-reversion-of-valuation signal.\n\nKey backtest
  results (MSCI ACWI Investable Market Index constituents, Jan 1997-Oct 2024): the
  crowding factor has generated persistently NEGATIVE returns (near-monotonic decile
  relationship, information ratio of -1.5 globally, -0.8 to -1.5 across regions, i.e.
  annualized factor return of -0.9% to -1.2%/year) -- i.e., high time-series-crowding-score
  stocks systematically de-rate. The signal is slow-moving: monthly cross-sectional
  serial correlation of exposure is 0.87, and predictive power persists into the 2nd
  and 3rd month, not just the 1st. Crowding-score spreads widen especially around
  the dot-com bust, the 2008 GFC, and COVID-19. Practical application: adding a time-series-crowding-score
  constraint (crowding score below market) to a momentum strategy with a 3% tracking-error
  budget improved risk/return versus unconstrained momentum, because it filters out
  ''overbought'' high-momentum names -- consistent with the well-documented value/momentum
  interaction (cites Asness, Moskowitz & Pedersen 2013 ''Value and Momentum Everywhere'').
  Does not analyze Apple or name-specific crowding; framework is index/portfolio-level.'
utility_score: 13.0
---

# Crowd Control, Momentum and Concentrated Markets
Blog post
5 min read
[Donald Sze](https://www.msci.com/research-and-insights/contributor/donald-sze), [Stuart Doole](https://www.msci.com/research-and-insights/contributor/stuart-doole), [Anurag Kumar](https://www.msci.com/research-and-insights/contributor/anurag-kumar)
December 6, 2024
Key findings
  * Equity investors seeking to manage their portfolio risk in concentrated, sentiment-driven markets could use quantitative tools to help identify where the greater risk of de-rating lives.
  * We show how the integrated crowding score can be used to build insight, leveraging its relationship with time-series valuations.
  * We translate this signal information into portfolio construction by showing how a simple constraint based on the time-series crowding score has improved the risk/return characteristics of a momentum-based strategy.


Global equity markets remain highly concentrated, [creating headwinds for active managers to express their best ideas and manage portfolio risk](https://www.msci.com/research-and-insights/paper/divide-and-conquer). Using the MSCI Security Crowding Model and the related factor built into the MSCI Global Equity Factor Trading Model, we demonstrate how portfolio managers can better identify the securities potentially most vulnerable to future de-rating. Additionally, we show how to translate these pure factor perspectives into a practical portfolio-construction technique. This approach could be particularly relevant to strategies with a strong sentiment exposure.
Identifying stocks vulnerable to de-rating
Stocks with a high MSCI integrated crowding score can be thought of as representing a "happy hunting ground" for companies vulnerable to de-rating. These stocks tend to be more expensive, riskier and highly traded, with sentiment and multiples that have increased sharply relative to their own history as well as to the market.[1] The associated crowding factor focuses on the time-series aspect to better fit into an equity risk model. Any such clash is further reduced by neutralizing it against familiar standard factors — in practice, it is the momentum exposures that are largely removed. Therefore, stocks flagged by the crowding score, and which also score highly on the crowding factor, could be sold from a portfolio without fighting against the momentum factor. Indeed, the portfolio could benefit from the factor return earned from the reversion of stock valuations. This last point is borne out by our findings that show the crowding factor has steadily generated negative returns for MSCI ACWI Investable Market Index (IMI) constituents since 1997 (this result is resilient to changes in region[2]). Decile portfolios show a near-monotonic relationship between a higher crowding factor and negative excess return.
Higher crowding factor exposures are associated with negative returns
Data from January 1997 to October 2024. Annualized decile returns are calculated using monthly excess returns. Decile portfolios are square-root cap-weighted.
This relatively slow-moving signal has had predictive power not only in the next month, but also, materially, in the second and third months.[3] Stock-specific residual volatility follows an analogous trend over these horizons.
Crowding factor has had a predictive power over a three-month horizon
Data from January 1997 to October 2024. Annualized decile returns are calculated using monthly excess returns. Decile portfolios are square-root cap-weighted. Decile spread is the difference in return of the top- and bottom-decile portfolios.
Integrating crowding scores into portfolio construction
Purely in factor terms, the difference between the information in the score and the factor-model exposure can be seen in the quintile return spreads, especially in the dot-com bubble's bursting, the 2008 global financial crisis and the COVID-19 pandemic.
Historically, the crowding score has been more volatile than the crowding factor
Data from January 1997 to October 2024. Quintile portfolios are square-root cap-weighted.
Since the realized crowding score correlates with its input components, its long-short return spread reflects all of their influences, especially, momentum's. In contrast, the key influence on the model factor's return is the mean reversion of stock valuations.
Correlation of crowding score with select equity factors
Data from January 1997 to October 2024. Average monthly cross-sectional correlations of integrated crowding score with select model factors for constituents of the MSCI ACWI IMI.
How might a portfolio manager directly control the aggregate "de-rating risk" in their portfolios? We begin by looking at the underlying signals. With time-series value as the key driver of the crowding factor's strong returns, and given value and momentum's well-known historical relationship,[4] we would expect to see an improvement in the behavior of the momentum factor when it is combined with information from a crowding score. We established this by adding a crowding score in a customization of our long-term factor models and observed how momentum's behavior shifted across time and regions.[5]
Time-series crowding-score signals improved behavior of momentum factor
Data from January 1997 to October 2024. Monthly factor return to momentum in MSCI Equity Factor Models (Long Term) as base case, then augmented with the time-series crowding score and the time-series valuation score.
A two-factor alpha is not needed to consistently incorporate this finding in portfolio construction. Instead, we can use a simple constraint based on the crowding score. We constructed a monthly rebalancing strategy that maximizes, at the portfolio level, the momentum exposure with a predicted tracking-error limit of 3% and a time-series crowding score below that of the market.[6] In the long run, this simple time-series approach using a crowding-score-based constraint has produced favorable risk/return outcomes because it helps ensure that stock selection within high-momentum quintiles avoids overbought stocks.
A simple crowding-score constraint improved risk/return outcomes
Data from January 1999 to October 2024. The monthly "simple" momentum strategy maximizes, at the portfolio level, the momentum exposure with a predicted tracking-error limit of 3% and is "enhanced" by a constraint on the time-series crowding score to be below that of the market.
The score constraint applied to high-momentum scores also enforces a strong average underweight of the crowding factor (active -0.5 standard deviation for this period and universe) because of the neutralization. The neutralization prevents the equivalent factor-based constraint delivering the same control.
A simple constraint on crowding score forces a strong control on the crowding factor
Data from January 1999 to October 2024. Active factor exposures are monthly averages using the EFMGEMTR model. We show factors with absolute median active exposure over 0.1 standard deviation.
The crowding score and a control on momentum
In concentrated markets, investors can become wary of portfolios dominated by sentiment factors. We have shown how the crowding score can help investors identify securities most at risk of de-rating. Uncrowded, high-momentum stocks have performed well, while crowded, lower-momentum stocks have been vulnerable to price correction. We also translated these insights into a simple constraint that has historically improved momentum-based strategies, leveraging the well-known value/momentum interaction.
[ Donald Sze Executive Director, MSCI Research & Development ](https://www.msci.com/research-and-insights/contributor/donald-sze)
[ Stuart Doole Managing Director, MSCI Research & Development ](https://www.msci.com/research-and-insights/contributor/stuart-doole)
[ Anurag Kumar Senior Associate, MSCI Research & Development ](https://www.msci.com/research-and-insights/contributor/anurag-kumar)
## 
Subscribe today
to have insights delivered to your inbox.
Subscribe
#### MSCI Security Crowding Model
#### Can Crowding Scores Quantify US Stocks’ Fragility?
#### Crowd Control for Fund Managers
1 Formally, the score measures stocks based on their valuation (price-to-earnings and/or price-to-book ratios), short interest, momentum, liquidity and residual volatility relative to other stocks (cross-sectional) and relative to their own history (time-series). Exact weights are in the MSCI Security Crowding Model Factsheet, Realized loadings align with the model.2 The information ratio (IR) globally is -1.5 between January 1997 and October 2024: the third-strongest risk-adjusted monthly return among the styles in the MSCI Global Equity Factor Trading Model. Across regions, the IR varies between -0.8 to -1.5 (an annualized factor return of -0.9% to -1.2% per year over the same period.)3 The average monthly cross-sectional serial correlation of the exposure is 0.87 in the MSCI Global Equity Factor Trading Model between January 1997 and October 2024.4 See, for example, Clifford Asness, Tobias Moskowitz and Lasse Pedersen, “Value and Momentum Everywhere,” Journal of Finance 68, no. 3, 2013, and Clifford Asness, “Momentum in Japan: The Exception that Proves the Rule,” Journal of Portfolio Management 31, no. 4, 2011.5 We ran monthly cross-sectional factor-return regressions between January 1997 and October 2024 with the latest MSCI Equity Factor Models (Long Term) for a given region, as the base case.6 We can consider this a proxy for any sentiment-driven investment strategy. In the simulation, we limited annual turnover to 100% and active positions to less than 50 times benchmark weight. Active factor exposures are monthly averages using the EFMGEMTR model. We show factors with absolute median active exposure over 0.1 standard deviation.
The content of this page is for informational purposes only and is intended for institutional professionals with the analytical resources and tools necessary to interpret any performance information. Nothing herein is intended to recommend any product, tool or service. For all references to laws, rules or regulations, please note that the information is provided “as is” and does not constitute legal advice or any binding interpretation. Any approach to comply with regulatory or policy initiatives should be discussed with your own legal counsel and/or the relevant competent authority, as needed.
We use cookies to optimize site functionality and give you the best possible experience. For more information, please review our[Cookie Notice](https://www.msci.com/cookie-policy)
Manage Cookies
Reject Accept
## Privacy Preference Center
This website uses cookies and other tracking technologies to collect information about your website experience for analytics, advertising, and other purposes. For more information, please visit our: [Cookie Notice](https://www.msci.com/cookie-policy)
Accept
###  Manage Consent Preferences
#### Strictly Necessary Cookies
Always Active
These cookies are necessary for the website to function and cannot be switched off in our systems. They are usually only set in response to actions made by you which amount to a request for services, such as setting your privacy preferences, logging in or filling in forms. You can set your browser to block or alert you about these cookies, but some parts of the site will not then work. These cookies do not store any personally identifiable information.
Cookies Details
#### Performance Cookies
Performance Cookies
These cookies allow us to count visits and traffic sources so we can measure and improve the performance of our site. They help us to know which pages are the most and least popular and see how visitors move around the site. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies we will not know when you have visited our site, and will not be able to monitor its performance.
Cookies Details
#### Analytics Cookies
Analytics Cookies
These cookies allow us to analyze how visitors use our site so we can improve user experience and site functionality. They help us understand user interactions across the site, such as navigation patterns and content usage. All information these cookies collect is aggregated and therefore anonymous. If you do not allow these cookies, we will be unable to analyze site usage or improve how users interact with our website.
Cookies Details
#### Functional Cookies
Functional Cookies
These cookies enable the website to provide enhanced functionality and personalisation. They may be set by us or by third party providers whose services we have added to our pages. If you do not allow these cookies then some or all of these services may not function properly.
Cookies Details
#### Targeting Cookies
Targeting Cookies
These cookies may be set through our site by our advertising partners. They may be used by those companies to build a profile of your interests and show you relevant adverts on other sites. They do not store directly personal information, but are based on uniquely identifying your browser and internet device. If you do not allow these cookies, you will experience less targeted advertising.
Cookies Details
Back Button
### Cookie List
Search Icon
Filter Icon
Clear
  * checkbox label label


Apply Cancel
Consent Leg.Interest
checkbox label label
checkbox label label
checkbox label label
Reject Confirm My Choices
