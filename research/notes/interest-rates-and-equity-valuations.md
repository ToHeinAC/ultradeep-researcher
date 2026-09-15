---
title: Interest Rates and Equity Valuations∗
id: interest-rates-and-equity-valuations
tags:
- apple-earnings-durability-thesis-b8b3f1
- equity-duration
- discount-rate-sensitivity
- pure-discounting
created: '2026-09-13T06:07:26.595335Z'
updated: '2026-09-15T19:32:22.129056Z'
source: https://ebenlazarus.github.io/RatesEquity.pdf
source_domain: ebenlazarus.github.io
fetched_at: '2026-09-13T06:07:26.594913Z'
fetch_provider: crawl4ai
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'Gormsen & Lazarus (NBER w34814, full text July 2026 draft, formerly circulated
  as ''Equity Duration and Interest Rates'') decompose real-rate changes into three
  structural drivers -- expected growth, risk/uncertainty, and ''pure discounting''
  (a time-preference-like shock) -- and show only the pure-discounting component transmits
  one-for-one to equity valuations, with weak-to-negative transmission from growth
  and risk shocks. This resolves the ''stock-yield disconnect'': across G7 countries
  the raw change in equity yield since 1990 is essentially uncorrelated with the change
  in trend real rates (adj. R^2 = -0.02), but is tightly related to the pure-discounting
  component alone (slope 1.1, adj. R^2 = 0.79). CENTRAL ESTIMATES: pure discounting
  explains 80% of cross-country valuation changes since 1990; in the U.S. specifically,
  only 35% of the post-1990 real-rate decline (roughly 1 of ~3 percentage points)
  is attributable to pure discounting -- the rest reflects growth/risk shocks that
  do not mechanically re-rate equities. Cross-sectional duration analysis (using IBES
  analyst long-term-growth forecasts to sort five duration quintiles, following Gormsen
  & Lazarus 2023): regressing 3-year returns on 3-year changes in the pure-discounting
  term gives a slope of about -10 for the shortest-duration quintile versus about
  -30 for the longest-duration quintile -- implied cash-flow duration differs by a
  factor of about 3x, with a lower bound of about 20 years'' difference between longest
  and shortest quintiles (1990-2023 US sample). CRITICALLY: when the same portfolios
  are regressed on the RAW (undecomposed) 10-year nominal yield rather than the pure-discounting
  term, loadings are small and even wrong-signed for all quintiles -- i.e., ''equity
  duration does not correspond to the price sensitivity of equity to an arbitrary
  change in interest rates,'' only to its sensitivity to pure-discounting shocks specifically.
  Applied to the value premium: a naive 30-year duration gap between growth and value
  at a 3pp rate decline would imply ~90pp relative growth outperformance, but since
  only ~1pp of that decline is pure discounting and the actual duration spread is
  well under 30 years, the actual pure-discounting contribution to HML''s post-1990
  underperformance is much smaller than the naive calculation suggests (quantified
  in Figure 9). The paper does not analyze Apple or any single mega-cap name; findings
  are at the market/portfolio level.'
raw_file: raw/interest-rates-and-equity-valuations.pdf
utility_score: 16.0
---

*Suggested by [[interest-rates-and-equity-valuations-nber]] — author-hosted full-text PDF of NBER w34814 abstract page*

Interest Rates and Equity Valuations∗
Niels Joachim Gormsen and Eben Lazarus
July 2026
Abstract
How do changes in interest rates affect equity valuations? The impact depends on the
underlying driver of the rate change. We decompose real-rate changes into three drivers:
expected growth, risk, and “pure discounting.” Only pure-discounting shocks should
transmit one-for-one to valuations, with weak-to-negative transmission from growth
and risk. Using survey forecasts and asset prices, we estimate that pure-discounting
shocks indeed transmit one-for-one to equity and explain 80% of cross-country valuation
changes since 1990. Only 35% of the post-1990 U.S. rate decline, however, reflects pure
discounting. We use our decomposition to study cross-sectional rate exposures, the
equity premium, and monetary policy.
Keywords: Stock prices, interest rates, duration, long-term growth
JEL Codes: G10, G12, E44, F30
∗An early draft of this paper circulated as “Equity Duration and Interest Rates.” We thank Andy Atkeson,
Jules van Binsbergen, John Campbell, Mike Chernov, Max Croce, Darrell Duffie, Mihir Gandhi, Matthieu
Gomez, Dan Greenwald, Sam Hanson, Magnus Irie, Rohan Kekre, Amir Kermani, Ralph Koijen, Martin
Lettau, Sydney Ludvigson, Hanno Lustig, Ian Martin, Peter Maxted, Stefan Nagel, Emi Nakamura, Lasse
Pedersen, Rob Rogers, Alexi Savov, David Sraer, Jón Steinsson, Luis Viceira, Jessica Wachter, Olivier Wang,
and seminar participants at Princeton, Stanford GSB, NYU, UCLA, HEC Montréal, UC Berkeley, Copenhagen
Business School, Chicago Booth, the SF Fed, the ECB, Arrowstreet Capital, the Annual Valuation Workshop,
the BI-SHoF Conference, and the NBER SI Asset Pricing Meeting for very helpful comments. We thank
the Fama-Miller Center, Fama Faculty Fellowship, and Danish National Research Foundation (grant no.
DNRF167 and DNRF199) for financial support. Gormsen is at Copenhagen Business School, the University
of Chicago, NBER, CEPR, and the Danish Finance Institute, and Lazarus is at the Haas School of Business,
University of California, Berkeley, and NBER. Contact: njg.fi@cbs.dk and lazarus@berkeley.edu.


---

1.
Introduction
Advanced economies’ long-term interest rates have declined significantly in recent decades.
How do such changes in rates transmit to equity valuations? A potentially tempting line of
reasoning is to assume that equity discount rates move one-for-one with interest rates; since
equity is a long-term asset whose value is highly sensitive to discount rates, this assumption
implies that stock valuations should have increased substantially as a result of the secular
decline in interest rates. High-level evidence might appear consistent with this view: in the
U.S., for example, the market’s equity yield has declined substantially in recent decades,
corresponding to a large increase in equity valuations over this period.
Empirically, however, there is no clear relationship between long-term changes in equity
valuations and interest rates. The left panel of Figure 1 presents one view of this stock–yield
disconnect: across G7 economies, the change in a country’s equity yield since 1990 is effectively
completely unrelated to that country’s change in the trend long-term real rate r∗, described
further below. In addition to the example in Figure 1, it is well known that the correlation
between stock and bond returns is weak and often negative (e.g., Campbell, Sunderam, and
Viceira 2017) — another example of the stock–yield disconnect.
The apparent stock–yield disconnect arises because the interest-rate sensitivity of stock
prices is more complicated than alluded to in our opening paragraph. Interest rates are
determined endogenously and may decline for multiple possible structural reasons, each of
which may affect equity differently. Interest rates may, for instance, decline because of a
decrease in expected growth rates in the economy, which — keeping all else constant — will
decrease equity prices and thus mute the effects of the decline in interest rates on equity.
In this paper, we provide a framework and measurement approach to control for the
underlying drivers of interest-rate movements and estimate the interest-rate sensitivity of
equity prices. We start with a simple but general theoretical decomposition under which
any change in trend real rates can be split into three mutually exclusive shocks: a change in
expected growth, a change in uncertainty, and a “pure discounting” shock akin to a change in
the rate of time preference. We then characterize how these shocks transmit to equity yields,
the inverse of equity valuation ratios. The pure discounting shock transmits one-for-one from
rates to equity yields, inducing perfect comovement between stocks and duration-matched
bonds. But the remaining terms induce a weak and ambiguous relationship between stocks and
bonds: a growth-rate shock affects both equity discount rates and cash-flow growth, while an
uncertainty shock causes interest rates and equity risk premia to move in opposing directions.
Isolating the pure discounting component of real rates is therefore key for understanding how
much any given change in interest rates has passed through to equities.
1


---

Figure 1: Preview of Main Results: Long-Term Decomposition
CAN
DEU
FRA
GBR
ITA
JPN
USA
-3
-2
-1
0
1
2
Δequity yield
-4
-3.5
-3
-2.5
-2
-1.5
Δr* (1990–2023, %)
Adj. R2 = -0.02 
Stock–Yield Disconnect
CAN
DEU
FRA
GBR
ITA
JPN
USA
-3
-2
-1
0
1
2
-2
-1
0
1
2
Δr* from pure discounting
Slope = 1.1
Int. = 0.2
Adj. R2 = 0.79 
Stock–Pure Discount Reconnect
Notes: This figure plots the country-level changes in equity yields against changes in trend interest rates (left
panel) and against estimated changes in the pure discounting component of interest rates (right panel), for
G7 economies. The sample is 1990–2023, or the longest available span for the given country. Measurement
details for all variables are provided in Section 3.
We next implement the decomposition empirically using a combination of survey data and
option prices to estimate the underlying structural drivers. The punchline of our empirical
implementation is that most of the secular changes in stock valuations over the past 35 years
can be explained by movements in the pure discounting part of interest rates. This result is
illustrated in the right panel of Figure 1, which shows that 80% of the changes in valuation
ratios of equities in G7 countries can be explained by changes in the pure discounting part of
interest rates. This pure discounting component is estimated purely from our decomposition
for interest rates, so there is nothing mechanical about the tight fit in explaining almost the
entirety of the country-by-country change in equity valuations over recent decades.
The pure discounting part of interest rates also explains a sizable share of fluctuations in
stock prices at higher frequencies, consistent with the long cash-flow duration of the stock
market, and it can be used to understand the pricing of the cross-section of equities. Our
framework allows us to revisit outstanding questions on why stock prices move, the size of the
ex ante equity premium, the impact of interest rates on wealth inequality, and the channels
through which monetary policy influences stock prices, all of which we elaborate on below.
The key input for our measurement is an international panel of long-term professional
forecasts for interest rates, inflation, and growth rates, which we obtain from Consensus
Economics. For each country, we back out forecast-implied series for the trend long-term real
rate r∗(a five-year-ahead forecast of the 10-year interest rate, net of expected inflation) and
2


---

trend growth rate (real output growth five years ahead), and we augment these with option-
based measures of uncertainty. After stripping out growth-rate and uncertainty changes, the
remaining interest-rate change is our estimate of the pure discounting shock.
In the U.S., we attribute around 35% of the decline in r∗since 1990 to pure discount-rate
changes, and the remaining 65% to the other components. So while equities have benefited
somewhat from the decline in U.S. interest rates, assuming full pass-through of r∗to equity
yields would overstate the effect by close to three times. And the pass-through of the decline
in rates to equities has been even lower in most other G7 countries. In the U.S., the pure
discounting term declined substantially in the 1990s; since 2000, it has stayed mostly flat,
implying that the decline in rates since 2000 is driven by forces other than pure discounting.
Our measurement of r∗from forecasts of long-term bond yields is motivated by a key
theoretical result: we show that for non-parallel shifts in the discount-rate curve, the most
relevant rate for equity is a long-horizon one. Given this long-horizon measurement, however,
one natural concern is that our estimated pure discounting term might spuriously pick up a
decline in expected bond term premia. Two features of our results make this interpretation
unlikely. First, a term premium change should not in general transmit to equity yields. The
near one-for-one pass-through we estimate is therefore difficult to square with a strong role for
term premia. Second, we obtain nearly identical results when we measure r∗from short-term,
rather than long-term, natural-rate estimates.
In addition to explaining secular changes, our decomposition also speaks to higher-
frequency movements in interest rates and equities. Without adjusting for the endogeneity of
rates, the raw relation between market returns and yield changes is small and imprecisely
estimated. But when we implement our decomposition, pure discount-rate shocks generate
strong negative comovement between ∆r∗
t and annual equity returns. The loading of stock
returns on pure discounting shocks provides a theoretically well-founded measure of equity
duration (i.e., the weighted-average time to maturity of cash flows), and we estimate a lower
bound for duration of about 20 years for the U.S. market. By contrast, equity returns have a
small and insignificant relation to the rate change attributable to growth shocks, and a positive
relation with the change attributable to uncertainty shocks. These offsetting components
illustrate why equity duration is not equivalent to the price sensitivity to arbitrary changes
in rates, and why one must isolate the pure discounting component to estimate duration.
We next use our decomposition to better understand the cross-section of stocks and their
exposure to interest rates. Following Gormsen and Lazarus (2023), we sort firms by their
predicted cash-flow duration and measure these duration-sorted portfolios’ returns. We show
that these portfolios do not differ in their exposure to raw interest-rate changes, but that the
long-duration firms have significantly greater exposure to the pure discounting shock. This
3


---

holds in spite of the unconditional negative alpha to long-duration relative to short-duration
stocks, and it implies a sizable spread (greater than 20 years) in the duration of long- versus
short-duration firms’ cash flows. These results provide a further out-of-sample validation of
both the duration sort and the construction of the pure discounting term.
Our results are robust across a range of alternative specifications and measurement choices.
This includes the use of alternative measures of r∗, g∗, and uncertainty in our interest-rate
decomposition. Moreover, we provide a set of theoretical and empirical robustness results on
the role of changes in the profit share of income, or the ratio of earnings to aggregate output.
Using separate forecast data on earnings and dividends, we find that our main U.S. empirical
results are effectively unchanged when allowing for a time-varying profit share.
Taken together, our results show that isolating the pure discounting term is essential
for understanding how shocks to interest rates are reflected in stock prices. While changes
to this term are equivalent to changes in the pure rate of time preference for the marginal
investor, we do not view this as the only (or main) source of likely variation. To better
interpret this term, we discuss how capital flows represent a candidate source of this pure
discounting variation, as they may affect interest rates in a manner not fully accounted for by
changes in fundamentals (growth or risk). We then show that the changes in the estimated
pure discounting terms align reasonably well with cross-country capital flows empirically. We
also briefly discuss other plausible contributors to changes in the pure discount rate.
Implications
Our findings on interest-rate pass-through speak to a range of issues raised in the literature:
(i) Our results clarify analyses of the relation between interest rates and equity valuations.
A prominent interpretation of classic valuation decompositions is that valuations move
mainly with risk premia rather than interest rates (e.g., Campbell and Cochrane 1999;
Lettau and Ludvigson 2001). In contrast to this “risk premium view,” we find that
changes in the pure discounting term explain most of the secular changes in equity
yields across G7 countries since 1990, as well as 77% of the time variation in U.S. equity
yields in this sample. Because interest rates comove with risk premia, isolating the
pure discounting term is key for understanding the role of rates in equity valuation
fluctuations. Doing so reveals a larger role for rates than previously recognized.
(ii) Estimating the ex ante equity premium based on realized returns can lead to biased
estimates if interest rates or risk premia change over the sample (Fama and French
2002). One approach to control for declining interest rates is to subtract from stock
returns the returns on duration-matched bond portfolios (van Binsbergen 2024; Polk and
Vuolteenaho 2026). While this is useful for measuring the realized returns associated
4


---

with dividend risk, we show that it leads to less precise equity-premium estimates
in general. This arises because of the imperfect pass-through from bonds to stocks:
only the pure discounting term passes through to equities in line with their duration,
and much of the decline in rates reflects growth and risk shocks. We instead suggest
subtracting the returns on a duration-matched “pure discounting” claim, which hedges
only against pure discounting changes. In simulations, this produces equity-premium
estimates that are 20% more precise than comparing stock returns to ex ante yields,
and 50% more precise than comparing to duration-matched bond returns. Empirically,
we estimate a large ex ante equity premium using our approach.
(iii) Recent work has argued that the decline in interest rates has influenced wealth inequality.
If r∗declines have passed through fully to equity, held disproportionately by wealthy
households, then much of the increase in inequality in recent decades may be driven
purely by interest-rate changes; see Fagereng et al. (2025) for a review of this literature.
Our findings help speak to this debate. We find that only a small share of the decline in
r∗was transmitted directly to equity, implying that declining interest rates had a much
smaller impact on wealth inequality than calculations based on full pass-through would
imply. This argument is consistent with Greenwald, Lettau, and Ludvigson (2025) and
Irie (2025), who find a larger role for other forces (particularly cash-flow changes) versus
discount-rate declines in explaining equity returns and changes in inequality.
(iv) Both academic research and practitioner commentary have discussed how the decline
in interest rates may have affected factor returns and cross-sectional anomalies (e.g.,
Asness 2022). One view holds that portfolios tilted toward short-duration cash flows
(such as value, or high book-to-market, portfolios) would have performed better in
recent decades in a counterfactual without the rate decline.1 We find that while value
stocks have limited exposure to raw interest-rate movements in general, they are highly
exposed to the pure discounting component of rates. We use this distinction to clarify
the role of declining rates in value’s recent poor performance: the pure discounting
component explains some, though far from all, of this underperformance.
(v) As a further application, we use our decomposition to unpack the effects of surprise
changes in short-term interest rates by monetary policymakers. Some papers implicitly
treat the resulting changes in long-term yields as pure discounting shocks, but this need
not hold: while the change in the short-term rate is indeed exogenous, the long-term
yield responds to changes in both the pure discount rate and perceived long-run growth
and uncertainty (e.g., Hanson and Stein 2015). Using our estimation results along with
high-frequency asset-price changes, we back out announcement-specific changes in both
1See Maloney and Moskowitz (2021), and citations therein, for related discussion.
5


---

the pure discounting term and expected growth. On average, we find that most of the
change in long-term yields around policy shocks indeed stems from the pure discounting
component. But we find as well that growth expectations change in a manner consistent
with an information effect on average (Nakamura and Steinsson 2018; Gilchrist, Yang,
and Zhao 2024), with substantial heterogeneity across announcements.
Overall, we provide a toolkit for understanding how changes in interest rates have, and have
not, affected a range of risky assets and aggregate outcomes over the short and long run.
Additional Related Literature
In addition to the connections described above, our paper relates to a long literature on the
time-varying relationship between stocks and bonds; Campbell, Pflueger, and Viceira (2025)
provide a recent review. Much of this work studies higher-frequency comovement between
stocks and nominal bonds and the role of inflation risk (e.g., Song 2017; Campbell, Pflueger,
and Viceira 2020). We focus on real yields. Chernov, Lochstoer, and Song (2025) study a real
channel driven by the mix of permanent and transitory consumption shocks, while Laarits
(2025) emphasizes changing precautionary savings motives. Our framework accommodates
both of these channels via the uncertainty (i.e., entropy) term in our real-rate decomposition,
though we do not focus directly on variation in the high-frequency comovement.
Our paper is closer to work studying longer-term stock–bond comovement. Campbell
and Ammer (1993) use VARs to relate this comovement to long-term expected returns. We
instead use surveys and asset prices to map bond and equity valuations to three structural
drivers of real rates, not to expected returns in reduced form. Barsky (1989) studies the
comovement in a two-period framework; we allow for pure discounting shocks and estimate
our more general decomposition empirically.2 Farhi and Gourio (2018) use a growth model
to account for secular valuation changes. Our exercise is less tightly parameterized, but our
evidence is consistent with their finding that real rates have comoved negatively with equity
premia. Bianchi, Lettau, and Ludvigson (2022) relate equity valuations to the monetary
policy stance; this focus is more specific than ours, but the two approaches similarly highlight
the need to isolate precise sources of rate variation to understand pass-through to stocks.
We also relate to work studying long-term drivers of stock prices and interest rates. For
equity, Greenwald, Lettau, and Ludvigson (2025) argue that increased profit shares are a key
driver of stock-price increases in the U.S. data. While their model-based estimation differs
from ours, our results are consistent: profit-share increases have affected both prices and cash
2In allowing for pure discounting shocks, we relate to macro–finance work on preference-related changes
in discount rates (e.g., Albuquerque et al. 2016). Lettau and Wachter (2011) also study a reduced-form
stochastic discount factor and exogenous (pure) real-rate shocks. Our general decomposition also builds on
the SDF characterizations of Hansen (2012), Backus, Chernov, and Zin (2014), and Martin (2017).
6


---

flows while having a limited effect on their ratio (Section 4.2). For rates, our paper connects
to the secular decline in the natural rate (Del Negro et al. 2019; Bauer and Rudebusch 2020).
We decompose this trend into structural components and measure how each transmits to
equity (and at which horizon). A related literature studies its sources, including demographics,
inequality, and global imbalances (Mian, Straub, and Sufi 2021; Auclert et al. 2025; Caballero,
Farhi, and Gourinchas 2008). We view these as potential channels driving the components
of the real rate, and we show in Section 5.1 that the capital flows emphasized by Caballero,
Farhi, and Gourinchas (2008) line up with our estimated pure discount-rate changes.3
Organization
We begin with our theoretical decompositions in Section 2. We then turn to our data,
measurement approach, and main findings in Section 3, and Section 4 provides robustness
results. In Section 5, we analyze additional implications of our findings. Section 6 discusses
and concludes. Derivations and additional results can be found in the Online Appendix.
2.
Theory: Rate Components and Equity Valuations
This section develops our theory linking interest rates and equity valuations. We decompose
the trend real rate into three interpretable and measurable fundamental components, such that
one component induces perfect comovement of bonds and stocks. Isolating this component will
then allow us to measure the degree to which rate changes transmit to equity valuations. Our
analysis also guides the measurement of each object in the data; we show, for instance, that
the trend long-term real rate is the relevant starting point for understanding pass-through.
We begin in Section 2.1 with a general real-rate decomposition, imposing minimal assump-
tions on fundamentals or the stochastic discount factor. We then specialize to an interpretable
consumption-based version. We consider what each term in the decomposition means for
equity prices (Section 2.2) and for equity duration (Section 2.3), and we then characterize
the relevant empirical objects for our estimation (Section 2.4).
2.1
Decomposing the Trend Real Rate
A General SDF-Based Version
We start with a general stochastic discount factor (SDF) Mt+1 such that Et[Mt+1Rt+1] = 1
for an arbitrary asset’s gross return Rt+1. This implies Rf
t+1 = 1/Et[Mt+1], where Rf
t+1 is the
3More broadly, our joint use of bonds and stocks relates to work using assets’ comovements to study
underlying shocks, especially bonds and exchange rates (e.g., Kekre and Lenel 2024). Our use of long-horizon
surveys to link fundamentals and returns also parallels Kremens, Martin, and Varela (2025).
7


---

real risk-free rate. Taking logs (and denoting logged variables in lowercase),
rf
t+1 = −Et[mt+1] −Lt(Mt+1),
(1)
where Lt(Mt+1) ≡log Et[Mt+1] −Et[mt+1] is the conditional entropy of the SDF. We note
that all expectations Et[·] are interpretable as either objective or subjective.
For now, we put very little structure on the SDF. We assume that the log SDF can be
additively decomposed as follows:
mt+1
=
−ρt
⏞⏟⏟⏞
predetermined
trend
−
(f(Xt+1) −f(Xt))
⏞
⏟⏟
⏞
difference for
Markov X
+
εt+1
⏞⏟⏟⏞
mean 0
martingale diff.
.
(2)
This additive representation is constructed following Hansen (2012, Theorems 3.1–3.2), and
it holds under a general set of primitive assumptions. See Appendix A.1 for formal details.
As discussed there, the term f(Xt+1) −f(Xt) is either stationary or difference-stationary.
In interpreting (2), the trend −ρt shifts the intertemporal marginal rate of substitution
mt+1 in all states, so ρt can be thought of as a time discount rate. We interpret the Markov
state Xt+1 as determining aggregate cash flows (again see Appendix A.1), so f(Xt+1) −f(Xt)
can be thought of as the realized marginal utility from cash flow growth. Finally, εt+1 is the
remaining martingale component of the log SDF. These terms’ interpretation will map to
their interpretation in the consumption-based framework in the next subsection.
Plugging (2) into (1), the log risk-free rate satisfies
rf
t+1
=
ρt
⏞⏟⏟⏞
trend (discounting)
+
Et[f(Xt+1) −f(Xt)]
⏞
⏟⏟
⏞
expected growth
−
Lt(Mt+1)
⏞
⏟⏟
⏞
uncertainty/prec. savings
.
(3)
The first two terms’ labels align with the interpretations discussed above. For the labeling of
Lt(Mt+1) as an uncertainty or precautionary savings term, note that by definition of entropy,
Lt(Mt+1) =
∞
∑︂
n=2
κn,t(mt+1)
n!
,
(4)
where κn,t(mt+1) is the nth conditional cumulant of the log SDF distribution. Conditional
entropy therefore encodes the higher (n ⩾2) moments of marginal utility, as is standard.
Our main interest will be in understanding changes in the trend real rate r∗
t . Analogous to
Bauer and Rudebusch (2020), we define this as the Beveridge–Nelson permanent component
of the one-period rate, r∗
t ≡lims→∞Et[rf
t+s+1]. But unlike Bauer and Rudebusch, we are
interested in longer-horizon real rates: we allow the period length to be long, with one period
8


---

