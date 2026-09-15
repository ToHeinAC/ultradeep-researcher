---
title: 'In Search of the Origins of Financial Fluctuations: The Inelastic Markets
  Hypothesis (Gabaix & Koijen, NBER w28967)'
id: in-search-of-the-origins-of-financial-fluctuations-the-inelastic-markets-hypothe
tags:
- apple-earnings-durability-thesis-b8b3f1
- inelastic-markets
- multiplier
- factor-crowding
created: '2026-09-12T17:36:03.157516Z'
updated: '2026-09-15T19:32:22.262693Z'
source: https://doi.org/10.3386/w28967
status: evergreen
type: note
tier: ground_truth
content_type: paper
deprecated: false
summary: 'Gabaix & Koijen, inelastic markets hypothesis (NBER w28967). IV estimate:
  $1 of net equity flow raises aggregate US market value by ~$5 (range $3-$8); aggregate
  demand elasticity ~0.2; ~100x larger price impact than rational models predict.
  Aggregate-market estimate, not stock-level.'
doi: 10.3386/w28967
citation_count: 252
venue: National Bureau of Economic Research
is_retracted: false
---

NBER WORKING PAPER SERIES
IN SEARCH OF THE ORIGINS OF FINANCIAL FLUCTUATIONS:
THE INELASTIC MARKETS HYPOTHESIS
Xavier Gabaix
Ralph S. J. Koijen
Working Paper 28967
http://www.nber.org/papers/w28967
NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
June 2021
We thank Ehsan Azarmsa, Aditya Chaudhry, Antonio Coppola, Zhiyu Fu, Dong Ryeol Lee, Hae-
Kang Lee, Simon Oh, and Lingxuan Wu for excellent research assistance. We thank Francesca 
Bastianello, Jean-Philippe Bouchaud, Michael Brandt, John Campbell, Francesco Franzoni, 
Robin Greenwood, Valentin Haddad, Lars Hansen, Sam Hanson, John Heaton, Tim Johnson, 
Arvind Krishnamurthy, Spencer Kwon, John Leahy, Hanno Lustig, Alan Moreira, Knut Mork, 
Toby Moskowitz, Stefan Nagel, Jonathan Parker, Lasse Pedersen, Joel Peress, Jean-Charles 
Rochet, Ivan Shaliastovich, Andrei Shleifer, Jeremy Stein, Johannes Stroebel, Larry Summers, 
Adi Sunderam, Jean Tirole, Harald Uhlig, Dimitri Vayanos, Motohiro Yogo, and participants at 
various seminars for comments. Gabaix thanks the Sloan Foundation for financial support. Koijen 
acknowledges financial support from the Center for Research in Security Prices at the University 
of Chicago Booth School of Business. The views expressed herein are those of the authors and do 
not necessarily reflect the views of the National Bureau of Economic Research.
NBER working papers are circulated for discussion and comment purposes. They have not been 
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies 
official NBER publications.
© 2021 by Xavier Gabaix and Ralph S. J. Koijen. All rights reserved. Short sections of text, not 
to exceed two paragraphs, may be quoted without explicit permission provided that full credit, 
including © notice, is given to the source.

In Search of the Origins of Financial Fluctuations: The Inelastic Markets Hypothesis 
Xavier Gabaix and Ralph S. J. Koijen
NBER Working Paper No. 28967
June 2021
JEL No. E7,G1,G32,G4
ABSTRACT
We develop a framework to theoretically and empirically analyze the fluctuations of the 
aggregate stock market. Households allocate capital to institutions, which are fairly constrained, 
for example operating with a mandate to maintain a fixed equity share or with moderate scope for 
variation in response to changing market conditions. As a result, the price elasticity of demand of 
the aggregate stock market is small, and flows in and out of the stock market have large impacts 
on prices.
Using the recent method of granular instrumental variables, we find that investing $1 in the stock 
market increases the market's aggregate value by about $5. We also develop a new measure of 
capital flows into the market, consistent with our theory. We relate it to prices, macroeconomic 
variables, and survey expectations of returns.
We analyze how key parts of macro-finance change if markets are inelastic. We show how 
general equilibrium models and pricing kernels can be generalized to incorporate flows, which 
makes them amenable to use in more realistic macroeconomic models and to policy analysis.
Our framework allows us to give a dynamic economic structure to old and recent datasets 
comprising holdings and flows in various segments of the market. The mystery of apparently 
random movements of the stock market, hard to link to fundamentals, is replaced by the more 
manageable problem of understanding the determinants of flows in inelastic markets. We 
delineate a research agenda that can explore a number of questions raised by this analysis, and 
might lead to a more concrete understanding of the origins of financial fluctuations across 
markets.
Xavier Gabaix
Department of Economics
Harvard University
Littauer Center
1805 Cambridge St.
Cambridge, MA 02138
and NBER
xgabaix@fas.harvard.edu
Ralph S. J. Koijen
University of Chicago
Booth School of Business
5807 S Woodlawn Ave
Chicago, IL 60637
and NBER
Ralph.koijen@chicagobooth.edu
An online appendix is available at http://www.nber.org/data-appendix/w28967

1
Introduction
One key open question is why the stock market exhibits so much volatility. This paper provides
a new model and new evidence suggesting that this is because of ﬂows and demand shocks in
surprisingly inelastic markets. We make the case for this theoretically and empirically, and delineate
some of the numerous implications of that perspective.
We start by asking a simple question: when an investor sells $1 worth of bonds and buys $1
worth of stocks, what happens to the valuation of the aggregate stock market? In the simplest
“eﬃcient markets” model, the price is the present value of future dividends, so the valuation of the
aggregate market should not change. However, we ﬁnd both theoretically and empirically, using
an instrumental variables strategy, that the market’s aggregate value goes up by about $5 (our
estimates are between $3 and $8, and we will use $5 for simplicity in the theory and discussion).1
Hence, the stock market in this simple model is a very reactive economic machine, which turns an
additional $1 of investment into an increase of $5 in aggregate market valuations.
Put another way, if investors create a ﬂow of 1% as a fraction of the value of equities, the model
implies that the value of the equity market goes up by 5%. This is the mirror image of the low
aggregate price-elasticity of demand for stocks: if the price of the equity market portfolio goes up
by 5%, demand falls by only 1%, so that the price elasticity is 0.2. In contrast, most rational or
behavioral models would predict a very small impact, about 100 times smaller, and a price elasticity
about 100 times larger. This high sensitivity of prices to ﬂows has large consequences: ﬂows in the
market and demand shocks aﬀect prices and expected returns in a quantitatively important way.
We refer to this notion as the “inelastic markets hypothesis.”
We lay out a simple model explaining market inelasticity. In its most basic version, a represen-
tative consumer can invest in two funds: a pure bond fund, and a mixed fund that invests in stocks
and bonds according to a given mandate — for instance, that 80% of the fund’s assets should be
invested in equities. Then, we trace out what happens if the consumer sells $1 of the pure bond
fund and invests this $1 in the mixed fund. The mixed fund must invest this inﬂow into stocks and
bonds: but that pushes up the prices of stocks, which again makes the mixed fund want to invest
more in stocks, which pushes prices up, and so on. In equilibrium, we ﬁnd that the total value of
the equity market increases by $5.
Then, the paper explores inelasticity in richer setups and ﬁnds that the ramiﬁcations of this
simple model are robust. For instance, the core economics survives, suitably modiﬁed, if the fund
is more actively contrarian, so that its policy is to buy more equities when the expected excess
return on equities is high. Moreover, the model aggregates well. If diﬀerent investors have diﬀerent
elasticities, the total market elasticity is the size-weighted elasticity of market participants. Impor-
tantly, the correct measure of size is the share of equity they hold. The model also clariﬁes how to
measure net ﬂows into the aggregate stock market (even though for every buyer there is a seller),
which guides the empirical analysis. Moreover, it extends readily to an inﬁnite horizon: in that
case, the price today is inﬂuenced by the cumulative inﬂows to date and the present value of future
expected ﬂows — divided again by the market elasticity.
The empirical core of this paper is to provide a quantiﬁcation of the market’s aggregate elasticity.
To do that, we use a new instrumental variables approach, which was conceived for this paper and
worked out in a stand-alone paper (Gabaix and Koijen (2020)), the “granular instrumental variables”
1The price impact is linear and symmetric: selling $2 worth of equities (buying $2 worth of bonds) decreases the
valuation of aggregate equities by $10.
2

(GIV) approach. The key idea is that we use the idiosyncratic demand shocks of large institutions
or sectors as a source of exogenous variation. We extract these idiosyncratic shocks from factor
models estimated on the changes in holdings of various institutions and sectors. We then take the
size-weighted sum of these idiosyncratic shocks (the GIV), and use it as a primitive instrument
to see how these demand shocks aﬀect aggregate prices and the demand of other investors. This
way, we can estimate both the aggregate sensitivity of equity prices to demand shocks (which is the
multiplier around 5 we mentioned above) and the demand elasticity of various institutions (around
0.2).
Importantly, the data are consistent with a quite long-lasting price impact of ﬂows. Indeed, in
the simplest version of the model, the price impact is perfectly long-lasting. This is not necessarily
because ﬂows release information, but instead simply because the permanent shift in the demand
for stocks must create a permanent shift in their equilibrium price. We perform a large number of
robustness checks, for example using diﬀerent data sets (the Flow of Funds as well as 13F ﬁlings).
The ﬁndings are consistent across speciﬁcations, in the sense that the price impact multiplier remains
around 5. We also construct a measure of capital ﬂows into the market. We ﬁnd that this measure
is strongly correlated with realized returns and survey expectations of returns, but it is only weakly
correlated with macroeconomic growth.
Here are three a priori reasons to entertain that markets would be inelastic
First of
all, if one wants to buy $1 worth of equities, many funds actually cannot supply that: for instance, a
fund that invests entirely in equities cannot exchange them for bonds. Many institutions have tight
mandates, something that we conﬁrm empirically. Relatedly, it is hard to ﬁnd investors who could
act as macro arbitrageurs. For instance, hedge funds are relatively small (they hold less than 5% of
the equity market), and they tend to reduce their equity allocations in bad times (due to outﬂows
and binding risk constraints; see Ben-David et al. (2012)). Second, the transfer of equity risk across
investor sectors is small (about 0.6% of the aggregate value of the equity market per quarter for
the average pair of investor sectors). This implies that the demand elasticity of most investors is
quite small or that investors experience nearly identical demand shocks (as if they were to disagree,
we would see large ﬂows in elastic markets), something which may be implausible. Third, a large
literature estimates demand elasticities for individual stocks using a variety of methodologies, where
the latest estimates of this “micro” demand elasticity are approximately 1 (we provide complete
references below).
As the macro elasticity should arguably be lower than the micro elasticity
(considering that, for example, Ford and General Motors are closer substitutes than the stock
market index and a bond), this suggests a low macro elasticity, perhaps less than 1. Consistent
with this reasoning, a new literature explores elasticities for “factors” in the US, such as size and
value, and ﬁnds elasticities of around 0.2. Hence, in light of this existing evidence, our low macro
elasticity may be less surprising.
Suppose that the “inelastic markets hypothesis” is true; why do we care?
First, investor-
speciﬁc ﬂows and demand shocks are quantitatively impactful. As a result, one can replace the “dark
matter” of asset pricing (whereby price movements are explained by hard-to-measure latent forces)
with tangible ﬂows and the demand shocks of diﬀerent investors. This suggests a research program
in which determinants of asset prices can be traced back to measurable demand shocks and ﬂows
of concrete investors. By studying the actions of these investors, we can infer their demand curves,
and theorize about their determinants.
3

If equity markets are indeed inelastic, several questions that are irrelevant or uninteresting in
traditional models become interesting. For instance, if the government buys stocks, stock prices go
up — again by this factor of 5. This may be useful as a policy tool — a “quantitative easing” policy
for stocks rather than long-term bonds. It may also be used to analyze previous policy experiments,
in Hong Kong, Japan, and China, and give a quantitative framework to complement the previous
qualitative discussions of policy proposals of this kind (Tobin (1998); Farmer (2010); Brunnermeier
et al. (2020)).
Also, ﬁrms as ﬁnanciers materially impact the market in our calibration. Prior research showed
that ﬁrms react to price signals, such as in their decisions to issue dividends or raise funds in stocks
versus bonds (Baker and Wurgler (2004); Ma (2019)): now we can quantify how ﬁrms’ actions
impact the market. For instance, stock buybacks can have a large aggregate eﬀect. Suppose that
the corporate sector buys back $1 worth of equities rather than paying $1 worth of dividends. In the
traditional Modigliani-Miller world, the market value of equities does not change at all. In contrast,
in an inelastic world, the value of equities goes up, by a tentative estimate of around $2.2 As a
naive non-economist might think, “if ﬁrms buy shares, that drives up the price of shares.” A rational
ﬁnancial economist might say that this is illiterate. But the naive thinking is actually qualitatively
correct in inelastic markets. Hence, potentially, as share buybacks account for a large portion of
ﬂows (they have been about as large as dividend payments in the recent decade), corporate actions
account for a sizable share of equity purchases, and therefore of the volatility and increase in the
value of the stock market. This “corporate ﬁnance of inelastic markets” is an interesting avenue of
research.
If markets are inelastic, then macro-ﬁnance should reﬂect that. Accordingly, we construct a
general equilibrium model in the spirit of Lucas (1978) where there is a central role for ﬂows and
inelasticity. It clariﬁes the role of demand shocks and ﬂows, the determination of the interest rate,
and shows how to augment traditional general equilibrium models with ﬂows in inelastic markets.
That makes those models more realistic, and better suited for policy. This model may serve as a
prototype for models enriched by inelasticity. Indeed, it calibrates well, and replicates quantitatively
the salient features of the stock market, such as the volatility and size of the equity premium, the
slow mean-reversion of the price-dividend ratio, and the ability to predict stock return with the
price-dividend ratio at diﬀerent horizons. We also show how the model can be used to match the
strong correlation between prices and subjective beliefs about long-term growth (Bordalo et al.
(2020)), even if ﬂuctuations in beliefs have only a modest impact on actions (Giglio et al. (2021a)),
as the resulting ﬂows are ampliﬁed in inelastic markets. We conclude that our general equilibrium
model with “inelastic markets” is competitive with other widely-used general equilibrium models
that match equity market moments, be it via habit formation (Campbell and Cochrane (1999)), long
run risks (Bansal and Yaron (2004)), or variable rare disasters (Gabaix (2012), Wachter (2013)).
In addition to proposing a new ampliﬁcation mechanism, its main advantage, as we see it, is that
is relies on an observable force, ﬂows in and out of equities.
We also show how to connect ﬂows to the “stochastic discount factor” (SDF) approach: the ﬂows
are primitive, and the SDF is a book-keeping device to record their inﬂuence on prices. This model
could be helpful to get correct risk prices in macroeconomic models, including their variation due
to ﬂows.
One limitation of our study is that we postpone to future research the detailed investigation
of what determines ﬂows in the ﬁrst place: instead, we provide descriptive statistics showing they
2The estimate is tentative, in part as it relies on estimates of the rationality of the consumer after the buybacks.
4

correlate sensibly with other variables, such as prices and measured beliefs. The reason is chieﬂy
that this would be a stand-alone paper. But we think it is quite doable, and indeed we are working
on this. Rather than studying “shocks to noise traders” abstractly, we replace them with investor-
level ﬂows and demand shocks that may be easier to understand. Indeed, episode by episode, one
can ask questions such as “why did ﬁrms lower their buybacks?” (answer: because they had lower
earnings), “why did pension funds buy?” (answer: because their mandate forces them to buy stocks
after stocks fall), or “why did hedge funds sell?” (answer: their investors sold, given their low past
returns).
Literature review
Our paper is about the macro elasticity, in contrast to the micro elasticity
estimated in the literature, including Shleifer (1986), Harris and Gurel (1986a), Wurgler and Zhu-
ravskaya (2002), and Duﬃe (2010).3 We summarize the evidence on existing elasticity estimates in
more detail in Section 2.4.
We build on the insights of De Long et al. (1990), who write an equilibrium model in which
noisy beliefs create demand shocks that move the market and the equity premium. They discuss a
rich set of qualitative ideas, some of which we can formally analyze and quantify, such as the failure
of the Modigliani-Miller theorem and the notion that if most market participants passively hold
the market portfolio, prices react sharply to ﬂows. De Long et al. (1990) dealt with these issues
qualitatively, but, inﬂuenced by it, a literature has studied the impact of mutual fund ﬂows in the
market, for example Warther (1995).4 In addition, an active literature studies the impact of mutual
fund and ETF ﬂows on the cross-section of equity prices, for instance Frazzini and Lamont (2008),
Lou (2012), Ben-David et al. (2018), Dou et al. (2020), and Dong et al. (2021). One innovation
of our paper is to provide a systematic quantitative framework to think about this, to include all
sectors (not just mutual funds), and to think about causal inference at the level of the aggregate
stock market via GIV. Deuskar and Johnson (2011a) use high-frequency order ﬂow data for S&P 500
futures to show that about half of the price variation can be attributed to ﬂows shocks. Moreover,
they ﬁnd these shocks to be permanent over the horizons that they consider.5
A few papers have modeled how ﬂows might be important, examining general ﬂows in currencies
(Gabaix and Maggiori (2015), Greenwood et al. (2019), Gourinchas et al. (2020)), slow rebalancing
mechanisms in currencies (Bacchetta and Van Wincoop (2010)) and equities (Chien et al. (2012),
who emphasize ﬂows coming from the supply of shares by ﬁrms), or switching between types of
stocks (Barberis and Shleifer (2003), Vayanos and Woolley (2013b)). However, we believe we are
the ﬁrst to conceptually and quantitatively explore the elasticity of the aggregate stock market using
a simple economic model to link data on total holdings and ﬂows to ﬂuctuations in the aggregate
stock market. We also provide the ﬁrst instrumental variables estimate of the elasticity of the US
equity market. Camanho et al. (2019) provide a partial-equilibrium model of exchange rates with
ﬂows, quantiﬁed with the GIV methodology developed for the present paper and spelled out in
3A growing literature studies elasticities in global ﬁnancial markets, see for instance Dierker et al. (2016) and
Charoenwong et al. (2020).
4See also Edelen and Warner (2001), Goetzmann and Massa (2003), and Ben-Rephael et al. (2012).
5Deuskar and Johnson (2011a) study a system of equations in which ﬂows may impact returns and returns may
impact ﬂows. To identify price impact, they rely on identiﬁcation via heteroskedasticity as in Rigobon (2003). As
only the demand shock in futures markets is used, and not in cash markets, we cannot directly translate the estimates
into multipliers. However, under the assumption that ﬂows in cash markets are highly correlated with ﬂows in futures
markets, their results do show that ﬂows explain a large fraction of market ﬂuctuations, which is consistent with the
inelastic markets hypothesis.
5

