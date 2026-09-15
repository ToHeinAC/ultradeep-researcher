---
title: Duration-Driven Returns
id: duration-driven-returns
tags:
- apple-earnings-durability-thesis-b8b3f1
- equity-duration
- payout-policy
- apple-capital-return
- discount-rate-sensitivity
created: '2026-09-13T06:21:14.749820Z'
updated: '2026-09-15T19:32:22.158890Z'
source: https://ebenlazarus.github.io/Duration.pdf
source_domain: ebenlazarus.github.io
fetched_at: '2026-09-13T06:21:14.749412Z'
fetch_provider: crawl4ai
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Gormsen & Lazarus, ''Duration-Driven Returns,'' Journal of Finance (2023
  forthcoming/published; author-hosted full-text PDF, 1929-2019 samples). This is
  the precursor methodology paper behind the duration-sorted-portfolio analysis used
  in the authors'' later NBER w34814 ([[interest-rates-and-equity-valuations]]).\n\nCENTRAL
  THESIS, DIRECTLY RELEVANT TO Q A.4 (whether Apple''s front-loaded cash returns make
  it short- rather than long-duration): the paper explains the premia on five major
  equity risk factors -- value, profitability, investment, LOW-RISK, and PAYOUT --
  as a single ''duration risk factor.'' The long (higher-alpha) legs of all five factors
  are firms with SHORT cash-flow duration: specifically firms characterized by high
  book-to-market, high operating profitability, LOW asset growth (low investment),
  LOW market beta, and HIGH PAYOUT RATIO. The paper''s own logic: ''firms with low
  investment and high payout ratios... invest only sparsely in future projects, [so]
  they also imply that these firms will have low growth and thus a short cash-flow
  duration. Similarly, high-profit firms have short duration because they have large
  profits today relative to the value of future profits.'' This directly implies that
  a firm with Apple''s profile -- high payout ratio via buybacks and dividends, high
  profitability -- sits on the SHORT-duration, higher-realized-alpha side of this
  framework, not the long-duration side.\n\nDIRECT EVIDENCE using single-stock dividend
  futures (dividend strips, 2010-2019 sample): CAPM alpha on individual-firm dividend
  claims decreases smoothly with the MATURITY of the claim -- starting at approximately
  8%/year for the 1-year claim and falling to approximately 4%/year for the 4-year
  claim -- and, crucially, this maturity-return relationship is ALMOST IDENTICAL across
  value and growth firms (a 3-year claim on a value firm earns about the same risk-adjusted
  return as a 3-year claim on a growth firm). This means the duration premium attaches
  to the CASH-FLOW MATURITY itself, not to a firm-level growth/value label -- supporting
  the query''s analytical point that a firm returning cash close to the present (via
  buybacks) is effectively monetizing/pricing in the near-term high-alpha segment
  of its cash-flow stream, which should carry LESS discount-rate sensitivity than
  an equivalent claim on distant cash flows, regardless of how ''growth-like'' the
  firm''s headline narrative is. Apple itself is not named or studied individually;
  findings are at the portfolio/factor level, US and international equities 1929-2019
  (dividend-growth/asset data) and 1990-2019 (broad global sample).'
raw_file: raw/duration-driven-returns.pdf
utility_score: 15.0
---

*Suggested by [[interest-rates-and-equity-valuations]] — precursor paper defining the cash-flow duration measure and duration-sorted portfolios used in the NBER w34814 analysis*

Duration-Driven Returns
NIELS JOACHIM GORMSEN and EBEN LAZARUS∗
ABSTRACT
We propose a duration-based explanation for the premia on major equity factors, in-
cluding value, profitability, investment, low-risk, and payout factors. These factors
invest in firms that earn most of their cash flows in the near future and could therefore
be driven by a premium on near-future cash flows. We test this hypothesis using a
novel data set of single-stock dividend futures, which are claims on dividends of indi-
vidual firms. Consistent with our hypothesis, the expected CAPM alpha on individual
cash flows decreases in maturity within a firm, and the alpha is not related to the
above characteristics when controlling for maturity.
Keywords: asset pricing, cross-section of stock returns, cash-flow growth, duration,
survey expectations, dividend strips.
JEL classification: G10, G12, G40.
∗Niels Joachim Gormsen is at the University of Chicago, Booth School of Business, and Eben Lazarus is
at the MIT Sloan School of Management. We are grateful for helpful comments from Francesca Bastianello,
Bruno Biais, John Campbell, Mike Chernov, John Cochrane, Will Diamond, Darrell Duffie, Eugene Fama,
Andrei Gonçalves, Stefano Giglio, Robin Greenwood, Sam Hartzmark, Ralph Koijen, Serhiy Kozak, Lars
Lochstoer, Rajnish Mehra, Tobias Moskowitz, Stefan Nagel, Lubos Pastor, Lasse Pedersen, Sophie Shive,
Larry Schmidt, Andrei Shleifer, David Thesmar, Jessica Wachter, Wei Xiong, and Dacheng Xiu, as well
as three anonymous referees, seminar participants at Chicago Booth, City University of Hong Kong, Duke
University, HEC Paris, Hong Kong University of Science and Technology, and London Business School,
and participants at the 2020 AFA conference, the 2020 ASU Sonoran Winter Finance Conference, the
2019 NBER Behavioral Finance meeting, the 2020 NBER Asset Pricing meeting, the 2020 ITAM Finance
Conference, the 2020 Utah Winter Finance Conference, the 2020 UNC Junior Finance Roundtable, and the
UK Virtual Finance Seminar Series. Vanessa Hu, Sanhitha Jugulum, and Jinyuan Zhang provided excellent
research assistance. Gormsen thanks the Fama-Miller Center for Research in Finance and the Asness Junior
Faculty Fellowship at the University of Chicago Booth School of Business for research support. We have
read the Journal of Finance disclosure policy and have no conflicts of interest to disclose.
Correspondence: Niels Joachim Gormsen, University of Chicago, Booth School of Business, 5807 South
Woodlawn Avenue, Chicago, IL 60637; e-mail: niels.gormsen@chicagobooth.edu.


---

In this paper we provide a simple framework for understanding the major equity risk factors
in asset pricing. We focus our analysis on value, profit, investment, low-risk, and payout
factors. These five categories of risk factors have a large impact on stock prices given their
high persistence, and they form the basis of leading factor models such as the Fama and
French models.1 Yet the economics behind these factors are not well understood because
the factors are hard to relate to common economic fundamentals. We relate the risk factors
back to economic fundamentals, and identify the source of their high risk-adjusted returns,
by studying the timing of the cash flows of the firms in the portfolios of the risk factors.
The analysis centers around the duration of cash flows, which is the value-weighted time
to maturity of a firm’s future cash flows.
We find that the risk factors invest in firms that have a short cash-flow duration. This
finding is illustrated in Figure 1 Panel A, which plots future cash flows for firms in the long
and short legs of each risk factor, averaged across risk factors. Each cash flow is measured
as its present value relative to the present value of all the future cash flows. As shown in
orange, the firms in the long leg have relatively large near-future cash flows and therefore
a short cash-flow duration. The opposite holds for the firms in the short leg, which are
shown in blue. The figure is based on an average of the major risk factors (its construction
is detailed in the sections below), but similar results obtain for each of the individual risk
factors considered. These risk factors thus share a fundamental economic characteristic –
the duration of their cash flows – and can accordingly be summarized by a new duration
risk factor.
The fact that the risk factors invest in short-duration stocks is key to understanding
their expected returns. Previous research on the equity term structure finds that claims on
near-future cash flows on the market portfolio have high risk-adjusted returns.2 A natural
extension of this finding is that near-future cash flows on individual firms also have high
risk-adjusted returns. Indeed, we argue that the major risk factors arise as a product of
this premium on near-future cash flows.
To understand our argument, note that the expected return on a given stock, or asset,
can be written as the value-weighted return on all of its future cash flows,
Et[rt+1] =
∞
X
m=1
wm
t Et[rm
t+1],
(1)
where rm
t+1 is the one-period excess return on the t + m cash flow and wm
t
is its ex ante
1See, for example, Fama and French (2015).
2See, for example, Binsbergen, Brandt, and Koijen (2012), Binsbergen and Koijen (2017).
1


---

Figure 1. The timing and pricing of the cash flows of the major risk factors
Panel A shows the relative present value of future dividends for firms in the long and short
legs of a duration risk factor, which is a combination of the profit, investment, low-risk,
and payout factors. All present values are calculated using a nominal discount rate of 10%.
Standard error bars (±1 SE) are computed using the delta method and the procedure
in Chen (2017, Appendix A), which accounts for serial correlation and cross-correlation
across portfolio×maturity using the Driscoll-Kraay estimator with 15 lags. Panel B shows
the Capital Asset Pricing Model (CAPM) alpha on single-stock dividend strips for firms
in the long and short legs of the risk factor. Panel C shows the CAPM alpha of corporate
bonds for firms in the long and short legs of the risk factor. The samples are 1929 to 2019
for Panel A, 2010 to 2019 for Panel B, and 2002 to 2016 for Panel C.
relative present value. Our hypothesis is that, for a given maturity, risk-adjusted returns
on cash flows are more or less the same across firms. However, the returns decrease in
maturity for all firms. Firms with higher weights on near-future cash flows therefore have
higher risk-adjusted returns.
We provide direct evidence of such a duration-based explanation using novel data. We
study a data set of single-stock dividend futures, which are claims to stock level dividends
2


---

that are paid out during a given calendar year.
These claims are often referred to as
dividend strips and can be thought of as the equity equivalent of a zero-coupon bond for
an individual firm, only with the face value being the stochastic dividend. These dividend
strips allow us to study the returns to the individual cash flows of individual firms. We
find that the risk-adjusted return decreases with the maturity of the cash flows, but they
do not vary systematically across the underlying firms — for instance, the three-year claim
on a value firm has the same risk-adjusted return as the three-year claim on a growth firm.
This finding is illustrated in Figure 1 Panel B, which shows the CAPM alpha on the cash
flows of the long and short legs of the risk factors. For both legs of the risk factors, the
alphas start at around 8% per year for the one-year claim and decrease to around 4% for
the four-year claim. Moreover, for each maturity, the risk-adjusted returns are almost the
same for both legs of the risk factors.
As this exercise shows, the single-stock dividend futures allow us to hold fixed all of
the characteristics of a given firm and vary only the maturity, or duration, of claims on
that firm’s cash flows, and conversely to hold fixed the cash-flow maturity and vary the
firm characteristics.
The dividend futures thus allow us to directly identify a relation
between duration and stock returns that cannot be explained by firm-level characteristics.
We provide further details on this strategy in Section IV. This type of identification is
unique within the cross-section of stock returns, as we usually cannot obtain model-free
identification of the role of a given characteristic.
The single-stock dividend futures trade in an established market on the Eurex exchange.
We observe around e4 billion notional outstanding by the end of our sample in 2019, which
is on the same order of magnitude as the market for the index dividend futures studied
by Binsbergen and Koijen (2017). The main players in the dividend futures market are
financial intermediaries and institutions, which are often considered important in price
determination in the cross-section (e.g. Adrian, Etula, and Muir (2014)).
We also provide a robustness analysis using corporate bonds. Like the dividend strips,
corporate bonds allow us to study the returns to claims on horizon-specific cash flows
of individual firms. The payoff on a corporate bond depends on the firm’s cash flow at
maturity, and the bond is thus approximately a claim on this cash flow, allowing for return
comparisons across horizons. The evidence provided by these comparisons is not as direct as
the evidence provided by dividend strips, given additional features of corporate bonds (e.g.,
optionality). But the bonds are available for a longer time series and longer maturities, and
they are traded in larger volumes, which makes them useful for robustness. As summarized
in Figure 1 Panel C, we again find that the CAPM alphas on cash flows are similar across
firms but decrease in maturity, consistent with a premium on near-future cash flows. We
3


---

note that while this corporate bond analysis is intended as a robustness check, the fact that
these results are consistent with those of the dividend-strips analysis suggests a promising
possible avenue for unifying the cross-section of equity and debt.
We emphasize that all of the results above relate mainly to CAPM alphas. In particular,
it is the CAPM alpha on stocks, dividend strips, and corporate bonds that decreases in
maturity. For equity claims, expected returns also decrease slightly in maturity, but the
effect is insignificant for dividend strips and only marginally significant for stocks.3 Our
organizing fact is thus that near-future cash flows have high returns relative to conventional
measures of risk, such as market beta and volatility (leading to high CAPM alphas and
high Sharpe ratios).4 As noted by Cochrane (2011, p. 1059), “All [cross-sectional] puzzles
are joint puzzles of expected returns and betas” (emphasis his). Our unifying explanation
of the cross-sectional factors we consider is accordingly an explanation of CAPM alphas.
We next address why near-future cash flows have high CAPM alphas. A natural ex-
planation is that near-future cash flows are riskier than their market betas suggest. For
example, Gormsen and Koijen (2020) show that the value of near-future dividends dropped
by as much as 40% during February and March of 2020 at the outbreak of the coronavirus
crisis, substantially more than suggested by their unconditional betas. If near-future div-
idends are highly exposed to such bad economic shocks, this may help explain why their
returns are high relative to more conventional measures of risk.5 We address this possibility
by studying the consumption risk in duration-sorted portfolios. We find that the market-
adjusted returns on short-duration firms are positively exposed to consumption risk while
the market-adjusted returns on long-duration firms are negatively exposed to consump-
tion risk. This finding suggests that consumption risk may play a role in the premium on
3The fact that CAPM alphas decrease in maturity more than expected returns is consistent with the
results on the equity term structure, for which the robust finding is that risk-adjusted returns decrease
in maturity, whereas the effect on returns is debated. Indeed, Binsbergen, Brandt, and Koijen (2012)
find a negative but insignificant relation between expected returns and maturity. Binsbergen and Koijen
(2017) also find a negative relation between maturity and expected returns but emphasize that the relation
between maturity and risk-adjusted returns is much stronger (Bansal et al. (2020)).
4Unsurprisingly, longer-duration portfolios have higher market betas. Perhaps more surprisingly, their
average returns are nearly identical to the average returns on short-duration portfolios, leading to significant
alphas on these short-duration portfolios.
5See models by Lettau and Wachter (2007) and Hasler and Marfe (2016).
4


---

near-future cash flows and thus the premium on the duration factor.6
However, the data also do not rule out the possibility of an additional behavioral driver
that is unrelated to a premium on near-future cash flows. Indeed, while we find no relation
between firm characteristics and expected CAPM alphas on the dividend strips, we do find
a relation between firm-level growth rates and realized CAPM alphas. In particular, div-
idend strips for high-growth firms (long-duration firms) have low realized CAPM alphas,
even controlling for maturity. Such a negative relation between growth rates and realized
alphas is consistent with theories of overreaction in which investors overestimate the ex-
pected growth rates on high-growth firms (La Porta (1996), Bordalo et al. (2019)). The
relation between growth rates and realized alphas is generally statistically insignificant but
it nonetheless leaves open the possibility that the duration factor is not only driven by a
premium on near-future cash flows, but behavioral overreaction plays a role as well.
Finally, at first glance, it might be surprising that the major risk factors all share
the common economic feature of investing in firms with a short cash-flow duration. We
argue, however, that this commonality is intuitive. Consider, for instance, firms with low
investment and high payout ratios, that is, firms that the long legs of the investment
and payout factors invest in. Because both of these characteristics imply that the given
firms invest only sparsely in future projects, they also imply that these firms will have low
growth and thus a short cash-flow duration. Similarly, high-profit firms have short duration
because they have large profits today relative to the value of future profits. Firms with
high valuation ratios are referred to as growth firms precisely because of the high present
value of growth opportunities implied by those ratios, and thus naturally have long cash-
flow duration in general (and conversely for firms with low valuation ratios). Finally, a low
beta is often a symptom of a short cash-flow duration. Indeed, firms with short cash-flow
duration are less exposed to the discount-rate shocks that account for much of the variation
in aggregate prices, leading them to comove less with the market and thus have low betas.7
The remainder of the paper proceeds as follows. We discuss our relation to previous
literature immediately below. Section I explains our data and methodology. Section II
6Alternative explanations of why the premium on near-future cash flows exists include risk pricing
(Eisenbach and Schmalz (2016), Lazarus (2019)), behavioral (Cassella et al. (2019)), or institutional (Belo,
Collin-Dufresne, and Goldstein (2015)) mechanisms.
7The fact that short-horizon cash flows are less exposed to discount rate shocks is a feature shared by
fixed-income securities. This commonality in part motivates our use of the term duration in describing the
timing of cash flows accruing to equity-holders, by analogy to its use for fixed-income securities.
5


---