potentially standing in for a horizon of many years. (We defer to Section 2.4 the question of
which horizon is most relevant for equity.) The zero-coupon yield at arbitrary horizon s is
Rf
t,t+s = Et[Mt,t+s]−1
s, where Mt,t+s = Mt+1 · · · Mt+s, so (3) carries through when relabeling
a single period to span horizon s.4 At longer horizons, term premia may affect yields through
the multi-period entropy term Lt(Mt,t+s); see Backus, Chernov, and Zin (2014). We use
one-period notation for convenience and return to term premia below.
For the trend real rate r∗
t , equation (3) directly implies that it satisfies
r∗
t = ρ∗
t + ˜︁g∗
t −L∗
t,M,
(5)
where ρ∗
t = ρt, ˜︁g∗
t = lims→∞Et[f(Xt+s+1) −f(Xt+s)] and L∗
t,M = lims→∞Et[Lt+s(Mt+s+1)].
This is the first version of our real-rate decomposition into three terms corresponding to
discounting, expected growth, and uncertainty. The analysis in this section shows that such
a decomposition can be derived quite generally — up to the issue of interpretation of each of
the three terms — starting from an additive decomposition of the log SDF.
A Consumption-Based Version
To put more structure on the decomposition in (5), we now consider a more standard
consumption-based framework. We assume an endowment economy in which a representative
agent has power utility over consumption,5
Ut = Et
∞
∑︂
s=0
βs
t
C1−γ
t+s
1 −γ .
(6)
The time discount factor βt and corresponding rate of time preference ρt = −log βt are
potentially time-varying. We assume that relative risk aversion γ, or the inverse elasticity of
intertemporal substitution (EIS), is constant.
Given (6), the log SDF is mt+1 = −ρt −γgt+1, where gt+1 ≡ct+1 −ct is log consumption
growth. Plugging this into (1),
rf
t+1 = ρt + γEt[gt+1] −Lt(Mt+1)
= ρt + γEt[gt+1] −
∞
∑︂
n=2
(−γ)nκn,t(gt+1)
n!
,
(7)
where the final expression for Lt(Mt+1) in terms of the growth-rate cumulants κn,t(gt+1) is as
4More formally, rf
t,t+s = ρt + s−1Et[f(Xt+s) −f(Xt)] −s−1Lt(Mt,t+s).
5See Appendices A.1–A.2 for extensions with Epstein–Zin preferences, time-varying risk aversion, or other
departures. Decompositions of the form (5) or (8) still hold in these alternative specifications.
9


---

in Backus, Chernov, and Martin (2011) or Martin (2013); see Appendix A.2. In a lognormal
setting, this simplifies to the familiar solution rf
t+1 = ρt + γEt[gt+1] −γ2
2 Vart(gt+1).
Given (7), the trend real rate can be expressed as
r∗
t = ρ∗
t + γg∗
t −L∗
t,M,
(8)
where ρ∗
t = lims→∞Et[ρt+s], g∗
t = lims→∞Et[gt+s+1], and L∗
t,M = lims→∞Et[Lt+s(Mt+s+1)].6
Thus exactly as in (5), the real rate can move due to changes in (i) time preference (a stand-in
for pure discounting shocks), (ii) expected growth rates (via an intertemporal substitution
channel), or (iii) risk or uncertainty (via a precautionary savings channel).
2.2
Pass-Through to Equity Valuations
We now move to equity and ask how each of the three terms in our r∗decomposition
transmits to equity valuations. This requires further structure on equity cash flows and other
fundamentals. Using a set of standard assumptions, we derive a version of a Gordon growth
formula for equity dividend yields. We then apply this to show how each component of our
real-rate decomposition maps to equity valuations in a simple, intuitive way.
We pick up from the same consumption-based framework as in Section 2.1, though the
main equity-valuation decompositions below in fact apply as well under Epstein–Zin utility
(see Appendix A.3). For equity cash flows, we follow Campbell (1986) and Abel (1999) and
model equity as a levered claim to consumption, paying dividends Dt = Cλ
t , with λ > 0. This
imposes a tight link between dividend growth and output and consumption growth. While
this works well to explain the long-term trends observed in our data, this need not always be
the case (particularly at high frequencies). We accordingly extend our analysis in Section 4.2
to allow for time variation in the profit share of output, which we then discipline in the data
with additional survey expectations. For now, however, we assume that λ is constant.
Denote the gross equity return by Rmkt
t+1 and the log return by rmkt
t+1, and define µt ≡Et[rmkt
t+1]
and rpt ≡µt −rf
t+1. The equity yield is defined as
eyt ≡log(1 + Dt/Pt),
(9)
where Pt is the price of the equity claim. This is slightly different from the usual log dividend–
price ratio (dpt ≡log(Dt/Pt)). We define eyt as in (9) because it puts the equity yield
in equivalent units as the log real rate. It also yields straightforward characterizations of
steady-state ey∗
t building on results from Martin (2013) and Gao and Martin (2021).
6As discussed in Appendix A.1.3, in a stationary setting in which the limiting expectations here are
constant, we redefine these terms as infinite-horizon discounted sums of expected outcomes.
10


---

To show that our results apply across a range of standard environments, we consider
two cases for the dynamics of fundamentals.
Each will inform different aspects of the
empirical analysis. Case I features permanent shocks to fundamentals. This case gives an
exact decomposition for equity yields and is useful for considering secular changes over our
full sample, as well as higher-frequency permanent shocks. In Case II, fundamentals are
instead stationary. We obtain the same decomposition for equity yields in an approximate
(Campbell–Shiller) form, but this setting further allows us to characterize precisely which
interest rate is most relevant for measuring the effect of persistent, mean-reverting shocks.
Case I (Gordon Growth): Assume that log output growth gt+1 = ct+1 −ct is conditionally
i.i.d. with arbitrary distribution, so that as of time t, agents expect growth to be i.i.d. with
the current parameters forever. We allow for unanticipated shocks to these parameters, which
then become the new steady state. Given this structure, we write g∗
t = Et[gt+1] = Et[gt+s] for
all s ⩾1, and the growth-rate cumulants satisfy κn,t(gt+1) = κn,t+s(gt+s+1) for all s ⩾1. We
similarly allow for unanticipated shocks to the preference parameter ρ∗
t = ρt. This setting
provides a clean starting point for understanding secular changes, and we show below that it
can be generalized to non-i.i.d. cases without loss of generality.
This i.i.d. environment closely builds on that of Martin (2013), and we apply and extend
his results; see Appendix A.3 for details and derivations. Given the constant growth rates and
discount rates, a Gordon growth formula applies as follows (where we use the i.i.d. assumption
to set all relevant variables equal to their conditional steady-state values):
ey∗
t = r∗
t + rp∗
t −λg∗
t .
(10)
The log equity premium satisfies
rp∗
t =
∞
∑︂
n=2
κn,t(gt+1)
n!
((−γ)n −(λ −γ)n)
= Lt(Mt+1) −Lt(Mt+1Rmkt
t+1) = L∗
t,M −L∗
t,MR.
(11)
As discussed in the appendix, the fact that rpt = Lt(Mt+1)−Lt(Mt+1Rmkt
t+1) is fully general: it
holds under no arbitrage and does not require i.i.d. fundamentals or any assumptions on utility.
If λ = γ, then Mt+1Rmkt
t+1 = 1, and rp∗
t = L∗
t,M.7 Alternatively, for arbitrary λ and γ, if growth
is lognormal so that κn,t(gt+1) = 0 for n > 2, then rp∗
t = 1
2λ(2γ −λ)Vart(gt+1) = λ(2γ−λ)
γ2
L∗
t,M.
Using (8), (10), and (11), we obtain a solution for equity yields summarized along with
7This is a restatement of the fact that the Alvarez and Jermann (2005) SDF entropy lower bound holds
with equality in the growth-optimal case (i.e., with Mt+1Rmkt
t+1 = 1): Lt(Mt+1) = Et[rmkt
t+1 ] −rf
t+1.
11


---

the real risk-free rate in the following result.
Result 1. The steady-state real risk-free rate and equity dividend yield satisfy
r∗
t = ρ∗
t + γg∗
t −L∗
t,M,
ey∗
t = ρ∗
t + (γ −λ)g∗
t + (rp∗
t −L∗
t,M)
= ρ∗
t + (γ −λ)g∗
t −L∗
t,MR.
Changes in the risk-free rate can arise due to (i) pure discounting shocks (changes in ρ∗
t),
(ii) growth-rate shocks (g∗
t ), or (iii) risk (entropy) shocks (L∗
t,M). Each of the three has
different implications for equity valuations:
(i) Pure discounting shocks: Bonds and equity comove perfectly, with ey∗
t increasing by
1 basis point for each 1 basis point increase in r∗
t .
(ii) Growth-rate shocks: Equity yields change by γ−λ
γ
per unit increase in r∗
t . If γ = λ
(e.g., with log utility and an unlevered consumption claim), ey∗
t is unaffected by changes
in r∗
t induced by growth shocks. If λ > γ, growth shocks induce negative comovement.
(iii) Risk shocks: Equity yields change by −∂rp∗
t
∂L∗
t,M + 1 per unit increase in r∗
t if
∂rp∗
t
∂L∗
t,M is
well-defined. Otherwise, equity yields change on average by −βL + 1 per unit increase in
r∗
t , where βL ≡
Cov(rp∗
t ,L∗
t,M)
Var(L∗
t,M) . If γ = λ, then ey∗
t is unaffected by changes in r∗
t induced
by risk shocks. If βL > 1, risk shocks induce negative comovement.
The key implication of this result is that only the pure discounting channel generates
perfect pass-through from interest rates to equity yields, and from bond prices to duration-
matched stock prices (as discussed below). The range of past work assuming that the decline
in rates has passed through fully to equity valuations — as discussed in Section 1 — has
therefore implicitly assumed that the decline in r∗
t has arisen due to such pure discounting
shocks. Changes in ρ∗
t can be thought of as capturing, for example, demographic changes, or
something akin to a savings glut. We discuss such interpretations further in later sections.
For growth-rate changes, note that the equity yield depends on r∗
t −λg∗
t (our version
of r −g), so a decline in g∗
t will have roughly offsetting effects: it decreases both discount rates
and growth rates.8 While we do not impose this, it is common to assume that γ ⩽λ — or,
in the Epstein–Zin case, that 1
ψ ⩽λ, where ψ is the EIS — so that a decline in growth rates
8The ey∗
t decomposition in Result 1 does not separate between discount rates and growth rates in the
same manner as a Campbell–Shiller decomposition. Instead, it collects terms such that the g∗
t term, for
example, contains both the direct cash-flow effect (λg∗
t ) and the discount-rate effect (γg∗
t ). This reflects our
desire to decompose risk-free discount rates into structural components rather than composite terms.
12


---

also decreases equity valuations (corresponding to a higher ey∗
t ). This would imply that
growth-rate changes generate weakly negative comovement between bonds and stocks.
For changes in risk, there are offsetting effects on the risk-free rate and the risk premium.
These changes may approximately offset or may cause stocks to move in the opposite direction
of bonds. As L∗
t,M loads on all the higher cumulants of the growth distribution as in (7),
the stock-price response will depend on the specific parameter change underlying the risk
shock. In Appendix A.3, we characterize the bond–stock comovement in three benchmark
cases: (i) in a lognormal setting with power utility and γ̸ = λ, r∗
t and ey∗
t comove positively
given changes in risk, though the pass-through is less than one-for-one if 2γ > λ; (ii) in a
rare-disasters model as in Barro (2006), if γ < λ, then r∗
t and ey∗
t comove negatively given
changes in the average disaster size (or, more generally, given changes in skewness or other
odd moments); (iii) with Epstein–Zin utility, if γ > 1, ψ > 1, and λ = 1, then r∗
t and
ey∗
t comove negatively given changes in even moments of the growth distribution (variance,
kurtosis, and so on), as in Martin (2013). So while positive risk shocks robustly decrease the
risk-free rate and generally induce a muted or negative stock–bond comovement, we treat
their precise pass-through to stocks as an open question to be disciplined empirically.
Result 1 is our main decomposition for trend real rates and equity valuations. We now
show that it also applies under arbitrary permanent shocks, without imposing conditionally
i.i.d. fundamentals. To do so, assume that the distributions of growth rates and preference
parameters are such that eyt follows a martingale, eyt = Et[eyt+1]. Campbell (2018) refers to
this as a “drifting steady state” model for ey∗
t = eyt, and Campbell and Thompson (2008)
show that such a model has success at forecasting medium-to-long-horizon returns. To a first
order for eyt+1 around its expectation eyt, we have in this case that eyt = Et[rmkt
t+1 −λgt+1]
(Gao and Martin 2021; again see the appendix). This implies that
ey∗
t = eyt = Et[rmkt
t+1 −λgt+1] = Et[rmkt
t+2 −λgt+2] = . . . = r∗
t + rp∗
t −λg∗
t ,
(12)
assuming the individual limiting values exist as t + s →∞. In addition, r∗
t satisfies the same
decomposition as in (8). Result 1 therefore holds exactly, and the same takeaways apply.
These steady-state facts can be equivalently stated as applying to one-period-ahead
conditional expectations:
eyt = ρt + (γ −λ)Et[gt+1] + (rpt −Lt(Mt+1)),
and similarly for the risk-free rate as in equation (7). These versions are useful for interpreting
higher-frequency permanent shocks to rates and prices.
13


---

Case II (Stationarity): We now instead assume that eyt and all fundamentals are stationary,
with no unanticipated permanent shocks. To non-trivially characterize the pass-through from
interest-rate changes to equity valuations in this case, we must reinterpret all the previous
starred terms to capture persistent rather than permanent variation. Concretely, we redefine
the starred terms zt ∈{rf
t+1, rpt, ρt, gt+1, Lt(·)} as Campbell–Shiller-type discounted sums:
z∗
t ≡(1 −δ)
∞
∑︂
s=0
δsEt[zt+s],
(13)
where δ ∈(0, 1) is a loglinearization term defined in Appendix A.3. Since (1 −δ) ∑︁∞
s=0 δs = 1,
(13) defines the starred long-run terms as weighted averages of all future expected outcomes.
Given (13), we again follow Gao and Martin (2021) to obtain the loglinear approximation
ey∗
t ≡eyt = r∗
t + rp∗
t −λg∗
t ,
exactly as in (10), where r∗
t = ρ∗
t + γg∗
t −L∗
t,M and rp∗
t = L∗
t,M −L∗
t,MR. So given the
redefinitions in (13), Result 1 again applies exactly as stated.
The pure discounting term ρ∗
t in this case is a weighted average of the expected path
of one-period pure discount rates. The permanent shocks in Case I shift this entire “pure
discounting curve” in parallel, whereas mean-reverting shocks shift it non-uniformly across
horizons (with an effect summarized by dρ∗
t). We consider the full curve in more detail below.
To summarize, in both cases for fundamentals, our decomposition delivers effectively equivalent
results, as characterized in Result 1. Only shocks to the pure discounting component of real
rates pass through perfectly to equity valuations (in the form of equity yields). Shocks to
the other two components in our decomposition — growth rates and uncertainty — generate
ambiguous and possibly negative comovement between rates and equity valuations.
2.3
Implications for Equity Duration
Having analyzed the relation between interest rates and equity yields, we now consider
what the decomposition implies for equity duration. We show that equity duration does not
correspond to the price sensitivity of equity to an arbitrary change in rates, and the only rate
change that leads to an equity price change equal to its duration is a pure discounting shock.
To make this point, we first express equity prices in levels. We consider a constant-growth
steady state and drop time subscripts to simplify:
(︃P
D
)︃∗
=
1
exp(r∗+ rp∗−λg∗) −1 =
1
exp(µ∗−λg∗) −1 ≈
1
µ∗−λg∗.
(14)
14


---

Equity cash-flow duration D is the value-weighted time to maturity of expected future cash
flows:
D ≡
∞
∑︂
s=1
se−s(µ∗)Et[Dt+s]
P
=
1
1 −e−(µ∗−λg∗) ≈
1
µ∗−λg∗.
(15)
This measure is equivalent to the equity price sensitivity to the log equity discount rate,
−∂log P
∂µ∗
=
1
1 −e−(µ∗−λg∗) = D,
(16)
which parallels the usual result for the exposure of bond prices to a shift in the yield curve.
More important here, though, is price sensitivity to interest-rate changes arising from each
of the terms in our decomposition. Given (14), we have the following result describing how
price sensitivity depends on the underlying structural driver of interest-rate changes.
Result 2 (Three Interest-Rate Sensitivities). The sensitivity of stock prices with respect to
each of the three terms in the interest-rate decomposition r∗= ρ∗+ γg∗−L∗
M is as follows.
(i) The interest-rate sensitivity of stock prices with respect to pure discount-rate shocks is
Sr(ρ) ≡−∂log P
∂ρ∗
=
1
1 −e−(µ∗−λg∗) = D.
(ii) The interest-rate sensitivity of stock prices with respect to growth shocks is
Sr(g) ≡−∂log P
∂(γg∗) =
(︃
1 −λ
γ
)︃
D < D.
(iii) Assuming that ∂rp,L ≡∂rp∗
∂L∗
M is well-defined and positive, the interest-rate sensitivity of
stock prices with respect to risk shocks is
Sr(L) ≡−∂log P
∂(−L∗
M) = (1 −∂rp,L) D < D.
Part (i) tells us that price sensitivity to the pure discount rate pins down equity duration
in a manner equivalent to price sensitivity to the equity discount rate in (16). The other
interest-rate terms do not share this feature: price sensitivity to growth shocks is strictly less
than duration, as is price sensitivity to risk shocks under general assumptions. To take a
benchmark example, with log utility (γ = 1) and equity modeled as an unlevered consumption
claim (λ = 1), the price sensitivity of equity to a change in rates due to g∗or L∗
M are both
exactly zero. More generally, as long as equities move positively with expected growth and
15


---

negatively with respect to risk, the rate sensitivities in parts (ii)–(iii) will both be negative.
So only a change in rates induced by a shock to ρ∗moves equities in line with their duration,
and equity duration is not equivalent to price sensitivity to an arbitrary change in r∗.
The fact that equity duration is equal to price sensitivity to pure discount-rate changes
also provides a novel avenue for measuring duration. Measuring duration using realized
growth rates, as in (15), requires a long sample. Measurement using price sensitivity to µ∗,
as in (16), is challenging given the difficulty in measuring expected equity returns. So if our
interest-rate decomposition provides reliable estimates of the pure discount rate term ρ∗over
time, then estimating the exposure of equity returns to changes in this parameter allows for
clean estimation of duration, both for the aggregate market and for narrower portfolios.
2.4
Which Interest Rate? Non-Parallel Discounting Shifts
An open question in the literature is what interest-rate horizon should be used as a benchmark
for equity (see Section 5.2 for an example). In our setting, this question arises in terms of
implementation: estimating our decomposition empirically requires taking a stand on the
horizon at which to measure interest rates and their components. So far, we have treated
each term in the rate decomposition as a single number (ρ∗, g∗, and L∗
M). This works well
for considering permanent shocks (as in Case I of Section 2.2): these induce parallel shifts in
the real yield curve, so all horizons are equally valid for understanding equity pass-through.
But with non-parallel shifts (e.g., in the mean-reverting Case II), equity responds differently
to shocks at different horizons. We thus face the question of which horizon’s change is most
relevant. Since shocks to the pure discounting term ρ∗generate perfect pass-through in
Result 1, we focus on the pure discounting curve and define the relevant horizon on that
curve as the one that similarly generates perfect pass-through.
Let ρ∗(s) ≡Et[ρt+s−1] denote the expected one-period pure discount rate applying over
period s (so ρ∗(1) = ρt), and let {ρ∗(s)} denote the pure discounting curve.9 Again start from
a flat steady state in which ρ∗(s) = ρ∗for all s (and similarly for all other expected future
variables), and we consider a possibly non-parallel shock {dρ∗(s)}. Let Ps ≡Et[Mt,t+sDt+s]
denote the price of the s-period dividend strip paying the single t+s dividend. As usual, equity
is a claim to all of these strips, with price P = ∑︁
s Ps and strip value weights ws = Ps/P. In
the flat steady state, strip value weights are geometric in the horizon s, ws = (eey∗−1) e−s(ey∗),
and the mean strip-weighted horizon is equal to equity duration, ∑︁
s s ws = D.
The following result characterizes the equity response to the shift {dρ∗(s)}.10 We first
9As in Section 2.1, we continue to allow a period to be of arbitrary length. For concreteness of interpretation,
however, it is useful here to think of periods as being annual, as we do below.
10Formally, we characterize the directional (Gâteaux) derivative in the direction of the shift.
16


---

consider an arbitrary shift, and then an affine case that can be viewed as a first-order
approximation to an arbitrary shift. The affine case identifies a single relevant horizon.
Result 3 (Non-Parallel Discounting Shifts and the Relevant Horizon). Start from the flat
steady state, and consider an unanticipated shift {dρ∗(s)}.
(i) General shift: To first order, the equity yield moves by the strip-weighted average of
the pure-discounting changes, and the log stock price sensitivity is D times that average:
d ey∗=
∞
∑︂
s=1
ws dρ∗(s),
d log P = −D d ey∗.
(17)
(ii) Affine shift and the relevant horizon: For an affine shift dρ∗(s) = a + bs, the
strip-weighted average change satisfies ∑︁∞
s=1 ws dρ∗(s) = dρ∗(D). As a result, the equity
yield moves one-for-one with the pure discounting change at horizon D, and the log
stock price sensitivity to ρ∗(D) is equal to D:
d ey∗= dρ∗(D),
d log P = −D dρ∗(D).
(18)
The relevant horizon is thus equal to equity duration.
(iii) Parallel shift: If dρ∗(s) = dρ∗for all s, then d ey∗= dρ∗and d log P = −D dρ∗,
recovering Result 1(i) and Result 2(i); every horizon is then equally relevant.
Part (i) of the result emphasizes that equity in general responds to a weighted average
of forward pure discount rates. Part (ii) then tells us that the single horizon that best
approximates the overall average change is equal to equity duration.11 As a result, to a first
order, ey∗moves one-for-one with ρ∗(D), the pure discount rate at horizon D. By contrast, a
shift in the short-term (one-period) pure discount rate ρ∗(1) moves the equity yield by only
w1 = 1/D. To understand equity valuation changes in response to rate shocks induced by ρ∗,
then, we must consider longer horizons approximately equal to equity duration.
In the data, we will generally consider measures of expected pure discount rates averaged
over future periods m to n: ¯ρ∗(m, n) ≡
1
n−m+1
∑︁n
s=m ρ∗(s). Part (ii) implies that the equity
yield moves one-for-one with ¯ρ∗(m, n) if and only if its midpoint is equal to duration, m+n
2
= D.
We therefore aim to estimate pure discount rates starting from long-horizon measures of r∗
with mean horizon of approximately D.
Finally, part (iii) formally restates the fact that the horizon of measurement should not
matter for permanent shifts in ρ∗. We will test whether this holds for the full-sample secular
11To see that the affine shift first-order approximates a general shift, expand the value-weighted average
around D: ∑︁
s ws dρ∗(s) = dρ∗(D)+ 1
2 dρ∗′′(D) D(D−1)+· · · . An affine shift produces ∑︁
s ws dρ∗(s) = dρ∗(D).
17


---

changes we estimate in our data. For higher-frequency changes, we expect non-parallel shifts
in the discounting curve to be relevant.
The takeaway is that long-horizon rate measures are most relevant as a benchmark for
equity. This conclusion holds even though long-term yields are affected by term premia. As
in Section 2.1, term premia affect yields through the entropy term: the average s-period term
premium is L∗
t(Mt,t+1) −s−1L∗
t(Mt,t+s). Since the term premium is part of the uncertainty
term rather than the pure discount rate, a term-premium change should not transmit directly
to equity valuations. A strong estimated pass-through of ρ∗to equity is thus inconsistent
with confounding from term premia or similar issues. We turn now to this estimation.
3.
Empirical Implementation
We now implement our real-rate decomposition empirically and study how interest rates
and their three components transmit to equities across countries. We lay out our data and
measurement approach in Section 3.1. We then estimate the terms in our decomposition, first
in levels to study secular trends (Section 3.2), and then in changes to study transmission to
equity returns (Section 3.3) and portfolio returns in the cross-section of stocks (Section 3.4).
3.1
Data and Baseline Measurement Approach
Recall that our goal is to measure each of the terms in the trend real-rate decomposition
from Result 1 (or equation (5)): r∗
t = ρ∗
t + γg∗
t −L∗
t,M, where ρ∗
t is the pure discounting term,
g∗
t is long-term expected output growth, and L∗
t,M is uncertainty (entropy). Our approach
will be to measure r∗
t and g∗
t as directly as possible; measure L∗
t,M using a proxy from option
prices; and then back out the pure discounting term as a residual.
For trend long-horizon real rates and expected growth rates, our main input is a panel of
long-term forecast data obtained from Consensus Economics. They collect survey expectations
of country-level economic and financial outcomes from professional forecasters, with 10–30
forecasters per survey for each country. We use the Long-Term Economic Forecasts data,
which are available for the G7 countries (Canada, France, Germany, Italy, Japan, the U.K.,
and the U.S.) from 1990 through 2023, and for a subset of other developed economies
(Netherlands, Norway, Spain, Sweden, and Switzerland) starting in 1995 or 1998. These
long-term forecasts are available twice annually for 1990–2013, and quarterly since 2014.
Three key features of the Consensus data are useful here. First, data are available for a
panel of countries. Second, the forecasts are provided as forward expectations: we observe
separate forecasts for year t+1, year t+2, . . ., as opposed to forecasts stated as averages over
the next X (e.g., 5 or 10) years. The long-horizon forward forecasts remove cyclical variation
18


---

