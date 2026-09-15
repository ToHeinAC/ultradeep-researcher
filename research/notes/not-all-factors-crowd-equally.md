---
title: 'Not All Factors Crowd Equally:'
id: not-all-factors-crowd-equally
tags:
- apple-earnings-durability-thesis-b8b3f1
- factor-crowding
- withdrawn-preprint
- low-authority
- alpha-decay
created: '2026-09-13T06:14:57.617341Z'
updated: '2026-09-15T19:32:22.145936Z'
source: https://arxiv.org/pdf/2512.11913v1
source_domain: arxiv.org
fetched_at: '2026-09-13T06:14:57.617016Z'
fetch_provider: crawl4ai
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: 'PROVENANCE FLAG (read first): this is v1 (11 Dec 2025) of a SELF-WITHDRAWN
  single-author preprint (Chorok Lee, KAIST, q-fin.PM). The author withdrew v2 on
  27 Dec 2025 stating the empirical validation in Sections 5-7 does not support the
  paper''s global-applicability claims, while standing by the theoretical model. Not
  peer-reviewed. Use with caution and label explicitly as a preliminary/withdrawn
  preprint if cited.\n\nModel: derives hyperbolic alpha decay a(t) = K/(1+lambda*t)
  from a Nash-equilibrium game where N agents split a fixed alpha capacity K (a_i
  = K/N), with entrants arriving via a Poisson process at rate lambda. Tested on 8
  Fama-French factors (1963-2024, French data library), fit via rolling 36-month Sharpe
  ratio, 1995-2024 in-sample: momentum fits hyperbolic decay best (R^2=0.65) vs linear
  (0.51) and exponential (0.61); long-term reversal R^2=0.30; but judgment-based factors
  -- value/HML (R^2=0.05), quality/RMW (R^2=0.05), investment/CMA (R^2=0.01) -- show
  essentially no fit under any decay model. Proposes a ''mechanical vs judgment''
  taxonomy (mean R^2=0.37 for mechanical factors like momentum/reversal vs 0.04 for
  judgment factors like value/quality, a claimed order of magnitude difference), paralleling
  Hua & Sun (2024, SSRN) ''barriers to entry.'' Out-of-sample (train 1995-2015, test
  2016-2024) the model OVER-predicts momentum''s remaining alpha (0.30 predicted vs
  0.15 actual), and this over-prediction correlates with factor-ETF trading-volume
  growth (Pearson rho=-0.63, p<0.001) -- interpreted as ETF-driven crowding accelerating
  beyond the historical decay rate post-2015. A real-time crowding signal (prediction
  residual) correctly flags 7 of 8 factors as crowded but crowding-timed trading strategies
  UNDERPERFORM a naive factor-momentum benchmark (Sharpe 0.22 vs 0.39), i.e. crowding
  info does not generate mean-return alpha because it is efficiently priced.\n\nTAIL-RISK
  RESULT (most relevant to unwind risk): out-of-sample 2001-2024, crowded reversal
  factors show 1.65-1.84x higher crash probability (bottom-decile-return threshold)
  than uncrowded states (e.g. short-term reversal: 16.9% vs 9.2% crash probability,
  p=0.078), while crowded MOMENTUM shows LOWER crash risk (0.38x, p=0.006) -- confirming
  Barroso, Edelen & Karehnke (2022, JFQA) that momentum crowding does not generate
  tail risk because crowding reinforces rather than fights the prevailing trend. The
  paper''s own framing: convergent/mean-reverting strategies (reversal) that crowd
  are ''coordinated wrong-way risk'' if the trend continues, while crowding into a
  trend-following/divergent strategy (momentum) is a sign of trend strength, not fragility
  -- directly bearing on whether momentum-driven crowding in mega-cap ''quality''/low-beta
  names is dangerous (paper''s own logic implies momentum-type crowding is lower-risk
  than mean-reversion-type crowding, though the paper does not study individual stocks
  or the 2025 quant unwind).'
raw_file: raw/not-all-factors-crowd-equally.pdf
doi: arXiv:2512.11913v1
utility_score: 13.0
---

