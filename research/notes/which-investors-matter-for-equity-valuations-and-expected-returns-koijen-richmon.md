---
title: Which Investors Matter for Equity Valuations and Expected Returns? (Koijen,
  Richmond, Yogo, NBER w27402)
id: which-investors-matter-for-equity-valuations-and-expected-returns-koijen-richmon
tags:
- apple-earnings-durability-thesis-b8b3f1
- inelastic-markets
- passive-investing
- demand-system
created: '2026-09-12T17:36:28.245550Z'
updated: '2026-09-15T19:32:22.265609Z'
source: https://doi.org/10.3386/w27402
status: evergreen
type: note
tier: ground_truth
content_type: paper
deprecated: false
summary: 'Demand-system estimate: active-to-passive shift 2007-2016 caused a 14% AGGREGATE
  counterfactual repricing (pooled largest-90%-by-market-cap firms); investor-type
  price elasticities range 0-1 (hedge funds ~0.5, most elastic); no firm-specific/Apple
  elasticity is estimated -- the model is pooled by investor type, not by company
  identity.'
doi: 10.3386/w27402
citation_count: 119
venue: National Bureau of Economic Research
is_retracted: false
---

NBER WORKING PAPER SERIES
WHICH INVESTORS MATTER FOR EQUITY VALUATIONS 
AND EXPECTED RETURNS?
Ralph S. J. Koijen
Robert J. Richmond
Motohiro Yogo
Working Paper 27402
http://www.nber.org/papers/w27402
NATIONAL BUREAU OF ECONOMIC RESEARCH
1050 Massachusetts Avenue
Cambridge, MA 02138
June 2020, Revised September 2023
A previous draft of this paper was titled “Which Investors Matter for Global Equity Valuations 
and Expected Returns?” We thank Han Xu and the Macro Finance Research Program of the 
Becker Friedman Institute at the University of Chicago for computational support. For comments 
and discussions, we thank John Campbell, Christopher Conlon, Kent Daniel, Xavier Gabaix, 
Tarek Hassan, Stefan Nagel, Anna Pavlova, Carolin Pflueger, Stijn Van Nieuwerburgh, and 
seminar participants at Boston College, Columbia University, New York University, Shanghai 
Advanced Institute of Finance, University of Chicago, University of Hong Kong, University of 
Notre Dame, the 2019 Adam Smith Asset Pricing Conference, the 2019 NBER New 
Developments in Long-Term Asset Management Conference, the 2019 NBER Summer Institute 
International Asset Pricing Conference, the 2019 UCLA Conference on Financial Markets, the 
2019 Annual Conference of the Paul Woolley Centre, and the 2020 AFA Annual Meeting. We 
thank Miguel Ferreira and Pedro Matos for discussions on the FactSet data. Koijen acknowledges 
financial support from the Center for Research in Security Prices and the Fama Research Fund at 
the University of Chicago Booth School of Business. The data underlying this article are 
available in Zenodo at https://doi.org/10.5281/zenodo.8192998. The views expressed herein are 
those of the authors and do not necessarily reflect the views of the National Bureau of Economic 
Research.
NBER working papers are circulated for discussion and comment purposes. They have not been 
peer-reviewed or been subject to the review by the NBER Board of Directors that accompanies 
official NBER publications.
© 2020 by Ralph S. J. Koijen, Robert J. Richmond, and Motohiro Yogo. All rights reserved. 
Short sections of text, not to exceed two paragraphs, may be quoted without explicit permission 
provided that full credit, including © notice, is given to the source.

Which Investors Matter for Equity Valuations and Expected Returns?
Ralph S. J. Koijen, Robert J. Richmond, and Motohiro Yogo
NBER Working Paper No. 27402
June 2020, Revised September 2023
JEL No. G1
ABSTRACT
Based on an asset demand system, we develop a framework to quantify the impact of market 
trends and changes in regulation on asset prices, price informativeness, and the wealth 
distribution. Our leading applications are the transition from active to passive investment 
management and climate-induced shifts in asset demand. The transition from active to passive 
investment management had a large impact on equity prices but a small impact on price 
informativeness because capital did not flow from more to less informed investors on average. 
This finding is based on a new measure of investor-level informativeness that identifies which 
investors are more informed about future profitability. Climate-induced shifts in asset demand 
have a potentially large impact on equity prices and the wealth distribution, implying capital 
gains for passive investment advisors, pension funds, insurance companies, and private banking 
and capital losses for active investment advisors and hedge funds.
Ralph S. J. Koijen
University of Chicago
Booth School of Business
5807 S Woodlawn Ave
Chicago, IL 60637
and NBER
Ralph.koijen@chicagobooth.edu
Robert J. Richmond
Stern School of Business
New York University
44 W. 4th Street, 9-81
New York, NY 10012
and NBER
rrichmon@stern.nyu.edu
Motohiro Yogo
Department of Economics
Princeton University
Julis Romo Rabinowitz Building
Princeton, NJ 08544
and NBER
myogo@princeton.edu

1.
Introduction
Many questions in ﬁnancial economics with policy relevance require an understanding of
how capital ﬂows across investors and how shifts in asset demand for a group of investors
aﬀect asset prices, price informativeness (i.e., the information content of asset prices), and
the wealth distribution across investors. For example, how does the transition from active
to passive investment management aﬀect the cross section of equity prices and expected
returns? Do equity prices become less informative when passive investors own a larger share
of the market? How do climate-induced shifts in asset demand in response to sustainable
investing or changes in climate regulation aﬀect the cross section of equity prices and the
ﬁrms’ cost of capital? How do these capital ﬂows and shifts in asset demand aﬀect the wealth
distribution across institutional investors and thereby ﬁnancial stability?
We develop a new framework to quantify the impact of market trends and changes in
regulation on asset prices, price informativeness, and the wealth distribution. We apply the
framework to study the transition from active to passive investment management, climate-
induced shifts in asset demand, and the relative importance of institutional investors for
cross-sectional asset pricing. An asset demand system, which has become a practical re-
ality due to the availability of portfolio holdings data and recent progress on longstanding
identiﬁcation challenges, plays a central role in quantifying the impact of market trends and
changes in regulation for four reasons.
First, we use an asset demand system to estimate how portfolio holdings respond to
asset prices and ﬁrm characteristics. For example, we can observe that a hedge fund tilts
its portfolio toward browner stocks, but this reduced-form relation does not tell us whether
the hedge fund is simply responding to browner stocks being less expensive (i.e., lower book-
to-market equity) or considers the fundamentals of browner stocks to be relatively strong
(i.e., higher proﬁtability or lower risk). To separate these eﬀects, we estimate the elasticities
of demand to asset prices and ﬁrm characteristics at the investor level. Second, with this
separation in hand, we use the asset demand system to model market trends and changes in
regulation as capital ﬂows across investors or shifts in asset demand. For example, we model
the trend toward sustainable investing as a shift in asset demand toward greener stocks (i.e.,
an increase in the elasticity of demand to the environmental score). Third, following capital
ﬂows across investors or shifts in asset demand, market clearing implies counterfactual asset
prices such that supply is equal to the aggregate demand across all investors. The asset
demand system fully accounts for substitution eﬀects. For example, if investors other than
hedge funds increase their demand for greener stocks (i.e., a shift in the demand curve), the
equilibrium prices of greener stocks increase, and hedge funds substitute toward browner
2

stocks to accommodate the other investors’ demand. Fourth, as market trends and changes
in regulation aﬀect asset prices, we use the asset demand system to measure their impact
on other important statistics that depend on asset prices, such as price informativeness
and the wealth distribution. These four reasons combined explain why an asset demand
system is necessary for quantitative answers to questions that cannot be credibly answered
by reduced-form analysis.
We start with a simple asset pricing model that illustrates the framework. Investors have
heterogeneous beliefs or sentiment about future proﬁtability and agree to disagree. Investors
believe that expected proﬁtability and proﬁtability risk depend on observed characteristics
and unobserved (to the econometrician) characteristics that we call latent demand. Latent
demand could also arise from investor sentiment (e.g., Barberis et al., 1998) or portfolio
constraints (e.g., Brunnermeier and Pedersen, 2009) that are not easily modeled as a function
of observed characteristics. Thus, optimal portfolio choice implies that asset demand is a
linear function of asset prices, ﬁrm characteristics, and latent demand.
Market clearing
implies that asset prices are a linear function of ﬁrm characteristics and the weighted average
of latent demand, where the slopes on ﬁrm characteristics are weighted averages of the
investors’ demand elasticities. The model delivers three insights. First, capital ﬂows change
asset prices by changing the relative importance of investors in the weighted average. Second,
asset prices change when the elasticities of demand to ﬁrm characteristics respond to market
trends and changes in regulation. Third, the degree to which capital ﬂows and shifts in
asset demand aﬀect asset prices depends on heterogeneity in asset demand and demand
elasticities.
We estimate the asset demand system by instrumental variables using quarterly US in-
stitutional holdings data from 2000 to 2019. The estimated demand system reveals rich
heterogeneity across institutional investors, even conditional on investor type and wealth.1
For example, the wealth-weighted semi-elasticity of demand to the environmental score is
2.82% for small-passive investment advisors and −1.56% for hedge funds per one standard
deviation change in the environmental score.2 That is, for small-passive investment advi-
sors, an equity holding changes by 2.82% per one standard deviation change in the ﬁrm’s
environmental score. The price elasticity of demand is low on average and varies from zero
to one across investors. Even hedge funds, which are the most elastic among institutional
1We group institutional investors into investment advisors (including mutual funds), hedge funds, long-
term investors (i.e., pension funds and insurance companies), private banking, and brokers. We further
split investment advisors by wealth and the active share into large-passive, small-passive, large-active, and
small-active.
2The environmental scores are from Sustainalytics (Morningstar, 2020). The environmental scores are
industry adjusted, reﬂecting diﬀerences in environmental risk across ﬁrms within an industry.
3

investors, have a wealth-weighted price elasticity of demand around 0.5. Thus, we agree with
a recent literature, which builds on an earlier literature on index eﬀects (Harris and Gurel,
1986; Shleifer, 1986), that ﬁnds price elasticities of demand that are much lower than those
predicted by traditional asset pricing models (Chang et al., 2014; Koijen and Yogo, 2019;
Pavlova and Sikorskaya, 2022).
Based on the estimated demand system, we answer two questions of current policy inter-
est. The ﬁrst question is how the transition from active to passive investment management
aﬀects the cross section of equity prices and price informativeness. We start by documenting
two key facts. First, the aggregate active share of institutional investors declined from 38.9%
in 2007.Q4 to 32.8% in 2016.Q4, which is a similar rate to a longer decline from 46.6% in
1980.Q4 to 31.7% in 2017.Q4. Second, the capital ﬂows from active to passive investors,
rather than the investment strategies becoming more passive, explain most of the decline
in the aggregate active share from 2007 to 2016. Based on these facts, we compute coun-
terfactual equity prices in 2016 if the wealth distribution across institutional investors were
to remain the same as that in 2007. Equity prices change as the active investors’ portfolio
strategies become more inﬂuential in the counterfactual market. The value-weighted absolute
percent change in equity prices, which we call equity repricing throughout the paper, is quite
large at 14%. However, the transition from active to passive investment management has
little impact on price informativeness, as measured by a cross-sectional regression of future
proﬁtability on market-to-book equity (Bai et al., 2016). To explain this ﬁnding, we develop
a new measure of investor-level informativeness that identiﬁes which institutional investors
are more informed about future proﬁtability. The intuition is that a more informed investor
has demand shifters, which are outputs of the demand estimation, that predict future prof-
itability in the cross section of its equity holdings. Using the investor-level informativeness,
we ﬁnd that capital did not ﬂow from more to less informed investors on average, which
explains the small impact on price informativeness.
The second question is how climate-induced shifts in asset demand due to sustainable
investing or changes in climate regulation aﬀect equity prices.
Such shifts could change
the wealth distribution across institutional investors and ultimately aﬀect ﬁnancial stability.
Thus, the framework has potential policy relevance as a basis for implementing climate
stress tests. Based on a survey by Stroebel and Wurgler (2021), we focus on stakeholder risk
(i.e., changing preferences of customers and employees) and regulatory risk as the primary
sources of risk at the ﬁve-year horizon. We model realized stakeholder risk as an increase in
the elasticity of demand to the environmental score for all institutional investors. Because
of initial heterogeneity in the portfolio strategies along the environmental score, realized
stakeholder risk has a large impact on the wealth distribution across institutional investors.
4

On the one hand, passive investment advisors, pension funds, insurance companies, and
private banking earn capital gains.
On the other hand, active investment advisors and
hedge funds earn capital losses. In contrast to realized stakeholder risk, realized regulatory
risk that aﬀects only pension funds and insurance companies has a small impact on equity
prices and the wealth distribution.
Building on the two policy-relevant applications, we use the asset demand system to
study the relative importance of institutional investors for cross-sectional asset pricing. A
longstanding question in ﬁnancial economics is why ﬁrm characteristics are priced in the
cross section of equity valuations and expected returns (e.g., Fama and French, 1995; Daniel
and Titman, 2006; Campbell et al., 2010). Asset pricing theory tells us that ﬁrm charac-
teristics relate to diﬀerences in beliefs or sentiment about future proﬁtability, and we use
the asset demand system to infer these beliefs from investor portfolios. Analogous to the
ﬁrst application of the transition from active to passive investment management, we com-
pute counterfactual equity prices in response to capital ﬂows from a group of investors to
other institutional investors. Relative to their size, hedge funds play an outsized role with
equity repricing of $3.58 per dollar of wealth, followed by small-active investment advisors
with equity repricing of $2.28 per dollar of wealth. The magnitude of the equity repricing
depends on two factors. First, the equity repricing is larger for capital ﬂows from investors
who have asset demand that is more diﬀerent from the other investors. Second, the equity
repricing is larger for capital ﬂows from investors who are relatively price elastic because the
outﬂow faces relatively inelastic demand, resulting in a higher price impact. In terms of the
relation between market-to-book equity and ﬁrm characteristics, a notable ﬁnding is that
small-active investment advisors and foreign investors have opposite eﬀects on the pricing of
the environmental score. On the one hand, the cross-sectional slope between market-to-book
equity and the environmental score would steepen in the absence of small-active investment
advisors. On the other hand, the cross-sectional slope would ﬂatten in the absence of foreign
investors.
An older literature estimated asset demand systems on sector-level portfolio holdings
(Brainard and Tobin, 1968) and inferred the importance of heterogeneous expectations for
asset prices (Friedman, 1977, 1978). Building on this tradition, Koijen and Yogo (2019)
developed demand system asset pricing as a systematic approach to studying asset prices
using portfolio holdings data. Relative to this literature, our contribution is to develop a new
framework to quantify the impact of market trends and changes in regulation. Along the
way, we make four methodological contributions. First, we endogenize the investors’ wealth
in counterfactual analysis to study the wealth distribution. Second, we incorporate price
informativeness as a policy-relevant outcome and develop a measure of investor-level infor-
5

mativeness to understand the mechanism behind the counterfactual analysis. The investor-
level informativeness identiﬁes which investors are more informed about future proﬁtability
and could have broader application in studying price discovery and market eﬃciency. Third,
we develop an instrumental variables ridge estimator to estimate asset demand for investors
with concentrated portfolios. This estimator allows for more heterogeneity in asset demand,
which is important for the quantitative results.
Fourth, we improve the classiﬁcation of
investor types and separate hedge funds, which play an important role in our analysis.
2.
Asset pricing model
We develop an asset pricing model that illustrates how we use an asset demand system to
quantify the impact of market trends and changes in regulation. The model delivers three
insights.
First, capital ﬂows change asset prices by changing the relative importance of
investors. Second, asset prices change when the elasticities of demand to ﬁrm characteristics
respond to market trends and changes in regulation. Third, the degree to which capital ﬂows
and shifts in asset demand aﬀect asset prices depends on heterogeneity in asset demand and
demand elasticities. We use the model to explain the applications in the subsequent sections.
The model is static and intentionally stylized to focus on the core economic mechanisms. We
leave extensions, such as a dynamic model of portfolio choice with income shocks or liquidity
eﬀects, for future research.
We present the assumptions and the results in this section and leave all derivations for
Appendix A. To summarize the notation, we denote vectors and matrices in bold and index
their elements in parentheses (e.g., x(n) is the nth element of the vector x). We denote an
identity matrix as I. We use the subscript 1 to denote all variables in period 1 and omit the
subscript for all variables in period 0.
2.1.
Financial market
There are two periods indexed by t = 0, 1. There are N stocks, indexed by n = 1, . . . , N, with
the supply of each stock normalized to one. There is also a riskless asset in perfectly elastic
supply with a constant interest rate normalized to zero. Let P be an N-dimensional vector
of equity prices in period 0. Because the supply is normalized to one, P is also the vector
of market equity in period 0. Let B be an N-dimensional vector of book equity in period
0. Let D1 be an N-dimensional vector of terminal dividends in period 1. For each stock
n, we deﬁne market-to-book equity in period 0 as MB(n) = P(n)/B(n) and proﬁtability
in period 1 as d1(n) = D1(n)/B(n).
Thus, the N-dimensional vectors corresponding to
market-to-book equity and proﬁtability are respectively MB and d1.
6