documents that the major equity risk factors invest in short-duration firms. Section III
uses this fact to combine the major risk factors into a new duration risk factor and shows
that this factor summarizes most of the premia on major equity risk factors, it works
well in a broad global sample, and it provides a robust and meaningful contribution in
explaining the cross-section even relative to a large set of previous factors. Section IV
studies single-stock dividend futures and corporate bond returns to isolate duration as
a driver of risk-adjusted returns on the duration factor. Section V studies the economic
mechanisms behind our results on duration-driven returns. Finally, Section VI concludes.
Related Literature: Our paper relates to a literature on duration and the cross-section of
stock returns. Dechow, Sloan, and Soliman (2004) study a measure of cash-flow duration
in the cross-section of U.S. stock returns. Lettau and Wachter (2007) provide a model
in which the value premium is explained by the short cash-flow duration of value firms.
More recently, Weber (2018) shows that the relation between duration and stock returns
is stronger when sentiment is higher, and Chen and Li (2018) and Gonçalves (2020) argue
for a duration-based explanation of the profitability and investment premia. We provide a
series of contributions to this literature as explained below.
First, we directly link five major characteristics to duration by studying their relation to
cash flow growth, highlighting that these characteristics are similar along a key dimension.8
This similarity is sufficiently pronounced that the characteristics can be combined into, and
in large part explained by, a single duration factor.9 We provide evidence that this risk
factor price long-run returns well, that it is priced in a broad global sample, and that it
can be at least partly explained by exposure to consumption risk.
Second, and crucially, we provide identification of the role of duration. Previous studies
have documented a correlation between duration and returns, but there is no evidence
8Previous research by Chen (2017) has studied the growth rates of the firms in the value factor. Chen
finds that value firms grow faster, not slower, than growth firms, which challenges the duration-based
explanation for the value premium. However, this result only holds in the early US sample and we show
that it is driven by microcap firms. When excluding the smallest 20% of listed firms, the cash flows of value
firms indeed grow slower than those of growth firms, both in the full sample and in the modern sample
that we consider. See Section II.C for detail.
9The finding helps explain why the different risk factors often subsume each other in factor regressions,
a finding that has caused debate in the asset pricing literature (Asness et al. (2020), Bali et al. (2017),
(Fama and French (2016), Liu, Stambaugh, and Yuan (2018)).
6


---

that duration actually influences returns. That is, it is unclear whether short-duration
firms have high alpha because of the cash-flow duration or because of other characteristics
associated with short-duration firms, such as low valuation ratios. Unlike other papers in
prior literature, we directly identify an effect of duration using dividend strips, as discussed
in detail in Section IV. This point is important not only for the literature on duration but
also for the literature on the cross-section more generally: to our knowledge, no prior study
has been able to obtain model-free identification of a proposed risk factor.
More generally, the dividend strips allow us to study the returns on individual cash
flows. Hansen, Heaton, and Li (2008) emphasize the importance of studying individual
cash flows separately, but the lack of data has challenged this approach. The dividend
strips fill this gap, allowing for more careful analysis of asset pricing dynamics. Almost
any model of the cross-section is going to make predictions about prices of individual cash
flows of individual firms; going forward, such predictions can now be tested and disciplined
by data.
We also contribute to the literature on the aggregate equity term structure. Binsbergen
and Koijen (2017) document that the risk-adjusted returns on claims to all dividends on the
market portfolio decrease in maturity.10 However, this result could be driven by how the
composition of the market portfolio varies over the term structure. We extend the evidence
and show that risk-adjusted returns also decrease in maturity for single-stock dividends,
which implies that the results on aggregate dividends are not driven entirely by composition
effects. More generally, our paper contributes to the role of duration in understanding stock
prices (Binsbergen (2020)).
Our paper also relates to a recent literature on the so-called factor zoo.11 The goal
of this literature is to determine which characteristics are most important for predicting
returns. The literature achieves this goal mainly through statistical analysis. We differ
in our approach and shrink the cross-section based on economic intuition.12 We use basic
10Miller (2020), Chen (2020), and Giglio, Kelly, and Kozak (2020) study the slope of the equity term
structure in the cross-section of stock returns using different methods. In addition to the literature review
in Binsbergen and Koijen (2017), see also Andrews and Gonçalves (2020), Cejnek and Randl (2020), and
Gormsen (2021) for evidence on aggregate term structures.
11See, for instance, Feng, Giglio, and Xiu (2020), Giglio, Liao, and Xiu (2020), Harvey and Liu (2017),
Harvey, Liu, and Zhu (2016), and Kozak, Nagel, and Santosh (2020).
12We do, however, use the Feng, Giglio, and Xiu (2020) test to assess the contribution of our duration
factor relative to previous factors, and it performs well in this test; see Section IV of the Internet Appendix,
7


---

economic arguments, together with analysis of dividend growth rates and novel dividend
futures data, to argue that a range of the most prominent characteristics are symptoms of
short-duration cash flows, and that many cross-sectional anomalies can thus be explained
by a duration characteristic, which in turn is consistent with the evidence on the equity
term structure of the market portfolio.
I.
Data and Methodology
A.
Equities
We study equities in a global sample covering 67,842 stocks in 23 countries between
August 1926 and December 2019. The 23 markets in our sample correspond to the countries
belonging to the MSCI World Developed Index as of December 31, 2019. Stock returns are
from the union of the CRSP tape and the XpressFeed Global Database. All returns are in
USD and do not include any currency hedging. All excess returns are measured as excess
returns above the U.S. Treasury bill rate. Data needed to construct investment, profit, and
payout characteristics are available from 1952.
We study risk factors both in the individual countries in our sample and in a broad
global sample. Our broad sample of global equities contains all available common stocks
in the union of the CRSP tape and the XpressFeed Global database from 1990 until 2019.
B.
Single-Stock Dividend Futures
We obtain daily prices on single-stock dividend future from Deutsche Borse, which is
the owner of the Eurex Exchange on which the futures trade. The sample runs from 2010
to 2019 and contains 190 different firms. We match the underlying firms of the dividend
futures to our equity database using the International Securities Identification Number
(ISIN). We explain the nature of the data and data handling in detail in section IV and
Appendix B.
C.
Bond Returns
We obtain bond returns from the Wharton Research Data Services (WRDS) Bond
Return database. Our sample includes 23,211 bonds issued by 1,352 U.S. firms and runs
from July 2002 to January 2016.
available in the online version of this article on The Journal of Finance website.
8


---

D.
Expectations
We obtain long-term growth (LTG) expectations from the Insitutional Bankers’ Esti-
mate Systemm (IBES) database, for which data are available from 1981 to 2019. These
expectations are defined as annualized expected earnings growth rates over a company’s
“next full business cycle.”
In some analyses we convert these values into cross-sectional
percentiles, while in other analyses we work with the annualized numerical earnings growth
values directly. In all cases we use median estimates for expected dividends.
E.
Defining Cash-Flow Duration
Macaulay (1938) defines cash-flow duration as the weighted-average years to maturity
of an asset’s expected cash flows,
Durt =
∞
X
m=1
i × ωm
t .
(2)
The weight ωm
t is the present value of the given cash flow relative to the total value of the
assets,
ωm
t = Et[CFt+m]/(1 + r)m
Pt
,
(3)
where CFt+m is the realized cash flow in period t + m, r is the yield to maturity on the
asset, and Pt is the price of the asset. The weights ωm
t are slightly different than the weights
in equation (1); the weights ωm
t
are based on present values that are calculated using the
yield on the equity, whereas the weights wm
t in (1) are based on the prices of the individual
cash flows (i.e., using cash-flow-specific discount rates).
As can be seen in equation (3), cross-sectional variation in duration comes from differ-
ences in expected growth and discount rates. The higher the growth rate and the lower
the discount rate, the larger the weight on the distant future cash flows and the longer the
duration.
As discount rates are ultimately the variable we seek to explain, we focus most of our
analysis on variation in duration that comes from variation in growth rates. Indeed, the
analysis in Section II focuses on understanding the timing, or growth rate, of cash flows.
Similarly, the duration characteristic that we introduce in Section III is in fact a growth
rate characteristic. In the analysis of dividend strips in Section IV, the timing and duration
of cash flows is conveniently the same as the strips only have one payment.
9


---

II.
The Timing of Cash Flows for the Major Risk
Factors
We first document that the major risk factors invest in firms with low growth rates.
Because these firms have low growth rates, their near-future cash flows ceteris paribus are
large relative to their distant-future cash flows.13
We focus our analysis on value, profitability, investment, low-risk, and payout factors.14
We consider commonly used versions of these risk factors, which are based on the follow-
ing characteristics: high book-to-market, high operating profitability to book equity, low
annual growth in total assets, low market beta, and high payout ratio. Precise definitions
of the characteristics can be found in Appendix A. Throughout the paper, we sign all char-
acteristics such that a higher characteristic value implies a higher CAPM alpha. We start
this section with an analysis of realized growth rates. We then move on to expected growth
rates.
A.
Realized Growth Rates
We first look at the relation between characteristics and realized growth rates. To do so,
we create 50 characteristics-sorted portfolios, 10 for each characteristic. For each portfolio
i and year t, we calculate growth rates in dividends and earnings from year t to t + 15 and
regress them on the vector of time-t characteristics Xi,t:
Growth ratei,t,t+15 = β0 + X′
i,tB + ϵi,t.
(4)
The methodology for calculating growth rates is provided in Appendix A. For this exercise,
all characteristics are measured as percentiles of the firm-level cross-sectional distribution
in t and then aggregated to the portfolio level, and we include time fixed effects in the
13As discussed at the end of Section I, we abstract here from the effect of discount rates on duration.
But as we will argue below, firms with high growth rates in fact also have lower discount rates, which
reinforces the positive effect of growth rates on duration.
14We consider these risk factors given their prominence in the post–Fama and French (1993) literature,
and the fact that their persistence suggests that they are quantitatively important for explaining valuation
ratios in addition to expected returns (in contrast to, for example, momentum). But any such selection
is of course subjective, so we consider the applicability of our framework for other anomalies in Internet
Appendix D and E.
10


---

regression.
We consider the 1963 to 2019 sample and to align with Fama and French
(1993) time t is the end of July of the given year.
Panel A of Table I reports the results of regression (4). The first row uses ex post
dividend growth rates on the left-hand side. These growth rates load negatively on all
the characteristics, though the effect is insignificant for investment. The next row uses
ex-post earnings growth rates on the left-hand side. The results are similar, with beta now
insignificant and with the loading on investment now positive but still insignificant. Given
the noise in earnings, the R2 in the earnings-growth regression is much lower than that of
the dividend-growth regression in the first row (0.05 versus 0.38). These results provide
suggestive evidence that the characteristics are associated multivariately with low growth
rates, with the more predictable dividend growth rates yielding somewhat stronger results.
In both cases, however, the results in Panel A may be biased upward: these char-
acteristics may predict returns in part because the firms in high-return portfolios have
overperformed in-sample, generating higher cash-flow growth than expected. If this were
the case, the actual relation between characteristics and expected growth rates would be
more strongly negative than presented here. In addition and perhaps more importantly,
these results are only at the portfolio level, which limits statistical power.15 We thus move
next to a firm-level analysis using ex ante expectations data.
B.
Expected Growth Rates
To get more precise results and increase statistical power, we next consider the contem-
poraneous relation between characteristics and ex ante expected growth rates from IBES.
These expectations are known to embed their own biases, as we discuss below. For now,
however, we are interested only in the rankings of expected growth rates, as we consider
cross-sectional percentile values for this estimation.
As documented further below, the
IBES-based expectations do correctly rank firms’ growth rates on average.
Panel B of Table I documents the univariate correlation between the expected growth
rate and the contemporaneous characteristics of the same firm. The long-term expected
growth rate is negatively correlated with all the characteristics, in line with the analysis in
Panel A.
To go beyond univariate correlations, we run a panel regression of expected growth rates
15A firm-level analysis with realized growth rates would be subject to survivorship bias issues, particu-
larly at such a long horizon. The analysis above is thus intended as a first-pass summary.
11


---

on contemporaneous characteristics,
LTGj,t = Γj + X′
j,tB + ϵj,t,
(5)
where LTGj,t is the median expected long-term growth of firm j at time t, and Xj,t is a vector
containing the firm-j characteristics at time t, again both transformed into cross-sectional
percentiles. The firm fixed effects Γj are included only in a subset of the regressions.16
Our baseline analysis uses the number of analysts by firm as regression weights, though we
consider alternative specifications as well.
Panel C of Table I shows the U.S. results.
The LTG expectations load negatively
on all the characteristics. In our baseline results (columns (1) to (3)), we exclude firm
fixed effects, meaning right-hand-side variation is driven by both permanent and transitory
differences in characteristics. With firm-level fixed effects (columns (4) to (6)), the results
are again highly significant and negative but quantitatively smaller in magnitude. The
result holds across sample splits and using different regression weights. The R2 is high
in all specifications. Thus, the characteristics all predict low expected growth rates, even
multivariately, and they jointly explain expected growth rates well.
We obtain similar results in our international (non-U.S.) sample, as shown in Panel D
of Table I. In our baseline regressions, weighted by the number of analysts, the expected
growth rates again load negatively on all of the characteristics. The results are robust to
using market-cap weights, but they are not entirely robust to removing weights or splitting
the sample in the international case.
Panel A of Figure 2 shows the estimated loadings of expected growth rates on charac-
teristics for each individual country in our sample.17 The clear majority, more than 85%,
of the parameter estimates are negative. Panel B zooms in on the G7 countries. Again,
almost all estimates are negative, with the exception of the investment characteristic, which
is slightly positive in a few countries.
16Given the use of cross-sectional percentile values for all variables, the estimation implicitly incorporates
date fixed effects as well.
17See Figure A1 of the Internet Appendix for the same results split out by individual characteristics,
which shows more clearly which characteristics have varying loadings across countries.
12


---

C.
Comments and Relation to Previous Research
The long-term growth rates are ideal because we directly link firm characteristics to ex
ante expectations. By doing so, we avoid drawing our inference based on ex post realized
growth, which would be biased to the extent that the characteristics are products (at
least in part) of data mining. On the one hand, the IBES expectations might themselves
be biased and not reflect true consensus earnings-growth expectations. There is indeed
evidence — see, for example, Chan, Karceski, and Lakonishok (2003) – that the long-term
growth rates suffer from overreaction. However, as documented in the next section, these
expectations are not pure noise. Firms with high expected long-term growth do have higher
realized ex post growth rates than firms with low long-term growth expectations.18 This
latter property is sufficient for our purposes in this section, as we measure expectations
in cross-sectional percentiles and focus on qualitative relations between growth rates and
characteristics.
The results on the book-to-market ratio may seem counter to the findings of Chen
(2017), who studies realized growth rates of value and growth firms. Chen (2017) finds
that value firms have lower growth rates than growth firms in his modern sample period
(post-1963), but higher growth rates in the early sample (1926 to 1962) and in the full
sample. Two points of relation between Chen’s results and ours merit comment. First, in
this analysis we also study the modern sample period (post-1952, or post-1981 when IBES
data is needed), and our results are thus consistent within this period. Second, and more
importantly, the results in the early sample are driven by micro-cap firms. Once we discard
the smallest 20% of listed firms, value firms have lower growth rates in the full sample as
well, as documented in Internet Appendix Table IA.I.19,20
In conclusion, the major risk factors share a common feature, namely, their long legs
18The earlier literature also contested the claim that these expectations had any predictive power for
realized growth. We do not find support for this finding in the updated data, but we do find evidence that
the expectations tend to be upwardly biased on average, consistent with Chan, Karceski, and Lakonishok
(2003).
19Micro-cap firms have a strong effect on the results given that Chen (2017) forms portfolios by sorting
univariately on book-to-market. This ratio is known to be highly correlated with firm size, implying that
some of the portfolios contain a relatively large number of micro-cap firms.
20Chen (2017) also studies growth rates of “rebalanced” portfolios, which are the usual portfolios studied
for purposes of forward-looking expected return predictions. (The label “rebalanced” as used here in fact
refers to portfolios that are both rebalanced and refreshed every calendar year.)
But these portfolios
13


---

invest in firms with low growth rates relative to their short legs. In the following sections,
we address the asset pricing implications of this new stylized fact.
III.
Factor Regressions
The previous section emphasizes that the firms in the major risk factors are similar
along a key economic characteristic, namely, the timing, or growth rate, of their cash flows.
In this section, we combine the major risk factors into a single low-growth factor to study
the similarity of the risk factors in return space. We find that the premia on the major risk
factors to a large extent can be summarized by this combined factor.
A.
Factor Characteristic
To explore the similarity of the major risk factors, we first combine the characteristics
underlying the major risk factors into a single low-growth characteristic. Since the major
characteristics are all associated with a low growth rate, one approach would be to equal-
weight the characteristics into a single low-growth characteristic, something we explore
in the Internet Appendix.
In the main specification, however, we instead exploit that
some characteristics appear more strongly related to the growth rates than others.
In
particular, we construct the combined characteristic as the weighted average of the profit,
investment, beta, and payout characteristics, where the weights are given by the factor
loadings in regression (5) of Table I, Panel C. We exclude book-to-market from our combined
characteristic because sorting on book-to-market ratios involves sorting on prices, which is
ultimately the variable we seek to explain.21
Given this construction, the low-growth characteristic measures the expected growth
rate of the firm, conditional on the firm’s book-to-market ratio.22 Empirically, the charac-
provide little evidence on firm-level growth rates, as discussed on p. 2281 of Chen (2017). Instead, they
largely reflect the relative performance of value and growth firms, as shown in Section IV of Chen (2017).
21In the Internet Appendix, we provide robustness analysis on two alternative methods for computing
this characteristic. The first, as above, uses the equal-weighted average of the characteristics instead of the
weighted average; the second includes the book-to-market characteristic as well. Our main results in this
section are unchanged when using the equal-weighted average and differ only slightly when also including
the book-to-market characteristic (see Table IA.IX).
22For two firms with the same book-to-market ratio, the characteristic captures the difference in expected
growth.
Empirically, the characteristic is close to uncorrelated with book-to-market ratios, so sorting
14


---

teristic is associated with both a low growth rate and a high expected return, as documented
below. Both of these contribute to a shorter cash-flow duration (see Section I.E), and we
therefore refer to the combined characteristic as a duration characteristic, but we emphasize
again that the characteristic omits variation in duration coming from the book-to-market
ratio.
B.
Properties of the Duration Portfolios and Factor
Table II studies returns on ten portfolios sorted on our duration characteristic, from
short to long duration. The portfolio breakpoints are based on NYSE firms and refreshed
every year. The portfolios are value-weighted and rebalanced each calendar month. As
can be seen in the first row, the average monthly excess returns decrease slightly as dura-
tion increases, but the effect is nonmonotonic and statistically insignificant. However, the
CAPM alpha decreases almost monotonically as the duration increases. This effect is both
economically and statistically significant as the long-short portfolio has an alpha of -0.79%
per month, with a t-statistic of -4.94. As discussed in the introduction, our unifying ex-
planation of the cross-sectional factors we consider is accordingly an explanation of CAPM
alphas.
The last row of Table II also reports the realized and expected cash-flow growth rates
of the portfolios. The expected cash-flow growth rate is based on the long-term growth
expectations in the subsample for which we have expectations data. Expected cash-flow
growth, as measured by the long-term growth rates from IBES, increases monotonically
as portfolio duration increases. More importantly, the realized growth rates also increase
monotonically. The realized growth rates are for the full sample, so they do not directly
compare to the expected growth rates from the 1981 to 2019 sample. This issue aside,
it does appear that the expected growth rates are biased upward relative to the realized
growth rates, though this bias does not affect the ranking of portfolios’ cash-flow growth
rates ex post relative to ex ante. To put the growth rates in perspective, we calculate
realized duration under the assumption that the realized growth rates continue forever and
that the discount rate is equal to the realized average market return for all stocks. As shown
at the bottom of Table II, the realized duration varies from 15 years for the short-duration
portfolios to 59 years for the long-duration portfolio, suggesting that the differences in
growth rates lead to sizable differences in cash-flow duration.
portfolios on this characteristic is conceptually similar to considering double-sorted portfolios that are
sorted first on book-to-market and then on expected growth rates.
15


---

Table III analyzes returns on our duration factor, which is constructed using the Fama
and French (1993) method.23 The factor goes long the short-duration firms and short long-
duration firms. The U.S. results in Panel A are largely similar to the results in Table II:
the factor has only marginally significant expected returns but a highly significant CAPM
alpha of 0.50% per month (t-statistic of 5.64). The large alpha is driven neither by the
small cap firms nor by the short leg of the portfolio alone. The result is robust across
subperiods, as can be seen in Figure 3, which plots the cumulative alpha and return.
The two last rows of Table III, Panel A show the expected and realized dividend growth
rates of the different portfolios in our duration factor. Both of the long-duration portfolios
have realized and expected growth rates above those in the short-duration portfolios. The
realized growth rates are from the full sample whereas the expected growth rates are from
the 1981 to 2019 sample. Figure 4 further shows the cumulative dividend growth for the
short- and long-duration portfolios as a function of time after the portfolio formation period.
As can be seen in the figure, the long-duration firms have higher growth rates than the
short-duration firms in every year after the formation period. After 15 years, the earnings
of the long-duration portfolio have increased by almost 100 percentage points more than
the short-duration portfolio. These results verify that our measure of ex ante duration does
indeed predict ex post differences in growth rates (and thus duration).
Panel B of Table III reports the performance of the duration factor in the global sample.
The factor has a positive and statistically significant CAPM alpha of 0.44% per month.
Similarly, Figure 5 shows that the factor has positive alpha in 20 out of 23 countries in
our sample, and that it is statistically significant in the majority of them as well, despite
the sample being quite short in many exchanges. Given that the characteristics and load-
ings that underlie our duration factor are all based on our analysis in the U.S. data, this
international evidence mitigates data-mining concerns.
23Each June, we sort stocks into six portfolios using breakpoints based on the median market capital-
ization and the 30th and 70th percentiles of the duration characteristic. In the U.S., portfolio breakpoints
are unconditional and based on NYSE firms. In the international sample, breakpoints are conditional
and based on the largest 20% of firms. (We follow standard practice in using conditional breakpoints for
the international data given small-sample issues; see, for example, Asness, Frazzini, and Pedersen (2019).)
Portfolios are value-weighted and rebalanced at the end of each calendar month.
16


---

C.
Spanning Regressions
We use three-factor regressions to study the extent to which our duration factor summa-
rizes the five major equity risk factors studied in Section II. For each factor, we regress the
returns on the market, a small-minus-big portfolio, and the duration factor in the following
regression:
ri
t+1 = αi
DUR + βi
Mkt(rMkt
t+1 −rf
t ) + βi
smbrSmb
t+1 + βi
DurrDur
t+1 + ϵt+1,
(6)
where ri
t+1 is the excess return on risk factor i. The small-minus-big factor is based on the
six portfolios sorted on duration and size that are used to construct the duration factor.
The size factor goes long the small firms and short the large firms. Including the size
factor does not influence our results much, as our left-hand-side variables are size-neutral
by construction. However, without the size factor, the model struggles to explain portfolios
that are not size-neutral. On average, small stocks have higher growth rates than large
stocks, which means they are long-duration stocks.
As such, based on duration alone,
one would expect them to have low returns, but empirically the small firms have high
returns.
This size premium could potentially arise from liquidity effects or from other
market microstructure issues related to small firms. But regardless of the origin of this
premium, it illustrates that our duration factor of course does not (along with the market)
explain the entirety of the cross-section.
Panel A of Table IV presents results of our factor regressions in the U.S.. The first
three columns report the results from the CAPM regressions using the market alone. The
risk factors all have positive and statistically significant CAPM alphas. In addition, they
all have negative CAPM betas.
We next consider the three-factor regressions in the middle columns. The major risk
factors all load positively on our duration factor in these regressions. The loadings are
statistically significant. The remaining alphas for the factors are all insignificant in the
three-factor model.24 Panel B reports similar results in the global sample: the major risk
factors all load on our duration factor, and the remaining alpha is insignificant, except for
24While the table reports results from the three-factor model including a small-minus-big factor, the
duration factor in fact provides the bulk of the explanatory power and reduction in alpha. The average R2
in analogous two-factor regressions, including only the market and the duration factor, is 0.48 (compared
to 0.52 in the three-factor results in the table); similarly, the average alpha in these two-factor regressions
is 0.07% per month (compared to 0.02% per month in the three-factor case).
17


---

the profit factor.
We provide additional analysis in the Internet Appendix.
Table A2 finds that the
duration factor generally has positive alpha in the five-factor model of Fama and French
(2015). Internet Appendix D then shows, using the “factor zoo” test developed by Feng,
Giglio, and Xiu (2020), that our risk factor provides a significant contribution in pricing
the cross-section relative to a high-dimensional set of existing factors.
D.
Multi-Horizon Returns Test
We next test the duration factor’s ability to price returns at multiple horizons using the
multi-horizon returns (MHR) misspecification test proposed by Chernov, Lochstoer, and
Lundeby (CLL, 2022). CLL construct a moment condition for use in a generalized method
of moments (GMM) overidentification test based on the fact that a correctly specified
model must price not only one-period returns but also cumulated multi-horizon returns.
They test a given model’s ability to price its own factors’ returns at multiple horizons,
which “allows for testing most, if not all, aspects of conditional model misspecification”
(p. 1311). In order to compare models on common ground, they also consider a common
set of test assets, namely, the multi-horizon returns for the Fama and French (2015) five
(FF5) factors. We consider both versions of the MHR test in Table V.25
The first entry in the first row of Table V shows that the GMM J-statistic for our
three-factor model has a p-value of roughly 0.06 when tested to match its own factors’
returns at multiple horizons (1, 3, 6, 12, 24, and 48 months, as in CLL). It is thus not
rejected at the 5% level, though it would be rejected at the 10% level. This performance
is nonetheless on par with or stronger than all leading recent factor models considered by
CLL, including the Carhart (1997) four-factor model (p = 0.07), a Mkt + BAB model
(p = 0.06), the Hou, Xue, and Zhang (2015) q-factor model (p = 0.02), and the FF5 model
(p = 0.02); see their Table I.26 Our model’s outperformance in capturing conditional factor
dynamics, and thus in pricing multi-horizon returns, is even more strongly apparent in the
second column: its p-value when tested against the multi-horizon FF5 returns is roughly
0.62, whereas all leading models they consider — including FF5 itself — are rejected at
the 5% level in this test conducted on common ground (p = 0.00 for the Carhart model,
p = 0.00 for Mkt+BAB and for the CAPM, p = 0.04 for the q-factor model, and p = 0.02
25We thank the authors for helpful discussions.
26The only model they consider that is not rejected at the 10% level is the CAPM (p = 0.191), as the
market appears to capture its own conditional dynamics reasonably well.
18


---

for FF5, as in their Table A5).27 The three-factor model thus performs relatively well in
explaining returns at longer horizons. As discussed by CLL, this ability to price MHR
suggests that the duration factor model provides a parsimonious but accurate summary of
conditional factor dynamics for the major risk factors.28
E.
Summary
Sections II and III show that the major equity risk factors invest in short-duration
stocks and can largely be summarized by a duration factor that invests in firms with short
cash-flow duration. However, it is unclear whether the premium on the duration factor
arises as a product of the short cash-flow duration of the firms in the factor or if it arises
from other characteristics associated with these firms.
In the next section, we address
this issue by leveraging a novel data set of single-stock dividend futures that allows us to
identify the effect of cash-flow duration on expected returns.
IV.
Identification from Dividend Strips
In this section, we identify the effect of cash-flow duration on stock returns using a
novel data set of single-stock dividend futures. The starting point for this analysis is the
following identity from the law of one price that links the CAPM alphas on individual firms
to CAPM alphas on individual cash flows:
αi
t =
∞
X
m=1
wi,m
t
αi,m
t
,
(7)
where αi
t is the CAPM alpha on firm i, αi,m
t
is the CAPM alpha on the t + m cash flow of
firm i, and wi,m
t
is the cash flow’s relative present value.
27The remaining rows of Table V, compared against the results provided in CLL (2022), show that
our model also performs well on mean absolute pricing errors and on the maximal information ratio for
multi-horizon returns, with a maximal Sharpe ratio that is comparable to those of other leading models.
28A nonrejection in the MHR test requires that the ratio of the expected factor return to its second
moment is roughly constant over horizons. One possible explanation for these results, therefore, is that by
combining many characteristics into one, our factor essentially extracts the more stable component of the
premia associated with these factors, thereby allowing it to price long-horizon returns more robustly.
19


---

Equation (7) shows that firm-level differences in CAPM alphas can arise from two
sources: alphas on individual cash flows may vary with the maturity of the cash flows
(m) for a given firm, they may vary across firms (i) for all maturities (or both).
Our
hypothesis is that CAPM alphas decrease with the maturity m of the cash flows. Such
a pattern would generate relatively high CAPM alphas for short-duration firms because
they have relatively large weights on near-future cash flows. Under this hypothesis, we say
that the timing of cash flows affects firm-level alphas: the decomposition in (7) implies
that changing the weights on the individual cash flows, while holding fixed the alphas on
individual cash flows, would lead to a change in the firm-level alpha whenever cash-flow-
level alphas decrease in maturity.29
The alternative hypothesis is that CAPM alphas on individual cash flows do not vary
with maturity but instead vary across firms. For instance, the characteristics underlying our
duration sorts could proxy for firm-level differences in riskiness that cause CAPM alphas
on all individual cash flows to vary across firms. In this case, cash-flow duration might be
correlated with firm-level CAPM alpha, but changing the weight on the individual cash
flows, holding fixed the individual alphas, would not affect firm-level alpha.
We can thus identify the effect of cash-flow duration on firm-level alpha by studying the
CAPM alphas on individual cash flows for individual firms. To do so, we turn to a novel
data set on single-stock dividend futures. We first describe the data. We then describe our
estimation strategy. Finally, we present and discuss our empirical results.
A.
An Introduction to Single-Stock Dividend Futures
Single-stock dividend futures are claims to individual dividends on individual firms.
For instance, the future on the 2021 dividend for Nestlé gives the buyer the right to the
dividends paid by Nestlé during the 2021 calendar year. As such, these assets allow us to
29Holding fixed the alphas on the individual cash flows amounts to holding fixed the riskiness of the
individual cash flows. One could imagine, for example, a change to the expected growth rate of a firm’s
cash flows while keeping their riskiness (i.e., stochastic discount factor covariances) constant. By contrast,
counterfactuals in which one changes cash-flow timing while also changing the riskiness of the individual
cash flows would not necessarily change firm-level alphas. Consider, for example, a case in which a firm
starts allowing customers to make delayed payments (with interest), with all accounts settled and dividends
paid out only in even years. This affects cash-flow weights and thus duration, but the riskiness of the
individual cash flows would also change, and our hypothesis would not in general predict a change in alpha
from such an accounting-induced change in duration. We thank a referee for suggesting this example.
20


---

study the prices and returns on individual dividends for individual firms.
The single-stock dividend futures have traded as dividend swaps in an over-the-counter
market since the early 2000s (Manley and Mueller-Glissmann (2008)). Starting in 2010,
single-stock dividend futures have traded as a standardized product on the Eurex Exchange.
Eurex initially offered dividend futures on 50 firms but as of 2020 offers futures on more
than 200 firms. The availability of maturities varies across firms, with the most liquid firms
having maturities as far as 7 years.
The single-stock dividend futures are similar in nature to the index dividend futures
that have become commonly used in asset pricing.30 The index dividend futures are claims
to the dividends on an underlying index, such as the S&P 500 or Euro Stoxx 50. The
market for single-stock dividend strips is roughly of the same order of magnitude as the
market for Euro Stoxx 50 dividend strips, which also trade on the Eurex Exchange.31
Despite being an exchange traded product, the market for single-stock dividend strips
continues to exhibit some of the features of over-the-counter markets. Indeed, most of
trading in the single-stock futures market are over-the-counter trades that are subsequently
brought onto the order book through the Eurex OTC trading facilities for risk-clearing
purposes. As such, prices can be stale, as discussed shortly, and bid-ask quotes from the
order book are unlikely to be a good measure of actual prices. Throughout the analysis,
we keep these features of the market in mind.
As explained in Section I.B, we obtain daily data from Eurex through Deutsche Borse.
The data reflect volume from the OTC trading facilities as well as the usual on-the-book
trades. We observe daily volume, open interest, and settlement prices. The settlement
prices are the end-of-day prices that positions are cleared against in the risk management
systems. The prices are based either on traded prices or on a combination of quotes and
proprietary models. To ensure that our prices are based on traded prices, we keep track of
prices in calendar time and only update prices on days when we see volume in the market.
To give a sense of the data, Figure VI plots the price, open interest, and daily volume
for the futures on the 2020 dividends of AXA and Deutsche Bank. The AXA futures are
some of the most liquid in our sample whereas Deutsche Bank are some of the least liquid.
As shown in the left part of the figure, the AXA futures trade fairly frequently and do
30See Binsbergen et al. (2013) for an introduction to index dividend futures.
31Euro Stoxx 50 dividend futures had a notional outstanding of around e12 billion as of mid-2018
(Gormsen and Koijen, 2020). By comparison, we observe a total notional in the single-stock market of
around e4 billion at this point. Both markets have around 20,000 contracts traded daily, although the
single-stock dividend futures generally trade at 1/10 the price of the index dividends.
21


---

not exhibit any dramatic swings over the sample. We also note that there is no sign of
a bid-ask bounce.32 The open interest increases over time, reflecting the growing nature
of the market. As shown in the right side of the figure, the Deutsche Bank futures trade
more rarely, with trades sometimes being several months apart. This makes the claim on
Deutsche Bank ill-suited for high-frequency analysis like event studies, but the stale prices
are less of an issue when considering annual returns, as we do in the subsequent sections.
We will nonetheless keep the issue of stale prices in the illiquid contracts in mind through
the rest of the analysis and ensure that results are not driven by the pricing of the least
liquid strips.
B.
Summary Statistics and Representativeness
Table VI shows summary statistics for the dividend futures. Panel A reports statistics
on annual returns, volume, open interest, and notional outstanding. We calculate annual
returns at the end of December each year (as the contracts mature at the end of December)
as explained in Appendix B (Section B.C). The average raw returns are around 5%, and
average log returns are around 3.4%. These are futures returns, which means they are in
excess of the risk-free rate. The average annual volume is 11,864 contracts and the average
open interest is 5,444 contracts. A contract is a claim to the dividends paid out on 1,000
shares and trades on average at around e2,000. The average notional outstanding is around
e4 million. The total value of all the notional outstanding is around e4 billion at the end
of the sample.
Panel B presents summary statistics as they relate to maturity and CAPM betas. The
average maturity is 2 years. The average CAPM beta for an individual strip is 0.51. We
estimate CAPM betas in regressions of monthly returns on the monthly returns of the
market portfolio in the country of incorporation of the underlying firm, accounting for
stale prices; see Appendix B (Section B.D) for details. We trim the betas to be between -1
and 1.5.33
Panel C addresses the representativeness of the sample. The panel reports the aver-
age characteristics of the firms underlying the strips. We measure the characteristics in
cross-sectional percent of the characteristics on the full universe of firms in the country in
which the firm is traded, meaning that the degree of nonrepresentativeness can be roughly
32In tests using all strips, we find no significant evidence that returns on the strips are autocorrelated.
33For robustness, Tables IA.X–IA.XII show results using betas that are instead winsorized by maturity
at the 5% level.
22


---

measured using the difference of the average value of each characteristic from 50. Although
the sample contains firms with cash-flow duration below average, the sample is generally
fairly representative. The main dimension along which it is not representative is market
size, as the sample generally contains only the largest firms in the universe of firms.
Finally, Figure A2 in the Internet Appendix shows a histogram of monthly returns.
The figures excludes all observations in which returns are equal to zero. Returns look fairly
symmetric but have negative skewness and exhibit excess kurtosis.
C.
Expected Returns and CAPM Alphas
We begin our analysis of the dividend strips by analyzing the expected returns and
alphas. For this purpose, we use expected dividends from IBES to estimate the expected
yield-to-maturity on a given claim. That is, we calculate expected returns and alphas as:
Et[ri,m
t+m] =
 
Et

Di
t+m

f i,m
t
!1/m
−1,
(8)
where Di
t+m is analysts’ time-t expectations of the dividends paid out on firm i at time
t + m and f i,m
t
is the price of the m-maturity strip on firm i at time t. See Appendix B
(Section B.C) for details. We note that a cleaner way to map the results on the dividend
futures to the cross-section of stock returns would be to look at expected one-period returns
instead of the expected yield-to-maturity. When looking at expectations, the data does not
allow us to study one-period returns as we do not observe next-period expected prices.
However, in the next section we study realized returns, which do allow us to study one-
period returns.
We further calculate expected CAPM alphas by subtracting the product of the CAPM
beta and the expected market risk premium from the expected returns, assuming a market
risk premium of 5%:
αi,m
t
= Et[ri,m
t+m] −βi,m
maturity × 5%,
(9)
where βi,m
maturity is the beta-to-maturity. The estimation of the strip-level betas is outlined
in Appendix B (Section B.D).
As a first look at the data, Table VII reports the average CAPM alphas for dividend
strips on long- and short-maturity firms. The first row shows the average CAPM alphas
of the strips on the short-duration firms. The alpha starts at 8% per year for the one-year
claim and decreases steadily to around 4% for the four-year claim. The row below shows
23


---

the alphas of the strips on the long-duration firms. Here, the alpha starts at around 9%
for the one-year claim and decreases to around 3.5% for the four-year claim. The alphas
are thus decreasing in the maturity of cash flows even when keeping the underlying firms
constant. In addition, the alphas on the cash flows do not appear higher for short-duration
firms than for long-duration firms.
The analysis in Table VII is a powerful way of separating between our duration-driven
hypothesis and other potential drivers of the premium on short-duration firms. Indeed,
when going from left to right in Table XII, we are keeping all of the firm-level characteristics
fixed and varying only the maturity, or duration, of the cash flows. Similarly, when going
from top to bottom, we are varying all of the firm-level characteristics but keeping the
duration of the cash flows constant. This analysis reveals that duration, and not other
firm-level characteristics, drives returns.
We do a more rigorous analysis of dividend strips in Table VIII. The table reports the
results of the following end-of-year panel regressions:
yi,m
t,t+m = b2Dm
2 + b3Dm
3 + b4Dm
4 + B′
1Xi,m
t
+ B′
2Xi
t + ei,m
t
,
(10)
where yi,m
t,t+m = Et[ri,m
t,t+m] or yi,m
t,t+m = αi,m
t,t+m, D2 to D4 are maturity dummies for the claims,
Xi,m
t
is a vector of time t strip-level characteristics, and Xi
t is a vector of time t firm-level
characteristics. Time t is the end of December of a given year. One of the right-hand side
characteristics is duration, which we scale by its cross-sectional standard deviation for ease
of interpretation.
The leftmost regression in the table has expected returns on the left-hand side and on
the right-hand side it has the CAPM beta of the strip, the CAPM beta of the underlying
firm, and the cash-flow duration of the underlying firm. We find a positive relation between
expected returns and both the beta of the strip and the beta of the underlying firm. This
finding suggests that betas are priced in the dividend strips and that there is a link between
the pricing of strips and the risk of the underlying firm. We find no relation between the
cash-flow duration of the underlying firm and the expected returns. The regressions control
for date and currency fixed effects.34 We cluster standard errors by date and firm.
The next regression instead has the maturity dummies on the right-hand side. We find
a slightly negative relation between maturity and dummies, in the sense that the loadings
on the dummies are negative, and increasingly so, for the three- and four-year claim. The
effect is significant for the four-year claim. Column (3) augments the regression with the
34The contracts are traded in the currency in which the dividends are paid out.
24


---

CAPM betas. Doing so intensifies the negative relation between returns and maturity, such
that the effect is significant for both the two-year and three-year claims. This result reflects
the notion that CAPM betas increase in maturity, as shown in the rightmost columns of
the table.
The fourth and fifth columns of Table VIII have CAPM alpha on the left-hand side. The
CAPM alphas load negatively on the maturity dummies, and increasingly so, suggesting
a negative relation between maturity and alpha on the strips. We again find no effect
of cash-flow duration of the underlying firm.
The results are robust to using notional
outstanding as weight, which ensures that the results are not driven by the less liquid
strips.
In Internet Appendix Table IA.III, we further study the effects of liquidity by
including liquidity measures such as volume and open interest on the right-hand side of our
regressions. Doing so has no impact on the results, further suggesting that the results are
not driven by liquidity issues related to the dividend strips.
The final column has CAPM betas on the left-hand side, finding that betas indeed
increase in maturity and that the beta of the individual strip is related to the beta of the
underlying firm on the stock exchange. The fact that the CAPM beta of the underlying
firm is significantly related to the beta and expected return on the firm’s dividend strips
is important because it alleviates concerns about potential segmentation between the two
markets.
The analysis in Tables VII and VIII essentially decomposes the alpha of the dividend
strips into the part that can be explained by maturity and the part that can be explained
by duration characteristics. However, alphas could vary across firms even after controlling
for duration. Table IA.IV in the Internet Appendix addresses this concern by including firm
fixed effects in the regressions. The fixed effects indeed increase the R2, suggesting there
could be firm-level effects on the strips. Importantly, however, there do not appear to be
firm-level differences along the duration characteristic, and controlling for these differences
with fixed effects do not influence the results on the maturity dimension.
D.
Realized Returns and Alphas
Looking at expected as opposed to realized returns brings additional power to our tests
but it also leaves open the possibility that analysts’ expectations are biased. We therefore
also look at realized returns. At the end of each year, we calculate the realized returns
from buying a contract and selling it one year later. If the contract has matured upon
selling, we use the settlement price as the selling price. For CAPM alphas, we calculate
realized alphas as the difference between realized returns and the product of the beta and
25


---

the realized return on the market in which the firm is incorporated.
See Appendix B
(Section B.C) for details.
We start by projecting the realized returns onto the ex ante expected returns. Table IX,
Panel A reports the results. Without regression weights, the slope coefficients are between
0.68 and 0.80, depending on the choice of fixed effects and type of return. We generally
cannot reject that the slope coefficients are equal to 1 in the equal-weighted regressions.
We next project the realized returns onto the maturity dummies from the panel regres-
sion above. These regressions include firm fixed-effects as we have no firm-level characteris-
tics on the right-hand side. The first two regressions in Panel B have realized returns on the
left hand side. We find a largely flat effect between returns and maturity. We next project
the realized alphas onto the dummies. Here we find a negative relation between alpha and
maturity. The coefficients are larger than those from the expected alphas, but the signif-
icance is substantially weaker given the noise inherent in looking at realized returns. We
cluster by date and firm, or alternatively by date and strip (i.e., date and firm×maturity).
Clustering at the higher (date and firm) level is more conservative, and yields slightly less
significant results than clustering by date and strip.
Panel C replaces the firm fixed effects with the cash-flow maturity of the underlying
firm on the right-hand side. The results reveal a positive relation between realized alphas
and duration characteristics, which mean that longer cash-flow duration of the underlying
firm corresponds to lower returns. The effect is marginally significant in one specification.
These results contrast to the results on expected returns, where there we find no relation
between returns and duration.
The discrepancy might reflect noise, or it might reflect
overoptimistic beliefs. In either case, it suggests that realized returns have been lower than
expected for long-duration firms.
Panel D highlights this finding by taking the difference between realized and expected
returns on the left-hand side. We find no relation between these expectations errors and
the maturity dummies. But we do find a negative relation between the expectations er-
rors and the cash-flow duration, again emphasizing that beliefs in this sample have been
overoptimistic. The findings on realized returns suggest that overoptimistic expectations
about growth rates of long-duration firms could play a role in explaining the returns on the
duration factor. We explore this explanation more in Section V. We note, however, that an
overreaction explanation cannot easily account for the negative relation between cash-flow
maturity and both realized and expected alphas.
In conclusion, the dividend strips reveal a negative relation between the maturity of the
strips and the risk-adjusted return. These results suggest that cash-flow duration plays a
role in the returns associated with the major risk factors.
26


---

E.
Alpha Accounting
The analysis above identifies a relation between cash-flow duration and stock returns.
We next explore whether cash-flow duration can quantitatively explain the return on the
duration factor. To asses the quantitative effects, we need the full term structure of CAPM
alphas for dividend strips. As we only observe prices of dividend strips for the first few
years, we specify a functional form for the term structure and calibrate it such that it
is consistent with the dividend strips we observe and such that the market has a CAPM
alpha of zero. We then analyze whether such a term structure can generate a meaningful
difference in the expected returns between long- and short-duration firms.
We specify that CAPM alphas on dividend strips of maturity m follow
bαm = κ0 −κ1 ln (m)
(11)
and set κ0 = 9%. We choose κ1 such that the market portfolio has a CAPM alpha of zero.
To do so, we must take a stand on how the weights on future cash flows develop for the
market portfolio. We assume that the weight on the m-th period cash flow is
wm =
1 + g
1 + r
m
= (0.97)m ,
(12)
which results in a cash-flow duration of 33.33 years.35 We then choose κ1 such that
∞
X
m=1

0.97m × (κ0 −κ1 ln(m))

= 0.
(13)
Figure VII plots the resulting term structure of CAPM alphas for the first 100 years.
The term structure starts at 9% by assumption and reaches -5.5% for the 100-year claim.
We next study the CAPM alphas to a long- and a short-duration firm. For the short-
duration firm, we assume that the ratio of growth rates to discount rates is 0.94, which
results in a duration of approximately 16 years. For the long-duration firm, we assume a
ratio of 0.985, which results in a duration of approximately 66 years.
Table X shows the average CAPM alphas and weights for different parts of the term
structure in this exercise. The first row shows that the average CAPM alpha for the 1-
35In calculating duration, we approximate the weights ωm by the weights wm. As explained in Section
I.E, these two weights are slightly different because the weights for duration, ωm, are based on present
values calculated based on the yields whereas wm are weights based on the actual present values.
27


---

to 20-year claims is around 2.8% per year. From there it decreases as shown in Figure
VII. The table also reports the average weights that the market portfolio puts on different
parts of the term structure. More importantly, it shows the average weights that long- and
short-duration firms put on different parts of the term structure and the resulting CAPM
alphas.
The CAPM alpha on short-duration firms is 2.11% per year and the CAPM alpha on
long-duration firms is -2.27% per year. These results compare well to the results on the
large-cap firm portfolios in Table III. The large-cap short-duration portfolio has an annual
alpha of around 2% and the long-duration portfolio has a CAPM alpha of around -2.9%.
As such, the effect of cash-flow duration is quantitatively large enough to explain most of
the CAPM alpha of large-cap firms in this example (we cannot easily evaluate the CAPM
alpha of small-cap firms as these firms do not have dividend futures traded on them).
The above is a reduced-form approach meant to illustrate the quantitative effects of
cash-flow duration. A more rigorous approach would be to specify a flexible functional
form for the data generating process and the pricing kernel, to estimate these, and to
calculate implied prices of dividend strips as in Hansen, Heaton, and Li (2008). In this
context, one can discipline the model by forcing it to price the dividend futures we observe.
We consider this approach an interesting avenue for future research.
F.
Relation to the Results on Index-Level Dividends
Binsbergen and Koijen (2017) study the pricing of index-level dividends and find a
negative relation between maturity of dividends and risk-adjusted returns. These results
are consistent with ours but it is important to emphasize that the negative relation be-
tween maturity and CAPM alphas on index-level dividends does not necessarily imply a
similar effect at the firm level. The reason is that the composition of the index varies
with maturity.
By construction, the near-future index has a relatively large weight on
short-duration firms while the distant-future dividends have a relatively large weight on
long-duration firms.36 Accordingly, when comparing near- and distant-future dividends on
the market portfolio, one is effectively comparing cash flows on long- and short-duration
firms. As discussed above, these cash flows may have different returns because of cash-flow
duration or because of other differences in the characteristics of long- and short-duration
firms, something we cannot distinguish between without the single-stock dividend futures.
36This effect can be large. In the example in Section IV.E, long-duration firms have twice as large a
weight in the market portfolio as in the near-future dividends.
28


---

In addition, the index-level dividends naturally cannot speak to whether or not there are
firm-level differences in the alpha on the individual cash flows.
G.
Robustness Analysis from Corporate Bonds
We perform a similar exercise using the corporate bonds described in Section I.C. At
time t, we sort all firms for which we have bonds into two groups based on firm-level
characteristics at time t. We then sort corporate bonds issued by these firms into portfolios
based on maturity and study their performance.
Table XI reports the CAPM alphas for bond portfolios sorted on firm-level character-
istics and maturity. The CAPM alpha is the intercept in a regression of equal-weighted
excess returns of the portfolio’s bonds on the market. We measure excess returns as returns
in excess of the return on a Treasury with the same maturity.
Panel A considers portfolios sorted on the duration characteristics and maturity. For
both long- and short-duration firms, the alpha decreases in maturity.
In addition, the
alpha does not vary across the duration characteristic. These results again suggest that the
maturity of the cash flows, not firm-level characteristics, is the main driver of risk-adjusted
returns. We find similar results for the other characteristics. Figure A3 shows t-statistics
for portfolios sorted on the other firm-level characteristics. None of these characteristics
predict differences in the bonds’ CAPM alphas, but for all sorts, the alphas decrease in the
maturity of the claim.
Our corporate bond analysis is intended as a robustness check for our results on dividend
strips.
We note, however, that the consistency of these two sets of results suggests a
promising avenue for unifying the cross-section of equity and debt in a parsimonious way.
V.
Economic Mechanisms
In previous section, we identify an effect of cash-flow timing on equity returns. We
show that part of the alpha on our duration factor must come from the fact that near-
future cash flows have high CAPM alphas. In Section V.A below, we analyze potential
economic drivers of such a premium on near-future cash flows. In Section V.B, we address
alternative economic drivers of the duration factors that are unrelated to the timing of cash
flows. Finally, in Section V.C, we relate our results to the investment CAPM.
29


---

A.
Duration-Driven Returns through Consumption Risk
The results on dividend futures, and the duration factor in general, are conceptually
consistent with a simple framework that features a consumption, or cash flow, risk factor,
and a discount-rate risk factor, where the former has a high premium and the latter has a
low premium, as in Campbell and Vuolteenaho (2004).
To see how, consider the extreme case in which only consumption risk is priced. If
consumption risk is constant over the term structure, all claims will have largely simi-
lar expected returns, as we indeed find in Tables III, VII, and VIII. If, at the same time,
discount rate risk increases in horizon, betas will increase in maturity, as is observed empir-
ically. However, if this discount-rate risk is unpriced, it will not increase expected returns
and CAPM alphas will therefore decrease in maturity. In Internet Appendix C, we study
a model with some of these dynamics based on Lettau and Wachter (2007), which shows
that the major risk factors are indeed priced in such a setting.
The key for the above dynamics is that there is more consumption risk per unit of beta
in the near-future claims than in the distant-future claims. We test whether this is the case
by studying consumption risk in the 10 duration-sorted portfolios in Table II.
Figure VIII, Panel A plots the covariance between future consumption and quarterly
returns net of the market exposure of the given portfolio. We consider two-year consump-
tion as opposed to quarterly consumption to allow for lags in the consumption response
to bad news.37 The figure shows a higher exposure to consumption risk for short-duration
portfolios than for long-duration portfolios. More precisely, when short-duration firms un-
derperform relative to their market exposure, consumption tends to decrease over the next
two years and vice versa for long-duration firms. The negative consumption beta for the
long-short portfolio is statistically significant. The economic significance is more difficult
to evaluate without a structural model, but we note that the covariances are modest. If we
consider covariance with dividends instead of consumption, the covariances are more than
ten times as large, suggesting larger economic significance.
Panel B shows that consumption risk of raw returns on duration-sorted portfolios is
more or less constant across duration. This finding is consistent with the fact that we find
very limited variation in expected returns across duration-sorted portfolios. Panel C shows
the relation between realized returns and future two-year returns on the market portfolio.
With some simplification, this relation captures how exposed a given portfolio is to changes
in expected returns and thus to discount rate risk; a more negative loading suggests a higher
37In addition, contemporaneous consumption is essentially uncorrelated with returns in this exercise.
30


---

exposure to discount-rate risk. As expected, long-duration firms appear more exposed to
changes in expected returns, though the effect is imprecisely estimated. This discount-rate
risk may partly explain why long-duration firms have high CAPM betas, as realized market
returns mostly reflect discount-rate risk (Cochrane, 2011).
In conclusion, the evidence in Figure 8 is consistent with consumption risk and discount
rate risk playing a role in the alpha on our duration factor and on the dividend strips more
generally. We note, however, that other forces such as horizon-dependent risk aversion
(Eisenbach and Schmalz (2016), Lazarus (2019)) or institutional features (Belo, Collin-
Dufresne, and Goldstein (2015)) may also play a role.
B.
Alternative Drivers of the Duration Factor
The returns on our duration factor are driven at least in part by the premium on near-
future future cash flows, and above we discuss how that premium can arise. However, as
discussed earlier, the duration factor can in principle also arise from firm-level differences in
returns. One option is that there are firm-level differences in expected returns on individual
cash flows, but the evidence in Table VII suggests that this is unlikely. The expected CAPM
alpha is almost the same for long- and short-duration firms, and if anything, long-duration
firms have higher expected CAPM alphas than short-duration firms. These findings suggest
that rational explanations of the duration factor have to revolve around a premium on near-
future cash flows.
However, another possibility is that there are differences in unexpected returns across
dividend strips, as implied by certain behavioral theories. In particular, La Porta (1996)
and Bordalo et al. (2019) argue that high-growth firms have low realized returns because
investors overestimate the expected growth rates.
This theory predicts that there are
no firm-level differences in expected alpha on dividend strips, as is the case empirically.
However, the theory also predicts that, going forward, high-growth firms have lower realized
growth than expected, leading to low realized returns on these firms. As reported in Table
IX, Panel C, we indeed find that long-duration firms have lower realized returns than short-
duration firms, suggesting that this theory has some validity. The statistical significance
is very marginal, with p-values going below 10% in only one specification where we weight
by notional and consider log-alphas. In this sense, our data do not allow us to say that
diagnostic expectations influence returns with very high levels of confidence. At the same
time, we cannot rule out that overreaction plays a role for the duration factor.
It is important to emphasize that the behavioral explanation from La Porta (1996) and
Bordalo et al. (2019) cannot explain the finding that alphas decrease in the maturity of the
31


---

cash flows. This would require a theory of maturity- rather firm-dependent expectations
errors, such as that proposed by Cassella et al. (2021). As shown in Table IX, Panel D,
we do not find significant evidence that investors make horizon-dependent forecast errors
in this sample.
C.
The Link to Production-Based Asset Pricing
Our duration-based framework is related to the production-based model (Cochrane
(1991, 1996)) and the investment CAPM (Zhang (2005), Hou, Xue, and Zhang (2015),
Hou et al. (2020)). These papers study stock returns from the perspective of corporations,
building on the idea that corporate investment responds to discount rates from financial
markets.
In particular, the first principle of investment implies that firms with higher
profit and lower investment must have higher discount rates to prevent them from investing
more, a prediction that is strongly supported by the data. This is essentially a supply-side
approach, focusing on how the supply of capital, or cash flows, ensures that the law of one
price holds.
Our approach instead takes the supply of cash flows as given and focuses on the demand
side, namely, how investors price these cash flows. In our framework, the relevant firm-level
information is summarized by the timing of its expected cash flows, so it is sufficient to treat
firms essentially as machines generating cash flows with different duration. One advantage
of this approach is that it is more easily mapped to pricing dynamics in traditional exchange
economies (Lucas, 1978). However, it is also somewhat more restrictive, as it only focuses
on discount rate variation coming from one dimension, whereas the production CAPM can
reflect discount rate variation coming from many different dimensions at once. The fact
that both approaches produce similar fundamental predictions is reassuring and suggests
that the two may be able to be combined into a common framework.
VI.
Conclusion
We study the economics of the major equity risk factors in asset pricing. Across a
broad global sample of 23 countries, risk factors based on value, profit, investment, low-
risk, and payout invest in firms with low growth rates. This common feature is sufficiently
pronounced that the risk factors can be summarized by a single factor that invests in low-
growth firms. We refer to our new factor as a duration factor, because the firms in the long
leg of the factor have not only low growth rates but also a short cash-flow duration.
We document that cash-flow duration is an important determinant of the premium on
32


---

short-duration firms. Using a new data set of single-stock dividend strips, we find that
expected and realized CAPM alphas decrease in the maturity of cash flows for individual
firms, implying a direct link between duration and CAPM alphas.
At the same time,
the firm-level duration characteristic does not explain the expected CAPM alphas on the
individual strips, suggesting that the duration characteristic only predicts expected CAPM
alphas because it predicts the duration of cash flows.
Our results thus bring identification to a large literature on the role of cash-flow duration
in stock returns. Lettau and Wachter (2007), for example, suggest a model in which value
firms have high returns because they load more on near-future cash flows, which have a
high alpha. But it is not ex ante obvious that it is the timing of cash flows — rather than
other firm-level characteristics — that generates the premium on value firms. Our data
allow us to control for firm-level characteristics and study the effect of maturity within
a given firm. Doing so, we provide direct evidence for the role of duration not only for
understanding the value premium, but also for understanding profit, investment, low-risk,
and payout premia.
Having identified an effect of duration on returns, the next question that arises is
whether the effect is strong enough to fully explain the premium on the duration factor.
We observe dividend strips only for a subset of the future dividends, meaning we cannot
provide a model-free answer to this question. That said, we show that under reasonable
assumptions about the term structure of CAPM alphas and the duration of cash flows, the
effect of duration is indeed large enough to explain the premium on the duration factor.
We also provide suggestive evidence on why near-future cash flows have high CAPM
alphas. A large literature discusses this question (see Binsbergen and Koijen, 2017, for
review). A common explanation is that near-future cash flows are more exposed to cash-
flow risk, potentially due to mean-reversion in growth rates, as in the Lettau and Wacther
(2007). Consistent with such theories, we indeed find that our duration factor is exposed
to consumption risk in that low abnormal returns on our factor are associated with lower
consumption over the subsequent two years.
However, we cannot reject the possibility that irrational expectations also play a role
for the returns to our duration factor. While there are no differences across firms in ex-
pected return and CAPM alpha by cash-flow maturity, the realized return and alpha on
individual cash flows do vary across firms. In particular, long-duration firms have lower
realized returns than short-duration firms. This finding is consistent with a theory of over-
reaction, where the high growth rates on long-duration firms make investors overestimate
the expected growth and thereby subsequently be disappointed. The statistical significance
for this finding, however, is very marginal. In addition, this behavioral explanation cannot
33


---

account for the maturity dimension of CAPM alphas, which exists in both expected and
realized returns.
Going forward, we hope that our data set of single-stock dividend futures can be used
to test and discipline new theories of the cross-section of stock returns. Almost any model
of the cross-section of stock returns will have implications for the expected returns on
individual cash flows, implications that can be tested directly in our data. As such, the
data could be useful for our continued understanding of the cross-section.
Initial submission: [DATE]; Accepted: [DATE CONDITIONALLY ACCEPTED]
Editors: Stefan Nagel, Philip Bond, Amit Seru, and Wei Xiong [OR ACTING
EDITOR]
34


---

Appendix A.
Detail on Data and Estimation
A.
Measuring Realized Growth Rates
We calculate realized dividend growth rates for characteristic-sorted portfolios following
Chen (2017). Each June, we construct portfolio breakpoints based on the most recent
characteristics. We then calculate value-weighted portfolio weights for the subsequent 180
months. Using these weights, we calculate sans and cum dividend returns of the portfolio in
each month. Using the sans dividend returns, we calculate how the value of a $1 investment
in each portfolio develops over time, including delisting returns. Using the value of the
portfolio and the difference between the cum and sans dividend return, we calculate the
monthly dividends to the portfolio.
More precisely, the value at time t + s of the portfolio formed at period t is given by:
V t
t+s = V t
t+s−1(1 + retxt
t+s),
(A.1)
where retxt
t+s is the sans dividend return between periods t+s−1 and t+s to the portfolio
formed at time t. The dividends in period t + s of the portfolio formed at period t is then
given by:
Dt
t+s = V t
t+s−1(rett
t+s −retxt
t+s),
(A.2)
where rett
t+s is the cum dividend return between periods t + s −1 and t + s to the portfolio
formed at time t.
For each formation period, we calculate the average dividends per $100 initial investment
in each year after formation until year 15.
To calculate the dividend growth rate, we
calculate the average dividends per year after formation across the different formation
periods and finally calculate dividend growth rates as the growth in the average dividends
over the 15 years after formation.
For earnings growth, we again use the methodology developed in Chen (2017).
To
mitigate the fact that earnings are volatile, we average earnings over three years before
calculating growth rates. In particular, to calculate 15-year growth rates, we compare the
average earnings in years 13, 14, and 15 after formation to the average earnings in the year
after formation, the year of formation, and the year prior to formation.
35


---

B.
Definition of Equity Characteristics
We define the book-to-market, profit, and investment characteristics following Fama
and French (2015). We use the beta characteristic from Frazzini and Pedersen (2014). We
follow Asness, Frazzini, and Pedersen (2019) and define payout as the total payout over
the last five years divided by total profits over the last five years. Here, payout is measured
as net income minus change in book equity from the year before, and total income is sales
minus cost of goods sold.
C.
Sample Periods
We work with three different sample periods in the U.S. depending on data availability.
Whenever we need IBES data, the sample starts in 1981. When we conduct cross-sectional
factor analysis, the sample starts in 1963 because that is when the Fama and French
five-factor model becomes available. Finally, when studying the duration characteristic,
the sample starts in 1929 because this is when the first variable needed to construct the
characteristic becomes available (market beta).
Appendix B.
Details on Single-Stock Dividend Strips
A.
Matching and Cleaning
We obtain data on single-stock dividend futures directly from the Eurex Exchange.
The strips are organized by product ID. Each product ID is associated with an underlying
ISIN, which is the asset that keeps track of the dividend points for the given firm. Each
product ID is also associated with a firm ISIN, which is the firm that the underlying ISIN
is associated with. Finally, each contract is also associated with a currency, a contract
size,38 and a minimum price change. At each point in time, a firm can be associated with
multiple product IDs.
We first match the firm underlying each product ID to a GVKEY in Compustat using
ISIN. In the case that product ID is associated with multiple GVKEYS, we use the first
issuance number in Compustat. We then aggregate contracts across GVKEYS such that at
each point in time t, we have only one firm (i) × maturity (m) observation. We aggregate
notional outstanding and volume across contracts. Only in three cases do we observe a
38Almost all contracts are for 1,000 contracts of the underlying, that is, 1000 shares, but this can vary
for some of the contracts.
36


---

firm that has multiple dividend claims of a given maturity traded at different prices. In
two of the cases, this occurs because the underlying index (the asset that keeps track of the
dividends) is different. The dividend indexes are apparently different because of spin-offs.39
In all three cases, the prices are fairly close, so we simply value-weight across the claims.
Regarding currencies, the Vodafone claim has both a euro and a pound version, but since the
euro version has no open interest, we simply discard it from our data set. We also discard
all observations without any open interest, which is a substantial number of observations.
The resulting data set comprises 599,125 unique day×firm×maturity observations.
B.
Prices
We observe the daily end-of-day settlement prices on Eurex Exchange. These are the
prices that the outstanding contracts are settled against in the risk management systems.
These reflect a combination of traded prices, quotes, and proprietary models. The settle-
ment prices are sometimes updated without there being any trading. We complement these
settlement prices with a time series of traded prices that we construct ourselves. For each
claim, we create a traded price that we keep track of in calendar time and update to the
new settlement price only on days where we observe traded volume for the particular claim.
Our main returns are based on our traded prices, but we note that in some cases,
settlement prices are likely more useful. For instance, Deutsche Bank announced a dividend
ban in July 2019. Naturally, there was no trading in the 2020 claim following the ban, as
the contracts were worthless, which means that traded prices stay at the pre-ban level.
Settlement prices, however, were adjusted by Eurex to 0.
C.
Calculating Returns
C.1. Realized Returns and Alphas
We calculate realized annual returns by looking at the one-year change in prices. At
the end of each December, we calculate the realized returns over the next year as
ri,m
t+1 = f i,m−1
t+1
f i,m
t
−1.
(B.1)
39We conjecture that one of the indexes includes the dividends associated with the company subject to
the spin-off.
37


---

We use traded prices as the time t prices. We also use traded prices as the time t+1 prices
unless the contract matures at t + 1, in which case we use settlement prices. Note that
these are futures returns, meaning that they are measured in excess of the risk-free rate.
We also calculate a time series of realized monthly returns that we use to calculate
CAPM betas (see Section B.D of this appendix). The monthly realized returns are based
on settlement prices to minimize the impact of market micro-structure issues.
Finally, we calculate realized alphas by looking at the realized market returns,
˜αi,m
t
= ri,m
t+1 −βi,mri,MKT
t+1
.
(B.2)
Here, the market return is the excess return on the stock market in the country in which
the firm is listed. Betas are calculated as explained in Section B.D of this appendix.
C.2. Expected Returns and Alphas
We match the data to expected dividends from IBES. For each claim at time t, we
match the observation to the most recent IBES expectations for the same firm, matched
by GVKEY, for the period ending at the expiration of the claim. We use annual expected
dividends per share.
Using these expectations, we calculate expected yield-to-maturity as:
Et[ri,m
t,t+m] =
 
Et[Di,m
t+m]
f i,m
t
!1/m
−1,
(B.3)
where Et[ri,m
t,t+m] is the expected return between periods t and t + m for the dividend on
firm i that is paid out at period t + m. The term Et[Di,m
t+m] is the time t expected value of
the dividend.
There is a risk that the dividends expectations in IBES refer to a different traded version
of the firm than the dividend strip refers to. We therefore discard any observation for which
the expected annualized return is above 30% or below -10%.
We calculate expected yield-to-maturity alphas as:
αi,m
t,t+m = Et[ri,m
t,t+m] −βi,m
MaturityλMkt
t,t;m,
(B.4)
where αi,m
t,t+m is the annualized alpha between periods t and t + m for the dividend paid out
by firm i in period t+m, and λMkt
t,t;m is equal to the market risk premium (in future returns),
which we assume is 5%. Finally, βi,m
Maturity is the beta-to-maturity, calculated as explained
38


---

in the next section.
D.
Calculating CAPM Betas
We estimate CAPM betas in regressions of monthly returns on the strip on the market
return, where we include lags of the market to account for stale prices following Dimson
(1979) and Lewellen and Nagel (2006). Following the literature, we impose the restriction
that the last three lags have the same slope parameter to reduce the number of parameters
and run the following regression:
ri,m
t,t+1 =βi,m
0
+ βi,m
1
rM,e
t+1 + βi,m
2
rM,e
t
+ βi,m
3
(rM,e
,t−1 + rM,e
t−2 + rM,e
t−3) + ϵi,m
t,t+1,
(B.5)
where rM,e
t+1 is the excess return on the market between periods t and t + 1. The market is
again the return on the market portfolio in the country in which the main trading vehicle of
the underlying firm is located. We calculate βi,m = βi,m
1
+ βi,m
2
+ βi,m
3
. Here, t is measured
in months and the maturity m is measured in years. We round up the maturity of the
claim to the nearest integer; since the regressions are monthly, the maturity measured
in years is often noninteger, that is, a claim has a maturity of n when 12 × (n −1) <
maturity in months ≤12 × n.
When calculating the expected alpha-to-maturity, we use yield-to-maturity betas. We
calculate these as the average betas over the remaining life of a given strip:
βi,m
Maturity = 1
m
m
X
j=1
βi,j.
(B.6)
For instance, the yield-to-maturity beta of a 3-year claim is the average beta on the 1-year,
2-year, and 3-year strips on the given firm.
39


---

REFERENCES
Adrian, Tobias, Erkko Etula, and Tyler Muir, 2014, Financial intermediaries and the cross-
section of asset returns, Journal of Finance 69, 2557–2596.
Andrews, Spencer, and Andrei S. Gonçalves, 2020, The bond, equity, and real estate term
structures, Working Paper.
Asness, Cliff, Andrea Frazzini, Niels Joachim Gormsen, and Lasse Heje Pedersen, 2020,
Betting against correlation: Testing theories of the low-risk effect, Journal of Financial
Economics 135, 629–652.
Asness, Clifford S, Andrea Frazzini, and Lasse Heje Pedersen, 2019, Quality minus junk,
Review of Accounting Studies 24, 34–112.
Bali, Turan G., Stephen J. Brown, Scott Murray, and Yi Tang, 2017, A lottery-demand-
based explanation of theÂ beta anomaly, Journal of Financial and Quantitative Analysis
52, 2369–2397.
Bansal, Ravi, Shane Miller, Dongho Song, and Amir Yaron, 2020, The term structure of
equity risk premia, Journal of Financial Economics p. forthcoming.
Belo, Frederico, Pierre Collin-Dufresne, and Robert S Goldstein, 2015, Dividend dynamics
and the term structure of dividend strips, Journal of Finance 70, 1115–1160.
Binsbergen, Jules H. van, 2020, Duration-based stock valuation, Working paper, National
Bureau of Economic Research.
Binsbergen, Jules H. van, Michael Brandt, and Ralph Koijen, 2012, On the timing and
pricing of dividends, American Economic Review 102, 1596–1618.
Binsbergen, Jules H. van, Wouter Hueskes, Ralph Koijen, and Evert Vrugt, 2013, Equity
yields, Journal of Financial Economics 110, 503–519.
Binsbergen, Jules H. van, and Ralph SJ Koijen, 2017, The term structure of returns: Facts
and theory, Journal of Financial Economics 124, 1–21.
Bordalo, Pedro, Nicola Gennaioli, Rafael La Porta, and Andrei Shleifer, 2019, Diagnostic
expectations and stock returns, Journal of Finance 74, 2839–2874.
Campbell, John Y, and Tuomo Vuolteenaho, 2004, Bad beta, good beta, American Eco-
nomic Review 94, 1249–1275.
Carhart, Mark M, 1997, On persistence in mutual fund performance, Journal of Finance
52, 57–82.
Cassella, Stefano, Benjamin Golez, Huseyin Gulen, and Peter Kelly, 2019, Horizon bias
and the term structure of equity returns, Available at SSRN 3328970.
40


---

Cassella, Stefano, Benjamin Golez, Huseyin Gulen, and Peter Kelly, 2021, Horizon bias in
expectations formation, Available at SSRN.
Cejnek, Georg, and Otto Randl, 2020, Dividend Risk Premia, Journal of Financial and
Quantitative Analysis 55, 1199–1242.
Chan, Louis K. C., Jason Karceski, and Josef Lakonishok, 2003, The level and persistence
of growth rates, Journal of Finance 58, 643–684.
Chen, Huafeng (Jason), 2017, Do cash flows of growth stocks really grow faster?, Journal
of Finance 72, 2279–2330.
Chen, Shan, and Tao Li, 2018, A unified duration-based explanation of the value, prof-
itability, and investment anomalies, Profitability, and Investment Anomalies (November
26, 2018).
Chen, Zhanhui, 2020, Inferring stock durations around fomc surprises: Estimates and
implications, Journal of Financial and Quantitative Analysis pp. 1–55.
Chernov, Mikhail, Lars A. Lochstoer, and Stig R. H. Lundeby, 2022, Conditional Dynamics
and the Multihorizon Risk-Return Trade-Off, Review of Financial Studies 35, 1310–1347.
Cochrane, John H., 1991, Production-based asset pricing and the link between stock returns
and economic fluctuations, Journal of Finance 46, 209–237.
Cochrane, John H., 1996, A cross-sectional test of an investment-based asset pricing model,
Journal of Political Economy 104, 572–621.
Cochrane, John H., 2011, Presidential Address: Discount Rates, Journal of Finance 66,
1047–1108.
Dechow, Patricia M, Richard G Sloan, and Mark T Soliman, 2004, Implied equity duration:
A new measure of equity risk, Review of Accounting Studies 9, 197–228.
Dimson, Elroy, 1979, Risk measurement when shares are subject to infrequent trading,
Journal of Financial Economics 7, 197–226.
Eisenbach, Thomas M., and Martin C. Schmalz, 2016, Anxiety in the Face of Risk, Journal
of Financial Economics 121, 414–426.
Fama, Eugene F., and Kenneth R. French, 1993, Common risk factors in the returns on
stocks and bonds, Journal of Financial Economics 33, 3–56.
Fama, Eugene F., and Kenneth R. French, 2015, A five-factor asset pricing model, Journal
of Financial Economics 116, 1 – 22.
Fama, Eugene F., and Kenneth R. French, 2016, Dissecting anomalies with a five-factor
model, Review of Financial Studies 29, 69–103.
41


---

Feng, Guanhao, Stefano Giglio, and Dacheng Xiu, 2020, Taming the factor zoo: A test of
new factors, Journal of Finance 75, 1327–1370.
Frazzini, Andrea, and Lasse Heje Pedersen, 2014, Betting against beta, Journal of Financial
Economics 111, 1–25.
Giglio, Stefano, Bryan T Kelly, and Serhiy Kozak, 2020, Equity term structures without
dividend strips data, Yale University working paper.
Giglio, Stefano, Yuan Liao, and Dacheng Xiu, 2020, Thousands of alpha tests, Review of
Financial Studies p. forthcoming.
Gonçalves, Andrei, 2020, The short duration premium, Journal of Financial Economics p.
forthcoming.
Gormsen, Niels Joachim, 2021, Time variation of the equity term structure, Journal of
Finance 76, 1959–1999.
Gormsen, Niels Joachim, and Ralph SJ Koijen, 2020, Coronavirus: Impact on stock prices
and growth expectations, The Review of Asset Pricing Studies 10, 574–597.
Hansen, LarsÂ Peter, JohnÂ C. Heaton, and Nan Li, 2008, Consumption strikes back?
measuring long-run risk, Journal of Political Economy 116, 260–302.
Harvey, Campbell, and Yan Liu, 2017, Lucky factors, Working Paper.
Harvey, Campbell R., Yan Liu, and Heqing Zhu, 2016, ... and the cross-section of expected
returns, Review of Financial Studies 29, 5–68.
Hasler, Michael, and Roberto Marfe, 2016, Disaster recovery and the term structure of
dividend strips, Journal of Financial Economics 122, 116–134.
Hou, Kewei, Haitao Mo, Chen Xue, and Lu Zhang, 2020, An augmented q-factor model
with expected growth, Review of Finance.
Hou, Kewei, Chen Xue, and Lu Zhang, 2015, Digesting anomalies: An investment approach,
Review of Financial Studies 28, 650–705.
Kozak, Serhiy, Stefan Nagel, and Shrihari Santosh, 2020, Shrinking the cross-section, Jour-
nal of Financial Economics 135, 271–292.
La Porta, Rafael, 1996, Expectations and the cross-section of stock returns, Journal of
Finance 51, 1715–1742.
Lazarus, Eben, 2019, Horizon-Dependent Risk Pricing: Evidence from Short-Dated Op-
tions, Working Paper.
Lazarus, Eben, Daniel J Lewis, James H Stock, and Mark W Watson, 2018, HAR inference:
Recommendations for practice, Journal of Business and Economic Statistics 36, 541–559.
42


---

Lettau, Martin, and Jessica A. Wachter, 2007, Why is long-horizon equity less risky? a
duration-based explanation of the value premium, Journal of Finance 62, 55–92.
Lewellen, Jonathan, and Stefan Nagel, 2006, The conditional capm does not explain asset-
pricing anomalies, Journal of Financial Economics 82, 289–314.
Liu, Jianan, Robert F. Stambaugh, and Yu Yuan, 2018, Absolving beta of volatility’s
effects, Journal of Financial Economics 128, 1–15.
Lucas, Robert E. Jr., 1978, Asset prices in an exchange economy, Econometrica 46, 1429–
1445.
Macaulay, Frederick R, 1938, Some theoretical problems suggested by the movements of
interest rates, bond yeilds and stock prices in the United States Since 1856. (National
Bureau of Economic Research, New York).
Manley, Richard, and Christian Mueller-Glissmann, 2008, The market for dividends and
related investment strategies (corrected), Financial Analysts Journal 64, 17–29.
Miller, Shane, 2020, The term structures of equity risk premia in the cross-section of equi-
ties, Duke University working paper.
Weber, Michael, 2018, Cash flow duration and the term structure of equity returns, Journal
of Financial Economics 128, 486–503.
Zhang, Lu, 2005, The value premium, Journal of Finance 60, 67–103.
43


---

 44 
 
 
Table I  
Growth Rates and the Characteristics that Predict Returns 
This table shows the relation between future growth rates and the characteristics that predict returns. Panel A reports 
results of a panel regression for 50 characteristic-sorted portfolios. The dependent variables are the realized 15-year 
growth rates of dividends and earnings and the explanatory variables are the characteristics of the 50 portfolios. The 
regressions include time fixed effects. Panel B reports the univariate correlations between the expected growth rates 
and firm characteristics. The expected growth rates are the median long-term growth (LTG) expectations from IBES. 
Panels C and D reports results from monthly firm level panel regressions. The dependent variable is the long-term 
growth rates from survey data and the explanatory variables are contemporaneous firm characteristics. All 
characteristics and survey growth rates are measured in cross-sectional percentiles. Standard errors are two-way 
clustered across firm and date. We report t-statistics below the parameters and statistical significance is denoted by 
*** p<0.01, ** p<0.05, * p<0.1. The sample is 1963 to 2019 in Panel A and 1981 to 2019 in Panels B through D.   
Panel A: Portfolio level regressions 
Dependent variable: 
Explanatory variables 
 
  
High value 
High profit 
Low inv 
Low beta 
High pay 
R2 
 
Realized 15-year 
dividend growth rate 
  
-0.01*** 
-0.02** 
-0.00 
-0.02*** 
-0.02*** 
0.38  
(-2.74) 
(-2.07) 
(-0.16) 
(-4.35) 
(-4.57) 
 
 
Realized 15-year 
earnings growth rate 
-0.10** 
-0.07** 
0.11** 
-0.01 
-0.06** 
0.05 
 
(-2.22) 
(-2.50) 
(1.99) 
(-0.33) 
(-2.49) 
 
 
 
  
  
  
  
  
  
 
Panel B: Firm-level univariate correlations between characteristics and analyst expectations of growth rates 
 
High BM 
High profit 
Low invest 
Low beta 
High pay 
 
 
Expected growth (LTG) 
-0.38 
-0.13 
-0.26 
-0.29 
-0.30 
  
 
 
 
  
 
 
 
Panel C: Firm-level regressions of survey expected growth rates on different characteristics 
U.S. Only 
Dependent variable: analyst expected growth rates (LTG) 
 
 
(1) 
(2) 
(3) 
(4) 
(5) 
(6) 
 
High BM 
-0.490*** 
-0.511*** 
-0.445*** 
-0.334*** 
-0.331*** 
-0.328*** 
 
 
(-53.60) 
(-21.63) 
(-53.21) 
(-34.10) 
(-27.53) 
(-22.54) 
 
High profit 
-0.197*** 
-0.293*** 
-0.212*** 
-0.095*** 
-0.056*** 
-0.168*** 
 
 
(-22.61) 
(-9.554) 
(-24.70) 
(-11.40) 
(-6.230) 
(-11.42) 
 
Low investment 
-0.0923*** 
-0.094*** 
-0.074*** 
-0.046*** 
-0.036*** 
-0.041*** 
 
 
(-16.33) 
(-4.841) 
(-13.99) 
(-12.23) 
(-7.025) 
(-8.599) 
 
Low beta 
-0.173*** 
-0.280*** 
-0.131*** 
-0.067*** 
-0.026*** 
-0.046*** 
 
 
(-18.51) 
(-12.65) 
(-15.33) 
(-9.053) 
(-2.745) 
(-4.777) 
 
High payout 
-0.259*** 
-0.168*** 
-0.229*** 
-0.116*** 
-0.120*** 
-0.086*** 
 
 
(-33.51) 
(-6.810) 
(-31.18) 
(-16.63) 
(-12.91) 
(-9.287) 
 
Fixed effect 
Date 
Date 
Date 
Firm/Date 
Firm/Date 
Firm/Date 
 
Cluster 
Firm/Date 
Firm/Date 
Firm/Date 
Firm/Date 
Firm/Date 
Firm/Date 
 
Weight 
Analysts 
Market Cap 
None 
Analysts 
Analysts 
Analysts 
 
Sample 
Full 
Full 
Full 
Full 
Early 
Late 
 
Observations 
 582,580  
 582,580  
 582,580  
 582,488  
 267,544  
 314,914  
 
R2 
0.467 
0.406 
0.321 
0.740 
0.810 
0.707 
 
 
 
 
 
 
 
 
 


---

 45 
 
 
 
Table I -- Continued 
Growth Rates and the Characteristics that Predict Returns 
 
Panel D: Firm-level regressions of survey expected growth rates on different characteristics – 
International Evidence 
Non-U.S. 
Dependent variable: analyst expected growth rates (LTG) 
 
 
(1) 
(2) 
(3) 
(4) 
(5) 
(6) 
 
High value 
-0.166*** 
-0.191*** 
-0.151*** 
-0.132*** 
-0.146*** 
-0.161*** 
 
 
(-16.92) 
(-9.280) 
(-17.15) 
(-10.93) 
(-6.197) 
(-9.475) 
 
High profit 
-0.090*** 
-0.112*** 
-0.076*** 
-0.157*** 
-0.055** 
-0.270*** 
 
 
(-8.964) 
(-5.087) 
(-8.768) 
(-12.71) 
(-2.129) 
(-15.15) 
 
Low investment 
-0.025*** 
-0.007 
-0.023*** 
0.019*** 
-0.021** 
0.036*** 
 
 
(-3.613) 
(-0.525) 
(-3.778) 
(-3.40) 
(-2.173) 
(-5.492) 
 
Low beta 
-0.055*** 
-0.115*** 
-0.052*** 
0.007 
0.021 
0.04*** 
 
 
(-5.770) 
(-7.124) 
(-5.990) 
(-0.765) 
(-1.179) 
(-2.8210) 
 
High payout 
-0.152*** 
-0.135*** 
-0.138*** 
-0.062*** 
-0.045** 
-0.049*** 
 
 
(-17.53) 
(-8.381) 
(-17.65) 
(-7.075) 
(-2.547) 
(-4.053) 
 
Fixed effect 
Date 
Date 
Date 
Firm/Date 
Firm/Date 
Firm/Date 
 
Cluster 
Firm/Date 
Firm/Date 
Firm/Date 
Firm/Date 
Firm/Date 
Firm/Date 
 
Weight 
Analysts 
Market Cap 
None 
Analysts 
Analysts 
Analysts 
 
Sample 
Full 
Full 
Full 
Full 
Early 
Late 
 
Observations 
366,867 
366,867 
366,867 
366,795 
104,264 
262,498 
 
R2 
0.06 
0.09 
0.04 
0.32 
0.49 
0.35 
 
 
 
 
 
 
 
 
 


---

 
 46 
 
 
Table II 
Risk and Return for Portfolios Sorted on Duration 
This table reports the risk and return characteristics for 10 long-only portfolios sorted on duration and a long-short portfolio. We sort stocks into 10 groups based 
on our measure of ex ante duration. Portfolio weights are value-weighted and rebalanced monthly and the breakpoints are refreshed each June and based on NYSE 
firms. CAPM alpha is the intercept in a regression of the excess return to the portfolio on the excess return to the market portfolio. We report t-statistics in 
parentheses under parameter estimates and statistical significance is denoted by *** p<0.01, ** p<0.05, * p<0.1.  Sharpe ratios and information ratios are annualized. 
Excess returns and alphas are in monthly percent. Realized duration is calculated based on the assumption that dividend growth rates of the portfolios continue 
forever and a constant discount rate of 8% per year for all portfolios. The sample is U.S. firms from 1929 to 2019.  
 
Portfolios sorted on duration 
Long/short 
 
1 
2 
3 
4 
5 
6 
7 
8 
9 
10 
10 minus 1 
Excess return 
0.67*** 
0.68*** 
0.68*** 
0.69*** 
0.73*** 
0.83*** 
0.71*** 
0.71*** 
0.7*** 
0.55* 
-0.13 
 
(5.87) 
(5.22) 
(4.57) 
(4.28) 
(4.09) 
(4.35) 
(3.34) 
(3.16) 
(2.70) 
(1.80) 
(-0.53) 
CAPM alpha 
0.30*** 
0.23*** 
0.15*** 
0.11** 
0.09 
0.14** 
-0.05 
-0.10 
-0.22** 
-0.49*** 
-0.79*** 
 
(5.18) 
(4.38) 
(3.08) 
(2.33) 
(1.69) 
(2.58) 
(-0.82) 
(-1.38) 
(-2.43) 
(-3.79) 
(-4.94) 
CAPM beta 
0.61*** 
0.73*** 
0.86*** 
0.95*** 
1.06*** 
1.13*** 
1.25*** 
1.33*** 
1.51*** 
1.69*** 
1.08*** 
 
(56.68) 
(74.66) 
(93.59) 
(108.21) 
(109.33) 
(109.59) 
(105.90) 
(103.92) 
(91.62) 
(71.32) 
(36.73) 
Sharpe ratio 
0.62 
0.55 
0.48 
0.45 
0.43 
0.46 
0.35 
0.33 
0.28 
0.19 
-0.06 
Information ratio 
0.55 
0.46 
0.33 
0.25 
0.18 
0.27 
-0.09 
-0.15 
-0.26 
-0.40 
-0.52 
Adjusted-R2 
0.75 
0.84 
0.89 
0.91 
0.92 
0.92 
0.91 
0.91 
0.89 
0.82 
0.55 
# of observations 
1091 
1091 
1091 
1091 
1091 
1091 
1091 
1091 
1091 
1091 
1091 
Realized dividend growth rates 
2% 
3% 
4% 
4% 
4% 
4% 
5% 
5% 
6% 
7% 
 
 
 
 
 
 
 
 
 
 
 
 
 
Analyst expected growth rates 
7% 
8% 
9% 
9% 
10% 
11% 
12% 
13% 
13% 
16% 
 
Realized duration 
15 
17 
18 
18 
20 
20 
24 
28 
33 
59 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


---

 
 47 
 
 
Table III 
The Duration Factor 
This table shows the risk and return characteristics for the portfolios that constitute our duration factor.  We sort stocks 
into six portfolios based on ex ante size and duration. The breakpoints are the median market capitalization and the 
30th and 70th percentiles of duration. Portfolio weights are value-weighted and rebalanced monthly, and the breakpoints 
are refreshed each June and based on NYSE firms. The duration factor is long 50 cents in the two short-duration 
portfolios and short 50 cents in each of the two long-duration portfolios. CAPM alpha is the intercept in a regression 
of the risk factor on the excess return to the market portfolio. We report t-statistics in parentheses under parameter 
estimates and statistical significance is denoted by *** p<0.01, ** p<0.05, * p<0.1.  Sharpe ratios and information 
ratios are annualized. Excess return and alphas are in monthly percent. Returns in the U.S. sample are from 1963 to 
2019, realized growth is from 1929 to 2020, and expected growth is from 1981 to 2019. The global sample is from 
1990 to 2019.  
Panel A: U.S. 
 
Long duration 
Short duration 
Duration factor 
 
Large cap 
Small cap 
Large cap 
Small cap 
 
Excess return 
0.43** 
0.63** 
0.58*** 
0.94*** 
0.23* 
 
(1.99) 
(2.33) 
(4.10) 
(5.66) 
(1.91) 
CAPM alpha 
-0.24*** 
-0.13 
0.15*** 
0.48*** 
0.50*** 
 
(-4.38) 
(-0.93) 
(3.08) 
(5.63) 
(5.64) 
CAPM beta 
1.24*** 
1.40*** 
0.79*** 
0.85*** 
-0.50*** 
 
(99.19) 
(45.72) 
(69.39) 
(43.91) 
(-24.69) 
Sharpe ratio 
0.26 
0.31 
0.55 
0.75 
0.25 
Information ratio 
-0.59 
-0.12 
0.41 
0.76 
0.76 
Adjusted-R2 
0.94 
0.76 
0.88 
0.74 
0.47 
# of observations 
678 
678 
678 
678 
678 
Analyst expected growth 
14.0% 
15.9% 
8.1% 
8.9% 
 
Realized dividend growth 
4.6% 
6.0% 
1.3% 
1.5% 
 
 
 
 
 
 
 
Panel B: Global 
 
Long duration 
Short duration 
Duration factor 
 
Large cap 
Small cap 
Large cap 
Small cap 
 
Excess return 
0.37 
0.36 
0.54*** 
0.69*** 
0.25** 
 
(1.32) 
(1.19) 
(2.74) 
(3.31) 
(1.97) 
CAPM alpha 
-0.22*** 
-0.24* 
0.13** 
0.28*** 
0.44*** 
 
(-3.80) 
(-1.88) 
(2.33) 
(3.18) 
(4.82) 
CAPM beta 
1.22*** 
1.24*** 
0.84*** 
0.83*** 
-0.39*** 
 
(89.00) 
(41.83) 
(62.29) 
(39.80) 
(-18.34) 
Sharpe ratio 
0.24 
0.22 
0.50 
0.61 
0.36 
Information ratio 
-0.70 
-0.35 
0.43 
0.59 
0.89 
Adjusted-R2 
0.96 
0.83 
0.92 
0.82 
0.49 
# of observations 
354 
354 
354 
354 
354 
Analyst expected growth 
11.4% 
14.4% 
7.2% 
8.3% 
 
 
 


---

 
 48 
 
 
Table IV 
Summarizing the Major Risk Factors with the Duration Factor 
This table reports the results of factor regressions in the U.S. sample and in the broad global sample. Each factor is on 
six portfolios based on ex ante size and the characteristic the portfolio is sorted on. The breakpoints are the median 
market capitalization and the 30th and 70th percentiles of duration. Portfolio weights are value-weighted and rebalanced 
monthly, and the breakpoints are refreshed each June and based on NYSE firms. Each factor is long 50 cents in the 
two high-characteristic portfolios and short 50 cents in each of the two low-characteristic portfolios, except the SMB 
factor, which is long the small duration-sorted portfolios and short the large duration-sorted portfolios. We construct 
global factors as the market-cap-weighted average of country-specific factors. Three-factor alpha is in the intercept in 
a regression of the given equity risk factor on the market portfolio, the duration factor, and the SMB factor. CAPM 
alpha is the intercept in a regression of the risk factor on the excess return to the market portfolio. We report t-statistics 
in parentheses under parameter estimates and statistical significance is denoted by *** p<0.01, ** p<0.05, * p<0.1.  
The U.S. sample is from 1963 to 2019 and the global sample is from 1990 to 2019.  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Panel A:  U.S. 
Factor 
 
CAPM model 
 
Three-factor model 
 
 
 
 
 
!"#$% 
&"#$% 
'( 
 
!)*+ 
&%,- 
&./0 
&)*+ 
'( 
 