*Suggested by [[251211913-not-all-factors-crowd-equally-modeling-measuring-and-trading-on-alpha]] — v1 full text before author withdrawal*

Not All Factors Crowd Equally:
Modeling, Measuring, and Trading on Alpha Decay
Chorok Lee
KAIST
choroklee@kaist.ac.kr
Abstract
We derive a specific functional form for factor alpha
decay—hyperbolic decay α(t) = K/(1 + λt)—from
a game-theoretic equilibrium model, and test it against
linear and exponential alternatives. Using eight Fama-
French factors (1963–2024), we find: (1) Hyperbolic
decay fits mechanical factors. Momentum exhibits
clear hyperbolic decay (R2
= 0.65), outperform-
ing linear (0.51) and exponential (0.61) baselines—
validating the equilibrium foundation. (2) Not all fac-
tors crowd equally. Mechanical factors (momentum,
reversal) fit the model; judgment-based factors (value,
quality) do not—consistent with a signal-ambiguity
taxonomy paralleling Hua and Sun’s “barriers to en-
try.”
(3) Crowding accelerated post-2015.
Out-
of-sample, the model over-predicts remaining alpha
(0.30 vs. 0.15), correlating with factor ETF growth
(ρ = −0.63). (4) Average returns are efficiently
priced. Crowding-based factor selection fails to gen-
erate alpha (Sharpe: 0.22 vs. 0.39 factor momentum
benchmark). (5) Crowding predicts tail risk. Out-of-
sample (2001–2024), crowded reversal factors show
1.7–1.8× higher crash probability (bottom decile re-
turns), while crowded momentum shows lower crash
risk (0.38×, p = 0.006). Our findings extend equilib-
rium crowding models (DeMiguel et al.) to temporal
dynamics and show that crowding predicts crashes, not
means—useful for risk management, not alpha gener-
ation.
Keywords: factor investing, alpha decay, crowding,
game theory, market efficiency
1
Introduction
The momentum factor returned approximately 10%
annually in the 1990s. Today, that figure is closer to
2%. What happened?
A growing body of evidence documents the de-
cay of factor premia following academic publication.
McLean and Pontiff [McLean and Pontiff, 2016] found
that approximately 50% of anomaly alpha disappears
post-publication, consistent with investors learning
from research and arbitraging away returns. Yet while
the existence of decay is well-established, its mechan-
ics remain poorly understood. Do all factors decay
similarly? Can we predict the rate of decay? And
crucially—can we profit from this knowledge?
We address these questions through a game-
theoretic model of factor crowding. The core insight
is simple: when N agents discover and trade the same
profitable signal, they compete for a fixed “alpha ca-
pacity” K.
In Nash equilibrium, each agent earns
αi = K/N. As agents discover the signal over time,
aggregate alpha decays hyperbolically:
α(t) =
K
1 + λt
(1)
where λ is the rate of strategy discovery.
This model yields four testable predictions, which
we evaluate using data on eight Fama-French factors
from 1963–2024:
1. Hyperbolic decay fits better than alternatives.
For momentum, our model achieves R2 = 0.65, out-
performing linear decay (0.51) and exponential decay
(0.61). The improvement validates the game-theoretic
foundation.
2.
Not all factors crowd equally.
The model
fits “mechanical” factors—those with unambiguous,
easily replicated signals like momentum (“buy recent
winners”)—but fails for “judgment” factors like value,
where the signal (“what is cheap?”) admits multiple
interpretations.
3.
Crowding accelerated post-2015.
Training
on 1995–2015 and predicting 2016–2024, the model
1
arXiv:2512.11913v1  [q-fin.PM]  11 Dec 2025


---