Gabaix and Koijen (2020).
A related literature ﬁnds convincing evidence that supply and demand changes do aﬀect prices
and premia in partially segmented markets, for bonds (for example as in Greenwood and Vayanos
(2014), Greenwood and Hanson (2013), and Vayanos and Vila (2020)), mortgage-backed securities
(Gabaix et al. (2007)), or options (Garleanu et al. (2009)), with models which typically feature
CARA investors and partial equilibrium. Here our focus is on stocks, while our model is quite
diﬀerent from the models in that literature (in particular, it avoids CARA restrictions on investor
preferences) and is also developed in general equilibrium.
Our work also relates back to the work on ﬂows and asset demand systems by Brainard and
Tobin (1968) and Friedman (1977), among others. This literature faced two important challenges
that we address; ﬁrst, data on asset holdings were not as readily available as they are now and,
second, there were no obvious methods to identify the slopes of asset demand curves. We share
with Koijen and Yogo (2019) and Koijen et al. (2019) our reliance on holdings data by institutions,
and the desire to estimate a demand function. We are mostly interested in the equilibrium in the
aggregate stock market, as opposed to the cross-sectional focus of Koijen and Yogo (2019), and
we emphasize the role of ﬂows, and the dynamics of prices and capital ﬂows over time. Using a
similar modeling strategy as in Koijen and Yogo (2019), Koijen and Yogo (2020) estimate a global
demand system across global equity and bond markets to understand exchange rates, bond prices,
and equity prices across countries. We also relate to the literature on slow-moving capital (Mitchell
et al. (2007); Duﬃe (2010); Duﬃe and Strulovici (2012); Moreira (2019); Li (2018)), providing a
new model for price impact with long-lasting eﬀects, and an identiﬁed estimation. Finally, part of
our contribution is a new model of intermediaries (He and Krishnamurthy (2013)), with a central
role for ﬂows, trading mandates, and inelasticity.
Much more distant to our paper is the theoretical microstructure literature (Kyle (1985)). There,
inﬂows cause price changes, but crucially those inﬂows do not change the equity premium on average
(as the mechanism is rational Bayesian updating, rather than limited risk-bearing capacity, unlike
Kondor and Vayanos (2019)), and hence do not create excess volatility. In contrast, in our paper,
inﬂows do change the equity premium, creating excessively volatile prices.
Outline
Section 2 gives some simple suggestive facts on equity shares and potential macro ar-
bitrageurs such as broker dealers and hedge funds. It also summarizes the existing literature on
elasticity estimates. Section 3 develops our basic model of the stock market: it lays out the basic
notions, and deﬁnes clearly elasticity and its link with price impact. It also gives the theoretical
framework that we take to the data. Section 4 contains the empirical analysis, including with an
instrumental variable estimation of the aggregate market elasticity. Section 5 provides a general
equilibrium model that helps to think about how everything ﬁts together: it specializes the ba-
sic model of Section 3 as it endogenizes the interest rate and links cash ﬂows to production and
consumption. Section 6 discusses how the eﬀectiveness of government policy and corporate ﬁnance
change with inelastic markets. Section 7 provides a conclusion and thoughts about the research
directions suggested by the present approach. The appendix contains the basic proofs, and details.
The online appendix contains a number of robustness checks and extensions.
Notations
We use E for equities, E for expectations, and E for equal-weighted averages. We
call δ the average dividend-price ratio of the equity market. We generally use lowercase notations
for deviations from a baseline. For a vector X = (Xi)i=1...N and a series of relative shares Si with
6

PN
i=1 Si = 1, we let XE :=
1
N
PN
i=1 Xi, XS := PN
i=1 SiXi, XΓ := XS −XE so that XE is the
equal-weighted average of the vector’s elements, XS is the size-weighted average, and XΓ is their
diﬀerence. We deﬁne the mean of Xi (with i = 1 . . . N) with weights ωi as: Eω [Xi] :=
P
i ωiXi
P
i ωi .
2
Data and Suggestive Facts on Equity Shares and Flows
In this section we document several stylized facts and discuss how they are related to our model and
to traditional, elastic asset pricing models. These facts are meant to be no more than suggestive:
the core empirical results are in Section 4, in which we try to carefully quantify the key parameters
of our model.
After discussing the data construction in Section 2.1, we document that institutions often have
quite stable equity shares in Section 2.2, and relatedly we seek to identify investors with elastic
demand for the aggregate stock market in Section 2.3. That is, we ask: who are the deep-pocketed
arbitrageurs that could make the aggregate stock market elastic? This question relates to the work
by Brunnermeier and Nagel (2004), who show that hedge funds did not provide elasticity to the
market during the technology bubble in the late nineties.
2.1
Data sources and construction
We summarize the data sources that we use and deﬁne some of the key variables. We leave a
detailed description for Appendix C.
We use sector-level data from the Flow of Funds (FoF) on holdings of equities and bonds as well
as ﬂows into both asset classes. Flows are diﬀerences in levels adjusted for mechanical valuation
eﬀects. We compute total bond holdings as the sum of Treasury and corporate bond holdings, and
analogously for ﬂows. As the FoF reports combined values of holdings and ﬂows of foreign and US
assets (except for Treasuries), we adjust these series (Appendix C.1.3). We assume that the ﬂows
transact at end-of-period prices. The sample is quarterly from 1993 to 2018 and we use the June
2019 vintage of the FoF data.6
We use monthly disaggregated data on assets under management, the share invested in US
equities, and ﬂows from Morningstar for mutual funds and ETFs that are domiciled in the US and
that have the US dollar as the base currency. We select the funds in Morningstar’s US category
groups “US Equity,” “Sector Equity,” “Allocation,” and “International Equity.”7 We use the sample
from 1993 to 2019 for mutual funds and from 2002 to 2019 for ETFs.8
For state and local pension funds, we use data from the Center for Retirement Research at
Boston College. The sample is from 2002 to 2019. We use data on the share invested in equities
and ﬁxed income as well as target holdings in equities and ﬁxed income (including cash). State and
local pension funds report once a year (although in diﬀerent quarters). We use a fund’s actual and
target allocation to equity and ﬁxed income and scale it so that the sum of the shares equals 100%
for each fund.
We use disaggregated data on equity holdings by institutional investors via form 13F ﬁlings. We
source the 13F ﬁlings from FactSet and the construction is as in Koijen et al. (2019). The sample
6Data of diﬀerent vintages can be downloaded from this website.
7We remove fund of funds in our analysis to avoid double counting.
8We omit a small number of fund-quarters in which the US equity share exceeds 300% or is lower than -300%, as
these may be data errors.
7

Figure 1:
Equity shares. The left panel of the ﬁgure plots the equity share in 1993 (orange bars)
and in 2018 (green bars) by institutional sector using Flow of Funds data. The right panel displays
the value-weighted average equity share of mutual funds, ETFs, and state and local pension plans.
The equity share of the diﬀerent institutions are averaged using the relative equity size of each
investor. The construction of the data is discussed in Appendix C.
0
.1
.2
.3
.4
.5
Households
Mutual funds
Foreign sector
ETFs
State & local pension funds
Private pension funds
Life insurance companies
Property & casualty insurers
Fed govt retirement funds
State and local govts
Broker dealers
Banks
Closed−end funds
2018
1993
0
.2
.4
.6
.8
1
Equity share
1993q1
1997q3
2002q1
2006q3
2011q1
2015q3
2020q1
Date
Mutual funds
ETFs
Pension funds (actual)
Pension funds (target)
is from 1999 to 2019.
We use quarterly data on real GDP growth from the St. Louis Federal Reserve Bank FRED
database, series GDPC1. Data on returns with and without dividends are from the Center for
Research in Security Prices. We use the monthly, value-weighted return with and without dividends
to compute the monthly dividend payment.
Lastly, we use survey expectations of returns from Gallup, as also used by Greenwood and
Shleifer (2014), who use the fraction of investors who are bullish (optimistic or very optimistic)
minus the fraction of investors who are bearish. We update their data, which starts in 1996.Q4, to
2018.Q4, and the resulting series has some gaps.
2.2
Institutions often have a quite stable equity share
As a point of reference, we summarize in Figure 1 the evolution of ownership of the US equity
market from 1993 (orange bars) to 2018 (green bars) based on FoF data. During the last 25 years,
equity ownership moved from households’ direct holdings to institutions. The ﬁgure understates
this trend as the “household sector” in the FoF includes various institutional investors such as hedge
funds and non-proﬁts (e.g., endowments). Broker dealers, who received much attention in the recent
asset pricing literature, hold only a small fraction of the US equity market. This limits their ability
to provide elasticity to the market.
For some of these sectors, such as mutual funds, exchange-traded funds, and pension funds, we
have investor-level data on equities and ﬁxed income holdings. In the right panel of Figure 1, we
plot the equity share. We aggregate diﬀerent investors in a given sector using the relative sizes of
their equity portfolios as opposed to assets under management, consistently with our theory (see
the discussion around 15). To appreciate the importance of this diﬀerence, consider an economy
with only pure equity and pure bond funds that have the same amount of assets under management.
The equity-weighted equity share equals 100% while the asset-weighted equity share equals only
8

50%. As the relative size of equity and bond assets move, so will the asset-weighted equity share.
Yet, the equity-weighted share will be a constant 100%. It is the equity-weighted equity share that
is relevant per our theory.
The plot shows that equity shares are quite stable over time for broad classes of investors. This
is consistent with many institutions having a rather rigid mandate to maintain a stable equity
share. In the model that we introduce in Section 3, this mandate rigidity will be captured by a low
elasticity (κ) of funds’ asset location to the expected return on equities. In recent work, Cole et
al. (2021) show that a large fraction of households9 also have a high average equity share at 79.2%
with little variation over time (the equity-weighted equity share only drops to 76.4% at the end of
2008). This stability is in part explained by the introduction of target date funds.
2.3
In search of macro arbitrageurs
Figure 1 shows that the equity shares of large groups of investors, such as mutual funds, ETFs, and
pension funds, are stable over time. As the foreign sector consists of similar institutions, this fact
naturally raises the question of who carries out arbitrage across asset classes or, equivalently, which
group of investors aggressively times the market. In the survey that we discuss in the introduction,
two investor sectors are frequently mentioned: hedge funds and broker dealers.10
As Figure 1 shows, broker dealers are very small and hold less than 0.5% of the equity market
directly. So while perhaps important for the micro elasticity, broker dealers are not well-positioned
to absorb large equity ﬂows over longer periods of time. The hedge fund sector is also quite small,
with holdings below 4% of the equity market in long positions going into the ﬁnancial crisis. Ben-
David et al. (2012) document two important facts. First, hedge funds sold a large fraction of their
equity holdings during the ﬁnancial crisis, averaging to 3.06% per quarter from 2007.Q3 to 2009.Q1.
Given their small size, this corresponds to selling on average 0.1% of the market each quarter (or
0.7% in total). Redemptions and leverage constraints explain about 80% of this decline in equity
holdings. Second, ﬂows across sectors are small. Ben-David et al. (2012) decompose the market
into hedge funds, mutual funds, short sellers, other institutional investors (e.g., pension funds and
insurance companies), and non-institutional investors (e.g., households). Measured as a fraction of
the market, these investor sectors sell or buy on average just 0.25% of the market per quarter. We
extend these calculations using data from the FoF for the technology crash in 2000-2002 and the
2008 global ﬁnancial crisis in Appendix D.3. As a fraction of the market, ﬂows between groups
average to at most 0.5% of the market.
In summary, many funds appear to have fairly tight mandates, hedge funds do not appear to
arbitrage the aggregate stock market and amplify demand shocks during severe downturns, and
ﬂows between sectors are small.
The small ﬂows across sectors has implications for the properties of demand shocks, which
are shocks to investors’ beliefs or risk appetite, given the elasticity of demand. The signature of
elastic demand is that disagreement among investors is associated with large ﬂows and quantity
movements. As ﬂows are small, theories featuring elastic demand imply that investors should agree
almost perfectly in their beliefs about expected growth rates and their riskiness, and also have similar
risk aversion. In inelastic markets, in contrast, there can still be large common shocks to beliefs, for
9Their sample appears to be representative of the middle 80% of the retirement wealth distribution of retirement
investors between age 25 and 65.
10While a large literature explores the micro elasticity of hedge funds, we are interested in their market elasticity.
In the FoF, hedge funds are part of the household sector and we cannot study them separately using these data.
9

instance as during the 2008 ﬁnancial crisis, but there is much more scope for disagreement.11 This
second interpretation of ﬁnancial markets may be more consistent with the data on beliefs, which
points to signiﬁcant ﬂuctuations in disagreement over time (Giglio et al. (2021a)).
2.4
The micro and macro elasticity of markets: Summary of existing
evidence
This paper is about the macro-elasticity of the market (that is, how the aggregate stock market’s
valuation increases if one buys $1 worth of stock by selling $1 worth of bonds). This is in contrast
with the very large literature that studies the micro-elasticity of the market (which describes how
much the relative price of two stocks changes if one buys $1 of one, and sells $1 of the other).
In Panel A of Table 1, we provide a summary of recent estimates of the micro multiplier, which is
the percent change in prices when an investors purchases a certain fraction of the shares outstanding
in a particular company, while controlling for movements in the aggregate market.12 While there is
a range of estimates, the order of magnitude of the multiplier is around 1. That is, buying 1% of
the shares outstanding of a given stock results makes its price increase by around 1%.
In addition, several recent studies have looked at the “factor-level” multiplier, which is the price
impact if an investor buys a fraction of the shares outstanding of a cross-sectional factor such as size
or value. We report those estimates in Panel B. The studies report a multiplier that is substantially
above 1 and closer to 5. In Panel C, we report recent estimates of the “macro multiplier,” the
parameter of interest in this paper, for the Chilean and Chinese stock markets. Once again, the
multiplier estimates are well above 1. Equivalently, the macro elasticity, which is the inverse of the
multiplier, is well below 1.
Taken together, the existing evidence in the literature suggests a micro multiplier around 1 (so,
a micro elasticity around 1), and a factor or macro multiplier that is well above 1 (so, a macro
elasticity below 1).
11To make this more concrete, using the notation of the next section, consider the simple decomposition of demand
∆qit = −ζ∆pt + f ν
it. If markets are as elastic as in standard models, say ζ = 10, then f ν
it = ∆qit + 10∆pt. As the
volatility of ∆qit is modest, demand shocks are largely dominated by the second term, 10∆pt, and almost perfectly
correlated. This leaves little room for disagreement among investors, even though this is widely document in beliefs
data, as the signature prediction of a model with elastic markets and belief disagreement is the presence of large
ﬂows coupled with small price changes. When markets are inelastic, say ζ = 0.2, then f ν
it = ∆qit + 0.2∆pt. Demand
shocks still contain a large common component, but the correlation between demand shocks is much lower and there
is more scope for disagreement.
12Also, the empirical market microstructure estimates of price impact are larger than what we ﬁnd: the price
impact that the microstructure literature ﬁnds is a factor of about 15 (Bouchaud et al. (2018); Frazzini et al. (2018)),
which may make our estimate of 5 seem moderate. Microstructure results are typically couched in a form such as
“buying 2.5% of the daily volume of a stock creates a permanent price increase of 0.15%”. At ﬁrst glance, values in
this range might appear to imply a small price impact. However, they work out to a large price impact multiplier of
M = 15: with 250 days of trading in a year, and a 100% per year turnover, the trade in our example would represent
a purchase of 2.5%
250 = 0.01% of the market capitalization of a stock, so that the impact of 0.15% on the price results in
a multiplier of 15. The interpretation of this kind of microstructure estimates requires some caution, as we discuss in
Section G.5. To sum up, a microstructure estimate of 15 may have the following interpretation: in inelastic markets
with a micro elasticity equal to 1, a large market-wide desired trade (“metaorder”) is on average split into 15 smaller
trades executed over time, by one or several institutions collectively (for example, by three funds pursuing a similar
strategy, each splitting their desired position change into ﬁve smaller trades). These microstructure estimates are
also themselves to be taken with caution, since identiﬁcation tends to be diﬃcult as trades are not exogenous to
prices. Using high frequency data with a GIV-based identiﬁcation may be a promising way to enrich identiﬁcation
procedures in microstructure.
10

Table 1: Multiplier estimates in the existing literature. The table reports multiplier estimates in
the existing literature for individual stocks (Panel A), factors such as size and value (Panel B), and
the aggregate stock market (Panel C). The multiplier is deﬁned as the percent change in prices per
percent change in shares outstanding purchased or sold by an investor. We discuss footnote 12 and
Appendix G.5 how to interpret the trade-level estimates of Frazzini et al. (2018) and Bouchaud et
al. (2018); here, we simply report the “prima facie” estimates.
Panel A: Micro multiplier
Methodology
Multiplier
Chang, Hong and Liskovich (2014)
Index inclusion
0.7 to 2.5
Pavlova and Sikorskaya (2020)
Index inclusion
1.5
Schmickler (2020)
Dividend payouts
0.8
Frazzini et al. (2018), Bouchaud et al. (2018)
Trade-level permanent price impact
15
Panel B: Factor-level multiplier
Ben-David, Li, Rossi and Song (2020a)
Morningstar ratings change
5.3
Peng and Wang (2021)
Fund ﬂows
4.8
Li (2021)
Fund ﬂows+SVAR
5.7
Panel C: Macro multiplier
Da, Larrain, Sialm and Tessada (2018)
Pension fund rebalancing Chile
2.2
Li, Pearson and Zhang (2020b)
IPO restrictions in China
2.6-6.5
How do these estimates compare to the elasticities implied by standard asset pricing models? It
is well known (e.g. Petajisto (2009)) that the micro elasticity in standard models is very large, of the
order of 1000 or above. This implies that the micro multiplier (the inverse of the micro elasticity)
is essentially zero and “demand curves are virtually ﬂat.” Based on the estimates reported in Table
1, the models are several orders of magnitudes oﬀin terms of the micro elasticity.
Our focus is on the macro elasticity and we compute it for various asset pricing models in Section
F.4.13 The summary is that in traditional, elastic asset pricing models the macro elasticity is around
10 to 20, leading to a multiplier around 0.1 to 0.05. As any two stocks are closer substitutes than
stocks and bonds, the micro multiplier is much lower than the macro multiplier in standard asset
pricing models. However, the micro multiplier as estimated in the literature (see Panel A) is already
an order of magnitude larger than the macro multiplier implied by standard asset pricing models.
The macro multiplier estimates are even larger, which deepens the disconnect between existing
estimates and asset pricing models. A multiplier of 0.05 implies that if a sovereign wealth fund, for
instance, were to buy 10% of the US aggregate stock market, prices would rise by just 50bp.
The profession’s view on the macro elasticity and the underlying mechanism
While
the disconnect between the empirical estimates and asset pricing models follows from the existing
literature, these facts have typically not been targeted in macro-ﬁnance asset pricing models. In
fact, as we will discuss now, this evidence does not appear to be widely known or accepted in the
profession.
13We discuss the elasticity in the models of Lucas (1978), Bansal and Yaron (2004), Barro (2006), Gabaix (2012),
and the link between our ﬁndings and Johnson (2006).
11