affecting the short-horizon or averaged forecasts; we find this is important for measuring trend
variables, as we observe lower volatility and mean reversion than in other forecast data (e.g.,
SPF or IBES). Third, the forecasters are typically professional economists at large investment
banks and firms, whose expectations are likely relevant for asset-price determination.
For all series, we use consensus (mean) forecasts at the five-year forward horizon.12 To
estimate the long-term real rate r∗
t,j for date t and country j, we take the consensus forecast
of the 10-year nominal interest rate at the end of year t + 5 and subtract the inflation
forecast for year t + 5. We use the forecast of the 10-year yield following Result 3, which
shows that the relevant rate for equity is a long-horizon one on the order of equity duration.
For the expected growth rate g∗
t,j, we use the forecast of real output growth for year t + 5.
One potential concern is a possible mechanical relation between this and r∗
t,j arising from
forecasters using a model tying these variables together. While this is possible, the fact that
these forecasters work at institutions with a key role in trading and pricing assets means
that their expectations are relevant irrespective of how they are formed. Further, our main
exercises — testing if the estimated real-rate components transmit to equity in the manner
predicted by theory — will provide an out-of-sample validation of the rate decomposition.
We also consider many alternative measures of r∗
t,j and g∗
t,j in robustness checks in Section 4.
To proxy for the uncertainty term L∗
t,M,j, we build on results from Section 2.2 and Martin
(2017). We show in Appendix A.3 that if the market is growth-optimal and the distribution
of log growth is symmetric, then the entropy of the SDF is equal to that of the market,
L∗
t,M,j = L∗
t,R,j. And as shown in Martin (2017, Result 3), VIX2
t,j is proportional to the
market’s risk-neutral entropy. We therefore set L∗
t,M,j ∝VIX2
t,j for our baseline, with the
constant of proportionality estimated in our regressions below. We will also use VIX2
t,j for
the risk term in the equity yield decomposition, as would hold in the growth-optimal case or
with lognormality. Our VIX-based proxy for risk may induce some mismeasurement at higher
frequencies, but less so when examining full-sample secular changes. To measure VIX2
t,j, we
use a global panel of index option prices from OptionMetrics. The sample, data filters, and
calculations are taken from Gandhi, Gormsen, and Lazarus (2025); see Appendix B.1 for
details. We calculate the squared VIX at the six-month horizon, which is longer than the
CBOE’s 30-day VIX given our desire to measure long-term uncertainty.13
As mentioned above, we also consider a range of alternative variables to test the robustness
of our decomposition results. This includes using trend short-term (rather than 10-year)
12This is the longest horizon for which we directly observe a specific forward forecast. The surveys also
elicit average expectations over years 6–10, which give nearly identical results (Section 4.1).
13Illiquidity in long-term options makes it infeasible to calculate something closer to a five-year VIX.
Gandhi, Gormsen, and Lazarus (2025) show that implied volatility decays slowly at long maturities, so we
view our measure as a reasonable proxy for long-term uncertainty (and again see Section 4.1).
19


---

interest rates for r∗
t,j; alternatives to Consensus survey data; and alternatives to VIX2
t,j for
uncertainty. We describe these alternatives in Section 4, and results are robust in all cases.
For equities, we use data from the CRSP/XpressFeed global database to obtain market
indices for each country. To measure equity yields eyt,j, we start with the five-year earnings-to-
price ratio Et−4,t,j/Pt,j = [(Et−4,j +. . .+Et,j)/5]/Pt,j, where earnings and prices are calculated
on a value-weighted basis for all available stocks in the country (see Appendix B.1). All
equity values are thus measured as aggregates rather than on a per-share basis. We map the
earnings yield to the equity yield considered in our theory by multiplying this by 0.5, which
is the full-sample average payout ratio: half of earnings (more precisely, 49.4%) are paid out
to shareholders in an average year–country observation, with the remainder reinvested.14
For our cross-sectional analyses, we use returns on duration-sorted portfolios following
Gormsen and Lazarus (2023). That paper measures duration based on analyst forecasts
of long-term expected earnings growth, or LTG (with higher cash-flow growth indicating a
longer duration). We also obtain data on value-sorted portfolios via Ken French’s website.
3.2
Secular Trends
To study long-term trends, we start by estimating our decomposition for trend real rates in
levels. For all available dates t and countries j, we estimate a regression
r∗
t,j = ρ0 + γ g∗
t,j + β VIX2
t,j + Γj + εt,j,
(19)
with country fixed effects Γj. In our main specification, we also allow the VIX2 loading β to
differ by country (βj). While this is not important for our main results, it helps account for
cases in which sovereign credit risk affects a country’s r∗
t .15 It also allows for the possibility
of country-specific measurement error in the VIX, which may be an issue particularly for
countries with less-liquid option markets.
Given a set of estimated coefficients and OLS residuals, we then back out the implied
pure discounting term as
ˆ︁ρ∗
t,j = ˆ︁ρ0 + ˆ︁Γj + ˆ︁εt,j.
(20)
We thus have, by construction, that r∗
t,j = ˆ︁ρ∗
t,j + ˆ︁γg∗
t,j + ˆ︁βVIX2
t,j, which corresponds exactly
to our theoretical decomposition (with the uncertainty term −L∗
t,j proxied by ˆ︁βVIX2
t,j).
Estimates for the regression (19) are shown in Table 1, first for the U.S. only and then for
the full 12-country panel. The estimates correspond well to our theory. The estimated loading
14An alternative is to use dividend yields dpt,j directly in place of eyt,j. Since ∆dpt,j and ∆eyt,j are highly
correlated, this gives near-identical results: the cross-country regression of ∆dpt,j on the pure discounting
change has a slope of 1.01 and an adjusted R2 of 0.75, as compared to 1.14 and 0.79 in the right panel of
Figure 1. Our baseline starts from an earnings yield to address the fact that payout ratios have declined in
20


---

Table 1: Regressions for Trend Real Rates r∗
t,j
(1)
(2)
(3)
U.S.
All
All
Expected growth g∗
t,j
1.8***
2.1***
2.1***
(0.2)
(0.2)
(0.2)
Uncertainty VIX2
t,j
-10.1**
-3.8
βj
(4.5)
(3.0)
Constant
-1.9***
-1.9***
-2.0***
(0.5)
(0.4)
(0.4)
Country FEs
✗
✓
✓
Country-Specific VIX2
t,j Loading
✓
✗
✓
Obs.
86
932
932
R2
0.57
0.65
0.66
Within R2
—
0.60
0.61
Notes: This table shows OLS coefficient estimates in the regression (19), with standard errors in parentheses.
In column (1), standard errors are obtained using a block bootstrap with one-year blocks and 10,000 bootstrap
draws. In columns (2)–(3), standard errors are clustered by country and date. Statistical significance at
the 10% level, 5% level, and 1% level are denoted by *, **, and ***, respectively. In column (3), the
country-specific loadings on the squared VIX, βj, are statistically significant at the 1% level for 9 of the 12
countries in our sample. The sample is 1990–2023, or the longest available span for the given country.
on expected growth is strongly positive and consistently close to a value of 2, corresponding
to implied relative risk aversion of γ ≈2 and EIS of about 1/2. The loading on the VIX is
negative and significant in the U.S. case and for most countries in the country-specific case
shown in column (3). This limited set of variables explains a large share of the variation in
trend real rates, with R2 values of around 0.6 within-country and slightly higher overall. The
remaining variation is then attributed to the pure discounting residual.
To visualize the data, Figure 2 presents the estimation results for the decomposition
of r∗
t,j over time in the U.S. data. The trend real rate has fallen by close to 2.5 percentage
points (pp), or 250 basis points (bps), from the beginning to the end of the sample, starting
near 4% and ending near 1.5%. As can be seen in the green line, a large share of this decline
is attributed to a decline in long-term expected growth. Expected growth fell by around
0.75 pp over the sample, which when multiplied by γ ≈2 translates to a predicted decline
in yields of about 150 bps. While uncertainty affects real rates significantly during deep
recessions, it has only a small negative long-term effect over the full sample. Together, the
change in growth rates and uncertainty predicted a decline in real rates of around 160 bps
recent decades. In subsequent higher-frequency time-series plots, we generally use the dividend yield directly.
15Our theory suggests that the loading on uncertainty should be negative, but credit risk can induce an
offsetting positive relation between risk and long-term rates. We find that this effect is small on average.
21


---

Figure 2: U.S. Estimation Results for Decomposition of r∗in Levels
-1
0
1
2
3
4
Percent
1990
1995
2000
2005
2010
2015
2020
2025
r*
Exp. Growth Component
VIX Component
Pure Discounting Residual
Notes: This figure shows the U.S. trend real rate r∗
t,j and its components over time, estimated using (19)–(20)
following the main specification in column (3) of Table 1. For readability, the expected growth component is
shifted down by 3 percentage points (ˆ︁γg∗
t,j −3), and the pure discounting residual is plotted as ˆ︁εt,j.
overall, so the additional 90 bps of unexplained decline is attributed to the pure discounting
residual. This residual was particularly important in explaining the decline in interest rates
early in the sample. From 2000 onward, the decline in interest rates has been driven almost
exclusively by declines in expected growth rates, implying little impact on equity valuations.
As we show in Section 4, this finding is robust to numerous alternative ways of implementing
our r∗
t,j decomposition, including the use of shorter-horizon interest rates.
The remainder of this subsection studies how secular changes in equity valuations across
countries relate to changes in the different components of interest rates. Our goal is to
understand country-level changes in equity valuations over our sample period.
In the leftmost panel in Figure 3, we plot the change in equity yields against changes
in the pure discounting term in G7 countries. This is the same figure plotted in the right
panel of Figure 1 in the introduction. The figure illustrates that the large majority of the
changes in equity yields over this sample can be explained by changes in the pure discounting
term in interest rates; we show that this relationship is statistically significant in Section 4.1.
Since the pure discounting term is estimated purely from the interest-rate decomposition
in (19)–(20), without the use of equity valuations, there is nothing mechanical about the
explanatory power of pure discounting changes for stock valuations over this sample. This
finding therefore serves as a strong out-of-sample validation of the rate decomposition.
The magnitude of the relation between equity yields and the pure discounting term is,
22


---

Figure 3: Main Results: Long-Term Decomposition
CAN
DEU
FRA
GBR
ITA
JPN
USA
-3
-2
-1
0
1
2
Δequity yield
-2
-1
0
1
2
Δr* from pure discounting
Slope = 1.1
Int. = 0.2
Adj. R2 = 0.79 
CAN
DEU
FRA
GBR
ITA
JPN
USA
-3
-2
-1
0
1
2
-4 -3.5 -3 -2.5 -2 -1.5
Δr* from growth & VIX
Adj. R2 = 0.55 
CAN
DEU
FRA
GBR
ITA
JPN
USA
-3
-2
-1
0
1
2
-4 -3.5 -3 -2.5 -2 -1.5
Total Δr*
Adj. R2 = -0.02 
Notes: This figure plots the country-level changes in equity yields against changes in different components
of interest rates, estimated using (19)–(20) following the main specification in column (3) of Table 1. The
leftmost figure plots changes in equity yields against changes in the pure discounting term; the middle figure
plots changes in equity yields against changes in the growth and VIX components; the rightmost figure plots
changes in equity yields against changes in real rates themselves. The sample is 1990–2023, or the longest
available span for the given country. For countries for which we can only measure equity yields starting after
1990 (see Appendix B.1), we calculate both ∆equity yield and ∆r∗over the same window.
in addition, almost exactly equal to that predicted by theory. The figure shows that equity
yields decrease by one percentage point for every one-percentage-point decrease in the pure
discounting term, as in Result 1. And the pure discounting term explains not only relative
changes in equity valuations across countries, but also changes in valuations in absolute
terms: the intercept for the fit is very close to zero, which means the average equity yield has
moved by as much as the pure discounting term. This does not necessarily imply that other
factors influencing valuation ratios — such as growth rates and risk premia — have remained
constant, but it does imply that potential movements in growth rates and risk premia have,
on net, not played a significant role in changing equity valuations on average over this period.
The upshot is that to understand long-run valuation changes in this sample, understanding
the change in pure discount rates is nearly sufficient.
The middle panel of Figure 3 illustrates the relation between equity yields and the change
in interest rates induced by changes in expected growth rates and uncertainty, taken together.
As expected, we find that valuation ratios have dropped in countries where interest rates
have dropped because of declines in growth rates and increases in risk: while these changes
have decreased interest rates, they have also depressed growth rates on equities and increased
equity premia, with the predicted effect on equity valuations being negative. This relationship
is noisier than the one in the left panel, consistent with the more ambiguous theoretical
23


---

predictions for valuations given changes in growth rates and uncertainty, but the negative
relationship is at least moderately strong in the cross-section of G7 countries.
How can the negative relation in the middle panel be squared with the fact that the pure
discounting change can nearly perfectly explain the change in equity valuations over time (as
documented in the left panel)? Two aspects of the results help in interpreting this. First,
note that the best-fit line in the middle panel does not pass through the origin: unlike the
∆equity yield–∆pure discounting relationship in the left panel (which features an intercept
indistinguishable from zero), the line in the middle panel is shifted by 2.9 percentage points
to the left. Enforcing an intercept of zero in this ∆equity yield–∆ˆ︁r ∗relationship, we instead
estimate a very small slope (close to -0.1) and an adjusted R2 of -0.15. Explaining changes in
valuations in absolute terms evidently requires using the pure discounting change.
Second, after accounting for the pure discounting change in the left panel, the remaining
terms in ∆r∗provide very little additional explanatory power for long-term valuation changes.
In a regression for ∆equity yield on both the pure discounting change and the remaining
∆ˆ︁r ∗terms, only the coefficient on the pure discounting change is significant (slope 0.9,
p < 0.01), and the adjusted R2 increases only from 0.79 (in the left panel of Figure 3) to 0.81.
To visualize this marginal contribution from growth and uncertainty, Appendix Figure B.1
shows a version of the middle panel of Figure 3 where the change in the equity yield is
residualized against the change in the pure discounting term. The part of the equity yield
change unexplained by the pure discounting change is generally small quantitatively, and it
is now at most very weakly related to the change in rates from the growth and uncertainty
terms, consistent with the more ambiguous effects predicted theoretically.
Moving to the right panel of Figure 3: while we observe comovement between equity
yields and the different components of interest rates, there is almost no relation between
equity yields and rates themselves. The components of rate changes have happened to be
somewhat negatively related (albeit weakly so) across countries, so adding the horizontal-axis
values in the two left panels of the figure generates a muddled and weak relationship between
rates and equity yields. In addition, while the estimated slope of the best-fit line is positive,
note that it again does not pass through the origin: the average advanced economy had close
to no equity valuation change, while nonetheless experiencing growth-rate and uncertainty
shocks large enough to decrease real rates by nearly 300 bps. This emphasizes how comparing
equity valuations to real rates directly can paint a misleading picture.
Discussion and Interpretation
Taken together, Figure 3 provides a clear view of both (i) the secular declines in real rates
across countries in recent decades, and (ii) their relation to equity valuations. For the U.S., the
24


---

part of the r∗decline unexplained by changes in expected growth and uncertainty — around
90 bps, or 35% of the total r∗decline — represents the pure discounting shock, akin to a
decrease in the pure rate of time preference. Such a decrease predicts an increase in equity
valuations, exactly as we see in the left panel of the figure. Taking Japan as a contrasting
case, its decline in r∗of 330 bps is a much smaller decline than would have been expected
on the basis of the large decrease in long-term expected growth, indicating a positive pure
discounting shock. This positive shock similarly perfectly matches the decrease in Japanese
equity valuations. The same applies for all the other countries considered.
While the pure discounting shocks provide a very good description of equity valuation
changes in an accounting sense, the question of how to interpret them remains somewhat
open thus far. We do not view these changes as likely representing a true aggregate preference
(or patience) shock among domestic investors. Instead, a “global imbalances” view of cross-
country capital flows, as described by Caballero, Farhi, and Gourinchas (2008), appears to
be a reasonable candidate explanation. The main decline in the U.S.’s estimated ρ∗occurred
in the mid-to-late 1990s and early 2000s (see Figure 2). This period coincides with a large
decrease in the U.S.’s net foreign asset position. Japan’s estimated ρ∗, meanwhile, increased
during this decade. Strong demand for U.S. assets, particularly from investors in countries
experiencing large shocks to the perceived soundness of their financial system (e.g., in the
wake of the Japanese stock-market crash), matches both the timing and the cross-country
patterns observed in Figure 3, as we discuss in greater detail in Section 5.1 below.
3.3
Higher-Frequency Changes and Forecasting Regressions
Interest-rate movements influence not only secular changes in valuations but also higher-
frequency fluctuations. In this subsection, we study how stocks move with the different
components of real rates at a higher frequency. This allows us to examine these relationships
over time within a country, in contrast to considering full-sample changes across countries.
As motivating evidence, in Figure 4, we first examine whether variation in the previously
estimated pure discounting term aligns with stock-price changes over time in the U.S. data.
The figure illustrates a strong comovement between the two. Regressing the pure discounting
term on the equity yield allows us to estimate the share of variation in the equity yield that
can be explained by pure discounting, using the slope coefficient in this regression.16 That
number is 77%, emphasizing the important role of the pure discounting term on its own.
This strong comovement arises even though the pure discounting term is estimated
without any direct information about equity yields: it uses data only on interest rates,
16Writing eyt = ρt + other terms, equity yield variance is Var(eyt) = Cov(ρt, eyt) + Cov(other terms, eyt),
yielding the decomposition 1 = Cov(ρt,eyt)
Var(eyt)
+ Cov(other terms,eyt)
Var(eyt)
. The first term is the relevant regression slope.
25


---

growth expectations, and estimated entropy. One might worry that analysts back out their
growth forecasts from equity yield data, and that the growth expectations we use in our
decomposition thus mechanically contain information about equity yields. However, such
behavior would bias us against finding a relation between the pure discounting term and
equity yields: the pure discount rate is orthogonal to growth expectations by construction,
so if analysts assign variation in equity yields to expected growth, such variation would be
mechanically orthogonal to our pure discounting term.17
Figure 4 uses the pure discounting term estimated from a regression in levels; we now
estimate regressions in differences to study relationships between higher-frequency changes.
This further sidesteps the potential for spurious comovements between slowly moving variables
in levels. We balance two considerations in determining the frequency of measurement. First,
we wish to explain price and interest-rate variation for reasonably short holding periods.
Second, our estimation needs to allow for inertia in forecasters’ long-run growth and interest-
rate forecasts, which precludes us from considering, for example, monthly returns (since
forecasts are collected at most once per quarter). In our baseline analysis, we consider
three-year returns and estimate how these move with each of the components of real rates.18
The starting point for this analysis is a regression for changes in trend real rates, analogous
to equation (19) but in differences:
∆r∗
t,j = α0 + γ ∆g∗
t,j + βj ∆VIX2
t,j + Γj + εt,j,
(21)
where ∆denotes a three-year change and where the loading on the VIX term is again
country-specific.19 The residual term εt,j is now our measure of ∆ρ∗
t,j. Next, given this
estimated pure discounting change ˆ︁
∆ρ∗
t,j = ˆ︁εt,j, we regress three-year value-weighted net
market returns on that pure discounting term, the change in expected growth, and the change
in the VIX, along with a country fixed effect:
rmkt
t,j
= α1 + πρ ˆ︁
∆ρ∗
t,j + πg ∆g∗
t,j + πV ∆VIX2
t,j + Λj + νt,j.
(22)
17As an extreme case, imagine that rates depend only on pure discounting and growth, and that analysts
back out expected growth from the equity yield (Eanalysts
t
[gt+1] = eyt + constant). We would then estimate
r∗
t = α + γEanalysts
t
[gt+1] + εt = ˜︁α + γeyt + εt,
and recover ˆ︁ρ∗
t = ˜︁α + εt, which would be orthogonal to eyt by construction.
18In additional analysis, we find that our results are robust to the use of longer or somewhat shorter windows,
though the relationships weaken for windows shorter than two years (indicating inertia or measurement error).
19Coefficient estimates for regression (21) are presented in Table B.1 of Appendix B.6. The results are
similar to the level estimates in Table 1 but with smaller point estimates, suggesting stronger measurement-
error attenuation when estimating in differences (Griliches and Hausman 1986).
26


---

Figure 4: U.S. Equity Valuations and the Pure Discount Rate Over Time
1
2
3
4
Percent
1990
1995
2000
2005
2010
2015
2020
2025
Equity Div. Yield
Pure Discounting Term
(Explained Variance: 77%)
Notes: This figure shows the U.S. equity dividend yield and the pure discounting term over time, estimated
using (19)–(20) following the main specification in column (3) of Table 1. For readability, the pure discounting
term is plotted as the pure discounting residual shifted up by 2 percentage points (ˆ︁εt,j + 2).
Table 2 shows the resulting estimates. Before considering our main estimates from (22),
we start with a simpler exercise as a benchmark: we regress three-year stock returns on the
unadjusted change in the traded 10-year nominal yield. Column (1) shows the resulting
estimate for the U.S. sample. The slope coefficient is close to zero and statistically insignificant,
reflecting the well-known fact that returns on stocks and bonds are close to uncorrelated.20
In column (2), we present coefficient estimates from (22) in the U.S. data, showing how
stock returns load on each of the three drivers of interest-rate changes: changes in the pure
discount term, changes in expected growth, and changes in risk. The loading on the pure
discount term is -19 and statistically significant. This loading suggests that stock returns go
down by 19 percentage points when trend real rates increase by 1 percentage point due to
pure discounting. As in Result 2(i), this coefficient has a clear structural interpretation: it
is equal to the negative of the cash-flow duration of the overall market. This market-level
duration is often approximated by the inverse dividend yield, generating an estimate on the
order of 40 years (see, e.g., Gormsen and Lazarus 2023). While somewhat lower than that
figure, the estimate of 19 years from column (2) is of the same rough order of magnitude
and reinforces that the market is a long-duration claim. We view the estimate as a lower
bound given the potential for attenuation bias when using the higher-frequency variation in
the pure discounting term (see footnote 19 for related discussion).
The remaining estimates in column (2) show that stock returns load weakly on expected
growth changes, and significantly negatively on changes to risk, again consistent with theory.
20When regressing stock returns on the change in our r∗
t , the slope is also small and insignificant.
27


---

Table 2: Regressions for Three-Year Stock Returns
(1)
(2)
(3)
(4)
U.S.
U.S.
All
All
∆10y yield
4.19
-3.39
(3.51)
(2.20)
∆pure discount ( ˆ︃
∆ρ∗
t )
-19.1**
-9.61**
(7.64)
(3.26)
∆exp. growth
-1.49
16.9*
(14.0)
(8.82)
∆VIX2 × 100
-3.08**
-5.44***
(1.33)
(0.90)
Country FEs
✗
✗
✓
✓
Obs.
74
74
781
781
R2
0.04
0.20
0.05
0.27
Within R2
—
—
0.02
0.24
Notes: This table shows estimates from regressing three-year value-weighted market returns on changes in
10-year nominal yields (in columns (1) and (3)), and on changes in the three interest-rate components (in
columns (2) and (4)). The interest-rate components are estimated from (21), and the table presents estimates
from (22). Columns (1)–(2) consider the U.S. only, while (3)–(4) consider the full panel of developed countries
(and include country fixed effects). In columns (1)–(2), standard errors are obtained using a block bootstrap
with one-year blocks and 10,000 bootstrap draws. In columns (3)–(4), standard errors are clustered by
country and date. Statistical significance at the 10% level, 5% level, and 1% level are denoted by *, **, and
***, respectively. The sample is 1990–2023, or the longest available span for the given country.
Moving to columns (3) and (4) of Table 2, the results are largely similar in the global sample.
The slope on the pure discounting shock is smaller in the global data than in the U.S.,
conceivably reflecting greater measurement error in the non-U.S. data. Growth shocks are
also estimated to play a somewhat larger role in the global data.
These estimates allow for an accounting of the period-by-period contribution of different
interest-rate components to stock returns. We illustrate this higher-frequency return decom-
position for the U.S. data in Appendix Figure B.2, which plots the three-year annualized
equity return and each of the three fitted components from the return regression. Shocks to
risk, growth (including contemporaneous dividend growth), and pure discounting each affect
returns significantly in different periods.
As a final out-of-sample validation test for our rate decomposition, we ask whether our
estimated pure discounting term ˆ︁ρ∗
t predicts future equity returns (in addition to helping
account for contemporaneous realized returns). Long-horizon expected equity returns are
equal to µ∗
t = r∗
t + rp∗
t. Given that the uncertainty component of r∗
t is likely to be negatively
correlated with the equity risk premium rp∗
t, interest rates by themselves are unlikely to
28


---