over-estimates remaining alpha (0.30 predicted vs.
0.15 actual). This over-prediction correlates with fac-
tor ETF volume growth (ρ = −0.63), suggesting that
democratization of factor investing through ETFs ac-
celerated crowding beyond historical rates.
4. Crowding is detectable but efficiently priced.
We construct a real-time crowding signal based on pre-
diction residuals. While the signal correctly identifies
that 7 of 8 factors are systematically crowded, factor
timing strategies based on the signal fail to outperform
naive benchmarks (Sharpe: 0.22 vs. 0.39 for factor
momentum).
This last finding—a negative result—is itself infor-
mative. It suggests that crowding, once established,
is incorporated into prices quickly enough that public
signals offer no trading advantage. The signal’s value
lies in regime detection (identifying when factor in-
vesting faces headwinds) rather than alpha generation.
Our contributions are: (1) a game-theoretic model
that explains why alpha decays and predicts its func-
tional form; (2) empirical validation distinguishing
mechanical from judgment factors; (3) evidence that
post-2015 crowding acceleration correlates with ETF
growth; and (4) an honest evaluation showing that
crowding signals, while informative, do not generate
trading alpha.
2
Related Work
Post-publication
decay.
McLean
and
Pon-
tiff [McLean and Pontiff, 2016] documented that
returns to 97 characteristics decline by approximately
58% after publication. Falck et al. [Falck et al., 2021]
extend this to 72 factors, finding publication year
explains 30% of Sharpe decay variance. These papers
document that decay happens; we model why and
derive a specific functional form.
Game-theoretic
models.
DeMiguel
et
al. [DeMiguel et al., 2021] develop an equilib-
rium model where competition erodes factor profits,
showing profits scale with the number of investors.
Our work differs in focus: they study cross-sectional
equilibrium (how factors interact); we study temporal
dynamics (how alpha decays over time) and derive a
testable decay functional form they do not consider.
Crowding and predictability. Kang et al. [Kang
et al., 2021] show that CFTC position-based crowd-
ing measures predict commodity factor returns. We
test whether model-implied crowding predicts equity
factor returns and find it does not—suggesting mar-
ket structure differences between commodities (with
observable positioning) and equities (where crowding
must be inferred).
Heterogeneous crowding. Hua and Sun [Hua and
Sun, 2024] study heterogeneous crowding vulnerabil-
ity, attributing differences to “barriers to entry.” Our
mechanical-judgment taxonomy parallels this intuition
but operationalizes it through model fit: mechanical
factors exhibit hyperbolic decay; judgment factors do
not.
Crowding and tail risk.
Barroso, Edelen, and
Karehnke [Barroso et al., 2022] find that momentum
crowding is associated with lower crash risk, conclud-
ing that “crowding does not generate tail risk when ar-
bitrageurs rationally condition on feedback.” We con-
firm their momentum result but reveal factor-specific
heterogeneity: reversal factors show the opposite pat-
tern, with crowding predicting elevated crash proba-
bility.
Our contribution. We make three contributions:
(1) derive hyperbolic decay α(t) = K/(1 + λt) from
game-theoretic equilibrium, outperforming linear and
exponential alternatives for mechanical factors; (2)
show that average returns are efficiently priced—
crowding-based factor selection fails; (3) demonstrate
heterogeneous tail risk across factor types, extending
Barroso et al.’s momentum-only analysis to show that
reversal factors exhibit opposite tail risk dynamics.
3
Model
3.1
Setup
Consider N(t) agents who have discovered a prof-
itable signal at time t. Each agent is small relative to
the market but collectively they affect prices through
market impact.
Let the signal predict excess return r with edge α0
when undiscovered.
Total alpha capacity is K =
α0/2. Agents trade quantity qi and face linear price
impact ∆P = γ P
i qi, where γ is Kyle’s lambda.
2


---

3.2
Single-Period Nash Equilibrium
Each agent maximizes expected profit:
max
qi
E

qi ·

r −γ
N
X
j=1
qj