2.2.
Portfolio-choice problem
There are I investors indexed by i = 1, . . . , I. The investors choose an optimal portfolio in
period 0 and receive the dividends in period 1. Let qi(n) be the number of shares of stock n
that investor i holds in period 0. Equivalently, we express the investor’s holdings of stock n
in units of book equity as Qi(n) = B(n)qi(n). Let Oi be the dollar investment in the riskless
asset. Thus, the investor’s wealth in period 0 is
Ai =P ′qi + Oi
=MB′Qi + Oi.
The investor’s wealth in period 1 is
Ai,1 =Ai + (D1 −P )′qi
=Ai + (d1 −MB)′Qi.
(1)
Investors choose an optimal portfolio in period 0 to maximize expected constant absolute
risk aversion (CARA) utility over wealth in period 1:
max
Qi
Ei[−exp(−γiAi,1)].
(2)
Investors have heterogeneous coeﬃcients of absolute risk aversion, which we parameterize as
γi = 1/(τiAi). This assumption delivers the desirable implications of a constant relative risk
aversion model while maintaining the tractability of a CARA-normal model (Makarov and
Schornick, 2010). As the subscript i on the expectations operator denotes, investors have
heterogeneous beliefs or sentiment about future proﬁtability. We assume that the investors
agree to disagree.
2.2.1.
Heterogeneous beliefs about proﬁtability
We model investor i’s beliefs about future proﬁtability through a factor model:
d1 = μi + ρiF1 + η1.
The vector μi represents the investor’s beliefs about expected proﬁtability.
The vector
ρi represents the investor’s beliefs about exposure to a systematic factor F1, which is a
standard normal random variable. The vector η1 is a normally distributed idiosyncratic
shock (i.e., uncorrelated with the factor) with a mean of zero and a diagonal covariance
7

matrix Var(η) = σ2I. We assume constant idiosyncratic variance across stocks to simplify
notation.
Investors form expectations based on ﬁrm characteristics, which are public information.
We denote a vector of observed characteristics of stock n as x(n). We order the ﬁrm charac-
teristics so that the ﬁrst element is book equity and the last element is a constant. Investor
i’s beliefs about expected proﬁtability of stock n depend on its observed characteristics and
an unobserved (to the econometrician) characteristic φμ
i (n) as
μi(n) = Φμ′
i x(n) + φμ
i (n),
(3)
where Φμ
i is a vector of coeﬃcients on ﬁrm characteristics. Similarly, beliefs about factor
exposure of stock n depend on its observed characteristics and an unobserved characteristic
φρ
i (n) as
ρi(n) = Φρ′
i x(n) + φρ
i (n),
(4)
where Φρ
i is a vector of coeﬃcients on ﬁrm characteristics. In the spirit of asset pricing
in an endowment economy (Lucas, 1978), we assume that both observed and unobserved
characteristics are exogenous.
2.2.2.
Optimal portfolio choice
As we show in Appendix A, investor i’s optimal demand for stock n is
Qi(n) =
1
γiσ2
⎛
⎜
⎝−MB(n) + (Φμ
i −ciΦρ
i



βi
)′x(n) + φμ
i (n) −ciφρ
i (n)



ϵi(n)
⎞
⎟
⎠,
(5)
where ci is a scalar that does not vary across stocks. The ﬁrst term in equation (5) implies
that asset demand is downward sloping and decreasing in market-to-book equity. The second
term in equation (5) implies that asset demand increases in observed characteristics that
relate to higher expected proﬁtability or lower risk. However, the expression for βi shows
that the relation between asset demand and observed characteristics does not reveal whether
an investor tilts toward a particular characteristic because of expected proﬁtability, risk,
or sentiment.
We refer to the last term in equation (5) as latent demand because it is
unobserved to the econometrician. Again, the relation between asset demand and unobserved
characteristics could arise from expected proﬁtability, risk, or sentiment.
Equation (5) is an asset demand function that relates the cross section of equity hold-
8

ings to ﬁrm characteristics.
Equation (5) implies that investors with heterogeneous risk
preferences and beliefs could have diﬀerent elasticities of demand to equity prices and ﬁrm
characteristics. Asset demand is less price elastic for investors with higher risk aversion γi.
Asset demand is more elastic to the environmental score for investors with stronger beliefs
about the impact of climate change on expected proﬁtability or risk.
Equation (5) could arise from microfoundations other than heterogeneous beliefs.
In
Appendix A, we extend the model to background risk, such as income that is correlated
with climate risk. Alternatively, investors could have direct tastes for ﬁrm characteristics
(Fama and French, 2007), such as nonpecuniary beneﬁts that arise from investing in greener
ﬁrms (P´astor et al., 2021; Pedersen et al., 2021). Portfolio holdings data are not suﬃcient
to disentangle whether the demand for a particular characteristic arises from beliefs or sen-
timent about future proﬁtability, hedging motives, or nonpecuniary beneﬁts. Survey data
are promising for making progress on this issue (Krueger et al., 2020; Bauer et al., 2021).
2.3.
Equilibrium equity prices
Market clearing for each stock n is
B(n) =
I

i=1
Qi(n).
(6)
That is, supply is equal to the aggregate demand across all investors. Let e1 be a vector with
the ﬁrst element equal to one and the other elements equal to zero, so that e′
1x(n) = B(n)
(i.e., the ﬁrst element of x(n) is book equity). Substituting optimal demand (5) in market
clearing (6), we solve for the equilibrium equity prices as
MB(n) = β
′x(n) + ϵ(n),
(7)
where
β =
I

i=1
aiβi −
σ2e1

I
i=1 τiAi
,
ϵ(n) =
I

i=1
aiϵi(n),
ai =
τiAi

I
j=1 τjAj
.
Equation (7) establishes a cross-sectional relation between market-to-book equity and
9

ﬁrm characteristics. The vector β is a weighted average of the coeﬃcients on ﬁrm character-
istics in asset demand (5). Investors with larger βi have more extreme beliefs or sentiment
about future proﬁtability based on ﬁrm characteristics and consequently have a larger impact
on equity prices. The scalar ϵ(n) is a weighted average of latent demand across investors.
Investors with larger latent demand have a larger impact on equity prices.
Investor i is more inﬂuential for equity prices if its relative weight ai is larger.
The
relative weight depends on three factors. First, the relative weight increases in wealth Ai.
Second, the relative weight increases in the risk tolerance τi because the investor trades more
aggressively along its beliefs. Third, the relative weight increases if the other investors have
lower risk tolerance. This eﬀect arises from the fact that the investor faces a less elastic
demand curve on its trades, which results in a larger price impact.
By equation (1), the deﬁnition of return on stock n is R1(n) = d1(n) −MB(n). Taking
the expectation and rearranging, we have
MB(n) =E[d1(n)] −E[R1(n)]
=β
′x(n) + ϵ(n).
The ﬁrst line is a present-value formula. A high market-to-book equity signals either high
expected proﬁtability or low expected returns.
The second line, which repeats equation
(7), states that market-to-book equity is a linear combination of ﬁrm characteristics and
the weighted average of latent demand in period 0.
Combining the two lines, the same
characteristics that explain market-to-book equity predict either future proﬁtability or stock
returns. We will test this implication of the model in Section 3.
2.4.
Applications of the asset demand system
In Section 5, we estimate asset demand for all institutional investors and households. We
then use the estimated demand system to quantify the impact of capital ﬂows and shifts
in asset demand on equity prices, price informativeness, and the wealth distribution. We
describe the applications in the context of the simple asset pricing model in this section.
2.4.1.
Capital ﬂows across investors
According to equation (7), market-to-book equity depends on β, the weighted average of
the coeﬃcients on ﬁrm characteristics, and ϵ(n), the weighted average of latent demand.
Investors with more wealth are more important in the weighted average. Therefore, equity
prices change when capital ﬂows across investors change the wealth distribution. A stock
becomes more expensive if it has characteristics or latent demand that are more highly valued
10

by investors who become larger. In Section 6, we study capital ﬂows from active to passive
investors. In Section 8, we study capital ﬂows across diﬀerent types of institutional investors.
The capital ﬂows from active to passive investors could also aﬀect price informativeness.
Let E1(n) be future earnings before interest and taxes. Bai et al. (2016) deﬁne price in-
formativeness based on a cross-sectional regression of future proﬁtability on market-to-book
equity:
E1(n)
B(n) =α + πMB(n) + ν1(n)
=α + π
I

i=1
ai(β′
ix(n) + ϵi(n)) −
πσ2

I
i=1 τiAi
B(n) + ν1(n).
(8)
The regression coeﬃcient π measures price informativeness, where a higher coeﬃcient implies
that equity prices are more informative. The second line of equation (8) follows from equation
(7).
Equation (8) shows why the asset demand system is important for understanding price
informativeness. Investor i’s demand shifters β′
ix(n) + ϵi(n) vary across stocks, reﬂecting
beliefs or sentiment about future proﬁtability. A more informed investor has demand shifters
that predict future proﬁtability in the cross section of its equity holdings. Therefore, the
capital ﬂows from active to passive investors could decrease price informativeness if passive
investors have less informative demand shifters. This insight leads to a measure of investor-
level informativeness to understand the mechanism through which the capital ﬂows aﬀect
price informativeness. We estimate the demand shifters based on the ﬁrm characteristics, the
estimated demand coeﬃcients, and latent demand. We then estimate price informativeness
for each investor through a cross-sectional regression of future proﬁtability on the demand
shifters. The investor-level regression coeﬃcients identify which investors are more informed
about future proﬁtability.
2.4.2.
Shifts in asset demand
In Section 7, we quantify the impact of climate-induced shifts in asset demand. We model
realized stakeholder risk as an increase in the coeﬃcient on the environmental score in equa-
tion (5) from βi(k) to βi(k) + Δi, where Δi > 0 for all institutional investors and Δi = 0
for the household sector. We model realized regulatory risk as an increase in the coeﬃ-
cient on the environmental score for only pension funds and insurance companies. Then
equation (7) implies that the cross-sectional slope between market-to-book equity and the
environmental score increases from β(k) to β(k) + 
I
i=1 aiΔi. That is, market-to-book eq-
11

uity increases for greener stocks and decreases for browner stocks. The linearity of the asset
pricing model implies no impact on the cross-sectional slope between market-to-book equity
and ﬁrm characteristics other than the environmental score.
These counterfactuals also have implications for the wealth distribution. Investors with
diﬀerent initial portfolios have diﬀerent capital gains when equity prices change. For example,
investors with an initial tilt toward greener stocks have higher capital gains than those with
an initial tilt toward browner stocks. Depending on the particular investors who are aﬀected,
such shifts in the wealth distribution could aﬀect ﬁnancial stability. Thus, the framework
has potential policy relevance as a basis for implementing climate stress tests.
2.5.
Extension to endogenous characteristics
Our baseline model assumes that ﬁrm characteristics are exogenous. This assumption may
be reasonable for ﬁrm characteristics that primarily relate to productivity and market power.
However, it may be too strong for ﬁrm characteristics that relate to policies that could depend
on equity prices, such as capital structure or payout policy. In Appendix A.3, we extend the
model to allow the ﬁrm characteristics to depend on market-to-book equity. The extended
model has an important implication for the identiﬁcation of asset demand, as we discuss in
Appendix D.3.
3.
Stock market data and motivating facts
We construct US stock market data on institutional equity holdings, equity prices, and ﬁrm
characteristics. We summarize the essential elements of the data construction and leave the
details for Appendix B.
3.1.
Institutional equity holdings
Data on quarterly US institutional equity holdings from 2000.Q1 to 2019.Q4, based on
Securities and Exchange Commission (SEC) Form 13F ﬁlings, and shares outstanding are
from FactSet Ownership (FactSet, 2020). We group institutional investors into investment
advisors (including mutual funds), hedge funds, long-term investors (i.e., pension funds and
insurance companies), private banking, and brokers.3
Because investment advisors are a
large group, we further split them into four subgroups: large-passive, small-passive, small-
active, and large-active. At each date, we ﬁrst split the investment advisors into two groups
by wealth (i.e., total equity holdings), so that the total wealth is equal across the groups.
3Private banking includes private banking and wealth management, family oﬃces, private equity, and
venture capital.
12

Within each wealth group, we split the investment advisors into two groups at the median
of the active share, which is the total share of the investor’s portfolio that deviates from the
market weights (Cremers and Petajisto, 2009). The active share is one-half times the sum of
the absolute diﬀerences between the portfolio weights and the market weights over the set
of stocks that are in the investor’s investment universe.
We construct the household sector as shares outstanding minus the sum of institutional
holdings. In rare cases, the sum of institutional holdings exceeds shares outstanding because
SEC Form 13F does not report short positions and may contain reporting errors (Lewellen,
2011). If the sum of institutional holdings exceed shares outstanding, we rescale all institu-
tional holdings proportionally to add up to shares outstanding.4
We identify foreign investors based on the investors’ domicile reported by FactSet. For
some of our analysis, we tabulate foreign investors separately to study whether they behave
diﬀerently from domestic investors. For example, Norges Bank Investment Management is a
long-term investor but also a foreign investor. Therefore, we include Norges Bank Investment
Management in the tabulation for long-term investors as well as an additional tabulation for
foreign investors.
Table 1 provides a perspective on the range of institutional investors by listing the largest
investor by investor type. The largest passive investment advisor is Vanguard, managing
$2,494 billion in 2019.Q4. The largest hedge fund is Renaissance Technologies, managing $89
billion in 2019.Q4. As documented in the literature, institutional ownership is concentrated
among a small group of large investors (Gompers and Metrick, 2001), and this concentration
has increased over time (Ben-David et al., 2021).
Figure 1 reports the ownership shares by investor type from 2000.Q1 to 2019.Q4. The
institutional ownership share has increased over time. Part of this trend is due to a ﬁxed re-
porting threshold of $100 million in total 13(f) securities, which implies increased coverage of
institutional ownership over time. Passive investors account for a large share of institutional
ownership, which has important asset pricing implications as we discuss in Section 6.
3.2.
Sample of ﬁrms
Our sample consists of US ﬁrms with ordinary common shares that trade on the New York
Stock Exchange, the American Stock Exchange, or Nasdaq. Table 2 reports summary statis-
tics by deciles of market equity. In 2019.Q4, the largest 57 ﬁrms alone accounted for 50%
of total market equity. The largest 541 ﬁrms that accounted for 90% of total market equity
cover 81% of total sales and 88% of total earnings before interest and taxes. That is, market
4Our data construction implies that we estimate asset demand for institutional investors on long positions
only, and the short positions of institutional investors are aggregated with the household sector.
13

equity and earnings are even more concentrated than sales. A comparison of 2000.Q1 and
2019.Q4 shows that the market concentration has increased among the largest 90% of ﬁrms
by market equity.
We study the equity prices of the largest 90% of ﬁrms by market equity, which capture
most of the economic activity among publicly traded ﬁrms. In modeling the asset demand
system in Section 4, the largest 90% of ﬁrms are the inside assets. We aggregate the remaining
10% of ﬁrms into an outside asset. This treatment ensures that our estimates of the asset
demand system are based on the largest and most liquid stocks (Asness et al., 2013).
3.3.
Equity prices and ﬁrm characteristics
Data on equity prices, shares outstanding, and market equity are from FactSet Ownership
(FactSet, 2020).5 Data on ﬁnancial statements are from Compustat Fundamentals (S&P
Global, 2020). Data on stock returns are from the CRSP US Stock Database (Center for
Research in Security Prices, 2020). Guided by the asset pricing model in Section 2, we model
expected proﬁtability and proﬁtability risk as a function of ﬁrm characteristics. We focus on
eight characteristics in the baseline speciﬁcation of asset demand: the environmental score,
the governance index, log book equity, the foreign sales share, the Lerner index, the ratio of
sales to book equity, the ratio of dividends to book equity, and market beta.
The environmental scores are from Sustainalytics (Morningstar, 2020).
The environ-
mental scores are industry adjusted, reﬂecting diﬀerences in environmental risk across ﬁrms
within an industry. The environmental scores from Sustainalytics do not necessarily have
high correlation with those from other environmental rating agencies. However, Sustaina-
lytics is an important driver of mutual fund ﬂows (Hartzmark and Sussman, 2019).
Following Bebchuk et al. (2009), we construct the governance index as the total number
of entrenchment provisions among six that include staggered boards, limits to shareholder
bylaw amendments, poison pills, golden parachutes, supermajority requirements for mergers,
and supermajority requirements for charter amendments. The entrenchment provisions are
from the Governance Database (Institutional Shareholder Services, 2020). Bebchuk et al.
(2009) ﬁnd that these entrenchment provisions matter for equity valuations among the 24
governance provisions that Gompers et al. (2003) studied. A higher governance index means
that the ﬁrm is more entrenched and has weaker governance.
Log book equity captures ﬁrm size. The foreign sales share relates to productivity since
the most productive ﬁrms export their goods (Melitz, 2003). The Lerner index, which is the
ratio of operating income after depreciation to sales, is a measure of proﬁtability that relates
5We use FactSet instead of CRSP to more easily align the institutional holdings and shares outstanding
with respect to stock splits.
14

to market power (e.g., Guti´errez and Philippon, 2017). We use the market beta as a measure
of risk, estimated from a 60-month rolling regression of excess stock returns on the excess
market returns. A combination of ﬁrm characteristics could capture other characteristics
that are not directly in our speciﬁcation. For example, the combination of proﬁtability (i.e.,
the Lerner index), investment, market beta, and payout (i.e., the ratio of dividends to book
equity) captures the duration of cash ﬂows (Gormsen and Lazarus, 2023).
The sample period is 2000 to 2019. For part of the analysis that requires the environmen-
tal score or the governance index, we focus on a shorter sample from 2010 to 2019. For stocks
that do not have an environmental score or a governance index, we construct an indicator
variable that is equal to one if the corresponding variable is missing. We standardize all
characteristics within each year to simplify the interpretation of the regression coeﬃcients.
3.4.
Relation between equity valuations and ﬁrm characteristics
An important issue in estimating the asset demand system is the choice of ﬁrm characteristics.
The asset pricing model in Section 2 gives us guidance. According to equation (7), ﬁrm
characteristics that enter asset demand have explanatory power for the cross section of
market-to-book equity.
Therefore, we estimate a panel regression of log market-to-book
equity on the eight characteristics in the baseline speciﬁcation:
mbt(n) = αt + β
′xt(n) + ϵt(n),
where αt are year ﬁxed eﬀects.6 Table 3 reports the regression coeﬃcients for the baseline
speciﬁcation in an annual sample from 2010 to 2019. It also reports the regression coeﬃcients
for a speciﬁcation without the environmental score or the governance index in a longer sample
from 2000 to 2019.
The eight characteristics in the baseline speciﬁcation explain most of the cross-sectional
variation in market-to-book equity.
The adjusted within R2 is 64%, which excludes the
explanatory power of the year ﬁxed eﬀects.
The fact that a relatively small number of
ﬁrm characteristics have explanatory power for the cross section of market-to-book equity is
consistent with Asness et al. (2019). Market-to-book equity increases in the environmental
score and decreases in the governance index (i.e., less entrenchment). A standard deviation
increase in the environmental score implies a 17% increase in market-to-book equity.
A
6We estimate this regression by ordinary least squares under the maintained assumption that the ﬁrm
characteristics are exogenous. However, we extend the framework to allow for endogenous characteristics
that could respond to equity prices in Appendix D.3. Furthermore, the literature on sustainable investing
and corporate governance suggests instruments for these characteristics, which could apply to our context
as well.
15