be useful for predicting future realized returns. The pure discounting component of r∗
t , by
contrast, strips out the uncertainty component of risk-free rates, and therefore should align
well with future equity returns. We conduct such predictability tests in Appendix Table B.2,
which shows coefficients from regressions of annualized market returns over the subsequent
three years on ex ante yield-related predictors. Neither nominal yields nor our r∗
t help predict
equity returns on an unadjusted basis. This provides evidence that risk premia comove
negatively with risk-free yields, as emphasized by Farhi and Gourio (2018). Meanwhile, the
pure discounting term strongly predicts future returns.
Our rate decomposition therefore succeeds at stripping out shocks to risk-free yields with
offsetting effects on equity risk premia or growth rates, leaving us with a useful measure
of the pure discounting component of long-term rates. This pure discounting term can be
exploited as a counterfactual long-term risk-free rate to use in calculating a duration-matched
equity premium; we will return to this insight in Section 5.2.
3.4
Cross-Sectional Portfolios
We now turn to the cross-section of stock returns, and study whether firms with different
cash-flow duration have different exposure to the pure discounting term. A large literature
studies the risk and return properties of firms with different cash-flow timing (see Gormsen
and Lazarus 2023, and citations therein), finding that firms with shorter-duration cash
flows have higher risk-adjusted returns. In this section, we use our methodology to quantify
cross-sectional differences in duration, which is a key (and debated) object for this literature.
We focus here on the measure of duration used in Gormsen and Lazarus (2023), which is
based on firm-level cash-flow growth estimates. We first obtain analysts’ median forecasts of
stock-level long-term earnings growth (LTG) from IBES (see Gormsen and Lazarus 2023 for
details). For each year, we sort stocks into quintile portfolios based on their cross-sectional
LTG rank; we do so separately for the U.S. and global data. These are then our five duration-
sorted portfolios for which we calculate value-weighted returns. According to this exercise,
firms with higher expected cash-flow growth have, all else equal, longer cash-flow duration.21
In Figure 5, we report slope coefficients of regressions of three-year realized returns onto
three-year changes in the pure discounting term for our five portfolios of U.S. stocks with
different cash-flow duration. The figure shows that the portfolio of firms with the shortest
cash-flow duration has a slope coefficient of around -10, while the portfolio of firms with the
longest cash-flow duration has a slope of -30. At face value, these estimates suggest that the
21Another standard approach is to proxy for duration by valuation ratios (like book to market), since a
higher valuation is associated with a longer cash-flow duration (i.e., growth firms are long-duration firms).
Using book-to-market ratios to measure duration does not affect this section’s results.
29


---

Figure 5: Portfolio Exposures to Pure Discount Rates and Yields: U.S. Stocks
1: Shortest Duration
2
3
4
5: Longest Duration
-40
-30
-20
-10
0
10
Percent Change Per 1pp Yield Change
Pure Discounting Change
Raw 10Y Yield Change
Notes: This figure shows slope estimates from univariate regressions for three-year returns of each of five
equity portfolios on the three-year change in (1) the pure discounting term ( ˆ︃
∆ρ∗
t ), marked in red, and (2) the
nominal 10-year yield, marked in orange. Each regression contains a constant. For example, the first point in
the top left of the figure shows ˆ︁β1 (and 95% confidence intervals) from rt,1 = α1 + β1 ( ˆ︃
∆ρ∗
t ) + εt,1, where
rt,1 is the three-year return on a value-weighted portfolio of the stocks in the bottom quintile of cash-flow
duration. The pure discounting term is estimated from (21) using U.S. data. Duration-sorted portfolios and
returns are calculated following Gormsen and Lazarus (2023). The sample is 1990–2023.
cash-flow duration of these portfolios varies from 10 to 30 years, significant both economically
and statistically. We show corresponding results for the global sample in Figure B.3.
As with the previous analysis, it is possible that the slope coefficients suffer from attenua-
tion bias. If such attenuation bias is driven by classical measurement error, it is similar (in
percentage terms) for the different portfolios. In this case, it is useful to focus on the ratio of
the cash-flow duration of the different portfolios, as this ratio will be unaffected by classical
measurement error. We find that the portfolio of firms with the longest duration has three
times as long a cash-flow duration as the portfolio of firms with the shortest duration. A
lower bound on this difference appears to be 20 years, but we cannot rule out that it is longer.
By contrast, as can be seen in the coefficients plotted in orange, long-duration stocks
are not substantially more exposed to raw interest-rate changes than short-duration stocks:
all of them have very small estimated loadings when regressing their returns on the change
in 10-year nominal yields. And the estimated coefficients go in the “wrong” direction, at
least with respect to an interpretation of all interest-rate changes as being exogenous pure-
discounting shocks: rather than returns decreasing when interest rates increase, they instead
weakly increase. This further reinforces the point made in Section 2.3: equity duration does
not correspond to the price sensitivity of equity to an arbitrary change in interest rates.
Instead, only pure discounting shocks induce interest-rate variation that passes through to
equity in proportion to its duration. Duration-sorted portfolios should not, and do not, vary
30


---

significantly in their exposure to nominal interest rates by themselves; instead, they vary
only in their exposure to pure discount-rate changes.
4.
Robustness and Statistical Tests
We now assess the robustness of our main results to alternative measurement choices, and we
also provide formal statistical tests of the results in Figure 3. We first show in Section 4.1
that our rate decomposition yields similar results under a range of approaches for measuring
the trend real rate and its components and is statistically robust. Section 4.2 then discusses
how our analysis generalizes to handle the case in which dividend growth is not proportional
to output growth due to time-varying profit shares.
4.1
Testing Alternative Measures for the Rate Decomposition
Table 3 shows a series of robustness tests for our main results under alternative measurement
approaches for the real-rate decomposition. The top panel repeats the main cross-country
pass-through analysis from the first panel of Figure 3 (and Figure 1 in the introduction),
confirming that the one-for-one relationship between equity yields and the pure discounting
term holds across specifications. The bottom panel verifies the U.S. time-series properties
of ρ∗documented in the previous section.
Column (1) reports results from the baseline specification. For the top panel, this is
the same regression as in the first panel of Figure 3, but now with standard errors and
statistical significance reported. These are computed via a non-stationary block bootstrap
described in Appendix B.2.
This bootstrap accounts for estimation uncertainty in the
generated regressor ˆρ∗, providing statistical evidence to buttress the strong visual relationship
in Figure 3. The slope coefficient of 1.14 is highly significant and statistically close to the
theoretical benchmark of 1, and the intercept is not significantly different from zero.
The remaining columns vary the inputs to the r∗decomposition, with data described fully
in Appendix B.3. Column (2) uses forecasts from the Survey of Professional Forecasters (SPF)
for the 10-year real yield and real GDP growth over the next 10 years, in place of the baseline
Consensus forecasts. The top panel for this column is blank given that the SPF is U.S.-specific.
Column (3) replaces our baseline r∗with the cross-country natural-rate estimates of Del Negro
et al. (2019). These are statistical-model-implied estimates of the trend short-term real rate,
so they differ from our baseline both in maturity and in being model-based rather than
survey-based. Because they explicitly separate the trend in expected short rates from the
term premium in long-term yields, the estimates are free of any term-premium component.
Column (4) uses a country-level 6-month GARCH(1,1) forecast of equity return variance
31


---

Table 3: Robustness to Alternative Measures for r∗Decomposition
(1)
(2)
(3)
(4)
(5)
Baseline
SPF-Based
Short-Term r∗
GARCH Vol.
Unc. Index
Inputs changed:
—
r∗, g∗
r∗
L∗
L∗
Robustness of Figure 3: Regressions of ∆ey∗on ∆ρ∗(G7)
Slope
1.14***
—
1.01***
1.01***
1.15***
(0.23)
(0.16)
(0.20)
(0.24)
Intercept
0.20
—
0.64**
0.31
0.28
(0.31)
(0.28)
(0.29)
(0.30)
Adj. R2
0.79
—
0.74
0.79
0.79
Robustness of ρ∗: Time-Series Properties (U.S.)
∆ρ∗over sample
-0.84
-1.35
-0.89
-0.94
-0.91
Corr(ρ∗, ρ∗
baseline)
1.00
0.83
0.84
0.98
0.99
Notes: This table shows robustness of the main results to alternative measurement approaches for the r∗
decomposition. All r∗decompositions follow the specification in column (3) of Table 1 for measures available
across countries (columns (1), (3)–(5)), and they follow column (1) of Table 1 for the U.S.-only measure
(col. (2)). Col. (1) uses the baseline specification as in the left panel of Figure 3. Col. (2) replaces the
Consensus data with SPF forecasts for the average 10-year real yield and real GDP growth over the next
decade. Col. (3) replaces the Consensus-based r∗with the cross-country short-term natural-rate estimates of
Del Negro et al. (2019). Col. (4) replaces VIX2 with a country-level 6-month GARCH(1,1) forecast of equity
return variance. Col. (5) replaces VIX2 with the country-level Baker, Bloom, and Davis (2016) uncertainty
index. The top panel shows cross-country (G7) regressions of full-sample changes in equity yields on changes
in ρ∗, for all available specifications. Standard errors in parentheses are obtained via block bootstrap by year
with 10,000 draws. Statistical significance at the 10% level, 5% level, and 1% level are denoted by *, **, and
***, respectively. The bottom panel shows U.S. time-series results. The first row shows the full-sample change
in the estimated ρ∗. The second row shows the correlation between the alternative measure of ρ∗and the
baseline measure from column (1). The sample is 1990–2023, or the longest available for the given country.
in place of VIX2, to help address the possibility that VIX2 may not adequately measure
uncertainty or its relation to equity risk premia. Similarly, column (5) uses the country-level
Baker, Bloom, and Davis (2016) economic policy uncertainty index in place of VIX2.
Across all specifications, the results are strongly consistent. For the cross-country regres-
sions, the slope coefficients range from 1.01 to 1.15, all highly significant and close to the
theoretical prediction of one-for-one pass-through. The U.S. time-series results are similarly
robust: the full-sample change in ρ∗ranges from -0.84 to -1.35 percentage points across
specifications, generally accounting for a minority of the overall change in r∗over the sample.
The correlations between each alternative ρ∗measure and the baseline are uniformly very
high, indicating that the different measurement approaches identify very similar variation in
the pure discounting term over time.
The results in column (3), in particular, provide evidence that our baseline pure discounting
32


---

term is not spuriously picking up variation in the expected term premium. We still find the
same one-for-one pass-through of ∆ρ∗to equity yields when starting from this short-term
r∗measure, and the full-sample change in ρ∗is nearly identical here as in the baseline.22
Both results are inconsistent with a strong role for term premia in our estimates. The near-
identical results for short- and long-term rate measures also have a structural interpretation:
Result 3(iii) tells us that the measurement horizon does not matter for permanent shifts
in ρ∗, so column (3) suggests that our full-sample estimates of ∆ρ∗are indeed identifying
secular changes. Similarly, columns (4)–(5) suggest that our main full-sample results are not
sensitive to the use of VIX2 to measure entropy. So while this VIX-based proxy may induce
some mismeasurement at higher frequencies, it again appears that this does not affect our
results for full-sample secular changes.
In Appendix Tables B.3 and B.4, we show that our results are also robust to measuring
Consensus forecasts at longer horizons. Table B.3 uses the 10-year horizon. These forecasts
are elicited as average expected outcomes over years 6–10, rather than as direct forward-year
forecasts. (This is why we use the five-year as our baseline.) The results are nonetheless very
close to those in Table 3. Table B.4 measures g∗as the Consensus growth forecast over years
6–10 while keeping r∗at the baseline five-year horizon, allowing expected yields in five years
to depend on forward-looking growth at that point. Results are again close to unchanged.
Overall, we find that the main conclusions from Figure 3 are strongly robust to alternative
measures used to implement our decomposition.
4.2
Time-Varying Profit Shares
Our main analysis assumes that dividend growth is proportional to output growth. While log
dividends and consumption should be cointegrated at a sufficiently long horizon, they do not
comove perfectly at all dates or forecast horizons. In recent decades in the U.S., for example,
equity cash flows have outpaced GDP and consumption given increases in the corporate profit
share of income (Greenwald, Lettau, and Ludvigson 2025). We briefly consider here how
time-varying profit shares affect our analysis, with full results in Appendix B.4.
As discussed in that appendix, even when allowing for an arbitrary dividend-growth
process gt+1,d = dt+1 −dt that may be imperfectly correlated with consumption growth, it
remains the case that only shocks to the pure discounting term ρ∗
t pass through directly
from rates to equity yields. And though the pass-through of growth-rate shocks may be
different than in Result 1, it is still the case that such shocks induce weaker pass-through
22As further illustration that our results hold with shorter-term yields, Appendix Figure B.4 shows r∗
constructed from 5-year Consensus forecasts of real bill yields (available over a shorter sample) and compares
the resulting ρ∗series to the baseline ρ∗. The two are nearly indistinguishable for the overlapping sample.
33


---

than pure-discounting shocks in general. While there may now be pure dividend-growth
shocks (i.e., changes to g∗
t,d without corresponding changes in g∗
t ), these are separate from the
interest-rate dynamics considered in our empirical decomposition for r∗
t .
To reconcile this with the importance of profit-share shocks estimated in recent literature,
note that such changes may raise contemporaneous cash flows without affecting expected
future growth. In this case, prices and cash flows rise together, leaving equity yields unaffected.
Alternatively, equity cash-flow growth expectations may have diverged meaningfully from
output-growth expectations. While these changes to expected future profit-share growth
would be separate from the interest-rate shocks we study, we can nonetheless estimate their
magnitude and effects on valuations using two additional U.S. forecast measures: Consensus
forecasts on corporate profit growth, and IBES forecasts of long-term earnings growth.
As shown in Appendix B.4, in both cases, profit-share shocks appear to have materialized
mainly as changes in current cash flows rather than expected future growth rates, leaving
equity yields close to unaffected. Our estimated pass-through of roughly 1/3 of the decline in
r∗
t to equity valuations in U.S. data remains unchanged, as do our higher-frequency return
regressions when we add profit-share controls. Our main results therefore still apply.
5.
Empirical Implications and Economic Mechanisms
This section considers a series of further applications of our framework and results. In
Section 5.1, we examine one potential mechanism underlying variation in the pure discount
rate over time: cross-country capital flows. We then use our framework to shed light on
three questions that have been debated in recent literature: (1) the “duration-matched”
equity premium (Section 5.2), (2) the effect of decreasing interest rates on the value premium
(Section 5.3), and (3) the potential role of an information effect in explaining stock-price
responses to monetary policy news (Section 5.4).
5.1
Cross-Country Capital Flows
While pure discount-rate shocks align closely with equity valuation changes in our sample,
how to interpret these shocks remains an open question. While ρ∗is formally equivalent
to the marginal investor’s rate of time preference, shifts in ρ∗are unlikely to reflect such
preference changes alone: the notion that Japanese households have become significantly
more impatient relative to U.S. households, for instance, seems dubious.23 As an alternative
candidate channel, we consider the potential role of cross-country capital flows in explaining
23Demographic changes could in principle drive such preference shifts. However, secular-stagnation theories
(e.g., Eggertsson, Mehrotra, and Robbins 2019) often predict that aging should be associated with larger
declines in rates. By contrast, we find that ∆ρ∗in Figure 3 is positively related to a country’s degree of aging.
34


---

Figure 6: Pure Discount Rates and Net Capital Flows in the U.S.
-6
-5
-4
-3
-2
-1
Percent of GDP
-1
-.5
0
.5
1
1.5
Percent
1990
2000
2010
2020
Pure Discounting Term (LHS)
Cap. Account Balance (RHS)
Notes: The blue line shows the end-of-year pure discounting term ˆ︁ρ∗
t,j in the U.S. data, as plotted in Figure 2.
The red line shows the U.S. net capital account balance as a share of GDP, measured from the IMF’s “Net
Financial Account” series. The figure plots ˆ︁ρ∗against annual flows, as Proposition 1 of Caballero, Farhi, and
Gourinchas (2008) shows that permanent shocks lead to persistent annual flow effects.
changes in pure discount rates. Such capital flows can in principle affect interest rates
in a manner not fully accounted for by domestic fundamentals; since ρ∗absorbs any rate
movements not explained by growth or risk, the flows must result in a change in this term.
Concretely, consider a shock that generates strong foreign demand for U.S. assets. For
example, following the “global imbalances” model of Caballero, Farhi, and Gourinchas (2008),
such demand might arise from foreign investors experiencing a shock to the perceived
soundness of their local financial system. The resulting demand for U.S. assets, if relatively
inelastic, can push down U.S. interest rates without corresponding changes in U.S. growth
expectations or uncertainty. In our decomposition, this would manifest as a decline in the
U.S. pure discounting term ρ∗.24 And as long as bond and equity markets are integrated,
this change in ρ∗then passes through to equity discount rates and prices following Section 2.
We therefore examine whether capital flows help explain our estimated pure discount-rate
changes. We begin with time-series evidence in the U.S. data. As Figure 6 shows, the
variation in estimated ρ∗(plotted on the left axis) aligns well with annual net capital flows
measured with IMF data (on the right axis, where negative numbers indicate net inflows into
U.S. assets). The main decline in the U.S.’s ρ∗occurred in the mid-to-late 1990s and early
2000s, a period coinciding with a sharp decrease in net capital flows.
In Appendix Figure B.5, we analyze whether capital flows help account for pure discount-
24An alternative to the global imbalances view is that pure discount rates and interest rates may have
converged toward a common global level given financial integration, with capital flows driving this convergence.
35


---

rate changes in the full panel of G7 countries. There is a fairly strong, positive relation
between the full-sample change in a country’s ρ∗and the change in its net foreign asset
position (calculated from cumulated net capital flows to remove mechanical valuation effects).
Countries that received more capital inflows experienced larger declines in ρ∗. Such capital
flows thus represent one plausible source of cross-country changes in pure discount rates. That
said, capital flows are themselves determined in equilibrium, and they relate to fundamentals
in ways that we do not consider here. So while these flows help account for the observed
changes in pure discount rates, we leave a deeper analysis of causal drivers for future work.
5.2
Estimating the Equity Premium
Recent work by van Binsbergen (2024) and Polk and Vuolteenaho (2026) reassesses the
performance of the stock market by comparing its realized returns to those of long-term
bonds.25 Both papers argue long-term bond returns provide a natural comparison for equities,
as equities have a long cash-flow duration themselves. They find that realized stock returns
are similar to the realized returns on a duration-matched Treasury portfolio in recent decades,
implying a realized excess return on stocks close to 0%. Van Binsbergen describes this finding
as a puzzle, possibly reflecting either low equilibrium compensation for dividend risk or
unexpected negative shocks to the path of cash flows.
Our analysis lends support to one aspect of these papers’ argument, as we show in Result 3
that a duration-matched rate measure is indeed the relevant benchmark for equity. That
result, however, applies to one specific rate measure: the pure discount rate. Unadjusted
bond returns, by contrast, may not be a good benchmark for stocks. Realized stock returns
are likely to appear low (or high) when compared to realized returns on long-term bonds:
only movements in bond prices (rates) that are driven by pure discounting shocks are fully
passed through to stocks. Movements that are driven by growth rates are mostly unrelated to
valuations, and movements driven by uncertainty have opposite effects on stocks and bonds.
Since bond returns are not incorporated into stock returns in general, stock returns are likely
to look high or low relative to bond returns even in relatively long samples.
We formalize this point through simulation studies of an artificial calibrated economy. We
consider a generic economy for which the additive decomposition of the log SDF in (2) holds
and calibrate it to match the data in terms of volatility of stock prices, growth rates, pure
discounting shocks, and risk shocks; see Appendix B.5 for details. We discipline the relation
between interest rates, growth, and risk premia based on the empirically observed relations,
but we note that using theoretically motivated parameters in the consumption-based version
25Van Binsbergen considers nominal bonds, while Polk and Vuolteenaho consider real bonds. In our
empirical analysis in Figure 8, we consider only nominal bonds to maximize the available sample.
36


---

Figure 7: Simulated Distributions of Average Excess Equity Returns
0
10
20
30
Density
-10
-5
0
5
10
15
Estimated Equity Premium (%)
Equity – Lagged Long-Term Yield
Equity – Dur.-Matched Bond Return
Equity – Pure Disc. Claim Return
Notes: This figure shows the results of simulations of calibrated economies. We simulate changes in growth
rates, pure discounting terms, and uncertainty in 30 year samples. Based on these realizations of the structural
variables, we calculate realized returns on equity and bonds. The figure shows the distributions of average
30-year realized excess returns on stocks across 100,000 simulations. The excess returns are calculated relative
to three benchmarks: the lagged long-term interest rate (black), the realized returns on a duration-matched
bond portfolio (red), and the realized returns on a duration-matched pure-discounting claim (blue), as defined
in equation (23). The true equity premium relative to the long-term yield is shown in the dashed gray line,
and the mean of all three distributions is equal to the true premium. Details of the simulations can be found
in Section 5.2 and Appendix B.5.
from Section 2.2 gives similar results. Using this model, we run 100,000 simulations of
artificial 30-year samples and calculate and compare realized returns on stocks and bonds.
Figure 7 shows that realized stock returns can deviate substantially from realized returns
on a duration-matched bond portfolio, and that the difference between the two is a poor
estimate of the equity risk premium. The figure shows distributions of average excess returns
on stocks relative to three benchmarks. For the first two benchmarks, we consider the ex
ante long-term interest rate (black) and the realized return on a duration-matched bond
portfolio (red). The two benchmarks deliver the same average excess returns across the
simulations (the risk premium of 4%), which is mechanical because the expected return on
the duration-matched bond portfolio is the long-run interest rate in our simulations. But
the distribution of estimated excess returns is much wider when comparing stock returns to
realized bond returns: while observing negative excess returns relative to the ex ante yield
is highly unlikely, there is a greater probability (around 10%) of observing negative excess
returns when comparing stocks to the realized returns on the duration-matched portfolio.
Seen in this light, a near-zero duration-matched equity premium may be somewhat unlikely,
37


---

but it is within the range of what should be expected from such exercises.
The results suggest that controlling for duration-matched bond returns is unlikely to
improve estimates of the equity risk premium. But our framework suggests that one can,
in fact, improve estimates by controlling for changes in the pure discounting term. As in
Results 2–3, the effect of a change in the pure discounting term ρ is given by the duration of
the stock market times the change in ρ. We can then calculate the realized excess returns
net of shocks to the pure discounting term as
rρ-hedged
t,t+n
= rstocks
t,t+n −rf
t,t+n −D(ρt −ρt+n),
(23)
where rf
t,t+n is the ex ante long-term interest rate. The value rf
t,t+n + D(ρt −ρt+n) can be
thought of as the return on a “pure discounting claim,” or a bond that appreciates only when
the pure discount rate decreases. The equity return net of this pure discount claim return
thus provides an equity return hedged against changes in ρ.
As shown in the third line in Figure 7, realized excess returns net of the pure discounting
claim offer a more precise estimate of the equity risk premium than the other approaches.
This distribution of excess returns (blue) has the same mean across simulations as the other
approaches, so the three methods extract the same equity risk premium on average (the true
equity premium). But the ρ-hedged excess returns have a tighter distribution around this true
premium: realized stock returns are influenced by unexpected shocks to ρ, and accounting
for these shocks brings the realized returns closer to the ex ante equity premium. Because of
the market’s long duration, these changes can have a meaningful impact even though the ρ
shocks are modest in magnitude. Given our calibrations, the 95% confidence interval for the
ρ-hedged excess return is 1.7 to 6.6%, which is tighter than the confidence interval for the
standard approach (1.2 to 7.4%). The confidence interval for the duration-matched bond
approach is twice as wide as the interval for the ρ-hedged approach (-1.0 to 9.2%).
Motivated by the above results, we estimate the U.S. equity risk premium over our sample
period based on the three approaches above: (1) the market return in excess of the long-term
nominal bond yield, (2) the market return in excess of the duration-matched nominal Treasury
return, analogous to van Binsbergen (2024),26 and (3) the market return hedged against
changes in the value of the pure discounting claim.
These cumulative returns are plotted in Figure 8. As can be seen in the black line, the
26Our nominal bond return calculation is somewhat less sophisticated than his. He constructs a bond
portfolio with multiple nominal bonds, each weighted in proportion to the value weight of the market’s
expected future dividend at the corresponding maturity. By contrast, our counterfactual nominal log bond
return is equal to rt+1,n = yt,t+19 −D(yt+1,t+20 −yt,t+19), where D = 19.1 years from Table 2, and where we
take the 19-year zero-coupon yield from Gürkaynak, Sack, and Wright (2006).
38


---

Figure 8: Cumulative Excess Returns for the U.S. Market
-50
0
50
100
150
Cumulative Log Return (%)
1990
2000
2010
2020
Market – Lagged Nominal Yield (Mean Simple Re: 6.7%)
Market – Dur.-Matched Pure Discounting Return (5.6%)
Market – Dur.-Matched Nom. Treasury Return (3.0%)
Notes: This figure shows cumulative log returns on the value-weighted U.S. stock market in excess of three
different counterfactual bond returns. The black line shows the return relative to the one-period-lagged
19-year nominal zero-coupon yield from Gürkaynak, Sack, and Wright (2006), where we use a 19-year duration
given the results in Table 2. The blue line shows the return relative to the duration-matched pure discounting
claim, calculated as in (23) using the estimated ˆ︁ρ∗
t from (20). The red line shows the return relative to an
unadjusted nominal Treasury security with duration D = 19.1 years; see footnote 26 for details of construction.
In all cases, we calculate cumulative log returns for equity and for bonds separately and plot the respective
difference. The mean simple excess returns listed in the legend are calculated as average arithmetic (not
logarithmic) excess returns for non-overlapping one-year periods.
market has had high average returns relative to the long-term risk-free rate over this period,
with a realized annual arithmetic equity premium of 6.7%. The red line shows a version of
the finding in van Binsbergen (2024) and Polk and Vuolteenaho (2026): when compared
to the holding-period returns on long-term Treasuries, much of this premium disappears.
The full-sample average return on this nominal-Treasury-adjusted basis is 3.0%. But before
considering the last three years of the sample (which featured increasing interest rates and
high equity returns), there was no excess return relative to the duration-matched nominal
Treasury: the red line in Figure 8 crosses zero in the fourth quarter of 2020, indicating
precisely zero average excess return in the preceding 30 years of the sample.
By contrast, the return on equity in excess of the pure discounting claim, shown in blue,
is high and stable. On an annualized basis, this realized excess return is estimated to be 5.6%
over this period, only slightly lower than the 6.7% benchmark. As a result, we can conclude
that the estimated equity risk premium is close to the historical average even after accounting
for the secular decline in the pure discount rate. Over the sample, the pure discount rate
goes down by slightly less than 1 pp, which, accounting for the duration effect, leads to a
19% reduction in the realized excess log stock return. This effect has to be averaged out over
39