(2)
Taking first-order conditions and imposing symme-
try (qi = q∗for all i):
q∗=
α0
2γN
(3)
Substituting back, equilibrium alpha per agent is:
αi = α0
2N = K
N
(4)
Result 1:
Alpha per agent decays as 1/N—
hyperbolic in the number of discoverers.
3.3
Dynamic Model with Entry
Agents discover the signal according to a Poisson pro-
cess with rate λ. The expected number at time t is
E[N(t)] = λt. Substituting into the equilibrium con-
dition:
α(t) =
K
1 + λt
(5)
This is our hyperbolic decay model (Equation 1).
The key distinction from exponential decay (Ke−λt)
is that hyperbolic decay is slower initially but has a
heavier tail—alpha persists longer but at lower levels.
3.4
Why Hyperbolic, Not Exponential?
Table 1: Decay models and their assumptions
Model
Assumption
Decay Form
Nash (ours)
Compete for fixed K
K/(1 + λt)
Learning
Price incorporation
Ke−λt
Ad hoc
None
K −bt
The hyperbolic form arises specifically from the
1/N profit-splitting in Nash equilibrium. Alternative
assumptions yield different forms (Table 1). We test
these alternatives empirically.
4
Empirical Analysis
4.1
Data
We use monthly returns for eight factors from Kenneth
French’s data library (1963–2024): market (MKT),
size (SMB), value (HML), profitability (RMW), in-
vestment (CMA), momentum (Mom), short-term re-
versal (ST Rev), and long-term reversal (LT Rev).
Our alpha proxy is the rolling 36-month Sharpe ratio.
4.2
Model Fit and Baseline Comparison
Table 2 reports R2 for each model-factor combination,
fitting on positive Sharpe observations from 1995–
2024.
Table 2: Model comparison: In-sample R2 (1995–
2024). Bold indicates best fit.
Factor
Hyperbolic
Linear
Exponential
Mom
0.65
0.51
0.61
LT Rev
0.30
0.26
0.29
ST Rev
0.15
0.14
0.15
SMB
0.10
0.17
0.13
MKT
0.07
0.07
0.07
HML
0.05
0.07
0.06
RMW
0.05
0.05
0.05
CMA
0.01
0.01
0.01
For momentum, hyperbolic decay achieves R2 =
0.65, outperforming linear (0.51) by 27% and expo-
nential (0.61) by 7%. Long-term reversal also shows
a clear hyperbolic pattern (R2 = 0.30).
However,
judgment-based factors (HML, RMW, CMA) show
poor fits across all models (R2 < 0.10).
Figure 1 illustrates this contrast visually. For mo-
mentum (left panel), the hyperbolic curve tracks the
rolling Sharpe ratio’s decline from ∼1.5 in the mid-
1990s to ∼0.25 today.
For value (right panel), no
model captures the erratic pattern—the factor oscil-
lates without systematic decay.
4.3
Mechanical vs. Judgment Taxonomy
We propose a taxonomy based on signal ambiguity:
Mechanical factors have unambiguous signals:
• Momentum: “Buy stocks with high past returns”
• Reversal: “Buy stocks with low recent returns”
3


---

Figure 1: Model fit comparison: Momentum (mechan-
ical) exhibits clear hyperbolic decay (R2 = 0.65);
Value (judgment) shows no systematic decay pattern
(R2 = 0.05).
Judgment factors require interpretation:
• Value: “What is cheap?” (book/market? earn-
ings?)
• Quality: “What is quality?” (ROE? accruals?)
The hypothesis is that mechanical factors crowd
quickly because the replication path is clear, while
judgment factors crowd diffusely because different in-
vestors implement different versions.
Figure 2 shows R2 by factor type.
Mechanical
factors achieve mean R2 = 0.37; judgment factors
achieve mean R2 = 0.04—an order of magnitude
lower.
Figure 2: Model fit by factor type. Mechanical factors
fit hyperbolic decay; judgment factors do not.
4.4
Out-of-Sample Prediction
We train on 1995–2015 and predict 2016–2024. For
momentum:
• Direction: Correct—model predicts continued
decay
• Magnitude: Over-predicted (mean 0.30 vs. ac-
tual 0.15)
• RMSE: 0.19
The systematic over-prediction is informative.
A
model trained on 1995–2015 captures that era’s equi-
librium decay rate.
The over-prediction post-2015
suggests crowding accelerated beyond historical rates.
4.5
ETF Correlation
To test whether ETF proliferation explains the acceler-
ation, we correlate the cumulative prediction residual
with factor ETF trading volume (2013–2024).
Finding: Pearson ρ = −0.63 (p < 0.001).
The negative correlation indicates that as ETF vol-
ume grows, the model increasingly over-predicts re-
maining alpha (Figure 3).
Figure 3: Cumulative residual vs. factor ETF volume.
Correlation ρ = −0.63 suggests ETF growth acceler-
ated crowding.
5
Can We Trade on Crowding?
5.1
Signal Construction
We construct a real-time crowding signal:
1. Fit hyperbolic model on expanding window (min
120 months)
2. Compute predicted Sharpe for current period
3. Residual = Actual −Predicted
4. Negative residual ⇒crowding accelerated
4