standard deviation decrease in the governance index implies a 10% increase in market-to-
book equity.
The negative coeﬃcient on log book equity means that smaller ﬁrms have
higher market-to-book equity. The positive coeﬃcients on the foreign sales share and the
Lerner index mean that more productive and proﬁtable ﬁrms have higher market-to-book
equity.
In Table D1 of Appendix D, we test the robustness of the baseline speciﬁcation by adding
three characteristics: investment, the ratio of net repurchases to book equity, and earnings
surprises. These characteristics are known to be strong predictors of stock returns (Daniel
et al., 2020). We ﬁnd that the adjusted within R2 increases only modestly from 64% to 68%.
The fact that the additional characteristics do not signiﬁcantly increase explanatory power
further supports the baseline speciﬁcation with eight characteristics in the asset demand
system.
3.5.
Relation between proﬁtability and ﬁrm characteristics
As we discussed in Section 2, the same characteristics that explain market-to-book equity
predict either future proﬁtability or stock returns. Let et+1,t+5(n) be ﬁve-year proﬁtability
for stock n from year t + 1 to t + 5, which we deﬁne in Appendix B. We estimate a panel
regression of future proﬁtability on the eight characteristics in the baseline speciﬁcation:
et+1,t+5(n) = αt + π′xt(n) + νt+5(n),
where αt are year ﬁxed eﬀects. In Table 3, we ﬁnd that the ﬁrm characteristics have sig-
niﬁcant explanatory power for future proﬁtability with an adjusted within R2 of 49%. The
regression coeﬃcients have the same sign and similar magnitude to those for market-to-book
equity. This ﬁnding supports the assumption in equation (3) that expected proﬁtability is
a function of ﬁrm characteristics. Nevertheless, we caution that expected proﬁtability is
challenging to estimate accurately in a short panel.
In Section 8, we use equation (7) to decompose the relative importance of institutional
investors for the cross section of market-to-book equity. We also show that the same decom-
position has immediate implications for the cross section of expected returns.
4.
An empirically tractable asset demand system
The linear demand system in Section 2 is highly tractable for obtaining closed-form solutions
for equity prices. For estimation, we use a corresponding logit demand system because the
portfolio holdings data are much closer to a lognormal distribution. The logit demand sys-
16

tem corresponds to optimal portfolio choice under expected log utility, following a derivation
analogous to that for the linear demand system in Section 2 (Koijen and Yogo, 2019). By
market clearing, the logit demand system implies a unique solution for equity prices, analo-
gous to equation (7). The only diﬀerence is that the solution is numerical instead of closed
form.
4.1.
Investment universe
Following the same notation as Section 2, there are N inside assets indexed by n = 1, . . . , N.
In addition, there is an outside asset n = 0 that consists of micro-cap stocks, as we described
in Section 3. There are I investors indexed by i = 1, . . . , I. Investor i = 1 is households,
which is a residual sector that holds all remaining shares that are not held by the institutional
investors.
Each investor i allocates wealth Ai,t in period t across its investment universe Ni,t ⊆
{1, . . . , N} and the outside asset. The investment universe is a subset of stocks that an
investor is allowed to hold, determined by its investment mandate or benchmarking. For
example, an S&P 500 index fund is only allowed to hold stocks in the index. Alternatively,
the investment universe could arise from informational frictions that limit an investor’s choice
set to a subset of stocks (Merton, 1987).
4.2.
Asset demand
Based on equation (5), we model asset demand to be loglinear in ﬁrm characteristics. Investor
i’s portfolio weight on stock n ∈Ni,t in period t is
wi,t(n) =
δi,t(n)
1 + 
m∈Ni,t δi,t(m),
(9)
where
δi,t(n) = exp(αi,t + β0,i,tmbt(n) + β′
1,i,txt(n))ϵi,t(n).
(10)
The portfolio weight depends on investor-time ﬁxed eﬀects αi,t, log market-to-book equity
mbt(n), a vector of observed characteristics xt(n), and latent demand ϵi,t(n). The portfolio
weights inclusive of the outside asset add up to one. Thus, the portfolio weight on the outside
asset is
wi,t(0) = 1 −

n∈Ni,t
wi,t(n) =
1
1 + 
m∈Ni,t δi,t(m).
(11)
17

Investors with lower values of β0,i,t have more elastic demand, and their portfolio weights
vary more with log market-to-book equity. That is, more price elastic investors tilt their
portfolios toward stocks with lower market-to-book equity, holding other characteristics con-
stant.
Latent demand ϵi,t(n) ≥0 is the part of investor i’s demand for stock n that arises
from unobserved (to the econometrician) characteristics. Within its investment universe,
the investor chooses a zero portfolio weight for stock n when ϵi,t(n) = 0. We normalize the
mean of latent demand across an investor’s investment universe to one so that the intercept
αi,t in equation (10) is identiﬁed.
However, the mean of latent demand across investors
need not equal one for a given stock. According to equation (7), any variation in market-
to-book equity that ﬁrm characteristics do not explain is due to the weighted average of
latent demand. In equilibrium, market-to-book equity is higher for stocks that have a higher
weighted average of latent demand due to beliefs or sentiment about future proﬁtability.
4.3.
Market clearing
Let Pt(n) be market equity for stock n in period t, which is also the equity price because we
normalize shares outstanding to one. Market clearing for each stock n is
Pt(n) =
I

i=1
Ai,twi,t(n; Pt).
(12)
Market equity is equal to the sum of asset demand, which is wealth times the portfolio weight,
across all investors. In equation (10) for the portfolio weight, we can write log market-to-
book equity as log market equity minus log book equity. Thus, the notation in equation
(12) emphasizes that the portfolio weight for stock n depends on the N-dimensional vector
of equity prices Pt.
Market clearing (12) is a system of N nonlinear equations in N equity prices. Koijen and
Yogo (2019) show that β0,i,t < 1 for all investors is a suﬃcient condition for the system of
equations to have a unique solution. Therefore, we impose the coeﬃcient restriction β0,i,t < 1
in the demand estimation.
4.4.
Counterfactuals with endogenous wealth
As we explained in Section 2, we consider two types of counterfactuals. The ﬁrst is capital
ﬂows from a group of investors to other investors, such as from active to passive investors.
The second is a shift in asset demand through a change in the coeﬃcient for a particular
characteristic, such as the environmental score. We solve for the counterfactual equity prices
18

by market clearing, maintaining the assumption in Section 2 that shares outstanding and ﬁrm
characteristics do not change in the spirit of an endowment economy. However, we allow
the investors’ wealth to change endogenously with equity prices, which is a contribution
relative to Koijen and Yogo (2019). Thus, the counterfactuals have implications for the
wealth distribution, which is an important step toward welfare analysis. We leave formal
welfare analysis, which is challenging in a model with heterogeneous beliefs (Brunnermeier
et al., 2014), for future research.
Let the superscript C denote the counterfactual values of the corresponding variables.
Investor i’s wealth in the counterfactual market is
AC
i,t

PC
t

= Ai,t
⎛
⎝wi,t(0) +

n∈Ni,t
P C
t (n)
Pt(n) wi,t(n)
⎞
⎠



capital gain
+Fi,t.
(13)
The ﬁrst term is the investor’s initial portfolio revalued at the counterfactual vector of equity
prices PC
t . The second term is the capital ﬂow Fi,t. We can specify the set of capital ﬂows
and compute the counterfactual wealth distribution by equation (13). Equivalently, we can
specify the counterfactual wealth distribution directly and implicitly deﬁne the set of capital
ﬂows that supports that distribution.
The counterfactual equity prices are a solution to market clearing:
P C
t (n) =
I

i=1
AC
i,t

PC
t

wC
i,t

n; PC
t

.
(14)
We assume that the investors maintain the same outside portfolio weights in the counter-
factual market (i.e., wC
i,t(0) = wi,t(0)), which ensures that our results are not driven by
substitution into the outside asset (i.e., micro-cap stocks). We solve for the counterfactual
equity prices by iterating on equation (14) until convergence, using the algorithm in Koijen
and Yogo (2019, Appendix C). Equation (13) at the converged vector of equity prices implies
the counterfactual wealth distribution.
5.
Estimating the asset demand system
We face two main challenges in the demand estimation. First, market-to-book equity and
latent demand are jointly endogenous, which we address through instrumental variables. Sec-
ond, many investors do not have enough observations in the cross section of equity holdings
for accurate demand estimation, which we address through a ridge estimator. After estimat-
19

ing the asset demand system, we summarize the evidence on heterogeneity in asset demand
and low demand elasticities across institutional investors. Finally, we test the robustness of
our identifying assumptions.
5.1.
Estimation equation
For each investor i, we divide the portfolio weight for stock n (9) by the outside portfolio
weight (11) to obtain a nonlinear regression equation:
wi,t(n)
wi,t(0) = δi,t(n) = exp(αi,t + β0,i,tmbt(n) + β′
1,i,txt(n))ϵi,t(n).
(15)
The cross-sectional relation between the portfolio weights and the ﬁrm characteristics iden-
tiﬁes the demand coeﬃcients. More price elastic investors tilt their portfolios toward stocks
with lower market-to-book equity, controlling for other characteristics. Investors who tilt
their portfolios toward greener stocks have larger coeﬃcients on the environmental score,
controlling for other characteristics.
We use two estimation samples for the demand estimation. The ﬁrst is quarterly data
from 2000.Q1 to 2019.Q4, for which we use six characteristics: log book equity, foreign sales
share, the Lerner index, the ratio of sales to book equity, the ratio of dividends to book
equity, and market beta. The second is quarterly data from 2010.Q1 to 2019.Q4, for which
we add the environmental score and the governance index as additional characteristics.
5.2.
Instrumental variables
Our baseline assumption is that the observed characteristics xt(n) are exogenous in the
spirit of an endowment economy.
However, we discuss how to relax this assumption to
allow for endogenous characteristics in Appendix D.3. Even with exogenous characteristics,
log market-to-book equity and latent demand are jointly endogenous. This correlation could
arise for larger investors with price impact or smaller investors with correlated latent demand
that have price impact in the aggregate.
Following Koijen and Yogo (2019), we construct an instrument under the assumption
that the investors have an exogenous component of demand that arises from predetermined
investment mandates. For example, mutual funds have investment mandates or an eﬀective
investment universe that arises from benchmarking. Hedge funds, pension funds, and insur-
ance companies also have investment mandates or an eﬀective investment universe that arises
from capital regulation and ﬁduciary rules. Alternatively, an investment universe could arise
from informational frictions that limit an investor’s choice set to a subset of stocks.
20

Although investment mandates and benchmarking are ubiquitous, they are not systemat-
ically disclosed except for some mutual funds and exchange traded funds. Following Koijen
and Yogo (2019), we estimate the investment universe in each quarter as the set of stocks
that an investor currently holds or has ever held in the past 11 quarters. Consistent with the
notion that the investment universe is predetermined and exogenous to contemporaneous
demand shocks, Koijen and Yogo (2019) show that this empirical estimate of the invest-
ment universe is very stable over time. A threat to identiﬁcation is that any changes in
the estimated investment universe could reﬂect changing beliefs about future proﬁtability.
In Appendix D, we test the robustness of our estimates to changing the deﬁnition of the
investment universe to address this concern.
Let Ni,t be the investment universe of investor i in period t. Let |Ni,t| be the number of
stocks in the investment universe. Let
 i(n) be an indicator function that is equal to one
if stock n is in investor i’s investment universe. Under the assumption that our empirical
estimates of the investment universe are exogenous, we construct an instrument for log
market equity of stock n as
zi,t(n) = log
⎛
⎝
j /∈{i,1}
Aj,t
 j(n)
1 + |Nj,t|
⎞
⎠.
This instrument corresponds to log market equity for stock n in a counterfactual market
if investors were to hold an equal-weighted portfolio within their investment universe. The
instrument is investor speciﬁc (and thus indexed by i) because we exclude own holdings and
the household sector (i.e., j = 1). The identifying assumption is that the investment universe
of other institutional investors aﬀects the portfolio choice of investor i only through equity
prices.
5.3.
Estimation methodology
Another challenge in the demand estimation is that most institutional investors hold concen-
trated portfolios. Thus, many investors do not have enough observations in the cross section
of equity holdings for accurate demand estimation. This challenge is especially relevant since
we deﬁne inside assets as the largest 90% of ﬁrms by market equity, which makes the cross
section smaller than the universe of all US stocks. In estimating equation (15), we pool the
data across the four quarters of a given year and assume that the demand coeﬃcients are
constant within each year. However, we allow the intercept αi,t to vary across quarters.
For investors with fewer than 2,000 holdings across the four quarters (inclusive of the zero
holdings), we estimate their demand coeﬃcients through a two-step instrumental variables
21

ridge estimator (Hoerl and Kennard, 1970). In the ﬁrst step, we estimate the shrinkage
target. We sort the investors by investor type and average wealth over the four quarters.
We group the investors so that there are at least 2,000 holdings per group. Let 0 be a vector
of zeros. Let et be a four-dimensional vector of quarter ﬁxed eﬀects, where the t-element is
one and the other elements are zero. For each group, we estimate the demand coeﬃcients
through the moment condition:
E
⎡
⎢⎣(δi,t(n) exp(−β0mbt(n) −α′
iet −β′
1xt(n))



ϵi,t(n)
−1)
⎛
⎜
⎝
zi,t(n)
et
xt(n)
⎞
⎟
⎠
⎤
⎥⎦= 0.
(16)
We denote the estimated coeﬃcients for log market-to-book equity and other characteristics
respectively as β0 and β1.
In the second step, we estimate the demand coeﬃcients for each investor, using the group-
level estimates as the shrinkage target. We impose an inﬁnite penalty on the coeﬃcient for
log market-to-book equity to avoid weak identiﬁcation, which is conceptually related to two-
sample instrumental variables estimation (Angrist and Krueger, 1992). We estimate the
coeﬃcients on the other characteristics through the moment condition:
E

δi,t(n) exp(−α′
iet −β′
1,ixt(n)) −1
 
et
xt(n)

−
λ
|Ni|ξ

0
β1,i −β1

= 0,
(17)
where δi,t(n) = δi,t(n) exp(−β0mbt(n)).
A quadratic penalty on the generalized method
of moments objective function leads to a linear term in the moment condition (17). The
penalty is inversely related to |Ni|, which is the number of investor i’s holdings across the
four quarters. The penalty shrinks the demand coeﬃcients toward the group-level estimate
β1.
We select the penalty parameters by cross validation. For each investor, we randomly
split the estimation sample in half within each quarter. We estimate asset demand in the
ﬁrst subsample and compute the mean squared error of predicted demand in the second
subsample. We select the penalty parameters to minimize the mean squared error, which
results in λ = 120 and ξ = 0.7. In Appendix C, we describe a fast numerical algorithm to
compute the instrumental variables ridge estimator.
For investors with at least 2,000 holdings across the four quarters (inclusive of the zero
holdings), we estimate their demand coeﬃcients individually by generalized method of mo-
ments through the moment condition (16).
22

5.4.
Estimated demand system
To summarize the cross-sectional variation in the demand coeﬃcients, we compute the time-
series average of the estimated demand coeﬃcients for each investor over the sample period
during which both investor holdings and ﬁrm characteristics are available. Therefore, the
sample period for the environmental score and the governance index is limited to 2010 to
2019. Except for log market-to-book equity and log book equity, we standardize and multiply
the demand coeﬃcients by 100, so that they can be interpreted as the percent change in
demand per one standard deviation change in the ﬁrm characteristic.
Figure 2 reports the cross-sectional distribution of the average demand coeﬃcients across
investors.
The colored vertical lines represent a wealth-weighted average of the demand
coeﬃcients by investor type, in which an investor’s weight is the time-series average of its
wealth share by investor type. The wealth-weighted coeﬃcient on the environmental score
is 2.82% for small-passive investment advisors and −1.56% for hedge funds. That is, for
small-passive investment advisors, an equity holding changes by 2.82% per one standard
deviation change in the ﬁrm’s environmental score. A negative coeﬃcient means that hedge
funds prefer browner stocks, holding equity prices and other characteristics constant.
The average coeﬃcient on log market-to-book equity varies from 1 (i.e., inelastic demand)
to around 0 (i.e., approximately unit elasticity) across investors. This coeﬃcient determines
the price elasticity of demand, which is approximately 1 −β0,i,t. Even hedge funds, which
are the most elastic among institutional investors, have a wealth-weighted price elasticity
of demand around 0.5. Figure 2 reports signiﬁcant heterogeneity in the demand coeﬃcients
across investors, beyond the heterogeneity across investor types.
Table 4 summarizes the cross-sectional variation in the demand coeﬃcients across in-
vestors. Panel A reports a wealth-weighted regression of the demand coeﬃcients on investor-
type ﬁxed eﬀects. Passive investment advisors (both large and small) and brokers have a
higher demand for stocks with higher environmental scores. Small-active investment advi-
sors and brokers have a higher demand for stocks with lower governance indices (i.e., less
entrenchment). On the one hand, hedge funds and small-active investment advisors have
lower coeﬃcients on log market-to-book equity, implying higher price elasticities of demand.
On the other hand, large investment advisors (both passive and active), long-term investors,
and brokers have higher coeﬃcients on log market-to-book equity.
Panel A of Table 4 also reports the adjusted R2 for the regression of the demand co-
eﬃcients on investor-type ﬁxed eﬀects. Log market-to-book equity, which determines the
price elasticity of demand, has an adjusted R2 of 49%. Log book equity, which captures
demand for ﬁrm size, has an adjusted R2 of 59%. Except for these two characteristics, the
demand coeﬃcients have a low R2. The investor type alone does not explain much of the
23