---

the 35-year sample; when converted to simple returns, the estimated equity risk premium
decreases by roughly 1% per year.
Taken together, this section argues against comparing realized stock returns to a duration-
matched bond counterfactual if the goal is to estimate the equity premium. Subtracting
realized bond returns from realized stock returns adds more noise than it subtracts, leading
to less precise estimates of the equity premium on average. In our sample, this approach
leads to an excess stock return close to 0%. This estimate can appear puzzling, but it is
explained by changes in growth rates and risk premia. Once accounting for these changes,
realized stock returns are close to the historical equity premium.
5.3
The Value Premium and Interest Rates
We next turn to a puzzling pattern observed in the cross-section of stocks in recent decades.
The value premium — measured as the average return on stocks with high book-to-market
ratios minus stocks with low book-to-market ratios, or HML (Fama and French 1993) —
has been substantially weaker in recent decades than implied by historical averages. One
potential explanation for this underperformance could be that interest rates have dropped,
which has led to an unexpected capital gain for the long-duration growth firms, leading
growth firms to have performed better than expected ex ante.27 On the surface, this effect
could be meaningful. Imagine that growth firms have a 30-year longer duration than value
firms. A naive calculation would imply that a roughly 3 percentage point drop in interest
rates would have led to a 90 percentage point relative outperformance of growth firms. Over
a 20-year span, this translates to a relative outperformance of more than 4 percent per year,
which is large enough to wipe out effectively the entirety of the historical value premium.
The above calculations are, however, not the full story, as discussed in previous sections.
First, while interest rates have dropped by close to 3 percentage points in the U.S., the pure
discounting term has dropped by only about 1 percentage point, and it is only this component
that should pass through to long-duration assets. Second, we estimate that the spread in
duration for value-sorted portfolios is substantially below the 30 years assumed above. The
net effect on the realized return on the value factor is therefore substantially smaller.
We illustrate and quantify the effect of changes in the pure discounting term for the value
factor in the U.S. data in Figure 9. The figure shows both cumulative returns for the HML
factor (in black, corresponding to the left axis), and the estimated contribution of changes
in the pure discounting component of real rates (in blue, right axis). This pure-discounting
contribution is estimated by regressing HML returns on the change in the residual ˆ︁ρ∗
t,j from
27This hypothesis is discussed by Maloney and Moskowitz (2021) and Asness (2022), among others.
40


---

Figure 9: The Contribution of Pure Discount Changes to Value Factor Returns
-30
-20
-10
0
10
Percent
-30
0
30
60
90
Percent
1990
2000
2010
2020
Cumulative HML Return (LHS)
Cumulative Pure Discounting Contribution (RHS)
Notes: The black line shows the cumulative return on the Fama and French (1993) HML value factor for
the U.S. sample since 1990, obtained via Ken French’s website, plotted on the left axis. The blue line
shows the contribution we estimate is attributable to the pure discounting component of real rates, plotted
in cumulative percent terms on the right axis. For this estimated contribution, we begin with the pure
discounting residual ˆ︁ρ∗
t,j, estimated using (19)–(20) following the main specification in column (3) of Table 1,
as plotted in Figure 2. We regress three-year HML returns on the three-year change in this residual, along
with the three-year change in expected growth rates and the three-year change in the squared VIX (akin
to (22)). The estimated contribution from the three-year residual is then the estimated coefficient on ∆ˆ︁ρ∗
t,j
multiplied by the cumulative change in ˆ︁ρ∗
t,j since 1990.
equations (19)–(20), controlling for changes in growth rates and uncertainty,28 and then
multiplying the estimated coefficient by the cumulative change in ˆ︁ρ∗
t,j since 1990.
As the figure shows, the effect of the pure-discounting term is modest but non-trivial,
reaching a cumulative effect of -20% return at the trough in 2020, but only -10% over the full
sample. In addition, the crash and rebound of the value factor from 2020–2023 matches the
dramatic changes to the pure discount term experienced over those years at least in timing,
if not fully in magnitude: the cumulative HML return over that period is around 30% (on
the left axis), while the percent attributable to the pure discounting term is around 10% (on
the right axis). So while the pure discounting contribution is often important, it is clearly
not the full story explaining the performance of value in recent decades in the U.S. sample.
In Appendix Figure B.6, we exploit our global panel to study what share of the cross-
28This estimation exercise parallels the one in equation (22) for the overall market, with the exception
that here we use the change in the residual ˆ︁ρ∗
t,j estimated in levels from (19) (rather than the residual from
the first-difference estimation in (21)). We do so because this allows for straightforward estimation of a
cumulative effect of the change in ˆ︁ρ∗
t,j in levels, as needed for the exercise in Figure 9. Cumulating the
effects of three-year changes ˆ︁
∆ρ∗
t,j, by contrast, would only allow for measurement of the pure discounting
contribution every three years (so the blue line in Figure 9 would only show 11 equally spaced points).
41


---

country differences in realized value returns since 1990 can be explained by cross-country
differences in the evolution of the pure discounting term. The figure shows that value firms
in countries that have experienced a larger decrease in the pure discount term have had
lower realized premia relative to growth firms over the sample period. The cross-sectional
R2 demonstrates meaningful explanatory power, but it also indicates that the returns to the
value factor cannot be fully summarized by changes in the pure discounting term.29 So the
pure discounting change is again important for explaining a share, but not the entirety, of
the performance of value portfolios across countries.
5.4
Unpacking Monetary Policy Shocks
As a final exercise, we use our decomposition and estimation results to help unpack the effects
of surprise changes in short-term interest rates by monetary policymakers. These surprises,
when properly measured (e.g., using high-frequency changes in interest rates around policy
announcements), are by construction exogenous shocks to short-term nominal rates. But
while it may seem intuitive to treat the resulting changes in long-term rates as if they represent
pure discounting shocks,30 this is not necessarily a valid assumption: while the change in the
short-term rate is exogenous, the long-term yield change depends on changes to the pure
discount rate as well as changes to perceived long-term growth and uncertainty. That is,
the long-term real yield change depends not just on the short-rate shock (and its perceived
persistence), but also on the market’s perceived future changes to endogenous outcomes
resulting from this shock, as also pointed out by Chen (2022). Further, the sensitivity of
stock prices to these shocks does not identify stocks’ cash-flow duration.
A benefit of our framework is that we can directly estimate the perceived effect of any
given shock on the separate components of real rates. One approach to this would be to
observe the change in expected growth rates around an announcement and then strip out
these changes, akin to the approach taken in Section 3. But the timing of the Consensus
Economics surveys makes such an approach challenging when considering high-frequency
shocks like monetary policy surprises. First, the surveys are conducted infrequently (either
every six months or every three months), and forecasters may exhibit inertia in changing
their growth-rate forecasts after a given shock. Second, the surveys prior to a given shock
may be stale by the time of the FOMC meeting, inducing a possibly spurious positive relation
between expected-growth revisions and policy surprises; see Bauer and Swanson (2023a).
Instead, we use the fact that we observe three high-frequency asset-price changes on the
29We find that the same results hold — both within and across countries — when considering HML alpha
(i.e., on a market-adjusted basis), rather than considering the raw value premium.
30See, for instance, Kroen et al. (2022).
42


---

Table 4: Responses of Recovered Rate Components to Monetary Policy Shocks
(1)
(2)
(3)
(4)
∆10y yield
∆pure discount ( ˆ︃
∆ρ∗
t )
∆exp. growth
∆VIX2 × 100
mps⊥
0.42***
0.28***
0.09*
1.15***
(0.06)
(0.04)
(0.05)
(0.38)
Obs.
292
292
292
292
R2
0.37
0.31
0.05
0.04
Notes: This table shows estimates of β from regressions ∆xt = α+βmps⊥
t +εt, where ∆xt is the high-frequency
change in variable xt around an FOMC announcement, and mps⊥
t is the orthogonalized monetary policy
shock from Bauer and Swanson (2023b) in percentage points. In column (1), ∆xt is the 30-minute change in
the 10-year nominal yield. In columns (2)–(3), ∆xt are the recovered 30-minute changes in pure discount rates
and expected growth based on the high-frequency stock-price and interest-rate changes, as obtained from
(24)–(25). In column (4), the outcome variable is the daily change in the squared VIX. Standard errors are
obtained using a block bootstrap with one-year blocks and 10,000 bootstrap draws. The sample is 1990–2023.
announcement dates: the change in long-term yields ∆yt,t+n, the return on the market rmkt
t
,
and the change in uncertainty proxied by ∆VIX2
t. And our previous estimation provides a
mapping from any change in ρt, expected growth gt, and uncertainty VIX2
t to a change in
long-term yields and stock returns. As a result, this mapping can be inverted to provide an
estimate of the change in ρt and gt implied by the observed asset-price changes. For example,
a positive market return coinciding with an increase in yields implies that expected growth
must have increased by enough, or uncertainty must have decreased by enough, to offset
any given increase in the pure discounting term. Given that we can observe the change in
uncertainty, these two reactions in fact pin down the required change in both terms.
To implement this idea for the high-frequency data, we start from estimates of the
rate decomposition in (21) using three-year changes in the 10-year r∗, and the stock-return
regression in (22) using the three resulting terms from the rate decomposition. These give
us the loadings mapping changes in growth, uncertainty, and pure discount rates to yield
changes and stock returns, and we will assume that these mappings hold as well on policy
announcement days.
We then use data from Bauer and Swanson (2023b), who provide changes in 10-year
nominal yields, S&P 500 futures returns, and monetary policy shocks (orthogonalized with
respect to ex ante predictors) in 30-minute windows around FOMC announcements. Based on
the results of Nakamura and Steinsson (2018, Table I), we assume that the change in 10-year
nominal yields is equal to the change in 10-year real yields, ∆yt,t+10. Finally, we calculate
the daily change in the VIX2
t on the announcement day. Using these observed high-frequency
changes and our estimated coefficients in the real-rate and stock-return regression, we invert
43


---

the following two equations for the two unknowns ∆ρt and ∆gt:
∆yt,t+10 = ∆ρt + ˆ︁γ ∆gt + ˆ︁βj ∆VIX2
t,
(24)
rmkt
t,j
= ˆ︁πρ ∆ρt + ˆ︁πg ∆gt + ˆ︁πV ∆VIX2
t.
(25)
We then regress the recovered ∆ρt and ∆gt, as well as ∆yt,t+10 and ∆VIX2
t, on the
orthogonalized monetary policy shocks mps⊥
t from Bauer and Swanson (2023b). Table 4
presents the results. Column (1) shows that a 100-basis-point shock — that is, a shock scaled
so that the one-year Eurodollar futures rate changes by +100 bps — results in a 10-year yield
increase of 42 bps, nearly identical to Nakamura and Steinsson (2018, Table I). Columns
(2)–(4) effectively decompose this change. The majority is attributable to an increase in the
pure discount rate of 28 bps. We estimate a weak but nonetheless positive change in expected
growth of 9 bps. There is also a significant increase in risk.
As a result, we conclude that the average monetary policy shock indeed appears reasonably
close to a pure discounting shock, at least in its effect on long-term yields. But there
is nonetheless a small, somewhat noisily estimated positive expected-growth-rate change
estimated as resulting from a contractionary shock. Intuitively, while stock returns decrease
following contractionary shocks, they do not decrease on average by quite enough — i.e.,
they decrease by less than 19% (given an estimated duration of around 19 years) for every
one-percentage-point change in long-term yields — to be consistent with a pure discounting
shock alone.31 As a result, we find some evidence in favor of an information effect on average,
using different methods than those used by Nakamura and Steinsson (2018).
The low R2 in the growth-rate regression indicates that there is meaningful announcement-
specific heterogeneity in the perceived effects on growth rates (as well as the other outcome
variables): there are some announcements with strong conventional policy responses, and
others with strong apparent information effect–type responses. To illustrate this heterogeneity,
Figure B.7 in Appendix B.6 shows binned scatter plots of implied changes in the pure discount
rate and expected growth rate against monetary policy shocks. The pure discount channel
of monetary policy is very clean and consistent: implied ρ∗
t changes increase uniformly in
mps⊥
t . The expected growth channel, meanwhile, appears non-monotonic: large easing shocks
generate conventional policy responses (whereby more negative mps⊥
t predicts a greater
increase in expected growth), while other shocks generate an apparent information effect.
31They would in fact need to decrease by more than 19%, given the small positive effect on the VIX.
44


---

6.
Conclusion
We provide a new framework and measurement tools to decompose any change in real interest
rates into mutually exclusive underlying structural changes. According to our decomposition,
only pure discounting shocks should pass through perfectly from long rates to equity valuations
theoretically. When implemented empirically with long-term survey forecast data and a panel
of asset prices, the decomposition works very well: pure discounting shocks pass through
one-for-one to equity yields, while the other components of real-rate changes do not.
The recovered pure discounting component of real rates helps us answer a range of
questions related to asset pricing, macroeconomics, and secular economic trends observed in
recent decades. In the U.S. data, we estimate that a sizable share of the decline in interest rates
since 1990 — around 35% — is attributable to the pure discounting term, indicating some
meaningful pass-through from declining yields to rising risky-asset valuations. But assuming
perfect pass-through, as a range of literature has done, nonetheless overstates the effect of
declining interest rates by roughly three times. The partial pass-through we find implies
that much of the rise in household wealth (and inequality) was likely non-mechanical.32 Our
estimates also suggest that stocks have continued to exhibit a sizable equity premium relative
to a duration-adjusted counterfactual. In further analysis, we use our decomposition to speak
to higher-frequency equity returns, explain the role of interest rates in the cross-section of
stocks, and better understand the perceived effects of monetary policy shocks.
Unpacking the drivers of country-level changes in the pure discounting term in a structural
sense, over and above the analysis of capital flows in Section 5.1, will be important for better
understanding how to interpret these changes. But in spite of the work to be done on this, our
paper provides a clear framework and tools to understand the relationship between stocks and
bonds. This bond-stock relationship appears chaotic, both at high frequencies and over the
long run, as is apparent from the stock–yield disconnect shown in the left panel of Figure 1.
But our simple framework, combined with long-term survey data, works well at isolating
a pure discounting component of interest rates that explains both higher-frequency stock
returns and longer-term secular changes in equity valuations, as in the right panel of Figure 1.
One implication of our findings is that we can nearly perfectly explain the long-term
changes in both interest rates and equities without the need for any additional convenience
yield specific to Treasuries. While such market-specific shocks may be quite important for
explaining shorter-term fluctuations, “standard” asset pricing evidently works reasonably well
at explaining the data at a low frequency.
32That said, more work needs to be done to understand the pass-through of interest-rate changes to assets
other than equity, which are important for many households’ wealth.
45


---

References
Abel, A. B. (1999): “Risk Premia and Term Premia in General Equilibrium,” Journal of Monetary
Economics, 43, 3–33.
Albuquerque, R., M. Eichenbaum, V. X. Luo, and S. Rebelo (2016): “Valuation Risk and
Asset Pricing,” Journal of Finance, 71, 2861–2904.
Alvarez, F. and U. J. Jermann (2005): “Using Asset Prices to Measure the Persistence of the
Marginal Utility of Wealth,” Econometrica, 73, 1977–2016.
Asness, C. (2022): “Is Value Just an Interest Rate Bet?” AQR Research Note.
Atkeson, A. G., J. Heathcote, and F. Perri (2025): “The End of Privilege: A Reexamination of
the Net Foreign Asset Position of the United States,” American Economic Review, 115, 2151–2206.
Auclert, A., H. Malmberg, F. Martenet, and M. Rognlie (2025): “Demographics, Wealth,
and Global Imbalances in the Twenty-First Century,” NBER Working Paper 29161.
Backus, D., N. Boyarchenko, and M. Chernov (2018): “Term Structures of Asset Prices and
Returns,” Journal of Financial Economics, 129, 1–23.
Backus, D., M. Chernov, and I. Martin (2011): “Disasters Implied by Equity Index Options,”
Journal of Finance, 66, 1969–2012.
Backus, D., M. Chernov, and S. Zin (2014): “Sources of Entropy in Representative Agent
Models,” Journal of Finance, 69, 51–99.
Baker, S. R., N. Bloom, and S. J. Davis (2016): “Measuring Economic Policy Uncertainty,”
Quarterly Journal of Economics, 131, 1593–1636.
Bansal, R. and A. Yaron (2004): “Risks for the Long Run: A Potential Resolution of Asset
Pricing Puzzles,” Journal of Finance, 59, 1481–1509.
Barro, R. J. (2006): “Rare Disasters and Asset Markets in the Twentieth Century,” Quarterly
Journal of Economics, 121, 823–866.
Barsky, R. B. (1989): “Why Don’t the Prices of Stocks and Bonds Move Together?” American
Economic Review, 79, 1132–1145.
Bauer, M. D. and G. D. Rudebusch (2020): “Interest Rates under Falling Stars,” American
Economic Review, 110, 1316–1354.
Bauer, M. D. and E. T. Swanson (2023a): “An Alternative Explanation for the ‘Fed Information
Effect’,” American Economic Review, 113, 664–700.
——— (2023b): “A Reassessment of Monetary Policy Surprises and High-Frequency Identification,”
NBER Macroeconomics Annual, 37, 87–155.
Bianchi, F., M. Lettau, and S. C. Ludvigson (2022): “Monetary Policy and Asset Valuation,”
Journal of Finance, 77, 967–1017.
van Binsbergen, J. H. (2024): “Duration-Based Stock Valuation: Reassessing Stock Market
Performance and Volatility,” NBER Working Paper 27367.
Bordalo, P., N. Gennaioli, R. L. Porta, and A. Shleifer (2024): “Belief Overreaction and
Stock Market Puzzles,” Journal of Political Economy, 132, 1450–1484.
Borovička, J., L. P. Hansen, and J. A. Scheinkman (2016): “Misspecified Recovery,” Journal
of Finance, 71, 2493–2544.
Caballero, R. J., E. Farhi, and P.-O. Gourinchas (2008): “An Equilibrium Model of ‘Global
Imbalances’ and Low Interest Rates,” American Economic Review, 98, 358–393.
Campbell, J. Y. (1986): “Bond and Stock Returns in a Simple Exchange Model,” Quarterly Journal
of Economics, 101, 785–803.
46


---

——— (2018): Financial Decisions and Markets: A Course in Asset Pricing, Princeton: Princeton
University Press.
Campbell, J. Y. and J. Ammer (1993): “What Moves the Stock and Bond Markets? A Variance
Decomposition for Long-Term Asset Returns,” Journal of Finance, 48, 3–37.
Campbell, J. Y. and J. H. Cochrane (1999): “By Force of Habit: A Consumption-Based
Explanation of Aggregate Stock Market Behavior,” Journal of Political Economy, 107, 205–251.
Campbell, J. Y., C. Pflueger, and L. M. Viceira (2020): “Macroeconomic Drivers of Bond
and Equity Risks,” Journal of Political Economy, 128, 3148–3185.
——— (2025): “Bond-Stock Comovements,” Unpublished Manuscript, Harvard University and
University of Chicago.
Campbell, J. Y., A. Sunderam, and L. M. Viceira (2017): “Inflation Bets or Deflation Hedges?
The Changing Risks of Nominal Bonds,” Critical Finance Review, 6, 263–301.
Campbell, J. Y. and S. B. Thompson (2008): “Predicting Excess Stock Returns Out of Sample:
Can Anything Beat the Historical Average?” Review of Financial Studies, 21, 1509–1531.
Chen, Z. (2022): “Inferring Stock Duration Around FOMC Surprises: Estimates and Implications,”
Journal of Financial and Quantitative Analysis, 57, 669–703.
Chernov, M., L. A. Lochstoer, and D. Song (2025): “The Real Channel for Nominal Bond-
Stock Puzzles,” Forthcoming, Journal of Finance.
Constantinides, G. M. and D. Duffie (1996): “Asset Pricing with Heterogeneous Consumers,”
Journal of Political Economy, 104, 219–240.
Décaire, P. H. and M. Guenzel (2025): “What Drives Very Long-Run Cash Flow Growth
Expectations?” Working Paper.
Del Negro, M., D. Giannone, M. P. Giannoni, and A. Tambalotti (2019): “Global Trends
in Interest Rates,” Journal of International Economics, 118, 248–262.
Dowla, A., E. Paparoditis, and D. N. Politis (2013): “Local Block Bootstrap Inference for
Trending Time Series,” Metrika, 76, 733–764.
Eggertsson, G. B., N. R. Mehrotra, and J. A. Robbins (2019): “A Model of Secular
Stagnation,” American Economic Journal: Macroeconomics, 11, 1–48.
Epstein, L. G. and S. E. Zin (1989): “Substitution, Risk Aversion, and the Temporal Behavior of
Consumption and Asset Returns: A Theoretical Framework,” Econometrica, 57, 937–969.
Fagereng, A., M. Gomez, É. Gouin-Bonenfant, M. Holm, B. Moll, and G. Natvik (2025):
“Asset-Price Redistribution,” Journal of Political Economy, 133, 3494–3549.
Fama, E. F. and K. R. French (1993): “Common Risk Factors in the Returns on Stocks and
Bonds,” Journal of Financial Economics, 33, 3–56.
——— (2002): “The Equity Premium,” Journal of Finance, 57, 637–659.
Farhi, E. and F. Gourio (2018): “Accounting for Macro-Finance Trends: Market Power, Intangi-
bles, and Risk Premia,” Brookings Papers on Economic Activity, 147–250.
Gandhi, M., N. J. Gormsen, and E. Lazarus (2025): “Forward Return Expectations,” NBER
Working Paper 31687.
Gao, C. and I. W. R. Martin (2021): “Volatility, Valuation Ratios, and Bubbles: An Empirical
Measure of Market Sentiment,” Journal of Finance, 76, 3211–3254.
Gilchrist, S., E. Yang, and G. Zhao (2024): “Equity Price Responses and the Fed Information
Effect,” Working Paper.
Gormsen, N. J. and E. Lazarus (2023): “Duration-Driven Returns,” Journal of Finance, 78,
1393–1447.
47


---

Greenwald, D. L., M. Lettau, and S. C. Ludvigson (2025): “How the Wealth Was Won:
Factor Shares as Market Fundamentals,” Journal of Political Economy, 133, 1083–1132.
Griliches, Z. and J. A. Hausman (1986): “Errors in Variables in Panel Data,” Journal of
Econometrics, 31, 93–118.
Gürkaynak, R. S., B. Sack, and J. H. Wright (2006): “The U.S. Treasury Yield Curve: 1961
to the Present,” Federal Reserve Finance and Economics Discussion Series, No. 2006-28.
Hansen, L. P. (2012): “Dynamic Valuation Decomposition Within Stochastic Economies,” Econo-
metrica, 80, 911–967.
——— (2019): “Additive Functionals,” Lecture Notes.
Hansen, L. P. and T. J. Sargent (2022): “Risk, Uncertainty, and Value,” Manuscript, University
of Chicago and New York University.
Hanson, S. G. and J. C. Stein (2015): “Monetary Policy and Long-Term Real Rates,” Journal of
Financial Economics, 115, 429–448.
Irie, M. (2025): “Wealth Inequality and Changing Asset Valuations in the Distributional National
Accounts,” Working Paper.
Kekre, R. and M. Lenel (2024): “Exchange Rates, Natural Rates, and the Price of Risk,” Working
Paper.
Kremens, L., I. W. R. Martin, and L. Varela (2025): “Long-Horizon Exchange Rate Expecta-
tions,” Journal of Finance, 80, 3695–3724.
Kroen, T., E. Liu, A. R. Mian, and A. Sufi (2022): “Falling Rates and Rising Superstars,”
NBER Working Paper 29368.
Laarits, T. (2025): “Precautionary Savings and the Stock-Bond Covariance,” Working Paper.
Lettau, M. and S. Ludvigson (2001): “Consumption, Aggregate Wealth, and Expected Stock
Returns,” Journal of Finance, 56, 815–849.
Lettau, M. and J. A. Wachter (2011): “The Term Structures of Equity and Interest Rates,”
Journal of Financial Economics, 101, 90–113.
Maloney, T. and T. J. Moskowitz (2021): “Value and Interest Rates: Are Rates to Blame for
Value’s Torments?” Journal of Portfolio Management, 47, 65–87.
Martin, I. (2013): “Consumption-Based Asset Pricing with Higher Cumulants,” Review of Economic
Studies, 80, 745–773.
——— (2017): “What Is the Expected Return on the Market?” Quarterly Journal of Economics,
132, 367–433.
Mian, A., L. Straub, and A. Sufi (2021): “Indebted Demand,” Quarterly Journal of Economics,
136, 2243–2307.
Nagel, S. and Z. Xu (2022): “Asset Pricing with Fading Memory,” Review of Financial Studies,
35, 2190–2245.
Nakamura, E. and J. Steinsson (2018): “High-Frequency Identification of Monetary Non-
Neutrality: The Information Effect,” Quarterly Journal of Economics, 133, 1283–1330.
Paparoditis, E. and D. N. Politis (2002): “Local Block Bootstrap,” Comptes Rendus Mathema-
tique, 335, 959–962.
Polk, C. and T. Vuolteenaho (2026): “Purifying the Equity Premium,” Working Paper.
Song, D. (2017): “Bond Market Exposures to Macroeconomic and Monetary Policy Risks,” Review
of Financial Studies, 30, 2761–2817.
48