---

5.2
Signal Properties
Across 8 factors (2006–2024):
• Mean
residual:
−0.41
(systematic
over-
prediction)
• 7 of 8 factors have negative mean residual
• Only RMW shows slight uncrowding (+0.07)
5.3
Trading Strategies
We test three strategies (Table 3):
Table 3: Strategy performance (2017–2025)
Strategy
Sharpe
Factor Momentum
0.39
Crowding-Timed
0.22
Equal Weight
0.17
Factor
momentum
(0.39)
outperforms
both
crowding-timed (0.22) and equal weight (0.17). While
crowding-timed marginally beats equal weight, the
improvement is economically insignificant and fails to
match the simple factor momentum benchmark.
5.4
Why Doesn’t the Signal Work?
Three hypotheses:
H1: Contemporaneous, not predictive. The sig-
nal tells you factors are crowded but doesn’t predict
which will underperform next.
H2: Efficiently priced. Market participants already
incorporate crowding information.
H3: Insufficient dispersion.
When 7/8 factors
show the same signal, there’s no differentiation to ex-
ploit.
Our evidence is most consistent with H2—crowding
is observable but efficiently priced.
6
Utilization: Tail Risk Prediction
If crowding does not predict average returns, what can
practitioners do with crowding information? We hy-
pothesize that crowding predicts tail risk—the proba-
bility of extreme losses—even when it fails to predict
mean returns.
6.1
Intuition: The Crowded Exit Problem
When many investors hold the same position, aver-
age returns may be efficiently priced.
However, in
stress scenarios, crowded positions face correlated liq-
uidation—everyone exits simultaneously, amplifying
losses. This suggests crowding should predict crash
probability, not average returns.
6.2
Out-of-Sample Test
We establish thresholds using training data (1980–
2000) only:
• Crowding threshold:
training-period median
residual per factor
• Crash threshold: training-period 10th percentile
of returns
We then apply these thresholds to out-of-sample
data (2001–2024) and compute crash probabilities
conditional on crowding state.
Table 4: Tail risk by crowding state (OOS 2001–2024)
Factor
P(crash|crowded)
P(crash|uncrowded)
Ratio
p-value
ST Rev
16.9%
9.2%
1.84
0.078
MKT
15.0%
8.9%
1.68
0.215
LT Rev
19.4%
11.8%
1.65
0.095
CMA
8.6%
6.7%
1.30
0.677
SMB
8.0%
7.3%
1.10
0.773
Mom
10.9%
28.2%
0.38
0.006
6.3
Heterogeneous Tail Risk
The results reveal factor-specific patterns that reflect
the underlying economic mechanisms:
Reversal factors (ST Rev, LT Rev) show elevated
crash risk when crowded (1.65–1.84×). The mech-
anism: reversal strategies bet on mean reversion—
buying recent losers, selling recent winners.
When
many investors crowd into this contrarian bet, they are
collectively positioned against the prevailing trend. If
the trend continues rather than reverses, all contrar-
ian positions lose simultaneously, generating a crash.
Crowded reversal represents coordinated wrong-way
risk.
Momentum shows the opposite pattern: crowded
momentum has lower crash probability (0.38×, p =
0.006). The mechanism: momentum strategies ride
5


---