heterogeneity in asset demand across investors.
Panel B of Table 4 reports a wealth-weighted regression of the demand coeﬃcients on the
log average wealth share, the active share, and a foreign-investor ﬁxed eﬀect. Larger, more
passive, and foreign investors have a higher demand for stocks with higher environmental
scores. Smaller and foreign investors have a higher demand for stocks with lower governance
indices (i.e., less entrenchment). Smaller and more active investors have lower coeﬃcients
on log market-to-book equity, implying higher price elasticities of demand. Except for log
market-to-book equity and log book equity, the demand coeﬃcients have a low R2.
Figure 3 summarizes the diﬀerences in the wealth-weighted demand coeﬃcients between
domestic and foreign investors.
Foreign investors have a higher demand for stocks with
higher environmental scores and lower governance indices (i.e., less entrenchment).
This
ﬁnding implies that foreign investors play an important role in lowering the cost of capital
for greener US ﬁrms. Foreign investors also have a higher demand for stocks with a higher
foreign sales share, perhaps due to more familiarity with those ﬁrms. Finally, foreign investors
have a higher demand for safer stocks with a lower market beta.
In summary, we ﬁnd rich heterogeneity in asset demand across investors that are not
well captured by simple characteristics such as investor type, wealth, active share, and
geography. This ﬁnding has several important implications. First, it highlights the relevance
of the instrumental variables ridge estimator that allows for heterogeneity in asset demand
within investor type and wealth group. Second, it opens a new research agenda to explain
the heterogeneity using more granular information about investors such as their capital
regulation, investment mandates, and funding structure. Third, the heterogeneity in asset
demand implies that ownership could have an important impact on equity prices as we study
in Sections 6–8.
5.5.
Robustness of the identifying assumptions
We have made a number of choices in the identifying assumptions and in specifying asset
demand. We would like to ensure that our results are robust to reasonable variation in these
assumptions. In particular, we test whether our results are robust to the deﬁnition of the
investment universe, the choice of ﬁrm characteristics, and the exogeneity of ﬁrm character-
istics. Our criteria for robustness are the estimated demand coeﬃcients and their impact on
the counterfactual equity prices, price informativeness, and the wealth distribution in the
applications of Sections 6–8. We summarize the results here and leave the full presentation
for Appendix D.
A threat to identiﬁcation is that any changes in the estimated investment universe could
reﬂect changing beliefs about future proﬁtability. The baseline deﬁnition of the investment
24

universe is the set of stocks that an investor currently holds or has ever held in the past 11
quarters. We test whether our results are robust to changing the deﬁnition in three ways.
First, we construct the instrument without hedge funds to address the concern that their
investment universe may adjust more to changing beliefs than that of other institutional
investors.
Second, we change the window for estimating the investment universe, both
backward and forward by up to ﬁve years. This exercise exposes potential sensitivity of our
results to higher frequency changes in beliefs about future proﬁtability. Third, we randomly
increase the number of stocks in the investment universe by up to 100%. Our results are
robust to each of these alternative assumptions.
We have eight characteristics in the baseline speciﬁcation of asset demand.
We test
whether our results are robust to the choice of ﬁrm characteristics by adding three char-
acteristics: investment, the ratio of net repurchases to book equity, and earnings surprises.
These characteristics are known to be strong predictors of stock returns (Daniel et al., 2020).
Our results are robust to the additional characteristics, suggesting that the baseline speciﬁ-
cation is not especially sensitive to the choice of ﬁrm characteristics.
The baseline assumption is that ﬁrm characteristics other than log market-to-book equity
are exogenous. However, some ﬁrm decisions, such as dividend policy, could depend on equity
prices. Our results are robust to an alternative estimator of asset demand that allows the
ratio of dividends to book equity to be endogenous.
6.
Transition from active to passive investment management
The estimated demand system reveals rich heterogeneity in asset demand across investors.
The heterogeneity between active and passive investors is one dimension of current policy
interest because of the potential impact of the transition from active to passive investment
management. We ﬁrst show that the decline in the aggregate active share is mostly due
to the capital ﬂows from active to passive investors, rather than the investment strategies
becoming more passive. Based on this fact, we design a counterfactual to quantify the impact
of the transition from active to passive investment management on equity prices and price
informativeness.
6.1.
Trend in the aggregate active share
We use the active share, appropriately modiﬁed for our application, as a measure of active
investment management (Cremers and Petajisto, 2009). As we deﬁned previously, Ni,t is
the set of stocks in investor i’s investment universe in period t. Let AI
i,t = Ai,t(1 −wi,t(0))
be the investor’s wealth excluding the outside assets (i.e., micro-cap stocks). Let wI
i,t(n) =
25

Pt(n)qi,t(n)/AI
i,t be the investor’s portfolio weight on stock n among inside assets only, which
is zero for a stock in the investment universe that the investor does not currently hold. Let
wM
i,t(n) = Pt(n)/ 
m∈Ni,t Pt(m) be the corresponding portfolio weight if the investor were
to hold the market portfolio among its inside assets.7 We deﬁne investor i’s active share in
period t as
ASi,t = 1
2

n∈Ni,t
wI
i,t(n) −wM
i,t(n)
 .
(18)
The active share measures the total share of the investor’s portfolio that deviates from the
market weights. The division by two avoids double counting and ensures the active share is
between zero (most passive) and one (most active).
We then deﬁne the aggregate active share as a wealth-weighted average of the active
shares across all institutional investors, excluding the household sector (i.e., i = 1):
ASt =
I

i=2
ai,tASi,t,
where ai,t = Ai,t/ 
I
j=2 Aj,t is the wealth share. Panel A of Figure 4 shows that the aggregate
active share declined from 2000 to 2019, based on our sample from FactSet Ownership.
Panel B shows a longer decline from 46.6% in 1980.Q4 to 31.7% in 2017.Q4, based on the
Thomson Reuters Institutional Holdings Database (Koijen and Yogo, 2019). We focus our
analysis on 2007.Q4 to 2016.Q4, which is a subperiod that has a similar rate of decline to the
overall trend from 1980 to 2017. The end date of 2016.Q4 leaves room for us to construct
three-year future proﬁtability, which is necessary for studying price informativeness. The
aggregate active share declined from 38.9% in 2007.Q4 to 32.8% in 2016.Q4, for the subset
of institutional investors who exist in both 2007.Q4 and 2016.Q4.8
For this subset of institutional investors, we decompose the change in the aggregate active
share as
ASB
2016 −ASB
2007 =
I

i=2
aB
i,2007(ASi,2016 −ASi,2007) +
I

i=2

aB
i,2016 −aB
i,2007

ASi,2016,
7Alternatively, we could deﬁne the active share based on strictly positive holdings in the investment
universe. We have veriﬁed that the key facts about the aggregate active share remain robust to this alternative
deﬁnition.
8This subset of investors managed 90% of all institutional equity holdings in 2016.Q4. Without condi-
tioning on this subset of investors, we ﬁnd a similar decline in the aggregate active share from 40.2% in
2007.Q4 to 33.8% in 2016.Q4.
26

where the variables with the superscript B are deﬁned over investors who exist in both
2007.Q4 and 2016.Q4. The aggregate active share can change for two reasons. The ﬁrst term
captures the change in the investment strategies, holding the wealth distribution constant.
The second term is the change in the wealth distribution, holding the investment strategies
constant. We ﬁnd that the change in the aggregate active share is the sum of −1.3% for the
ﬁrst term and −4.8% for the second term. Thus, the decline in the aggregate active share is
mostly due to the capital ﬂows from active to passive investors, rather than the investment
strategies becoming more passive.
6.2.
Impact on equity prices
Based on this fact about the aggregate active share, we design a counterfactual to quantify
the impact of the transition from active to passive investment management on equity prices
and price informativeness. Within the subset of institutional investors who exist in both
2007.Q4 and 2016.Q4, we replace their wealth distribution in 2016.Q4 with that in 2007.Q4.9
However, we do not change their asset demand functions (i.e., the demand coeﬃcients and
latent demand) in 2016.Q4. For the household sector and the institutional investors who
exist only in 2016.Q4, we do not change their wealth or asset demand functions. As we
discussed in Section 4, this change in the wealth distribution deﬁnes a set of capital ﬂows
across investors by equation (13). By market clearing, we compute counterfactual equity
prices in 2016.Q4 if the wealth distribution across institutional investors were to remain the
same as that in 2007.Q4.
Panel A of Figure 5 is a scatter plot that compares the wealth distribution in 2007.Q4
and 2016.Q4. Both axes are in units of log wealth shares. Above the 45-degree line are
investors whose wealth share increased from 2007.Q4 and 2016.Q4. These investors are more
passive on average and would have a lower wealth share in the counterfactual market.
Panel B of Figure 5 is a scatter plot of the actual log market equity in 2016.Q4 versus
the counterfactual log market equity. Equity prices change substantially, especially among
smaller stocks.
Above the 45-degree line are stocks that become more expensive in the
counterfactual market. These stocks have characteristics or latent demand that are more
highly valued by investors who become larger in the counterfactual market. We summarize
Panel B by deﬁning equity repricing as the value-weighted absolute percent change in equity
9We have veriﬁed that the results in this section are robust to an alternative counterfactual that isolates
the capital ﬂows that correlate with the active share. We run a cross-sectional regression of the log diﬀerence
in wealth shares between 2007.Q4 and 2016.Q4 on the active share in 2016.Q4. We then multiply the wealth
shares in 2016.Q4 by the exponential of the predicted values from the regression to obtain the counterfactual
wealth distribution in 2007.Q4.
27

prices:

N
n=1
P C
t (n) −Pt(n)


N
n=1 Pt(n)
,
(19)
where P C
t (n) is the counterfactual price of stock n. We ﬁnd an economically signiﬁcant
estimate of 14%.
6.3.
Impact on price informativeness
The transition from active to passive investment management could have implications for
price informativeness. Equity prices could become less informative if capital ﬂowed from
more to less informed investors. We ﬁrst estimate how the change in the wealth distribution
from 2007.Q4 to 2016.Q4 aﬀected price informativeness. We then investigate the mechanism
with a measure of investor-level informativeness.
Let Et(n) be earnings before interest and taxes for stock n in year t.10 Let At(n) be book
assets for stock n in period t. Following Bai et al. (2016), we measure price informativeness
based on a cross-sectional regression of future proﬁtability on the ratio of market equity to
book assets:
Et+3(n)
At(n)
= α + π log
 Pt(n)
At(n)

+ ρEt(n)
At(n) + νt(n).
(20)
The regression coeﬃcient π measures price informativeness, where a higher coeﬃcient implies
that equity prices are more informative.
Bai et al. (2016) motivate their measure of price informativeness in a class of models
in which investors have information about future productivity (and thereby proﬁtability)
that managers do not have.
Therefore, managers learn about the investors’ information
from asset prices, which improves the eﬃciency of real investment. D´avila and Parlatore
(2022) propose a diﬀerent measure of price informativeness based on essentially the reverse
regression of changes in market equity on contemporaneous and future changes in earnings.
They establish the conditions under which their measure of price informativeness is equivalent
to that of Bai et al. (2016), up to scaling by the variance of the innovations to earnings.
Sammon (2022) proposes a diﬀerent measure of price informativeness based on the price
drift before earnings announcements. Thus, the deﬁnition of price informativeness depends
on the motivating theory and econometric speciﬁcation. Although we apply our framework
10Following Bai et al. (2016), we use this measure that is diﬀerent from the clean-surplus earnings that
we used in Table 3. However, we have checked that the results in Table 3 are similar when we use earnings
before interest and taxes.
28

to a leading measure of price informativeness, the broader framework also applies to other
measures of price informativeness. We leave the implementation to these other measures for
future research.
In 2016.Q4, the standardized coeﬃcient measuring price informativeness is 0.049 with a
standard error of 0.003. This estimate implies that a standard deviation change in the ratio
of market equity to book assets predicts a 4.9 percentage point change in proﬁtability.
We quantify the impact of the change in the wealth distribution from 2007.Q4 to 2016.Q4
on price informativeness. We reestimate the cross-sectional regression (20), replacing the
actual market equity in 2016.Q4 with the counterfactual market equity under the wealth
distribution in 2007.Q4. Panel C of Figure 5 shows that the regression coeﬃcient for price
informativeness hardly changes. The ﬁrst bar in Panel C represents the regression coeﬃcient
0.049 estimated on actual data, together with a 95% conﬁdence interval. The second bar
shows the impact of changing the wealth distribution for only large-passive investment advi-
sors to that in 2007.Q4. The third bar shows the cumulative impact of changing the wealth
distribution for small-passive and large-passive investment advisors to that in 2007.Q4. In
each step, we rescale total wealth by investor type so that the relative size of the investor
types match the actual distribution in 2016.Q4. We keep adding investor types sequentially
until the ﬁnal bar, which shows the cumulative impact of changing the wealth distribution
for all institutional investors to that in 2007.Q4.
6.4.
Investor-level informativeness
To investigate why the change in the wealth distribution had a small impact on price in-
formativeness, we develop a measure of investor-level informativeness. We are guided by
equation (8), which shows that the investors’ demand shifters reﬂect beliefs or sentiment
about future proﬁtability. A more informed investor has demand shifters that predict future
proﬁtability in the cross section of its equity holdings. Thus, we identify which investors are
more informed about future proﬁtability to directly test whether capital ﬂowed from more
to less informed investors.
For each investor in 2016.Q4, we estimate the demand shifters based on the ﬁrm char-
acteristics, the estimated demand coeﬃcients, and latent demand.
We then estimate a
cross-sectional regression of future proﬁtability on the demand shifters:
Et+3(n)
At(n)
= α + πi log
exp(β′
1,i,txt(n))ϵi,t(n)
At(n)

+ ρEt(n)
At(n) + νt(n).
The investor-level informativeness is the standardized version of the regression coeﬃcient πi.
A higher coeﬃcient implies that the investor’s demand shifters are more informative about
29

future proﬁtability. We focus on the subsample of investors with at least 30 positive holdings.
Nevertheless, we caution that expected proﬁtability is challenging to estimate accurately in
a single cross section. Future research could extend our estimation exercise to the entire
panel to systematically study price discovery and market eﬃciency.
Panel D of Figure 5 is a bin scatter plot of the changes in the log wealth share from
2007.Q4 to 2016.Q4 versus the investor-level informativeness.
There is little correlation
between the two variables, which implies that capital did not ﬂow from more to less informed
investors on average. Thus, the transition from active to passive investment management
did not reduce price informativeness, despite the large eﬀect that it had on equity prices.
7.
Climate-induced shifts in asset demand
Stroebel and Wurgler (2021) surveyed 861 ﬁnance academics, policy economists, profession-
als, and public sector regulators regarding climate risk. Over a shorter horizon of ﬁve years,
the survey ﬁnds that regulatory risk is the primary source of climate risk. The survey also
identiﬁes stakeholder risk as a secondary source of climate risk, which includes the changing
preferences of customers and employees. Over a longer horizon of 30 years, the survey ﬁnds
that physical risk is the primary source of climate risk. By an overwhelming margin, the
respondents believe that asset prices underestimate climate risk.
Based on this survey, we focus on regulatory and stakeholder risks. A comprehensive
analysis of these risks on asset prices, ﬁrms, and the macroeconomy is beyond the scope of
this paper. We focus on one important aspect of this problem, which is the potential impact
on equity prices and the wealth distribution across institutional investors. Our counterfactual
analysis could be a building block in a more comprehensive climate stress test of the ﬁnancial
sector.
7.1.
Modeling the impact of climate risk on asset demand
We focus on one aspect of regulatory risk, which is a tighter constraint on the portfolio
choice of long-term investors (i.e., pension funds and insurance companies). Pension and
insurance regulators could become increasingly concerned that some ﬁrms are exposed to
greater stakeholder or physical risk. Alternatively, some ﬁrms are exposed to greater uncer-
tainty over a carbon tax. To limit the climate risk exposure, pension and insurance regulators
could change the investment mandates to favor green ﬁrms or increase the capital charges on
brown ﬁrms as part of risk-based capital regulation. For example, the National Association
of Insurance Commissioners has set up a Climate and Resiliency Task Force to explore the
impact of climate risk on the insurance industry.
30