We quantify this via two surveys. We provide a detailed discussion in Section E and summarize
the main insights here. We conducted a ﬁrst survey by putting out a request via Twitter (using
the #econtwitter tag) to complete an online survey.
In addition, we asked participants of an
online seminar at VirtualFinance.org to complete the same survey – this latter audience being
naturally more representative of the population of academic researchers in ﬁnance. Both surveys
were conducted before the paper was available online and before the seminar was conducted. We
received 192 responses for the Twitter survey and 102 responses for the survey connected to the
ﬁnance seminar.
The survey question was the following: “If a fund buys $1 billion worth of US equities (perma-
nently; it sells bonds to ﬁnance that position), slowly over a quarter, how much does the aggregate
market value of equities change?” The answer given in this paper is M times a billion, where M is
the macro multiplier, which we estimate to be around M = 5. In both surveys, the median answer
was M = 0: surveyed economists, logically enough, rely on the traditional asset pricing model in
which prices are unperturbed by ﬂows. The median positive answer was M = 0.01.14 Hence, sur-
veyed economists’ views are in line with the traditional model, but far from the estimates reported
in the empirical literature, and the new estimates we provide.
We also asked about the sector supposedly providing elasticity to the market to be able to
explore the mechanism. The two most common responses were hedge funds and broker dealers.
As discussed before, those sectors are unlikely to provide elasticity to the aggregate market, in
particular during times of stress.
3
The Inelastic Markets Hypothesis: Theory
We now provide a model that we think is more realistic to think concretely about the determinants
of stock demand, and about how ﬂows impact prices. It is highly stylized, but will be useful to
think about the determinants of elasticity (both conceptually and in terms of calibration) and to
guide empirical work. We start with a two-period version, and then proceed to an inﬁnite-horizon
variant.
3.1
Two-period model
There is a representative stock in ﬁxed supply of Q shares, with an endogenous price P.
The
economy lasts for two periods t = 0, 1. The dividend D is paid at time 1. We call π = De
P −1 −rf
the equity premium (with De := E[D] the expected dividend at time 0 and rf the risk-free rate), ¯π
the average equity premium, and ˆπ := π −¯π the deviation of the equity premium from its average.
There is also a riskless bond with time-0 price equal to 1 (we endogenize the risk-free rate in Section
5).15
A representative consumer invests into stocks and bonds via I institutions or funds.16 We call
Wi fund i’s wealth (or equivalently assets under management) and Qi the number of stock market
14The answer M ≥1 was given by only 2.5% of respondents in the Twitter survey and by 4% of respondents in
the VirtualFinance.org survey. Section E provides further details.
15Here, ﬂows move equity prices but not bond prices. In the general equilibrium version of Section 5, this happens
because the consumer’s demand is inﬁnitely elastic with respect to bond prices. We sketch the case where both
equity and bond demands are inelastic in Section G.1: the economics is similar, replacing the elasticity by a matrix
of own- and cross-elasticities.
16Those funds act competitively, i.e. are price takers.
12

shares it holds. Therefore the fraction of fund i’s wealth invested in equities is PQi
Wi . We assume that
fund i’s demand for stocks is given by a mandate, saying that it should have a fraction invested in
equities equal to:17
PQi
Wi
= θieκiˆπ,
(1)
while the rest is in the riskless bond. In the simplest case, κi = 0, fund i has a ﬁxed mandate to
invest a fraction θi ≥0 of its wealth in equities. When κi > 0 the fund allocates more in equities
when they have higher expected excess returns (hence, κi indexes how contrarian or forward-looking
the fund is). This demand function appears sensible, and could be micro-founded along many lines
– but to go straight to the eﬀects we are interested in, we take it as an exogenous mandate.18′19′20
We use the index i = 0 for a special fund, a “pure bond fund” that only holds bonds (so, its θi and
κi are 0).
If consumers were fully rational, the mandate would not matter: consumers would undo all
mechanical impacts of the mandate. But consumers will not be fully rational, so mandates will
have an impact.
The elasticity of demand for stocks of a fund
We use bars to denote values at time t = 0−,
before any shocks. At that time 0−, fund i has wealth ¯Wi, and holds ¯Qi shares. We assume that
before the shocks, equities have an equity premium ¯π, so that the dividend-price ratio is at its
corresponding value, δ =
¯
De
¯P , where ¯P, ¯De are the baseline values for the stock’s price and the
expected dividend.
At time 0, the representative household invests ∆Fi extra dollars in each fund i (taking those
dollars from the pure bond fund), which represents a fractional inﬂow fi =
∆Fi
¯
Wi .
An outﬂow
corresponds to ∆Fi < 0. We study the impact of this on the aggregate market, independently of
the reasons for the ﬂows, which may be rational or behavioral. We also assume that there may be a
change d in the value of expected fundamentals. We call qi and d the fractional deviations of equity
demand and of the expected dividend from their baseline values:
qi = Qi
¯Qi
−1,
d = De
¯
De −1.
(2)
The next proposition gives the change in demand by fund i. Its proof is in Appendix A. We
perform the analysis for small disturbances fi, d, and hence small p, qi, here and throughout the
paper.21
17We write the mandate in “number of shares,” but it is equivalent to a “fraction of assets invested in equity”
formulation.
18This fund’s mandate can be viewed as a stand-in for other frictions such as inertia or a rule of thumb that a
behavioral household might follow for its stock allocation. As a result, the institutionalization of the market does
not necessarily result in more inelasticity as it depends on how households manage their own portfolios. Parker et
al. (2020) argue that the growth of target date funds made the market more elastic. In the our notation, target date
funds have κi = 0.
19Buﬀa et al. (2019) explore the implications of tracking error constraints on asset prices.
20The mandate does not feature volatility, as volatility is not crucial here to obtain demand curves (though volatility
is crucial for that in the traditional model). One could easily write extensions where the allocation decreases in
volatility. In the dynamic model, we add a demand shock that can include volatility terms.
21Following common practice in macro-ﬁnance, we do Taylor expansions of the leading terms, omitting the formal
mentions of O (·) terms.
13

Proposition 1. (Demand for aggregate equities in the two-period model) Fund i’s demand change
(compared to the baseline) is, linearizing:
qi = −ζip + κiδd + fi,
(3)
where δ is the baseline dividend-price ratio, and ζi is the elasticity of equity demand by fund i,
ζi = 1 −θi + κiδ.
(4)
The aggregate elasticity of demand for stocks, and the “representative mixed fund”
We
now move from fund-level demand to the aggregate demand for stocks, which is Q = P
i ¯Qi (1 + qi) .
We call W E
i the equity holdings (in dollars) of fund i, and Si its share of total equity holdings:
W E
i = QiP = θiWi,
Si =
¯W E
i
P
j ¯W E
j
=
¯Qi
P
j ¯Qj
.
(5)
Finally, for a given variable xi (with i = 1 . . . I), we deﬁne xS to be its equity-holdings weighted
mean:
xS :=
X
i
Sixi.
(6)
So, the aggregate demand change is:
q = ∆Q
Q =
P
i ¯Qiqi
Q
=
X
i
Siqi = qS.
To derive an expression for it, we take the individual demand curves (3), and consider their equity-
holdings weighted average, which gives the (linearized) aggregate demand curve for equities:
qS = −ζSp + κSδd + fS.
Proposition 2 sums this up.
Proposition 2. (Aggregate demand for aggregate equities in the two-period model) The aggregate
demand for equities is
q = −ζp + κδd + f,
(7)
where ζ = ζS = P
i Siζi is the equity-holdings weighted demand elasticity of all funds i, and likewise
for the other quantities:
θ = θS,
κ = κS,
ζ = ζS,
f = fS.
(8)
In particular, ζ is the macro elasticity of demand:
ζ = 1 −θ + κδ.
(9)
Hence, the universe of equity-holding funds in the model aggregates (up to second order terms in fi
and d) to a “representative mixed fund” with wealth W = PI
i=1 Wi, and whose mandate is to hold
an equity share PQ
W = θeκˆπ.
14

The “aggregate ﬂow into equities” is non-zero even though “for every buyer there is a
seller”
The equity-share weighted ﬂow fS = P
i Sifi in (8) can also be expressed as22
fS =
P
i θi∆Fi
¯W E
,
(10)
i.e. as the sum of the dollar inﬂows ∆Fi into each fund i, times the marginal propensity of fund i
to invest in equities, θi, as a fraction of the the baseline value of aggregate equities W E = Q ¯P.23
At the same time the net total ﬂow is 0, P
i ∆Fi = 0, as one bond removed from one fund goes to
another fund, and the net amount of equities purchased is 0, P
i ∆Qi = 0, as the net amount of
shares is constant:24
X
i
∆Fi = 0,
X
i
∆Qi = 0.
(11)
Hence, there is a well-deﬁned notion of “the aggregate ﬂow into equities,” fS (equation (10)) which
is generically non-zero, even though “for every buyer there is a seller” (equation (11)).
The impact of ﬂows on the aggregate price
We now analyze what happens after the aggregate
inﬂow fS in equities. We assume from now on that ζ > 0. As the supply of shares does not change,
we must have q = 0 in the equilibrium after the ﬂow shock. Given (7), we have 0 = q = −ζp + f,
and the price change must be p = f
ζ . Proposition 3 summarizes this.25
Proposition 3. Suppose that the representative consumer invests ∆Fi in each fund i, so that the
total inﬂow in equities is a fraction f = fS = P
i Si
∆Fi
¯
Wi of the value of equities. Then, the stock
price changes by a fraction p := P−¯P
¯P
equal to:
p = f
ζ ,
(12)
where ζ is the macro elasticity of demand deﬁned in (9).
This illustrates that ﬂows can have large price impacts if the price elasticity of demand ζ is
suﬃciently low, and shows the key role of this price elasticity, which is the center of this paper.26
An undergraduate example
To think through the economics of Proposition 3, we found the
following simple, undergraduate-level example useful. Suppose that there are just two funds: the
pure bond fund and the representative mixed fund, which always holds 80% in equities (the mag-
nitude suggested by Figure 1). Then, θ = 0.8, κ = 0, so that ζ = 1 −θ = 0.2 and 1
ζ = 5. Then an
extra 1% inﬂow into the stock market increases the total market valuation by 5%.
It is instructive to think through the logic of this example. Suppose that the representative
mixed fund starts with $80 in stocks (of which there are 80 shares, worth $1 each) and $20 in
22Indeed, as θi =
¯
W E
i
¯
Wi ,we have fS = P
i Sifi = P
i
¯
W E
i
W E
∆Fi
¯
Wi =
1
W E
P
i θi∆F E
i .
23This is analogous to the marginal propensity to take risk in Kekre and Lenel (2020).
24For instance, if there are just the pure bond fund and a mixed fund, then the bond ﬂow into the mixed fund
∆F1 is compensated by a ﬂow out of the pure bond fund, so ∆F0 = −∆F1.
25It is exact when all κi = 0 and it uses a ﬁrst-order Taylor expansion for small ﬂows f when κi̸ = 0.
26If d̸ = 0, there is an extra eﬀect, and p = f
ζ + κδ
ζ d, with κδ
ζ < 1. This implies that unaided by ﬂows, prices
under-react to fundamentals in inelastic markets.
15

bonds. There are also $B worth of bonds outstanding. Suppose now that an outside investor sells
$1 of bonds from the pure bond fund (he had $B −$20 in the pure bond fund, and now he has
$B −$21), and invests this $1 into the mixed fund. In terms of “direct impact”, there is a $0.8 extra
demand for the stock (equal to 1% of the stock market valuation), and $0.2 for the bonds. But that
is before market equilibrium forces kick in.
What is the ﬁnal outcome? In equilibrium, the pure bond fund still holds $B −$21 worth of
bonds. The balanced fund’s holdings are $21 in bonds (indeed, it holds the remaining $21 of bonds)
and 4 × $21 = $84 in stocks (as the balanced fund keeps a 4:1 ratio of stocks to bonds, the value
of the stocks it holds must be $84). As the balanced fund holds all 80 shares, the stock price is
P = $84
80 = $1.05, whereas it started at P = $1: stock prices have increased by 5%. The fund’s
value also has increased by 5%, to $105.
We see that the increase in stock prices is indeed by a factor 1
ζ =
1
1−θ = 5. Only $0.8 was
invested in equities, yet the value of the equity market increased by $4, again a ﬁve-fold multiplier.
We conclude with a few remarks.
Share repurchases and issuances are just a type of ﬂow
Suppose that corporations buy
back shares, meaning that they buy:
fC = Net repurchases (in value)
Total equity value
= −Net issuances (in value)
Total equity value
.
(13)
Then, the basic net demand for shares is as above, using the total ﬂow:
f := fS + fC,
(14)
which is equal to the size-weighted total ﬂow in the funds, fS, plus share repurchases (as a fraction
of the market value of equities). In short, on top of the traditional ﬂows of investors into equities,
we want to add share repurchases by corporations. In addition, if ﬁrms have a supply elasticity ζC,
then the basic equilibrium is: fS −ζp = −fC + ζCp. That is, a change in demand fS −ζp equals a
change in supply −fC + ζCp. Therefore p = fS+fC
ζ+ζC , so that the eﬀective market elasticity is ζ + ζC.
In much of the paper, we assume that the supply of shares is inelastic, ζC = 0, which will prove to
be a good approximation.
The representative mixed fund’s equity share vs. the market-wide equity share
There
are two notions of equity share. The traditional one is the wealth-weighted equity share:
θW =
W E
W E + W B =
Total value of Equities
Total value of Equities + Bonds,
(15)
which can also be expressed as θW =
P
i Wiθi
P
i Wi . The other one is the equity-holdings weighted equity
share deﬁned earlier, θS =
P
i W E
i θi
P
i W E
i , where W E
i
was the equity holding of fund i.
The former
share (θW) is directly available in aggregated data, while the latter (θS) is what matters for the
macro elasticity. They are diﬀerent, and indeed θS > θW.27 This makes the disaggregation issues
potentially non-trivial, and will require some care in the empirical part.
27Indeed, using W E
i = θiWi, θS = ES [θi] = P
i Siθi =
P
i W E
i θi
P
i W E
i
=
P
i Wiθ2
i
P
i Wiθi =
EW[θ2
i]
EW [θi] ≥EW [θi] = θW . As long as
there is a pure bond fund, the θi are not identical, and the inequality is strict. Formally, we assume that all funds
have weakly positive total wealth.
16

Take the undergraduate example with just two funds, the mixed fund and the pure bond fund,
and κ = 0. Then, whatever the ﬂows, θS = θ is always constant, pinned by the mandate θ of that
mixed fund. However, θW varies over time, as ﬂows in and out of equities change the market value
of equities, P.
3.2
Inﬁnite horizon model
We extend the static model to a dynamic one. The forces will generalize in an empirically imple-
mentable way. There is again a constant risk-free rate rf, taken here to be exogenous. Section 5
endogenizes it in general equilibrium, but here we concentrate on the core economics of inelasticity.
The representative stock gives a dividend Dt.
We consider the case where there is a pure bond fund and “representative mixed fund” trading
stocks and bonds. This allows us to zoom in on the core economics: an economy with several
funds can be represented via a single mixed fund to the leading order, as in Proposition 2.28 The
representative mixed fund has a mandate: the fraction invested in equities, PtQt
Wt , should be
PtQt
Wt
= θeκˆπt+νt,
(16)
where as before ˆπt := πt −¯π is the deviation of the equity premium from its average, and we allow
for additional demand shocks, νt. These can be thought of as shocks to tastes or perceptions of risk.
We assume that dividends and interest rates on bonds are passed to consumers: hence, reinvesting
dividends counts as an inﬂow.
To analyze this economy, it is useful to linearize it. This needs to be done around a simpler,
“baseline” economy, which is on a balanced growth path with a constant equity premium ¯π. We call
¯Pt, ¯Dt, ¯Wt, and ¯Q the baseline price, dividend, wealth, and quantity of shares held by the mixed
fund. We assume that
  ¯Pt, ¯Dt, ¯Wt

=
  ¯P0, ¯D0, ¯W0

Gt: they grow with a common cumulative growth
factor Gt, such that Gt+1
Gt
follows an i.i.d. growth process with mean g. As the equity premium is
always ¯π in the baseline economy, rf + ¯π −g = (1 + g) δ, with
¯Pt ¯Q
¯
Wt = θ and
¯Dt
¯Pt = δ.29 At the same
time, the bond holdings of the mixed fund are ¯B0 + ¯Ft, where ¯Ft is the cumulative dollar inﬂow
since time 0 (so ¯F0 = 0): the only “new” bonds that the representative mixed fund has must come
from inﬂows, like in the undergraduate model above. They should also represent a fraction 1 −θ of
the wealth of the fund, so that we have: ¯B0 + ¯Ft = 1−θ
θ ¯PtQ. This means that ¯Ft = 1−θ
θ
  ¯Pt −¯P0
 ¯Q.
This is the ﬂow consistent with a balanced growth path in the rational economy.
We call pt, wt, dt, qt the deviations from the baseline, so that dt = Dt
¯Dt −1, pt = Pt¯Pt −1, wt = Wt
¯
Wt −1,
and qt = Qt
¯Q −1. We deﬁne the ﬂow ft as the scaled cumulative inﬂow in excess of the baseline:30
ft = Ft −¯Ft
¯Wt
.
(17)
We call the expected dividend deviation de
t = Etdt+1. The expected excess return is πt = Et[∆Pt+1+Dt+1]
Pt
−
rf, and we use the following Taylor expansion (see Section F for a derivation):
ˆπt = δ (de
t −pt) + Et [∆pt+1] .
(18)
28This is detailed in Appendix G.7.
29Indeed, 1 + rf + ¯π = Et
h ¯
Pt+1+ ¯
Dt+1
¯
Pt
i
= Et
h ¯
Pt+1(1+δ)
¯
Pt
i
= (1 + g) (1 + δ) .
30This is extremely close to another deﬁnition, ft = Pt
s=0
∆Fs−∆¯
Fs
Ws−1
, but the above deﬁnition is the one warranted
by the theory.
17

The aggregate demand for stocks is as follows, generalizing (7).
Proposition 4. (Demand for aggregate equities in the inﬁnite-horizon model) The demand change
for equities (compared to the baseline) is
qt = −ζpt + ft + νt + κδde
t + κEt [∆pt+1] ,
(19)
where ζ = 1 −θ + κδ is the aggregate elasticity of the demand for stocks, as in (9).
As the total number of shares is constant, the equilibrium condition is given by qt = 0. This
yields the stock price as follows (the proof is in Appendix A).
Proposition 5. (Equilibrium price in the inﬁnite-horizon model) The equilibrium price of aggregate
equities is (expressed as a deviation from the baseline):
pt
=
Et
∞
X
τ=t
1
(1 + ρ)τ−t+1

ρfτ + ντ
ζ
+ δde
τ

,
(20)
where ρ = ζ
κ is the “macro market eﬀective discount rate”,
ρ = ζ
κ = δ + 1 −θ
κ
.
(21)
The deviation of the equity premium from its average is:
ˆπt = (1 −θ) pt −(ft + νt)
κ
.
(22)
We next analyze the economics of Proposition 5. The classical (or undergraduate) “eﬃcient
markets” benchmark, where the risk premium is kept constant by very strong arbitrage forces,
corresponds to κ = ∞, so that ζ = ∞and ρ = δ.31
In (20), the price discounts future dividends at a rate ρ ≥δ given in (21). So, the market is
more myopic (higher ρ) when it is less sensitive to the equity premium (lower κ) and when the mixed
fund has a lower equity share (lower θ).32 It makes good sense that a lower sensitivity to the equity
premium makes the market less reactive to the future, hence more myopic.33,34 In the rest of this
section, we set νt = 0; the general case simply comes from replacing ft by ft + νt.
31Strictly speaking, this is only true with risk-neutral arbitrageurs, so that the risk premium is 0. The general case
is in Section F.4 where the elasticity is still very high.
32The formula extends to changes in the interest rate, as in rft = ¯rf + ˆrft. As (18) becomes ˆπt = Et∆pt+1 +
δ (de
t −pt) −ˆrft, all expressions are the same, replacing de
t by de
t −1
δ ˆrft, including in (20). We assume here that the
bond is very short term, with zero duration. If the bond has non-zero duration, there is another term corresponding
to the capital gains on bonds.
33The intuition for the sign of the impact of θ on ρ is as follows: the extra term 1−θ
κ
in ρ = δ + 1−θ
κ
is the ratio
of the “present looking” (myopic) demand elasticity 1 −θ to the “forward looking” elasticity κ. Hence a higher θ
leads to a less myopic demand. This myopia in (20) generates momentum: because the market is myopic (by (20)),
dividend news are only slowly incorporated into the price.
34Here the demand (19) depends on the equity premium as κ ˆπt = κEt∆pt+1 + κδ (de
t −pt). A variant would be
that investors “see” the price-dividend ratio as diﬀerently predictive from the expected price movement, so that in
their demand we equalize κˆπt with κEt∆pt+1 + κDδ (de
t −pt) where potentially κD̸ = κ (e.g., if “tangible” predictors
are deemed more reliable, κ < κD). Then the demand elasticity is ζ = 1 −θ + κDδ, the eﬀective discount factor is
ρ = ζ
κ, and (20) still holds, after multiplying δde
τ by κD
κ . This highlights that κD increases the market elasticity ζ,
while κ increases market “forward-lookingness” 1
ρ.
18

A permanent inﬂow has a permanent eﬀect on the price and future expected returns
of equities
Suppose that at time 0 there is an inﬂow f0 that does not mean-revert. Then, the
impact on the price at time t ≥0 is (via (20), with E0 [fτ] = f0):
E0 [pt] = 1
ζ f0.
(23)
So, the “price impact” is permanent. As a result, the equity premium is permanently lower, E0 [ˆπt] =
−δ f0
ζ (see (18)) This is simply because, if the equity demand has permanently increased, equity
prices should be permanently higher.35
Quantitatively, if prices increase by 10% due to uninformed ﬂows, the per annum expected excess
return falls by a mere 0.3% (indeed, assuming a dividend yield of 3%, ˆπ = −δp = −3%×0.1 = 0.3%).
This is a vivid reminder that the absence of detectable market timing strategies tells us little about
market eﬃciency (Shiller (1984)). Similarly, Black (1986) famously argued that the aggregate stock
market can be mispriced by as much as a factor of two; in our model, if this is due to a permanent
inﬂow, that would lead to a 2% change in the expected excess return,36 which is less than a single
standard error deviation of the expected excess return estimate if one were to use 30 years of data.
The impact of a mean-reverting ﬂow
Suppose now that at time 0 there is an inﬂow f0 that
mean-reverts at a rate φf ∈[0, 1], so that the cumulative ﬂow is E0 [fτ] = (1 −φf)τ f0. Then, if
there are no further disturbances, the impact on the time-t price is pt =
ft
ζ+κφf (see (20)), implying
E0 [pt] = (1 −φf)t
ζ + κφf
f0,
(24)
and the change in the equity premium is E0 [ˆπt] = −δ+φf
ζ+κφf (1 −φf)t f0 (see (22)). Hence, an inﬂow
that has faster mean reversion leads to a smaller change in the price of equities (compared to
a permanent inﬂow), but a larger change in their equity premium on impact (indeed,
δ+φf
ζ+κφf is
increasing in φf). Those eﬀects dissipate as the inﬂow mean-reverts, at a rate φf.
Predictable future inﬂows or changes in fundamentals create predictable price drifts
Suppose that it is announced at time 0 that a permanent inﬂow fT will happen at time T > 0. The
price impact for t ∈[0, T] is pt =
1
(1+ρ)T −t
fT
ζ (see (20), using fτ = 1τ≥TfT), so that after the initial
jump, the price gradually drifts upward (assuming for concreteness that the inﬂow is positive).
Hence, the risk premium is elevated by ˆπt = 1−θ
κ pt (for t ∈[0, T), see (22)), and more elevated as
one nears the inﬂow. After the inﬂow, though, we are back to the case of a permanently elevated
price and permanently lower equity premium (pt = fT
ζ and ˆπt = −δ fT
ζ for t ≥T). The same price
drift before the shock happens for a predictable increase in future fundamentals such as dividends.
A simple benchmark
To think about the stochastic steady state, it is useful to consider ft as
an autoregressive process with speed of mean-reversion φf:
ft = (1 −φf) ft−1 + εf
t ,
(25)
35In a Kyle (1985) model, ﬂows change prices, like in our model; but they do not on change the equity premium
(on average), which is a crucial diﬀerence with our model. Section G.5 details the link with the Kyle model.
36Indeed, with p = ln 2, ˆπ = −δp = −(3%) × 0.7 ≃−2%.
19

with Et−1
h
εf
t
i
= 0. Then, a high inﬂow increases equity prices and hence lowers the equity premium,
in the following precise manner:37
pt = bp
fft,
ˆπt = bπ
fft,
bp
f =
1
ζ + κφf
,
bπ
f = −(δ + φf) bp
f.
(26)
Calibration
We want to understand how a macro price impact of M ≃5 might arise, and for
this we calibrate the model. When ﬂows are mean-reverting with speed φf, the price impact is
M =
1
ζM , with ζM = ζ + κφf = 1 −θ + κ (δ + φf) (see (9), (24), and (26)). Some parameters
are easy to estimate. We take a dividend-price ratio δ = D
P = 3.7%/year (we use annualized units
throughout).38 We calibrate φf = 4%/year to match the speed of mean-reversion of the dividend-
price ratio.39 Given the results in Figure 1, we take an equity share θ = 87.5% (equity-holdings
weighted as in θS).
Calibrating κ is most challenging.
We perform a few thought experiments to see what we
might expect κ to be.
The simplest rational model of portfolio choice where θit =
πt
γiσ2 gives
κ = d ln θit
dπt
= 1
¯π = 22, using an annual equity premium of 4.4%.40 But, we rarely observe such large
swings in investors’ portfolios: the frictionless rational model predicts agents that are much too
reactive, like in much of this paper, and in much of economics (Gabaix (2019)). To get a further
feel for κ, suppose the equity premium increases from πt = 5% to πt = 10%, which is a shift
equal to about one to two standard deviations of its unconditional time-series variation (Cochrane
(2011); Martin (2017)). A very ﬂexible fund with an average equity share of 50% might change
its equity allocation from 50% to 75%. This ﬂexible fund would have κi = d ln θi
dπ
= ln 0.75−ln .5
0.05
≃8.
However, these are large swings in a fund’s strategic asset allocation that are not typically observed
empirically, so that they are at most valid only for very ﬂexible investors. As many balanced funds
have a ﬁxed-share mandate and κ = 0, we hypothesize a κi for a typical fund with equity share of 50%
equal to about 4. Moreover, a 100% equity funds needs to have κi = 0; more generally, the rigidity
mechanically should increase with the equity share θi. So, we might tentatively parametrize a typical
value of κ as κi = K (1 −θi), with K ≃8. So, we obtain κ = κS = K (1 −θS) ≃8×(1 −0.88) ≃1.
This gives a simple microeconomic interpretation for the value κ = 1. Together, this yields ζ = 0.16,
and ζM = 0.2, so that the price impact is indeed M =
1
ζM = 5. If the ﬂows are extremely persistent,
the subtle diﬀerence between ζ and ζM vanishes (κφf,which is 0.04 in the calibration, goes to 0).
4
Estimating the Aggregate Market Elasticity
The previous sections illustrate the importance of estimating the elasticity of the aggregate stock
market. Estimating this parameter is a challenge, as is the case for most elasticities in macroeco-
37This can be derived by plugging in those values in (19) with q = 0 in equilibrium, or via (20).
38Section H.1 details how to go from continuous to discrete time.
39We compute the dividend yield by summing dividends during the last 12 months relative to the current level
of the CRSP value-weighted return index from January 1947 to December 2018. The annual autocorrelation of the
log dividend yield during this sample is equal to ρOLS = 0.91 with OLS standard errors equal to 0.048. We then
remove the Kendall (1954) bias
1+3ρ
T
over our sample of T = 72 years, which is around
4
72. Thus we calibrate
φf = 1 −ρOLS −4
72 ≃4%.
40This is for a fund maximizing rationally a CRRA function of ﬁnancial wealth. In Section F.4 we consider a more
sophisticated thought experiment, with a consumer maximizing lifetime utility out of labor income in additional to
ﬁnancial wealth. Then, the value of ζ is even higher.
20

nomics. In the context of asset pricing, large literatures try to estimate the coeﬃcient of relative
risk aversion, the elasticity of inter-temporal substitution, and the micro-elasticity of demand, but
not the macro elasticity.41
The key diﬃculty is that prices and ﬂows are in part driven by other variables, such as macroeco-
nomic news, so that naively regressing prices on ﬂows or ﬂows on prices would not yield a consistent
estimate of the elasticities. Hence, we need an instrument. In this section, we provide ﬁrst estimates
of the macro elasticity of the US stock market using the method called Granular Instrumental Vari-
ables (GIV), which we conceived for the present paper, and lay out in Gabaix and Koijen (2020).
Given the relevance of this parameter, we believe it would be valuable for future empirical asset
pricing research to explore diﬀerent estimation and identiﬁcation strategies in estimating its value.
In Section 4.1, we provide the basic intuition behind the GIV estimator. We report the estimates
in Section 4.2 using sector-level data from the Flow of Funds and in Section 4.3 using investor-level
data by combining 13F ﬁlings and mutual fund ﬂows. We also connect capital ﬂows to macroeco-
nomic variables and measures of beliefs to provide an initial analysis of the potential determinants
of ﬂows into the equity market.
4.1
Intuition behind the GIV estimator
We ﬁrst provide a brief summary of the GIV method – the appendix and Gabaix and Koijen (2020)
provide many more details, such as a justiﬁcation of consistency and extensions. Recall that we use
the following notations, with the shares Sj adding up to 1:
XE := 1
N
N
X
i=1
Xi,
XS :=
N
X
i=1
SiXi,
XΓ := XS −XE.
(27)
Suppose that we have a time series of changes in investors’ equity holdings, ∆qit = Qit−Qi,t−1
Qi,t−1
,
where i indexes investors as before. The estimation procedure does not require data on ﬂows across
asset classes: equity holdings suﬃce, which is empirically relevant as investor-level data on ﬂows
are available only for a subset of investors.42 To ﬁx ideas, we model ∆qit as (omitting constants):43
∆qit = −ζ∆pt + f ν
it,
(28)
where ∆pt is the aggregate stock return, and ζ is the demand elasticity of interest — we take it
as constant across sectors in this introduction, but will relax this in Section 4.3. We consider the
following model for f ν
it:
f ν
it = λ′
iηt + uit,
(29)
41See Table 1 for a summary of estimates in the literature.
42If we were to have high-quality data on capital ﬂows, fit, then we could construct another granular instrumental
variable using capital ﬂows by extracting idiosyncratic shocks to fit. However, our theory implies that we need
accurate data on equity and bond holdings to measure capital ﬂows correctly, which are unavailable in the US.
Fortunately, however, we can implement the GIV procedure using ∆qit, which does not require knowledge of holdings
in other assets than equities. Also, in Section 4.3 we show how to use data on a subset of investors, in our case
mutual funds, to obtain another estimate.
43To lighten things up, we simplify a bit the notations. Compared to (19), we use the notation f ν
it for ∆f ν
it :=
∆fit + ∆νit + κi∆Et [δde
t + ∆pt+1]. Later, we absorb the change-in-expectation terms κi∆Et [δde
t + ∆pt+1] into the
“demand shifter” ∆νit.
21

where ηt is a vector of common shocks (which can include observable factors, such as GDP growth,
or latent factors), λi is a vector of factor loadings, and uit is an idiosyncratic shock. We make
throughout the key identiﬁcation assumption that
E [uitηt] = 0.
(30)
The GIV method identiﬁes ζ using variation that comes from the idiosyncratic shocks, uit.
Using market clearing, we have ∆qSt = 0, that is
∆pt = M (λ′
Sηt + uSt) ,
for the multiplier
M = 1
ζ .
The goal is to estimate M, which identiﬁes the demand elasticity, ζ.
The basic idea of the GIV is the following. We use idiosyncratic shocks to demand, uit, as
primitive disturbances to the system, and we see how they aﬀect prices and quantities. The GIV is
the size-weighted sum of those idiosyncratic shocks. Indeed, if we had access to uSt, we could just
estimate M by OLS, regressing ∆pt = MuSt+εt. We next detail how to measure those idiosyncratic
shocks empirically, or at least good proxies for them that make the above reasoning valid.
Simple example with uniform loadings
We start with the case where there is a single factor,
ηt, and λi = 1, so that all loadings on the common shock are uniform. Then, the GIV is constructed
from data as follows:
Zt := ∆qΓt = ∆qSt −∆qEt.
As ∆qSt = −ζ∆pt + ηt + uSt and ∆qEt = −ζ∆pt + ηt + uEt, we have:
Zt = uSt −uEt = uΓt.
(31)
As uΓt is a combination of idiosyncratic shocks only, it is uncorrelated with ηt, see (30).
This
orthogonality condition makes Zt = uΓt a valid instrument: it is our GIV. Furthermore, if uit
is homoskedastic, then uΓt is uncorrelated with uEt.44This implies that ∆pt = MuΓt + et, where
et = M (ηt + uEt) is uncorrelated with Zt. Hence, if we estimate the OLS regression
∆pt = MZt + et,
(32)
then this identiﬁes the true multiplier M. Alternatively, we can estimate ζ directly using Zt as an
instrumental variable for ∆pt in the regression
∆qEt = −ζ∆pt + ϵt,
(33)
with ∆pt instrumented by Zt.
Intuitively, we use the sector-speciﬁc, or idiosyncratic, demand shocks of one sector as a source
of exogenous price variation to estimate the demand elasticity of another sector.
Viewed this
way, the GIV estimator generalizes the idea behind the index inclusion literature to estimate the
44The same condition holds in the more general case of uncorrelated heteroskedastic uit, with the inverse variance
weights ˜E, so Zt := ∆qSt −∆q ˜
Et (see Gabaix and Koijen (2020)).
22

micro elasticity. In the index inclusion literature, a demand shock to the group of index investors
(assuming the inclusion of a stock into the index is random) can be used to estimate the slope of
the demand curve of the non-index investors.
We reiterate that the methodology works even if we do not have data on ﬂows fit – it is enough
to have data on changes in equity holdings ∆qit. This implies that we identify idiosyncratic shocks
to f ν
it = fit + νit, where fit are capital ﬂows and νit are demand shocks.
General case with non-uniform loadings
In the general case with non-uniform loadings and
an r-dimensional vector of common latent shocks ηt, we deﬁne ˇait := ait −aEt, that is, the cross-
sectionally demeaned value of a vector at. We run a principal component analysis (PCA) via the
model
∆ˇqit = ˇλ′
iηt + ˇuit.
(34)
In this way, we extract r principal components, ηt. Then, we run the following OLS regression,
using the extracted factors ηt as controls:
∆pt = MZt + β′ηt + et,
(35)
and estimate the multiplier M as the coeﬃcient on the GIV Zt. The rest of Gabaix and Koijen
(2020) discusses numerous extensions of this basic structure and show its optimality by various
metrics (e.g. it is GMM optimal). As before, we can estimate ζ directly using Zt as an instrumental
variable for ∆pt in the regression
∆qEt = −ζ∆pt + β′ηt + ϵt.
We leave the technical details of the speciﬁc algorithms that we use to Appendix B.1. We demon-
strate the performance of the GIV estimator in our speciﬁc setting in Appendix D.1 using simula-
tions.
GIV: Requirements and threats to identiﬁcation
For the GIV to be consistent, we need (30)
to hold: the idea is that there are random “bets” or “shocks” to various fund managers, institutions
and sectors, that are orthogonal to all reasonable common macro factors such as GDP, TFP, and so
forth. For the GIV to be a powerful instrument, we need large idiosyncratic shocks, and a few large
institutions, so that the market is “granular” in the sense that the idiosyncratic trading shocks of a
few large players meaningfully aﬀect the aggregate.45 Fortunately, this is veriﬁed in our setting, as
it is in related settings in macro (Gabaix (2011), Carvalho and Grassi (2019)), trade (Di Giovanni
and Levchenko (2012)) or ﬁnance (Amiti and Weinstein (2018), Herskovic et al. (forthcoming),
Galaasen et al. (2020)). Ben-David et al. (forthcoming) and Ghysels et al. (2021) study the impact
of investor granularity on the cross-section of US stock returns.
The main threats to identiﬁcation with GIV are that we do not properly control for common
factors, or that the loadings on the omitted factor are correlated with size, such that λS −λE̸ = 0.
To mitigate the risk of omitted factors, we extract additional factors and explore the stability of
the estimates as we add extra factors.
45Indeed, when ﬂow shocks have volatility σu, var (uS) = Hσ2
u, with H = P
j S2
j . This “Herﬁndahl” H of the
holdings shares must be high: so we need a few large entities, such as funds or sectors.
23

When ﬁrms are elastic and ﬂows mean-revert
When ﬁrms have a supply elasticity ζC, the
total elasticity is ζ + ζC, as we saw in Section 3.1. When ﬂows mean-revert with speed φf, the
measured elasticity is ζ + κφf, as we saw in (24) and (26). Combining those two extensions, the
measured price impact is
M = 1
ζM ,
ζM := ζ + κφf + ζC.
(36)
As κφf and ζC appear to be small, the diﬀerence between ζ, ζ + κφf and ζM is rather minor, and is
best ignored in the ﬁrst pass. Still, to be completely explicit, when we empirically measure “ζ”, we
actually measure a quantity that is ζ + κφf + ζC if ﬂows mean-revert at speed φf and ﬁrms have a
supply elasticity ζC, and is strictly speaking ζ only when ﬂows do not mean-revert and ζC = 0.46
4.2
Elasticity estimates using sector-level data
Benchmark estimates
We ﬁrst report the GIV estimates of the macro elasticity using data from
1993.Q1 to 2018.Q4 using the Flow of Funds (FoF). Throughout this section, we model investors’
demand as
∆qit = αi −ζ∆pt + λ′
iηt + uit,
(37)
where we assume that the demand elasticity is the same across sectors. We relax this assumption
below using 13F data. We consider the same model for the corporate sector, but allow for a diﬀerent
demand elasticity, ζC. The vector ηt includes GDP growth, a time trend,47 and one or more latent
factors, ηPC
t
.
The results are presented in Table 2. The ﬁrst column reports the estimates where we use a
single principal component to isolate the idiosyncratic shocks to various sectors, in addition to a
common factor on which all sectors load equally.
We estimate a multiplier of M = 7.1, implying that purchasing 1% of the market results in a
7.1% change in prices. The corresponding standard error is 1.9.48 In the second column, we add a
second principal component. This lowers the multiplier estimate to M = 5.3. That is, purchasing
1% of the market results in a 5.3% change in prices. Both estimates imply that the aggregate stock
market is quite macro inelastic.
In the next two columns, we estimate the elasticities, ζ, by regressing demand changes on
instrumented changes in prices, as in (33). With one principal component, we estimate an elasticity
of ζ = 0.13 and with two principal components, we estimate ζ = 0.17. In the next two columns, we
estimate the supply elasticity ζC of the corporate sector. The short-run elasticity is low at ζC = 0.01
for both one and two principal components.49 This implies that the combined elasticity is 0.14 (with
46Another enrichment would be to make capital ﬂows sensitive to contemporaneous returns, say with a semi-
elasticity ζf, as in ∆ft = −ζf∆pt + ∆˜ft. If ζq = 1 −θ + κδ is the elasticity of the fund’s holdings given ﬂows, the
total elasticity of the funds’ holdings is ζ = ζq + ζf. If we have only holdings data (but not ﬂows data), we can
measure ζq + ζf. If we have ﬂows data, we can also measure ζf using the GIV.
47We include a time trend as some sectors grew faster in the nineties, for instance, than in the later period. We
show the robustness of our results to not including the time trend.
48We report Newey-West standard errors using the bandwidth selection as in Newey and West (1994).
49This small contemporaneous elasticity of the supply of shares by the corporate sector, estimated here causally
by IV, is consistent with the OLS ﬁndings of Ma (2019). She ﬁnds (Table VII) that Gross equity issuance
Assets
= 0.01ˆπ (plus
other terms) at the quarterly frequency. Using that equity is about two thirds of assets, this leads, at the annual
frequency, to ∆qC = 3
2 · 4 · 0.01ˆπ = 0.06ˆπ, so that (by (18)) ζC = δ × 0.06 = 0.0024. However, these estimates do not
rule out the possibility that the medium- or long-run elasticities are higher and that ﬁrms play an important role in
stabilizing asset prices.
24

Table 2: Estimates of the macro elasticity.
The ﬁrst two columns report estimates of M with
one and two principal components, ηt, respectively. The next two columns report the elasticity
estimates, ζ, regressing the equal-weighted change in equity holdings ∆qE on the price change ∆p
instrumented by the GIV Z. The next two columns report the elasticity of the corporate sector,
ζC. The ﬁnal column reports the estimates of the same speciﬁcation as the ﬁrst column, but we
omit Zt, where Zt = P
i Si,t−1∆ˇqit and ∆ˇqit deﬁned in (63), to estimate the impact of sector-speciﬁc
shocks on prices. In constructing ∆ˇqit, all estimates control for quarterly GDP growth. We report
the standard errors, which are corrected for autocorrelation, in parentheses. The sample is from
1993.Q1 to 2018.Q4.
∆p
∆p
∆qE
∆qE
∆qC
∆qC
∆p
Z
7.08
5.28
(1.86)
(1.10)
∆p
-0.13
-0.17
-0.01
-0.01
(0.04)
(0.05)
(0.01)
(0.02)
GDP growth
5.99
5.97
0.56
0.85
0.22
0.23
5.93
(0.69)
(0.67)
(0.27)
(0.33)
(0.13)
(0.16)
(0.91)
η1
21.06
23.72
3.98
5.49
-0.72
-0.64
31.50
(13.58)
(12.79)
(2.08)
(2.07)
(0.69)
(0.81)
(15.57)
η2
29.95
5.62
0.29
(6.54)
(2.15)
(0.67)
Constant
-0.01
-0.01
0.00
0.00
-0.00
-0.00
-0.01
(0.01)
(0.01)
(0.00)
(0.00)
(0.00)
(0.00)
(0.01)
Observations
104
104
104
104
104
104
104
R2
0.436
0.515
0.279
25

Figure 2: Estimates of the aggregate multiplier M = 1
ζ by horizon. The ﬁgure plots the multi-
period impact of demand shocks: a demand shock of ft at date t increases the (log) price of equities
from t −1 to t + h by Mft. We use the GIV for instrumentation, see (38). The horizontal axis
indicates the horizon in quarters, from zero (that is, the current) to four quarters. Standard errors
are adjusted for autocorrelation. The sample is from 1993.Q1 to 2018.Q4.
−5
0
5
10
15
20
Multiplier
−1
0
1
2
3
4
Horizon (quarters)
Multiplier
95%−confidence interval
one principal component) or 0.18 (with two principal components). The corresponding multipliers,
M =
1
ζ+ζC , are M = 7.1 and M = 5.9, respectively.
In the ﬁnal column, we report the same regression as in the ﬁrst column but without the
instrument Zt. By comparing the R-squared values, we obtain an estimate of the importance of
sector-speciﬁc shocks on prices. We ﬁnd that the diﬀerence in R-squared values is 16%, which
highlights the importance of sector-speciﬁc shocks on prices.
The impact of ﬂows at longer horizons
In Figure 2, we explore how demand and ﬂow shocks
propagate across time. To this end, we extend the earlier analysis by estimating
pt+h −pt−1 = ah + MhZt + chηPC,e
t
+ dh∆yt + ϵt+h,
(38)
for h = 0, 1, . . . , 4 quarters, where pt+h −pt−1 is the (h + 1)−quarter (geometric) return on the
aggregate stock market. Recall that ηPC,e
t
is the principal component, extracted in the third step
of the GIV procedure as outlined in Section B.1. The ﬁgure reports Mh at a certain horizon. We
also consider a regression where we replace the left-hand side by pt−1 −pt−2, which we refer to as
h = −1. To construct the conﬁdence intervals, we account for the autocorrelation in the residuals
due to overlapping data.
We ﬁnd that the cumulative impact is fairly stable over time. This is intuitive as sharp reversals
would imply a strong negative autocorrelation in returns, which is not something that we observe
for the aggregate stock market at a quarterly frequency. As such, and consistent with the theory,
persistent ﬂow shocks lead to persistent deviations in prices. Size-weighted sector-speciﬁc demand
shocks are also not correlated with returns at t −1 (that is, h = −1). Unfortunately, however, the
26

conﬁdence interval widens quite rapidly with the horizon, which limits what we can say about the
long-run multiplier.
Robustness
We explore the robustness of our estimates along various dimensions. In the interest
of space, we report and discuss the tables in Appendix D.4. In Tables D.8–D.10, we consider a
variety of robustness checks related to the sample period, data construction, and implementation
choices of the GIV estimator. We conclude that our results are robust to these changes in the
empirical strategy with multiplier estimates ranging from 3.5 to 8.
4.3
Elasticity estimates using investor-level data
We provide an alternative estimate of the same elasticity, but now using more disaggregated,
investor-level 13F and mutual fund data.50 We use 13F data from FactSet that cover the period
from 2000.Q1 to 2019.Q4 and we follow the data construction as in Koijen et al. (2019). Monthly
mutual fund ﬂows come from Morningstar from January 1993 to December 2019. We provide details
in terms of the data construction in Appendix C.2. An advantage of these disaggregated data is that
we can allow for heterogeneous demand elasticities across investors. To provide another estimate of
the multiplier, we proceed in three steps.
First, we estimate innovations in fund ﬂows for mutual funds. Let ∆ft be the fractional inﬂow
into equity markets from mutual funds.51 We estimate
∆ft = a0 +
k
X
l=1
al∆ft−l + ct + ϵf
mt,
(39)
at a monthly frequency (see Table D.12 in Online Appendix D.6). We also deﬁne K =
1
1−Pk
l=1 al,
which is the cumulative ﬂow due to shocks ϵf
mt: as per Proposition 5, what matters is the cumulative
future inﬂow, which is Kϵf
mt.52
It is well known that the innovations, ϵf
mt, are correlated with contemporaneous realized returns
(Warther (1995); Edelen and Warner (2001); Goetzmann and Massa (2003)).
We extend this
literature by removing aggregate demand factors and isolating the idiosyncratic demand shocks
of mutual fund investors. In addition, we show how to translate the persistence in ﬂows to a theory-
based estimate of the multiplier via K. We aggregate the monthly innovations, ϵf
mt, for k = 3 in
each quarter and refer to these innovations as ϵf
t . We model
ϵf
t = β′
0ηt + β′
1Ct + uf
t ,
50In the US, all institutional investment managers managing over $100 million or more in “13F securities” (which
include stocks) must report their holdings on Form 13F every quarter.
51To compute the relevant measure of ﬂows, we start from the share invested in US equities by fund i, θit, assets
under management, Wit, and the ﬂow ∆Fit as deﬁned by Morningstar. When equity shares are missing at a monthly
frequency, we ﬁll in the equity shares using the most recent value for a given fund. We ﬁrst compute ∆fit =
∆Fit
Wi,t−1
and winsorize it at 1% and 99% in each period. We then compute ∆ft =
P
i θi,t−1Wi,t−1∆fit
P
i θi,t−1Wi,t−1
, which uses equity-
weighting, as warranted by the theory, see (10). We include “US equity,” “sector equity,” “international equity,” and
“allocation” funds in the analysis. Appendix C.2 provides additional details.
52In principle, it should be discounted at a rate ρ, but this is immaterial at the horizon of a few months that we
use. See Section G.5 for details.
27

where ηt are common unobserved factors, Ct are common observed factors, and uf
t are the unique
shocks to fund ﬂows.53
Second, we wish to estimate those common factors, ηt, to isolate the shocks that are unique to
mutual fund investors. To do so, we use the 13F ﬁlings of investors outside of the mutual fund
industry (e.g., pension funds, insurance companies, and so forth).54 We consider an extension of
the model in (37), where we allow for heterogeneity in demand elasticities, ζi,t−1:
∆qit = αi −ζi,t−1∆pt + λ′
i,t−1ηt + β′
iCt + uit.
We assume a parametric speciﬁcation for elasticities and a semi-parametric speciﬁcation for factor
loadings:
ζi,t−1 = ˙ζ′xi,t−1,
λi,t−1 = ˙λ′xi,t−1 + ¨λi,
where xi,t−1 is a vector of investor characteristics of which the ﬁrst element is equal to 1, and ˙ζ,
˙λ, and ¨λi are to be estimated. As investor characteristics, we use active share and log AUM. In
addition, we allow for non-parametric factors via ¨λi, as before. We also control for GDP growth and
allow investors to have heterogeneous exposures to macroeconomic conditions via β′
iCt. We discuss
in Section B.1 how we estimate the common factors, ηt, and we refer to the estimates as ηe
t .
Third, we regress returns on fund ﬂow innovations, while controlling for common factors,
∆pt = a + MZt + λ′ηe
t + m′Ct + et,
where Zt = KSMF
t−1 ϵf
t , with SMF
t−1 the share of aggregate equities held by the mutual fund sector:
after controls, this is the surprise inﬂow unique to mutual funds. As a common observed factor, Ct,
we use GDP growth. We also explore robustness to controlling for changes in volatility in Ct.
The results are summarized in Table 3.
The ﬁrst column presents the results with only Zt
and GDP growth, something we show for illustration but do not recommend using. The next four
columns add the factors extracted from the 13F data, ηe
t , as recommended by the GIV. In the
ﬁnal column, we also control for the quarterly (percentage) change in volatility. Without controls
other than GDP in Column 1, the multiplier estimate equals M = 10.9. By adding additional
controls, the R-squared value increases signiﬁcantly and the multiplier estimate lowers, as we would
expect since demand shocks and prices are positively correlated. With four additional factors, the
R-squared value equals approximately 60% and the multiplier drops to M = 7.7 with a standard
error of 2.3. In the ﬁnal column, we add changes in volatility. While these do not correlate strongly
with fund ﬂow innovations, they do correlate with returns. This suggests that other investors are
negatively sensitive to volatility and this also captures a source of demand shocks. The multiplier
lowers further to 7.6 and the R-squared is now 70%.55 In Figure D.8, we also repeat the long-horizon
analysis as in Figure 2. As before the impact of ﬂow shocks on prices is persistent although the
conﬁdence interval is wide at longer horizons of one year.
In summary, we ﬁnd that the multiplier estimates are quite consistent with the estimates we
found using the FoF data. These estimates well above 1 are consistent with the estimates for other
53Flows themselves may be sensitive to prices, so that ϵf
t = −ζf∆pt + β′
0ηt + β′
1Ct + uf
t . In this case, if ζf is
negative, as is the case when mutual fund investors engage in positive feedback trading, then our estimates provide
a lower bound.
54Speciﬁcally, we omit investors outside of the mutual fund industry using the same assignment of investor types
as in Koijen et al. (2019). This removes, for instance, investment advisors and mutual funds as classiﬁed by FactSet.
55As volatility is endogenous, it can be included only with interpretative circumspection. We include it here for
descriptive purposes.
28

Table 3: Estimates of the macro elasticity using mutual fund and 13F data. The ﬁrst ﬁve columns
provide estimates of the multiplier M, which is the coeﬃcient on Zt = KSMF
t−1 ϵf
t , the innovation in
the cumulated inﬂow into mutual funds after controls. We regress returns on unexpected ﬂows, ϵf
t ,
times the share of aggregate equities held by the mutual fund sector, SMF
t−1 , and adjusting for the fact
that inﬂows are autocorrelated (see (39) and the surrounding deﬁnition of K). In the ﬁrst column
we only control for GDP growth and in the next four columns we add one to four common factors
to isolate the idiosyncratic component in mutual fund ﬂows. The common factors are extracted
from 13F ﬁlings of institutions outside of the mutual fund industry. In the ﬁnal column, we add
the change in quarterly volatility as an additional control. We report the standard errors, which
are corrected for autocorrelation, in parentheses. The sample is from 2000.Q1 to 2019.Q4.
∆p
∆p
∆p
∆p
∆p
∆p
Z
10.93
10.85
8.54
7.69
7.69
7.62
(2.64)
(2.78)
(2.18)
(2.32)
(2.34)
(1.92)
GDP growth
4.19
4.21
4.94
4.99
5.00
3.43
(1.23)
(1.25)
(0.96)
(1.17)
(1.17)
(1.17)
PC1
-0.91
-0.94
-0.95
-0.95
0.06
(0.74)
(0.60)
(0.63)
(0.63)
(0.61)
PC2
-2.98
-3.07
-3.07
-0.82
(0.66)
(0.48)
(0.48)
(0.37)
PC3
-0.87
-0.87
-1.25
(0.56)
(0.56)
(0.41)
PC4
0.11
-0.21
(0.33)
(0.38)
∆σ
-0.10
(0.01)
Constant
0.00
0.00
-0.00
-0.00
-0.00
0.00
(0.00)
(0.00)
(0.01)
(0.00)
(0.00)
(0.00)
Observations
80
80
80
80
80
80
R2
0.426
0.438
0.556
0.565
0.566
0.699
29

countries and for style factors, see Table 1. Future research can explore other strategies to control
for common demand factors to sharpen the identiﬁcation.
4.4
A new measure of capital ﬂows into the stock market
In this ﬁnal section, we construct a new measure of capital ﬂows into the stock market consistent
with the theory in Section 3. While our theory provides conceptual clarity in terms of how to
measure ﬂows into the market, and to get around the problem that “for every buyer there is a
seller,” the data required are unfortunately not available for all investors.
In Section 4.4, we propose a way to construct an empirical counterpart to the measure based
on the available data. As this measure is new to the literature, we show its connection to prices,
macroeconomic variables, and beliefs. The results in this section provide an initial analysis of the
potential determinants of ﬂows into the aggregate stock market. These results are intentionally
descriptive in nature and understanding the primitive drivers of these ﬂows is an important task
for future research.
Measuring ﬂows into the stock market
We rely on the FoF data for these calculations and
we refer to Appendix C for details on the data construction of the ﬁxed income positions and ﬂows.
As (10) shows, the ﬂow into the aggregate stock market can be measured by ﬁrst computing the
ﬂow for each investor, ∆fit =
∆Fit
Wi,t−1, and then computing the equity weighted average, ∆fSt =
P
i
θi,t−1Wi,t−1
P
i θi,t−1Wi,t−1∆fit.
Unfortunately, the FoF aggregates data across many institutions and the
reported ﬂows can be mismeasured by this deﬁnition. To see this, consider the case in which some
households only invest in bonds and other households only invest in equities. If we view this as a
combined household, a 1% combined inﬂow into ﬁnancial markets does not necessarily lead to a 1%
increase in equity holdings as the ﬂow may be a ﬂow to bond funds only. With disaggregated data,
such problems can be solved, but such data are unfortunately unavailable.
We propose a simple diagnostic to assess whether ﬂows are measured accurately. In particular,
in our model, the elasticity of demand to ﬂows equals one, see (7). We therefore estimate
∆qit = α + βifit + γi∆pt + δi∆yt + ϵit.
(40)
We report the estimates of βj in Table D.13 in Appendix D. When we cannot reject H0 : βi = 1
at the 5% signiﬁcance level, we use the total ﬂow. If this null hypothesis is rejected, we use the
equity ﬂow instead. We refer to these “screened ﬂows” as f ∗
it. The aggregate ﬂow is then given by
f ∗
St = P
i Si,t−1f ∗
it + fCt, where fCt corresponds to net repurchases of equities by ﬁrms.
The correlation between capital ﬂows and equity returns
We relate our measure of capital
ﬂows into the stock market to returns. In the left panel of Figure 3, we show that our measure
of ﬂows is strongly correlated with returns using a binned scatter plot in the left panel. We again
ﬁnd that the slope is high, but we emphasize that, because of endogeneity, the slope is not a good
measure of the impact of ﬂows of the price. This is why earlier we developed an IV strategy to
measure that impact.56
56If one has data on capital ﬂows for a substantial number of sectors, then it would be possible to construct a GIV
estimate based on capital ﬂows alone. This would make it possible to estimate the causal impact of prices on capital
ﬂows and of capital ﬂows on prices.
30

Figure 3: Capital ﬂows into the stock market and price changes.
We plot the aggregate ﬂow
into the stock market, using the screened ﬂows, f ∗
jt, f ∗
St = PN
j=0 Sjf ∗
jt, versus the return on the
aggregate stock market in the left panel used a binned scatter plot. In the right panel, we construct
a cumulative (log) return index and compute cumulative ﬂows. We extract the cyclical component
using the methodology developed in Hamilton (2018). We standardize both measures over the full
sample to be able to plot them in the same ﬁgure. The sample for both ﬁgures is from 1993.Q1 to
2018.Q4.
−.2
−.1
0
.1
.2
Return
−.005
0
.005
.01
Flow
−4
−2
0
2
4
1995q1
2000q1
2005q1
2010q1
2015q1
2020q1
Date
Cycle flows
Cycle prices
We can also illustrate the strong co-movement between ﬂows and prices at lower frequencies.
In particular, we construct a cumulative (log) return index and compute cumulative ﬂows. We
then extract the cyclical component using the methodology developed in Hamilton (2018). We
standardize both measures, by removing the time-series mean and dividing them by their standard
deviations, over the full sample to be able to plot them in the same ﬁgure. These are shown in
the right panel of Figure 3. Consistent with the high-frequency co-movement that we uncover in
the left panel of Figure 3, we ﬁnd that prices and ﬂows co-move at a business cycle frequency. We
re-emphasize once again that these are merely correlations and it may be the case, for example,
that they reﬂect positive feedback trading by investors (Cutler et al. (1990), Shleifer (2000)).
Relating ﬂows to shocks to GDP and to return expectations
To conclude this initial
exploration of capital ﬂows into equity markets, we relate ﬂows to shocks to economic activity and
survey expectations of returns. We use GDP growth as our measure of economic activity, as before.
For return expectations, we use the survey from Gallup. The data are described in more detail
in Appendix C. Gallup has several missing observations and only starts in 1996.Q4. We only use
data for all series when they are non-missing, which gives us 79 quarterly observations. To obtain
innovations, we estimate an AR(1) model for each of the series (except returns). We standardize
each of the innovation series, by removing the time-series mean and dividing them by their standard
deviations, to simplify the interpretations of the regressions.
The results are presented in Table 4.
In the ﬁrst three columns, we relate capital ﬂows to
survey expectations and economic growth. We ﬁnd that ﬂows and survey expectations are strongly
correlated, conﬁrming Greenwood and Shleifer (2014) using a more comprehensive measure of capital
ﬂows. A one standard deviation increase in survey expectations of future returns is associated with
a 0.48 standard deviation increase in capital ﬂows.
This ﬁnding may point to a resolution of a recent challenge posed to the beliefs literature by
31

Table 4: Descriptive statistics on capital ﬂows, survey expectations of beliefs, economic activity,
and stock returns. The table reports the time-series regressions of innovations to ﬂows in the ﬁrst
three columns on innovations to survey expectations of returns (column 1), GDP growth innovations
(column 2), and both variables combined (column 3). We estimate the innovations in all cases by
estimating an AR(1) model, and normalize them to have unit standard deviation. Then we regress
returns on ﬂow innovations (column 4), innovations to survey expectations of returns (column 5),
GDP growth innovations (column 6), and all three variables combined (column 7). The sample is
from 1997.Q1 to 2018.Q4, with some gaps, due to missing data for the Gallup survey.
Flow
Flow
Flow
Return
Return
Return
Return
Gallup
0.48
0.46
0.61
0.33
(0.10)
(0.11)
(0.09)
(0.09)
GDP growth
0.21
0.06
0.41
0.21
(0.11)
(0.11)
(0.10)
(0.08)
Flow
0.65
0.45
(0.09)
(0.09)
Constant
0.00
0.00
0.00
0.00
0.00
0.00
0.00
(0.10)
(0.11)
(0.10)
(0.09)
(0.09)
(0.10)
(0.07)
Observations
79
79
79
79
79
79
79
R2
0.233
0.046
0.237
0.426
0.376
0.171
0.582
Giglio et al. (2021a). In particular, they ﬁnd that although survey expectations of returns are
volatile, the pass-through to actions (that is, portfolio rebalancing) is low. One possibility is that
the strong correlation between innovations to beliefs and prices (which equals 61% in our sample)
arises even though the pass-through is low, but small ﬂows into inelastic markets lead to large price
eﬀects.
Flows and economic activity, as analyzed in the second column, are also positively correlated,
but the relation is substantially weaker. In the third column, we combine survey expectations and
economic activity, and ﬁnd that the latter is insigniﬁcant. In the remaining columns, we study the
association between returns and ﬂows, beliefs, and economic activity. A one standard deviation
increase in capital ﬂows is associated with a 0.65 standard deviation increase in returns, which
is similar to a 0.61 standard increase in case of survey expectations. The link to GDP growth is
signiﬁcant, but weaker with a slope coeﬃcient of 0.41. In the ﬁnal column, we combine all ﬂows,
beliefs, and GDP growth and ﬁnd that even in this multiple regression, all variables are signiﬁcant.
The R-squared of this ﬁnal regression is high and amounts to R2 = 58%.
Obviously, this analysis is just an initial exploration into the determinants of ﬂows, and more
disaggregated data may be used to explore the determinants of capital ﬂows for various institutions
and across households. If the inelastic markets hypothesis holds, this is an important area for future
research.
32

5
General Equilibrium with Inelastic Markets
So far, we took both the risk-free rate rf and the average equity premium ¯π as exogenous. We now
endogenize them. For instance, we shall see how ﬂows from bonds to stocks, which alter the price
of stocks, can at the same time keep the risk-free rate constant (in our model, this is because the
optimizing household also trades oﬀsaving in bonds versus consumption, and this way ensures that
the consumption-based Euler equation for bonds holds). We view this as a prototype for how to
build general equilibrium models with inelastic markets, merging behavioral disturbances, the ﬂows
they create, their impact on prices, and potentially their impact on production.
5.1
Setup
For simplicity, we discuss in detail an endowment economy. It will be easy to then generalize the
model to a production economy. This general equilibrium model is a specialization of our inﬁnite-
horizon model of Section 3.2 – it speciﬁes things left general in that model, such as the origin of
the interest rate.
The endowment Yt follows a proportional growth process, with an i.i.d. lognormal growth rate
Gt:
Yt
Yt−1 = Gt = eg+εy
t −1
2 σ2
y, with εy
t+1 ∼N
 0, σ2
y

.
Utility is P
t βtu (Ct) with u (C) =
C1−γ
1−γ .
Because empirically dividend growth and GDP growth are not very correlated, we model that GDP
Yt is divided as Yt = Dt + Ωt into an aggregate dividend Dt and a residual Ωt, where the dividend
stream has i.i.d. lognormal growth,
Dt
Dt−1 = GD
t
= eg+εD
t −1
2 σ2
D, so that the balanced growth path
speciﬁed in Section 3.2 has a cumulative growth factor Gt = GD
t . . . GD
1 . The “residual” Ωt can be
thought of as a combination of wages, entrepreneurial income, and so forth (and indeed it is the
vast majority of GDP).57 The representative ﬁrm raises capital entirely through equity, and passes
the endowment stream as a per-share dividend Dt = Dt
Q , where Q is the number of shares of equities
supplied by the corporate sector, which is an unimportant constant in this baseline model without
share buybacks and issuances. Bonds are in zero net supply.58 We write the price of equities as
Pt = Dt
δ ept, where δ is the average dividend-price ratio and pt is the deviation of the price from the
baseline pt = 0. Those quantities are all endogenous.
There are two funds: a pure bond fund, which just holds bonds, and the representative mixed
fund, which holds bonds and equities. The mixed fund has a mandate, to hold a fraction in equities
equal to:
θt = θ exp
 −κDpt + κEt [∆pt+1]

,
(41)
which is the same as before in (1), to the leading order (in terms of deviations from the steady
state), with κD = κδ. The formulation here is slightly more general.59
Consumption and investment by households
We describe the behavior of the representative
household. Section G.8 provides more formalism and further details. The dynamic budget constraint
57Formally, it could become negative, as in Campbell and Cochrane (1999), though this is a very low probability
event in our calibration. Then, the interpretation is that of a residual liability. In addition, it would be easy to keep
Dt/Yt stationary, at the cost of having it as one more state variable, reverting to its mean.
58We can easily have the government issue bonds, backed by taxation, see Section G.8.1.
59But here we allow the mandate to potentially diﬀerentiate between “return predictability coming from the price-
dividend ratio” (captured by −κDpt) and “return predictability because the price is predictable”. In a number of
settings the ﬁrst one (the “carry”) is stronger than the last one (Koijen et al. (2018)), so having two κ’s is sensible.
33

of household h entails:60
QB,h
t
+ Dh
t + Ωh
t = Ch
t + ∆F h
t + QB,h
t+1
Rf,t
.
(42)
Indeed, the left-hand side is the bond asset position of the household at the beginning of period t:
QB,h
t
gives the bond holdings at the beginning of period t, while Dh
t and Ωh
t are the dividend and
residual income received by the household in its pure bond fund (which includes the “dividends”
paid by the mixed fund). This bond position is spent on consumption Ch
t , ﬂows ∆F h
t into the mixed
fund, and investment in bonds, with a face value QB,h
t+1.
We need a behavioral element, otherwise the investor would fully undo the funds’ mandate. We
choose to decompose the household as a rational consumer, who only decides on consumption (so
dissaving from the pure bond fund), and a behavioral investor, who trades between the pure bond
fund and the mixed fund.
The rational consumer part of the household chooses consumption (but not equity shares) to
maximize lifetime utility, subject to the dynamic budget constraint for bonds (42). She takes the
actions of the investor as given.61 As she is rational, she satisﬁes the Euler equation for bonds:
Et
"
β
Ct+1
Ct
−γ
Rft
#
= 1,
(43)
with Ct = Yt in equilibrium. This pins down the interest rate Rft, which is constant in our i.i.d.
growth economy.
The behavioral investor part of the household is inﬂuenced by bt, a behavioral disturbance. It
is a simple stand-in for noise in institutions, beliefs, tastes, fears, and so on. We assume that the
investor trades (between stocks and bonds) with a form of “narrow framing” objective function (as
in Barberis et al. (2006)). He seeks to maximize Et [V p (Wt+1)] with V p (W) = W 1−γ−1
1−γ
a proxy
value function. Speciﬁcally, when bt = 0, he chooses his allocation ¯θM in the mixed fund as:
¯θM = argmax
θM
E

V p   1 −θM
Rft + θMRM,t+1

|bt = 0

,
(44)
where RM,t+1 is the stochastic rate of return of the mixed fund. This choice of a “narrow framing”
benchmark is opposed to the fully rational value function, which would have all the Merton-style
hedging demand terms, and would lead to the consumption CAPM holding on average: in particular,
the equity premium would be too small, as in the equity premium puzzle (at ¯π = γcov
 εD
t , εy
t

).
Instead, the above formulation with narrow framing will lead to a high equity premium ¯π = γσ2
r,
where the σ2
r is the volatility of the stock market, which is aﬀected by ﬂow shocks.62
If there are no behavioral disturbances, an investor wishing to maintain a constant allocation ¯θM
in the mixed fund should invest via ¯Ft = 1−θ
θ
  ¯Pt −¯P0
 ¯Q, as in Section 3.2, that is, ∆¯Ft = 1−θ
θδ ∆Dt.
We assume that his policy, however, is aﬀected by the behavioral disturbance bt, so that the actual
ﬂow is
∆Ft = 1 −θ
θδ ∆Dt + 1
δ∆(btDt) ,
(45)
60There is also the usual transversality condition, limt→∞βt  Ch
t
−γ QB,h
t
= 0.
61One could imagine a variant, where the consumer manipulates the investor’s actions. This would lead her to
distort her Euler equation for consumption.
62This choice of “narrow framing” leads to a high equity premium. It could be replaced by another device such as
disasters. We choose here narrow framing as this behavioral ingredient is well in the behavioral spirit of this section.
34

which is higher than the baseline amount ∆¯Ft by a fraction ∆bt of the “fundamental value”
Dt
δ of
the equity market. Here we will specify that bt is an AR(1).
In Appendix G.9, we provide a formal microfoundation of ﬂows via beliefs: the ﬁnancier part of
the household believes that the deviation of the equity premium from trend is ˆπH
t . Under simple
conditions, this leads to a ﬂow
ft = κHˆπH
t ,
(46)
with κH the sensitivity to the risk premium, and to a behavioral deviation bt =
ft
θ . Using the
empirical ﬁndings of Giglio et al. (2021a), we estimate that κH ≃2, a value that we rationalize by
calibrating it in terms of other behavioral parameters. This estimate is in contrast with a rational
model, which would imply κH = 1
¯π ≃22, a very large pass-through from beliefs to portfolio shares.
A low value of κH means that people have “bold forecasts” (excess variations in the perceived equity
premium) but make “timid choices” (small ﬂows), very much as in Kahneman and Lovallo (1993).63
This type of model can be also made to match the perspective in Bordalo et al. (2020), in which
all variation in prices, ﬂows, and the perceived risk premium ˆπH
t
comes from changes in the long-
term growth forecast gt (all in deviations from a trend), in a way still governed by (46): Section G.9
provides details and a calibration. One could image a richer model for the perceived risk premium
ˆπH
t , e.g. with extrapolative beliefs based on realized returns or growth rates. One could then work
out the implications for ﬂows (via (46)) and prices (via Proposition (5)).
We conclude that linking ﬂows to beliefs is a promising and manageable line of research, and
the analytics that we provide in this section and in Appendix G.9 help thinking about this. At the
same time, there may be other determinants of ﬂows, for instance binding risk constraints, changes
in regulation or policy, and reaction to fairly irrelevant news, which is why we ﬁnd it useful to
separate the impact of the behavioral deviation bt from its determinants.
We ﬁnally formally deﬁne the equilibrium.
Deﬁnition 1. The state vector is Zt = (Yt, Dt, Dt−1, bt) . An equilibrium comprises the following
functions: the stock price P (Z), the interest rate Rf (Z), and the consumption and asset allocation
C (Z), B (Z), such that the mixed fund’s allocation θ (P, Z) follows its mandate, and: (i) the
consumer follows the consumption policy C (Z), which maximizes utility subject to the above
constraints; (ii) the investor follows the behavioral policy (45), where the average allocation in the
mixed fund is given by (44), so that it is quasi-rational with narrow framing on average, but with
disturbance bt; (iii) the mixed fund’s demand for stocks Q (Z) follows its mandate (41); (iv) the
consumption market clears, C (Z) = Y (Z); and (v) the equity market clears, Q (Z) = Q.
5.2
Model solution
Proposition 6 describes the solution of this economy. In particular, it shows that the link between
the disturbance bt and the cumulative ﬂow ft is as follows. Starting from an equilibrium situation,
where b0 = 0, the cumulative “excess” ﬂow is equal to:
ft = θbt.
(47)
This holds for any process bt. Now, we specialize to the case where bt follows an AR(1) with speed of
mean-reversion φf. Then, so does ft, so that we are in the “simple benchmark” case of (25)-(26), and
63Quantitatively, to match the calibrated volatility of ﬂows of σf = 2.8% (as in Table 6) we need a moderate
variation of beliefs σπH = 1.4%.
35

now with an endogenous interest rate and unconditional equity premium. This AR(1) assumption is
just a placeholder for richer behavioral assumptions, for example driven by time-varying beliefs (as
in Caballero and Simsek (2019), Bordalo et al. (2020)), positive or negative feedback trading rules,
and so on. We defer to future research for richer, empirically-grounded models of the “behavioral
deviation” bt, and hence of the ﬂows. The limited goal of this framework is to have a simple model
of the impact of the ﬂows in general equilibrium, which can be fully solved and which lends itself
to a number of variants. Importantly, it relies on observable ﬂows.
Proposition 6. The solution of the economy obtains in closed form as follows, taking the limit of
small time intervals and only the ﬁrst order terms in ft. The market elasticity ζ and the “macro
market eﬀective discount rate” ρ (see Proposition 5) are:
ζ = 1 −θ + κD,
ρ = ζ
κ.
(48)
The price of equities is:
Pt = Dt
δ ept,
(49)
where Dt is the dividend, δ = rf + ¯π −g is the average dividend-price ratio, and pt is the deviation
of the price from its rational average, which increases with ﬂows:
pt = bp
fft,
bp
f =
1
ζ + κφf
.
(50)
Hence the variance of stock market returns is
σ2
r = var

εD
t + bp
fεf
t

,
(51)
and depends on both fundamental risk ( εD
t ) and ﬂow risk (εf
t ). Both contribute to the average equity
premium, which is:
¯π = γσ2
r.
(52)
The equity premium at time t is lower than its average when ﬂows have been high, as:
πt = ¯π + bπ
fft,
bπ
f = −(δ + φf) bp
f.
(53)
Finally, the interest rate is constant, and given by the consumption Euler equation (43):
rf = −ln β + γg −γ (γ + 1) σ2
y
2 .
(54)
Hence, we have a fairly traditional economy, except that, crucially, prices and risk premia are
now driven by ﬂows and ﬂow risk, in addition to fundamentals, and that markets are inelastic.
Hence, the equity premium is time-varying (because of ﬂows), and on average higher than in the
consumption CAPM (because it reacts to ﬂow risk, not just fundamental risk, and because the nar-
row framing makes the investor react to the variance of equity returns, rather than their covariance
with consumption), as given in (52).
36

5.3
Pricing kernel consistent with ﬂow-based pricing
We show how to express the economics of ﬂows in inelastic markets in the language of pricing
kernels or stochastic discount factors (SDFs). To do so, we use a simple general method to complete
a “default” pricing kernel so that it reﬂects the impact of ﬂows on asset prices. The idea is simply
that there is a fringe of inﬁnitesimal traders that can absorb any inﬁnitesimal amount of new
assets. That gives rise to a “ﬂow-based” pricing kernel (see Section G.10 for details). In our general
equilibrium model, this SDF is:
Mt+1 = exp(−rf −πt
εD
t+1
σ2
D
+ ξt),
πt = ¯π + bπ
fft,
(55)
where σ2
D = var
 εD
t+1

and ξt is a deterministic term ensuring that Et [Mt+1] erf = 1, so that
ξt = −π2
t
2σ2
D if εD
t+1 is Gaussian.
This “ﬂow-based” pricing kernel is an alternative to the consumption-based kernel of Lucas
(1978). The core economics is in how ﬂows aﬀect prices, and the pricing kernel (55) just reﬂects
that. The ﬂow ft modiﬁes the price Pt according to Proposition 6 and also the pricing kernel Mt+1,
in such a way that Pt = Et [Mt+1 (Dt+1 + Pt+1)] holds. The pricing kernel is in a sense a symptom
rather than a cause in that market.
To sum up, the ﬂow-based SDF (55) reacts to ﬂows, and prices equities and bonds:
Et [Mt+1RM,t+1] = 1,
Et [Mt+1Rft] = 1.
However, in this model, consumption does not directly price equities, though it does price bonds:
Et[β
Ct+1
Ct
−γ
RM,t+1]̸ = 1,
Et[β
Ct+1
Ct
−γ
Rft] = 1.
5.4
Calibration of the general equilibrium model
We now calibrate the general equilibrium model. This extends the calibration of Section 3.2, which
is natural as the general equilibrium model is an extension of the basic inﬁnite horizon model. We
use the parameter values given in Table 5, which are all presented in annualized terms for clarity.
We provide a summary discussion of our parameter choices here, leaving some details to Section H.
Risk aversion is moderate, at γ = 2. The macroeconomic parameter values are standard, except for
the pure rate of time preference.64 We set a speed of mean reversion of the behavioral disturbance
of φb = 4%/year, which induces the same speed of mean reversion for ﬂows ft and for the P/D
ratio. Likewise, we choose its standard deviation to generate the requisite volatility of ﬂows. For
parsimony, we assume zero correlation between ﬂow shocks and dividend shocks.
Table 6 shows the resulting moments implied by the model. It veriﬁes that we match all the
“classic” moments, for instance the risk-free rate, the average equity premium, and the volatility of
64To get a small risk-free rate of 1% (and only for this reason), we need to make the agents very patient, so that
β > 1. Indeed, this comes from the Ramsey equation (54), which is rf ≃−ln β + γg (neglecting precautionary
eﬀects, which are very small in our calibration) with γg = 4%. We share this issue with the overwhelming majority
of the macroeconomics literature: if we normalized the average growth rate to zero, like most of the macroeconomics
literature, we would not have this diﬃculty. It would be easy to amend that, for example by adding a small probability
of a disaster risk or by using Epstein-Zin preferences. We do not do that, because we do not wish to complicate the
model.
37

Table 5: Parameter values used in the calibration
Variable
Value
Growth rate of endowment and dividend
g = 2%
Std. dev. of endowment growth
σy = 0.8%
Std. dev. of dividend growth
σD = 5%
Mixed fund’s equity share
θ = 87.5%
Mixed fund’s sensitivity to risk premium
κ = 1
Speed of mean-reversion rate of behavioral disturbance
φb = 4%
Std. dev. of innovations to behavioral disturbance
σb = 3.3%
Time preference
β = 1.03
Risk aversion
γ = 2
Notes. Values are annualized.
Table 6: Moments generated by the calibration
Variable
Value
Macro elasticity
ζ = 0.16
Macro elasticity with mean-reverting ﬂow
ζM = ζ + κφf = 0.2
Macro market eﬀective discount factor, ρ = ζ/κ
ρ = 16%
Risk free rate
rf = 1%
Average equity premium
¯π = 4.4%
Average dividend-price ratio
δ = 3.4%
Std. dev. of stock returns
σr = 15%
Share of variance of stock returns due to ﬂows
89%
Share of variance of stock returns due to fundamentals
11%
Mean reversion rate of cumulative ﬂow and log D/P
φf = 4%
Std. dev. of innovation to cumulative ﬂow
σf = 2.8%
Slope of log price deviation to ﬂow
bp
f = 5
Slope of equity premium to ﬂow
bπ
f = −0.37
Notes. Values are annualized.
38

Table 7: Some stock market moments and predictive regressions
(a) Stock market moments
Data
Model
Std. dev. of excess stock returns
0.17
0.15
Mean P/D
37
33
Std. dev. of log P/D
0.42
0.5
(b) Predictive regressions
Data
Model
Horizon
Slope
S.E.
R2
Mean of slope
95% CI of slope
S.E.
R2
1 yr
0.11
(0.034)
0.07
0.14
[0.04, 0.32]
(0.048)
0.09
4 yr
0.36
(0.14)
0.18
0.61
[0.18, 1.19]
(0.17)
0.28
8 yr
1.00
(0.34)
0.40
1.34
[0.39, 2.50]
(0.31)
0.43
Notes. The data are for the United States for 1947-2018, and are calculated based on the CRSP
value-weighted index. The predictive regressions for the expected stock return in panel (b) are
Rt→t+T = αT + βT ln Dt
Pt , at horizon T (annual frequency). S.E. denotes the Newey-West standard errors
with 8 lags. 95% CI denotes the 95% conﬁdence interval of the estimated coeﬃcients on the simulated
data. Each run in the simulation uses 72 years.
stock returns. We see that the model features a large “excess volatility”: the ﬂow shocks (with their
2.8% annual standard deviation) account for almost 90% of the variance of stock returns. It may
be surprising that we can match the equity premium without any of the “modern” asset pricing
ingredients, such as a very high risk aversion or disaster risk. The reason is that the preferences of
our behavioral investors feature “narrow framing”, which leads to an average risk premium given by
¯π = γσ2
r.
Table 7 shows more moments speciﬁc to the stock market. We broadly match the volatility of
the log P/D ratio, its speed of mean reversion, and the predictive power of forecasting regressions
with that P/D ratio.
We conclude that our general equilibrium model featuring inelastic markets is competitive with
other widely-used general equilibrium models that match equity market moments. Its main advan-
tages, as we see it, are that it relies on an observable force, ﬂows in and out of equities and that it
matches our evidence on the macro elasticity of the market. Also, it retains the CRRA structure, so
it is easier to mesh with the basic macro models. Hence, it might be a useful prototype highlighting
how to think about inelastic market in general equilibrium.
6
Government Policy and Corporate Finance in Inelastic Mar-
kets
We now examine how a number of issues in ﬁnance change when markets are inelastic: government
and corporate policies. Many readers may wish to skip to the conclusion, but in our experience a
39

good fraction of readers will be interested in these topics.
6.1
Governments might stabilize the stock market via quantitative easing
in equities
In inelastic markets, the government might prop up asset values, perhaps in times of crisis, or to
help ﬁrms invest by raising equity at a high price. Indeed, suppose that the government buys f G
percent of the market, and keeps it forever. Then, the market’s valuation increases by p = fG
ζ .65 So,
if the government buys 1% of the market (which may represent roughly 1% of GDP), the market
goes up by 5%.66
This is what a number of central banks have done. In August 1998, the Hong Kong government,
when it was under a speculative attack, bought 6% of the Hong Kong stock market: this resulted in a
24% abnormal return, which was not reversed in the following eight weeks (Bhanot and Kadapakkam
(2006)).
This eﬀect is not entirely well-identiﬁed, but is consistent with a large price impact
multiplier 1
ζ, around 4. Likewise, the Bank of Japan owned 5% of the Japanese stock market in
March 2018 (Charoenwong et al. (2020)) and the Chinese “national team” (a government outﬁt)
owned a similar 5% of Chinese stocks in early 2020.67 In inelastic markets, this may have a large
price impact.68 Those government purchases of equities oﬀer a potentially attractive government
policy, as they increase market values and lower the cost of capital for ﬁrms, and relax credit
constraints. So, they might increase hiring and real investments by ﬁrms, and GDP. We think this
is an interesting direction for future research.69
6.2
Corporate ﬁnance in inelastic markets
Imagine that ﬁrms (the aggregate corporate sector) buy back shares in one period, reducing divi-
dends and hence keeping total payouts constant. What happens?
In a frictionless model, this does not aﬀect the ﬁrms’ values, as per Modigliani-Miller. In an
inelastic model, it should now be clear that buybacks can increase the aggregate value of equities.
How much depends on the rationality of households, as we now detail. For clarity and brevity,
we focus on the two-period model (the same economics holds with an inﬁnite horizon, but the
expressions are more complicated; see Section G.11). At time 0, we imagine the representative ﬁrm
buys back a fraction b of the equity shares, where b is small (so that the new number of shares is
Q′
0 = (1 −b) Q0). The buyback is ﬁnanced by a fall in the time-0 dividend, so the total dividend
payout falls from D0 to D′
0 = D0 −P0Q0b, where P0 is the ex-dividend price, and P0Q0b is used to
ﬁnance the share buyback.
65Note that we assume that investors do not change their holdings to counteract the government’s holdings,
meaning that Ricardian equivalence does not hold, perhaps because of a form of inattention to the government’s
actions (Gabaix (2020)).
66If the government buys it for just T periods, the impact is p =

1 −
1
(1+ρ)T

f G
ζ . Set ft = f G10≤t<T in (20).
With the above calibration, this can be a moderate dampening if T is large enough.
67Lockett, Hudson. “How the invisible hand of the state works in Chinese stocks.” Financial Times, 2/4/2020.
68We are not aware of a quantiﬁcation of the macro elasticity for Japan.
Barbon and Gianinazzi (2019) and
Charoenwong et al. (2020) quantity a micro elasticity – the diﬀerential impact on individual stocks that are owned
versus not owned by the government.
69Brunnermeier et al. (2020) caution about potentially adverse eﬀect if the government’s purchases might become
too central.
40

We need to take a stance on the households’ reaction to those buybacks. Call µD (respectively
µG) the fraction of the change in dividends (respectively, of the change in capital gain) that is
“absorbed” by the households – that is, consumed or reinvested in the pure bond fund. If the extra
dividend (respectively extra capital gain) is X dollars, consumers will “remove from the mixed fund”
µDX (respectively µGX) dollars. As households’ marginal propensity to consume is higher after a $1
dividend rather than a $1 capital gain (Baker et al. (2007)), it is likely that 0 < µG < µD < 1. We do
not seek here to endogenize µD and µG, which would be a good application of limited attention. We
simply trace their implications for the price impact of share buybacks in the following proposition
(which is proved in Section F).
Proposition 7. (Impact of share buybacks in a two-period model) Suppose that, at time 0, corpo-
rations buy back a fraction b of shares, lowering their dividend payments by the corresponding dollar
amount, hence keeping total payout constant at time 0. Then, the aggregate value of equities moves
by a fraction
v =
 µD −µG
θ
ζ + µGθ
b,
(56)
where µD (respectively µG) is the fraction of the change in dividends (respectively change in capital
gains) “absorbed” by households, i.e. removed from the mixed fund. If µD > µG (so that the marginal
propensity to consume out of dividends is higher than that out of capital gains), then share buybacks
increase the aggregate market value: v > 0.
A provisional calibration
Using the estimates of Di Maggio et al. (2020b), we set µD ≃
0.5 and µG ≃0.03. Then, (56) says that a buyback of 1% of the market increases the market
capitalization by 2.2%. The above papers (Baker et al. (2007); Di Maggio et al. (2020b)) do not
exactly measure µD and µG: they measure the impact on consumption, not on consumption plus
reallocation to pure bond funds. It is conceivable that some of the capital gains or dividends are
reinvested in bonds, even if they’re not consumed. So, µD (respectively µG) is likely to be higher
than the marginal propensity to consume out of dividends (respectively capital gains). In addition,
what matters is the “long run” propensity, which is hard to measure, and one may conjecture that
the long-run consumption adjustment to a lasting policy change will have µD −µG closer to 0.
One upshot is that it would be interesting for the empirical literature to estimate the long-run µD
and µG, as it is important to understand the impact of ﬁrms’ actions such as buybacks in inelastic
markets.
7
Conclusion
This paper ﬁnds, both theoretically and empirically, that the aggregate stock market is surprisingly
price-inelastic, so that ﬂows in and out of the market have a signiﬁcant impact on prices and risk
premia. We refer to this as the inelastic markets hypothesis. We provide tools to analyze inelastic
markets, with a simple model featuring key elasticities and an identiﬁcation strategy using the
recently developed method of granular instrumental variables, conceived for this project and laid
out in detail in Gabaix and Koijen (2020).
We emphasize though that the “inelastic market hypothesis” remains just that: a hypothesis.
Our empirical analysis relies on a new empirical methodology and on fairly unexplored data in this
41

context. An important takeaway from this paper is that the demand elasticity of the aggregate
stock market is a key parameter of interest in asset pricing and macro-ﬁnance, just like investors’
risk aversion, their elasticity of inter-temporal substitution, and the micro elasticity of demand. We
provide a ﬁrst estimate, and we hope that future research will explore other identiﬁcation strategies
to improve and sharpen this estimate.
If the inelastic markets hypothesis is correct, it invalidates or qualiﬁes a number of common
views in ﬁnance and it provides new directions to answer longstanding questions in ﬁnance. We
outline and then discuss those tenets.
How tenets of ﬁnance change if the inelastic markets hypothesis is correct
“Permanent price impact must reﬂect information.”
In Proposition 5, a one-time, non mean-
reverting inﬂow permanently changes prices (as in p =
f
ζ ), even if it contains no information
whatsoever. This is because a permanent change in the demand for equities must permanently
change their equilibrium prices – and this eﬀect is quantitatively important in inelastic markets.
The typical empirical strategy to look for reversals as signs of ﬂows (rather than information) moving
prices does not work in this case. By the same logic, we can see large changes in prices but small
changes in long-horizon expected returns.
“Fast and smart investors (perhaps hedge funds) will provide enough elasticity to the market.”
This is not true: in part because hedge funds are small (they own less than 5% of the market,
see Section 2), they cannot provide much elasticity for the market as a whole (so ζ remains low),
even though they might ensure short term news are incorporated quickly (so that κ is quite high).
In addition, those smart-money investors often face risk constraints and outﬂows that limit their
ability to aggressively step in during aggregate downturns.
“Trading volume is very high, so the equity market must be very elastic.” Trading volume in the
equity market is high (about 100% of the value of the market each year), but most of it exchanges
one share for another share (perhaps via a round-trip through cash).
These trades within the
universe of equities do no count toward the aggregate ﬂow f, which is a (signed) ﬂow from bonds
to equities.
“For every buyer there is a seller; so, saying ‘there was an increase in the demand for equities’
is meaningless.” Economists often appeal to the truism that “for every buyer there is a seller” to
disregard the notion that a measurable increase in the willingness of the average trader to buy
more of the market will push prices up (“buying pressure”). Our model clariﬁes that this reasoning
is incorrect. In Proposition 2, f is the pressure to buy stocks (if it is positive), and the demand
q = −ζp + f has a component −ζp expressing that “sellers” appetite to sell shares to “buyers”
represented by f. So there are both buyers and sellers (or really, a force making the representative
fund buy, and a force making it sell), but at the same time, buying pressure f does move the price
by p = f
ζ . Moreover, it is directly measurable via the change in asset holdings (bonds in the case of
the undergraduate example of Section 3.1), as in (10).
“The market often looks impressively eﬃcient in the short run, so it must be quite macro-
eﬃcient.” The contrast between the market’s “short run eﬃciency” and “macro-eﬃciency” is sharp
in equation (20): future events are discounted at a rate ρ =
ζ
κ = δ + 1−θ
κ , so that a highly far-
sighted market has a lower value of ρ. So, the market can be very forward-looking (low ρ), even if
it is very macro-inelastic (low ζ), provided that “far-sightedness” κ is relatively high compared to
ζ (for example, because there are a few powerfully forward-looking arbitrageurs). As an example,
consider the announcement of an event that will take eﬀect in a week, such as a permanent increase
42

in dividends or inﬂows. In our calibration, the market’s current reaction to the announcement is a
fraction 99.8% of the eventual present value of the future dividends or inﬂows.70 In that sense, the
market looks impressively eﬃcient. But again, it is “short-term predictability eﬃcient” (it smooths
announcements) and “micro eﬃcient” (it processes well the relative valuations of stocks), but it is
not “macro eﬃcient” (as Samuelson (1998) put it) or “long-term predictability eﬃcient” – it does
not absorb well very persistent shocks. Furthermore, even though prices respond promptly around
major events, it is generally hard to assess whether the market moved by just the right amount,
or instead under- or over-reacted. In addition to a large literature demonstrating drifts in prices
before and after macro events (such as Federal Open Market Committee meetings), our model
implies that persistent ﬂows around such events can lead to persistent deviations in prices, and
typical event study graphs that do not display much of a drift in prices following the event would
be uninformative about macro eﬃciency.
“Share buybacks do not aﬀect equity returns, as proved by the Modigliani-Miller theorem.” In
the traditional frictionless model, the return impact of a share buyback should be zero. However,
in our model, if ﬁrms in the aggregate buy back $1 worth of equity, that can increase aggregate
valuations (Section 6.2 detailed this). Hence, share buybacks are potentially a source of ﬂuctuations
in the market. In our model, a combination of fund mandates and consumers’ bounded rationality
leads to a violation of the Modigliani-Miller neutrality. More broadly, corporate actions such as
share issuances, transactions by insiders, et cetera, may have a large impact on prices beyond any
informational channel. Most extant empirical evidence focuses on announcements at the ﬁrm level,
while we emphasize their impact at the aggregate level. By focusing on well-identiﬁed ﬁrm-level
responses, one identiﬁes the micro-elasticity, not the macro elasticity ζ. It will be interesting to
explore in detail how important corporate decisions are for ﬂuctuations in the aggregate stock
market.
“Markets must be macro elastic as otherwise small ﬂows would imply large price changes and
market timing strategies would be too proﬁtable.” The Sharpe ratios of market timing strategies
depend on the properties of ﬂows, see (23) and (24). If ﬂows are highly persistent, prices may move
a lot, but the per-period expected excess returns do not change much. Indeed, in the model in
Section 5, the persistence of the dividend yield matches its empirical counterpart and using it for
market-timing purposes does not work well out of sample.
We next discuss a few questions that seem important for future research.
Why is the aggregate demand for equities so inelastic?
The core of the inelastic markets
hypothesis is that the macro demand elasticity ζ is low. Why is it so low? We highlighted two
reasons, namely ﬁxed-share mandates (so that ζ > 0, κ = 0), such as those of many funds that
are 100% in equities and hence have zero elasticity, and inertia (i.e., some funds or people are just
buy-and-hold, creating ζ = κ = 0). This may be due to a taste for simplicity, or to agency frictions:
as the household is not sure about the quality of the manager, a simple scheme like a constant share
in equities may be sensible – otherwise the manager may take foolish risks.
There are other possibilities.
If some funds have a Value-at-Risk constraint, and volatility
goes up a lot in bad times, they need to sell when the markets fall, so that their ζ and κ are
negative. A diﬀerent possibility is that when prices move, people’s subjective perception of the
equity premium does not move much. One reason might be that investors think the rest of the
market is well-informed. Also, going from market prices to the equity premium is a statistically
70Indeed, (1 + ρ)−T = 99.8%, taking the ρ calibrated in Section 3.2 and T = 1/52 years.
43

error-prone procedure, so that market participants may shrink towards no reaction to this (Black
(1986), Summers (1986)). Alternatively, many investors may not place much weight on the price-
earnings ratio as a reliable forecasting tool, perhaps because they want parsimonious models and
price-dividend ratios are not that useful as short-run forecasters, or because many investors just
do not wish to bother paying attention to them (Gabaix (2014), Chinco and Fos (2019)). The
pass-through between subjective beliefs and actions might be low, as it is for retail investors (Giglio
et al. (2021a)). Finally, demand may respond little to prices because demand shocks are highly
persistent.71 In the end, while identifying the exact reasons for low market elasticity is interesting,
this question has a large number of plausible answers. Fortunately, it is possible to write a framework
in a way that is relatively independent to the exact source of low elasticity, and this is the path we
chose.
What are the determinants of ﬂows?
It is clear that it would be desirable to know more
about the determinants of ﬂows at a high frequency.
We provided a minimalist model with a
“behavioral disturbance” (which was enough to study its general equilibrium impact), and some
simple correlations in Section 4.4, but this is clearly a ﬁrst pass. Establishing the various channels
of ﬂows could be a whole line of enquiry, perhaps with micro data such as those used by Calvet et
al. (2009) or Giglio et al. (2021a).
To appreciate the richness of those determinants, let us observe that ﬂow shocks could come from
various sources, such as: (i) changes in beliefs about future ﬂows or fundamentals, as these both
aﬀect expected returns, per Proposition 5; (ii) “liquidity needs”, for instance insurance companies
selling stocks after a hurricane; (iii) more generally, heterogeneous income or wealth shocks to
diﬀerent groups (including foreign versus domestic investors) changing the eﬀective propensity to
invest in stocks by the average investor; (iv) corporate actions by ﬁrms such as decisions to buy
back or issue shares; (v) shocks to substitute assets, which might for example prompt investors to
rebalance towards stocks when bond yields go down; (vi) changes in the advertising or advice by
institutional advisers, as explored in Ben-David et al. (2020b); (vii) “road shows” in which ﬁrms
or governments try to convince potential investors to buy into a prospective equity oﬀering or
privatization; (viii) mechanical forced trading via “delta hedging,” whereby traders who have sold
put options and continuously hedge them need to sell stocks when stock prices fall.
Some further outstanding questions
In addition to the two questions we just discussed, our
framework makes a number of further issues interesting and researchable. For example, how much
can and should governments intervene in equity markets? Do share buybacks account for a large
share of market ﬂuctuations? How forward-looking are the policies of funds (κ)? Generalizing,
what are the cross-market elasticities, meaning the forces that create “contagion” across market?
These same eﬀects will also generalize to other markets (such as the markets for corporate bonds
71For instance, imagine a very simple model ft = P
k FkI
 t ∈

τ 0
k, τ 1
k

, where Fk is constant,

τ 0
k, τ 1
k

the period of
time that a ﬂows stays in the market, and τ 1
k −τ 0
k ∼exp (λ) . From an institutional perspective, one can also imagine
that a large asset manager launches a fund that attracts capital, and that this capital is sticky, but the period for
which it stays is unclear. If λ is low, then prices will respond sharply to the ﬂow, even though the expected return
does not move much. Uncertainty about the persistence of the demand shock introduces uncertainty about how
the price change maps to expected returns, leading to a muted response and a low ζ. This model is in quite sharp
contrast with the traditional view in which ﬂows have a temporary price impact (for instance Coval and Staﬀord
(2007)).
44

and currencies): if so, how and what are the policy implications? This is a rich number of questions
that hopefully economists will be able to answer in the coming years.
A
Appendix: Main proofs
Proof of Proposition 2
At time 0−, before the inﬂow shocks, fund i’s wealth is ¯Wi = ¯P ¯Qi + ¯B,
where ¯P ¯Qi and ¯Bi are respectively the fund’s holdings of equities and bonds:
¯P ¯Qi = θi ¯Wi,
¯Bi = (1 −θi) ¯Wi.
At time 0, after the inﬂow shock, and the change in the equilibrium price to P, the fund’s wealth
is Wi = P ¯Qi + ¯Bi + ∆Fi, so that ∆Wi = (∆P) ¯Qi + ∆Fi. So, the value of the assets in the fund
changes by a fraction:
wi := ∆Wi
¯Wi
=
¯Qi∆P
¯Wi
+ ∆Fi
¯Wi
=
¯P ¯Qi
¯Wi
× ∆P
¯P
+ fi = θi × p + fi,
that is:
wi = θip + fi.
(57)
This means that the value of the fund increases via the inﬂow of fi, and via the appreciation of the
stock p, to which the fund has an exposure θi.
Let us ﬁrst take the case κi = 0. The demand (1) is:
Qi = θiWi
P
= θi ¯Wi (1 + wi)
¯P (1 + p)
= ¯Qi
1 + wi
1 + p ,
so that the fractional change in the fund’s demand for shares is:
qi = Qi
¯Qi
−1 = wi −p
1 + p = θip + fi −p
1 + p
= fi −ζip
1 + p ,
with ζi = 1 −θi. We see how −ζi is the (signed) demand elasticity, which includes crucial income
eﬀects.72 For small price changes, this gives qi ≃fi −ζpi. We also see that, when κi = 0 for all
funds, the equilibrium condition qD
S = 0 leads to p = fS
ζS exactly.
Next, consider the case with a general κi. Taking logs and then deviations from the baseline
D/P ratio gives:
∆ln De
P = ∆ln De −∆ln P = d −p.
On the other hand, as δ = De
P = 1 + rf + π, we have ∆ln De
P =
∆π
1+rf+π = δˆπ (with ˆπ = ∆π), so that:
ˆπ = δ (d −p) .
(58)
72This is the compensated or Hicksian elasticity of demand: indeed, after the price change, the fund can purchase
its old holdings (which is the foundation of the Hicksian demand), simply because it already owns them). Controlling
for fund wealth, the demand elasticity is −1. But given fund wealth has an elasticity θ to the price, the total demand
elasticity (−ζ) is −1 + θ.
45