existing trends—buying recent winners. Crowded mo-
mentum means many investors are reinforcing the
trend, which tends to sustain rather than reverse it.
Here, crowding is a sign of trend strength, not vul-
nerability. This confirms Barroso et al.’s [Barroso et
al., 2022] finding that momentum crowding does not
generate tail risk.
Key insight: The tail risk relationship depends on
whether the strategy follows or fights the trend:
• Trend-following (momentum):
Crowding con-
firms trend strength →lower crash risk
• Mean-reverting (reversal): Crowding bets against
trend →higher crash risk if trend continues
Pooled result: Across all factors, crowded states
show 18% higher crash probability (13.4% vs. 11.3%).
Five of eight factors show ratio > 1.
6.4
Implications
Crowding predicts tail risk, not average returns:
• Position sizing: Reduce exposure to crowded re-
versal factors
• Stop-losses: Tighter thresholds on crowded posi-
tions
• Factor-specific: Momentum crowding is benign;
reversal crowding is dangerous
This finding reconciles efficient pricing of average
returns with actionable risk information—crowding
matters for the tails, not the mean.
7
Discussion
Implications for practitioners. (1) Mechanical fac-
tors crowd fastest—monitor capacity.
(2) Abandon
crowding-based factor selection—average returns are
efficiently priced. (3) Use crowding for tail risk man-
agement: reduce exposure to crowded reversal factors,
but note that momentum crowding is benign.
Implications for researchers. Our results distin-
guish between efficient pricing of average returns and
predictability of tail risk. This separation—crowding
predicts crashes, not means—offers a framework for
future work on factor risk management.
Limitations. Only 8 factors (more factors would
strengthen results). US equities only. Tail risk signif-
icance is marginal for individual factors (p ≈0.08–
0.10) though directionally consistent (5/8 factors).
Momentum’s opposite pattern requires further inves-
tigation.
8
Conclusion
We developed a game-theoretic model of factor crowd-
ing that explains why alpha decays, predicts its func-
tional form, and distinguishes mechanical from judg-
ment factors. The model fits momentum well (R2 =
0.65) and reveals accelerated crowding post-2015 cor-
relating with ETF growth.
Our central finding: crowding predicts tail risk,
not average returns.
Cross-sectional factor timing
fails—average returns are efficiently priced.
How-
ever, out-of-sample (2001–2024), crowded reversal
factors show 1.7–1.8× higher crash probability, while
crowded momentum shows lower crash risk (0.38×).
The key insight: crowding is tail risk information,
not return information. It tells you about crash prob-
ability, not expected returns—and this relationship is
factor-specific.
For practitioners: use crowding for position sizing
and stop-loss calibration on reversal factors; momen-
tum crowding is benign. For researchers: the separa-
tion between efficiently priced means and predictable
tails offers a framework for factor risk management.
“Crowding doesn’t tell you where the mar-
ket is going. It tells you how hard you’ll hit
the ground if it falls.”
References
R. D. McLean and J. Pontiff. Does academic research
destroy stock return predictability? Journal of Fi-
nance, 71(1):5–32, 2016.
V. DeMiguel, A. Martin-Utrera, and R. Uppal. What
alleviates crowding in factor investing? Journal of
Finance, forthcoming, 2021.
W. Kang, K. G. Rouwenhorst, and K. Tang. Crowding
and factor returns. Working paper, Yale School of
Management, 2021.
6


---

R. Hua and C. Sun.
Dynamics of factor crowding.
Working paper, SSRN 5023380, 2024.
P. Barroso, R. M. Edelen, and P. Karehnke. Crowd-
ing and tail risk in momentum returns. Journal of
Financial and Quantitative Analysis, 57(4):1313–
1342, 2022.
A. Falck, A. Rej, and D. Thesmar.
Why and how
systematic strategies decay. CFM Working Paper,
2021.
A. S. Kyle. Continuous auctions and insider trading.
Econometrica, 53(6):1315–1335, 1985.
R. Arnott, N. Beck, V. Kalesnik, and J. West. How can
smart beta go horribly wrong? Research Affiliates
Working Paper, 2016.
N. Jegadeesh and S. Titman.
Returns to buying
winners and selling losers.
Journal of Finance,
48(1):65–91, 1993.
E. F. Fama and K. R. French. Common risk factors in
the returns on stocks and bonds. Journal of Finan-
cial Economics, 33(1):3–56, 1993.
7