We model realized regulatory risk as an increase in the coeﬃcient on the environmental
score for long-term investors by 0.1, which is approximately one standard deviation in its
cross-sectional distribution (see Figure 2). A increase of 0.1 implies that the portfolio weight
changes by 10% (e.g., from 5% to 5.5% of wealth) per one standard deviation change in the
environmental score. We assume that the coeﬃcients on the other characteristics remain
constant because the environmental score is only weakly correlated with the other charac-
teristics. However, we could choose a value diﬀerent from 0.1 or allow the coeﬃcients on the
other characteristics to change to tailor the counterfactual to a particular policy proposal.
Stakeholder risk arises from the possibility that many institutional investors unexpectedly
shift their portfolios toward greener ﬁrms in response to the changing preferences of customers
and employees. We model realized stakeholder risk as an increase in the coeﬃcient on the
environmental score for all institutional investors by 0.1. An important caveat is that the
counterfactual only captures the short-run eﬀects on equity prices, holding the composition
of ﬁrms and their environmental scores ﬁxed. In the long run, the composition of ﬁrms and
their policies could change with climate-induced shifts in asset demand.
7.2.
Impact on equity prices
As a reference point, the ﬁrst column of Table 5 reports a regression of log market-to-book
equity on ﬁrm characteristics in 2019. This regression is essentially the same as that in
Table 3, except that we limit the sample to a single cross section.
The second column of Table 5 reports the change in the regression coeﬃcients in response
to realized stakeholder risk, when the elasticity of demand to the environmental score in-
creases for all institutional investors. We estimate the second column through a regression
of the diﬀerence between counterfactual and actual log market-to-book equity on the ﬁrm
characteristics. The regression coeﬃcient on the environmental score increases by 0.57. That
is, market-to-book equity changes by 57% more per one standard deviation change in the
environmental score. As we explained Section 2, the regression coeﬃcients on the other char-
acteristics do not change in a linear asset pricing model. Thus, the fact that the regression
coeﬃcients on the other characteristics hardly change implies approximately linear eﬀects in
the counterfactual.
The third column of Table 5 reports the change in the regression coeﬃcients in response to
realized regulatory risk, when the elasticity of demand to the environmental score increases
for long-term investors only. The regression coeﬃcient on the environmental score increases
by 0.03, which is a much smaller eﬀect because the regulation applies to a smaller group
of investors. This ﬁnding implies that pension funds and insurance companies could reduce
climate risk exposure without a large impact on the stock market. An important caveat
31

is that pension funds and insurance companies are larger in ﬁxed income markets, so the
overall impact on ﬁnancial markets could be larger than the limited scope of our analysis.
7.3.
Impact on the wealth distribution
Because of initial heterogeneity in the portfolio strategies along the environmental score,
the wealth distribution across institutional investors changes when equity prices change.
Panel A of Figure 6 is a bin scatter plot of the coeﬃcient on the environmental score versus
the percent change in wealth in response to realized stakeholder risk. Investors whose initial
portfolios tilt toward greener stocks beneﬁt when these stocks become more expensive in the
counterfactual market.
Panel B of Figure 6 reports the percent change in wealth in response to climate-induced
shifts in asset demand.
Stakeholder risk has a larger impact on the wealth distribution
than regulatory risk because of larger changes in equity prices. On the one hand, passive
investment advisors, long-term investors, and private banking earn capital gains. On the
other hand, active investment advisors and hedge funds earn capital losses. Thus, active
investment advisors and hedge funds have the greatest exposure to climate risk.
8.
Impact of institutional investors on equity prices
Building on the two policy-relevant applications in the previous sections, we use the asset
demand system to study the relative importance of institutional investors for cross-sectional
asset pricing. Our starting point is equation (7), which shows that market-to-book equity is a
wealth-weighted average of the demand shifters across investors. The variation in the demand
shifters across investors reﬂects heterogeneous beliefs or sentiment about future proﬁtability.
Consequently, equity prices change with the wealth distribution across institutional investors.
We quantify the relative importance of a group G of investors through a counterfactual
ﬂow from this group to other institutional investors in proportion to their wealth. In the
counterfactual, we set Ak,t = 0 for all investors k ∈G (e.g., hedge funds) and keep the
household wealth A1,t constant. The other institutional investors receive an oﬀsetting ﬂow
Fi,t =
Ai,t

j /∈{G,1} Aj,t

k∈G
Ak,t

.
This ﬂow deﬁnes a new wealth distribution across institutional investors through equation
(13). We do not change the asset demand functions (i.e., the demand coeﬃcients and latent
demand) in this counterfactual. By market clearing, we compute counterfactual equity prices
in response to capital ﬂows from a group of investors to other institutional investors.
32

8.1.
Impact on equity prices
In Table 6, the ﬁrst column reports the wealth distribution as a share of total wealth. The
second column reports equity repricing (19) in response to capital ﬂows from the given
group of investors to other institutional investors. Comparing the ﬁrst two columns, the
equity repricing is larger for capital ﬂows from a larger group of investors.
The largest
equity repricing is 26.7% for capital ﬂows from small-active investment advisors. The equity
pricing is modest for smaller groups of investors including hedge funds, long-term investors,
private banking, and brokers. For example, the equity pricing is 1.8% for brokers because
they manage only 1.1% of the stock market.
In Table 6, the last column reports the ratio of equity repricing in the second column to
the wealth share in the ﬁrst column. Thus, the last column is the absolute dollar change in
equity prices per dollar of wealth. Relative to their size, hedge funds play an outsized role
with equity repricing of $3.58 per dollar of wealth. Small-active investment advisors also play
an important role with equity repricing of $2.28 per dollar of wealth. In contrast, passive
investment advisors (both large and small) and long-term investors play a less important
role with equity repricing of about $1 per dollar of wealth.
Figure 7 explains the mechanism behind the relative importance of institutional investors
for equity prices. Panels A and B report the same information as Table 6. Panel A reports
the wealth distribution and the equity repricing by investor type.
Panel B reports the
equity repricing per dollar of wealth by investor type.
Panels C and D explain the two
important inputs behind the equity repricing per dollar of wealth in Panel B. The ﬁrst input
is heterogeneity in asset demand. The equity repricing per dollar of wealth is larger for
capital ﬂows from a group of investors who have asset demand that is more diﬀerent from
the other investors. A simple statistic that captures the heterogeneity in asset demand is
the active share (18). Panel C shows a positive correlation between the active share and
the equity repricing per dollar of wealth across investor types. Hedge funds have the largest
equity repricing per dollar of wealth because their portfolio strategies are the most diﬀerent
from the other investors.
The second input is the relative price elasticities of demand across investors. For a group
of investors who have relatively elastic demand, their outﬂow faces the relatively inelastic
demand of the other investors, leading to a larger price impact.
A simple statistic that
captures the price elasticity of demand by investor type is the wealth-weighted average of
one minus the coeﬃcient on log market equity (i.e., 1 −β0,i,t). Panel D shows a positive
correlation between the wealth-weighted price elasticity of demand and the equity repricing
per dollar of wealth across investor types. Hedge funds have the largest equity repricing
per dollar of wealth because they have relatively elastic demand, so that their outﬂow faces
33

the relatively inelastic demand of the other investors. In summary, the combination of more
active portfolio strategies and more elastic demand implies that hedge funds have the largest
impact on equity prices per dollar of wealth.
8.2.
Relation between equity valuations and ﬁrm characteristics
Table 3 shows that ﬁrm characteristics explain a large share of the variation in market-to-
book equity. Financial analysts, economists, and reporters sometimes provide narratives for
the relation between equity valuations and ﬁrm characteristics. One narrative is that retail
investors and hedge funds drove up the prices of growth stocks during the dot-com bubble
and COVID-19. Another narrative is that pension funds and sovereign wealth funds drive
up the equity prices of sustainable or socially responsible ﬁrms. The asset demand system
provides a framework to quantitatively assess these narratives, by inferring the investors’
beliefs or sentiment about future proﬁtability from their portfolios.
In Table 7, the ﬁrst column reports the regression of actual log market-to-book equity on
ﬁrm characteristics, which is identical to the ﬁrst column of Table 3. The remaining columns
reestimate the regression with counterfactual log market-to-book equity for capital ﬂows from
the given group of investors to other institutional investors. Small-active investment advisors
and foreign investors have opposite eﬀects on the pricing of the environmental score. On
the one hand, the regression coeﬃcient on the environmental score increases from 0.17 to
0.21 for capital ﬂows from small-active investment advisors. That is, a standard deviation
change in the environmental score would change equity prices by 21% instead of 17%. On
the other hand, the regression coeﬃcient on the environmental score decreases from 0.17 to
0.14 for capital ﬂows from foreign investors.11
Small-active investment advisors and hedge funds are inﬂuential in pricing the governance
index. The regression coeﬃcient on the governance index increases from −0.10 to −0.09 for
capital ﬂows from small-active investment advisors or hedge funds.
That is, a standard
deviation decrease in the governance index (i.e., less entrenchment) would increase equity
prices by 9% instead of 10%.
8.3.
Relation between expected returns and ﬁrm characteristics
The decomposition of market-to-book equity into the relative importance of institutional
investors has immediate implications for expected returns. Let rt be the log stock return
and et be log proﬁtability in year t, which we deﬁne in Appendix B. Cohen et al. (2003)
11Future research could examine whether foreign ownership increases investment in greener technology,
building on previous ﬁndings that foreign ownership increases long-term investment and price informativeness
(Bena et al., 2017; Kacperczyk et al., 2021).
34

derive a present-value model for log market-to-book equity:
mbt =
∞

s=1
ρs−1(Et[et+s] −Et[rt+s]).
If expected returns were to follow an autoregressive process so that Et[rt+s] = φs−1μt, this
equation simpliﬁes to
μt = (1 −ρφ)

−mbt +
∞

s=1
ρs−1Et[et+s]

.
(21)
Expected returns are high when log market-to-book equity is low or when expected prof-
itability is high. The sensitivity of expected returns to log market-to-book equity decreases
in the persistence of expected returns (i.e., decreases in φ).
Suppose that the econometrician’s forecast of expected proﬁtability does not change
in a counterfactual. We can use equation (21) to translate the counterfactual change in
log market-to-book equity to the corresponding change in expected returns. For example,
consider the counterfactual capital ﬂow from small-active investment advisors in Table 7.
Log market-to-book equity for a stock with the environmental score equal to one standard
deviation increases by 0.04. Based on an estimate of 1 −ρφ = 1 −0.932 × 0.969 = 0.097
(Binsbergen and Koijen, 2010), the annual expected return decreases by 39 basis points (i.e.,
0.097 × 0.04). More generally, we can translate all of Table 7 to units of annual expected
returns by simply multiplying each cell by −0.097.
9.
Conclusion
Based on an asset demand system, we develop a new framework to quantify the impact
of market trends and changes in regulation on asset prices, price informativeness, and the
wealth distribution. We apply the framework to quantify the importance of capital ﬂows
and shifts in asset demand in two applications of current policy interest. First, we ﬁnd that
the transition from active to passive investment management has a large impact on equity
prices but a small impact on price informativeness. To explain the latter result, we develop
a measure of investor-level informativeness to identify which investors are more informed
about future proﬁtability. The investor-level informativeness could have broader application
in studying price discovery and market eﬃciency. Second, climate-induced shifts in asset
demand that aﬀect all institutional investors have a large impact on equity prices and the
wealth distribution. Such shifts imply capital gains for passive investment advisors, pension
funds, insurance companies, and private banking and capital losses for active investment
35

advisors and hedge funds.
The set of policy-relevant questions will change over time. However, the framework that
we develop could be generally useful for counterfactual analysis of ﬁnancial markets. In ad-
dition, future research could extend the framework to study other policy-relevant outcomes.
For example, the transition from active to passive investment management could reduce
trading and liquidity. An analysis of liquidity would beneﬁt from higher frequency trans-
actions data, which are available in other countries such as Norway and Brazil (Betermier
et al., 2022; Schmickler and Tremacoldi-Rossi, 2022).
36

References
Angrist, J. D. and A. B. Krueger (1992). The eﬀect of age at school entry on educational
attainment: An application of instrumental variables with moments from two samples.
Journal of the American Statistical Association 87(418), 328–336.
Asness, C. S., A. Frazzini, and L. H. Pedersen (2019).
Quality minus junk.
Review of
Accounting Studies 24(1), 34–112.
Asness, C. S., T. J. Moskowitz, and L. H. Pedersen (2013). Value and momentum everywhere.
Journal of Finance 68(3), 929–986.
Bai, J., T. Philippon, and A. Savov (2016). Have ﬁnancial markets become more informative?
Journal of Financial Economics 122(3), 625–654.
Barberis, N., A. Shleifer, and R. Vishny (1998). A model of investor sentiment. Journal of
Financial Economics 49(3), 307–343.
Bauer, R., T. Ruof, and P. Smeets (2021). Get real! individuals prefer more sustainable
investments. Review of Financial Studies 34(8), 3976–4043.
Bebchuk, L., A. Cohen, and A. Ferrell (2009, 11). What matters in corporate governance?
Review of Financial Studies 22(2), 783–827.
Ben-David, I., F. Franzoni, R. Moussawi, and J. Sedunov (2021). The granular nature of
large institutional investors. Management Science 67(11), 6629–6659.
Bena, J., M. A. Ferreira, P. Matos, and P. Pires (2017).
Are foreign investors locusts?
the long-term eﬀects of foreign institutional ownership.
Journal of Financial Eco-
nomics 126(1), 122–146.
Betermier, S., L. E. Calvet, S. Kn¨upfer, and J. Kvaerner (2022). What do the portfolios
of individual investors reveal about the cross-section of equity returns? Working paper,
McGill University.
Binsbergen, J. H. v. and R. S. J. Koijen (2010). Predictive regressions: A present-value
approach. Journal of Finance 65(4), 1439–1471.
Brainard, W. C. and J. Tobin (1968). Pitfalls in ﬁnancial model building. American Eco-
nomic Review 58(2), 99–122.
37

Brunnermeier, M. K. and L. H. Pedersen (2009). Market liquidity and funding liquidity.
Review of Financial Studies 22(6), 2201–2238.
Brunnermeier, M. K., A. Simsek, and W. Xiong (2014). A welfare criterion for models with
distorted beliefs. Quarterly Journal of Economics 129(4), 1753–1797.
Campbell, J. Y., C. Polk, and T. Vuolteenaho (2010). Growth or glamour? fundamentals
and systematic risk in stock returns. Review of Financial Studies 23(1), 305–344.
Center for Research in Security Prices (2020). CRSP U.S. Stock Database. https://wrds-
www.wharton.upenn.edu/. Accessed 2020-12-20.
Chang, Y.-C., H. Hong, and I. Liskovich (2014). Regression discontinuity and the price
eﬀects of stock market indexing. Review of Financial Studies 28(1), 212–246.
Cohen, R. B., C. Polk, and T. Vuolteenaho (2003).
The value spread.
Journal of Fi-
nance 58(2), 609–641.
Cremers, K. J. M. and A. Petajisto (2009). How active is your fund manager? a new measure
that predicts performance. Review of Financial Studies 22(9), 3329–3365.
Daniel, K., D. Hirshleifer, and L. Sun (2020). Short- and long-horizon behavioral factors.
Review of Financial Studies 33(4), 1673–1736.
Daniel, K. and S. Titman (2006). Market reactions to tangible and intangible information.
Journal of Finance 61(4), 1605–1643.
D´avila, E. and C. Parlatore (2022). Identifying price informativeness. Working paper, Yale
University.
FactSet (2020). FactSet Ownership. https://www.factset.com/. Accessed 2020-12-20.
Fama, E. F. and K. R. French (1995). Size and book-to-market factors in earnings and
returns. Journal of Finance 50(1), 131–155.
Fama, E. F. and K. R. French (2007). Disagreement, tastes, and asset prices. Journal of
Financial Economics 83(3), 667–689.
Fama, E. F. and K. R. French (2015). A ﬁve-factor asset pricing model. Journal of Financial
Economics 116(1), 1–22.
38

French,
K.
R.
(2020).
U.S.
Research
Returns
Data.
https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data library.html.
Accessed
2020-12-21.
Friedman, B. M. (1977). Financial ﬂow variables and the short-run determination of long-
term interest rates. Journal of Political Economy 85(4), 661–689.
Friedman, B. M. (1978).
Who puts the inﬂation premium into nominal interest rates?
Journal of Finance 33(3), 833–845.
Gompers, P., J. Ishii, and A. Metrick (2003).
Corporate governance and equity prices.
Quarterly Journal of Economics 118(1), 107–156.
Gompers, P. A. and A. Metrick (2001). Institutional investors and equity prices. Quarterly
Journal of Economics 116(1), 229–259.
Gormsen, N. J. and E. Lazarus (2023). Duration-driven returns. Journal of Finance 78(3),
1393–1447.
Guti´errez, G. and T. Philippon (2017). Declining competition and investment in the U.S.
NBER Working Paper 23583.
Harris, L. and E. Gurel (1986). Price and volume eﬀects associated with changes in the S&P
500 list: New evidence for the existence of price pressures. Journal of Finance 41(4),
815–829.
Hartzmark, S. M. and A. B. Sussman (2019). Do investors value sustainability? a natural
experiment examining ranking and fund ﬂows. Journal of Finance 74(6), 2789–2837.
Hoerl, A. E. and R. W. Kennard (1970). Ridge regression: Biased estimation for nonorthog-
onal problems. Technometrics 12(1), 55–67.
I/B/E/S
International
(2020).
IBES
Academic
Database.
https://wrds-
www.wharton.upenn.edu/. Accessed 2020-12-20.
Institutional
Shareholder
Services
(2020).
Governance
Database.
https://wrds-
www.wharton.upenn.edu/. Accessed 2020-12-21.
Kacperczyk, M. T., S. Sundaresan, and T. Wang (2021). Do foreign institutional investors
improve market eﬃciency? Review of Financial Studies 34(3), 1317–1367.
Koijen, R. S. J. and M. Yogo (2019). A demand system approach to asset pricing. Journal
of Political Economy 127(4), 1475–1515.
39