LTG 
# obs 
HML 
 
0.39*** 
-0.16*** 
0.06 
 
-0.02 
0.13*** 
0.37*** 
0.66*** 
0.32 
 
-9.5% 
678 
 
 
(3.75) 
(-6.73) 
 
 
(-0.26) 
(4.62) 
(10.65) 
(15.49) 
 
 
 
 
RMW 
 
0.32*** 
-0.11*** 
0.05 
 
0.09 
0.14*** 
-0.07*** 
0.48*** 
0.35 
 
-5.1% 
678 
 
 
(3.87) 
(-5.93) 
 
 
(1.31) 
(6.34) 
(-2.67) 
(15.03) 
 
 
 
 
CMA  
 
0.37*** 
-0.18*** 
0.15 
 
0.09 
0.02 
0.25*** 
0.44*** 
0.38 
 
-6.7% 
678 
 
 
(5.19) 
(-10.87) 
 
 
(1.38) 
(1.15) 
(10.56) 
(15.48) 
 
 
 
 
BETA 
 
0.49*** 
-0.73*** 
0.53 
 
-0.04 
-0.20*** 
-0.02 
1.05*** 
0.85 
 
-7.9% 
678 
 
 
(4.22) 
(-27.87) 
 
 
(-0.52) 
(-9.63) 
(-0.80) 
(33.59) 
 
 
 
 
PAYOUT 
 