We take logs in (1), so that ln Qi = ln Wi + ln θi −ln Pi + κiˆπ. Given that initially ln ¯Qi =
ln ¯
Wi + ln θi −ln ¯P, taking diﬀerences we have ∆ln Qi = ∆ln Wi −∆ln P + κiˆπ. Finally, we use the
Taylor expansion ∆ln Wi ≃wi and ∆ln P ≃p to yield:
qi = wi −p + κiˆπ.
(59)
Using (57), we obtain (7):
qi = −(1 −θi) p + fi + κiδ (d −p) = −(1 −θi + κiδ) p + fi + κiδd.
Proof of Proposition 4
We call Ft the cumulative inﬂow into the mixed fund, normalizing F0 to
be the mixed fund’s initial endowment of bonds. Then, as all dividend and bond coupon are given
to the consumer, Wt = PtQ+Ft, and in the baseline economy ¯Wt = ¯PtQ+ ¯Ft. We call ˜Ft := Ft −¯Ft
the deviation of the dollar ﬂows from the baseline. Subtracting, we have Wt−¯Wt =
 Pt −¯Pt

Q+ ˜Ft,
i.e. ¯Wtwt = ¯PtQpt + ˜Ft, so with ft =
˜Ft
¯
Wt,
wt = θpt + ft.
(60)
Now, from the demand for stocks, we have QtPt = Wtθeκˆπt+νt, while in the baseline economy
¯Qt ¯Pt = ¯Wtθ. Dividing through, we get: QtPt
¯Qt ¯Pt = Wt
¯
Wteκˆπt+νt, so that (1 + qt) (1 + pt) = (1 + wt) eκˆπt+νt.
Linearizing, qt + pt = wt + κˆπt + νt. Hence, by (60),
qt = −(1 −θ) pt + κˆπt + ft + νt.
(61)
Finally, using ˆπt = δ (de
t −pt) + Et [∆pt+1] (see (18)), we obtain qt = −(1 −θ + κδ) pt + κδde
t +
κEt [∆pt+1] + ft + νt.
Proof of Proposition 5
Equation (19) can be rewritten as qt = κ (Et∆pt+1 −ρpt + δde
t)+ft+νt.
As qt = 0, this is also:
Et∆pt+1 −ρpt + δde
t + ft + νt
κ
= 0.
(62)
Deﬁning zt := δde
t + ft+νt
κ , this gives pt = Etpt+1+zt
1+ρ
, so that pt = Et
P∞
τ≥t
zτ
(1+ρ)τ−t+1. The equity
premium comes from (61) with qt = 0.
B
Appendix: Identiﬁcation methodology
We summarize the algorithms that we use to estimate the multipliers and elasticities in Section
4.2 and the multipliers in Section 4.3. The algorithms are the same, with some minor adjustments
given the unique features of either the FoF data or 13F data.
B.1
Algorithm used for sector-level data
We summarize the algorithm that we use for the Flow of Funds (FoF) data in Section 4.2.
46