---

Online Appendix:
Interest Rates and Equity Valuations
Niels Joachim Gormsen and Eben Lazarus
July 2026
Contents
A. Theoretical Derivations and Additional Discussion . . . . . . . . . . . . . .
1
A.1 Additive Log SDF Decomposition . . . . . . . . . . . . . . . . . . . . . . . .
1
A.2 Interest-Rate Decomposition . . . . . . . . . . . . . . . . . . . . . . . . . . .
7
A.3 Results for Equity Yields and Duration . . . . . . . . . . . . . . . . . . . . .
9
B. Additional Empirical Details and Results
. . . . . . . . . . . . . . . . . . .
18
B.1 Baseline Measurement Details . . . . . . . . . . . . . . . . . . . . . . . . . .
18
B.2 Details on Block Bootstrap Inference . . . . . . . . . . . . . . . . . . . . . .
19
B.3 Robustness Measures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
20
B.4 Robustness to Time Variation in Profit Shares . . . . . . . . . . . . . . . . .
21
B.5 Details on Simulations for Figure 7 . . . . . . . . . . . . . . . . . . . . . . .
23
B.6 Additional Results: Tables and Figures . . . . . . . . . . . . . . . . . . . . .
25
A.
Theoretical Derivations and Additional Discussion
This appendix provides proofs, derivations, and discussion of theoretical results as referenced
in the main text.
A.1
Additive Log SDF Decomposition
This subsection discusses the additive decomposition for the log SDF in equation (2), and
its relation to the decomposition in Hansen (2012). Given our discrete-time environment,
for notational simplicity we will in fact more directly build on Proposition 4.2.1 of Hansen
and Sargent (2022). That result provides a discrete-time analogue to the continuous-time
1


---

decomposition for additive functionals in Theorems 3.1–3.2 of Hansen (2012),33 which we
then apply to our specific setting.
We begin by defining the process ˜︂
M such that ˜︂
M0 = 1 and Mt+1 =
˜︂
Mt+1
˜︂
Mt , so mt+1 =
˜︁mt+1 −˜︁mt. We consider three settings for fundamental dynamics, mapping to the cases
considered in Section 2.2: the first two settings (stationarity with unanticipated breaks, and
a drifting steady state) underlie Case I,34 while the third (full stationarity) underlies Case II.
A.1.1
Stationarity with Unanticipated Breaks
Following Hansen and Sargent (2022), begin by defining Xt (t = 0, 1, 2, . . .) to be a stationary
Markov process of dimension n with transition equation
Xt+1 = φ(Xt, Wt+1),
(A.1)
where φ(·, ·) is a Borel-measurable function and Wt+1 is a k-dimensional vector of unanticipated
shocks satisfying Et[Wt+1] = E[Wt+1|Xt] = 0. The dynamics in (A.1) induce a transition
distribution P for X.
Given the log SDF mt+1 = ˜︁mt+1 −˜︁mt, assume that the process ˜︁m is an additive functional,
in the sense that it can be represented as
˜︁mt+1 = ˜︁mt + κ(Xt, Wt+1),
where κ : Rn × Rk →R is a measurable function. Define the unconditional expectation of
the increment ˜︁mt+1 −˜︁mt to be ν = E[κ(Xt, Wt+1)]. Define κ(x) = E[κ(Xt, Wt+1)|Xt = x] −ν
to be the deviation of the expected increment conditional on Xt = x from its unconditional
mean. Using the infinite sum of all such future deviations as of t, define
Ht = κ(Xt−1, Wt) −ν
⏞
⏟⏟
⏞
( ˜︁mt−˜︁mt−1)−ν
+
∞
∑︂
j=0
Et[κ(Xt+j)],
(A.2)
and assume that the sum in (A.2) converges in mean square to a finite variable. Next, define
h(Xt) = Et[Ht+1] =
∞
∑︂
j=0
Et[κ(Xt+j)].
(A.3)
33See also Hansen (2019).
34The first setting is a generalization of the first part of Case I, allowing for arbitrary Markov dynamics
(rather than the specialized version with conditionally i.i.d. dynamics in Section 2.2) along with unanticipated
breaks.
2


---

Finally, define the martingale increment
εt+1 = Ht+1 −h(Xt),
(A.4)
so that Et[εt+1] = 0 by construction.
Given the above setup and the additional assumption that E[κ(Xt, Wt+1)2] < ∞, Propo-
sition 4.2.1 of Hansen and Sargent (2022) then gives that mt+1 = ˜︁mt+1 −˜︁mt satisfies the
following additive decomposition:35
mt+1 = ν + h(Xt) −h(Xt+1) + εt+1.
(A.5)
The first term represents the linear trend in ˜︁mt. The second component, h(Xt) −h(Xt+1), is
a stationary difference. The last term is a mean-zero martingale increment.
We now map to our interpretation of the first term as representing discounting and the
second term as depending on cash-flow growth. Denote the log cash-flow process by ct, and
assume that
ct+1 −ct = µc(Xt) + σc(Xt)BcWt+1,
Xt+1 = AxXt + σx(Xt)BxWt+1,
(A.6)
where µc(Xt), σc(Xt), and σx(Xt) are measurable functions. This nests many common
specifications for fundamentals. If (i) Wt is a 3 × 1 i.i.d. standard normal vector, where
the first entry contains a shock to contemporaneous cash flows (so only the first entry of
the row vector Bc is non-zero), (ii) Xt is a 2 × 1 vector, where the first entry X1,t affects
expected cash-flow growth (µc(Xt) = µ + X1,t), the second captures stochastic volatility
(σc(Xt) = σx(Xt) =
√︁
σ2 + X2,t), Ax is diagonal, and Bx = (02×1 ˜︁Bx) for a 2 × 2 diagonal ˜︁Bx,
then this represents the long-run risks model of Bansal and Yaron (2004) with stochastic
volatility. The Campbell and Cochrane (1999) habit formation model, meanwhile, applies if
Wt is scalar i.i.d. standard normal, µc(Xt) = µ, σc(Xt) = σ, Bc = 1, and Xt is the deviation
of the log surplus consumption ratio ˜︁st from its long-run mean (with σx(Xt) being Campbell
and Cochrane’s “sensitivity function” λ(˜︁st)). Other settings fit similarly within the framework.
To relate the SDF dynamics to cash flows, assume that the log SDF can be written as
mt+1 = −ρ −˜︁γ(ct+1 −ct) + nt+1,
(A.7)
35Theorem 3.2 of Hansen (2012) gives an exactly analogous decomposition in continuous time, with the
added interpretation of h as a finite-second-moment solution to limt↘0 1
t E0[h(Xt) −h(x)|X0 = x] = −κ(x),
where κ(x) is the deviation of the local mean of the increment in ˜︁m from its unconditional mean ν.
3


---

for some constant ˜︁γ and process nt+1 = µn(Xt)+σn(Xt)BnWt+1. This is again quite general.36
As in Section 2.1, it holds in a representative-agent, power-utility setting, where ρ = −log β
is the time discount rate, ˜︁γ = γ is relative risk aversion, and nt+1 = 0. If the representative
agent has Epstein-Zin preferences with elasticity of intertemporal substitution (EIS) ψ,
time discount rate ρ, and relative risk aversion γ, (A.7) holds, but now with ˜︁γ =
1
ψ and
nt+1 = (1/ψ −γ)(vt+1 −(1 −γ)−1 log Et[V 1−γ
t+1 ]), where Vt+1 is continuation utility and vt+1 is
its log.37 In the Campbell and Cochrane (1999) habit setting, (A.7) holds, with ˜︁γ = γ again
representing risk aversion and nt+1 = −γ(˜︁st+1 −˜︁st), where ˜︁st is the log surplus consumption
ratio. It can also be mapped straightforwardly to various heterogeneous-agent models, such
as that of Constantinides and Duffie (1996) or subsequent models.
To relate the above representation to the additive decomposition (A.5), we can construct
each of the terms in that decomposition under our assumptions on cash flows in (A.6) and the
SDF in (A.7). Define νc = E[ct+1−ct] = E[µc(Xt)] and νn = E[nt+1] = E[µn(Xt)], and assume
that νn = 0. This will hold as long as the additional perturbation nt+1 to the log SDF either
(i) follows a martingale difference sequence or (ii) features transitory, unconditional-mean-zero
disturbances, as is the case in many models.38 The ν in (A.5) is therefore
ν = −ρ −˜︁γνc.
(A.8)
Similarly, split κ(Xt) into two parts, κ(Xt) = κc(Xt)+κn(Xt), where κc(Xt) = −˜︁γµc(Xt)+˜︁γνc
and κn(Xt) = µn(Xt). Build up hc(Xt) and hn(Xt) accordingly from these κ functions as
in (A.3), and h(Xt) = hc(Xt) + hn(Xt). The εt+1 term inherits the remaining martingale-
difference components of −˜︁γ(ct+1 −ct) and nt+1, as in (A.4).39 Define these two processes’
respective martingale increment terms as εc,t+1 and εn,t+1. Finally, define the martingale
difference ˜︁εt+1 = εt+1 −εc,t+1 = εn,t+1.
To map the above steps and results to the decomposition in (2), we construct an expanded
state vector ˜︁
Xt = (ct, Xt)′, where Xt is the previous state vector. This expanded state vector
still follows a Markov process. With non-zero average consumption growth, ˜︁
Xt will no longer
be stationary, but its differences will be. This expanded state vector will stand in for the
36It is slightly more general, for example, than the assumption in Backus, Chernov, and Zin (2014, eq. (22)).
37In the unit EIS case with ψ = 1, Nt+1 = exp(nt+1) is a martingale, but nt+1 is typically not.
38This holds in, for example, the Campbell and Cochrane (1999) model, and see Borovička, Hansen, and
Scheinkman (2016) for further discussion. If it does not hold, then the ρ in our decomposition should be
understood to contain both the time discount rate and any small component arising from E[nt+1] (e.g.,
from a Jensen’s inequality correction for the continuation utility term in an Epstein–Zin framework). See
Appendix A.2 for a discussion of how this affects the r∗
t decomposition in a tractable alternative case.
39See Borovička, Hansen, and Scheinkman (2016) for explicit characterizations of the martingale components
in alternative models.
4


---

state vector used in (2). We can now construct our alternative decomposition. Define
f( ˜︁
Xt+1) −f( ˜︁
Xt) = ˜︁γ(ct+1 −ct) + (hn(Xt+1) −hn(Xt)).
(A.9)
Using (A.5), (A.8), and (A.9), we accordingly have our decomposition
mt+1 = −ρ −(f( ˜︁
Xt+1) −f( ˜︁
Xt)) + ˜︁εt+1,
(A.10)
where f( ˜︁
Xt+1)−f( ˜︁
Xt) is a stationary difference and ˜︁εt+1 is a mean-zero martingale difference,
as in (2). Note that while Et[f( ˜︁
Xt+1) −f( ˜︁
Xt)] does not depend only on cash-flow growth
ct+1 −ct in general, the limiting forward expectation lims→∞Et[f( ˜︁
Xt+s+1) −f( ˜︁
Xt+s)] used in
the trend real-rate decomposition (5) does:
˜︁g∗
t = lim
s→∞Et[f( ˜︁
Xt+s+1) −f( ˜︁
Xt+s)] = ˜︁γE[ct+1 −ct] = ˜︁γνc.
(A.11)
Finally, to complete the characterization of this setting’s decomposition, we now allow for
unanticipated changes in the economic environment. We accordingly denote the transition
distribution describing the Markov process X at date t to be Pt, and assume that this
distribution governs Xt+1 and is expected to govern Xt+1+s for all s > 0. There may then be
an unanticipated change in the transition distribution to Pt+1, at which point this distribution
will govern Xt+2 and will be expected to govern all future Xt+2+s thereafter. Again defining
the expanded state vector ˜︁
Xt = (ct, Xt)′, the stationary (under Pt) difference f( ˜︁
Xt+1)−f( ˜︁
Xt)
in (A.9), and the now potentially time-varying ρt in (A.7), our decomposition (A.10) becomes
mt+1 = −ρt −(f( ˜︁
Xt+1) −f( ˜︁
Xt)) + ˜︁εt+1.
(A.12)
This now aligns with (2), with ˜︁
Xt and ˜︁εt+1 here in place of Xt and εt+1 in the text. The
limiting expectation ˜︁g∗
t as defined in (A.11) may also be time-varying here, as ˜︁g∗
t = ˜︁γtνc,t.
A.1.2
Drifting Steady State
Analogous to the drifting-steady-state form of Case I in Section 2.2, we now consider an
alternative case in which fundamentals (and resulting expected returns and valuation ratios)
follow a random walk, or “drifting steady state.” Define Wt+1 as in Appendix A.1.1, and
assume that the cash-flow process c and one-dimensional process X are modified from (A.6)
to now follow
ct+1 −ct = µc + Xt + σc(Xt)BcWt+1,
Xt+1 = Xt + σx(Xt)BxWt+1.
5


---

The volatility term σx(Xt) may be specified so as to ensure that X remains bounded in L2 in
order to rule out explosive dynamics (or one could assume alternative bounded-martingale
dynamics for X), but we do not impose this directly.40
In place of (A.7), the log SDF follows
mt+1 = −ρt −˜︁γ(ct+1 −ct) + nt+1,
ρt+1 = ρt + BρWt+1,
nt+1 = ηt+1 −ηt,
where Et[ηt+1] = ηt. Defining ˜︁
Xt = (ct, Xt)′, we again immediately obtain a decomposition of
the form (A.12) and (2):
mt+1 = −ρt −(f( ˜︁
Xt+1) −f( ˜︁
Xt)) + ˜︁εt+1,
where f( ˜︁
Xt+1) −f( ˜︁
Xt) = ˜︁γ(ct+1 −ct) = ˜︁γ(µc + Xt + σc(Xt)BcWt+1) is difference-stationary,
and where ˜︁εt+1 = nt+1 is a martingale difference.
A.1.3
Stationarity
Finally, analogous to Case II in Section 2.2, we consider a setting building on Appendix A.1.1,
without unanticipated breaks but with stationary variation in ρt. The stationarity of Xt and
ρt in this setting will imply that infinite-horizon expectations of the discounting and growth
terms are constant. As a result, we discuss how to redefine long-run expectations in a manner
incorporating persistent time variation in these processes.
We start with exactly the same setting as in Appendix A.1.1, with everything through
equation (A.6) unchanged. We modify (A.7) slightly to allow for ρt to follow stationary
Markov dynamics: assume that ρt is an element of the state vector Xt in (A.1) and (A.6),
and
mt+1 = −ρt −˜︁γ(ct+1 −ct) + nt+1,
with the assumptions on the remaining terms in mt+1 unchanged. We also define ρ = E[ρt].
The above time variation in ρ can be thought of as representing a time-varying subjective
discount rate for the representative agent, but it also serves as a stand-in for many other
sources of potential variation in the intertemporal marginal rate of substitution. It may arise
from demographic changes, a heterogeneous-agents model with time variation in the marginal
40Instead, the drifting steady state model is intended as a convenient tool to represent persistent fluctuations
in fundamentals, rather than being a reasonable candidate model over an infinite horizon.
6


---

investor (and differences in investors’ personal discount rates), or as discussed later in the
appendix, capital flows from foreign investors.
We can then follow nearly exactly the same steps as in Appendix A.1.1 to obtain the
following valid decomposition:41
mt+1 = −ρt −(f( ˜︁
Xt+1) −f( ˜︁
Xt)) + ˜︁εt+1,
with f( ˜︁
Xt+1) −f( ˜︁
Xt) defined as in (A.9) and ˜︁εt+1 defined as before (A.9).
In this case, all infinite-horizon expectations defined after the r∗
t decomposition (5) are
constant, with ρ∗
t = lims→∞Et[ρt+s] = ρ, ˜︁g∗
t = lims→∞Et[f( ˜︁
Xt+s+1) −f( ˜︁
Xt+s)] = ˜︁γνc, and
L∗
t,M = lims→∞Et[Lt+s(Mt+s+1)] = ∑︁∞
n=2
κn(mt+1)
n!
, where κn(mt+1) is the nth cumulant of the
unconditional log SDF distribution. To formalize long-horizon variation in the terms in our
r∗
t decomposition in this context, we redefine the above terms as discounted sums:
z∗
t = (1 −δ)
∞
∑︂
s=0
δsEt[zt+s],
(A.13)
zt ∈{ρt, gt+1, Lt(Mt+1), rf
t+1},
where δ ∈(0, 1) is a loglinearization constant and where gt+s+1 ≡f( ˜︁
Xt+s+1) −f( ˜︁
Xt+s). We
define the loglinearization constant δ in the appendix for Section 2.2 below, and we discuss
how the definition (A.13) maps well to the equity yield decomposition in the stationary
case. As (1 −δ) ∑︁∞
s=0 δs = 1, equation (A.13) defines the starred long-run terms as weighted
averages of all future expected realizations of zt, as in (13) in the main text.
A.2
Interest-Rate Decomposition
A.2.1
Benchmark Case
The general version of the decomposition for r∗
t provided in equation (5) in Section 2.1
follows immediately from the SDF decomposition derived and discussed in Appendix A.1,
along with equations (1) and (3). For the consumption-based version in Section 2.1, the
second expression provided in (7) starts from equation (4) and then applies equation (25)
of Backus, Chernov, and Martin (2011), which relates the log SDF’s cumulants to the
41To spell out these steps in further detail: first, with the same definitions and assumptions on νc
and νn as before, the ν in (A.5) becomes ν = −ρ −˜︁γνc. We now split κ(Xt) into three parts, κ(Xt) =
κρ(Xt) + κc(Xt) + κn(Xt), where κc(Xt) and κn(Xt) are as before, and κρ = −µρ(Xt) + ρ. Build up hρ(Xt),
hc(Xt), and hn(Xt) accordingly from these κ functions as in (A.3), and h(Xt) = hρ(Xt) + hc(Xt) + hn(Xt).
The εt+1 term inherits the remaining martingale components of ct+1 −ct and nt+1 as in (A.4), with no
additional term for ρt given its stationary Markov dynamics, so we define ˜︁εt+1 as before. The expanded state
vector is again ˜︁
Xt = (ct, Xt)′. The decomposition thus applies as stated.
7


---

consumption-growth cumulants in a power-utility setting according to
κn,t(mt+1) = (−γ)nκn,t(gt+1).
(A.14)
See also equation (8) and the preceding equation in Martin (2013), which provides the same
interest-rate expression as in (7). Equation (8) then follows directly from the preceding steps.
Again see the previous appendix subsection for details on the definitions of the terms in (5)
and (8) given each of our sets of assumptions on the dynamics of fundamentals.
A.2.2
Extension with Epstein–Zin Preferences
As discussed above equation (A.8) and in detail in footnote 38, if the additional term nt+1
in the log SDF specification (A.7) does not feature E[nt+1] = 0, then the ρ (or ρt) in our
decomposition should be understood to contain both the time discount rate and any small
component arising from E[nt+1]. This does not pose serious issues for either the decompositions
or the paper’s interpretation of ρt: as discussed in Section 3.2, we do not view shifts in ρt in
the data as likely to be arising purely from changes in aggregate patience among domestic
investors. That said, given the use of Epstein–Zin preferences in Section 2.2, we briefly discuss
precisely how such preferences affect the interest-rate decomposition in a tractable case.
In place of (6), we follow Epstein and Zin (1989) and set
Ut =
{︂
(1 −βt)C
1−γ
θ
t
+ βt(Et[U 1−γ
t+1 ])
1
θ
}︂
θ
1−γ ,
where θ ≡(1 −γ)/(1 −1
ψ) and where ψ is the elasticity of intertemporal substitution (EIS).
We again set ρt = −log βt. In a complete-markets setting in which there is a consumption
claim whose value is aggregate wealth, the SDF is
Mt+1 =
(︄
βt
(︃Ct+1
Ct
)︃−1
ψ )︄θ (︁
Rw
t+1
)︁−(1−θ) ,
(A.15)
where Rw
t+1 is the gross return on the wealth portfolio. If we further assume jointly lognormal
and homoskedastic Ct+1 and Rw
t+1, the risk-free rate is then
rf
t+1 = ρt + 1
ψEt[gt+1] −
θ
2ψ2σ2
g −1 −θ
2
σ2
w,
(A.16)
as in Campbell (2018), equation (6.44), where σ2
g = Vart(gt+1) and σ2
w = Vart(rw
t+1). Given
8


---

(A.15), the SDF’s entropy is
Lt(Mt+1) = θ2
2ψ2σ2
g + (1 −θ)2
2
σ2
w + θ(1 −θ)
ψ
σgw,
(A.17)
where σgw = Covt(gt+1, rw
t+1). Combining this with (A.16), we can write
rf
t+1 = ρt + 1
ψEt[gt+1] −Lt(Mt+1) + θ(θ −1)
2
Vart
(︃gt+1
ψ
−rw
t+1
)︃
= ˜ρt + 1
ψEt[gt+1] −Lt(Mt+1),
where ˜ρt = ρt + θ(θ−1)
2
Vart
(︂
gt+1
ψ −rw
t+1
)︂
. As a result, (8) still holds, with ˜ρ∗
t in place of ρ∗
t
and with 1
ψ in place of γ.
The additional term in ˜ρt can be thought of as capturing the variance of the innovation to
the Epstein–Zin certainty equivalent.42 One might thus prefer to group this additional term
with the risk component of the SDF instead of ρt. To obtain this equivalent representation,
note that since Lt(Mt+1) = 1
2Vart
(︂
θgt+1
ψ
−(θ −1)rw
t+1
)︂
from (A.17), we can write
rf
t+1 = ρt + 1
ψEt[gt+1] −(1 + ω)Lt(Mt+1),
where
ω ≡
θ(1 −θ)Vart
(︂
gt+1
ψ −rw
t+1
)︂
Vart
(︂
θgt+1
ψ
−(θ −1)rw
t+1
)︂
is a constant given the homoskedastic setting. Given that our empirical estimation allows for a
flexible loading of the risk-free rate on our SDF entropy proxy, this constant of proportionality
1 + ω will be incorporated in the empirical versions of the decompositions in such a setting.
As an alternative to the assumption of lognormality after (A.15), assume that gt+1 is i.i.d.,
in which case the log SDF becomes mt+1 = −ρt −γgt+1, exactly as in the benchmark case in
the consumption-based version in Section 2.1, so the previous decomposition applies.
A.3
Results for Equity Yields and Duration
Following the main text (and similar to Appendix A.1), we derive our results for equity yields
in two settings. We then discuss how the implications for equity duration follow directly,
prove the stated results for non-parallel discounting shifts, and discuss our empirical entropy
proxy.
42We thank Mike Chernov for helpful discussion related to this point.
9


---

A.3.1
Case I (Gordon Growth)
Equity Yields and Risk Premia. Given i.i.d. consumption growth gt+1 = ct+1 −ct and
dt+1 −dt = λgt+1, the setting here mirrors that of Martin (2013, Section 1). He works with a
risk premium defined slightly differently than ours: while we use the expected log return and
set rpt ≡Et[rmkt
t+1] −rf
t+1, he instead uses the log expected return and considers what we will
define as ˜︁rpt ≡log Et[Rmkt
t+1] −rf
t+1. By definition of entropy, these two risk premia differ by
˜︁rpt −rpt = Lt(Rmkt
t+1) =
∞
∑︂
n=2
λnκn,t(gt+1)
n!
,
(A.18)
where the second equality uses that rmkt
t+1 = λgt+1 + constant (where the constant is in fact
ey) in this i.i.d. setting, and then applies the same relation as in (A.14).
Result 1 of Martin (2013), and in particular equation (7), gives that
ey∗
t = r∗
t + ˜︁rp∗
t −
∞
∑︂
n=1
λnκn,t(gt+1)
n!
,
(A.19)
where we note that the summation in the last term starts with the first cumulant (n = 1) rather
than the second as in (A.18). This last term is therefore equal to the cumulant-generating
function (CGF) for consumption growth,
c(ϑ) ≡
∞
∑︂
n=1
ϑnκn,t(gt+1)
n!
,
(A.20)
evaluated at ϑ = λ. Using (A.18) and (A.19), we have that
ey∗
t = r∗
t + rp∗
t −λg∗
t ,
(A.21)
as stated in equation (10) and Result 1.
For the risk-premium expressions in (11), we start from equation (5) of Martin (2013),
which gives that ˜︁rp∗
t = c(λ) + c(−γ) −c(λ −γ), and solve for rp∗
t using (A.18):
rp∗
t = ˜︁rp∗
t −(c(λ) −λg∗
t )
= λg∗
t + c(−γ) −c(λ −γ)
=
∞
∑︂
n=2
(−γ)nκn,t(gt+1)
n!
−
∞
∑︂
n=2
(λ −γ)nκn,t(gt+1)
n!
= Lt(Mt+1) −Lt(Mt+1Rmkt
t+1).
(A.22)
10