0.26*** 
-0.30*** 
0.37 
 
-0.03 
-0.02 
0.04** 
0.57*** 
0.70 
 
-7.2% 
678 
 
 
(3.86) 
(-19.89) 
 
 
(-0.72) 
(-1.67) 
(2.32) 
(25.83) 
 
 
 
 
Panel B: Global 
Factor 
 
CAPM model 
 
Three-factor model 
 
 
 
 
 
!"#$% 
&"#$% 
'( 
 
!12+33 
&%,- 
&./0 
&)*+ 
'( 
 
LTG 
# obs 
HML 
 
0.29** 
-0.09*** 
0.03 
 
-0.02 
0.17*** 
0.24*** 
0.66*** 
0.24 
 
-7.1% 
354 
 
 
(2.40) 
(-3.18) 
 
 
(-0.15) 
(4.62) 
(4.12) 
(9.93) 
 
 
 
 
RMW 
 
0.42*** 
-0.14*** 
0.18 
 
0.22*** 
0.04** 
-0.12*** 
0.47*** 
0.56 
 
-5.1% 
354 
 
 
(6.02) 
(-8.74) 
 
 
(4.25) 
(2.39) 
(-4.42) 
(15.27) 
 
 
 
 
CMA  
 
0.29*** 
-0.17*** 
0.18 
 