1. We construct pseudo-equal value weights ˜Ei,t−1, where we start from ˜Eσ
i =
σ−2
i
PN
k=1 σ−2
k , where
σi = σ (∆qit), and deﬁne ˜Ei = min
n
ξ ˜Eσ
i , 1.5
N
o
, where ξ ≥1 is tuned so that P
i ˜Ei = 1. We
exclude the corporate sector in constructing the instrument. This winsorizes the quasi-equal
weights to be at most 50% higher than strict equal weights. This adjustment ensures that the
equal weights are not too concentrated for sectors with very stable ∆qit.73 This is relevant
when the number of sectors is small, as is the case for the FoF.
2. We run the panel regression
∆qit = αi + βt + γi∆yt + δit + ∆ˇqit,
(63)
using ˜E as regression weights, and construct the ∆ˇqit as the residuals. Here ∆yt is quarterly
real GDP growth and we allow for a time trend as some sectors grew substantially faster in,
for instance, the nineties than in the subsequent period.
3. We extract the principal components of ˜E
1
2
i ∆ˇqit and denote the estimated vector of principal
components by ηPC,e
t
.
4. We construct the GIV instrument:74
Zt =
N
X
i=1
Si,t−1∆ˇqit.
(64)
5. We estimate the multiplier, M, using the time-series regression
∆pt = α + MZt + λ′
Pηe
t + et,
(65)
where ηe
t =