---

The first line uses the definition of the CGF in (A.18); the second substitutes in the ˜︁rp∗
t
solution above; the third expands the CGFs and uses that the first moments cancel; and the
last uses that mt+1 + rmkt
t+1 = constant + (λ −γ)gt+1 and applies (A.14). (See also Backus,
Chernov, and Martin 2011, p. 2008, for similar steps.) Both lines of (11) follow directly.
To see that rpt = Lt(Mt+1) −Lt(Mt+1Rmkt
t+1) holds in any no-arbitrage setting, one can
follow Backus, Boyarchenko, and Chernov (2018, p. 12): take logs of the pricing equation
Et[Mt+1Rmkt
t+1] = 1 and use the definition of entropy and equation (1) to obtain
0 = log Et[Mt+1Rmkt
t+1] = Et[mt+1 + rmkt
t+1] + Lt(Mt+1Rmkt
t+1)
= Et[rmkt
t+1] −rf
t+1 −Lt(Mt+1) + Lt(Mt+1Rmkt
t+1).
Rearranging gives that rpt = Lt(Mt+1) −Lt(Mt+1Rmkt
t+1), as stated.
Using (A.21) and (A.22), along with the interest-rate decomposition derived in the previous
appendix sections, Result 1 then follows. We note as well that equations (5) and (7) of Martin
(2013) also hold with Epstein–Zin utility, so (A.21) and (A.22) are identical in this case, as
stated on page 10.
Risk Shocks. In part (iii) of Result 1, it is stated that equity yields change by −∂rp∗
t
∂L∗
t,M + 1
per unit increase in r∗
t if
∂rp∗
t
∂L∗
t,M is well-defined. The third line of (A.22) shows the need for
this qualification: L∗
t,M and rp∗
t are both functions of the consumption growth cumulants
κn,t(gt+1), and there are many potential changes to the different cumulants that generate
identical changes in Lt(Mt+1) but different effects on rp∗
t.43 In certain settings, though, this
partial derivative is well-defined. One such setting is when γ = λ: in this case, rp∗
t = L∗
t,M,
so
∂rp∗
t
∂L∗
t,M = 1.
Case (i) of the three bond–stock comovement cases described on page 13 is another such
setting. This case assumes lognormal growth, so that κn,t(gt+1) = 0 for n > 2. We therefore
have that rp∗
t = 1
2λ(2γ −λ)Vart(gt+1) = λ(2γ−λ)
γ2
L∗
t,M, so
−∂rp∗
t
∂L∗
t,M
+ 1 = −λ(2γ −λ)
γ2
+ 1 = (λ −γ)2
γ2
,
which is strictly positive if λ̸ = γ. In a lognormal, power-utility setting, the discount-rate
effect of an increase in volatility always dominates, so equity prices increase given an increase
in volatility as considered here. But the pass-through of interest rates to equity yields (i.e.,
43This motivates our consideration of the average change using the beta of the risk premium with L∗
t,M,
where we use that Cov(rp∗
t −L∗
t,M, L∗
t,M) = Cov(rp∗
t , L∗
t,M) −Var(L∗
t,M). When the partial derivative does
not exist, one can take
∂rp∗
t
∂L∗
t,M to represent a stand-in for βL.
11


---

−∂rp∗
t
∂L∗
t,M + 1 above) is nonetheless strictly below one as long as (λ −γ)2 < γ2, or equivalently
2γ > λ, as stated in the text.
We now consider the other two cases introduced on page 13. Case (ii) is based on the
rare-disasters model of Barro (2006). Consumption growth is modeled as gt+1 = g1,t+1 +g2,t+1,
where the two components g1,t+1 and g2,t+1 are independent of each other and independent
over time. The first component is normal with Et[g1,t+1] = g∗
1 and variance σ2. The second
component is a jump component, and we follow Backus, Chernov, and Martin (2011) and
assume that it follows a Poisson-normal mixture: a given period has j ∈N jumps with
probability e−ωωj/j! (so ω is the effective jump intensity), and conditional on j, the jump
size is normal with mean −jm (with m > 0) and variance js2. This implies (see p. 2002 of
Backus, Chernov, and Martin) that the consumption-growth CGF is
c(ϑ) = ϑg∗
1 + 1
2ϑ2σ2 + ω
(︂
e−ϑm+ 1
2 ϑ2s2 −1
)︂
.
Given that Lt(exp(ϑgt+1)) = c(ϑ) −ϑEt[gt+1] and that in this setting Et[gt+1] = g∗
1 −ωm, we
have that
L∗
t,MR = Lt(exp((λ −γ)gt+1)) = c(λ −γ) −(λ −γ)(g∗
1 −ωm)
= (λ −γ)ωm + 1
2(λ −γ)2σ2 + ω
(︂
e−(λ−γ)m+ 1
2 (λ−γ)2s2 −1
)︂
.
Using this,
ey∗
t = ρ∗
t + (γ −λ)g∗
t −L∗
t,MR
= ρ∗
t + (γ −λ)g∗
1 −1
2(λ −γ)2σ2 −ω
(︂
e−(λ−γ)m+ 1
2 (λ−γ)2s2 −1
)︂
.
Given a change in the average disaster size m, we therefore have
∂ey∗
t
∂m = (λ −γ) ω e−(λ−γ)m+ 1
2 (λ−γ)2s2
This is strictly positive (so valuations go down given an increase in mean disaster size) iff
λ > γ.
Meanwhile, following similar steps for the SDF’s entropy and plugging into the risk-free
rate decomposition,
r∗
t = ρ∗
t + γg∗
1 −1
2γ2σ2 −ω
(︂
eγm+ 1
2 γ2s2 −1
)︂
.
12


---

As a result,
∂r∗
t
∂m = −γ ω eγm+ 1
2 γ2s2 < 0,
so r∗
t strictly decreases given an increase in mean disaster size. We conclude that such changes
induce negative comovement between equity yields and real rates as long as γ < λ.
More generally, for any change in higher (n ⩾2) moments κn,t(gt+1) for n odd, if λ > γ,
∂L∗
t,M
∂κn,t(gt+1) = (−γ)n
n!
< 0,
∂L∗
t,MR
∂κn,t(gt+1) = (λ −γ)n
n!
> 0.
Thus, greater negative skewness (i.e., a decrease in κ3,t) will increase the SDF’s entropy L∗
t,M
but decrease the entropy of the discounted return L∗
t,MR, and similarly for other higher odd
cumulants. Since the risk-free rate decreases in L∗
t,M and the equity yield decreases in L∗
t,MR,
these odd-higher-moment shocks will induce negative comovement in the γ < λ case.
For case (iii) on page 13, with Epstein–Zin utility (and parameters as defined in Ap-
pendix A.2.2), using equations (4)–(5) in Martin (2013) and considering a consumption claim
(λ = 1), we can write
r∗
t = ρ∗
t +
∞
∑︂
n=1
κn,t(gt+1)
n!
((1 −1/θ)(1 −γ)n −(−γ)n)
ey∗
t = ρ∗
t +
∞
∑︂
n=1
κn,t(gt+1)
n!
(−(1 −γ)n/θ) .
So considering any change in higher (n ⩾2) moments κn,t(gt+1) for n even, we can use the
assumptions ψ > 1, γ > 1, and plug in for θ (and use θ < 0 with those assumptions) to get
∂r∗
t
∂κn,t(gt+1) = 1
n!
[︃(︃1
ψ −γ
)︃
(1 −γ)n−1 −(−γ)n
]︃
< 0,
∂ey∗
t
∂κn,t(gt+1) = 1
n! (−(1 −γ)n/θ) > 0,
so equity yields and risk-free rates move in opposite directions, as stated.
Drifting Steady State. We now generalize to the case with arbitrary permanent shocks.
If Et[eyt+1] = eyt ≡ey∗
t (and all underlying fundamentals similarly are martingales), we
can follow Gao and Martin (2021, eq (12)–(14)): since Rmkt
t+1 = Dt+1+Pt+1
Pt
, taking logs and
13


---

expectations yields
ey∗
t = Et[rmkt
t+1] −λEt[gt+1] −log
(︁
1 −e−eyt)︁
+ Et
[︁
log
(︁
1 −e−eyt+1)︁]︁
.
To a first order for eyt+1 around its expectation eyt, the last two terms cancel, giving
equation (12) as stated.
Given that r∗
t satisfies the same decomposition (as shown in
Appendix A.1.2), Result 1 therefore holds as stated.
A.3.2
Case II (Stationarity)
In this case, we apply Result 2 of Gao and Martin (2021) directly to obtain that to a first
order around the unconditional expectation ey ≡E[eyt],
ey∗
t ≡eyt = (1 −δ)
∞
∑︂
s=0
δsEt[rmkt
t+s+1 −λgt+s+1],
(A.23)
where δ ≡e−ey. Therefore, defining rp∗
t (and its underlying components) and g∗
t as in
(13), and using the definition for r∗
t and its underlying components from (A.13), the stated
decomposition follows. So given the decomposition for r∗
t as shown in Appendix A.1.3,
Result 1 again holds as stated.
A.3.3
Equity Duration
The equity duration implications in Section 2.3 for the most part follow from direct application
of the previous expressions. For equation (15), we use that Et[Dt+s] = Dtesλg∗and then
evaluate the resulting series. The remaining derivatives in (16) and Result 2 then follow
directly from (14)–(15).
A.3.4
Non-Parallel Discounting Shifts
We now prove Result 3 and additional results described in Section 2.4. As in that subsection,
we start at a flat steady state (as would arise in the conditionally i.i.d. setting in Case I)
for pure discount rates, growth, and risk, and we denote ρ∗(s) ≡Et[ρt+s−1]. Define ¯ρ∗(s) ≡
1
s
∑︁s
u=1 ρ∗(u) for the average one-period pure discount rate out to horizon s, and again define
δ ≡e−ey∗, which is equivalent to the loglinearization constant used in (A.23). Given this
definition, D = 1/(1 −δ) and δ = 1 −1/D by (15). We also make repeated use of the
geometric sums ∑︁
s⩾1 δs−1 =
1
1−δ, ∑︁
s⩾1 s δs−1 =
1
(1−δ)2, and ∑︁
s⩾1 s2δs−1 =
1+δ
(1−δ)3.
Compounding the one-period log SDF, and taking future pure discount rates for now at
14


---

their conditional means ρ∗(u),44
Mt,t+s = exp
(︄
s
∑︂
u=1
−(ρ∗(u) + γgt+u)
)︄
.
Further, the price of the s-period dividend strip is
Ps ≡Et[Mt,t+sDt+s] = Dt e−∑︁s
u=1 ρ∗(u) Et
[︄
exp
(︄
(λ −γ)
s
∑︂
u=1
gt+u
)︄]︄
= Dt e−s¯ρ∗(s)+s c(λ−γ),
where c(·) is the CGF defined in (A.20), and where the last equality uses that at the flat
steady state, the growth and risk contribution is the same at every horizon. The s-period
equity yield, defined by Ps = Dt e−s ey∗(s), is then ey∗(s) = ¯ρ∗(s) −c(λ −γ). Similarly, for
the s-period real bond, Et[Mt,t+s] = e−s¯ρ∗(s)+s c(−γ), so its yield is r∗(s) = ¯ρ∗(s) −c(−γ).
Substituting c(−γ) = −γg∗+ L∗
M from (7), and c(λ −γ) = (λ −γ)g∗+ L∗
MR from (A.22),
then gives
r∗(s) = ¯ρ∗(s) + γg∗−L∗
M,
ey∗(s) = ¯ρ∗(s) + (γ −λ)g∗−L∗
MR.
(A.24)
This is the maturity-specific version of Result 1. Holding growth and risk fixed, a change
d¯ρ∗(s) in the average forward discount rate out to horizon s passes one-for-one into both the
s-period real bond yield and the s-period strip yield, at every horizon.
At the flat steady state, ¯ρ∗(s) = ρ∗and ey∗(s) = ey∗for all s, so Ps/Dt = δs and
P/Dt = ∑︁
s δs =
1
eey∗−1, as in (14). The strip value weights are then
ws ≡Ps
P = (eey∗−1) e−s ey∗= (1 −δ) δs−1,
as stated in the text. These weights generate a mean strip-weighted horizon of ∑︁
s s ws = D,
consistent with (15) and as stated in the text, and the strip-weighted horizon variance is
Varw(s) = ∑︁
s s2ws −D2 =
δ
(1−δ)2 = D(D −1). We can now prove the three stated parts of
44We do not require ρt+u−1 = ρ∗(u) ex post, but the current proof conducts a perturbation for which this is
without loss of generality. Formally, for a deterministic sequence ζu, we define a perturbed economy in which
the one-period pure discount rate applying to the period ending at t + u is shifted in every state by εζu, while
the conditional distribution of growth and all other SDF terms is unchanged. Taking the Gâteaux derivative
at ε = 0 with ζu = dρ∗(u), the perturbed strip price at horizon s′ satisfies Ps′(ε) = Ps′(0) exp(−ε ∑︁
u⩽s′ ζu).
Thus d log P = −∑︁
u Wuζu, where Wu ≡∑︁
s′⩾u Ps′/P is the share of total equity value for cash flows at
maturities u and beyond. Since the increment ζu is deterministic, this holds regardless of the distribution of
ρt+u−1 or its correlation with growth. In other words, setting pure discount rates at their conditional means
in the SDF affects the baseline SDF but not the response of strip prices or equity.
15


---

the result in turn.
General Shift. Consider a shift {dρ∗(s)} of the forward pure discounting curve. Writ-
ing log P = log Dt + log ∑︁
s⩾1 exp(−s¯ρ∗(s) + s c(λ −γ)), the forward rate ρ∗(s) enters the
exponent of Ps′ with coefficient −1 exactly when s′ ⩾s, so
∂log P
∂ρ∗(s) = −
∑︁
s′⩾s Ps′
P
≡−Ws,
where Ws is the share of market value for cash flows at horizons s and beyond. To first order,
the shift moves the price by d log P = −∑︁
s⩾1 Ws dρ∗(s).45 Summing by parts,
∑︂
s⩾1
Ws = 1
P
∑︂
s′⩾1
s′ Ps′ =
∑︂
s′
s′ ws′ = D,
which is equal to the value-weighted mean maturity. Further, at the flat baseline, we have
that Ws = ∑︁
s′⩾s(1 −δ)δs′−1 = δs−1, so Ws/D = (1 −δ)δs−1 = ws coincides with the strip
value weight itself. The price response to an arbitrary shift is therefore
d log P = −D
∑︂
s
ws dρ∗(s).
The equity-yield response follows from (9). Since ey = log(P + Dt) −log P and Dt is
unchanged by a shift in the discounting curve, d ey = −
Dt
P+Dt d log P = −1
D d log P, using
Dt
P+Dt = 1 −e−ey∗= 1/D at the steady state. Combining the two,
d ey∗=
∑︂
s
ws dρ∗(s),
d log P = −D d ey∗,
which give (17) as stated. This proves part (i).
Affine Shift and the Relevant Horizon. For an affine shift dρ∗(s) = a + bs, the horizon-
weighted average shift is ∑︁
s ws dρ∗(s) = a + b ∑︁
s s ws = a + bD = dρ∗(D), equal to the
shift evaluated at the (potentially non-integer) horizon s = D. So d ey∗= dρ∗(D) and
d log P = −D dρ∗(D), which together give (18) as stated, and the relevant horizon is equity
duration. This proves part (ii).
To see how the affine shift first-order approximates a general shift (as in footnote 11), we
45This is the directional derivative in the direction of the shift. We assume that the derivative is well
defined (as would be the case, for instance, for a shift of at most polynomial growth in s, in which case Ws
decays geometrically). We read the affine shifts considered below as this derivative, or equivalently as a shift
that is affine out to a horizon H ≫D and bounded beyond.
16


---

can Taylor expand dρ∗(s) around the mean horizon s = D:
dρ∗(s) = dρ∗(D) + dρ∗′(D) (s −D) + 1
2 dρ∗′′(D) (s −D)2 + · · ·
Taking the strip-weighted average and using ∑︁
s ws = 1, ∑︁
s ws(s −D) = 0 (the weights have
mean D), and ∑︁
s ws(s −D)2 = Varw(s) = D(D −1),
∑︂
s
ws dρ∗(s) = dρ∗(D) + 1
2 dρ∗′′(D) D(D −1) + · · ·
The linear term is equal to zero in general, because the weights again have mean D. An affine
shift (dρ∗′′ = 0) then gives ∑︁
s ws dρ∗(s) = dρ∗(D) exactly, while a general shift has second-
and higher-order terms.
Parallel Shift. If dρ∗(s) = dρ∗for all s, then ∑︁
s ws dρ∗= dρ∗. Thus d ey∗= dρ∗and
d log P = −D dρ∗, and d¯ρ∗(s) = dr∗(s) = dρ∗at every horizon by (A.24). Every horizon is
then equally relevant, and the response recovers Result 1(i) and Result 2(i). This proves
part (iii).
Other Rate Measures. The strip value weights also allow us to characterize the response of
equity to changes in other (potentially composite) measures of pure discount rates, including
those discussed in the text. Since W1 = 1, a shift in the one-period pure discount rate alone
moves log P by its own size rather than by D times it, so the pass-through to the equity yield is
w1 = 1/D. A shift in horizons s ⩽k has total weight 1−δk. For the multi-period forwards we
use in the data, the forward rate averaged over periods m to n, ¯ρ∗(m, n) ≡
1
n−m+1
∑︁n
s=m ρ∗(s),
moves under an affine shift by a + b m+n
2 , which equals a + bD = dρ∗(D) if and only if
its midpoint satisfies
m+n
2
= D, as stated in Section 2.4. More generally, any measure
dM = ∑︁
s qs dρ∗(s) with ∑︁
s qs = 1 reproduces the response under affine shifts if and only if
its mean horizon ∑︁
s qs s equals D.
A.3.5
Empirical Entropy Proxy
As stated in Section 3 (see page 19), if the market is growth-optimal and the distribution of
log growth is symmetric, then L∗
t,M,j = L∗
t,R,j. To see this, note from (A.14) and (A.18) that
κn,t(mt+1) = (−γ)nκn,t(gt+1),
κn,t(rmkt
t+1) = λnκn,t(gt+1).
Growth optimality requires λ = γ, and a symmetric log growth distribution implies that
κn,t(gt+1) = 0 for all odd n (aside from n = 1, which does not enter into the entropy sum).
17


---

And for even n, given γ = λ, we have (−γ)n = λn. As a result, κn,t(mt+1) = κn,t(rmkt
t+1) for
all n, and so L∗
t,M,j = L∗
t,R,j, as stated. This (along with Martin 2017, Result 3) motivates
our use of the squared VIX to proxy for the SDF entropy term L∗
t,M in estimating our r∗
t
decomposition.46
B.
Additional Empirical Details and Results
This appendix provides additional measurement details and empirical results as referenced in
the main text.
B.1
Baseline Measurement Details
Section 3.1 explains most of our data sources and variable definitions for the baseline analysis.
Here, we provide additional details on two aspects of the data mentioned in the text.
VIX Measurement. The squared VIX is defined for horizon T −t as
VIX2
t,T = 2Rf
t,T
T −t
(︂∫︂Ft,T
0
putt,T(K)
K2
dK +
∫︂∞
Ft,T
callt,T(K)
K2
dK
)︂
,
where Ft,T is the forward price and putt,T(K) and callt,T(K) are prices of European put and
call options with strike K expiring at T. To implement this formula, we use a cleaned version
of a global panel of index option prices from OptionMetrics. As in the main text, the sample,
data filters, and implementation approach are taken from Gandhi, Gormsen, and Lazarus
(2025); see that paper for full details.
Our options data are available starting in 1990 in the U.S. sample, but the samples for
other countries start between 2002 and 2006. To obtain a full sample corresponding to
the forecast data, we project VIX2
t,j in the available sample onto realized volatility in the
country j index return, and then obtain predicted values ˆ︃
VIX
2
t,j using the observed volatility
for any dates in the sample for which we cannot calculate VIX directly.
Equity Yields and Data Availability. As in the text, the equity yield eyt,j is measured by
starting with the five-year earnings-to-price ratio Et−4,t,j/Pt,j = [(Et−4,j + . . . + Et,j)/5]/Pt,j,
where earnings and prices are calculated on a value-weighted basis for all available traded
stocks in the country. Earnings Et,j are defined as net income for the full calendar year
corresponding to date t, while prices Pt,j are end-of-period aggregate market capitalizations.
46Martin’s result is for risk-neutral entropy, so this proxy additionally requires an assumption of a constant
entropy risk premium (or, in the log-normal case, variance risk premium) over the sample. This is likely a
reasonable approximation for the full-sample differences considered in the secular trends analysis, though it
likely induces further measurement error for the higher-frequency analyses.
18


---

We then scale this Et−4,t,j/Pt,j by 0.5, very close to the unconditional average payout ratio of
0.494 in our post-1990 sample, to obtain our final measure of equity yields eyt,j. Algebraically,
ey ≡log(1 + D/P) ≈D/P = (D/E) × (E/P). Our unconditional average payout ratio is
calculated as the average ratio of five-year-average common dividends to five-year-average
net income, to put the dividend and earnings figures in common terms, and the average is
across all years and G7 countries starting in 1990.
In some countries, the share of publicly traded companies with available earnings data
is low in the early part of our sample. We drop any country–year equity yield observations
with such coverage issues. The resulting samples start in 1990 for the U.S. and Canada;
1992 for the U.K.; 1993 for Japan; 1994 for France and Germany; and 1998 for Italy. Any
estimated relationship between changes in earnings yields and changes in interest rates uses
a country-specific start date consistent with the beginning of this equity yield sample; for
example, the r∗difference for Italy in Figure 3 is the difference starting from 1998, consistent
with the difference calculated for its equity yields. While all our analyses use data through
2023, the need for full-year net income data to calculate eyt,j, along with the fact that our
data is only available through part of 2023, means that we measure equity yields through the
end of 2022. In all cases where we calculate full-sample differences in the real rate (and its
components), we again match this full-sample difference with the actual available sample
for our equity data. (Any analysis focusing solely on the real-rate data — for example, the
first-stage regression in Table 1 — uses all the data through 2023.)
B.2
Details on Block Bootstrap Inference
For the top panel of Table 3 in Section 4.1, we compute standard errors and confidence intervals
using a block bootstrap that clusters at the year level. We draw years with replacement
from the original sample, and for each bootstrap replication, we then construct a resampled
panel by including all country-quarter observations from each drawn year. We then run
the first-stage regression (19) using the specification in column (3) of Table 1 and obtain
the estimated pure discounting observations as in (20). Given these ˆ︁ρ∗
t,j values and the
resampled equity yields, we then collapse to the first and last available observation by country
to calculate full-sample differences and run the regression in the top panel of Table 3.
This last step is conducted in a manner that accounts for the pronounced trends in
our sample. In particular, before collapsing to the first and last observation by country to
calculate full-sample differences, we sort the resampled data so that the temporal ordering of
the years is preserved from the original sample. Specifically, if the bootstrap draw selects
years {t1, t2, . . . , tT} from the original sample (where t1 ⩽t2 ⩽. . . ⩽tT), we label these as
{1990, 1991, . . . , 1990 + T −1} in the resampled data (where T = 34). This means that early
19


---

observations in the bootstrap sample are drawn from years that appeared early in the original
sample, and late observations are drawn from years that appeared late in the original sample.
So when collapsing the data to the first observation in the year labeled 1990 and the last
observation in the year labeled 1990 + T −1, we preserve the nonstationarity of the original
data (i.e., the pronounced change from beginning to end), while nonetheless allowing the
possibility of moderate (local) changes in the start and end date.47
This approach implements a form of the local block bootstrap proposed and analyzed by
Paparoditis and Politis (2002) and Dowla, Paparoditis, and Politis (2013) for inference with
non-stationary time series. The classic block bootstrap assumes stationarity, which is violated
in our setting.48 The local block bootstrap instead ensures that resampled observations for
each time period are drawn from a local window around that period in the original sample,
preserving any local dependence structure and accommodating slowly varying distributions.
We use 10,000 bootstrap replications for all reported standard errors and significance
tests. Statistical significance is determined by inverting basic bootstrap confidence intervals,
computed as (2ˆ︁β −β∗
1−α/2, 2ˆ︁β −β∗
α/2), where ˆ︁β is the full-sample point estimate and β∗
x denotes
the x percentile of the bootstrap distribution.
B.3
Robustness Measures
This section describes the alternative input data used in Section 4 in more detail:
• Survey of Professional Forecasters (SPF): We obtain mean responses for three
SPF forecast variables via the Federal Reserve Bank of Philadelphia’s website: the
average annual 10-year nominal Treasury yield over the next 10 years, average CPI
inflation over the next 10 years, and average real GDP growth over the next 10 years.
These forecasts are provided once per year in the first quarter of each year. We calculate
the forecasted average real yield by subtracting the CPI forecast from the Treasury
yield forecast, and we use this as our alternative measure of r∗. We use the GDP
forecast as our alternative measure of g∗. These forecasts are only available starting
in 1992; to align the available sample with our main analysis, we run regressions of
the SPF variables on the corresponding variable from the baseline Consensus data and
47For example, if the first year in the resampled data set is 1992, then the full-sample change will be
calculated starting from 1992. In our setting, 99.8% of replications begin and end within the first and last
five years of the original sample, respectively. The order-preserving feature of this bootstrap helps explain the
strong statistical significance in the main regression despite the small apparent sample size of 7 countries: we
in fact have many observations per country with which to estimate the pure discount rate, and its behavior
from the start to the end of the sample is quite robust.
48This violation does not affect inference in cases where the ordering of the data does not matter. So for
the bootstrapped standard errors reported in Section 3 (for which the regressions are invariant to the data
ordering), we use this standard block bootstrap.
20