0.05 
0.03 
0.20*** 
0.51*** 
0.35 
 
-5.7% 
354 
 
 
(3.17) 
(-7.95) 
 
 
(0.56) 
(1.20) 
(4.56) 
(10.54) 
 
 
 
 
BETA 
 
0.42*** 
-0.65*** 
0.59 
 
-0.10 
-0.19*** 
0.10*** 
1.18*** 
0.89 
 
-6.6% 
354 
 
 
(3.47) 
(-22.79) 
 
 
(-1.58) 
(-9.01) 
(3.06) 
(30.87) 
 
 
 
 
PAYOUT 
 
0.28*** 
-0.19*** 
0.26 
 
0.03 
0.03* 
0.03 
0.56*** 
0.62 
 
-6.9% 
354 
 
 
(3.92) 
(-11.26) 
 
 
(0.64) 
(1.66) 
(1.04) 
(17.66) 
 
 
 
 


---

 
 49 
 
 
Table V 
Multi-Horizon Returns Tests for the Duration Factor 
This table reports results from the Chernov, Lochstoer, and Lundeby (CLL, 2022) multi-horizon return (MHR) tests 
for our three-factor model with the excess return on the market, the duration factor, and the duration-and-size-based 
smb factor. The first row gives the p-value of the GMM J-test provided in CLL (Section 2), which estimates the three-
factor model to fit one-period (monthly) returns and then tests the model’s ability to price the test assets’ longer-
horizon returns at 3, 6, 12, 24, and 48 months. The test assets for the first column are Mkt, Dur, and SMB at those 
horizons, while for the second column the FF5 factors at those horizons are used. Mean absolute pricing errors, Sharpe 
ratios, and information ratios in the remaining rows are with respect to the multi-horizon test asset returns. The sample 
is 1963 to 2019. 
  