Krueger, P., Z. Sautner, and L. T. Starks (2020).
The importance of climate risks for
institutional investors. Review of Financial Studies 33(3), 1067–1111.
Lewellen, J. (2011). Institutional investors and the limits of arbitrage. Journal of Financial
Economics 102(1), 62–80.
Livnat, J. and R. R. Mendenhall (2006). Comparing the post-earnings announcement drift
for surprises calculated from analyst and time series forecasts.
Journal of Accounting
Research 44(1), 177–205.
Lucas, Jr., R. E. (1978). Asset prices in an exchange economy. Econometrica 46(6), 1429–
1445.
Makarov, D. and A. Schornick (2010). A note on wealth eﬀect under CARA utility. Finance
Research Letters 7(3), 170–177.
Melitz, M. (2003). The impact of trade on intra-industry reallocations and aggregate industry
productivity. Econometrica 71(6), 1695–1725.
Merton, R. C. (1987). A simple model of capital market equilibrium with incomplete infor-
mation. Journal of Finance 42(3), 483–510.
Morningstar
(2020).
Sustainalytics
ESG
Risk
Rating.
https://wrds-
www.wharton.upenn.edu/. Accessed 2020-12-20.
P´astor, ˇLuboˇs., R. F. Stambaugh, and L. A. Taylor (2021). Sustainable investing in equilib-
rium. Journal of Financial Economics 142(2), 550–571.
Pavlova, A. and T. Sikorskaya (2022). Benchmarking intensity. Review of Financial Stud-
ies 36(3), 859–903.
Pedersen, L. H., S. Fitzgibbons, and L. Pomorski (2021). Responsible investing: The ESG-
eﬃcient frontier. Journal of Financial Economics 142(2), 572–597.
Sammon, M. (2022). Passive ownership and price informativeness. Working paper, Harvard
University.
Schmickler, S. and P. Tremacoldi-Rossi (2022). In good times and in bad: High-frequency
market making design, liquidity, and asset prices. Working paper, Princeton University.
Shleifer, A. (1986). Do demand curves for stocks slope down?
Journal of Finance 41(3),
579–590.
40

S&P Global (2020).
Compustat Fundamentals.
https://wrds-www.wharton.upenn.edu/.
Accessed 2020-12-21.
Stroebel, J. and J. Wurgler (2021). What do you think about climate ﬁnance? Journal of
Financial Economics 142(2), 487–498.
41

Table 1
Largest investors by investor type
Type
Investor
Wealth
Households
8,553
Large-passive IA
The Vanguard Group
2,494
Large-active IA
T. Rowe Price Associates
659
Long-term
Norges Bank Investment Management
292
Small-passive IA
Charles Schwab Investment Management
162
Small-active IA
PRIMECAP Management Company
117
Private banking
Goldman Sachs and Company
112
Hedge funds
Renaissance Technologies
89
Brokers
Schweizerische Nationalbank
84
Foreign
Norges Bank Investment Management
292
Notes: Wealth is US equity holdings in billions of US dollars in 2019.Q4. IA is abbreviation for investment
advisors.
42

Table 2
Firm size distribution
Market equity
Number
Sales
Earnings
percentile
of ﬁrms
percentile
percentile
Panel A: 2019.Q4
10
3
4
6
20
9
12
15
30
19
21
26
40
34
29
40
50
57
34
46
60
97
44
58
70
159
56
69
80
278
68
78
90
541
81
88
100
2,825
100
100
Panel B: 2000.Q1
10
3
2
3
20
8
7
7
30
17
12
15
40
29
16
19
50
48
21
30
60
80
34
47
70
142
42
55
80
274
55
68
90
615
72
83
100
5,137
100
100
Notes: This table reports summary statistics for publicly traded US ﬁrms by deciles of market equity. The
last column is for earnings before interest and taxes from Compustat (S&P Global, 2020).
43

Table 3
Explaining equity valuations and future proﬁtability with ﬁrm characteristics
2010–2019
2000–2019
Characteristic
Market-to-book
Proﬁtability
Market-to-book
Proﬁtability
Environment
0.17
0.06
(5.68)
(2.49)
Governance
−0.10
−0.08
(−3.79)
(−3.67)
Log book equity
−0.65
−0.23
−0.55
−0.20
(−23.89)
(−12.05)
(−25.55)
(−14.00)
Foreign sales
0.11
0.01
0.14
0.04
(5.17)
(0.79)
(8.48)
(3.45)
Lerner
0.08
0.14
0.09
0.16
(3.14)
(7.11)
(4.02)
(11.21)
Sales to book
0.22
0.20
0.21
0.18
(8.12)
(9.31)
(10.21)
(8.97)
Dividends to book
0.17
0.09
0.19
0.07
(8.18)
(5.64)
(11.00)
(5.61)
Market beta
−0.04
−0.03
0.02
−0.00
(−2.40)
(−2.53)
(1.40)
(−0.42)
Adjusted R2
0.65
0.50
0.57
0.38
Adjusted within R2
0.64
0.49
0.55
0.37
Observations
6, 399
2, 102
13, 664
6, 576
Notes: This table reports regressions of log market-to-book equity or proﬁtability on ﬁrm characteristics.
Log market-to-book equity is measured at the end of year t. Proﬁtability is the sum of discounted future
clean-surplus earnings from year t to t + 5. All characteristics are measured in year t and are standardized
within each year. The environmental scores are from Sustainalytics (Morningstar, 2020). The governance
index is the number of entrenchment provisions, following Bebchuk et al. (2009). The environmental scores
and the governance indices are available from 2010 to 2019. The speciﬁcations with these variables include
indicator variables for a missing environmental score or governance index. The Lerner index is the ratio of
operating income after depreciation to sales. All speciﬁcations include year ﬁxed eﬀects. The t-statistics,
based on robust standard errors clustered by ﬁrm, are reported in parentheses.
44

Table 4
Heterogeneity in asset demand by investor type, wealth, and active share
Investor
Log market-
Log book
Foreign
Sales
Dividends
Market
characteristic
Environment
Governance
to-book
equity
sales
Lerner
to book
to book
beta
Panel A: Investor type
Hedge Funds
−1.56
0.70
0.47
0.55
−2.51
0.29
1.81
−13.94
1.20
(−2.35)
(1.59)
(27.15)
(25.74)
(−8.91)
(0.79)
(2.96)
(−26.20)
(2.18)
Investment advisors:
Large-passive
2.25
2.10
0.98
1.38
3.78
0.49
5.00
0.01
1.46
(2.61)
(2.35)
(60.11)
(48.35)
(4.11)
(1.13)
(5.09)
(0.00)
(1.55)
Small-passive
2.82
0.89
0.83
1.16
3.12
3.83
1.81
−2.27
−3.52
(4.73)
(1.12)
(56.32)
(73.16)
(8.09)
(8.62)
(2.79)
(−2.54)
(−6.80)
Small-active
−2.71
−2.71
0.51
0.64
2.80
7.68
−1.48
−8.59
−4.17
(−3.23)
(−3.98)
(27.95)
(27.86)
(5.97)
(11.57)
(−2.30)
(−6.87)
(−5.16)
Large-active
0.72
3.36
0.95
1.26
3.77
0.02
2.17
−13.15
3.43
(0.74)
(3.08)
(58.61)
(43.28)
(3.54)
(0.01)
(1.42)
(−5.21)
(2.53)
Long-Term
0.94
−0.13
0.87
1.25
2.52
3.80
3.53
−2.08
−1.22
(1.48)
(−0.25)
(51.06)
(70.57)
(6.00)
(7.92)
(6.45)
(−3.08)
(−2.13)
Private banking
−4.39
0.22
0.76
1.02
4.61
4.74
0.57
4.49
−8.85
(−2.18)
(0.24)
(23.25)
(15.75)
(6.69)
(3.69)
(0.48)
(2.01)
(−5.19)
Brokers
4.40
−1.87
0.92
1.31
0.59
−0.98
3.66
−1.64
4.88
(4.68)
(−2.56)
(47.09)
(51.51)
(0.81)
(−0.96)
(3.96)
(−1.01)
(2.27)
Adjusted R2
0.08
0.07
0.49
0.59
0.05
0.15
0.07
0.16
0.15
Observations
6, 560
6, 560
7, 959
7, 959
7, 959
7, 959
7, 959
7, 959
7, 959
Panel B: Wealth, active share, and foreign investor
Log wealth share
0.94
1.24
0.11
0.13
0.59
−2.01
0.21
−2.84
2.47
(3.38)
(3.59)
(18.72)
(11.28)
(2.19)
(−6.50)
(0.56)
(−2.51)
(6.62)
Active share
−1.37
−0.14
−0.07
−0.15
−0.06
0.18
−1.51
−4.72
0.37
(−3.91)
(−0.49)
(−7.55)
(−9.71)
(−0.24)
(0.61)
(−4.15)
(−8.84)
(1.05)
Foreign
3.00
−0.79
0.04
0.10
1.92
−0.31
−0.12
0.88
−0.38
(3.81)
(−1.40)
(2.56)
(4.98)
(3.91)
(−0.52)
(−0.19)
(0.97)
(−0.53)
Adjusted R2
0.11
0.04
0.56
0.67
0.02
0.12
0.06
0.13
0.09
Observations
6, 560
6, 560
7, 959
7, 959
7, 959
7, 959
7, 959
7, 959
7, 959
Notes: This table reports regressions of the average demand coeﬃcients on investor characteristics. For each investor, we estimate asset demand on
quarterly holdings pooled by year with quarter ﬁxed eﬀects. The environmental scores are from Sustainalytics (Morningstar, 2020). The governance
index is the number of entrenchment provisions, following Bebchuk et al. (2009). The Lerner index is the ratio of operating income after depreciation
to sales. For each investor, the average demand coeﬃcients are time-series averages over the sample period over which both investor holdings and
ﬁrm characteristics are available (limited to 2010 to 2019 for the environmental score and the governance index). We multiply the demand coeﬃcients
by 100, except those for log market-to-book equity and log book equity. The investor characteristics in Panel A are investor-type ﬁxed eﬀects. The
investor characteristics in Panel B are the log average wealth share, the active share, and a foreign-investor ﬁxed eﬀect. An investor’s wealth is its
total equity holdings. The log average wealth share and the active share are standardized. The regression weighs the observations by the time-series
average of the investor’s wealth share. The t-statistics, based on heteroskedasticity-robust standard errors, are reported in parentheses.
45

Table 5
Impact of climate risk on valuation regressions
Counterfactual
Characteristic
Actual
Stakeholder
Regulatory
Environment
0.23
0.57
0.03
(4.19)
(47.06)
(30.26)
Governance
−0.14
−0.01
−0.00
(−2.24)
(−0.43)
(−1.83)
Log book equity
−0.74
−0.01
−0.00
(−16.39)
(−1.02)
(−1.77)
Foreign sales
0.11
0.00
−0.00
(3.31)
(0.31)
(−0.40)
Lerner
0.11
0.02
−0.00
(2.68)
(1.54)
(−0.34)
Sales to book
0.22
−0.00
−0.00
(4.63)
(−0.41)
(−2.03)
Dividends to book
0.16
0.01
0.00
(4.17)
(1.03)
(2.11)
Market beta
−0.04
0.00
0.00
(−1.26)
(0.67)
(1.81)
Adjusted R2
0.65
0.92
0.81
Observations
540
540
540
Notes: The ﬁrst column is a regression of log market-to-book equity on ﬁrm characteristics in 2019.Q4. The
second and third columns are regressions of the diﬀerence between actual and counterfactual log market-to-
book equity on ﬁrm characteristics. All characteristics are standardized within each year. For stakeholder
risk, asset demand for all institutional investors shifts as the coeﬃcient on the environmental score increases
by 0.1. For regulatory risk, asset demand for only long-term investors shifts as the coeﬃcient on the envi-
ronmental score increases by 0.1. All speciﬁcations include indicator variables for a missing environmental
score or governance index. The t-statistics, based on heteroskedasticity-robust standard errors, are reported
in parentheses.
46

Table 6
Equity repricing for counterfactual outﬂows by investor type
Wealth
Repricing per
Investor type
share (%)
Repricing
dollar wealth
Investment advisors:
Large-passive
17.7
15.9
0.90
Small-passive
16.4
17.2
1.05
Small-active
11.7
26.7
2.28
Large-active
11.1
18.4
1.65
Hedge funds
3.2
11.5
3.58
Long-term
3.9
3.9
1.01
Private banking
2.9
5.3
1.81
Brokers
1.1
1.8
1.56
Foreign
6.1
8.0
1.31
Notes: The ﬁrst column reports the wealth share by investor type. An investor’s wealth is its total equity
holdings. The second column reports the equity repricing for capital ﬂows from the given group of investors
to other institutional investors. Equity repricing is the value-weighted absolute percent change in equity
prices. The last column reports the ratio of equity repricing in the second column to the wealth share in the
ﬁrst column. Each cell is a time-series average of the quarterly estimates from 2000.Q1 to 2019.Q4.
47

Table 7
Valuation regressions for counterfactual outﬂows by investor type
Investment advisors
Large-
Small-
Small-
Large-
Hedge
Long-
Private
Characteristic
Actual
passive
passive
active
active
funds
term
banking
Brokers
Foreign
Environment
0.17
0.17
0.14
0.21
0.16
0.18
0.17
0.17
0.17
0.14
(5.68)
(5.18)
(4.44)
(6.23)
(5.39)
(5.60)
(5.54)
(5.77)
(5.60)
(4.55)
Governance
−0.10
−0.11
−0.11
−0.09
−0.12
−0.09
−0.10
−0.10
−0.10
−0.10
(−3.79)
(−3.64)
(−3.55)
(−2.65)
(−4.79)
(−3.09)
(−3.52)
(−3.69)
(−3.70)
(−3.43)
Log book equity
−0.65
−0.69
−0.73
−0.44
−0.66
−0.59
−0.67
−0.66
−0.65
−0.69
(−23.89)
(−25.44)
(−24.92)
(−14.38)
(−24.44)
(−20.51)
(−24.45)
(−24.44)
(−24.01)
(−24.42)
Foreign sales
0.11
0.13
0.11
0.07
0.10
0.12
0.10
0.11
0.11
0.09
(5.17)
(5.60)
(4.89)
(2.86)
(5.20)
(5.30)
(4.71)
(5.07)
(5.19)
(4.17)
Lerner
0.08
0.08
0.05
0.05
0.09
0.09
0.07
0.07
0.08
0.06
(3.14)
(3.27)
(1.92)
(1.57)
(4.42)
(3.55)
(2.83)
(2.79)
(3.21)
(2.69)
Sales to book
0.22
0.21
0.21
0.26
0.22
0.20
0.21
0.21
0.21
0.21
(8.12)
(7.66)
(7.52)
(8.09)
(8.66)
(7.08)
(7.64)
(8.14)
(8.05)
(7.48)
Dividends to book
0.17
0.12
0.10
0.27
0.19
0.23
0.15
0.14
0.17
0.14
(8.18)
(5.73)
(4.33)
(10.72)
(9.51)
(10.77)
(7.23)
(7.04)
(8.11)
(6.59)
Market beta
−0.04
−0.03
−0.03
−0.05
−0.04
−0.06
−0.04
−0.04
−0.04
−0.03
(−2.40)
(−1.41)
(−1.58)
(−2.74)
(−2.58)
(−3.09)
(−2.20)
(−2.14)
(−2.51)
(−1.56)
Adjusted within R2
0.64
0.61
0.61
0.45
0.65
0.57
0.63
0.63
0.64
0.63
Observations
6, 399
6, 399
6, 399
6, 399
6, 399
6, 399
6, 399
6, 399
6, 399
6, 399
Notes: The ﬁrst column is a regression of the actual log market-to-book equity on ﬁrm characteristics. The remaining columns are regressions of the
counterfactual log market-to-book equity on ﬁrm characteristics. All characteristics are standardized within each year. Each column corresponds to
capital ﬂows from the given group of investors to other institutional investors. All speciﬁcations include year ﬁxed eﬀects and indicator variables for
a missing environmental score or governance index. The t-statistics, based on standard errors clustered by ﬁrm, are reported in parentheses. The
sample period is 2010 to 2019.
48

0.00
0.25
0.50
0.75
1.00
2000
2005
2010
2015
Year
Ownership Share
Type
Households
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Figure 1
Ownership shares by investor type
Notes: This ﬁgure reports the ownership shares for the US stock market by investor type. IA is abbreviation
for investment advisors. The household share is based on shares outstanding minus institutional ownership.
The quarterly sample period is 2000.Q1 to 2019.Q4.
49

Sales to Book
Dividend to Book
Market Beta
Log Book Equity
Foreign Sales
Lerner
Environment
Governance
Log Market-to-Book
-20
-10
0
10
20
-20
0
20
-20
0
20
0.0
0.5
1.0
1.5
-20
-10
0
10
20
-10
0
10
20
30
-20
0
20
-30 -20 -10 0
10 20
0.00 0.25 0.50 0.75 1.00
0.0
0.2
0.4
0.6
0.8
0.0
0.3
0.6
0.9
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
0.0
0.2
0.4
0.6
0.8
0.0
0.2
0.4
0.6
0.8
0.0
0.3
0.6
0.9
Percent of Investors
Type
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Domestic
Foreign
Figure 2
Heterogeneity in asset demand by investor type
Notes: This ﬁgure reports the cross-sectional distribution of the average demand coeﬃcients across investors.
For each investor, we estimate asset demand on quarterly holdings pooled by year with quarter ﬁxed eﬀects.
We then compute the time-series average of the estimated demand coeﬃcients for each investor over the
sample period during which both investor holdings and ﬁrm characteristics are available (limited to 2010 to
2019 for the environmental score and the governance index). Finally, we compute a wealth-weighted average
of the demand coeﬃcients by investor type, in which an investor’s weight is the time-series average of its
wealth share by investor type. An investor’s wealth is its total equity holdings. The colored vertical lines
represent the wealth-weighted average demand coeﬃcients by investor type. IA is abbreviation for investment
advisors. The environmental scores are from Sustainalytics (Morningstar, 2020). The governance index is
the number of entrenchment provisions, following Bebchuk et al. (2009). The Lerner index is the ratio of
operating income after depreciation to sales. We multiply the demand coeﬃcients by 100, except those for
log market-to-book equity and log book equity.
50