∆yt, ηPC,e
t

. This regression is also the ﬁrst stage to estimate the elasticities.
Instrumenting ∆pt by Zt in both cases, we estimate the demand elasticity via
∆qEt = αE −ζ∆pt + λ′
Eηe
t + et,
(66)
and the supply elasticity via
∆qCt = αC −ζC∆pt + λ′
Cηe
t + et.
(67)
73Quasi-equal weights ˜Ej are preferable to equal weights Ej =
1
N as they add precision — in the same way in
which to estimate a mean, weighing by inverse variance is better than equal weighing (Gabaix and Koijen (2020)).
The primary objective of inverse variance weighing is to downplay the importance of very volatile sectors that may
distort the estimation of the common factors. If the inverse variance weights get too concentrated as some sectors
are very stable, the same concern applies, and we therefore winsorize the weights at 1.5
N . While 50% is somewhat
arbitrary, it is a signiﬁcant departure from equal weights. We also explore the sensitivity of our results to this cutoﬀ
in Section D.4, and ﬁnd them to be robust.
74An equivalent way to proceed is to use zt = PN
i=1 Si,t−1ˇuit, where ˇuit is the measure of idiosyncratic shock
common from step 4. This way, zt is made of idiosyncratic shocks. As we control for ηP C,e
t
below, the two procedures
are similar.
47