Test Assets: 
Own Model’s Factors 
FF5 Factors 
p-value (GMM) 
0.060 
0.619 
Mean absolute price error (annualized) 
0.042 
0.036 
Max. Sharpe ratio 
1.133 
1.133 
Max. information ratio (annualized) 
0.776 
0.779 
 
 
 


---

 
 50 
 
 
Table VI 
Summary Statistics on Single-Stock Dividend Futures 
This table reports summary statistics for our matched sample on single-stock dividend futures. Single-stock dividend 
futures are futures prices for dividends paid out in a given calendar-year on a given firm. Panel A reports statistics for 
realized annual returns on the individual strips. Each contract is for the dividends on 1,000 shares. The price of the 
contract is measured in local currency, which can be USD, EUR, GBP, or CHE. Panel B reports summary statistics 
on the maturity of the strips and CAPM betas of the strips. The CAPM betas are measured in time-series regressions 
of monthly returns on the market portfolio in the given country, including lags, as explained in Appendix B. Panel C 
shows the characteristics of the firms in our sample, measured in cross-sectional percent of the firms listed in same 
country as the given firm. The sample is from 2010 to 2019.  
 
 
 
# obs 
Mean 
Sd 
Min 
Max 
Panel A: Returns and Prices 
Annual returns 
  