Sales to Book
Dividend to Book
Market Beta
Log Market-to-Book
Log Book Equity
Lerner
Environment
Governance
Foreign Sales
Domestic
Foreign
Domestic
Foreign
Domestic
Foreign
0
1
2
3
4
0
1
2
3
4
-3
-2
-1
0
-0.5
0.0
0.5
1.0
0.0
0.3
0.6
0.9
-4
-2
0
0
1
2
3
0.0
0.2
0.4
0.6
0.8
0.0
0.5
1.0
1.5
2.0
Demand Coefficient
Figure 3
Heterogeneity in asset demand between domestic and foreign investors
Notes: This ﬁgure reports the wealth-weighted average demand coeﬃcients for domestic and foreign investors.
An investor’s wealth is its total equity holdings. For each investor, we estimate asset demand on quarterly
holdings pooled by year with quarter ﬁxed eﬀects. We then compute the time-series average of the estimated
demand coeﬃcients for each investor over the sample period during which both investor holdings and ﬁrm
characteristics are available (limited to 2010 to 2019 for the environmental score and the governance index).
Finally, we compute a wealth-weighted average of the demand coeﬃcients by investor type, in which an
investor’s weight is the time-series average of its wealth share by investor type. The environmental scores are
from Sustainalytics (Morningstar, 2020). The governance index is the number of entrenchment provisions,
following Bebchuk et al. (2009). The Lerner index is the ratio of operating income after depreciation to
sales. We multiply the demand coeﬃcients by 100, except those for log market-to-book equity and log book
equity.
51

Panel A. FactSet, 2000-2019
Panel B. Thomson Reuters, 1980-2018
2000
2005
2010
2015
1980
1990
2000
2010
0.30
0.35
0.40
0.45
0.50
Year
Active Share
Figure 4
Aggregate active share
Notes: For each investor, the active share is one-half times the sum of the absolute diﬀerences between the
portfolio weights and the market weights over the set of stocks that are in its investment universe. The
aggregate active share is a wealth-weighted average of the active shares across all institutional investors, in
which an investor’s weight is its wealth as a share of total wealth. An investor’s wealth is its total equity
holdings. This ﬁgure reports an annual average of the quarterly estimates of the aggregate active share.
Panel A is based on FactSet Ownership from 2000.Q1 to 2019.Q4 (FactSet, 2020). Panel B is based on the
Thomson Reuters Institutional Holdings Database for 1980.Q1 to 2018.Q4 (Koijen and Yogo, 2019).
52

-15
-10
-5
-12
-9
-6
-3
Log Wealth Share in 2007
Log Wealth Share in 2016
Panel A
22
23
24
25
26
27
22
23
24
25
26
27
Actual Log Market Equity
Counterfactual Log Market Equity
Panel B
0.00
0.02
0.04
0.06
Actual
Large-Passive IA
Small-Passive IA
Large-Active IA
Small-Active IA
Long-Term
Private Banking
Hedge Funds
Brokers
Price Infromativeness
Panel C
-0.02
0.00
0.02
0.04
-2
0
2
Change in Log Wealth Share
Investor-Level Informativeness
Panel D
Figure 5
Counterfactual market in 2016 under the 2007 wealth distribution
Notes: Panel A is a scatter plot of the log wealth shares in 2007.Q4 versus 2016.Q4. An investor’s wealth
is its total equity holdings. Panel B is a scatter plot of the actual log market equity in 2016.Q4 versus the
counterfactual log market equity under the wealth distribution in 2007.Q4. In the counterfactual, wealth
changes only for institutional investors who exist in both periods. Panel C reports the cumulative eﬀects
on price informativeness when we change the wealth distribution by sequentially adding each investor type.
The range around the point estimate represents the 95% conﬁdence interval. Panel D is a bin scatter plot
of the changes in the log wealth share from 2007.Q4 to 2016.Q4 versus the investor-level informativeness in
2016.Q4.
53

-5
0
5
10
-0.4
-0.2
0.0
0.2
0.4
Coefficient on Environmental Score
Percent Change in Wealth
Panel A
-12
-8
-4
0
4
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Percent Change in Wealth
Stakeholder Risk
Regulatory Risk
Panel B
Figure 6
Impact of climate risk on the wealth distribution across institutional investors
Notes: Panel A is a bin scatter plot of the demand coeﬃcient on the environmental score versus the percent
change in log wealth in response to realized stakeholder risk. An investor’s wealth is its total equity holdings.
Panel B reports the percent change in log wealth by investor type in response to a climate-induced shift in
asset demand. For each investor type, we compute a wealth-weighted average of the log change in wealth, in
which an investor’s weight is its wealth share by investor type. IA is abbreviation for investment advisors.
For stakeholder risk, asset demand for all institutional investors shifts as the coeﬃcient on the environmental
score increases by 0.1. For regulatory risk, asset demand for only long-term investors shifts as the coeﬃcient
on the environmental score increases by 0.1. Each reported value is a time-series average of the quarterly
estimates from 2019.Q1 to 2019.Q4.
54

0
10
20
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Foreign
Percent
Wealth Share
Repricing
Panel A
0
1
2
3
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Foreign
Repricing Per Dollar Wealth
Panel B
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Foreign
0.2
0.4
0.6
1
2
3
Repricing Per Dollar Wealth
Active Share
Panel C
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Foreign
0.0
0.1
0.2
0.3
0.4
0.5
1
2
3
Repricing Per Dollar Wealth
1-b0
Panel D
Figure 7
Equity repricing for counterfactual outﬂows by investor type
Notes: Panel A reports the wealth share by investor type and the equity repricing for capital ﬂows from the
given group of investors to other institutional investors. An investor’s wealth is its total equity holdings.
Equity repricing is the value-weighted absolute percent change in equity prices.
IA is abbreviation for
investment advisors. Panel B reports the equity repricing per dollar of wealth, which is the ratio of equity
repricing to the wealth share. Panel C is a scatter plot of the equity repricing per dollar of wealth versus
the active share by investor type.
For each investor, the active share is one-half times the sum of the
absolute diﬀerences between the portfolio weights and the market weights over the set of stocks that are
in its investment universe. Panel D is a scatter plot of the equity repricing per dollar of wealth versus the
wealth-weighted average of one minus the coeﬃcient on log market equity (i.e., 1 −β0,i,t). Each reported
value is a time-series average of the quarterly estimates from 2000.Q1 to 2019.Q4.
55