B.2
Algorithm used for investor-level data
We summarize the algorithm that we use to extract factors, ηt, in Section 4.3.
1. We run the panel regression
∆qit = ai + bi∆yt + ct + η1tx1i,t−1 + η2tx2i,t−1 + ∆ˇqit,
where ∆yt is GDP growth, ai is an investor ﬁxed eﬀect, ct is a time ﬁxed eﬀect, x1i,t−1 is
lagged size, and x2i,t−1 lagged active share. We collect the residuals, ∆ˇqit.
2. We compute the time-series standard deviation of ∆ˇqit by investor. In each quarter, we sort
investors into 20 groups based on this standard deviation. Intuitively, funds with diﬀerent
volatilities of ∆ˇqit are likely to have diﬀerent exposures to the factors. By group and quarter,
we average ∆ˇqit, ∆ˇqE
gt, where g indexes the groups.
3. We extract principal components based on the panel of 20 groups of ∆ˇqE
gt.
References
Amiti, Mary and David E Weinstein, “How much do idiosyncratic bank shocks aﬀect investment? Evidence
from matched bank-ﬁrm loan data,” Journal of Political Economy, 2018, 126 (2), 525–587.
Bacchetta, Philippe and Eric Van Wincoop, “Infrequent portfolio decisions: A solution to the forward discount
puzzle,” American Economic Review, 2010, 100 (3), 870–904.
Baker, Malcolm and Jeﬀrey Wurgler, “A catering theory of dividends,” The Journal of Finance, 2004, 59 (3),
1125–1165.
Baker, Malcolm, Stefan Nagel, and Jeﬀrey Wurgler, “The Eﬀect of Dividends on Consumption,” Brookings
Papers on Economic Activity, 2007, 38 (1), 231–292.
Bansal, Ravi and Amir Yaron, “Risks for the Long Run: A Potential Resolution of Asset Pricing Puzzles,”
Journal of Finance, 2004, 59 (4), 1481–1509.
Barberis, Nicholas and Andrei Shleifer, “Style investing,” Journal of ﬁnancial Economics, 2003, 68 (2), 161–199.
Barberis, Nicholas, Ming Huang, and Richard H Thaler, “Individual preferences, monetary gambles, and
stock market participation: A case for narrow framing,” American economic review, 2006, 96 (4), 1069–1090.
Barbon, Andrea and Virginia Gianinazzi, “Quantitative Easing and Equity Prices: Evidence from the ETF
Program of the Bank of Japan,” The Review of Asset Pricing Studies, 2019, 9 (2), 210–255.
Barro, Robert J, “Rare disasters and asset markets in the twentieth century,” The Quarterly Journal of Economics,
2006, 121 (3), 823–866.
Ben-David, Itzhak, Francesco Franzoni, and Rabih Moussawi, “Hedge fund stock trading in the ﬁnancial
crisis of 2007–2009,” The Review of Financial Studies, 2012, 25 (1), 1–54.
Ben-David, Itzhak, Francesco Franzoni, and Rabih Moussawi, “Do ETFs Increase Volatility?,” The Journal
of Finance, 2018, 73 (6), 2471–2535.
Ben-David, Itzhak, Francesco Franzoni, Rabih Moussawi, and John Sedunov, “The granular nature of
large institutional investors,” Management Science, forthcoming.
48