1,474 
0.049 
0.21 
-1 
1.32 
Annual returns (using settlement prices) 
  
1,474 
0.050 
0.21 
-1 
1.32 
Annual log-returns  
 
1,465 
0.034 
0.22 
-2.33 
0.84 
Annual volume  
 
1,711 
11,864 
41,701 
0 
1.07e+06 
Open interest 
 
1,711 
5,444 
15,438 
1 
341,816 
Price of contract   
 
1,711 
2,149 
3,943 
0 
69,000 
Notional (in thousands) 
 
1,711 
4,075 
7,011 
0 
71,781 
 
 
 
 
 
 
 
Panel B: Maturity and Betas 
One-year dummy 
 
1,711 
0.36 
0.48 
0 
1 
Two-year dummy 
 
1,711 
0.33 
0.47 
0 
1 
Three-year dummy 
 
1,711 
0.22 
0.42 
0 
1 
Four-year dummy 
 
1,711 
0.090 
0.29 
0 
1 
Maturity (in years) 
 
1,711 
2.04 
0.97 
1 
5 
CAPM beta of strip 
 
1,711 
0.51 
0.85 
-1 
1.50 
# Obs for CAPM beta  
 
1,711 
36.4 
27.5 
2 
101 
 
 
 
 
 
 
 
Panel C: Sample Representativeness 
Duration 
 
1,711 
33.1 
28.7 
0.078 
100 
Book-to-market 
 
1,696 
52.8 
27.0 
0.26 
100 
Market cap 
 
1,711 
97.2 
3.24 
74.1 
100 
Operating profit 
 
1,689 
62.4 
22.7 
4.47 
99.9 
Investment 
 
1,699 
48.8 
21.9 
2.55 
99.5 
Beta 
 
1,700 
74.5 
18.0 
7.45 
100 
Payout  
 
1,669 
67.3 
21.3 
0.51 
100 
 
 
 
 
 
 
 
 
 
 


---

 
 51 
 
 
Table VII 
Expected CAPM Alpha for Single-Stock Dividend Futures 
This table reports the expected average CAPM alpha for portfolios of dividend strips on different firms. At the end of 
December, we assign all dividend strips to a long- or short-duration portfolio based on the cash-flow duration of the 
underlying firm. Firms are categorized as having long (short) duration if the cash-flow duration is above (below) the 
median of all firms on the exchange in which the firm is listed. We then calculate a pooled average CAPM alpha for 
all strips of a given maturity in a given portfolio. Standard errors reported below the estimates are clustered by firm 
and date. See Appendix B for details on how we calculate CAPM alphas. The data are from 2010 to 2019.  
 
 
 
Maturity of Strip 
 
 
 
1 year 
2 year 
3 year 
4 year 
Average 
Short-duration firms 
  
0.078 
0.068 
0.056 
0.038 
0.066 
 
 
(0.0046) 
(0.0061) 
(0.0070) 
(0.0057) 
(0.0045) 
Long-duration firms 
  
0.092 
0.077 
0.064 
0.035 
0.077 
 
 
(0.011) 
(0.011) 
(0.0071) 
(0.0070) 
(0.0090) 
Average across firms 
 
0.085 
0.073 
0.060 
0.037 
 
 
 
(0.0066) 
(0.0077) 
(0.0057) 
(0.0054) 
 
 
 
 
 
 
 
 


---

 
 52 
 
 
Table VIII 
Expected Return and Alpha on Single-Stock Dividend Futures 
This table reports results from panel regressions with expected return and alphas to single-stock dividend futures as 
dependent variables. We calculate expected returns as the expected yield-to-maturity using expected dividends per 
share from the IBES database. Alphas are expected returns minus beta times a market risk premium of 5%. Regressions 
are annual using end-of-December prices. See Appendix B for details on how we calculate expected return and betas. 
The cash-flow duration characteristic is standardized by the cross-sectional standard deviation.  In the equations below, 
t, i, and m denote the time, firm, and maturity of the strip at time t (measured in years). The data are from 2010 to 
2019. Standard errors reported in parentheses are two-way clustered as specified in the table. Statistical significance 
is denoted by *** p<0.01, ** p<0.05, * p<0.1. 
 
Expected returns:    4-56-7/
8,/ : = <
=>[)>@A
B
] 
E>
B,A
F
G//
 
CAPM alphas:         !-7/
8,/ = 4-56-7/
8,/ : −&/J-*+8-K
8,/
× 5% 
 
 
 
 
 
 
 
Dependent variable 
Expected ret 
Expected ret 
Expected ret 
CAPM alpha 
CAPM alpha 
CAPM beta 
2-year dummy 
 
-0.000 
-0.004 
-0.013* 
-0.012* 
0.427*** 
 
 
(0.005) 
(0.006) 
(0.006) 
(0.006) 
(0.119) 
3-year dummy 
 
-0.002 
-0.009* 
-0.027*** 
-0.025*** 
0.816*** 
 
 
(0.003) 
(0.004) 
(0.005) 
(0.005) 
(0.111) 
4-year dummy 
 
-0.017*** 
-0.022*** 
-0.045*** 
-0.044*** 
0.805*** 
 
 
(0.004) 
(0.004) 
(0.007) 
(0.007) 
(0.137) 
CAPM beta of strip (&8,/) 
0.011*** 
 
0.014*** 
 
 
 
 
(0.003) 
 
(0.004) 
 
 
 
CAPM beta of firm (&8) 
0.044** 
 
0.044** 
 
 
0.599** 
 
(0.016) 
 
(0.016) 
 
 
(0.195) 
Cash-flow duration of firm 
-0.004 
 
-0.003 
-0.001 
-0.002 
 
(higher = shorter duration) 
(0.004) 
 
(0.004) 
(0.004) 
(0.004) 
 
Observations 
1,226 
1,236 
1,226 
1,236 
1,236 
1,699 
R2 
0.13 
0.10 
0.14 
0.10 
0.12 
0.20 
Fixed effect 
Date/Cur 
Date/Cur 
Date/Cur 
Date/Cur 
Date/Cur 
Date/Cur 
Cluster 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Weight 
None 
None 
None 
None 
Notional 
None 
 
 
 
 
 
 
 
 
 


---

 
 53 
 
 
Table IX 
Realized Return and Alpha on the Annual Horizon for Single-Stock Dividend Futures 
This table reports results from panel regressions with realized return and alphas to single-stock dividend futures as 
dependent variables. A single-stock dividend future is the price for the dividend that is paid out in a given year by a 
given firm. We calculate realized annual returns for each calendar year. We calculate realized alpha as the realized 
return minus the product of the realized market return and the beta of the strip. The beta of the strip is estimated in 
first-stage regressions (see Appendix A for details). The cash-flow duration characteristic is standardized by the cross-
sectional standard deviation. In the equations below, t, i, and m denote the time, firm, and maturity of the strip at time 
t (measured in years). The data are from 2010 to 2019. Standard errors reported in parentheses are two-way clustered 
as specified in the table. Statistical significance is denoted by *** p<0.01, ** p<0.05, * p<0.1. 
Panel A: Realized versus expected returns 
Expected returns: 4-56-7/
8,/ : = <
=>[)>@A
B
] 
E>
B,A
F
G//
 
 
Realized returns:  6-7G
8,/ = P-7G
8,/7G/P-
8,/ 
 
 
 
 
 
 
 
 
Dependent variable 
Realized 
return 
Realized 
returns 
Realized log-
return 
Realized log-
return 
Realized 
return 
Realized log-
return 
Expected return 
0.68*** 
0.76*** 
 
 
0.58*** 
 
 
(0.17) 
(0.17) 
 
 
(0.17) 
 
Expected log-return 
 
 
0.71*** 
0.80*** 
 
0.71*** 
 
 
 
(0.14) 
(0.14) 
 
(0.12) 
 
 
 
 
 
 
 
Observations 
1,059 
1,059 
1,054 
1,054 
1,059 
1,054 
R2 
0.203 
0.251 
0.171 
0.218 
0.187 
0.194 
Fixed effect 
Firm 
Date/Firm 
Firm 
Date/Firm 
Firm 
Date/Firm 
Cluster 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Weight 
None 
None 
None 
None 
Notional 
Notional 
Panel B: Realized returns and alphas 
Realized returns:  6-7G
8,/ = P-7G
8,/7G/P-
8,/ 
 