Appendix A.
Model solution
We solve a more general version of the model in Section 2 with background risk. We change
investor i’s wealth in period 1 from equation (1) to
Ai,1 = Ai + (d1 −MB)′Qi + Yi,1,
where Yi,1 is exogenous income in period 1. Alternatively, Yi,1 could represent other sources
of background risk including benchmarking or time-varying investment opportunities. As
stated in equation (2), investors choose an optimal portfolio in period 0 to maximize expected
utility.
Investors have heterogeneous expectations about income and believe that it is normally
distributed with mean Ei[Yi,1] and variance Vari(Yi,1). Analogously to beliefs about factor
exposure (4), investor i’s beliefs about the covariance between stock n’s proﬁtability and its
income is
Covi(d1(n), Yi,1) = ΦY ′
i x(n) + φY
i (n).
(A1)
The subscript i on the covariance operator represents heterogeneous beliefs. The investor
forms beliefs based on a vector of observed characteristics x(n) and a scalar φY
i (n), which
represents unobserved (to the econometrician) characteristics of stock n that relates to back-
ground risk.
A.1.
Optimal portfolio choice
Given the normality assumptions, we can write the investor’s objective function as
Ei[−exp(−γiAi,1)] = −exp(−γi(Ai + (μi −MB)′Qi + Ei[Yi,1])
+γ2
i
2 (Q′
i(ρiρ′
i + σ2I)Qi + Vari(Yi,1) + 2Q′
iCovi(d1, Yi,1))

.
The ﬁrst-order condition for optimal portfolio choice is
−(μi −MB) + γi(ρiρ′
i + σ2I)Qi + γiCovi(d1, Yi,1) = 0.
56

We solve for the optimal demand as
Qi = 1
γi
(ρiρ′
i + σ2I)−1(μi −MB −γiCovi(d1, Yi,1))
= 1
γiσ2

I −
ρiρ′
i
ρ′
iρi + σ2

(μi −MB −γiCovi(d1, Yi,1))
= 1
γiσ2(μi −MB −γiCovi(d1, Yi,1) −ciρi).
(A2)
The second line follows from the Woodbury matrix identity. The scalar
ci = ρ′
i(μi −MB −γiCovi(d1, Yi,1))
ρ′
iρi + σ2
is investor speciﬁc but does not vary across stocks. According to equation (A2), asset demand
increases in the expected return μi −MB, decreases in the background risk Covi(d1, Yi,1),
and decreases in the factor exposure ρi if ci > 0. Because of background risk, the investor
decreases allocation to stocks that have a positive covariance with income. Conversely, the
investor increases allocation to stocks that have a negative covariance with income because
they provide hedging beneﬁts.
Finally, we use the assumptions that expected proﬁtability, factor exposure, and the
background risk depend on observed and unobserved characteristics. Substituting equations
(3), (4), and (A1) in equation (A2), we have
Qi(n) =
1
γiσ2
⎛
⎜
⎝−MB(n) + (Φμ
i −γiΦY
i −ciΦρ
i



βi
)′x(n) + φμ
i (n) −γiφY
i (n) −ciφρ
i (n)



ϵi(n)
⎞
⎟
⎠.
(A3)
A special case of this equation without background risk is equation (5).
A.2.
Equity prices with exogenous characteristics
Substituting optimal demand (A3) in market clearing (6), we solve for the equilibrium equity
prices as
MB(n) =

I

i=1
1
γiσ2
−1 
I

i=1
1
γiσ2β′
ix(n) +
I

i=1
1
γiσ2ϵi(n) −B(n)

.
Equation (7) follows from the assumption that γi = 1/(τiAi).
57

A.3.
Equity prices with endogenous characteristics
In an extended version of the model, we allow the observed characteristics to depend on
market-to-book equity as
x(n) = ψ + ΨMB(n) + ν(n).
(A4)
The vector Ψ determines how the ﬁrm characteristics endogenously respond to equity prices.
The vector ν(n) represents an exogenous component of ﬁrm characteristics that relates to
technology or other factors that the ﬁrm does not control. Substituting equation (A4) into
equation (7), we solve for the equilibrium equity prices as
MB(n) = β
′(ψ + ν(n)) + ϵ(n)
1 −β
′Ψ
.
(A5)
This model has an important implication for the identiﬁcation of asset demand (5). Equa-
tions (A4) and (A5) imply that the observed characteristics depend on ϵ(n), which is the
weighted average of latent demand. Consequently, the identifying assumption that the ob-
served characteristics are uncorrelated with latent demand is no longer justiﬁed. However, we
could estimate asset demand through a two-step estimator that we describe in Appendix D.3.
In the ﬁrst step, we estimate equation (A4) by ordinary least squares. In the second step,
we estimate equation (5) by using the estimated residuals ν(n) as instruments for x(n).
Appendix B.
Data construction
B.1.
Institutional equity holdings
We construct institutional equity holdings at the end of each quarter from 2000.Q1 to
2019.Q4, based on FactSet Ownership (FactSet, 2020). The data come from SEC Form
13F ﬁlings, which are required for all institutional investment managers who exercise in-
vestment discretion on accounts holding 13(f) securities that exceed $100 million in total
market value. We exclude the holdings for two FactSet entity identiﬁers (0FSVG4-E and
000V4B-E), which contain known errors in comparison with the EDGAR 13F ﬁlings. We
compute the dollar amount of holdings by multiplying the number of shares by the price per
share.
We classify investors based on FactSet’s investor subtype codes. They are investment
advisors (IC, RE, PP, SB, and MF), hedge funds (AR, FH, FF, FU, and FS), long-term
investors (FO, SV, and IN), private banking (CP, FY, and VC), and brokers (BM, IB, ST,
and MM). FactSet classiﬁes an investment ﬁrm as a mutual fund if the majority of its
58

investments are in mutual funds. Otherwise, FactSet classiﬁes an investment ﬁrm as an
investment advisor if it is not a subsidiary of a bank, a brokerage ﬁrm, or an insurance
company.
We group mutual funds together with investment advisors because FactSet’s
distinction is not as economically meaningful.
We aggregate as an outside asset any ﬁrm that is in the bottom 10% of the market equity
distribution or has a missing characteristic (i.e., book equity, foreign sales share, the Lerner
index, the ratio of sales to book equity, the ratio of dividends to book equity, or market
beta). We aggregate into the household sector any small institutional investor who has less
than $10 million in total equity holdings, less than $1 million in the outside asset, or fewer
than ten stocks.
B.2.
Firm characteristics
Financial statements are from the Compustat Fundamentals Annual and Quarterly Databases
(S&P Global, 2020). We use the ﬁnancial statements closest to the end of each quarter, pri-
oritizing the annual statements if available and otherwise using the quarterly statements.
We merge the CRSP data in a given trading month to the Compustat data as of at least six
months and no more than 18 months prior. The lag of at least six months ensures that the
ﬁnancial statements were publicly available on the trading date.
We merge the institutional holdings and shares outstanding from FactSet with the CRSP-
Compustat data by CUSIP. We merge ﬁrms with the most recently available environmental
score of no more than 18 months prior by Capital IQ identiﬁer and CUSIP. We merge ﬁrms
with the most recently available governance index of no more than 18 months prior by
CUSIP.
We deﬁne the following ﬁrm characteristics, based on the deﬁnitions in Fama and French
(2015). The Compustat item codes corresponding to the variables are in parentheses.
• Book equity: Stockholders equity (seq) plus deferred taxes and investment tax credit
(txditc) minus preferred stock (pstk).
• Foreign sales share: Foreign sales divided by the sum of domestic and foreign sales. We
identify domestic (geotp 2) and foreign (geotp 3) segments based on the Compustat
Segments Database.
Foreign sales are the sum of the export sales (salexg) of the
domestic segments and the sales (sale) of the foreign segments. Total sales are the sum
of sales (sale) and export sales (salexg) across all segments. We set missing values to
zero.
• Lerner index: Operating income before depreciation (oibdp) minus depreciation (dp)
divided by sales (sale).
59

• Ratio of sales to book equity: Sales (sale) divided by book equity.
• Ratio of dividends to book equity: Annual dividends per split-adjusted share times
shares outstanding (csho) divided by book equity.
• Market beta: Estimated from a 60-month rolling regression of excess stock returns on
the excess value-weighted index returns (French, 2020). Excess returns are relative to
the one-month Treasury bill.
• Investment: Annual change in log assets (at).
• Ratio of net repurchases to book equity: Purchase of common and preferred stock
(prstkc) minus sale of common and preferred stock (sstk) divided by book equity. If
either the purchase or the sale of common and preferred stock is missing, we set it to
zero.
• Earnings before interest and taxes: Sales (sale) minus the cost of goods sold (cogs)
minus selling, general, and administrative expenses (xsga) minus depreciation (dp).
• Clean-surplus earnings: Change in book equity from year t −1 to t plus purchase of
common and preferred stock (prsckc) minus sale of common and preferred stock (sstk)
plus dividends.
• Proﬁtability: Let Et be clean-surplus earnings in year t. Let Bt be book equity at the
end of year t. Log proﬁtability in year t is et = log(1+Et/Bt−1). Five-year proﬁtability
from year t + 1 to t + 5 is et+1,t+5 = 
5
s=1 0.95s−1et+s.
We winsorize the ratio of dividends to book equity and the ratio of sales to book equity
at the 97.5 percentile within each quarter. We winsorize the Lerner index, market beta, in-
vestment, and proﬁtability at the 2.5 and 97.5 percentiles within each quarter. Furthermore,
we truncate the left tail of the Lerner index at −1.
B.3.
Earnings surprises
Following Livnat and Mendenhall (2006), we construct earnings surprises as the actual earn-
ings per share minus the median forecast divided by the price per share. The actual earnings
per share are from the IBES Actuals Database (I/B/E/S International, 2020). The earnings
forecasts are from the IBES Unadjusted Detail Database, where we select the latest fore-
cast for each analyst within 90 days of the earnings announcement. The price per share is
from the Compustat Fundamentals Quarterly Database. We construct the data through the
following procedure.
60

1. Based on the ibes.id ﬁle, construct a list of IBES tickers and CUSIPs for US ﬁrms.
Keep only the most recent sdates for each ticker-CUSIP pair. Merge permno from
the crsp.stocknames ﬁle by CUSIP. Merge gvkey from the crsp.ccmxpf linktable ﬁle by
permno if usedﬂag is 1 and linkprim is P or C.
2. In the IBES Unadjusted Detail ﬁle (ibes.detu epsus), select quarterly forecasts for the
current and the next ﬁscal quarter (i.e., fpi is 6 or 7).
3. Merge the data from steps 1 and 2 by CUSIP, ensuring that anndats is between linkdt
and linkenddt.
4. Keep the latest forecast for each group formed by ticker, forecast period end date
(fpedats), broker (estimator), and analyst (analys).
5. In the IBES Actuals ﬁle (ibes.actu epsus), select quarterly earnings per share (i.e.,
pdicity is QTR) and merge with the data from step 4 by ticker and forecast period
end date. Keep only the forecasts issued within 90 days of the report date (i.e., 0 <
repdats −anndats ≤90).
6. Adjust the forecasts and the earnings per share to be in the same stock-split basis, using
the CRSP adjustment factor (cfacshr in the ecrsp.dsf ﬁle). Align both the forecast date
and the announcement date with the closest preceding trading date in CRSP.
7. Compute the median forecast by ticker and forecast period end date.
8. Merge the data from step 7 and the price per share (prccq) from the Compustat
Fundamentals Quarterly ﬁle, ensuring that datadate is between linkdt and linkenddt.
Compute the earnings surprise as the actual earnings per share minus the median
forecast divided by the price per share.
For stocks that do not have earnings forecasts, we construct an indicator variable that is
equal to one if the earnings surprise is missing. We set missing values to zero and include
the indicator variable for a missing earnings surprise in the regressions.
Appendix C.
Instrumental variables ridge estimator of asset demand
We rewrite equation (17) as
E
 
δi,t(n) exp(−β′
iXt(n)) −1

Xt(n)
!
−Di

βi −β

= 0,
(C1)
61

where
βi =

αi
β1,i

, β =

0
β1

, Xt(n) =

et
xt(n)

, Di =
λ
|Ni|ξ

0
0
0
I

.
Ignoring the zero holdings, we obtain an initial estimate βi(1) by estimating asset demand
(15) in logarithms. The corresponding moment condition is
E
 
log

δi,t(n)

−βi(1)′Xt(n)

Xt(n)
!
−Di

βi(1) −β

= 0.
The estimator that solves this moment condition is
βi(1) = (E[Xt(n)Xt(n)′] + Di)−1 
E
 
log

δi,t(n)

Xt(n)
!
+ Diβ

.
A ﬁrst-order Taylor approximation of equation (C1) around βi(2) ≈βi(1) is
E
 
δi,t(n) exp(−βi(1)′Xt(n)) −1

Xt(n)
!
−Di

βi(1) −β

−

E
 
δi,t(n) exp(−βi(1)′Xt(n))Xt(n)Xt(n)′!
+ Di

(βi(2) −βi(1)) = 0.
This equation implies that
βi(2) =βi(1) +

E
 
δi,t(n) exp(−βi(1)′Xt(n))Xt(n)Xt(n)′!
+ Di
−1
×

E
 
δi,t(n) exp(−βi(1)′Xt(n)) −1

Xt(n)
!
−Di

βi(1) −β

.
We iterate on this equation until convergence, limiting the step size to the range [−1, 1] for
numerical stability. The estimator satisﬁes moment condition (C1) upon convergence.
Appendix D.
Robustness of the identifying assumptions
We test whether our results are robust to three components of the identifying assumptions:
the deﬁnition of the investment universe, the choice of ﬁrm characteristics, and the exogeneity
of ﬁrm characteristics. Our criteria for robustness are the estimated demand coeﬃcients
and their impact on the counterfactual equity prices, price informativeness, and the wealth
distribution in the applications of Sections 6–8.
62

D.1.
Deﬁnition of the investment universe
The baseline deﬁnition of the investment universe is the set of stocks that an investor cur-
rently holds or has ever held in the past 11 quarters. We test whether our results are robust
to changing the deﬁnition in three ways. First, we construct the instrument without hedge
funds to address the concern that their investment universe may adjust more to changing be-
liefs about future proﬁtability than that of other institutional investors. Second, we change
the window for estimating the investment universe, both backward and forward by up to
ﬁve years. Third, we randomly increase the number of stocks in the investment universe by
up to 100%.
D.1.1.
Instrument without hedge funds
Hedge funds’ investment universe may adjust more to changing beliefs about future prof-
itability than that of other institutional investors. Therefore, we exclude hedge funds in
constructing the instrument for log market equity. Panel A of Figure D2 is a scatter plot of
the estimated coeﬃcient on log market-to-book equity under the baseline instrument versus
an alternative instrument without hedge funds. The two sets of estimated coeﬃcients have a
correlation of 0.985, which conﬁrms that our estimates are robust to excluding hedge funds.
D.1.2.
Changing the window for the investment universe
Koijen and Yogo (2019) chose a three-year window to estimate the investment universe, based
on the fact that the set of stocks that an investor has ever held stabilizes with suﬃcient lags.
We change the window for estimating the investment universe, both backward and forward
by up to ﬁve years. Figure D1 reports the wealth-weighted coeﬃcient on log market-to-book
equity in 2010 by investor type for alternative windows. The alternative windows are labeled
[b, f], which means going back b years and going forward f years. The baseline window is
[3, 0], which means going back three years (or 12 quarters inclusive of the current quarter).
Although we see small variation around the baseline window for small-active investment
advisors and households, our estimates are suﬃciently robust to changing the window for
estimating the investment universe.
D.1.3.
Expanding the investment universe
For each investor-quarter, we randomly increase the number of stocks in the investment
universe by 10%, 25%, 50%, and 100%. For investors whose investment universe is already
close to the universe of inside assets (i.e., the largest 90% of ﬁrms by market equity), their
investment universe is equal to the universe of inside assets. Under the null hypothesis that
63

the baseline investment universe is valid, adding a random set of stocks would only weaken
the instrument. Panel B of Figure D2 is a scatter plot of the estimated coeﬃcient on log
market-to-book equity under the baseline instrument versus an alternative instrument with
a 25% larger investment universe. The two sets of estimated coeﬃcients have a correlation
of 0.921, which conﬁrms that our estimates are robust to expanding the investment universe.
For each expansion size, we reestimate the asset demand system on ten random samples
to make sure that the results do not depend on a particular draw. Based on the reestimated
demand system, we test the robustness of the three applications on the transition from
active to passive investment management, climate-induced shifts in asset demand, and cross-
sectional asset pricing. For the transition from active to passive investment management,
Panel C of Figure 5 is the baseline result on price informativeness. Figure D3 shows that
the results are robust to expanding the investment universe. The four rows correspond to
expanding the investment universe by 10%, 25%, 50%, and 100%. The red line represents
the baseline estimate. The ten bars in each panel correspond to the ten random samples.
For climate-induced shifts in asset demand, Figure 6 is the baseline result on the wealth
distribution across institutional investors. Figure D4 shows that the results are robust to
expanding the investment universe.
For cross-sectional asset pricing, Panel A of Figure 7 is the baseline result on equity
repricing by investor type. Figure D5 shows that the results are robust to expanding the
investment universe.
D.2.
Choice of ﬁrm characteristics
We test whether our results are robust to the choice of ﬁrm characteristics by adding three
characteristics: investment, the ratio of net repurchases to book equity, and earnings sur-
prises. Appendix B describes how we construct these characteristics.
Table D1 adds the three characteristics to the panel regressions of log market-to-book
equity and future proﬁtability in Table 3. The additional characteristics explain log market-
to-book equity with statistically signiﬁcant t-statistics. However, the adjusted within R2
increases only modestly from 64% to 68%. Of the additional characteristics, investment and
the ratio of net repurchases to book equity are statistically signiﬁcant predictors of future
proﬁtability. However, the adjusted within R2 increases only modestly from 49% to 50%.
Thus, the additional characteristics do not signiﬁcantly increase the explanatory power for
log market-to-book equity or future proﬁtability.
Panel C of Figure D2 is a scatter plot of the estimated coeﬃcient on log market-to-book
equity under the baseline speciﬁcation versus an alternative speciﬁcation with the additional
characteristics.
The two sets of estimated coeﬃcients have a correlation of 0.994, which
64

conﬁrms that our estimates are robust to the additional characteristics.
Based on the reestimated demand system, we test the robustness of the three applications
on the transition from active to passive investment management, climate-induced shifts in
asset demand, and cross-sectional asset pricing. For the transition from active to passive
investment management, Panel C of Figure 5 is the baseline result on price informativeness.
Figure D6 shows that the results are robust to the additional characteristics.
For climate-induced shifts in asset demand, Figure 6 is the baseline result on the wealth
distribution across institutional investors. Figure D7 shows that the results are robust to
the additional characteristics.
For cross-sectional asset pricing, Panel A of Figure 7 is the baseline result on equity
repricing by investor type. Figure D8 shows that the results are robust to the additional
characteristics.
D.3.
Identiﬁcation with endogenous characteristics
We relax the baseline assumption that ﬁrm characteristics other than log market-to-book
equity are exogenous. Our starting point is to split the ﬁrm characteristics into a subvector
x1,t(n) of endogenous characteristics and a subvector x2,t(n) of exogenous characteristics.
The endogenous characteristics relate to ﬁrm decisions that could depend on equity prices,
such as capital structure or payout policy. The exogenous characteristics primarily relate to
productivity and market power, which do not directly depend on equity prices.
We model the vector of endogenous characteristics as a function of log market-to-book
equity and the exogenous characteristics as
x1,t(n) = ψ + Ψ1mbt(n) + Ψ2x2,t(n) + νt(n).
(D2)
The vector νt(n) represents an exogenous component of ﬁrm characteristics that relate to
technology or other factors that the ﬁrm does not control. Then our identifying assumptions
are
E[νt(n)|mbt(n), x2,t(n)] = 0,
E[ϵi,t(n)|zi,t(n), νt(n), x2,t(n)] = 1.
(D3)
These moment conditions allow us to estimate asset demand consistently through a two-
step estimator. In the ﬁrst step, we estimate equation (D2) by ordinary least squares. We
denote the vector of estimated residuals as νt(n). In the second step, we estimate asset
demand (15) by generalized method of moments based on moment condition (D3), using the
65

estimated residuals νt(n) as the instruments.
We test the importance of endogenous characteristics by treating the ratio of dividends to
book equity as endogenous and the remaining characteristics as exogenous. In the Q-theory of
investment, investment depends on the equity price. The ﬁrm saves proﬁts net of investment
as retained earnings or pays them out to shareholders. Thus, dividends plausibly depend on
the equity price through investment. Other characteristics in our baseline speciﬁcation, such
as the foreign sales share or the Lerner index, relate to productivity and market power that
are plausibly exogenous. Of course, one could argue that all characteristics are ultimately
endogenous. We simply test the robustness of the baseline assumption to endogenizing one
characteristic. However, our identiﬁcation strategy is suﬃciently general to apply to a model
with more endogenous characteristics in future work.
Panel D of Figure D2 is a scatter plot of the estimated coeﬃcient on log market-to-book
equity under the baseline assumption versus an alternative assumption that is robust to
endogeneity of the ratio of dividends to book equity. The two sets of estimated coeﬃcients
have a correlation of 0.996, which conﬁrms that our estimates are robust to this form of
endogeneity. When ﬁrm characteristic k is endogenous, the baseline assumption leads to a
biased estimate β0,i,t + β1,i,t(k)Ψ1 for the coeﬃcient on log market-to-book equity. The bias
is small as long as Ψ1, which is the endogenous response of the ﬁrm characteristic to log
market-to-book equity, is small. Consistent with this intuition, we ﬁnd a small estimate of
Ψ1 when we estimate equation (D2) for the ratio of dividends to book equity.
66

Table D1
Explaining equity valuations and future proﬁtability with ﬁrm characteristics:
Robustness to additional characteristics
Additional characteristics
Baseline characteristics
Characteristic
Market-to-book
Proﬁtability
Market-to-book
Proﬁtability
Environment
0.15
0.06
0.17
0.06
(5.70)
(2.51)
(5.63)
(2.48)
Governance
−0.08
−0.07
−0.10
−0.08
(−3.11)
(−3.31)
(−3.81)
(−3.69)
Log book equity
−0.68
−0.25
−0.65
−0.23
(−24.22)
(−11.98)
(−23.82)
(−11.94)
Foreign sales
0.09
0.00
0.11
0.01
(4.97)
(0.22)
(5.17)
(0.78)
Lerner
0.06
0.13
0.08
0.14
(2.84)
(7.04)
(3.13)
(7.11)
Sales to book
0.20
0.20
0.22
0.20
(8.04)
(9.13)
(8.08)
(9.28)
Dividends to book
0.17
0.09
0.17
0.09
(9.21)
(5.87)
(8.21)
(5.65)
Market beta
−0.03
−0.03
−0.04
−0.03
(−2.10)
(−2.13)
(−2.41)
(−2.53)
Investment
0.14
0.02
(11.32)
(2.12)
Repurchases to book
0.17
0.04
(5.27)
(3.83)
Earnings surprises
−0.03
−0.01
(−3.37)
(−0.80)
Adjusted R2
0.69
0.51
0.65
0.50
Adjusted within R2
0.68
0.50
0.64
0.49
Observations
6, 395
2, 101
6, 395
2, 101
Notes: This table reports regressions of log market-to-book equity or proﬁtability on ﬁrm characteristics
including additional characteristics: investment, the ratio of net repurchases to book equity, and earnings
surprises. Log market-to-book equity is measured at the end of year t. Proﬁtability is the sum of discounted
future clean-surplus earnings from year t to t + 5.
All characteristics are measured in year t and are
standardized within each year.
All speciﬁcations include year ﬁxed eﬀects and indicator variables for a
missing environmental score, governance index, or earnings surprise. We restrict the sample to stocks with
nonmissing investment. The sample period is 2010 to 2019. The t-statistics, based on robust standard errors
clustered by ﬁrm, are reported in parentheses.
67

Private Banking
Brokers
Households
Large-Active IA
Hedge Funds
Long-Term
Large-Passive IA
Small-Passive IA
Small-Active IA
[1,1]
[1,0]
[2,2]
[2,0]
[3,3]
[3,0]
[4,4]
[4,0]
[5,5]
[5,0]
[1,1]
[1,0]
[2,2]
[2,0]
[3,3]
[3,0]
[4,4]
[4,0]
[5,5]
[5,0]
[1,1]
[1,0]
[2,2]
[2,0]
[3,3]
[3,0]
[4,4]
[4,0]
[5,5]
[5,0]
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
0.00
0.25
0.50
0.75
1.00
Window
Coefficient on Log Market-to-Book Equity
Figure D1
Coeﬃcient on log market-to-book equity:
Robustness to expanding the investment universe
Notes: The asset demand system is reestimated by changing the window for estimating the investment
universe to [b, f] (i.e., going back b years and forward f years). The baseline window is [3, 0], which means
going back three years (or 12 quarters inclusive of the current quarter). For each investor, we estimate asset
demand on quarterly holdings pooled by year with quarter ﬁxed eﬀects. The bars represent the time-series
average of the wealth-weighted coeﬃcient on log market-to-book equity.
68

Panel C. Additional Characteristics
Panel D. Endogenous Characteristics
Panel A. Without Hedge Funds
Panel B. Larger Investment Universe
-2
-1
0
1
-2
-1
0
1
-2
-1
0
1
-2
-1
0
1
Baseline Estimate
Alternative Estimate
Figure D2
Baseline versus alternative estimates of the coeﬃcient on log market-to-book equity
Notes: This ﬁgure compares the baseline estimates of the coeﬃcient on log market-to-book equity versus
four sets of alternative estimates. In Panel A, we construct the instrument for log market equity without
hedge funds. In Panel B, we increase the number of stocks in the investment universe randomly by 25%.
In Panel C, we add investment, the ratio of net repurchases to book equity, and earnings surprises to the
baseline speciﬁcation. In Panel D, we use a weaker identifying assumption that is robust to endogeneity in
the ratio of dividends to book equity.
69

Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
0.1
0.25
0.5
1
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
0.00
0.01
0.02
0.03
0.04
0.05
0.00
0.01
0.02
0.03
0.04
0.05
0.00
0.01
0.02
0.03
0.04
0.05
0.00
0.01
0.02
0.03
0.04
0.05
Random Sample
Price Informativeness
Expansion in Investment Universe
Figure D3
Counterfactual price informativeness in 2016 under the 2007 wealth distribution:
Robustness to expanding the investment universe
Notes: We reestimate the asset demand system by randomly increasing the number of stocks in the investment universe. The columns correspond
to the cumulative eﬀects on price informativeness when we change the wealth distribution from that in 2016.Q4 to 2007.Q4 by sequentially adding
each investor type. The rows correspond to expanding the investment universe by 10%, 25%, 50%, and 100%. The red lines represent the baseline
estimates from Panel C of Figure 5. The ten bars in each panel represent ten random samples.
70

Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
0.1
0.25
0.5
1
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
-10
-5
0
-10
-5
0
-10
-5
0
-10
-5
0
Random Sample
Percent Change in Wealth
Expansion in Investment Universe
Figure D4
Impact of climate risk on the wealth distribution across institutional investors:
Robustness to expanding the investment universe
Notes: We reestimate the asset demand system by randomly increasing the number of stocks in the investment universe. The columns correspond
to the percent change in total wealth by investor type in response to a climate-induced shift in asset demand due to stakeholder risk. The rows
correspond to expanding the investment universe by 10%, 25%, 50%, and 100%. The red lines represent the baseline estimates from Figure 6. The
ten bars in each panel represent ten random samples.
71

Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
0.1
0.25
0.5
1
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
1 2 3 4 5 6 7 8 910
0
10
20
30
0
10
20
30
0
10
20
30
0
10
20
30
Random Sample
Repricing
Expansion in Investment Universe
Figure D5
Equity repricing for counterfactual outﬂows by investor type:
Robustness to expanding the investment universe
Notes: We reestimate the asset demand system by randomly increasing the number of stocks in the investment universe. The columns represent the
equity repricing for capital ﬂows from the given group of investors to other institutional investors. The rows correspond to expanding the investment
universe by 10%, 25%, 50%, and 100%. The red lines represent the baseline estimates from Panel A of Figure 7. The ten bars in each panel represent
ten random samples.
72

0.00
0.01
0.02
0.03
0.04
0.05
Actual
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Price Infromativeness
Baseline
Additional Characteristics
Figure D6
Counterfactual price informativeness in 2016 under the 2007 wealth distribution:
Robustness to additional characteristics
Notes: We reestimate the asset demand system by adding investment, the ratio of net repurchases to book
equity, and earnings surprises to the baseline speciﬁcation. This ﬁgure reports the cumulative eﬀects on price
informativeness when the wealth distribution is changed from that in 2016.Q4 to 2007.Q4 by sequentially
adding each investor type. The baseline estimates are from Panel C of Figure 5.
73

-12
-8
-4
0
4
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Percent Change in Wealth
Baseline
Additional Charateristics
Figure D7
Impact of climate risk on the wealth distribution across institutional investors:
Robustness to additional characteristics
Notes: We reestimate the asset demand system by adding investment, the ratio of net repurchases to book
equity, and earnings surprises to the baseline speciﬁcation. This ﬁgure reports the percent change in total
wealth by investor type in response to a climate-induced shift in asset demand due to stakeholder risk. The
baseline estimates are from Figure 6.
74

0
10
20
Large-Passive IA
Small-Passive IA
Small-Active IA
Large-Active IA
Hedge Funds
Long-Term
Private Banking
Brokers
Repricing
Baseline
Additional Characteristics
Figure D8
Equity repricing for counterfactual outﬂows by investor type:
Robustness to additional characteristics
Notes: We reestimate the asset demand system by adding investment, the ratio of net repurchases to book
equity, and earnings surprises to the baseline speciﬁcation.
This ﬁgure reports the equity repricing for
capital ﬂows from the given group of investors to other institutional investors. The baseline estimates are
from Panel A of Figure 7.
75