Ben-David, Itzhak, Jiacui Li, Andrea Rossi, and Yang Song, “Non-Fundamental Demand and Style Returns,”
2020. Working Paper.
Ben-David, Itzhak, Jiacui Li, Andrea Rossi, and Yang Song, “Style Investing, Positive Feedback Loops, and
Asset Pricing Factors,” Working Paper, 2020.
Ben-Rephael, Azi, Shmuel Kandel, and Avi Wohl, “Measuring investor sentiment with mutual fund ﬂows,”
Journal of Financial Economics, 2012, 104 (2), 363–382. Special Issue on Investor Sentiment.
Bhanot, Karan and Palani-Rajan Kadapakkam, “Anatomy of a government intervention in index stocks: Price
pressure or information eﬀects?,” The Journal of Business, 2006, 79 (2), 963–986.
Black, Fischer, “Noise,” The Journal of Finance, 1986, 41 (3), 528–543.
Bordalo, Pedro, Nicola Gennaioli, Rafael La Porta, and Andrei Shleifer, “Expectations of Fundamentals
and Stock Market Puzzles,” Technical Report, National Bureau of Economic Research 2020.
Bouchaud, Jean-Philippe, Julius Bonart, Jonathan Donier, and Martin Gould, Trades, quotes and prices:
ﬁnancial markets under the microscope, Cambridge University Press, 2018.
Brainard, William C. and James Tobin, “Pitfalls in Financial Model Building,” American Economic Review:
Papers and Proceedings, 1968, 58 (2), 99–122.
Brunnermeier, Markus K. and Stefan Nagel, “Hedge Funds and the Technology Bubble,” The Journal of
Finance, 2004, 59, 2013–2040.
Brunnermeier, Markus K, Michael Sockin, and Wei Xiong, “China’s model of managing the ﬁnancial system,”
Technical Report, National Bureau of Economic Research 2020.
Buﬀa, Andrea M, Dimitri Vayanos, and Paul Woolley, “Asset management contracts and equilibrium prices,”
Technical Report, National Bureau of Economic Research 2019.
Caballero, Ricardo J and Alp Simsek, “A risk-centric model of demand recessions and speculation,” The Quar-
terly Journal of Economics, 2019.
Calvet, Laurent E., John Y. Campbell, and Paolo Sodini, “Fight Or Flight?
Portfolio Rebalancing by
Individual Investors,” Quarterly Journal of Economics, 2009, 124 (1), 301–348.
Camanho, Nelson, Harald Hau, and Hélène Rey, “Global portfolio rebalancing and exchange rates,” Working
Paper, 2019.
Campbell, John Y. and John H. Cochrane, “By Force of Habit: A Consumption-Based Explanation of Aggre-
gate Stock Market Behavior,” Journal of Political Economy, 1999, 107 (2), 205–251.
Carvalho, Vasco M and Basile Grassi, “Large ﬁrm dynamics and the business cycle,” American Economic
Review, 2019, 109 (4), 1375–1425.
Chang, Yen-Cheng, Harrison Hong, and Inessa Liskovich, “Regression Discontinuity and the Price Eﬀects of
Stock Market Indexing,” Review of Financial Studies, 2014, 28 (1), 212–246.
Charoenwong, Ben, Randall Morck, and Yupana Wiwattanakantang, “Bank of Japan Equity Purchases:
The Final Frontier in Extreme Quantitative Easing,” April 2020. NBER Working Paper 25525.
Chien, YiLi, Harold Cole, and Hanno Lustig, “Is the volatility of the market price of risk due to intermittent
portfolio rebalancing?,” American Economic Review, 2012, 102 (6), 2859–96.
Chinco, Alexander and Vyacheslav Fos, “The sound of many funds rebalancing,” 2019.
Cochrane, John H., “Presidential Address: Discount Rates,” The Journal of Finance, 2011, 66 (4), 1047–1108.
49

Cole, Allison, Jonathan Parker, and Antoinette Schoar, “Household Portfolios and Retirement Saving Over
the Life Cycle,” 2021. Working Paper, MIT Sloan.
Coval, Joshua and Erik Staﬀord, “Asset ﬁre sales (and purchases) in equity markets,” Journal of Financial
Economics, 2007, 86 (2), 479–512.
Cutler, David M, James M Poterba, and Lawrence H Summers, “Speculative Dynamics And The Role Of
Feedback Traders,” The American Economic Review Papers and Proceedings, 1990, 80 (2), 63–68.
Da, Zhi, Borja Larrain, Clemens Sialm, and Jose Tessada, “Destabilizing Financial Advice: Evidence from
Pension Fund Reallocations,” Review of Financial Studies, 2018, 31 (10), 3720–3755.
De Long, J. Bradford, Andrei Shleifer, Lawrence H. Summers, and Robert J. Waldmann, “Noise Trader
Risk in Financial Markets,” Journal of Political Economy, 1990, 98 (4), 703–738.
Deuskar, Prachi and Timothy C. Johnson, “Market Liquidity and Flow-driven Risk,” The Review of Financial
Studies, 2011, 24 (3), 721–752.
Di Giovanni, Julian and Andrei A Levchenko, “Country size, international trade, and aggregate ﬂuctuations
in granular economies,” Journal of Political Economy, 2012, 120 (6), 1083–1132.
Di Maggio, Marco, Amir Kermani, and Kaveh Majlesi, “Stock Market Returns and Consumption,” Journal
of Finance, 2020, 75 (6), 3175–3219.
Dierker, Martin, Jung-Wook Kim, Jason Lee, and Randall Morck, “Investors’ Interacting Demand and
Supply Curves for Common Stocks,” Review of Finance, 2016, 20 (4), 1517–1547.
Dong, Xi, Namho Kang, and Joel Peress, “How the Speed of Capital Aﬀects Factor Momentum, Reversal and
Volatility?,” Available at SSRN, 2021.
Dou, Winston, Leonid Kogan, and Wei Wu, “Common Fund Flows: Flow Hedging and Factor Pricing,”
Available at SSRN, 2020.
Duﬃe, Darrell, “Presidential Address: Asset Price Dynamics with Slow-Moving Capital,” Journal of Finance, 2010,
65 (4), 1237–1267.
Duﬃe, Darrell and Bruno Strulovici, “Capital mobility and asset pricing,” Econometrica, 2012, 80 (6), 2469–
2509.
Edelen, Roger M and Jerold B Warner, “Aggregate price eﬀects of institutional trading: a study of mutual
fund ﬂow and market returns,” Journal of Financial Economics, 2001, 59 (2), 195–220.
Farmer, Roger, Expectations, employment and prices, Oxford University Press, 2010.
Frazzini, Andrea and Owen A Lamont, “Dumb money: Mutual fund ﬂows and the cross-section of stock returns,”
Journal of Financial Economics, 2008, 88 (2), 299–322.
Frazzini, Andrea, Ronen Israel, and Tobias J Moskowitz, “Trading costs,” Working Paper, 2018.
Friedman, Benjamin M., “Financial Flow Variables and the Short-Run Determination of Long-Term Interest
Rates,” Journal of Political Economy, 1977, 85 (4), 661–689.
Gabaix, Xavier, “The granular origins of aggregate ﬂuctuations,” Econometrica, 2011, 79 (3), 733–772.
Gabaix, Xavier, “Variable rare disasters: An exactly solved framework for ten puzzles in macro-ﬁnance,” The
Quarterly journal of economics, 2012, 127 (2), 645–700.
Gabaix, Xavier, “A sparsity-based model of bounded rationality,” The Quarterly Journal of Economics, 2014, 129
(4), 1661–1710.
50

Gabaix, Xavier, “Behavioral Inattention,” Handbook of Behavioral Economics, 2019, 2, 261–344.
Gabaix, Xavier, “A behavioral New Keynesian model,” American Economic Review, 2020, 110 (8), 2271–2327.
Gabaix, Xavier and Matteo Maggiori, “International liquidity and exchange rate dynamics,” The Quarterly
Journal of Economics, 2015, 130 (3), 1369–1420.
Gabaix, Xavier and Ralph SJ Koijen, “Granular instrumental variables,” Working Paper 28204, National Bureau
of Economic Research December 2020.
Gabaix, Xavier, Arvind Krishnamurthy, and Olivier Vigneron, “Limits of arbitrage: theory and evidence
from the mortgage-backed securities market,” The Journal of Finance, 2007, 62 (2), 557–595.
Galaasen, S, R Jamilov, R Juelsrud, and H Rey, “Granular credit risk,” Technical Report, Working paper
2020.
Garleanu, Nicolae, Lasse Heje Pedersen, and Allen M. Poteshman, “Demand-Based Option Pricing,” Review
of Financial Studies, 2009, 22 (10), 4259–4299.
Ghysels, Eric, Hanwei Liu, and Steve Raymond, “Institutional Investors and Granularity in Equity Markets,”
2021. Working Paper.
Giglio, Stefano, Matteo Maggiori, Johannes Stroebel, and Stephen Utkus, “Five Facts About Beliefs and
Portfolios,” American Economic Review, 2021, 111 (5), 1481–1522.
Goetzmann, William N. and Massimo Massa, “Index Funds and Stock Market Growth,” The Journal of
Business, 2003, 76 (1), 1–28.
Gourinchas, Pierre-Olivier, Walker Ray, and Dimitri Vayanos, “A preferred-habitat model of term premia
and currency risk,” Working Paper, 2020.
Greenwood, Robin and Andrei Shleifer, “Expectations of returns and expected returns,” The Review of Finan-
cial Studies, 2014, 27 (3), 714–746.
Greenwood, Robin and Dimitri Vayanos, “Bond Supply and Excess Bond Returns,” The Review of Financial
Studies, 2014, 27 (3), 663–713.
Greenwood, Robin and Samuel G Hanson, “Issuer quality and corporate bond returns,” The Review of Financial
Studies, 2013, 26 (6), 1483–1525.
Greenwood, Robin, Samuel G Hanson, Jeremy C Stein, and Adi Sunderam, “A quantity-driven theory of
term premiums and exchange rates,” Working Paper, 2019.
Hamilton, James D., “Why You Should Never Use the Hodrick-Prescott Filter,” The Review of Economics and
Statistics, 2018, 100 (5), 831–843.
Harris, Lawrence and Eitan Gurel, “Price and Volume Eﬀects Associated with Changes in the S&P 500 List:
New Evidence for the Existence of Price Pressures,” Journal of Finance, 1986, 41 (4), 815–829.
He, Zhiguo and Arvind Krishnamurthy, “Intermediary Asset Pricing,” American Economic Review, 2013, 103
(2), 732–770.
Herskovic, Bernard, Bryan T Kelly, Hanno N Lustig, and Stijn Van Nieuwerburgh, “Firm volatility in
granular networks,” Journal of Political Economy, forthcoming.
Johnson, Timothy C, “Dynamic liquidity in endowment economies,” Journal of Financial Economics, 2006, 80
(3), 531–562.
51

Kahneman, Daniel and Dan Lovallo, “Timid choices and bold forecasts: A cognitive perspective on risk taking,”
Management science, 1993, 39 (1), 17–31.
Kekre, Rohan and Moritz Lenel, “Monetary policy, redistribution, and risk premia,” University of Chicago,
Becker Friedman Institute for Economics Working Paper, 2020, (2020-02).
Kendall, Maurice G, “Note on bias in the estimation of autocorrelation,” Biometrika, 1954, 41 (3-4), 403–404.
Koijen, Ralph SJ and Motohiro Yogo, “A demand system approach to asset pricing,” Journal of Political
Economy, 2019, 127 (4), 1475–1515.
Koijen, Ralph SJ and Motohiro Yogo, “Exchange Rates and Asset Prices in a Global Demand System,” 2020.
NBER Working Paper 27342.
Koijen, Ralph SJ, Robert J Richmond, and Motohiro Yogo, “Which investors matter for global equity
valuations and expected returns?,” Working Paper, 2019.
Koijen, Ralph SJ, Tobias J Moskowitz, Lasse Heje Pedersen, and Evert B Vrugt, “Carry,” Journal of
Financial Economics, 2018, 127 (2), 197–225.
Kondor, Péter and Dimitri Vayanos, “Liquidity risk and the dynamics of arbitrage capital,” The Journal of
Finance, 2019, 74 (3), 1139–1173.
Kyle, Albert S., “Continuous Auctions and Insider Trading,” Econometrica, 1985, 53 (6), 1315–1335.
Li, Jennifer, Neil D. Pearson, and Qi Zhang, “Impact of Demand Shocks on the Stock Market: Evidence from
Chinese IPOs,” 2020. Working Paper.
Li, Jiacui, “Slow-moving liquidity provision and ﬂow-driven common factors in stock returns,” Available at SSRN
2909960, 2018.
Li, Jiacui, “What Drives the Size and Value Factors?,” 2021. Working Paper, University of Utah.
Lou, Dong, “A Flow-Based Explanation for Return Predictability,” The Review of Financial Studies, 12 2012, 25
(12), 3457–3489.
Lucas, Robert E. Jr., “Asset Prices in an Exchange Economy,” Econometrica, 1978, 46 (6), 1429–1445.
Ma, Yueran, “Nonﬁnancial Firms as Cross-Market Arbitrageurs,” The Journal of Finance, 2019, 74 (6), 3041–3087.
Martin, Ian, “What is the Expected Return on the Market?,” The Quarterly Journal of Economics, 2017, 132 (1),
367–433.
Mitchell, Mark, Lasse Heje Pedersen, and Todd Pulvino, “Slow moving capital,” American Economic Review
Papers and Proceedings, 2007, 97 (2), 215–220.
Moreira, Alan, “Capital immobility and the reach for yield,” Journal of Economic Theory, 2019, 183, 907–951.
Newey, Whitney K. and Kenneth D. West, “Automatic Lag Selection in Covariance Matrix Estimation,” The
Review of Economic Studies, 10 1994, 61 (4), 631–653.
Parker, Jonathan A, Antoinette Schoar, and Yang Sun, “Retail Financial Innovation and Stock Market
Dynamics: The Case of Target Date Funds,” Working Paper, 2020.
Pavlova, Anna and Taisiya Sikorskaya, “Benchmarking Intensity,” Working Paper, 2020.
Peng, Cameron and Chen Wang, “Factor demand and factor returns,” Working Paper, 2021.
52

Petajisto, Antti, “Why do demand curves for stocks slope down?,” Journal of Financial and Quantitative Analysis,
2009, 44 (5), 1013–1044.
Rigobon, Roberto, “Identiﬁcation through Heteroskedasticity,” The Review of Economics and Statistics, 2003, 85
(4), 777–792.
Samuelson, Paul A, “Summing up on business cycles: opening address,” Conference Proceedings of the Federal
Reserve Bank of Boston, 1998, 42, 33–36.
Schmickler, Simon, “Identifying the Price Impact of Fire Sales Using High-Frequency Surprise Mutual Fund Flows,”
Working Paper, 2020.
Shiller, Robert, “Stock prices and social dynamics,” Brookings papers on economic activity, 1984, 1984 (2), 457–510.
Shleifer, Andrei, “Do Demand Curves for Stocks Slope Down?,” Journal of Finance, 1986, 41 (3), 579–590.
Shleifer, Andrei, “Ineﬃcient markets: An introduction to behavioural ﬁnance,” Oxford University Press, 2000.
Summers, Lawrence H, “Does the stock market rationally reﬂect fundamental values?,” The Journal of Finance,
1986, 41 (3), 591–601.
Tobin, James, “Monetary policy: recent theory and practice,” in “Current Issues in Monetary Economics,” Springer,
1998, pp. 13–21.
Vayanos, Dimitri and Jean-Luc Vila, “A preferred-habitat model of the term structure of interest rates,” Working
Paper, 2020.
Vayanos, Dimitri and Paul Woolley, “An Institutional Theory of Momentum and Reversal,” Review of Financial
Studies, 2013, 26 (5), 1087–1145.
Wachter, Jessica A, “Can time-varying risk of rare disasters explain aggregate stock market volatility?,” The
Journal of Finance, 2013, 68 (3), 987–1035.
Warther, Vincent A, “Aggregate mutual fund ﬂows and security returns,” Journal of ﬁnancial economics, 1995,
39 (2-3), 209–235.
Wurgler, Jeﬀrey and Ekaterina Zhuravskaya, “Does Arbitrage Flatten Demand Curves for Stocks?,” Journal
of Business, 2002, 75 (4), 583–608.
53