Realized alphas:  !Q-7G
8,/ = 6-7G
8,/ −&8,/6-7G
%,- 
 
 
 
 
 
 
 
 
Dependent variable 
Realized 
returns 
Realized log-
returns 
Realized 
alpha 
Realized 
alpha 
Realized log-
alpha 
Realized log-
alpha 
2-year dummy 
0.0021 
0.00066 
-0.035 
-0.035 
-0.037 
-0.037* 
 
(0.018) 
(0.016) 
(0.026) 
(0.023) 
(0.023) 
(0.019) 
3-year dummy 
0.011 
0.0018 
-0.062 
-0.062 
-0.071 
-0.071* 
 
(0.031) 
(0.028) 
(0.041) 
(0.041) 
(0.038) 
(0.038) 
4-year dummy 
-0.020 
-0.035 
-0.084* 
-0.084* 
-0.100** 
-0.100** 
 
(0.034) 
(0.032) 
(0.042) 
(0.042) 
(0.042) 
(0.041) 
Observations 
1,466 
1,457 
1,466 
1,466 
1,457 
1,457 
R2 
0.187 
0.156 
0.227 
0.227 
0.205 
0.205 
Fixed effect 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Cluster 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Strip 
Date/Firm 
Date/Strip 
Weight 
None 
None 
None 
None 
None 
None 


---

 
 54 
 
 
 
Panel C: Realizations and firm characteristics 
 
 
 
 
 
 
 
Dependent variable 
Realized 
returns 
Realized log-
returns 
Realized 
alpha 
Realized 
alpha 
Realized log-
alpha 
Realized log-
alpha 
2-year dummy 
0.0011 
-0.0012 
-0.034 
-0.035 
-0.035 
-0.037 
 
(0.019) 
(0.016) 
(0.025) 
(0.025) 
(0.021) 
(0.021) 
3-year dummy 
0.0028 
-0.0065 
-0.069 
-0.069 
-0.077* 
-0.076* 
 
(0.033) 
(0.029) 
(0.041) 
(0.040) 
(0.035) 
(0.035) 
4-year dummy 
-0.022 
-0.038 
-0.086* 
-0.091* 
-0.10* 
-0.11* 
 
(0.035) 
(0.033) 
(0.045) 
(0.046) 
(0.045) 
(0.047) 
Cash-flow duration of firm 
0.0052 
0.010 
0.015 
0.021 
0.020 
0.025** 
(higher = shorter duration) 
(0.015) 
(0.013) 
(0.014) 
(0.013) 
(0.011) 
(0.011) 
Observations 
1,473 
1,464 
1,473 
1,473 
1,464 
1,464 
R2 
0.045 
0.039 
0.064 
0.072 
0.066 
0.069 
Fixed effect 
Date/currency 
Date/currency 
Date/currency 
Date/currency 
Date/currency 
Date/currency 
Cluster 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
Weight 
None 
None 
None 
Notional 
None 
Notional 
 
 
 
 
 
 
 
Panel D: Expectations errors 
 
 
 
 
 
 
Dependent variable 
Realized returns – Expected 
returns  
Realized log-returns – 
Expected log-returns 
 
2-year maturity dummy 
0.0061 
0.0050 
-0.0012 
-0.0032 
 
 
(0.016) 
(0.016) 
(0.012) 
(0.014) 
 
3-year maturity dummy 
0.015 
0.011 
-0.0041 
-0.0059 
 
 
(0.031) 
(0.029) 
(0.029) 
(0.028) 
 
4-year maturity dummy 
-0.0020 
-0.0029 
-0.023 
-0.023 
 
 
(0.031) 
(0.029) 
(0.034) 
(0.032) 
 
Cash-flow duration of firm 
0.017 
0.017 
0.017 
0.018 
 
(higher = shorter duration) 
(0.012) 
(0.012) 
(0.010) 
(0.010) 
 
Observations 
1,065 
1,065 
1,060 
1,060 
 
R2 
0.078 
0.074 
0.074 
0.070 
 
Fixed effect 
Date/currency 
Date/currency 
Date/currency 
Date/currency 
 
Cluster 
Date/Firm 
Date/Firm 
Date/Firm 
Date/Firm 
 
Weight 
None 
Notional 
None 
Notional 
 
 
 
 


---

 
 55 
 
 
Table X 
Alpha Accounting 
This table reports an implied term structure of CAPM alpha and the implied CAPM alpha on long- and short-duration 
firms. We specify a functional form for the term structure of CAPM alphas and calibrate it such that it is consistent 
with the pricing of near-future dividends and such that the market has a CAPM alpha of zero. The table reports the 
average CAPM alpha for different parts of the term structure. It also reports the average weights of the market 
portfolios along these parts, calculated based on the assumption that discount rates are two percentage points higher 
than growth rates in perpetuity. The table also shows the weights and aggregate CAPM alphas for a hypothetical short-
duration firm and a hypothetical long-duration firm. See the text for more details. 
 
 
 
 
 
 
 
 
 
 
 
Maturity of claims (years) 
 
Total 
 
 
1-20 
21-40 
41-60 
61-80 
81-100 
100+ 
 
 
 
Average CAPM alpha 
2.8 
-1.40 
-3.14 
-4.27 
-5.11 
-7.27 
 
 
 
 
 
 
 
 
 
 
 
 
 
Market portfolio: 
 
 
 
 
 
 
 
 
 
Total weight 
0.46 
0.25 
0.14 
0.07 
0.04 
0.05 
 
1 
 
Duration (∑T/U) 
 
 
 
 
 
 
 
33.33 
 
CAPM alpha: (∑V/!/) 
 
 
 
 
 
 
 
0.00 
 
 
 
 
 
 
 
 
 
 
 
Short-duration firm: 
 
 
 
 
 
 
 
 
 
Total weight 
0.71 
0.21 
0.06 
0.02 
0.01 
0.00 
 
1 
 
Duration (∑T/U) 
 
 
 
 
 
 
 
16.7 
 
CAPM alpha: (∑V/!/) 
 
 
 
 
 
 
 
2.11 
 
 
 
 
 
 
 
 
 
 
 
Long-duration firm: 
 
 
 
 
 
 
 
 
 
Total weight 
0.28 
0.21 
0.16 
0.11 
0.08 
0.22 
 
1 
 
Duration (∑T/U) 
 
 
 
 
 
 
 
66.67 
 
CAPM alpha: (∑V/!/) 
 
 
 
 
 
 
 
-2.27 
 
 
 
 
 
 
 
 
 
 
 
 
 


---

 
 56 
 
 
Table XI 
CAPM Alpha on Corporate Bonds 
This table reports CAPM alphas for corporate bond portfolios. We sort firms into two groups based on the median 
firm characteristic. Within each group, we sort all outstanding corporate bonds into portfolios based on maturity. 
Portfolio weights are equal-weighted and rebalanced monthly. We calculate CAPM alpha as the intercept in a time-
series regression of monthly excess portfolio returns on excess market returns. Excess returns are calculated as returns 
in excess of a Treasury claim with the same maturity. The market return is the equal-weighted return across all bonds. 
We report t-statistics below parameter estimates in parentheses and statistical significance is denoted by *** p<0.01, 
** p<0.05, * p<0.1. Alphas are annualized. The sorting is such that the 2-year portfolio, for instance, contains all 
bonds with maturity between one and two years. The sample is U.S. firms from 2002 to 2016. 
 
 
 
Maturity of bonds (in years) 
 
 
 
1 
2 
5 
7 
10 
20 
30 
Average 
Panel A: Duration 
Short-duration firms 
  
0.02*** 
0.01*** 
0.00 
-0.01 
0.00 
-0.02*** 
-0.03* 
-0.01 
 
 
(5.25) 
(2.76) 
(0.71) 
(-1.41) 
(-0.05) 
(-3.10) 
(-1.94) 
 
Long-duration firms 
  
0.03*** 
0.01 
0.00 
-0.01 
-0.01 
-0.03*** 
-0.03 
-0.01 
 
 
(3.75) 
(1.13) 
(-0.63) 
(-1.29) 
(-0.92) 
(-4.09) 
(-1.19) 
 
Average  
 
0.02 
0.01 
0.00 
-0.01 
0.00 
-0.03 
-0.03 
 
 
 
 
 
 
 
 
 
 
 
Panel B: Growth 
Low-LTG firms 
  
0.03*** 
0.01* 
0.00 
-0.01* 
-0.01 
-0.03*** 
-
0.04** 
-0.01 
 
 
(4.27) 
(1.82) 
(0.19) 
(-1.85) 
(-0.91) 
(-3.75) 
(-2.30) 
 
High-LTG firms 
  
0.02*** 
0.01* 
0.00 
0.00 
0.00 
-0.02*** 
-0.03 
0.00 
 
 
(3.53) 
(1.67) 
(-0.25) 
(-1.22) 
(0.06) 
(-3.11) 
(-1.56) 
 
Average  
 
0.03 
0.01 
0.00 
-0.01 
0.00 
-0.02 
-0.04 
 
 
 
 
 
 
 
 
 
 
 
Panel C: Value 
Low BM firms 
  
0.01*** 
0.01 
0.00 
0.00 
0.00 
-0.02*** 
-0.03* 
-0.01 
 
 
(3.53) 
(1.64) 
(0.89) 
(-0.97) 
(-0.02) 
(-3.37) 
(-1.76) 
 
High BM firms 
  
0.03*** 
0.01* 
-0.01 
-0.01** 
-0.01 
-0.03*** 
-
0.04** 
-0.01 
 
 
(3.94) 
(1.75) 
(-0.95) 
(-2.04) 
(-1.21) 
(-3.86) 
(-2.20) 
 
Average 
 
0.02 
0.01 
0.00 
-0.01 
0.00 
-0.03 
-0.04 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 


---

 
 57 
 
 
 
 
Figure 1. The timing and pricing of the cash flows of the major risk factors. 
Panel A shows the relative present value of future dividends for firms in the long and short legs of a duration risk 
factor, which is a combination of the profit, investment, low-risk, and payout factors. All present values are calculated 
using a nominal discount rate of 10%. Standard error bars (±1 SE) are computed using the delta method and the 
procedure in Chen (2017, Appendix A), which accounts for serial correlation and cross-correlation across 
portfolio×maturity using the Driscoll-Kraay estimator with 15 lags. Panel B shows the Capital Asset Pricing Model 
(CAPM) alpha on single-stock dividend strips for firms in the long and short legs of the risk factor. Panel C shows the 
CAPM alpha of corporate bonds for firms in the long and short legs of the risk factor. The samples are 1929 to 2019 
for Panel A, 2010 to 2019 for Panel B, and 2002 to 2016 for Panel C. 
 
 


---

 
 58 
 
 
Panel A: All countries 
 
Panel B: G7 countries 
 
Figure 2. Loadings of expected growth rates on characteristics that predict returns: global 
evidence. 
This figure shows the loading of expected growth rates on characteristics that predict returns. In each country, we 
regress the expected growth rates on the below characteristics in multivariate panel regressions. In almost all cases, 
the characteristics that predict high also returns predict low expected growth.  
 
-0.60
-0.50
-0.40
-0.30
-0.20
-0.10
0.00
0.10
0.20
AUS
AUT
BEL
CAN
CHE
DEU
DNK
ESP
FIN
FRA
GBR
HKG
IRL
ISR
ITA
JPN
NLD
NOR
NZL
PRT
SGP
SWE
USA
High BM
High Profit
Low INV
Low beta
High Payout
-0.60
-0.50
-0.40
-0.30
-0.20
-0.10
0.00
0.10
CAN
DEU
FRA
GBR
ITA
JPN
USA
High BM
High Profit
Low INV
Low beta
High Payout


---

 
 59 
 
 
 
Figure 3. Cumulative return and CAPM alpha to the duration factor. 
This figure shows the cumulative excess return and CAPM alpha to the duration factor. The duration factor is 
constructed as follows. We sort stocks into six portfolios based on ex ante size and duration. The breakpoints are the 
median market capitalization and the 30th and 70th percentiles of duration. Portfolio weights are value-weighted and 
rebalanced monthly and the breakpoints are refreshed each June and based on NYSE firms. The duration factor is long 
50 cents in the two short-duration portfolios and short 50 cents in each of the two long-duration portfolios. The alpha 
is the return to the duration factor minus the product of the duration factor’s market beta and the excess return on the 
market portfolio.  
 
 
 


---

 
 60 
 
 
 
Figure 4. Realized dividend growth rates for long- and short-duration firms. 
This figure shows the realized dividend growth rates for the long and short legs of our duration factor. We sort stocks 
into six portfolios based on ex ante size and duration. The breakpoints are the median market capitalization and the 
30th and 70th percentile of duration. Portfolio weights are value-weighted and rebalanced monthly, and the breakpoints 
are refreshed each June and based on NYSE firms. The figure shows the average cumulative growth rate of the two 
high-duration portfolios per year after the formation period and the average cumulative real growth rate of the two 
low-duration portfolios. The results are based on the 1929 to 2019 U.S. sample. 
 
 
 
 


---

 
 61 
 
 
Panel A: t-statistics on CAPM alpha 
 
 
Panel B: Information Ratio on CAPM alpha in G7 
 
 
Figure 5. Risk-adjusted returns to the duration factor around the world. 
This figure shows the t-statistic for the CAPM alpha to the duration factor in different countries. The duration factor 
is constructed as follows. We sort stocks into six portfolios based on ex ante size and duration. The breakpoints are 
the median market capitalization and the 30th and 70th percentiles of duration. Portfolio weights are value-weighted 
and rebalanced monthly, and the breakpoints are refreshed each June and based on NYSE firms. The duration factor 
is long 50 cents in the two short-duration portfolios and short 50 cents in each of the two long-duration portfolios. The 
alpha is the intercept in a regression of excess returns to the duration factor on the excess return to the market portfolio. 
 
 
 
 
 


---

 
 62 
 
 
 
Figure 6. Single-stock dividend futures: two examples. 
This figure shows the price, open interest, and volume for single-stock dividend futures. The left figure shows the 
future for the 2020 dividend of AXA. Prices are measured in thousands of Euros on the left y-axis, and open interest 
is measured in number of contracts on the right y-axis. Volume, shown in bar charts, is standardized for ease of 
reading. The figure to the right shows similar statistics for the future on the 2020 dividend of Deutsche Bank.   
 
 
0
10000
20000
30000
40000
50000
60000
70000
0
0.2
0.4
0.6
0.8
1
1.2
1.4
1.6
1/17/17
1/17/18
1/17/19
The AXA 2020 Dividend
volume
Price
Open interest
0
5000
10000
15000
20000
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
1/9/17
1/9/18
1/9/19
The Deutsche Bank 2020 Dividend
Volume
Price
open_interest


---

 
 63 
 
 
 
Figure 7. A term structure of implied CAPM alphas. 
This figure shows an implied term structure of CAPM alpha for the first 100 dividend strips. We specify the following 
functional form for CAPM alphas: 
 !X/ = YZ −YG ln U,  
and choose YZ and YG such that the alphas are consistent with the evidence from dividend strips and such that the alpha 
on the market portfolio is equal to zero. The latter is based on assumptions about the weights on future cash flow for 
the market; see the text for details.  
 
 
-8.0
-6.0
-4.0
-2.0
0.0
2.0
4.0
6.0
8.0
10.0
1
4
7
10
13
16
19
22
25
28
31
34
37
40
43
46
49
52
55
58
61
64
67
70
73
76
79
82
85
88
91
94
97
100
Anuualized CAPM alpha
Maturity of dividend (years)


---

 
 64 
 
 
 
 
 
 
Figure 8. Consumption and discount rate risk for duration-sorted portfolios. 
This figure shows covariances between the returns on the duration-sorted portfolios considered in Table 2 and two-
year-ahead cumulative realized consumption growth and market returns. Panel A shows the covariances between each 
portfolio’s realized alpha in quarter t, measured as !-
8 = 6-
8 −&]8 × 6-
%,-, and log real consumption growth (PCE on 
nondurable goods and services, deflated by the CPI) summed t + 1 through t + 8. Panel B shows covariances between 
each portfolio’s raw return in quarter t and the same consumption measure. Panel C shows covariances between each 
portfolio’s raw return in quarter t and cumulative t + 1 through t + 8 market returns. Heteroskedasticity- and 
autocorrelation-robust standard errors (bars ±1 SE) are calculated using the quadratic spectral kernel with 13 lags, 
following the lag selection rule in Lazarus et al. (2018, eq. (22)). The samples are 1947 to 2019 for Panels A and B, 
and 1929 to 2019 for Panel C. 
 
-0.014
-0.012
-0.01
-0.008
-0.006
-0.004
-0.002
0
1
2
3
4
5
6
7
8
9
10
10 - 1
Covariance
Portfolio (1 = short-duration, 10 = long-duration)
Panel C: Raw Return and Two-Year-Ahead Market 
Return
-0.0002
0
0.0002
0.0004
0.0006
1
2
3
4
5
6
7
8
9
10
10 - 1
Portfolio (1 = short-duration, 10 = long-duration)
Panel B: Raw Return and Two-Year-Ahead 
Consumption Growth 
-0.0004
-0.0002
0
0.0002
1
2
3
4
5
6
7
8
9
10
10 - 1
Covariance
Portfolio (1 = short-duration, 10 = long-duration)
Panel A: Realized Alpha and Two-Year-Ahead 
Consumption Growth 