---

calculate the fitted values, which we use for the 1990 and 1991 observations.
• Del Negro et al. (2019): For this alternative short-term r∗measure, we use the
baseline cross-country natural-rate estimates provided by Del Negro et al. (2019). These
are model-based estimates of the trend short-term real rate, provided as an annual
panel that runs through 2019. To extend the U.S. series to the end of our sample to
calculate the full-sample change in ρ∗, we project the Del Negro et al.–based ρ∗onto
the baseline ρ∗, then use the fitted value for the post-2019 observations.
• GARCH(1,1): For each country, we fit a GARCH(1,1) model to their daily equity
returns data, and we use this to forecast variance at the six-month horizon. We then use
this in place of VIX2 in the interest-rate decomposition. Results are also quantitatively
nearly identical when using the GARCH variance forecast in addition to the VIX in
the decomposition, rather than as a replacement.
• Baker, Bloom, and Davis (2016) Uncertainty Index: We obtain the country-level
economic policy uncertainty series from https://www.policyuncertainty.com for the
set of available countries in our sample, and we use these data in place of VIX2 in the
interest-rate decomposition. Results are again quantitatively nearly identical when
using the uncertainty index in addition to the VIX in the decomposition, rather than
as a replacement.
B.4
Robustness to Time Variation in Profit Shares
This section presents and discusses the robustness results introduced in Section 4.2, first
theoretically and then empirically. For the theoretical results, we first note that our interest-
rate decomposition in Result 1, r∗
t = ρ∗
t + γg∗
t −L∗
t,M, is unchanged, as aggregate growth
gt+1 is the relevant outcome for the SDF. For equity cash flows, denote dividend growth
by gt+1,d = dt+1 −dt. Rather than imposing gt+1,d = λgt+1, we now allow for an arbitrary
dividend growth process. So it may be the case that Corr(g∗
t , g∗
t,d) < 1. Our equity-yield
decomposition now becomes
ey∗
t = ρ∗
t + γg∗
t −g∗
t,d + (rp∗
t −L∗
t,M)
= ρ∗
t + γg∗
t −g∗
t,d −L∗
t,MR.
As before, only shocks to the pure discounting term ρ∗
t pass through directly from rates to
equity yields. And though the pass-through of growth-rate shocks may be different than in
Result 1, it is still the case that such shocks induce weaker pass-through than pure-discounting
21


---

shocks as long as Corr(g∗
t , g∗
t,d) > 0. While there may now be pure dividend-growth shocks
(i.e., changes to g∗
t,d without corresponding changes in g∗
t ), these are entirely separate from
the interest-rate dynamics considered in our empirical decomposition for r∗
t .
For estimating the effect of profit-share changes on valuations empirically, we use two
sources of additional forecast data. First, the long-term Consensus Economics forecast data
provides nominal corporate profit growth forecasts since 1998 for only the U.S. sample. Using
this, we construct a proxy for real g∗
t,d by subtracting the inflation forecast from the nominal
profit-growth forecast for year t + 5. In this available post-1998 U.S. sample,49 profit-growth
forecasts have in fact fallen by meaningfully more than output-growth forecasts:
∆g∗
t = −0.50,
∆g∗
t,d = −1.26.
With a leverage parameter of λ ≈2 — close to the estimated coefficient on expected growth
in the real-rate decomposition in Table 1, consistent with the insignificant equity effect
estimated in Table 2 — we accordingly estimate that the change in the expected profit share
π∗
t ≡g∗
t,d −λg∗
t has been very close to 0 over this sample. As a result, our main conclusions
for the U.S. data are unchanged: profit-share shocks have affected current cash flows but
not expected future growth rates, leaving equity yields close to unaffected. As a result, the
previous estimated effect of the pure discounting residual, and the resulting pass-through of
roughly 1/3 of the decline in r∗
t to equity valuations in U.S. data, remains valid.
As a secondary check on this analysis, we obtain aggregate long-term earnings growth
(LTG) forecasts for U.S. equities from Nagel and Xu (2022). These are analyst forecasts
for earnings growth for U.S. equities, which Nagel and Xu aggregate to the index level and
convert to real terms by subtracting forecasted inflation. Using this series as our second
proxy for g∗
t,d, for the full sample over which we can implement our real-rate decomposition
and measure equity yields, we estimate that ∆g∗
t = −0.70, ∆g∗
t,d = −0.60.50 If one again
assumes a leverage parameter of about λ = 2.5, this implies that there has been a modest
increase in the profit-share term ∆π∗
t , but our main results are largely unaffected.
49This post-1998 sample corresponds to a period during which the majority of the decline in expected
output growth took place in the U.S. forecasts.
50We prefer the Consensus Economics data because the LTG-based forecasts are much more volatile than
the other forecast series (see Bordalo et al. 2024), so the full-sample differences are highly sensitive to the start
and end date. Starting the sample in 1992 instead of 1990 gives ∆g∗
t,d = −1.88; meanwhile, ending the sample
a year later gives ∆g∗
t,d = 0.14. Given such large cyclical LTG forecast variation (σLTG = SD(LTG) = 2.0, vs.
σprofit = 0.8, σGDP = 0.4), we view the baseline forecasts as better capturing low-frequency variation. For
another earnings-growth series, we obtained aggregate annual data on analyst-report-based terminal growth
expectations (typically at a longer horizon than the IBES LTG measure) from Décaire and Guenzel (2025),
and we thank Paul Décaire and Marius Guenzel for sharing their data. In line with the other ∆g∗
t,d proxies,
terminal growth expectations have declined in the U.S. since the early 2000’s (the start of their sample).
22


---

While Greenwald, Lettau, and Ludvigson (2025) differ from us in their focus on profit-
share effects on prices, our results echo some of their findings. They find that “essentially
all of the increase in equity values relative to output from the mid-1990s to the end of the
sample” can be accounted for by assuming a fixed ratio of market equity to earnings (p. 1093),
indicating that shocks to contemporaneous earnings relative to output drive the vast majority
of equity price (but not equity yield) movements. This is also reflected in the analysis of
Atkeson, Heathcote, and Perri (2025), who find that increases in the ratio of cash flows to
value added have affected valuation much more than the ratio of price to cash flows. While
we do not have direct evidence on the importance of profit-share changes outside the U.S.,
Atkeson, Heathcote, and Perri (2025) also estimate (see their Figure 7) that the increase in
cash flows to value added appears fairly specific to the U.S. data.
Finally, as noted in the main text, we rerun our higher-frequency return regressions in
Table 2, but now with changes in the two g∗
t,d proxies (profit growth and LTG) as explanatory
variables in addition to the change in expected output growth. Results are presented in
Table B.5 below. The results are very consistent with those presented in Table 2, with the
coefficient on (ˆ︃
∆ρ∗
t) very close to the original estimate of -19.1. The loading on ∆LTG is also
significant and positive. Overall, our main results continue to apply even when considering
changes in the profit share.
B.5
Details on Simulations for Figure 7
Figure 7 plots the distribution of average realized stock returns across 100,000 simulations of
an artificial economy. We now explain how each simulation is conducted. Each simulation has
two periods (0,1), and one period amounts to 30 years. We simulate expected consumption
growth g1 = g0 +εg
1 (abusing notation slightly), pure discounting terms ρ1 = ρ0 +ερ
1, and SDF
entropy L1,M = L0,M + εL
1 , as well as dividends d1 = d0 + µd + εD
1 . The equity risk premium
is rpt = Et[rmkt
t+1] −rf
t+1 = θt + Lt,M, where θ0 is chosen to match the average equity premium
and θ1 is either equal to θ0 or adjusts to ensure that the equity yield does not drop below
0.5%. Based on these variables, we calculate the ex ante interest rate as rf
t = ρt + γgt −Lt,M,
where we choose γ = 2 to match the empirically observed value. We calculate equity yields as
eyt = rf
t + rpt −λgt, and set the leverage parameter λ = 2 to match the empirical observation
that earnings yields are close to orthogonal to movements in growth rates. At time zero, our
calibration implies rp0 = 4% (relative to long-term yields), rf
0 = 4%, g0 = 2%, such that
ey0 = 4%, and the duration of the stock market is 25 years (which we view as somewhat
conservative).
The shocks ε are all drawn from heavy-tailed t-distributions with 5 degrees of freedom.
We choose the standard deviations of ερ and εg to match the standard deviations in our
23


---

global panel, and we choose the standard deviation of εL such that the volatility of realized
bond returns matches the annualized volatility of realized 30-year bond returns in the long
U.S. sample; we estimate this empirical counterpart to be around 2% based on data from
Robert Shiller’s website. Finally, we set the volatility of εD such that the volatility of realized
stock returns matches the volatility of realized 30-year stock returns in the long U.S. sample,
again based on data from Robert Shiller’s website. We conduct 100,000 simulations, and we
calculate and plot the distribution of realized excess returns relative to all three benchmarks
described in the main text.
24


---

B.6
Additional Results: Tables and Figures
See below for additional results referenced in the text, and see the main text for further
discussion and explanation of each of the tables and figures below.
Figure B.1: Residualized Equity Yield Changes vs. Growth and Uncertainty
CAN
DEU
FRA
GBR
ITA
JPN
USA
-1
-.5
0
.5
1
Δequity yield
(residualized on Δpure discounting)
-4
-3.5
-3
-2.5
-2
-1.5
Δr* from growth & VIX
Adj. R2 = -0.02 
Notes: This figure plots the country-level change in equity yields against changes in interest rates from growth
rates and uncertainty, where the equity yield change has now been residualized against the pure discounting
change shown in the left panel of Figure 3, ∆ˆ︁ρ∗
t,j. The sample is 1990–2023, or the longest available span for
the given country. See Figure 3 for additional details.
25


---

Table B.1: Regressions for Three-Year Changes in Trend Real Rates
(1)
(2)
(3)
U.S.
All
All
Change in expected growth ∆g∗
t,j
0.5**
0.3**
0.3**
(0.2)
(0.1)
(0.1)
Change in uncertainty ∆VIX2
t,j
-4.3**
-0.9
βj
(2.1)
(1.8)
Constant
-0.3***
-0.5***
-0.5***
(0.1)
(0.1)
(0.1)
Country FEs
✗
✓
✓
Country-Specific VIX2
t,j Loading
✓
✗
✓
Obs.
74
784
784
R2
0.17
0.05
0.06
Within R2
—
0.02
0.04
Notes: This table shows estimated OLS coefficients in the regression (21), along with standard errors in
parentheses. In column (1), standard errors are obtained using a block bootstrap with one-year blocks and
10,000 bootstrap draws. In columns (2)–(3), standard errors are clustered by country and date. Statistical
significance at the 10% level, 5% level, and 1% level are denoted by *, **, and ***, respectively. In column (3),
the country-specific loadings on the squared VIX, βj, are statistically significant at the 10% level for 6 of the
12 countries in our sample, and at the 5% level for 3 of the 12 countries (including the U.S.). The sample is
1990–2023, or the longest available span for the given country.
26


---

Figure B.2: Decomposition of U.S. Value-Weighted Equity Returns
-20
-10
0
10
20
30
Percent
1990 1995 2000 2005 2010 2015 2020 2025
3-Year Ann. Market Return
Growth Contribution
VIX Contribution
Pure Discounting Contribution
Notes: This figure shows three-year annualized average returns for the value-weighted U.S. stock market,
along with estimated underlying contributors. The growth contribution is the estimated coefficient ˆ︁πg in (22)
times the three-year change ∆g∗
t,j, plus the estimated contribution of contemporaneous cash flows. For this
additional contribution, we estimate a regression identical to (22) but with realized three-year log dividend
growth ∆dt,j as an additional predictor; the contemporaneous cash-flow contribution is equal to ∆dt,j times
its estimated coefficient. Each of the other two contribution terms in the figure is equal to the corresponding
predictor times its estimated coefficient in (22). The coefficient estimates are taken from column (2) of
Table 2, but divided by 3 (e.g., the pure discount loading is -6.3 rather than -19.1). This is to account for the
use of annualized returns in this plot, whereas the outcome variable for Table 2 is cumulative non-annualized
returns. The pure discounting predictor for (22) is obtained from the first-stage estimation in (21).
27


---

Table B.2: Forecasting Regressions for Future Three-Year Market Returns
(1)
(2)
(3)
10y yield
0.08
(0.38)
Survey-based r∗
t
0.50
(0.68)
Pure discounting term ˆ︁ρ∗
t
2.08***
(0.61)
Country FEs
✓
✓
✓
Obs.
1,050
842
842
R2
0.06
0.03
0.06
Within R2
0.00
0.00
0.03
Notes: This table shows coefficient estimates from forecasting regressions rmkt
t,t+3 = α + βXt + εt,t+3, where
rmkt
t,t+3 is the country-level annualized three-year market return, and Xt is an ex ante predictor. The first
column uses the 10-year nominal yield as the predictor variable, using data from each country’s central bank.
The second column uses our survey-based measure of the trend real rate r∗
t as predictor. The third column
uses our estimated pure discounting term ˆ︁ρ∗
t , estimated using (19)–(20) following the main specification in
column (3) of Table 1. Each regression includes country fixed effects, and all standard errors are clustered by
country and date. The sample is 1990–2023, or the longest available span for the given country.
28


---

Figure B.3: Portfolio Exposures to Pure Discount Rate Changes: Global Stocks
1: Shortest Duration
2
3
4
5: Longest Duration
-20
-10
0
10
Percent Change Per 1pp Yield Change
Pure Discounting Change
Raw 10Y Yield Change
Notes: This figure repeats the analysis shown in Figure 5 using the full global sample of stocks. We form
duration-sorted portfolios in the international panel following Gormsen and Lazarus (2023), and then we
estimate the same regressions as in Figure 5, with country-level fixed effects. The sample is 1990–2023.
29


---

Figure B.4: U.S. Estimation Results: Alternative with Short-Rate Forecasts
-1
0
1
2
3
Percent
1990
1995
2000
2005
2010
2015
2020
2025
r* (Bill)
Pure Disc. Term (Bill)
Pure Disc. Term (Baseline)
Notes: This figure replicates the U.S. decomposition in Figure 2, but with r∗measured using the Consensus
forecast of real bill yields (i.e., the forecasted nominal 3-month Treasury bill rate in year t+5, minus forecasted
inflation at the same horizon). The black line shows this bill-based r∗series, and the solid blue line shows the
implied pure discounting term, estimated as in Figure 2 but with the bill-based r∗as the outcome variable in
the decomposition regression. The dashed blue line shows the same pure discounting residual as plotted in
Figure 2. The short-rate sample is 1998–2023.
30


---

Table B.3: Robustness of r∗Decomposition: 10-Year Forecast Horizon
(1)
(2)
(3)
(4)
(5)
Baseline
SPF-Based
Short-Term r∗
GARCH Vol.
Unc. Index
Inputs changed:
—
r∗, g∗
r∗
L∗
L∗
Robustness of Figure 3: Regressions of ∆ey∗on ∆ρ∗(G7)
Slope
1.01***
—
0.84***
0.92***
1.03***
(0.21)
(0.15)
(0.19)
(0.22)
Intercept
0.12
—
0.35
0.23
0.21
(0.30)
(0.25)
(0.30)
(0.30)
Adj. R2
0.77
—
0.72
0.84
0.77
Robustness of ρ∗: Time-Series Properties (U.S.)
∆ρ∗over sample
-0.92
-1.35
-1.03
-0.94
-0.96
Corr(ρ∗, ρ∗
baseline)
1.00
0.73
0.75
0.99
1.00
Notes: In this version of Table 3, all relevant Consensus forecast inputs are taken at the 10-year horizon
(6-to-10-year average forecasts) rather than the main baseline five-year forward horizon. All alternative
regression inputs are as described in Table 3. As in that table, all r∗decompositions follow the specification
in column (3) of Table 1 for measures available across countries (columns (1), (3)–(5)), and they follow
column (1) of Table 1 for the U.S.-only measure (col. (2)). Col. (1) uses the baseline specification, with the
10-year forecasts used for r∗and g∗. Col. (2) replaces the Consensus data with SPF forecasts for the average
10-year real yield and real GDP growth over the next decade. Col. (3) replaces the Consensus-based r∗with
the cross-country short-term natural-rate estimates of Del Negro et al. (2019). These cross-country panel r∗
estimates are annual and run through 2019; the U.S. change in ρ∗is extended to the end of the sample using
a projection of this ρ∗onto the baseline ρ∗. Col. (4) replaces VIX2 with a country-level 6-month GARCH(1,1)
forecast of equity return variance. Col. (5) replaces VIX2 with the country-level Baker, Bloom, and Davis
(2016) uncertainty index. The top panel shows cross-country (G7) regressions of full-sample changes in equity
yields on changes in ρ∗, for all available specifications. Standard errors in parentheses are obtained via block
bootstrap by year with 10,000 draws. Statistical significance at the 10% level, 5% level, and 1% level are
denoted by *, **, and ***, respectively. The bottom panel shows U.S. time-series results. The first row shows
the full-sample change in the estimated ρ∗. The second row shows the correlation between the alternative
measure of ρ∗and this table’s version of the baseline measure from column (1). The sample is 1990–2023, or
the longest available span for the given country.
31


---

Table B.4: Robustness of r∗Decomposition: 6-to-10-Year Growth Forecasts
(1)
(2)
(3)
(4)
(5)
Baseline
SPF-Based
Short-Term r∗
GARCH Vol.
Unc. Index
Inputs changed:
—
r∗, g∗
r∗
L∗
L∗
Robustness of Figure 3: Regressions of ∆ey∗on ∆ρ∗(G7)
Slope
0.92***
—
0.84***
0.85***
0.94***
(0.19)
(0.15)
(0.16)
(0.19)
Intercept
-0.11
—
0.35
0.03
-0.02
(0.28)
(0.25)
(0.27)
(0.27)
Adj. R2
0.83
—
0.72
0.87
0.83
Robustness of ρ∗: Time-Series Properties (U.S.)
∆ρ∗over sample
-0.93
-1.35
-0.96
-0.98
-0.97
Corr(ρ∗, ρ∗
baseline)
1.00
0.75
0.78
0.99
0.99
Notes: In this version of Table 3, expected growth g∗is measured using the Consensus 6-to-10-year average
growth forecast rather than the main baseline five-year forecast. The trend real rate r∗is still measured at
the five-year forward horizon, so this version effectively imposes that expected yields in five years depend
on expected forward-looking growth rates at that point. All alternative regression inputs are as described
in Table 3. As in that table, all r∗decompositions follow the specification in column (3) of Table 1 for
measures available across countries (columns (1), (3)–(5)), and they follow column (1) of Table 1 for the
U.S.-only measure (col. (2)). Col. (1) uses the baseline specification, with the 6-to-10-year forecast used for
g∗. Col. (2) replaces the Consensus data with SPF forecasts for the average 10-year real yield and real GDP
growth over the next decade. Col. (3) replaces the Consensus-based r∗with the cross-country short-term
natural-rate estimates of Del Negro et al. (2019). These cross-country panel r∗estimates are annual and run
through 2019; the U.S. change in ρ∗is extended to the end of the sample using a projection of this ρ∗onto
the baseline ρ∗. Col. (4) replaces VIX2 with a country-level 6-month GARCH(1,1) forecast of equity return
variance. Col. (5) replaces VIX2 with the country-level Baker, Bloom, and Davis (2016) uncertainty index.
The top panel shows cross-country (G7) regressions of full-sample changes in equity yields on changes in ρ∗,
for all available specifications. Standard errors in parentheses are obtained via block bootstrap by year with
10,000 draws. Statistical significance at the 10% level, 5% level, and 1% level are denoted by *, **, and ***,
respectively. The bottom panel shows U.S. time-series results. The first row shows the full-sample change
in the estimated ρ∗. The second row shows the correlation between the alternative measure of ρ∗and this
table’s version of the baseline measure from column (1). The sample is 1990–2023, or the longest available
span for the given country.
32


---

Table B.5: Three-Year Return Regressions: Profit-Share Robustness
(1)
(2)
(3)
(4)
U.S.
U.S.
U.S.
U.S.
∆10y yield
4.19
(3.51)
∆pure discount ( ˆ︃
∆ρ∗
t )
-19.1**
-24.6***
-17.9***
(7.64)
(8.95)
(6.61)
∆exp. growth
-1.49
-15.3
-2.30
(14.0)
(16.7)
(12.7)
∆exp. profit growth
-0.14
(4.02)
∆LTG
5.94***
(2.03)
∆VIX2 × 100
-3.08**
-4.62***
-2.88***
(1.33)
(1.46)
(1.09)
Obs.
74
74
58
74
R2
0.04
0.20
0.47
0.36
Notes: This table replicates the analysis in Table 2 for U.S. data, but with additional predictor variables for
other measures related to equity dividend growth. See the notes for Table 2 for details on the estimation and
inference, and see Section 4.2 for descriptions of the additional predictor variables.
33


---

Figure B.5: Cross-Country Pure Discounting Changes vs. Total Capital Flows
CAN
DEU
FRA
GBR
ITA
JPN
USA
-3
-2
-1
0
1
Δr* from pure discounting
-100
-50
0
50
100
Σt (Capital Account)/GDP
Adj. R2 = 0.52 
Notes: The vertical axis shows the country-level change in the pure discounting residual, as plotted on the
horizontal axis in the first panel of Figure 3. The horizontal axis shows the cumulative sum of that country’s
net capital account balance as a share of annual GDP, measured from the IMF’s “Net Financial Account”
series. The sample is 1990–2023, or the longest available span for the given country.
34


---

Figure B.6: Interest Rates and Value Returns: Long-Term Global Evidence
CAN
DEU
FRA
GBR
ITA
JPN
USA
0
1
2
3
4
5
Average Ann. HML Return (%)
-5
-4.5
-4
-3.5
-3
-2.5
Δr* (1990–2023, %)
Adj. R2 = -0.17 
HML–Yield Disconnect
CAN
DEU
FRA
GBR
ITA
JPN
USA
0
1
2
3
4
5
-2
-1
0
1
2
3
Δr* from pure discounting
Adj. R2 = 0.26 
HML–Pure Discount Relationship
Notes: The left panel plots the country-level average annual return on the high-minus-low (HML) book-to-
market value factor versus the change in estimated trend real rate r∗over the 1990–2023 sample. Following
Fama and French (1993), each country’s HML factor is constructed based on a 2×3 size and book-to-market
double sort, with returns calculated as the average of the high-minus-low return for small and large firms.
See Gormsen and Lazarus (2023) for details. The right panel plots the same average annual HML return
against the change in the pure discounting term estimated using (19)–(20) following the main specification in
column (3) of Table 1. The sample is 1990–2023. Note that HML returns are available starting in 1990 for
all countries, whereas the equity yield samples start later than this in some cases (see Appendix B.1). As a
result, the ∆r∗terms in this figure may differ relative to Figure 3, given the earlier start date for the changes
calculated in this figure.
35


---

Figure B.7: Changes in Decomposition Terms Around Monetary Policy Shocks
-.04
-.02
0
.02
.04
High-frequency changes (pp)
-.2
-.1
0
.1
mps⊥
Implied ΔPure Discount Rate
-1 SD
-.02
-.01
0
.01
.02
-.2
-.1
0
.1
mps⊥
Implied ΔGrowth Rate   
Notes: This figure shows binned scatter plots of the change in the pure discount rate ˆ︃
∆ρ∗
t (left panel) and
the expected growth rate ∆gt (right panel) against the Bauer and Swanson (2023b) orthogonalized monetary
policy shock mps⊥
t in percentage points (pp). The changes in pure discount rates and expected growth are
recovered from (24)–(25) using the high-frequency (30-minute) stock-price and interest-rate changes. The
sample is 1990–2023. In the left panel, the line of best fit is estimated from all available observations using the
same regression as in Table 4, column (2). In the right panel, we show two fit lines: one for large expansionary
shocks for which mps⊥
t is less than one standard deviation below its sample mean (mps⊥
t < −0.065), and
one for the remaining shocks, separated by the vertical dashed line. Large expansionary shocks generate
conventional policy responses, whereby larger easing shocks lead to higher expected growth (as in the left
part of the panel). The remaining shocks otherwise generate a positive slope consistent with an information
effect (as in the right part of the panel).
36
