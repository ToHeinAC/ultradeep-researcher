---
title: Inferential Theory for Granular Instrumental Variables in High Dimensions*
id: inferential-theory-for-granular-instrumental-variables-in-high-dimensions
tags:
- apple-earnings-durability-thesis-b8b3f1
created: '2026-09-12T17:38:34.453614Z'
updated: '2026-09-15T19:32:22.085462Z'
source: https://arxiv.org/abs/2201.06605
source_domain: arxiv.org
fetched_at: '2026-09-12T17:38:34.453351Z'
fetch_provider: crawl4ai
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Pure econometric extension of Gabaix-Koijen's GIV estimator to large-N/large-T
  settings, applied empirically to the global crude oil market (not equities); shows
  market concentration (Herfindahl) raises estimator PRECISION, not the size of any
  price-impact multiplier; contains no equity or Apple-specific estimate and does
  not revise GK's aggregate multiplier.
raw_file: raw/inferential-theory-for-granular-instrumental-variables-in-high-dimensions.pdf
doi: arXiv:2201.06605
citation_count: 3
is_retracted: false
---

*Suggested by [[in-search-of-the-origins-of-financial-fluctuations-the-inelastic-markets-hypothe]] — identification-theory critique of GIV estimator underlying the multiplier*

Inferential Theory for Granular Instrumental Variables in High Dimensions*
Saman Banafti† and Tae-Hwy Lee‡
†Amazon; ‡University of California, Riverside.
Email: sbanafti@amazon.com, taelee@ucr.edu.
September 26, 2023
Abstract
The Granular Instrumental Variables (GIV) methodology exploits panels with factor error structures
to construct instruments to estimate structural time series models with endogeneity even after controlling
for latent factors. We extend the GIV methodology in several dimensions. First, we extend the identi-
fication procedure to a large N and large T framework, which depends on the asymptotic Herfindahl
index of the size distribution of N cross-sectional units. Second, we treat both the factors and loadings
as unknown and show that the sampling error in the estimated instrument and factors is negligible when
considering the limiting distribution of the structural parameters. Third, we show that the sampling error
in the high-dimensional precision matrix is negligible in our estimation algorithm. Fourth, we overiden-
tify the structural parameters with additional constructed instruments, which leads to efficiency gains.
Monte Carlo evidence is presented to support our asymptotic theory and application to the global crude
oil market leads to new results.
Keywords: Interactive effects, Factor error structure, Simultaneity, Power-law tails, Asymptotic Herfindahl
index, Global crude oil market, Supply and demand elasticities, Precision matrix.
JEL Classifications: C26, C36, C38, C46, C55
*We are grateful to Xu Cheng, Xavier Gabaix, Gloria Gonzalez-Rivera, Bruce Hansen, Jean Helwege, Bo Honoré, Guido
Imbens, Ralph Koijen, Andrew Patton, Markus Pelger, Hashem Pesaran, Ekaterina Seregina, Ruoyao Shi, Aman Ullah, Tiemen
Woutersen, Qiankun Zhou, seminar participants at UC Riverside and JSM 2021 for helpful comments and suggestions. We thank
Michael Bates for providing access to UCR’s High Performance Computing Center to carry out simulations efficiently.
arXiv:2201.06605v2  [econ.EM]  25 Sep 2023


---

1.
Introduction
In the absence of randomized control trials, finding valid and strong instruments to circumvent unob-
served confounders is a very challenging task. The Granular Instrumental Variables, hereafter GIV, method-
ology that Gabaix and Koijen (2021) propose, establishes a systematic way to construct instruments from
suitably weighted idiosyncratic shocks, from observational datasets and use them as instruments for aggre-
gate endogenous variables.
Constructing instruments. There are some existing methodologies which seek to eliminate the need
to find an instrument. A leading example is the Arellano and Bond (1991) framework in the context of
estimating the speed of adjustment or state dependence parameters using dynamic panel data models with
fixed effects, in which higher order lags of the dependent variable serve as instruments for the included lags
of the dependent variable. The Bartik (1991) methodology (aka shift-share estimators) where instruments
are constructed from identities involving the (endogenous) explanatory variable whose shift component
is interacted with shares. The Rigobon (2003) setting exploits the existence of structural breaks in the
conditional heteroskedasticity regime, which is common place in many applications of interest. This allows
one to bring a system with less equations than unknowns to a just identified system with as many equations as
unknowns. The Bai and Ng (2010) methodology lays out a panel simultaneous equations model (similar to
the model analyzed in this paper) where the estimated (strong) factors can be used as instrumental variables
under certain conditions. We will return to the Bai and Ng (2010) methodology when we overidentify the
structural parameters of interest as it is inspired by their framework. The vast methodological refinements
cited within the papers referenced above are not listed here for brevity.
Microeconomic (granular) origins of aggregate fluctuations. How can idiosyncratic shocks be
relevant for endogenous aggregate variables? The literature on "granularity" traces back to historic debates
in macroeconomics; no attempt to fully catalog this debate is made here, rather a concise summary is offered.
Long and Plosser (1983) demonstrate that in a multisector stochastic neoclassical growth model, sectoral
shocks (as opposed to aggregate shocks) can potentially lead to GDP fluctuations. Intuitively, complex pro-
duction processes form sectoral linkages which in turn provide a transmission mechanism of shocks across
sectors. Subsequently, Horvath (2000) and Dupor (1999) debate whether sectoral shocks decay according
to
1
?
N as the central limit theorem would suggest. Gabaix (2011) provides an initial theoretical solution to
the debate by showing that when the firm size distribution is heavy tailed, the central limit theorem does
not apply and sectoral volatility decays much slower than
1
?
N . Gabaix (2011) coins this mechanism as the
so-called "granular" hypothesis, in which the economy is composed of incompressible grains as opposed
1


---

to infinitesimally small micro units. Acemoglu et al. (2012) formulates a network approach to demonstrate
that sectoral idiosyncratic shocks generate non-negligible aggregate volatility when there exists sufficient
asymmetry in the input-output relationships. Pesaran and Yang (2020) build off of the theoretical approach
of Acemoglu et al. (2012) and develop econometric theory to measure the degree of network dominance and
in their application they find some evidence of sector-specific shock propagation albeit not overwhelmingly
strong for the US input-output accounts data over the period 1972-2002. More empirical evidence for such
propagation mechanism is presented in Gatti et al. (2005), Canals et al. (2007), Koren and Tenreyro (2007),
Blank et al. (2009), Malevergne et al. (2009), Yan (2011), Gabaix (2011), Carvalho and Gabaix (2013),
Schiaffi et al. (2013), Acemoglu et al. (2017), Jannati (2017) and Lera and Sornette (2017).
GIV, Gabaix and Koijen (2021). In an econometric framework, GK illustrate that when the market
under consideration is sufficiently concentrated, then one can use the collection of idiosyncratic shocks to
individual micro units, at each time period t, as an instrument for endogenous aggregate variables. The
instrumental relevance follows heuristically from the paragraphs above. The exogeneity condition, as in
any instrumental variables procedure, requires assumptions on unobserved random variables. However it
should be noted that the exogeneity condition exploited in this framework is a relatively mild assumption
that is often made in factor models (e.g. Bai and Ng (2002)) for identification purposes. The insight and
contribution of GK opens the doors to a wide possibility of ways in which one can continue building on the
promising new GIV methodology.
Contributions of this paper. Our contributions to the GIV methodology are primarily focused on the
underlying econometric issues. First, we naturally extend GK’s identification procedure to a large N and
large T framework (GK formally introduced GIV for a fixed N and large T) by establishing and restricting
the asymptotic behavior of the Herfindahl index for large N markets as a function of the tail index of
the size distribution. Given the large N and large T framework, we treat both the factors and loadings
as unknown and allow the idiosyncratic error term to be weakly cross-sectionally correlated.1 As such,
from our preliminary stage, we extract not only the estimated factors but also the estimated loadings via
principal components analysis, PCA hereafter, or depending on the generality of the model (kx̸ = 0 in
our notation from Section 2), we use the iterative OLS-PCA method of Bai (2009). Second, we show that
the sampling error in the estimated instrument and estimated factors is negligible when considering the
limiting distribution of the structural parameters of interest; that is, the estimator is robust to the latent factor
structure. Moreover, the exogeneity requirement for one of the structural parameters generally depends
1GK treat the factor loadings as known and extract the factors via period-by-period cross-sectional regressions. While they
advocate extraction of latent factors via principal components analysis when loadings are unknown, they abstract away from the
corresponding sampling error. We will show that the sampling error is indeed negligible.
2


---

on a potentially high dimensional precision matrix (the inverse of the covariance matrix). Third, we show
that the sampling error in the high dimensional precision matrix is negligible in our iterative estimation
algorithm for said structural parameter. Fourth, we overidentify the structural parameters which leads to
efficiency gains. This leads to new and improved results in our empirical application of GIV to the global
crude oil markets. Monte Carlo evidence is presented to confirm the finite sample behavior of our estimators
are well approximated by the asymptotic distributions. We label our refinement to the GIV methodology
as Feasible Granular Instrumental Variables or FGIV for short. Finally, an empirical application of the
estimation methods to estimate demand and supply elasticities of the global crude oil markets are presented
to demonstrate the estimation procedures.
Notation. We distinguish vectors and matrices from scalars by making an object bold. Let {Xit, i =
1, . . . , N; t = 1, . . . , T} be a double index process of random variables where N denotes the number of
cross-sectional units and T denotes the number of time periods. We frequently stack across i, in which we
obtain X·t
N×1
:=
´
X1t
. . .
XNt
¯′
. Similarly, if we stack across t we obtain Xi·
T×1
:=
´
Xi1
. . .
XiT
¯′
.
When Xit is itself a vector, say of dimension k, then we obtain a matrix when we stack across i or t, e.g. X·t
N×k
or Xi·
T×k
. Define Xwt as the cross-sectionally weighted average of Xit, that is Xwt := w′X·t = PN
i=1 wiXit.
Common weights, w
N×1 = (wi), used frequently throughout the paper are (1) the precision weights, E :=
Σ
−1
u ι
ι′Σ
−1
u ι where Σu
N×N
:= E(u·tu′
·t) is the covariance matrix of the idiosyncratic error term, uit,
ι
N×1 is a
vector of ones and (2) the share weights, which we simply refer to as size weights, S :=
´
S1
. . .
SN
¯′
.
Let r
Xit = Xit −¯Xt, where ¯Xt =
1
N
PN
i=1 Xit, denote a cross-sectionally demeaned variable. Unless
otherwise specified, we denote the L2-norm as ||·|| or sometimes explicitly as ||·||2, the L1-norm as ||·||1
and the Frobenius norm as ||·||F ; if another norm is used, it will be explicitly noted. Given a square matrix
A, let γmax(A) denote the maximum eigenvalue of A. Joint convergence of N and T will be denoted
as (N, T)
j→∞without any restriction on the relative rates; whenever restrictions on relative rates of
convergence are imposed, it will be explicitly noted. The expression
p→denotes convergence in probability
while
d→denotes convergence in distribution. The equation y = Op(x) states that the vector of random
variables y is at most of order x in probability. The equation a = Θp(b) states that a is stochastically
bounded by b and b is stochastically bounded by a, hence a and b rise jointly proportionally.
3


---

2.
Model
A general formulation of the model examined in this paper is given in the following panel simultaneous
equations model with factor error structure
yit = Bxit + Cat + vit,
vit = Λ′
iF t + uit,
where yit =
´
y1,it
. . .
yG,it
¯′
is a G × 1 vector of dependent variables, xit =
´
x1,it
. . .
xkx,it
¯′
is a kx × 1 vector of strictly exogenous variables (which can be arbitrarily correlated with the common
factors, F t, and/or the loadings, Λi), at =
´
a1,t
. . .
aka,t
¯′
is a ka × 1 vector of potentially endogenous
aggregate variables, vit is a G × 1 vector of composite error terms which admit a low-rank plus sparse
(factor structure) error decomposition, where Λi is an r × G matrix of latent factor loadings and F t is an
r × 1 vector of latent factors.
In our exposition, we focus on the canonical setting of estimating the supply and demand elasticities in
the global crude oil market, so we set the dimension of G = 2 for supply and demand variables respectively.
We take kx = 0 for ease of exposition but we present a general estimation algorithm for when kx̸ = 0.
Moreover, we assume that only one of the G = 2 variables has a panel structure, whereas the other variable
is an aggregate time series. The main results extend relatively naturally to the case where both variables have
a panel model. That is, yit =
´
dt
yit
¯′
where dt is the log change of aggregate crude oil consumption and
yit is the log change of country i’s crude oil production, at = pt, with ka = 1, is the log change of real crude
oil price (where we deflate the nominal oil price with the U.S. general price in3dex).2 Given our stylizations
the coefficient matrix C and composite error, vit becomes
C =
˜
ϕd
0
0
ϕs
¸
,
vit = Λ′
iF t + uit =
˜
1
0
0
λi
¸ ˜
εt
ηt
¸
+
˜
0
uit
¸
,
2One may wonder why pt is not disaggregated; in fact the pt we use can be considered as the weighted average of country
specific real oil prices (in changes). As shown in Mohaddes and Pesaran (2016), for a proper global analysis, deflating the nominal
oil price in U.S. dollars by the U.S. price index is generally theoretically invalid unless the law of one price holds universally.
Namely, let Pit denote the general price index faced by country i, Eit denotes country i’s exchange rate measured as units of
country i’s currency per U.S. dollar, pit denote country specific log of real oil prices and ˜pt denotes nominal oil prices in U.S.
dollars, if EitPUS,t = Pit ∀i; then it follows that PN
i=1 wipit = ˜pt + PN
i=1 wilog(Eit/Pit) = ˜pt + PN
i=1 wilog(1/PUS,t) =
˜pt −pUS,t := pt. As it turns out, pt = ˜pt −pUS,t is an appropriate approximation as documented in Mohaddes and Pesaran
(2016) for their long run analysis, in the sense that it respects the long-run equilibrium relationships. We assume it is an appropriate
approximation for our short-run analysis.
4


---

where the coefficients ϕd and ϕs denote the crude oil demand and supply elasticities, respectively, and ηt, λi
are r × 1 vectors of latent factors and latent loadings, respectively. Our stylized simultaneous equations
model takes the simple form
dt = ϕdpt + εt
(1)
yit = ϕspt + λ′
iηt + uit.
(2)
The global market clearing condition is given by ySt = dt, where ySt := S′y·t = PN
i=1 Siyit, S is the
N × 1 vector of shares that are normalized such that PN
i=1 Si = 1 and i and t take the values i = 1, . . . , N
and t = 1, . . . , T, respectively.3 Making use of the global market clearing condition we see that
pt =
1
ϕd −ϕs
`
uSt + λ′
Sηt −εt
˘
,
(3)
which makes the simultaneity clear, e.g., that prices are composed of size-weighted idiosyncratic shocks,
aggregate supply shocks and the demand shock. The objective of the GIV methodology is to extract the
idiosyncratic shocks and use them as instruments for price.
Demand estimation in the case of uniform loadings (λi = λ ∀i). To momentarily fix ideas, it is
helpful to consider a major simplification when constructing the instrument. Suppose that the loadings are
uniform, λi = λ ∀i. Then, the instrument, zt, can be formed as
zt = ySt −1
N
N
X
i=1
yit = (ϕdpt + λ′ηt + uSt) −(ϕdpt + λ′ηt + 1
N
N
X
i=1
uit),
= uSt −1
N
N
X
i=1
uit := uΓt,
(4)
where Γ := S −ι/N is an N × 1 random vector such that ι′Γ = PN
i=1 Γi = 0, by construction. Γi is
random because we assume the shares follow a fat-tailed distribution, see Assumption 4. Identification and
estimation of demand by GIV requires that
E(ztεt) = E
˜ N
X
i=1
ΓiE(uitεt|Γ)
¸
= 0.
(5)
(5) is our exogeneity condition and (3) gives E(ztpt)̸ = 0, relevance. A sufficient condition for the mo-
3As oil is a storable good, one could easily allow oil prices to adjust to the gap between supply and demand, e.g. as in Mohaddes
and Pesaran (2016). This introduces more complex notations without adding any substance to the main points of the paper.
5


---

ment condition in (5) to be zero is E(uitεt|Γ) = 0, which effectively requires that conditional on size,
uit and εt are uncorrelated. Given relevance, exogeneity implies the following demand elasticity estimator
pϕd =
P
t dtzt
P
t ptzt . Intuitively, zt places larger weights on the idiosyncratic shocks to larger oil producers, these
granular shocks will shift the supply curve while keeping the aggregate demand curve fixed since demand
responds to these shocks only through their affects on prices. This allows for consistent estimation of the de-
mand elasticity. The uniform loadings assumption in this case tremendously facilitate the analysis. Uniform
loadings allow one to construct the instrument, as in (4), from observables. In practice, uniform loadings
are quite restrictive and we subsequently relax this assumption. However, before moving on to the general
case, we also illustrate supply estimation under simplifying assumptions to fix ideas.
Supply estimation in the case of uniform loadings and uit i.i.d. Continuing on with the uni-
form loadings case, remarkably, GK show that one can use the same instrument, zt, to also estimate the
supply elasticity using a cross-sectionally aggregated supply equation. Now, GK further assume that uit
are i.i.d., E(u·tu′
·t) := Σu = σ2
uIN, where u·t :=
´
u1t
. . .
uNt
¯′
and IN is the identity matrix and
define the N × 1 precision weight vector E := Σ
−1
u ι
ι′Σ
−1
u ι which reduces to ι/N when uit are i.i.d. across i.
Aggregation of the supply equation is performed using the vector E, we have that yEt = ϕspt +λ′ηt +uEt.
Identification and estimation of supply by GIV requires that the instrument satisfies exogeneity with respect
to the composite error term4
E((λ′ηt + uEt)zt) = 0.
(6)
The first term in (6) has similar interpretation as in (5), i.e., size-weighted idiosyncratic supply shocks are
uncorrelated with the aggregate supply component, λ′ηt. Miraculously, the second term is exactly zero
E(uEtzt) = E(E′u·tu′
·tΓ) = E(E′E(u·tu′
·t|Γ)Γ) = σ2
u
N E(ι′Γ) = 0.5
(7)
The moment condition (7) is zero due to independence of Γi and uit by assumption and the sum-to-zero
property of Γ. For identification with large N, we assume size to follow a power law in tail (see Assumption
4), thus Γi is stochastic and assumed to be independent of uit.6 So again, we have E(ztpt)̸ = 0 and for this
simplified example, we avoid the need to estimate the factor structure since (i) due to uniform loadings, zt
4In the general case to follow, we estimate the factors and thus only exploit E(uEtzt) = 0 to estimate ϕs.
5One may wonder then why this particular form of Γ was selected. Appealing to Proposition 3 in GK, they establish that
Γ = S −E, for this example, turns out to be the optimal weight vector, amongst the class of weights which sum-to-zero. Γ is
optimal in the sense that it minimizes the asymptotic variance of the structural parameters.
6For a fixed N, it is not required to assume independence of Γi and uit because Γi can be treated as constant and (7) is zero
solely by virtue of the fact that ι′Γ = 0.
6


---

is constructed from observables and (ii) zt is uncorrelated with the composite error term. If either of (i) or
(ii) fails to hold, estimation of the factor structure becomes a preliminary step, as in our general procedure.
Nevertheless, (6) leads to the following simple supply elasticity estimator pϕs =
P
t yEtzt
P
t ptzt . The intuition here
is that, again, zt places larger weights on the idiosyncratic shocks to larger oil producers, these granular
shocks keep the simple average (or more generally precision-weighted, i.e., weighted heavily towards more
stable oil producers) supply curve fixed. That is, on average, precision-weighted supply responds to these
granular shocks only through their effects on prices (due to E((λ′ηt + uEt)zt) = 0) and at the same time
since smaller oil producers take as given price changes caused by these granular shocks, it will shift their
supply curves which enables consistent estimation of the supply elasticity.
Discussion. In the case of uniform loadings and uit i.i.d., the vector E and the instrument are con-
structed from observables, the large sample properties of pϕs and pϕd only entail fixed N, large T asymptotics
for which GK have laid out. In general, however, the cross-section will need to be exploited to estimate E
since one can not know if uit are i.i.d. across i. Indeed, the factors typically take care of a substantial portion
of the cross-sectional correlations but it is prudent to allow for cross correlations in uit since the exogeneity
condition for estimation of the supply elasticity heavily exploits the structure of Σu. Therefore, it will be
important to generally allow for some weak cross correlations in Σu, which our algorithm accommodates,
as discussed in Section 3 and Section 4.
Moreover, although homogeneous loadings was only an abstraction to illustrate the instrument, GK ad-
vocate the use of yΓt = ySt −1
N
P
i yit in practice even when the loadings are not uniform. In the general
heterogeneous loadings case, their instrument becomes
Zt := yΓt = uΓt + λ′
Γηt.
(8)
They label this instrument with a capital case convention, to distinguish it because it is no longer solely com-
posed of weighted idiosyncratic shocks, uΓt, as the λ′
Γηt term is contaminating the instrument. However,
this clever formulation is possible because they advocate estimation of the factors in practice, which they
augment to their structural equations, thereby controlling for the second term which can potentially make
their moment conditions different from zero.
3.
Feasible Granular Instrumental Variables
Homogeneous loadings are overly restrictive but relaxing this can be easily accommodated in practice
via PCA or iterative OLS-PCA methods, e.g., Bai (2003) or Bai (2009) in a preliminary stage to construct an
7


---

estimate of the instrument.7 Although in GK’s asymptotic theory they assume homogeneous loadings and
that the instrument is exogenous with respect to the composite error, which circumvents the need to estimate
the factor structure, they indeed advocate augmenting their structural equations with estimated factors ei-
ther via period-by-period cross sectional regressions when the loadings are known or via PCA in the case of
non-parametric (unknown) loadings. GK abstract away from the sampling error in suggesting the use of aug-
mented factors, which only vanishes for both large N and T. Bai and Ng (2006) and Greenaway-McGrevy
et al. (2012) have developed the asymptotic distribution for structural parameters in factor augmented re-
gressions in time series and panel models respectively. In this paper, a variant of their corresponding result
is established in showing the sampling error from estimating the high dimensional precision matrix, the
factors, as well as the instrument is negligible in the asymptotic distribution of the structural parameters.
The general heterogeneous loadings case and uit non-i.i.d. Now we formulate the estimation
approach in the general case, which makes much heavier use of the cross-section. When we cross-sectionally
demean the supply equation and stack across i we obtain (recall Ă
X denotes a generic demeaned variate)
ry·t = rΛηt + ru·t,
(9)
which is estimable with vanilla PCA when the factor structure is strong.8 Letting Q = (IN−rΛ(rΛ′ rΛ)−1 rΛ
′),
then Qry·t = Qru·t, completely purges the process of the common factors through the loading space. Pre-
multiplying the share weights gives the instrument
zt := S′Qry·t,
(10)
= S′Qru·t := Γ′ru·t,
(11)
where Γ := QS is unknown because Q is unknown, but Q is easily estimated from data. Once we have p
Q,
which just replaces rΛ with prΛ , we form pzt = S′ p
Qry·t from observables. Importantly, when λi = λ ∀i, then
Γ = (IN −rΛ(rΛ′ rΛ)−1 rΛ
′)S = S −ι/N as in the previous case with homogenous loadings. This gives
7For our theory, we assume a balanced panel. However, in the case of unbalanced panels with data missing at random (which
is beyond the scope of this paper) one can instead use the Bai et al. (2015) method or Bai and Ng (2021b) method to estimate
the factor structure and the instrument. In the more realistic case where data are not missing at random, one can use the methods
developed in Xiong and Pelger (2019). Remark?
8Strong factors in the sense that Λ′Λ/N
p→ΣΛ > 0; thus we assume the factors are strong/pervasive in the sense that a
significant fraction of cross-sectional units are affected by their presence. Consistent estimation of weak factors is beyond the scope
of this paper, see for example Onatski (2012), Bailey et al. (2016) or Freyaldenhoven (2021) for suitable conditions for which it
is possible. Even when estimable, their convergence rates are slower relative to estimates of strong factors, e.g., see Bai and Ng
(2021a). This will generally require modifications to the limiting distributions we derive in this paper.
8


---

rise to a more general demand elasticity estimator
pϕd = pϕd(pz) =
P
t dtpzt
P
t ptpzt
.
(12)
In Section 6, we show that the demand elasticity can be estimated as if the infeasible instrument, zt, is used.
In the case of the supply elasticity, the estimator will additionally depend on the estimated (potentially
high dimensional) precision matrix. That is, pϕs = pϕs(pz, pΣ
−1
u ). This creates the need to jointly estimate
pΣ
−1
u
to form p
E in order to aggregate the panel to estimate pϕs. We propose a simple iterative procedure and
show that the supply elasticity can be estimated as if the infeasible precision matrix, Σ−1
u , and instrument,
zt, were used. More specifically, let yEt = ϕspt + λ′
Eηt + uEt := f ′
tθs + uEt, where θs =
´
ϕs
λ′
E
¯′
and f t =
´
pt
η′
t
¯′
are (1 + r) × 1 vectors. The remarkable result E(ztuEt) = 0, shown in (7) for
the previous simple example with homogeneous loadings, continues to hold in this setting as well, with
zt = S′Q˜y·t = S′Q˜u·t and Γ = QS (recall that ι′Γ = 0)
E(uEtzt) = E
`
E′u·t˜u′
·tΓ
˘
= E(E′u·t(u·t −¯utι)′Γ) = E(E′u·tu′
·tΓ) −E(E′u·t¯utι′Γ)
= E(E′ E(u·tu′
·t|Γ)Γ) −0 =
1
ι′Σ−1
u ιE
`
ι′Γ
˘
= 0.
(13)
So we have that (where the estimated factors self-instrument)
E
«˜
zt
ηt
¸
· uEt
ff
= E
«˜
zt
ηt
¸
·
`
yEt −ϕspt −λ′
Eηt
˘
ff
= 0.
(14)
However, given our interest lies in inference for ϕs, it is useful to stack over t, yE = p ϕs+η λE+uE, where
yE, p, and uE are T × 1 vectors and y pE is the feasible counterpart of yE. Let M pη = (IT −pη(pη′ pη)−1pη′),
then it follows from standard partitioned regression results that
pϕs = pϕs(pz, pΣ
−1
u ) = pz
′ M pη y pE
pz
′ M pη p
.
(15)
As pΣ
−1
u
depends on pϕs, (15) generally requires an iterative estimation procedure. To that end, note that if ϕs
were known, yit −ptϕs = λ′
iηt +uit follows an approximate factor structure. Thus, a covariance estimator,
pΣu, for the idiosyncratic part can be obtained following Fan et al. (2013) by applying thresholding to the
eigenvalue decomposition, 1
T
PT
t=1(y·t −ιptϕs)(y·t −ιptϕs)′ = PN
i=1 γiξiξ′
i, where γi and ξi are the
eigenvalues (sorted in decreasing order) and corresponding eigenvectors, respectively. More specifically, if
9


---

ϕs were known, we have
pΣ(y·t−ιptϕs) :=
r
X
i=1
pγi pξi pξ
′
i + pΣu
T ,
(16)
where pΣ
T
u = PN
i=r+1 pγi pξi pξ
′
i = (pσT
u,ij)N×N,
pσT
u,ij =





pσu,ii,
i = j,
hij(pσu,ij),
i̸ = j,
(17)
and hij(·) is a generalized shrinkage function of Antoniadis and Fan (2001).9 Of course, ϕs can not be
known as it requires an estimate of Σ−1
u . Thus, we now address joint estimation of ϕs and Σ−1
u
in what fol-
lows and subsequently establish that the sampling error in p
E is negligible given some regularity conditions.
The iterative procedure is summarized in Algorithm 1 presented below.
Algorithm 1 FGIV for ϕs (when kx = 0):
• Step 1: Run PCA on (9) and obtain pzt = S′ p
Qry·t as the sample counterpart of (10).
• Step 2: Initialize pΣ
−1
u
= IN.
• Step 3: Obtain y pE(pΣ
−1
u ) and pϕs(pz, pΣ
−1
u ) as in (15).
• Step 4: Update pΣ
−1
u
by inverting pΣ
T
u defined in (17), y pE(pΣ
−1
u ) and pϕs(pz, pΣ
−1
u ).
• Step 5: Iterate Step 3 and Step 4 until convergence.
When r is unknown, one can augment Step 1 and estimate r using a procedure as in Bai and Ng (2002),
Onatski (2010) or Ahn and Horenstein (2013); we use the ER and GR methods of Ahn and Horenstein
(2013) (hereafter AH). For more details of the ER and GR methods, see Section C of the Supplementary
Appendix.
FGIV algorithm accommodating cross-section specific covariates. When kx̸ = 0 then the
demeaning transformation from (9) results in ry·t = rΛηt + rx·tβ + ru·t, where rx·t is an N ×kx matrix, which
leaves
β
kx×1
as an additional parameter to estimate. β can be easily estimated by adapting the procedure of
Bai and Liao (2017), which is generalizing Bai (2009), to handle endogeneity of prices even after controlling
9Examples of hij(·) include hard thresholding hij(x) = x1(|x|≥τij) and soft thresholding hij(x) = sgn(x)(|x|−τij)+. The
entry dependent threshold, τij > 0, can be defined as CωT
a
pαij, where pαij = 1
T
PT
t=1(puitpujt−pσu,ij)2, pσu,ij = 1
T
PT
t=1 puitpujt
and puit = yit −ϕspt −pλ
′
i pηt for some predetermined decreasing sequence ωT > 0 and C > 0. The choice of C can be data
driven; Fan et al. (2013) choose C through multifold cross-validation to maintain positive definiteness of pΣ
T
u (C). In our algorithm
below, we make use of the R package for POET, written by the authors Fan et al. (2013).
10


---

for latent common factors. More specifically,
β(rΛ, ηt, Σ−1
u ) =
˜ T
X
t=1
rx′
·tΣ−1
u rx·t
¸−1
T
X
t=1
rx′
·tΣ−1
u (ry·t −rΛηt),
(18)
(ry·t −rx·tβ) = rΛηt + ru·t,
(19)
since (19) follows a factor structure, the T ×r factor matrix, η(β, Σ−1
u ), can be estimated using the principal
components estimator whose columns are the eigenvectors corresponding to the largest r eigenvalues of the
T ×T matrix (ry··−rx··(β))Σ−1
u (ry··−rx··(β))′, where the T ×N matrix rx··(β) :=
´
rx1·β
. . .
rxN·β
¯
and
rΛ(β, Σ−1
u ) = 1
T
PT
t=1(ry·t −rx·tβ)η′
t(β, Σ−1
u ). Thus, to deal with general (strictly exogenous) covariates,
xit, Algorithm 2 can be applied.
Algorithm 2 FGIV for ϕs (when kx̸ = 0):
• Step 1: Initialize pβ = 0, pΣ
−1
u
= IN.
• Step 2: Run PCA on (19) to obtain pηt( pβ, pΣ
−1
u ) and prΛ( pβ, pΣ
−1
u ) as explained above.
• Step 3: Update pβ as the sample counterpart of (18).
• Step 4: Obtain pzt = S′ p
Q(ry·t −rx·t pβ).
• Step 5: Initialize y pE(pΣ
−1
u ) and pϕs(pz, pΣ
−1
u ) =
´
pz
′ M pη p
¯−1
pz
′ M pη (y pE −xi·β).
• Step 6: Update pΣ
−1
u
by inverting pΣ
T
u defined in (17), where pγi and pξi are the eigenvalues and eigen-
vectors (sorted in decreasing order) corresponding to the sample analog of
1
T
PT
t=1(y·t −ιptϕs −x·tβ)(y·t −ιptϕs −x·tβ)′ respectively.
• Step 7: Iterate Step 2 through Step 6 until convergence.
When r is unknown, one can augment Step 2 and iteratively estimate r using the ER and GR methods of
Ahn and Horenstein (2013).
The main takeaway is that when both (N, T) are large, one can generalize the GIV estimators proposed
by GK along different dimensions; here we accommodate latent heterogeneous loadings, latent factors and
latent precision matrix (e.g., uit can be weakly cross-correlated and heteroskedastic). As mentioned earlier,
we call the proposed estimators of the elasticities in (12), Algorithm 1 and Algorithm 2 as FGIV estimators.
Remark 1 In principle, the theory for the estimators proposed in this paper allows for N ≫T. This case is
relevant in many empirical settings (e.g., empirical industrial organization and finance). However, it may be
beneficial to avoid estimating the precision matrix for cases where N ≪T (e.g., empirical macro). But, as
(7) and (13) show, to have a valid instrument for which the moment equation is exactly zero, we must specify
11


---

Σu correctly. This is the primary motivation for estimating the general precision matrix in Algorithms 1
and 2. In order to avoid estimating the precision matrix, we must assume (potentially erroneously) uit are
cross-sectionally independent. We now analyze the consequences of making this assumption when in fact
uit are cross-sectionally correlated. Suppose we erroneously assume cross-sectional independence, then the
vector E reduces to ι/N and we end up with the following moment equation
E(uEtzt) = E
`
E′u·t˜u′
·tΓ
˘
= E(E′u·t(u·t −¯utι)′Γ)
= E(E′E(u·tu′
·t|Γ)Γ) −E(E′u·tι′Γ)¯ut = 1
N E(ι′ΣuΓ) −0 = o(1).
(20)
Hence, zt is not a valid instrument in the traditional sense because we allow E(uEtzt)̸ = 0 for any given
sample. Nevertheless, this moment converges to zero for large N. Indeed, the moment satisfies E(uEtzt) =
o p1q under our regularity assumptions, and thus, zt is asymptotically a valid instrument.10 This insight
reveals that this moment is approaching zero, hence it may prove to be beneficial to aggregate the panel,
yit, using weights ι/N regardless of the covariance structure. The immediate implication is that pϕs =
pϕs(pz, IN), so there is no need for an algorithmic estimation procedure, the simple analytical formula for the
supply elasticity estimator with potentially misspecified covariance structure for uit is given by pϕs(pz, IN) =
pz
′ M pη ¯y
pz
′ M pη p, where ¯y stacks ¯yt =
1
N
PN
i=1 yit for each t = 1, . . . , T; this estimator is essentially Step 2 and
Step 3 of Algorithm 1. Asymptotically, it holds that pϕs(pz, pΣ
−1
u ) = pϕs(pz, IN) + op(1). However, regarding
performance in finite samples, when uit are not i.i.d. and when N ≪T, it is not clear ex-ante if pϕs(pz, IN)
will outperform pϕs(pz, pΣ
−1
u ). When N ≫T one would expect ex-ante that pϕs(pz, IN) will be less efficient
than pϕs(pz, pΣ
−1
u ) since the former is not optimally weighting the observations, whereas the latter is. When
uit are indeed i.i.d. we would expect pϕs(pz, IN) to perform better.11
4.
Efficient GMM Estimation: Factor-Augmented FGIV
We now proceed to overidentify the elasticities, which yields overidentified FGIV estimators. We will
refer to the overidentified FGIV estimators simply as efficient GMM estimators and the just identified FGIV
estimators simply as FGIV estimators. It will be of interest to practitioners to see if overidentification is pos-
sible for the supply and demand equations. In this section, we show that the system is indeed overidentified
10It can be shown that ι′ΣuΓ = ι′ΣuQS ≤ι′ΣuSγmax(Q) = P
i,j σu,ijSj ≤
´P
i,j σ2
u,ij
¯1/2
||S||2
2= ||Σu||F ||S||2
2≤
||Σu||1||S||2
2≤O(mN)Θp(1) = o(N)Θp(1) = o(N), where mN is defined in Assumption 3 and mN = o(N).
11In unreported simulations where N ≪T and uit are non-i.i.d., we find that pϕs(pz, pΣ
−1
u ) typically has a smaller bias than
pϕs(pz, IN) (in absolute terms, the bias of both estimators are very small) but with a slightly larger variance.
12


---

to varying degrees for the supply and demand equations.
Demand. It is common practice to assume uncorrelated aggregate supply and aggregate demand shocks,
that is E(ηtεt) = 0. When we are willing to entertain this, then our supply factors, estimated via principal
components, serve as valid instruments in estimation of the demand elasticity, rendering an overidentified
parameter. In fact, the theory for using principal components as instruments was laid out in Bai and Ng
(2010) under strong instrument asymptotics, as well as Kapetanios and Marcellino (2010) under many/weak
instrument asymptotics. In the remainder of this section, we let the GIV be denoted as zt,GIV := zt to
distinguish it from the full instrument vector we introduce with upper case conventions. Our full instrument
matrix for the demand equation is
Zd
T×(1+r)
:=
´
zGIV
η
¯
with E(Zdtεt) = 0; Zdt simply augments
factors to be used as instruments. Making use of the (1+r)×1 dimensional moment condition, the efficient
GMM demand elasticity estimator is defined as
pϕd
GMM = argmin
ϕd
ε′Zd
T
W d
Z′
dε
T ,
=
ˆ
p′ pZd pΩ
−1
d
pZ
′
dp
˙−1
p′ pZd pΩ
−1
d
pZ
′
dd,
(21)
where
W d
(1+r)×(1+r)
is an arbitrary positive definite weight matrix, but is optimally set as x
W d = pΩ
−1
d , where
pΩd =
1
T
PT
t=1 pZdt pZ
′
dt(dt −ptpϕd
2SLS)2. It is clear that (21) nests the FGIV estimator for the demand
elasticity as a special case. In this sense, pϕd
GMM will be robust to scenarios where zt is weaker.
Supply. In the same vein, the supply elasticity can always be overidentified given our identifying as-
sumptions because E(εtuEt) = 0 and thus εt can serve as an additional instrument. To estimate the entire
parameter vector for the supply equation, let
Zs
T×(2+r)
:=
´
zGIV
ε
η
¯
, where the augmented factors
self-instrument as they are part of the supply equation. Then yE = fθs + uE and recall θs =
´
ϕs
λ′
E
¯′
and f t =
´
pt
η′
t
¯′
are (1 + r) × 1 vectors and the matrix f is T × (1 + r), which stacks f t. We have
E(ZstuEt) = 0; hence, making use of the (2 + r) × 1 dimensional moment conditions, the efficient GMM
supply elasticity estimator is defined as
pθ
s
GMM = argmin
θ
s
u′
EZs
T
W s
Z′
suE
T
,
=
ˆ
p
f
′ pZs pΩ
−1
s
pZ
′
s p
f
˙−1
p
f
′ pZs pΩ
−1
s
pZ
′
sy pE.
(22)
where
W s
(2+r)×(2+r)
is an arbitrary positive definite weight matrix, but is also optimally set as x
W s = pΩ
−1
s ,
13


---

where pΩs =
1
T
PT
t=1 pZst pZ
′
st(y pEt −pf
′
t pθ
s
GMM)2.12 It is clear that (22) nests the FGIV estimator for the
supply equation as a special case. As in the just identified case in (15), pθ
s
GMM in (22) depends on pΣ
−1
u ,
hence, will generally require an iterative estimation procedure. Algorithm 3 below generalizes Algorithm 1
by extending the joint estimation of the supply elasticity estimator and the precision matrix to the overiden-
tified case for when kx = 0. In view of Algorithm 2, Algorithm 3 can be further extended to the case when
kx > 0, but we omit the details for brevity.
Algorithm 3 Efficient GMM for ϕs (when kx = 0):
• Step 1: Run PCA on (9) and obtain pzt = S′ p
Qry·t as the sample counterpart of (10).
• Step 2: Initialize pΣ
−1
u
= IN.
• Step 3: Estimate (21) to obtain pε, initialize x
W s = ( pZ
′
s pZs)−1 and obtain pθ
s
2SLS( pZs, pΣ
−1
u ).
• Step 4: Obtain y pE(pΣ
−1
u ).
• Step 5: Update x
W s =
´
1
T
PT
t=1 pZst pZ
′
stpu2
pEt
¯−1
, where pu pEt = y pEt −pθ
s
GMM( pZs, pΣ
−1
u )′ p
f t and
construct pθ
s
GMM( pZs, pΣ
−1
u ) as the sample counterpart of (22).
• Step 6: Update pΣ
−1
u
by inverting pΣ
T
u defined in (17).
• Step 7: Iterate Step 4 through Step 6 until convergence.
In addition to efficiency gains, the efficient GMM estimators exhibit superior finite sample properties and
are also robust to the GIV itself being a weak instrument. We illustrate these points in greater detail in
Remark 5 and Section 7.
The intuition for the overidentified estimators can be seen from observing the reduced form equation
for (equilibrium) prices, pt =
1
ϕd−ϕs
`
uSt + λ′
Sηt −εt
˘
. Clearly E(ptηt)̸ = 0 and E(ptεt)̸ = 0 and so
instrumental relevancy is established. Thus, we are effectively back to the classical approach of finding
exogenous supply shifters, in this case εt, to estimate the supply elasticity and finding exogenous demand
shifters, in this case ηt, to estimate the demand elasticity. With the exception that these shifters, ηt and εt
are unobserved. In what follows, we show that estimating ηt and εt has a negligible effect on the limiting
distributions of the estimators of demand and supply elasticities, respectively.
5.
Assumptions
Below we lay out the assumptions needed to derive our main results. Assumption 1, Assumption 2 and
Assumption 3 are standard in the literature; see, for example, Bai (2003), Fan et al. (2013) and Bai and Liao
12In the case of the demand elasticity estimator in (21) we use 2SLS residuals to construct pΩd. However, we implement (22)
via Algorithm 3 which, by iteration, renders the residuals used to construct pΩs to be GMM residuals.
14


---

(2017), but are relevant for a thorough understanding of the subsequent theorems. Whereas, Assumption 4
parts ii.) and iii.) are new so we provide more details.
Assumption 1 (Factor Error Structure) The composite error term in (2) is assumed to admit an (approx-
imate) factor structure representation vit := λ′
iηt + uit, where ηt =
´
η1t
. . .
ηrt
¯′
is an r × 1 vector of
latent common factors and λi =
´
λ1i
. . .
λri
¯′
is an r × 1 vector of latent factor loadings. We assume
the factors are pervasive in the sense that Λ′Λ/N converges to some r × r positive definite matrix.
Assumption 2 (Strict Stationarity, Exponential Tails & Strong Mixing)
(A2i.) {ηt, uit, εt}t≥1 is strictly stationary and each with a zero mean.
(A2ii.) ∃c1, c2 > 0 with γmin(Σu) > c2, max
j≤N||γj||< c1, c2 < γmin(cov(ηt)) ≤γmax(cov(ηt)) < c1.
(A2iii.) Exponential tail: ∃r1, r2 > 0 and b1, b2 > 0, such that for any s > 0, i ≤N and j ≤r,
P(|uit|> s) ≤exp(−(s/b1)r1)), and P(|ηt,j|> s) ≤exp(−(s/b2)r2)).
(A2iv.) Strong Mixing: ∃r3, C > 0 ∀T > 0, r−1
1
+ r−1
2
+ r−1
3
> 1,
sup
A∈F 0
−∞, B∈F ∞
T
|P(A)P(B) −
P(AB)|< exp(−CT r3), where F0
−∞and F∞
T denote the σ-algebras generated by {(ηt, uit, εt) : t < 0}
and {(ηt, uit, εt) : t > T} respectively.
Assumption 3 (Sparsity on Σu) Let Σu = (σu,ij), for some q ∈[0, 1/2), define
mN = max
i≤N
N
X
j=1
|σu,ij|q.
(23)
We require that there is q ∈[0, 1/2) such that mNω1−q
N,T = o(1), where ωN,T =
b
log(N)
T
+
1
?
N .
Assumption 4 (Identification by GIV)
(A4i.) E(ztuEt) = E(ztεt) = E(ZstuEt) = E(Zdtεt) = 0.
(A4ii.) The sizes S1, . . . , SN are drawn i.i.d. from an arbitrary distribution for which the tail of the size
distribution (i.e. above some threshold) follows a power law, with tail index, µ > 0
P(S > s) = cs−µ.
The tail index µ determines the probability of observing extreme values. We assume that Si is independent
of uit.
(A4iii.) Suppose the sizes are ordered in decreasing fashion as such: S(1) ≥S(2) ≥. . . ≥S(N−1) ≥S(N),
15


---

and we partition the cross-section as, Ndominant := {1, . . . , N1} and Nfringe := {N1 + 1, . . . , N} such
that Ndominant ∪Nfringe := Nfull. Let Si =
Si
PN
j=1 Sj denote the normalized shares such that P
i Si = 1.
We assume ∀i ∈Ndominant, Si = Θp(1), and ∀i ∈Nfringe, Si = Op
` 1
N
˘
. We further assume that the
cardinality of the dominant units is fixed as N →∞, that is, |Ndominant|= N1 and N1 does not rise with
N while the cardinality of the fringe grows with N, |Nfringe|= N −N1 →∞as N →∞.
Remark 2 The first condition gives us instrumental exogeneity for the FGIV and efficient GMM estimators.
The second condition allows for instrumental relevance in the extension of a large N framework. An im-
portant implication of the second condition is that the Herfindahl index, hN,µ, has the following asymptotic
property
a
hN,µ = ||S||2 =





Θp p1q
for
µ ∈(0, 1),
Op pgN,µq
for
µ ∈[1, 2),
with Op pgN,µq ≫1/
?
N. The variance of the just identified estimators is inversely proportional to the
Herfindahl index, that is V(pϕj
FGIV ) = O(h−1
N,µ) for j = s, d, reflecting the fact that the more concentrated
the market, the more precise the GIV methodology will be and also reflecting the fact that if the Herfindahl
converges to zero in the limit, the variance will diverge.13 However, if µ is slightly greater than 1, theoret-
ically identification breaks down for large N but in any finite sample the GIV could be relevant (precisely
due to Op pgN,µq ≫1
?
N). Nevertheless, we rule this case out for the purpose of asymptotic inference.14
Note, that the third condition is consistent with µ ∈(0, 1), but is slightly stronger. The third condition
is also a generalization of the so-called "granular" weights in the panel data literature, say w
N×1, which are
typically assumed to satisfy ||w||2= O
´
1
?
N
¯
and
wi
||w||2 = O
´
1
?
N
¯
∀i. The third condition allows the
share vector to be partitioned into a dominant part and a fringe part. That is, S =
´
S′
d
S′
f
¯′
where Sd
is N1 × 1, is the dominant part and Sf is N2 × 1, is the fringe part; with N1 + N2 = N, the key being
that N1(N) = N1 is fixed while N2(N) →∞as N →∞. This assumption can be empirically justified
in concentrated markets, see Section 9 as an example; as well as mathematically justified, see Logan et al.,
1973.
Remark 3 Taking the variance of the equilibrium price process (assuming the covariances to be zero for
simplicity) we obtain V(pt) =
1
(ϕd−ϕs)2 (V(uSt) + V(λ′
Sηt) + V(εt)) = Θ(1), where the last equality
13The derivation of the asymptotic behavior of hN,µ can be found in Supplementary Appendix B.
14For more details on instrumental relevance for large N, see Section 7.
16


---

follows by the second and the third conditions in Assumption 4, details can be found in Lemma 1 in the
Appendix. Without these conditions, one would obtain the unsatisfactory result that V(pt) = O(N), that is,
the variance of the price process is unbounded for each t as N →∞. Effectively, Assumption 4 allows the
coexistence of a finite number of dominant units, in terms of size, whose cardinality can not grow with N,
while at the same time allowing for a bounded variance for the aggregate endogenous variable pt.
6.
Limiting Distributions
In this section, we first present the limiting distributions of the FGIV elasticity estimators, corresponding
to (12) and (15) with Algorithm 1. We then move on to the limiting distributions of the efficient GMM
elasticity estimators, corresponding to (21) and (22) with Algorithm 3.
Just identified demand elasticity. The just identified demand elasticity estimator in (12) is given by
pϕd(pz) =
PT
t=1 pztdt
PT
t=1 pztpt
=
PT
t=1
P
i,j Si pQij ˜yjtdt
PT
t=1
P
i,j Si pQij ˜yjtpt
.
Hence,
pϕd −ϕd =
˜X
t
pztpt
¸−1 ˜X
t
pztεt
¸
,
=
˜
T −1 X
t
ztpt + T −1 X
t
(pzt −zt)pt
¸−1 ˜
T −1 X
t
ztεt + T −1 X
t
(pzt −zt)εt
¸
.
From above, it is apparent we need to show 1
T
PT
t=1(pzt −zt)εt = 1
T
PT
t=1 S′( p
Q −Q)˜y·tεt = op(1) and
1
T
PT
t=1(pzt −zt)pt = 1
T
PT
t=1 S′( p
Q −Q)˜y·tpt = op(1). Indeed, we show in Lemma 2, in the Appendix,
that
T −1
T
X
t=1
S′( p
Q −Q)˜y·tεt = Op(C−2
NT ) + Op(C−2
NT ) · Op
ˆN
T
˙
+ Op
ˆ 1
?
N
· C−1
NT
˙
,
(24)
T −1
T
X
t=1
S′( p
Q −Q)˜y·tpt = Op(C−2
NT ) + Op(C−2
NT ) · Op
ˆN
T
˙
+ Op
ˆ 1
?
N
· C−1
NT
˙
,
(25)
where CNT := min{
?
N,
?
T}. The terms in (24) and (25) are op(1) when N < T without any restrictions;
however, when T < N we require the mild restriction that N/T 2 →0, i.e., if T < N, T 2 does not grow
17


---

too slowly relative to N. Thus, making use of (24) and (25) we obtain
pϕd −ϕd =
˜X
t
pztpt
¸−1 ˜X
t
pztεt
¸
=
˜
T −1 X
t
ztpt
¸−1
T −1 X
t
ztεt + op(1).
(26)
The order of the sampling error generally relies, in part, on the order of the Herfindahl. The order of the
Herfindahl, in turn, critically depends on µ, the tail index of the size distribution (see Remark 2). Results on
the order of the Herfindahl as a function of the tail index parameter µ entails a total of six possible cases.
The results can be found in Table 6 of Supplementary Appendix B. However, for inference, we require
µ ∈(0, 1) (regularly varying tails) or µ →0 (slowly varying tails) as discussed in detail in the previous
section’s remarks. Given this, even after pinning down the order of the Herfindahl, the panel dimensions can
distinguish more cases as seen above. Nevertheless, as (24), (25) and (26) indicate, for consistency we have
the following result:
Theorem 1 (Consistency of pϕd) Under Assumptions 1-4, as (N, T)
j→∞, we have that when N ≥T and
N/T 2 →0 or when N < T
pϕd −ϕd
p→0.
(27)
All proofs are deferred tot the appendix. Now, multiplying (26) by
?
T
?
T(pϕd −ϕd) =
˜
T −1 X
t
ztpt
¸−1 ˜
1
?
T
X
t
ztεt + Op
˜ ?
T
C2
NT
¸
+ Op
˜
N
?
T · C2
NT
¸
+ Op
˜
?
T
?
N · CNT
¸¸
.
(28)
We can state the following result for the limiting distribution:
Theorem 2 (Limiting distribution for pϕd) Under Assumptions 1-4 as (N, T)
j→∞, we have that when
N ≥T, N/T 3/2 →0 and
?
T/N →0; or when N < T only
?
T/N →0
?
T(pϕd −ϕd) d→N p0, vdq ,
(29)
where vd := m−2
zp vzε, vzε := E(z2
t ε2
t ) and mzp := E(ztpt).
18


---

vzε can be consistently estimated with
pvzε =









T −1 PT
t=1 pz 2
t pε 2
t
HC,
T −1 PT
t=1 pz 2
t pε 2
t + 2 · T −1 Pm
j=1
ˆ
1 −
j
m + 1
˙ PT
t=j+1 pztpεtpzt−jpεt−j
HAC,
(30)
where HC and HAC denote heteroskedasticity-consistent and heteroskedasticity and autocorrelation con-
sistent estimators, respectively.
Hence
?
T(pϕd−ϕd)
pv1/2
d
∼tdf
d→N(0, 1), where pv1/2
d
= pm−2
zp pv1/2
zε , with
pmzp = T −1 PT
t=1 pztpt also consistent for mzp. We will see in Section 8 that the asymptotic theory provides
good approximations to the finite sample distribution.
Remark 4 As in GK, we express vd as inversely related to the Herfindahl, hN,µ, as claimed in Remark 2, for
insights on the role of market concentration on precision of the GIV. Assuming conditional homoskedasticity
of εt and homoskedasticity of uit, we have that
vzε = E(z2
t ε2
t ) = σ2
ε · σ2
˜u · E(S′QS).
(31)
If λi = λ ∀i, then there is no need to purge the factor structure through the loading space. That is, a simple
cross-sectional demeaning transformation will suffice, Q = (IN −˜Λ(˜Λ′ ˜Λ)−1 ˜
Λ′) = (IN −ιι′
N ). We can
simplify equation (31) to (where we make use of the normalization that S′ι = 1)
vzε = σ2
ε · σ2
˜u ·
ˆ
E(S′S) −1
N
˙
= σ2
ε · σ2
˜u ·
ˆ
E(hN,µ) −1
N
˙
loooooooooooomoooooooooooon
E(z2
t )
,
whereas, mzp = E(ptzt) ∝E(z2
t ). Hence,
vd ∝σ2
ε · σ2
˜u ·
`
E(hN,µ) −1
N
˘
“
σ2
˜u ·
`
E(hN,µ) −1
N
˘‰2 =
σ2
ε
σ2
˜u ·
`
E(hN,µ) −1
N
˘.
(32)
Thus, the more concentrated the market, the more precise the estimator. See Section 7 for a more general
treatment.
Just identified supply elasticity. For the just identified supply elasticity estimator in (15), upon conver-
19


---

gence of Algorithm 1, we have that
pϕs −ϕs =
´
T −1pz
′ M pη p
¯−1
loooooooooomoooooooooon
p
A−1
T −1pz
′ M pη η · λ pE
loooooooooomoooooooooon
pB
+
´
T −1pz
′ M pη p
¯−1
T −1pz
′ M pη u pE
looooooomooooooon
pC
.
(33)
We can write the scalars pA, pB and pC as follows
pA = T −1z′ M η p + T −1(pz −z)′ M pη p
loooooooooomoooooooooon
a1
+ T −1z′ (M pη −M η) p
loooooooooooomoooooooooooon
a2
,
(34)
pB = T −1(pz −z)′ M pη ηλ pE
loooooooooooomoooooooooooon
b1
+ T −1z′ (M pη −M η) ηλ pE
loooooooooooooomoooooooooooooon
b2
,
(35)
pC = T −1z′ M η uE + T −1(pz −z)′ M pη u pE
looooooooooomooooooooooon
c1
+ T −1z′ (M pη −M η) u pE
looooooooooooomooooooooooooon
c2
+ T −1z′ M η (u pE −uE)
looooooooooooomooooooooooooon
c3
. (36)
It is shown in Lemma 3 of the Appendix that the terms ai, bi, cj are op(1) for i = 1, 2; j = 1, 2, 3, such that
pϕs −ϕs =
`
T −1z′ M η p
˘−1 `
T −1z′ M η uE
˘
+ op(1).
(37)
We can now state the following result:
Theorem 3 (Consistency of pϕs) Under Assumptions 1-4, as (N, T)
j→∞, we have
pϕs −ϕs
p→0.
(38)
Now, multiplying (37) by
?
T
?
T(pϕs −ϕs) =
`
T −1z′ M η p
˘−1
˜
z′ M η uE
?
T
+ Op
˜ ?
T
C2
NT
¸
+ Op
˜
?
T
?
NT · CNT
¸¸
+
`
T −1z′ M η p
˘−1
˜
Op
˜
N
?
T · C2
NT
¸
+ Op
˜
mNω1−q
N,T
?
T
¸¸
,
(39)
we can state the following result for the limiting distribution:
Theorem 4 (Limiting distribution for pϕs) Under Assumptions 1-4, as (N, T)
j→∞, we have that when
N ≥T, N/T 3/2 →0 and
?
T/N →0; or when N < T only
?
T/N →0
?
T(pϕs −ϕs) d→N p0, vsq ,
(40)
20


---

where vs := m−2
z˜p vzu, vzu := E(z 2
t (M η uE) 2
t ) and mz˜p = E(zt(M η p)t).
vzu can be consistently estimated with
pvzu =









T −1 PT
t=1 pz 2
t (M pη puE) 2
t
HC,
T −1 PT
t=1 pz 2
t (M pη pu p
E)2
t + 2 · T −1 Pm
j=1
ˆ
1 −
j
m + 1
˙ PT
t=j+1 pzt(M pη pu p
E)tpzt−j(M pη pu p
E)t−j
HAC.
(41)
Hence
?
T(pϕ s−ϕs)
pv 1/2
s
∼tdf
d→N(0, 1), where pv1/2
s
= pm−2
z˜p pvzu, with pmz˜p = T −1 PT
t=1 pzt(M pη p)t consistent
for mz˜p. We will see in Section 8 that asymptotic theory provides good approximations to the finite sample
distribution.
Overidentified demand elasticity. For the overidentified demand elasticity estimator in (21), recall
the estimated instrument matrix consists of pZd =
´
pzGIV
pη
¯
. For the strong factors, pη, estimated via
PCA, Bai and Ng (2010) showed that the generated regressors problem of Pagan (1984) does not arise
when both N and T are large. Thus, the sampling error in pη is negligible in consideration of the limiting
distribution of the overidentified demand elasticity estimate. In the previous section, we established that
estimation of pzGIV is also negligible under regularity, we can then use standard asymptotic theory to also
obtain asymptotic normality of the efficient GMM estimator in the case of demand since
pϕd
GMM −ϕd =
´
p′ pZd pΩ
−1
d
pZ
′
d p
¯−1
p′ pZd pΩ
−1
d
pZ
′
d ε,
=
´
p′ Zd Ω−1
d
Z
′
d p
¯−1
p′ Zd Ω−1
d
Z
′
d ε + op(1).
(42)
We can now state the following theorem:
Theorem 5 (Limiting distribution for pϕd
GMM) Under Assumptions 1-4, with E(εtηt) = 0 ∀t, as (N, T)
j→
∞, we have that when N ≥T, N/T 3/2 →0 and
?
T/N →0; or when N < T only
?
T/N →0
?
T(pϕd
GMM −ϕd) d→N
´
0, V(pϕd
GMM)
¯
,
(43)
where
V(pϕd
GMM) =
`
m′
Zdp Ω−1
d mZdp
˘−1 ,
(44)
with mZdp = E(Zdt pt) and Ωd = plim T −1 PT
t=1 pZdt pZ
′
dt(dt −ptpϕd
2SLS)2.
21


---

V(pϕd
GMM) can be consistently estimated using 2SLS residuals with
pV(pϕd
GMM) =
¨
˝p
′ pZd
T
pΩ
−1
d
pZ
′
d p
T
˛
‚
−1
,
(45)
where pΩd = T −1 PT
t=1 pZdt pZ
′
dt (dt −ptpϕd
2SLS)2. It is well known that V(pϕd
GMM) attains the semiparamet-
ric efficiency bound, as shown by Chamberlain (1987), which reduces to (44) in the linear model. Standard
overidentification tests can be carried out since
Jd = T ·
˜
T −1
T
X
t=1
Zdt εt(pϕd
GMM)
¸′
pΩ
−1
d
˜
T −1
T
X
t=1
Zdt εt(pϕd
GMM)
¸
d→χ2
dfd,
(46)
where the degrees of freedom is given by dfd = (1 + r) −kd = r and kd = 1 is the number of endogenous
regressors. We will see that simulation evidence shows that the size of the J-test is near the nominal size
when the true r is used and when rmax > r factors are used; which is important in empirical work when r
is typically estimated and it is generally known that an overestimate of r is preferred in order to prevent an
effect akin to omitted variable bias, see Moon and Weidner (2015) who formalize this notion.
Overidentified supply elasticity. The full instrument matrix for the overidentified supply elasticity
estimator in (22) consists of pZs =
´
pzGIV
pε
pη
¯
, (recall the factors self instrument here, as they are part
of the supply equation). We show that the sampling error in pZs is indeed negligible. This is again due to
both large N and T. As a result,
Ωs
(2+r)×(2+r)
= plim T −1 PT
t=1 pZst pZ
′
st(y pEt −p
f
′
t pθ
s
GMM)2 is sufficient
when constructing the efficient weighting matrix, even though it does not take the sampling error in our
estimate of ϕd into account (since pε = ε(pϕd
GMM)). That is
pθ
s
GMM −θs =
ˆ
f ′ pZs pΩ
−1
s
pZ
′
sf
˙−1
f ′ pZs pΩ
−1
s
pZ
′
suE,
=
´
f ′ Zs Ω−1
s
Z
′
sf
¯−1
f ′ Zs Ω−1
s
Z
′
suE + op(1).
(47)
We can now state the following theorem:
Theorem 6 (Limiting distribution for pθ
s
GMM) Under Assumptions 1-4, as (N, T)
j→∞, we have that
when N ≥T, N/T 3/2 →0 and
?
T/N →0; or when N < T only
?
T/N →0
?
T(pθ
s
GMM −θs) d→N
´
0, V(pθ
s
GMM)
¯
,
(48)
22


---

where
V(pθ
s
GMM) =
`
m′
Zsf Ω−1
s mZsf
˘−1 ,
(49)
with mZsf = E(Zstf ′
t) and Ωs = plim T −1 PT
t=1 pZst pZ
′
st(y pEt −p
f
′
t pθ
s
GMM)2.
V(pθ
s
GMM) can be consistently estimated using GMM residuals with
pV(pθ
s
GMM) =
¨
˝ p
f
′ pZs
T
pΩ
−1
s
pZ
′
s p
f
T
˛
‚
−1
,
(50)
where pΩs = T −1 PT
t=1 pZst pZ
′
st (y pEt −pf
′
t pθ
s
GMM)2. Just as in the case of the overidentified demand elas-
ticity estimator, (49) achieves the semiparametric efficiency bound. Overidentification tests can be carried
out since
Js = T ·
˜
T −1
T
X
t=1
Zst u pEt(pθ
s
GMM)
¸′
pΩ
−1
s
˜
T −1
T
X
t=1
Zst u pEt(pθ
s
GMM)
¸
d→χ2
dfs,
(51)
where the degrees of freedom are given by dfs = 2 −ks = 2 −1 = 1 and ks = 1 is the number of
endogenous regressors for the supply equation.
Remark 5 The asymptotic distribution of the FGIV and efficient GMM estimators of demand and supply
elasticities are established. However, the finite sample moments of these estimators, are unbounded to
different degrees. The extensive literature on the classic simultaneous equations model has documented
this result in many forms, see Mariano (1973), Hatanaka (1973), Sawa (1972), Takeuchi (1970), Ullah and
Nagar (1974), Sargan (1978), Fuller (1977) and Hillier and Srivastava (1981). A complete representation
of the above results was given by Kinal (1980). Kinal’s result for 2SLS states that, if the dependent variable,
explanatory variables and instruments are jointly normal, then E||pϕj
2SLS||m< ∞for m < ℓj −kj + 1,
j = d, s, where ℓj is the number of instruments and kj is the number of endogenous regressors.
Thus, the FGIV estimators for supply and demand exhibit no bounded absolute moments since ℓj = kj =
1, j = d, s. Whereas, the efficient GMM estimators exhibits ℓd −kd = (1 + r) −1 = r bounded absolute
moments in finite samples for the case of demand and ℓs −ks = 2 −1 = 1 bounded absolute moment in
finite samples for the case of supply. Hence, the efficient GMM elasticity estimators (overidentified FGIV
estimators) exhibit superior finite sample properties relative to their (just identified) FGIV counterparts. Of
course, in general, just identified instrumental variables estimators (with strong instruments) exhibit nice
23


---

properties asymptotically.
7.
Weak Instruments
The classical weak instruments framework introduced by Staiger and Stock (1997) has its analog in this
framework. Interestingly, here the "weak" aspect is partially linked to the Herfindahl index without making
the usual local-to-zero assumption as in Staiger and Stock (1997). Moreover, the traditional notion of local-
to-zero with
1
?
T scaling which matches the rate of convergence of the estimator need not necessarily apply
here for weak instruments to arise. More specifically, the locality to zero can be expressed as decaying
functions of N, except in the case of µ ∈(0, 1), which we require for inference under our maintained
strong instruments assumption; whereas the rate of convergence is at the
?
T rate. To make things more
clear, it is useful to see the reduced form, equilibrium price equation again. Recall from (3), we have that
pt =
1
ϕd −ϕs
`
uSt + λ′
Sηt −εt
˘
. Thus, it is clear that for finite N, Cov(pt, zt) > 0, which automatically
renders the GIV as relevant. However, for large N, writing zt = S′Q˜u·t we observe that
V(S′Q˜u·t) = E(S′QE(˜u·t˜u′
·t|Γ)QS) = E(S′Q Σ˜u QS),
(52)
where Σ˜u := E(˜u·t˜u′
·t). The term inside the expectation can be simplified to
S′Q Σ˜u QS = S′Q Σu QS + Op
`
N−1˘
≤S′QS γmax(Σu) + Op
`
N−1˘
≤S′S · γmax(Σu) · γmax(Q) + Op
`
N−1˘
= O p1q hN, µ + Op
`
N−1˘
,
(53)
where we make use of γmax(Σu) = O p1q and the fact that a symmetric idempotent matrix, such as Q, has
eigenvalues of 0 or 1 and so γmax(Q) = 1. Taken together, (52) and (53) imply
V(zt) ≤O p1q E(hN,µ) + O
`
N−1˘
.
(54)
As such, only when we are in a tail regime indexed by µ ∈(0, 1) do we avoid the locality to zero. For
example, when µ > 2, we have that V(S′Q˜u·t) ≤O p1q E(hN, µ>2) = O
` 1
N
˘
. As a result, when µ > 2,
we have that zt = S′Q˜u·t = Op
´
1
?
N
¯
, so our equilibrium price equation simplifies to the following large
24


---

N representation
pt =
1
ϕd −ϕs
`
λ′
Sηt −εt
˘
+ Op
ˆ 1
?
N
˙
.
(55)
This would render the GIV as very weak since Cov(pt, uSt) = Cov(pt, zt) = O
` 1
N
˘
. Note that the
Cov(pt, uSt) and Cov(pt, zt) are of the same order precisely because γmax(Q) = 1. (55) is effectively
the relationship that was exploited by Mohaddes and Pesaran (2016), who assumed the so-called "granular"
weights of order O
` 1
N
˘
and used this weak correlation for large N to ultimately deduce that prices can be
treated as weakly exogenous.15
Consider the well documented and empirically relevant case where µ is just above 1 (Zipf’s law corre-
sponds to µ = 1); when µ ∈(1, 2) we have hN, µ∈(1,2) = Op
´
1/(N2−2
µ )
¯
. So,
pt =
1
ϕd −ϕs
`
λ′
Sηt −εt
˘
+ Op
ˆ
1
N1−1
µ
˙
.
(56)
Therefore, even though Cov(pt, zt) = O
´
1/(N2−2
µ )
¯
, it is in fact decaying to zero so slowly for µ near 1,
that this potentially corresponds to a highly relevant instrument in any finite sample. That is, Cov(pt, zt) =
O
´
1/(N2−2
µ )
¯
, is potentially consistent with zt accounting for large fractions of aggregate variation, see
Gabaix (2011).
However, the case we theoretically entertain, for consistency and valid asymptotic inference, requires
µ ∈(0, 1), which in conjunction with the additional regularity assumptions, renders Cov(pt, zt) = Θ(1)
even as N →∞.
Rothemberg Representations. Moreover, to further assess the likelihood of weak instruments, we
can analyze the efficient GMM estimator of the demand elasticity which uses both the GIV and the factors
as instruments and for comparison we can analyze the just identified demand elasticity estimator which
uses only the GIV as an instrument. We analyze the overidentified case with conditional homoskedasticity
(assuming only for remainder of this section). Define the projection matrix P Zd = Zd(Z′
dZd)−1Z′
d, the
2SLS estimator takes the form
pϕd
GMM −ϕd = p′ P Zd ε
p′ P Zd p.
(57)
15"Granular" has a different definition in the panel data literature, which is referring to properties of weights and heuristically,
rules out the existence of dominant units, see e.g., Mohaddes and Pesaran (2016) and Remark 2. On the contrary, our usage of the
term "granular" follows Gabaix (2011) and is essentially referring to the existence of dominant cross-sectional units, see Section 1.
25


---

Write the structural and reduced form equations as
d = p ϕd + ε
p = zπ′ + v,
(58)
where
z
T×(1+r) =
´
uS
η
¯
,
π
(1+r)×1 =
´
1
ϕd−ϕs
1
ϕd−ϕs · λ′
S
¯′
and v
T×1 =
1
ϕd−ϕs · ε.
Remark 6 The difference between z in (58) and our actual instrument, Zd, boils down to the difference
between their first columns, Zd[·, 1] = zGIV = ˜u··QS and z[·, 1] = uS = u··S. In the case of the demand
equation, uS is ideal, whereas zGIV is a proxy. The reason the proxy is used is simply due to a simpler
theoretical exposition than a direct estimate for the ideal. Indeed zGIV is in fact a good proxy. For example,
the correlation between uS and zGIV is over 90% regardless of the complexity of our DGP in Monte Carlo
simulations even for small configurations of (N, T). Moreover, in the case of the supply equation, uS is
no longer valid, whereas zGIV is; see (13). Mathematically, S′u·t −S′Q˜u·t = S′P ˜Λu·t = S′P ˜ΛP ˜Λu·t
for each t, where P ˜Λ is the symmetric and idempotent projection matrix in the demeaned loading space.
Hence, S′P ˜ΛP ˜Λu·t is zero when the loadings and the share vector are asymptotically uncorrelated and/or
the loadings and idiosyncratic errors are asymptotically uncorrelated; which explains why our simulations
exhibit near perfect correlation.
Then, it follows from Rothenberg (1984) that (57) has the following illustrative representation
µd,GMM(pϕd
GMM −ϕd) =
ˆσ2
ε
σ2v
˙ 1
2
X + (ω1/µd,GMM)
1 + 2Y/µd,GMM + (ω2/µ2
d,GMM),
(59)
where X = π′z′P Zdε/(σ2
επ′z′zπ)
1
2 and Y = π′z′P Zdv/(σ2
vπ′z′zπ)
1
2 are bivariate standard normal
variates with correlation coefficient ρ. The random variable ω1 = v′P Zdε/(σ2
εσ2
v)
1
2 has mean equal to
rank(PZd)ρ = (r + 1)ρ and variance equal to (r + 1)(1 + ρ2). The random variable ω2 = v′P Zdv/σ2
v
has mean equal to rank(P Zd) = (r + 1) and variance equal to 2(r + 1). Finally, µd,GMM is the square
root of the so-called concentration parameter µ2
d,GMM = π′z′zπ/σ2
v for the demand equation. µd,GMM
plays the role of
?
T, that is, when µd,GMM is large, µd,GMM(pϕd
GMM −ϕd) is well approximated by a
N(0, 1) variate. Large values of µd,GMM are consistent with large values of T, i.e., our typical large sample
approximations. However, large values of µd,GMM are also consistent with small values of σ2
v, regardless
of the value of T, i.e., small-σ asymptotics, as introduced originally by Kadane (1971). More insights can
26


---

be gained by simplifying the concentration parameter for the demand elasticity
µ2
d,GMM = π′z′zπ/σ2
v = 1
σ2v
·
´
π1
π2′
¯ ˜
u′
SuS
u′
Sη
η′uS
η′η
¸ ˜
π1
π2
¸
≈u′
S uS + λ′
SλS
σ2ε
,
(60)
where the approximation is due to ignoring the terms involving η′uS, which are zero only in expectation.
(60) is very intuitive, if the proportion of the volatility in the GIV and size-weighted common components
dominate the volatility of the demand shocks, so that the ratio in (60) is large, then the concentration param-
eter µd,GMM will be large and one should expect good approximations to the finite sampling distributions.
On the other hand, when only the GIV is used as an instrument, if we redefine z
T×1 = uS, π
1×1 =
1
ϕd−ϕs
and v
T×1 =
1
ϕd−ϕs · (ε + ηλS) from (58) and simply follow the logic above through (60), we arrive at the
following concentration parameter for the FGIV estimator
µ2
d,FGIV ≈
u′
SuS
λ′
SλS + σ2ε
.
(61)
Thus, by inspection of (60) against (61) we can see that in the case of the just identified FGIV estimator,
we would need the volatility of just the GIV to drive up the ratio of the concentration parameter, µ2
d,GIV ,
and the size-weighted common component would be working against us (in the denominator), in this case,
instead of working for us as in µ2
d,GMM.
Although the literature on granularity has demonstrated that idiosyncratic shocks alone can be quite
volatile, in this context, we advocate starting with the efficient GMM estimators, since the J-test is well
sized as illustrated with simulation evidence, because the efficient GMM estimators can exhibit substantially
improved finite sample properties relative to the just identified estimators and are less likely to suffer from
weak instrument issues as well.
8.
Monte Carlo
We simulate the following panel simultaneous equations system with latent factor structure that was
analyzed in the theoretical sections:
dt = ϕdpt + εt, yit = ϕspt + λ1iη1t + λ2iη2t + uit, ySt = dt,
pt =
1
ϕd −ϕs
`
uSt + λ′
Sηt −εt
˘
, Si =
ˆ i
N
˙−1
µ
, Si =
Si
PN
j=1 Sj
.
27


---

We consider two sets of simulated experiments. In Design 1, we let uit be i.i.d. to establish a set of baseline
results. In Design 2, we allow for sparse cross-sectional dependence in uit. In addition, in unreported
simulations, we simulate zt,GIV to be a weak instrument to illustrate that the efficient GMM estimators
are robust to this as they optimally shift their weights away from this point of weakness, whereas the just
identified estimators of GK and our FGIV will substantially deteriorate in their performances.
Design 1 - uit i.i.d. case. We set ϕs = 0.1 and ϕd = −0.3. We draw the supply factors and loadings
as, η
T×r
i.i.d.
∼N(0, Ir) and Λ
N×r
i.i.d.
∼N(0, σ2
ΛIN), respectively, with r = 2.16 We draw the idiosyncratic
supply shocks as
u
T×N
i.i.d.
∼N(0, σ2
uIN ⊗IT ) and aggregate demand shocks as ε
T×1
i.i.d.
∼N(0, σ2
εIT ).
Design 2 - uit non-i.i.d. case. Everything is identical to Design 1, except that we no longer set
Σu = σ2
uIN for each t = 1, . . . , T. We generate a non-diagonal banded covariance matrix; as such, it
satisfies the sparsity requirement from Assumption 3.17 We consider the following banded idiosyncratic
covariance matrix with cross-sectional dependence and heteroskedasticity
σu,ij =





τ |i−j|?σu,iσu,j
|i −j|≤k; k ≥0,
0
|i −j|> k,
(62)
with bandwidth k = 3 and σ2
u,i are drawn from U[0.5, 1].
Target parameterizations. The variance of the price process takes the following form V(pt) =
c ·
`
V(uSt) + V(λ′
Sηt) + V(εt)
˘
, where c =
1
(ϕd −ϕs)2 . This conveniently allows us to parameter-
ize the relative volatilities of the various components of equilibrium prices. We parameterize the indi-
vidual variances, σ2
u (for Design 1), σ2
Λ and σ2
ε such that ψu := V p?c · uStq
V(pt)
∈(0.15, 0.35), ψu+η :=
V
`?c · (uSt + λ′
Sηt)
˘
V(pt)
∈(0.45, 0.65), and ψu+ε := V p?c · (uSt + εt)q
V(pt)
∈(0.45, 0.65).18 In Design 1,
we achieve an average across simulations of ¯ψu ≈0.23, ¯ψu+η ≈0.58 and ¯ψu+ε ≈0.65 which implies that
¯ψη = 0.35 and ¯ψε = 0.42. That is, the idiosyncratic shocks are not the dominating force in terms of ob-
served price volatility; however, their granular role is still substantial enough to draw inferences from when
used as instruments. In Design 2, we achieve an average across simulations of ¯ψu ≈0.27, ¯ψu+η ≈0.64 and
¯ψu+ε ≈0.63.
Let pϕj(m), j = d, s, denote the estimate in the mth monte carlo repetition, m = 1, ..., M. We report the
16The results do not change significantly if we draw the loadings from a Uniform distribution with non-zero mean.
17In unreported simulations, we find that the results do not change significantly if we generate a dense, non-diagonal Σu, such
as one arising from a cross-sectional AR(p) process. This is because although the cross-sectional AR(p) generates a dense matrix,
it is not too dense since the off-diagonals decay exponentially fast to 0 as |i −j|→∞.
18The interval for ψu is consistent with the literature on granularity, which has documented the proportion of aggregate fluctua-
tions traced back to idiosyncratic shocks falling in this specified range.
28


---

monte carlo bias: Bias(pϕj) =
ˆ 1
M
PM
m=1 pϕj(m) −ϕj
˙
for j = d, s; and square root of the monte carlo
MSE: RMSE(pϕj) =
c
1
M
PM
m=1(pϕj −ϕj)2 for j = s, d. Additionally we report the size of the t-test for
all estimators and size of the J-test for the efficient GMM estimators. The results are reported in Table 1
(Design 1) and Table 2 (Design 2). In Table 1, we multiply the bias by 100 because all the estimators perform
quite well in this ideal setting. For nearly each configuration of (N, T) the GMM estimators perform the
best, in terms of bias and RMSE, as the theory suggests. Importantly, the t-test and J-test is well sized even
when rmax = 3 > r = 2 factors are used. In Table 2, we report the bias as is, and we find that for a
given configuration of (N, T) the bias is two orders of magnitude larger in Design 2 relative to Design 1.
Nevertheless, as the theory would suggest, the efficient GMM estimators perform the best in terms of bias
and RMSE. There are some size distortions for the supply side estimators but the distortions are decreasing
in N for a given T.
9.
Application to Global Crude Oil Markets
The data construction follows the recent literature: Kilian (2009), Caldara et al. (2019), Baumeister and
Hamilton (2019) (hereafter BH) and GK. The following is a breakdown of the raw variables collected for
Jan. 1985 - Dec. 2015 (T = 372 months): monthly oil production for N = 22 countries from the U.S.
Energy Information Administration (hereafter EIA); world oil production from the U.S. EIA; monthly oil
prices based on the refiner acquisition cost of imported crude oil from the U.S. EIA; U.S. CPI from the
St. Louis FRED database; monthly change in inventories from BH; monthly industrial production index
from BH. The CPI is used to deflate nominal oil prices to arrive at the real price of oil, which is highly
non-stationary. Following the aforementioned literature, we take the logarithm of the real price of oil series
and then take first differences. We apply the same transformation to the monthly oil production for each
country. These transformations render the production and price series stationary as confirmed by a host of
Dickey-Fuller tests. For ensuring the tail index of the size-distribution, µ, is in the region the theory requires,
we provide visual evidence along with 6 estimates of µ that all fall beneath 1, see Table 3. Also, see Figure
1, Figure 2 & Figure 3.
Let yit denote the log difference of the oil supply for country i at time t and pt denote the log difference
of the real price of oil. Following GK, we estimate an OPEC factor using information on the cross-section
of countries (i.e., known loadings). To that end, let oit denote a dummy variable equal to 1 if country i is
an OPEC member at time t and note that oit = oi for most i, with the exception of Gabon and Ecuador in
our sample. Finally, ct−1 denotes a 4 × 1 vector containing: lagged pt, lagged world supply growth, lagged
29


---

change in inventories, and lagged growth in industrial production. The system is given as follows
yit = ϕspt + γs′ct−1 + oitηOPEC,t + λ′
iηt + uit,
(63)
dt = ϕdpt + γ′
dct−1 + λdηOPEC,t + εt,
(64)
N
X
i=1
Sit yit = dt;
(65)
where we lose the observation t = 1 due to differencing. The cross-sectionally demeaned supply equation
is given by the approximate factor model,
˜yit = yit −1
N
X
i
yit = ˜oitηOPEC,t + ˜λ
′
iηt + ˜uit = ˜oitηOPEC,t + ˜eit,
(66)
where ˜eit := ˜λ
′
iηt + ˜uit. Note that (66) implies we can obtain the OPEC factor, ηOPEC,t, via cross-sectional
regression, for each t > 1, that is pηOPEC,t = (˜o′
·t˜o·t)−1˜o′
·t˜y·t. Hence, in our preliminary stage, we extract
pηOPEC,t and then run PCA on p˜eit = ˜yit−pηOPEC,t to extract the latent demeaned loadings and latent factors.
Define y∗
·t := ˜y·t −˜x·tpηOPEC,t, then we purge the latent factors via Q as in the main text: Q y∗
·t = Q ˜u·t.
However, when forming the GIV, there is a minor difference that we have time-varying size-weights, so
we no longer construct zGIV with a time-invariant share vector Si, but rather we weight each idiosyncratic
component at time t with its corresponding share from time t −1 to avoid endogeneity issues arising from
contemporaneous weighting
zGIV
(T−1)×1
=
¨
˚
˚
˚
˚
˝
S′
·1Q ˜y∗
·2
S′
·2Q ˜y∗
·3
...
S′
·T−1Q ˜y∗
·T
˛
‹‹‹‹‚
.
(67)
Besides these modifications from the stylized model in the theory, we estimate the elasticities using the
estimators outlined in the main text. The number of factors, r, is estimated via the AH procedures (as
outlined in the Supplementary Appendix C). The ER method of AH estimated prER = 1, while the GR
method estimated prGR = 3; with kmax = 10. To be safe, we take pr = prGR + 1.
Supply results. The results for the supply elasticity are presented in Table 4. In Table 4, the 2nd
column displays GK’s results. The instrument GK use is given by (8) and their dependent variable is simply
the cross-sectional average of the log difference of oil supply (i.e., E = ι/N). Our results are in columns 3
and 4. In contrast to (8), the instrument we use in column 3 purges the common factors through the loading
30


---

space. The instrument we use in column 4 also adds an estimate of the unobserved aggregate demand shocks,
pεt, to our FGIV. Moreover, the dependent variable we use is weighted using the estimated precision vector
p
E, which allows for cross-sectional correlations and heteroskedasticity in uit. These differences lead to
significantly different results. Columns 2 and 3, which attempt to use only GIVs as instruments, both lead to
weak instruments as indicated by the first-stage F-statistics less than the rule of thumb, 10. Nevertheless, the
FGIV supply elasticity estimate (0.016) from column 3 (estimated via Algorithm 1) is roughly one third that
of GK’s (0.044). Whereas, our efficient GMM supply elasticity estimate (0.005) from column 4 (estimated
via Algorithm 3) is highly significant at the 1% level. Additionally, our results reveal that using estimates of
unobserved aggregate demand shocks as supply instruments indeed renders a strong instrument as indicated
by the first-stage F-stat of 14.33 in column 4. Moreover, the p-value for the J-statistic (0.11) fails to reject
the null hypothesis of a valid model. An F-stat greater than 10, coupled with a small J-statistic provides
statistical evidence in favor of our efficient GMM point estimate for the supply elasticity.
Demand results. Turning now to the demand elasticity in Table 5, the dependent variable GK use in
this case is the same as the one we use. However, the instruments are different. Column 2 displays GK’s
demand elasticity (-0.463), again using the instrument as in (8). Column 3 presents our result when using
only the FGIV as an instrument (-.0009), which is roughly 400 times smaller than GK’s estimate. Columns
4 through 7 sequentially add principal components to the instrument vector for our efficient GMM estimator
from column 3 until 4 principal components are used. Here we find that none of the models yield first-
stage F-statistics greater than 10. It is reassuring, however, that the J-statistic for columns 4 through 7 all
fail to reject the null of a valid model. Lastly, column 8 presents the Bai and Ng, 2010 estimator which
only includes the four principal components but not the FGIV as instruments, nearly all statistics remain
unchanged except that inclusion of the FGIV increases the t-stat by about 25%.
Taken together, our empirical results suggest that supply shocks, whether they be aggregate or idiosyn-
cratic supply shocks, albeit valid, do not serve as strong instruments for estimation of the demand elasticity.
Whereas, aggregate demand shocks indeed seem to be a strong source of exogenous variation to tease out
the supply elasticity.
10.
Concluding Remarks
In this paper, we have further developed the GIV methodology introduced by Gabaix and Koijen (2021),
which takes advantage of panel data to construct instruments for estimation of structural time series regres-
sion models that involve endogenous regressors. This paper focuses on the underlying econometric issues
31


---

involved in developing FGIV in a large N and large T framework where the loadings are treated as unknown
parameters to be estimated before constructing the FGIV instrument. We further demonstrate that the sam-
pling error arising from estimating the instrument, factors and a high dimensional precision matrix does not
affect the limiting distribution for the structural parameters of interest. We also overidentify the structural
parameters, which leads to new and improved results in the crude oil markets application and demonstrate
that the J-test is well sized with simulation evidence. Our Monte Carlo study illustrates that our estimators
and algorithms exhibit desirable performance with the finite sample distributions being well approximated
by the asymptotic distributions.
More fruitful areas of research would be empirical applications of the theoretical results derived in this
paper. Interesting theoretical extensions would be to allow for random slope coefficients with correlated
heterogeneity, the presence of weak factors and unbalanced panels with data not missing at random. We
are currently pursuing the dynamic panel data extension, as well as adapting the GIV methodology for
unit-specific endogenous variables.
32


---

Table 1: Bias×100, RMSE, Size of t-test and Size of J-test for Design 1.
Finite sample properties for Design 1.
N
T
µ
pϕs
FGIV
pϕs
GK
pϕs
GMM
pϕ s,rmax
GMM
pϕd
FGIV
pϕd
GK
pϕd
GMM
pϕd,rmax
GMM
1
30
400
0.92
0.0612
0.0910
0.0164
0.0273
-0.2760
-0.2723
0.1100
0.2100
(0.0344)
(0.0330)
(0.0204)
(0.0204)
(0.0152)
(0.0173)
(0.0079)
(0.0080)
[0.0635]
[0.1205]
[0.0830]
[0.0830]
[0.0570]
[0.0510]
[0.0685]
[0.0735]
{N.A.}
{N.A.}
{0.0540}
{0.0625}
{N.A.}
{N.A.}
{0.0490}
{0.0465}
2
50
400
0.85
0.0071
0.0774
0.0174
0.0224
-0.1803
-0.1649
0.1462
0.2306
(0.0313)
(0.0292)
(0.0200)
(0.0200)
(0.0106)
(0.0186)
(0.0058)
(0.0059)
[0.0650]
[0.2685]
[0.0710]
[0.0715]
[0.0555]
[0.0555]
[0.0700]
[0.0740]
{N.A.}
{N.A.}
{0.0520}
{0.0510}
{N.A.}
{N.A.}
{0.0480}
{0.0550}
3
100
400
0.80
0.0059
0.0159
0.0070
0.0102
-0.1886
-0.1558
0.1449
0.2330
(0.0287)
(0.0271)
(0.0196)
(0.0197)
(0.0068)
(0.0112)
(0.0039)
(0.0040)
[0.0610]
[0.2505]
[0.0585]
[0.0615]
[0.0515]
[0.0540]
[0.0705]
[0.0790]
{N.A.}
{N.A.}
{0.0495}
{0.0485}
{N.A.}
{N.A.}
{0.0440}
{0.0425}
4
200
400
0.77
0.0192
0.0246
-0.006
0.0010
-0.1896
-0.1713
0.0524
0.1409
(0.0276)
(0.0263)
(0.0188)
(0.0188)
(0.0046)
(0.0080)
(0.0027)
(0.0027)
[0.0600]
[0.2660]
[0.0545]
[0.0535]
[0.0410]
[0.0450]
[0.0625]
[0.0635]
{N.A.}
{N.A.}
{0.0590}
{0.0620}
{N.A.}
{N.A.}
{0.0495}
{0.0425}
5
500
400
0.75
-0.0013
-0.0078
-0.0097
-0.0102
0.2501
0.2255
-0.0893
-0.1747
(0.0287)
(0.0280)
(0.0188)
(0.0187)
(0.0028)
(0.0030)
(0.0016)
(0.0016)
[0.0545]
[0.0840]
[0.062]
[0.0625]
[0.0540]
[0.0590]
[0.0680]
[0.0730]
{N.A.}
{N.A.}
{0.0560}
{0.0535}
{N.A.}
{N.A.}
{0.054}
{0.051}
Notes: We report Bias×100, (RMSE), [t-test],and {J-test} (if applicable) with a nominal size of 5%. pϕs
FGIV , pϕs
GMM,
pϕs,rmax
GMM estimated with Algorithm 1, 3, 3 with r = 2 and rmax = 3, respectively and pϕs
GK, pϕd
GK both use (8) as an
instrument. pϕd
FGIV , pϕd
GMM, pϕd,rmax
GMM estimated with (12), (21), (21) with r = 2 and rmax = 3, respectively. µ set to
maintain hN,µ = 0.12 across all configurations of (N, T). ¯ψu = 0.23, ¯ψu+η = 0.58, ¯ψu+ε = 0.65.
33


---

Table 2: Bias, RMSE, Size of t-test and Size of J-test for Design 2.
Finite sample properties for Design 2.
N
T
µ
pϕs
FGIV
pϕs
GK
pϕs
GMM
pϕ s,rmax
GMM
pϕd
FGIV
pϕd
GK
pϕd
GMM
pϕd,rmax
GMM
1
30
400
0.92
0.0263
0.0225
0.0080
0.0089
-0.0021
-0.0016
0.0003
0.0009
(0.0365)
(0.0259)
(0.0150)
(0.0151)
(0.0371)
(0.0368)
(0.0148)
(0.0161)
[0.2730]
[0.2895]
[0.12450]
[0.1410]
[0.0500]
[0.0510]
[0.0560]
[0.0600]
{N.A.}
{N.A.}
{0.1895}
{0.3035}
{N.A.}
{N.A.}
{0.05200}
{0.0465}
2
50
400
0.85
0.0144
0.0136
0.0058
0.0063
-0.0009
-0.0007
0.0007
0.0013
(0.0245)
(0.0219)
(0.0154)
(0.0155)
(0.0381)
(0.0327)
(0.0112)
(0.0117)
[0.4030]
[0.4090]
[0.1245]
[0.1410]
[0.0465]
[0.0490]
[0.0705]
[0.0735]
{N.A.}
{N.A.}
{0.1185}
{0.1615}
{N.A.}
{N.A.}
{0.0425}
{0.0405}
3
100
400
0.80
0.0070
0.0065
0.0029
0.0031
-0.0006
-0.0004
0.0009
0.0014
(0.0221)
(0.0196)
(0.0137)
(0.0139)
(0.0117)
(0.0196)
(0.0068)
(0.0069)
[0.1365]
[0.3865]
[0.0925]
[0.0915]
[0.0465]
[0.0455]
[0.0530]
[0.0590]
{N.A.}
{N.A.}
{0.0895}
{0.0955}
{N.A.}
{N.A.}
{0.0495}
{0.0510}
4
200
400
0.77
0.0031
0.0029
0.0015
0.0016
-0.0011
-0.0009
0.0006
0.0010
(0.0216)
(0.0197)
(0.0139)
(0.0139)
(0.0071)
(0.0130)
(0.0044)
(0.0045)
[0.0950]
[0.3645]
[0.0745]
[0.0760]
[0.0400]
[0.0455]
[0.0640]
[0.0665]
{N.A.}
{N.A.}
{0.0590}
{0.0615}
{N.A.}
{N.A.}
{0.0510}
{0.0515}
5
500
400
0.75
0.0014
0.0014
0.0006
0.0006
-0.0011
-0.0009
0.0004
0.0008
(0.0218)
(0.0209)
(0.0141)
(0.0141)
(0.0037)
(0.0042)
(0.0024)
(0.0024)
[0.0690]
[0.1125]
[0.0670]
[0.0690]
[0.0515]
[0.0570]
[0.0605]
[0.0675]
{N.A.}
{N.A.}
{0.0535}
{0.0520}
{N.A.}
{N.A.}
{0.0575}
{0.0555}
Notes: We report Bias, (RMSE), [t-test],and {J-test} (if applicable) with a nominal size of 5%. pϕs
FGIV , pϕs
GMM, pϕs,rmax
GMM
estimated with Algorithm 1, 3, 3 with r = 2 and rmax = 3, respectively and pϕs
GK, pϕd
GK both use (8) as an instrument.
pϕd
FGIV , pϕd
GMM, pϕd,rmax
GMM estimated with (12), (21), (21) with r = 2 and rmax = 3, respectively. µ set to maintain
hN,µ = 0.12 across all configurations of (N, T). ¯ψu = 0.23, ¯ψu+η = 0.58, ¯ψu+ε = 0.65.
Table 3: Tail Index Estimates by Various
Methods
Tail index estimator
pµ
MLE
0.4216
OLS
0.5095
Percentiles Method
0.8987
Modified Percentiles Method
0.9000
Geometric Percentiles Method
0.5208
Weighted Least Squares
0.3725
Notes: The estimates are for a month selected
at random.
However, the estimates do not
change significantly if we estimate pµ for each
month and average across months.
34


---

Table 4: Global crude oil market: supply elasticity
pϕs
GK
pϕs
FGIV
pϕs
GMM
Supply instruments
ZGIV
zGIV
Zs = (zGIV , ε)
Dep. variable
¯y
y pE
y pE
p
0.044
0.016
0.005
t-stat
(1.43)
(1.35)
(4.32)
(N, T)
(21, 370)
(21, 370)
(21, 370)
J-stat p-value
{N.A.}
{N.A.}
0.11
First stage F-stat
< 10
< 10
14.33
First stage R2
0.26
0.14
0.21
Notes: pϕs
GK is estimated using (8) as the instrument; whereas pϕs
F GIV ,
and pϕs
GMM are estimated using Algorithm 1 and 3 respectively. See
Section 9 for more details. The t-stat is reported in parenthesis below
coefficient estimates. The coefficient estimates on pηt,pηOP EC,t and ct−1
are omitted for brevity.
Table 5: Global crude oil market: demand elasticity
pϕd
GK
pϕd
FGIV
pϕd
GMM(r)
FGMM, BN
Demand instruments
ZGIV
zGIV
(zGIV , η[, 1])
(zGIV , η[, 1 : 2])
(zGIV , η[, 1 : 3])
(zGIV , η[, 1 : 4])
η[, 1 : 4]
Dep. variable
d
d
d
d
d
d
d
p
−0.463
−0.0009
−0.0009
−0.0003
−0.0003
−0.0003
−0.0003
t-stat
(−3.54)
(−0.88)
(−0.89)
(−0.87)
(−0.93)
(−1.01)
(−0.80)
(N, T)
(21, 370)
(21, 370)
(21, 370)
(21, 370)
(21, 370)
(21, 370)
(21, 370)
J-stat p-value
{N.A.}
{N.A.}
0.83
0.67
0.85
0.93
0.98
First stage F-stat
< 10
< 10
< 10
< 10
< 10
< 10
< 10
First stage R2
0.58
0.12
0.12
0.15
0.15
0.16
0.16
Note: pϕd
GK is estimated using (8) as the instrument; whereas pϕd
F GIV , and pϕd
GMM are estimated using (12) and (21) respectively. See Section 9 for more
details. The t-stat is reported in parenthesis below coefficient estimates. The coefficient estimates on pηOP EC,t and ct−1 are omitted for brevity. The final
column represents the Bai and Ng (2010) factor GMM estimator (FGMM).
35


---

Appendix
In this appendix, we prove Theorems 1-6, which require 4 lemmas. Lemmas 1, 2 and 3 are included in
this appendix while Lemma 4 is deferred to Appendix B of the Supplementary Appendix.
Lemma 1 Under Assumptions 1-4, we have that
(i.)
˜
1
T
T
X
t=1
˜yitεt
¸2
= Op
ˆ 1
T
˙
(68)
(ii.) V(pt) = Θ(1)
(69)
(iii.)
˜
1
T
T
X
t=1
˜yitpt
¸2
= Op p1q
(70)
(iv.)
N
X
i=1
N
X
j=1
˜
1
T
T
X
t=1
Si˜yjtεt
¸2
= Op
ˆN
T
˙
.
(71)
Proof of Lemma 1: For (i.), we have that for large T, the sum is stochastically bounded by the central
limit theorem when scaled by T −1/2, thus the term inside the square is Op
´
1
?
T
¯
. For (ii.), note that by
Assumption 3 we can decompose our share vector into a dominant and a fringe part: S =
´
S′
d
S′
f
¯′
where Sd is N1 × 1, is the dominant part and Sf is N2 × 1, is the fringe part; with N1 + N2 = N. The
key being that N1(N) = N1 is fixed while N2(N) →∞as N →∞. Recall that prices are given by
pt =
1
ϕd −ϕs
`
uSt + λ′
Sηt −εt
˘
. For simplicity, suppose that supply and demand shocks are uncorrelated,
so that (ignoring the squared constant term)
V(pt) ∝E(S′ΣuS) + E(S′ΛΛ′S) + V(εt) = E(S′ΣuS) + E(S′
dΛdΛ′
dSd) + E(S′
fΛfΛ′
fSf) + V(εt)
≤E(||S||2
2γmax(Σu)) + E(||Sd||2
2γmax(ΛdΛ′
d)) + E(||Sf||2
2γmax(ΛfΛ′
f)) + O(1),
by Assumption 3 and Assumption 4; the first term consists of ||S||2, which is Θp(1) for µ ∈(0, 1), see
Lemma 4 in Appendix B of the Supplementary Appendix, and γmax(Σu) = O(1) by assumption, the
second term is O(1) by Assumption 4 and the third term is O( 1
N ) · O(N) = O(1) by Assumption 4. For
part (iii.),
˜
1
T
T
X
t=1
˜yitpt
¸
≤
˜
1
T
T
X
t=1
˜y2
it
¸ 1
2
·
˜
1
T
T
X
t=1
p2
t
¸ 1
2
=
ˆ 1
?
T
||˜yi·||
˙
·
ˆ 1
?
T
||p||
˙
= Op(1).
36


---

For part (iv.), we have
N
X
i=1
N
X
j=1
˜
1
T
T
X
t=1
Si˜yjtεt
¸2
= I + II + III + IV,
where I = Op
` 1
T
˘
= op(1), II = Op
` 1
T
˘
= op(1), III = Op
` 1
NT
˘
= op(1) and IV = Op(N
T ) which
are show below (where we repeatedly make use of part (i.) as well as the decomposition of the share vector
into fringe and dominant components)
I =
N1
X
i=1
S2
i
N1
X
j=1
˜
1
T
T
X
t=1
˜yjtεt
¸2
= ||Sd||2·Op
ˆN1
T
˙
= op(1)
II =
N
X
i=N1+1
S2
i
N
X
j=N1+1
˜
1
T
T
X
t=1
˜yjtεt
¸2
= ||Sf||2·Op(N2) · Op
ˆ 1
T
˙
= Op
ˆ 1
N
˙
Op
ˆN2
T
˙
= op(1)
III =
N
X
i=N1+1
S2
i
N1
X
j=1
˜
1
T
T
X
t=1
˜yjtεt
¸2
= ||Sf||2·Op
ˆN1
T
˙
= op p1q
IV =
N1
X
i=1
S2
i
N
X
j=N1+1
˜
1
T
T
X
t=1
˜yjtεt
¸2
= Op
ˆN
T
˙
by Assumption 4 and Lemma 1 part (i.)
■
Lemma 2 Under Assumptions 1-4, we have that
1
T
T
X
t=1
(pzt −zt)εt = 1
T
T
X
t=1
S′( p
Q −Q)˜y·tεt = Op(C−2
NT ) + Op(C−2
NT ) · Op
ˆN
T
˙
+ Op
ˆ 1
?
N
· C−1
NT
˙
(72)
1
T
T
X
t=1
(pzt −zt)pt = 1
T
T
X
t=1
S′( p
Q −Q)˜y·tpt = Op(C−2
NT ) + Op(C−2
NT ) · Op
ˆN
T
˙
+ Op
ˆ 1
?
N
· C−1
NT
˙
,
(73)
37


---

where CNT = min{
?
N,
?
T}.
Proof of Lemma 2: For the first term, it is well known that the loadings are only identified up to scale,
so the usual notion of consistency is altered to consider consistency up to a rotation instead. For notational
ease we will let ˜Λ be denoted by Λ. Recall, Q = IN −P ΛH−1 is an idempotent matrix spanned by the
null space of ΛH−1 and is invariant to an orthogonal transformation. Let p
D =
pΛ
′ pΛ
N
= 1
N
PN
i=1 pλipλ
′
i and
D = H−1′(Λ′Λ)H−1
N
= 1
N H−1′ PN
i=1 λiλ′
iH−1, then we have (omitting subscripts on P )
p
Q −Q = p
P −P
= N−1 pΛ
˜ pΛ
′ pΛ
N
¸−1
pΛ
′ −N−1ΛH−1
˜
H−1′(Λ′Λ)H−1
N
¸−1
H−1′Λ′
= N−1 ”
pΛ p
D−1 pΛ
′ −ΛH−1D−1H−1′Λ′ı
= N−1 ”
(pΛ −ΛH−1 + ΛH−1) p
D−1(pΛ −ΛH−1 + ΛH−1)′ −ΛH−1D−1H−1′Λ′ı
= N−1 r (pΛ −ΛH−1) p
D−1(pΛ −ΛH−1)′ + (pΛ −ΛH−1) p
D−1H−1′Λ′ + . . .
· · · + ΛH−1 p
D−1(pΛ −ΛH−1) + ΛH−1( p
D−1 −D−1)H−1′Λ′ s .
Therefore, 1
T
PT
t=1 S′( p
Q −Q)˜y·tεt = I + II + III + IV . Each term is analyzed below in order.19
I =
1
NT
T
X
t=1
S′(pΛ −ΛH−1) p
D−1(pΛ −ΛH−1)′˜y·tεt
= 1
N
N
X
i=1
N
X
j=1
(pλi −H−1λi)′ p
D−1(pλj −H−1λj) · 1
T
T
X
t=1
Si˜yjtεt
≤
¨
˝ 1
N2
N
X
i=1
N
X
j=1
”
(pλi −H−1λi)′ p
D−1(pλj −H−1λj)
ı2
˛
‚
1
2
·
»
–
N
X
i=1
N
X
j=1
˜
1
T
T
X
t=1
Si˜yjtεt
¸2fi
fl
1
2
(74)
≤
¨
˝ 1
N2
N
X
i=1
N
X
j=1
||(pλi −H−1λi)||2·|| p
D−1||2·||(pλj −H−1λj)||2
˛
‚
1
2
· Op
ˆN
T
˙
= || p
D−1||·
¨
˝
˜
1
N
N
X
i=1
||(pλi −H−1λi)||2
¸2˛
‚
1
2
· Op
ˆN
T
˙
= Op(1) · Op(C−2
NT ) · Op
ˆN
T
˙
= Op(C−2
NT ) · Op
ˆN
T
˙
,
where Op(C−2
NT ) follows from symmetry of Theorem 1 in Bai and Ng (2002), who show (while proving their
19In this Appendix, we use the Frobenius norm of a matrix A is ||A||F = rtr(A′A)s
1
2 =
”P
i
P
j|aij|2ı 1
2 , but omit the
subscript F for notational ease.
38


---

Lemma 2) || pD−1|| is Op(1) which again follows symmetrically here. Note, the first inequality follows from
Cauchy-Schwarz applied to the summation in (i, j); the second inequality follows from Cauchy-Schwarz
applied again but to the left most term’s inner term in brackets being squared, in equation (74).
II =
1
NT
T
X
t=1
S′(pΛ −ΛH−1) p
D−1H−1′Λ′˜y·tεt = 1
N
N
X
i=1
(pλi −H−1λi)′ p
D−1
N
X
j=1
H−1′ λj · 1
T
T
X
t=1
Sj ˜yitεt
loooooooooooooooooooomoooooooooooooooooooon
ai
r×1
= Op
`
C−2
NT
˘
,
(75)
which is the same rate as I. In (75), we make use of the fact that N−1 P
i(pλi −H−1λi)′ai = Op
`
C−2
NT
˘
,
which follows symmetrically from Lemma B.1 of Bai (2003). The same logic leads to III = Op
`
C−2
NT
˘
.
IV =
1
NT
T
X
t=1
S′ΛH−1( p
D−1 −D−1)H−1′Λ′˜y·tεt = 1
N
N
X
i=1
N
X
j=1
Siλ′
iH−1( p
D−1 −D−1)H−1′λj · 1
T
T
X
t=1
˜yjtεt
≤
¨
˝ 1
N2
N
X
i=1
N
X
j=1
S2
i
”
λ′
iH−1( p
D−1 −D−1)H−1′λj
ı2
˛
‚
1
2
· Op p1q
≤
¨
˝ 1
N2
N
X
i=1
N
X
j=1
S2
i · ||λ′
iH−1||2·|| p
D−1 −D−1||2·||H−1′λj||2
˛
‚
1
2
· Op p1q
= Op(C−1
NT ) ·
˜
1
N
N
X
i=1
S2
i · ||λ′
iH−1||2
¸ 1
2
· Op(1) · Op p1q
= Op(C−1
NT ) ·
¨
˝ 1
N
»
–
N1
X
i=1
S2
i · ||λ′
iH−1||2+
N
X
i=N1+1
S2
i · ||λ′
iH−1||2
fi
fl
˛
‚
1
2
· Op(1) · Op p1q
≤Op(C−1
NT ) ·
¨
˚
˝ 1
N
˜ N1
X
i=1
S4
i
¸ 1
2
·
˜ N1
X
i=1
||λ′
iH−1||4
¸ 1
2
+ 1
N
¨
˝
N
X
i=N1+1
S4
i
˛
‚
1
2
·
¨
˝
N
X
i=N1+1
||λ′
iH−1||4
˛
‚
1
2
˛
‹‚
1
2
= Op
`
C−1
NT
˘
·
ˆ
Op
ˆN1
N
˙
+ Op
ˆ 1
N
˙˙ 1
2
= Op
`
C−1
NT
˘
· Op
ˆ 1
?
N
˙
,
where || p
D−1 −D−1||= Op(C−1
NT ) again follows symmetrically from Bai and Ng (2002). All in all, we
have that
1
T
T
X
t=1
S′( p
Q −Q)˜y·tεt = Op(C−2
NT ) + Op(C−2
NT ) · Op
ˆN
T
˙
+ Op
ˆ 1
?
N
· C−1
NT
˙
,
39


---

which is as the Lemma claimed.
■
Proof of Theorem 1: In light of Lemma 2, the result follows immediately from (26) by observing that
1
T
P
t ptzt
p→E(ptzt) > 0 for µ ∈(0, 1). Similarly, 1
T
P
t ztεt
p→E(ztεt) = 0 by Assumption 4.
■
Proof of Theorem 2: Under Assumptions 1-4 and Lemma 2, the result follows immediately.
■
As in the case of the demand elasticity, we need Lemma 3 before consistency and the limiting distribution
of the supply elasticity can be established.
Lemma 3 Under Assumptions 1-4, we have that the terms ai, bi, cj for i = 1, 2; and j = 1, 2; defined in
equations (34), (35) and (36) are op p1q. While for j = 3, c3 is Op
ˆ
mNω1−q
N,T
T
˙
= op(1).
Proof of Lemma 3: The terms, a1, b1, and c1 follow very similarly as the proof for Lemma 2 and hence
are omitted and the terms a2, b2 and c2 follow symmetrically to the proof of Lemma 2 and thus, they
are also omitted. The term c3 is novel and warrants some further analysis. Recall c3 is given by c3 =
T −1z′ M η (u pE −uE). Let us focus on (u pE −uE) = u··( p
E −E) momentarily, where u·· is the T × N
matrix of idiosyncratic errors and p
E −E =
pΣ
−1
u ι
ι′ pΣ
−1
u ι
−Σ−1
u ι
ι′Σ−1
u ι. Let Θu := Σ−1
u , C := ι′Θuι
N
, then
E = Θuι/N
C
. We have that
p
E −E =
”
C pΘuι −pCΘuι
ı
/N
pCC
=
”
C pΘuι −CΘuι + CΘuι −pCΘuι
ı
/N
pCC
,
=
”
C( pΘu −Θu)ι + (C −pC)Θuι
ı
/N
pCC
,
=⇒|| p
E −E||1 ≤
”
C · ||( pΘu −Θu)ι||1+|C −pC|·||Θuι||1
ı
/N
| pC|C
,
(76)
where (76) follows from Callot et al. (2021). Let Θu,j denote the jth row of Θu written as a column vector.
Using Hölder’s inequality we have
| pC −C| =
ˇˇˇˇ
ι′( pΘu −Θu)ι
N
ˇˇˇˇ ≤||( pΘu −Θu)ι||1·||ι||max
N
≤max
1≤j≤N|| pΘu,j −Θu,j||1= || pΘu −Θu||1.
40


---

Thus,
|| p
E −E||1 ≤
”
C · ||( pΘu −Θu)ι||1+|C −pC|·||Θuι||1
ı
/N
| pC|C
,
≤
„
C · max
1≤j≤N|| pΘu,j −Θu,j||1+ max
1≤j≤N|| pΘu,j −Θu,j||1·||Θuι||1/N
ȷ
| pC|C
,
=
max
1≤j≤N|| pΘu,j −Θu,j||1rC · +||Θuι||1/Ns
| pC|C
≤
max
1≤j≤N|| pΘu,j −Θu,j||1
„
C + max
1≤j≤N||Θu,j||1
ȷ
| pC|C
,
≤|| pΘu −Θu||1rC + ||Θu||1s
|C + op(1)|C
=
Op(mNω1−q
N,T ) rOp(1) + Op(1)s
(Op(1) + op(1))Op(1)
= Op(mNω1−q
N,T ),
(77)
where C ≥γmin(Θu) > 0. Putting it all together for c3, we have that
c3 = T −1z′ M η(u pE −uE) = T −1z′ M η u·· ( p
E −E) ≤γmax(M η) · T −1z′ u·· ( p
E −E),
= T −1z′ u·· ( p
E −E) ≤T −1||u··′z||1·|| p
E −E||1≤T −1||u··′z||1·Op(mNω1−q
N,T ),
= T −1
N
X
i=1
|Si(u··′ y·· Q)i|·Op(mNω1−q
N,T ) = Op
ˆ 1
T
˙
· Op(mNω1−q
N,T ) = op(1),
which concludes the proof.
■
Proof of Theorem 3: In light of Lemma 3, the result follows immediately from (37).
■
Proof of Theorem 4: Under Assumptions 1-4 and Lemma 3, the result follows immediately.
■
Proof of Theorem 5: In light of Theorem 2 and Bai and Ng (2010), the result follows immediately.
■
Proof of Theorem 6: In light of the theorems in the just identified case and standard GMM theory, we
know that
?
T(pθ
s
GMM −θs) is asymptotically, a normal variate. The question remains whether using pε =
ε(pϕd
GMM) introduces sampling error that will effect the standard error of pθ
s
GMM. To that end, let
gst
(2+r)×1
:=
41


---

ZstuEt, we have that pθ
s
GMM solves the following first-order condition with probability approaching 1
0 =
˜
1
T
T
X
t=1
∂
∂θs gst(pθ
s
GMM; pϕd)
¸′
pΩ
−1
s
˜
1
T
T
X
t=1
gst(pθ
s
GMM; pϕd)
¸
(78)
=
˜
1
T
T
X
t=1
∂
∂θs gst(pθ
s
GMM; pϕd)
¸′
pΩ
−1
s
˜
1
T
T
X
t=1
gst(θs; pϕd)
¸
+
˜
1
T
T
X
t=1
∂
∂θs gst(pθ
s
GMM; pϕd)
¸′
pΩ
−1
s
˜
1
T
T
X
t=1
∂
∂θs gst(¯θs; pϕd)
¸
(pθ
s
GMM −θs)
(79)
= G′
s pΩ
−1
s
˜
1
?
T
T
X
t=1
gst(θs; pϕd)
¸
+ G′
s pΩ
−1
s
Gs
?
T(pθ
s
GMM −θs)
(80)
The basic idea of whether the sampling error from estimating pϕd can be ignored, boils down to whether
the following expression holds:
1
?
T
PT
t=1 gst(θs; pϕd) =
1
?
T
PT
t=1 gst(θs; ϕd) + op(1); when this equation
holds, then
?
T(pθ
s
GMM −θs) will not asymptotically depend on
?
T(pϕd −ϕd). This can be easily seen if
we take a mean value expansion of the left hand side of the expression above around ϕd, we obtain
1
?
T
T
X
t=1
gst(θs; pϕd) =
1
?
T
T
X
t=1
gst(θs; ϕd) + F
?
T(pϕd −ϕd) + op(1),
(81)
where
F
(2+r)×1 := E
”
∇ϕdgst(θs; pϕd)
ı
, is generally different from zero, but here we have F = Op(
1
?
N ).
This implies the asymptotic variance of
?
T(pθ
s
GMM −θs) need not take into account the sampling error
induced by pϕd. To see why, we need to get an expression for
?
T(pϕd −ϕd), let
gdt
(1+r)×1
= Zdtεt; then
taking a similar mean value expansion (as above) of the first-order conditions that pϕd solves with probability
approaching 1
0 = G′
d pΩ
−1
d
˜
1
?
T
T
X
t=1
gdt(ϕd)
¸
+ G′
d pΩ
−1
d Gd
?
T(pϕd −ϕd),
(82)
hence, we obtain the usual influence function representation
?
T(pϕd −ϕd) = −1
?
T
T
X
t=1
(G′
dΩ−1
d Gd)−1G′
dΩ−1
d gdt(ϕd) :=
1
?
T
T
X
t=1
rdt(ϕd).
(83)
42


---

Making use of (83) in (81) we obtain
1
?
T
T
X
t=1
gst(θs; pϕd) =
1
?
T
T
X
t=1
ˇgst(θs; ϕd) + op(1),
(84)
where ˇgst(θs; ϕd) := gst(θs; ϕd)+F rdt(ϕd). Putting (84) and (80) together and solving for
?
T(pθ
s
GMM −
θs) gives
?
T(pθ
s
GMM −θs) d→−(G′
s Ω−1
s
Gs)−1G′
s Ω−1
s
˜
1
?
T
T
X
t=1
gst(θs; ϕd) + F rdt(ϕd)
¸
+ op(1),
(85)
= −(G′
s Ω−1
s
Gs)−1G′
s Ω−1
s
˜
1
?
T
T
X
t=1
gst(θs; ϕd) + Op
ˆ 1
?
N
˙
Op p1q
¸
+ op(1),
(86)
which gives the result.
■
References
Acemoglu, D., V. M. Carvalho, A. Ozdaglar, and A. Tahbaz-Salehi (2012). “The network origins of aggregate fluctuations”. Econo-
metrica 80.5, pp. 1977–2016.
Acemoglu, D., A. Ozdaglar, and A. Tahbaz-Salehi (2017). “Microeconomic origins of macroeconomic tail risks”. American Eco-
nomic Review 107.1, pp. 54–108.
Ahn, S. C. and A. R. Horenstein (2013). “Eigenvalue ratio test for the number of factors”. Econometrica 81.3, pp. 1203–1227.
Antoniadis, A. and J. Fan (2001). “Regularization of wavelet approximations”. Journal of the American Statistical Association
96.455, pp. 939–967.
Arellano, M. and S. Bond (1991). “Some tests of specification for panel data: Monte Carlo evidence and an application to employ-
ment equations”. The Review of Economic Studies 58.2, pp. 277–297.
Bai, J. (2003). “Inferential theory for factor models of large dimensions”. Econometrica 71.1, pp. 135–171.
—
(2009). “Panel data models with interactive fixed effects”. Econometrica 77.4, pp. 1229–1279.
Bai, J. and Y. Liao (2017). “Inferences in panel data with interactive effects using large covariance matrices”. Journal of Economet-
rics 200.1, pp. 59–78.
Bai, J., Y. Liao, and J. Yang (2015). “Unbalanced panel data models with interactive effects”. The Oxford Handbook of Panel Data.
Bai, J. and S. Ng (2002). “Determining the number of factors in approximate factor models”. Econometrica 70.1, pp. 191–221.
—
(2006). “Confidence intervals for diffusion index forecasts and inference for factor-augmented regressions”. Econometrica
74.4, pp. 1133–1150.
—
(2010). “Instrumental variable estimation in a data rich environment”. Econometric Theory 26.6, pp. 1577–1606.
—
(2021a). “Approximate Factor Models with Weaker Loadings”. arXiv preprint arXiv:2109.03773.
43


---

Bai, J. and S. Ng (2021b). “Matrix completion, counterfactuals, and factor analysis of missing data”. Journal of the American
Statistical Association 116.536, pp. 1746–1763.
Bailey, N., G. Kapetanios, and M. H. Pesaran (2016). “Exponent of cross-sectional dependence: Estimation and inference”. Journal
of Applied Econometrics 31.6, pp. 929–960.
Bartik, T. J. (1991). “Who benefits from state and local economic development policies?” WE Upjohn Institute for Employment
Research.
Baumeister, C. and J. D. Hamilton (2019). “Structural interpretation of vector autoregressions with incomplete identification: Re-
visiting the role of oil supply and demand shocks”. American Economic Review 109.5, pp. 1873–1910.
Blank, S., C. M. Buch, and K. Neugebauer (2009). “Shocks at large banks and banking sector distress: The Banking Granular
Residual”. Journal of Financial Stability 5.4, pp. 353–373.
Caldara, D., M. Cavallo, and M. Iacoviello (2019). “Oil price elasticities and oil price fluctuations”. Journal of Monetary Economics
103, pp. 1–20.
Callot, L., M. Caner, A. Ö. Önder, and E. Ula¸san (2021). “A nodewise regression approach to estimating large portfolios”. Journal
of Business & Economic Statistics 39.2, pp. 520–531.
Canals, C., X. Gabaix, J. Vilarrubia, and D. Weinstein (2007). “Trade Shocks, Trade Balances, and Idiosyncratic Shocks”. Working
Paper 721.
Carvalho, V. and X. Gabaix (2013). “The great diversification and its undoing”. American Economic Review 103.5, pp. 1697–1727.
Chamberlain, G. (1987). “Asymptotic efficiency in estimation with conditional moment restrictions”. Journal of Econometrics 34.3,
pp. 305–334.
Dupor, B. (1999). “Aggregation and irrelevance in multi-sector models”. Journal of Monetary Economics 43.2, pp. 391–409.
Fan, J., Y. Liao, and M. Mincheva (2013). “Large covariance estimation by thresholding principal orthogonal complements”. Jour-
nal of the Royal Statistical Society. Series B, Statistical methodology 75.4.
Freyaldenhoven, S. (2021). “Factor models with local factors—Determining the number of relevant factors”. Journal of Economet-
rics.
Fuller, W. A. (1977). “Some properties of a modification of the limited information estimator”. Econometrica, pp. 939–953.
Gabaix, X. (2011). “The granular origins of aggregate fluctuations”. Econometrica 79.3, pp. 733–772.
Gabaix, X. and R. S. Koijen (2021). “Granular instrumental variables”. Available at SSRN 3368612.
Gatti, D. D., C. Di Guilmi, E. Gaffeo, G. Giulioni, M. Gallegati, and A. Palestrini (2005). “A new approach to business fluctuations:
heterogeneous interacting agents, scaling laws and financial fragility”. Journal of Economic Behavior & Organization 56.4,
pp. 489–512.
Greenaway-McGrevy, R., C. Han, and D. Sul (2012). “Asymptotic distribution of factor augmented estimators for panel regression”.
Journal of Econometrics 169.1, pp. 48–53.
Hatanaka, M. (1973). “On the Existence and the Approximation Formulae for the Moments of the k-Class Estimators”. The Eco-
nomic Studies Quarterly (Tokyo. 1950) 24.2, pp. 1–15.
Hillier, G. and V. Srivastava (1981). “The exact bias and mean square error of the k-class estimators for the coefficient of an
endogenous variable in a general structural equation”. mimeographed, Monash University.
Horvath, M. (2000). “Sectoral shocks and aggregate fluctuations”. Journal of Monetary Economics 45.1, pp. 69–106.
Jannati, S. (2017). “Geographic Spillover of Dominant Firms’ Shocks”. 8th Miami Behavioral Finance Conference. Vol. 2019.
Kadane, J. B. (1971). “Comparison of k-class estimators when the disturbances are small”. Econometrica, pp. 723–737.
44


---

Kapetanios, G. and M. Marcellino (2010). “Factor-GMM estimation with large sets of possibly weak instruments”. Computational
Statistics & Data Analysis 54.11, pp. 2655–2675.
Kilian, L. (2009). “Not all oil price shocks are alike: Disentangling demand and supply shocks in the crude oil market”. American
Economic Review 99.3, pp. 1053–69.
Kinal, T. W. (1980). “The existence of moments of k-class estimators”. Econometrica 48.1, pp. 241–249.
Koren, M. and S. Tenreyro (2007). “Volatility and development”. The Quarterly Journal of Economics 122.1, pp. 243–287.
Lera, S. C. and D. Sornette (2017). “Quantification of the evolution of firm size distributions due to mergers and acquisitions”.
PLOS One 12.8.
Logan, B. F., C. Mallows, S. Rice, and L. A. Shepp (1973). “Limit distributions of self-normalized sums”. The Annals of Probability
1.5, pp. 788–809.
Long, J. B. and C. I. Plosser (1983). “Real business cycles”. Journal of Political Economy 91.1, pp. 39–69.
Malevergne, Y., P. Santa-Clara, and D. Sornette (2009). Professor Zipf goes to Wall Street. Tech. rep. National Bureau of Economic
Research.
Mariano, R. S. (1973). “Approximations to the distribution functions of the ordinary least-squares and two-stage least-squares
estimators in the case of two included endogenous variables”. Econometrica, pp. 67–77.
Mohaddes, K. and M. H. Pesaran (2016). “Country-specific oil supply shocks and the global economy: A counterfactual analysis”.
Energy Economics 59, pp. 382–399.
Moon, H. R. and M. Weidner (2015). “Linear regression for panel with unknown number of factors as interactive fixed effects”.
Econometrica 83.4, pp. 1543–1579.
Onatski, A. (2010). “Determining the number of factors from empirical distribution of eigenvalues”. The Review of Economics and
Statistics 92.4, pp. 1004–1016.
—
(2012). “Asymptotics of the principal components estimator of large factor models with weakly influential factors”. Journal of
Econometrics 168.2, pp. 244–258.
Pagan, A. (1984). “Econometric issues in the analysis of regressions with generated regressors”. International Economic Review
25.1, pp. 221–247.
Pesaran, M. H. and C. F. Yang (2020). “Econometric analysis of production networks with dominant units”. Journal of Econometrics
219.2, pp. 507–541.
Rigobon, R. (2003). “Identification through heteroskedasticity”. Review of Economics and Statistics 85.4, pp. 777–792.
Rothenberg, T. J. (1984). “Approximating the distributions of econometric estimators and test statistics”. Handbook of Econometrics
2, pp. 881–935.
Sargan, J. (1978). “On the existence of the moments of 3SLS estimators”. Econometrica, pp. 1329–1350.
Sawa, T. (1972). “Finite-sample properties of the k-class estimators”. Econometrica, pp. 653–680.
Schiaffi, S. et al. (2013). “The Granularity of the Stock Market: Forecasting Aggregate Returns Using Firm-Level Data”. Rivista di
Politica Economica 4, pp. 141–169.
Staiger, D. and J. H. Stock (1997). “Instrumental Variables Regression with Weak Instruments”. Econometrica 65.3, pp. 557–586.
Takeuchi, K. (1970). “Exact sampling moments of the ordinary least squares, instrumental variable and two-stage least squares
estimators”. International Economic Review 11.1, pp. 1–12.
Ullah, A. and A. Nagar (1974). “The exact mean of the two-stage least squares estimator of the structural parameters in an equation
having three endogenous variables”. Econometrica 42.4, pp. 749–758.
45


---

Xiong, R. and M. Pelger (2019). “Large dimensional latent factor modeling with missing observations and applications to causal
inference”. arXiv preprint arXiv:1910.08273.
Yan, W. (2011). “Role of diversification risk in financial bubbles”. Swiss Finance Institute Research Paper 11-26.
46


---

Supplementary Appendices
This is the Supplementary Appendix to the paper, "Inferential Theory for Granular Instrumental Variables
in High Dimensions" by Saman Banafti and Tae-Hwy Lee. Section A contain figures pertaining to the
empirical work from Section 9. Section B contains theoretical results for Herfindahl’s in large N markets
along with Lemma 4. Section C contains the estimation methods we use when r is unknown. Section D
contains Algorithm 3′ which employs an alternative estimator for the precision matrix, which is a hybrid of
the factor approach and graphical models.
A.
Figures
47


---

OPEC
Residual Countries
United States
USSR/Russia
0.0
0.2
0.4
1980
1990
2000
2010
2020
Date
production_shares
country
Canada
China
Egypt
Gabon
Mexico
Norway
OPEC
Residual Countries
United Kingdom
United States
USSR/Russia
Figure 1: Temporal variation of production shares
48


---

0
10
20
0.00
0.05
0.10
0.15
0.20
shares
density
key
1985/01/01
1987/01/01
1989/01/01
1991/01/01
1993/01/01
1995/01/01
1997/01/01
1999/01/01
2001/01/01
2003/01/01
2005/01/01
2007/01/01
2009/01/01
2011/01/01
2013/01/01
2015/01/01
Figure 2: Distribution of production shares
49


---

0.001
0.010
0.100
1
3
10
rank (log scale)
shares (log scale)
key
1985/01/01
1987/01/01
1989/01/01
1991/01/01
1993/01/01
1995/01/01
1997/01/01
1999/01/01
2001/01/01
2003/01/01
2005/01/01
2007/01/01
2009/01/01
2011/01/01
2013/01/01
2015/01/01
Figure 3: Size-Rank plot (log-log scale)
50


---

B.
Herfindahl’s in Large N Markets
In this appendix we provide some basic information about properties of random variables that follow a
power law and then we conclude with the statement of Lemma 4 and its proof. The following draws on
Darling (1952), Gnedenko and Kolmogorov (1954), Feller (1971), Logan et al. (1973), Jakubowski (1993),
Jakubowski (1997), Davis and Hsing (1995), Malevergne et al. (2009), Gabaix (2011) and Durrett (2019).
Recall, the sizes S1, . . . , SN are drawn i.i.d. from a distribution for which the tail follows a power law, with
tail index, µ > 0. Note that the first and second moments can potentially diverge
E(S) =
Z ∞
1
sµs−µ−1ds =
Z ∞
1
µs−µds =
µ
1 −µs1−µ
ˇˇˇˇ
∞
1
=







∞
for µ ∈(0, 1]
−
µ
1 −µ
for µ ∈(1, ∞)
(87)
E(S2) =
Z ∞
1
s2µs−µ−1ds =
Z ∞
1
µs1−µds =
µ
2 −µs2−µ
ˇˇˇˇ
∞
1
=







∞
for µ ∈(0, 2]
−
µ
2 −µ
for µ ∈(2, ∞)
(88)
as a result of (87) and (88), E(S) is bounded for µ > 1, while V(S) is bounded for µ > 2. The literature
refers to the cases µ ≤2 as thick tail regimes since the variance is infinite, rendering extreme tail events
more likely. In light of this, there are some important cases to distinguish from one another when considering
the limiting behavior of hN,µ, which are outlined in Table 6 below.
Table 6: Limiting Behavior of the Asymptotic Herfindahl Index
Tail
index
regime
Tail variation
First
moment
Variance
Op pgN,µq
Case I
µ > 2
Exponential
E(S) < ∞
V(S) < ∞
1
?
N
Case II
µ = 2
Regularly
varying
E(S) < ∞
V(S) = ∞
c
log(N)
N
Case III
µ ∈(1, 2)
Regularly
varying
E(S) < ∞
V(S) = ∞
1
N1−1
µ
Case IV
µ = 1
Regularly
varying
E(S) = ∞
V(S) = ∞
1
log(N)
Case V
µ ∈(0, 1)
Regularly
varying
E(S) = ∞
V(S) = ∞
Θp(1)
Case VI
µ →0
Slowly
varying
E(S) = ∞
V(S) = ∞
Θp(1)
51


---

The Herfindahl is given by
hN,µ =
N
X
i=1
S 2
i =
N
X
i=1
˜
Si
PN
j=1 Sj
¸2
,
(89)
and the object of interest is the asymptotic Herfindahl and from (89), it can readily be written as
hµ := lim
N→∞hN,µ = lim
N→∞
N
X
i=1
˜
Si
PN
j=1 Sj
¸2
= lim
N→∞
1
N
N−1 PN
i=1 S2
i
´
N−1 PN
j=1 Sj
¯2 := lim
N→∞
1
N
aN
bN
.
(90)
In Case I, when E(S), E(S2) < ∞, the usual LLN and continuous mapping theorem gives us aN
p→
a = E(S2) and bN
p→b = pE(S)q2. Therefore, hN,µ →hµ = 0, for thin tailed regimes.20 We will skip
further details regarding Cases II-IV and state Lemma 4 which is pertaining to Cases V and VI.
Lemma 4 Under Assumption 4 (ii.), we have that
a
hN,µ = ||S||2= Θp(1)
for
µ ∈[0, 1).
(91)
Proof of Lemma 4: Note that P(S > s) = s−µ and hence, P(S−µ > s) = s. Or, put differently
P(S−µ > s) ∼U[0, 1]; which is equivalently denoted as Ui := 1−FS(si) = s−µ
i
, where FS(si) denotes the
CDF of si. As a result, U1, . . . , UN are an i.i.d. sample from U[0, 1]. It is well known that order statistics,
denoted as U(i) = 1 −FS(s(i)), of the uniform distribution on the unit interval have marginal distributions
belonging to the Beta distribution family. Hence, the PDF of the ith order statistic, U(i),N ∼Beta(α, β),
with α = i and β = N −i+1. Finally, the size of the ith largest unit out of N can be found by manipulating
the expected value of the ith order statistic, given by
E(U(i),N) = E(S−µ
(i),N) =
α
α + β =
i
N + 1,
(92)
hence, the size of the ith largest unit is
S(i),N =
ˆ
i
N + 1
˙−1
µ
≃
ˆ i
N
˙−1
µ
,
(93)
where the approximation is negligible for large N. Furthermore, S2
i has tail index µ
2 ≤1, since P(S2 >
20As we saw in (unreported) simulation evidence, a Herfindahl converging to zero in the large N limit, should not rule out
identification by GIV; although theoretically it does. As illustrated in Remark 4, the variance of the elasticities diverges.
52


---

s) = P(S > s
1
2 ) = s−µ
2 . Plugging (93) into (90), we obtain
lim
N→∞
1
N
N−1 PN
i=1 S2
i
´
N−1 PN
j=1 Sj
¯2 = lim
N→∞
1
N
N−1 PN
i=1
ˆ i
N
˙−2
µ
´
N−1 PN
j=1 Sj
¯2
= lim
N→∞
1
N2
1
N−2
µ
PN
i=1 i−2
µ
´
N−1 PN
j=1 Sj
¯2
= lim
N→∞
1
N2−2
µ
P∞
i=1 i−2
µ
ˆ
1
N1−1
µ
P∞
j=1 j−1
µ
˙2 = lim
N→∞
1
N2−2
µ
P∞
i=1 i−2
µ
1
N2−2
µ
´P∞
j=1 j−1
µ
¯2 = lim
N→∞
P∞
i=1 i−2
µ
´P∞
j=1 j−1
µ
¯2
=
ζ( 2
µ)
´
ζ( 1
µ)
¯2
(94)
Where ζ(·) denotes the Riemann-zeta function. Therefore, we have just showed that for µ ∈(0, 1), hN,µ →
hµ > 0.
■
C.
Estimating the Number of Factors
Generally, since the number of factors, r, is unknown we must estimate it. There are many estimators
for r in static approximate factor models. Some examples are Bai and Ng (2002), Onatski (2010) and
Ahn and Horenstein (2013). We make use of the ER(k) and GR(k) estimators proposed by Ahn and
Horenstein (2013) (hereafter AH), which have been shown to outperform the existing estimators in the
literature, particularly when the idiosyncratic errors are not i.i.d., which is likely to be the more relevant
case.
The estimators below can be used in (12) for estimation of the demand elasticity without affecting infer-
ence, and in Algorithm 1, 2, or 3 for estimation of the supply elasticity; again without affecting inference.
The AH estimators are given by maximizing the following criteria
ER(k) =
˜µNT,k
˜µNT,k+1
k = 1, . . . , kmax
(95)
GR(k) = ln rV (k −1)/V (k)s
ln rV (k)/V (k + 1)s
=
ln(1 + ˜µ∗
NT,k)
ln(1 + ˜µNT,k+1)
k = 1, . . . , kmax,
(96)
where ˜µNT,k := ψk rXX′/(NT)s = ψk rX′X/(NT)s, X denotes a T × N matrix and ψk(A) denotes
the kth largest eigenvalue of a positive semidefinite matrix A. V (k) = Pm
j=k+1 ˜µNT,j and ˜µ∗
NT,k =
˜µNT,k/V (k). Where V (k) is the sample mean of the squared residuals from the time series regressions of
53


---

individual response variables on the first k principal components of XX′/(TN). Hence, the estimators are
prER = argmax
1≤k≤kmax
ER(k),
(97)
prGR = argmax
1≤k≤kmax
GR(k).
(98)
The basic idea behind maximizing the ER(k) and GR(k) criteria is that
˜µNT,j
˜µNT,j+1
= Op(1) for j̸ = r,
while
˜µNT,r
˜µNT,r+1
= Op(CNT ). This effective idea stems from the seminal paper of Chamberlain and Roth-
schild (1983), who, among other things, demonstrate that only the r eigenvalues arising from the common
component remain unbounded as the sample size tends to infinity, while those from the idiosyncratic part
remain bounded. In particular, see their Theorem 4. Lastly, some recommendations on the choice of kmax
are provided by AH to avoid choosing pr < r wpa 1.
The important fact is that the limiting distribution of the elasticities remain unchanged so long as we
use a consistent estimator for r. Let pϕ j
pr , for j = s, d, denote the FGIV or efficient GMM estimator, using
a consistent estimator for r, such as the AH estimator. It is easy to show that pϕ j
pr has the same limiting
distribution as pϕ j
r , for j = d, s:
P
´?
T(pϕ j
pr −ϕ j) ≤x
¯
= P
´?
T(pϕ j
pr −ϕ j) ≤x|pr = r
¯
· P(pr = r)
+ P
´?
T(pϕ j
pr −ϕ j) ≤x|pr̸ = r
¯
· P(pr̸ = r)
(99)
→P
´?
T(pϕ j
pr −ϕ j) ≤x|pr = r
¯
(100)
= P
´?
T(pϕ j
r −ϕ j) ≤x
¯
.
(101)
From (99) to (100) we make use of the fact that pr is a consistent estimator for r, i.e. P(pr = r) →1. From
(100) to (101) we make use of the fact that conditional on pr = r, pϕ j
pr = pϕ j
r . Therefore,
ˇˇˇˇP
´?
T(pϕ j
pr −ϕ j) ≤x
¯
−P
´?
T(pϕ j
r −ϕ j) ≤x
¯ ˇˇˇˇ →0.
(102)
D.
Estimation of the High-Dimensional Precision Matrix via ℓ1-Penalized
Bregman Divergence
An alternative to using the POET like procedure of Fan et al. (2013) to estimate a high dimensional
precision matrix is to use graphical Lasso methods, as in Friedman et al. (2008). One thought would be to
54


---

directly estimate the precision matrix using graphical models, say by applying the graphical Lasso procedure
to the composite error, vit = λ′
iηt + uit, or by using a local (nodewise) graphical method as in Callot et al.
(2021) and applying to it vit.
However, these approaches rule out the presence of an approximate factor structure, as they assume
unconditional sparsity of the composite error term vit. It is clear that sparsity of vit fails given our (pervasive)
factor structure, as pointed out by Barigozzi et al. (2018), Brownlees et al. (2018) and Koike (2020).
An alternative, hybrid, approach to estimation of high dimensional covariance matrices is to adopt an
approximate factor structure, thereby decomposing the process into a low rank part (common component),
plus a sparse part (idiosyncratic component) like the approach we adopted in the main text of the paper.
Except now we will use a graphical model in estimation of the precision matrix, as opposed to the POET
estimation procedure. Thus, we can employ a hybrid approach known as the factor-adjusted graphical lasso
model or simply FGL of Lee and Seregina (2021). The FGL approach imposes conditional sparsity similar
to POET with the exception that sparsity is imposed on the precision matrix, Σ−1
u , of the idiosyncratic term
rather than the covariance matrix, Σu. That is, once the low dimensional common factors are conditioned
on, Σ−1
u
is assumed to be sparse in the sense that many of the off-diagonal elements are zero. Note that with
FGL, sparsity is assumed on the precision matrix, Σ−1
u , for the idiosyncratic term and not on the precision
matrix of the composite error, Σ−1
v
as in a traditional graphical method.
Along the POET procedures, Fan et al. (2013), Fan et al. (2018) and Bai and Liao (2017) amongst others,
estimate the high dimensional covariance matrix via thresholding techniques and then invert the estimate to
obtain an estimate of the precision matrix. Whereas, graphical methods directly estimate the precision
matrix. The FGL approach is essentially a hybrid of the two approaches. We adopt the FGL approach
of Lee and Seregina (2021), although in their paper endogeneity is not a concern. To that end, suppose
momentarily that the idiosyncratic error is observed
uit = yit −λ′
iηt −ϕspt,
= yit −ψ′
if t,
(103)
where ψi :=
´
λ′
i
ϕs
¯′
and f t is defined as in the main text. We apply the graphical Lasso procedure
of Friedman et al. (2008) to (103), to obtain pΣ
−1
u
as the solution to the ℓ1-penalized Bregman Divergence.
Bregman divergence is simply a measure of distance between two objects defined in terms of a strictly
convex function, say f(·). Introduce S++ as the set of symmetric positive definite matrices, then, for A1,
55


---

A2 ∈S++, the Bregman Divergence in this context, is defined as
df(A1, A2) := f(A1) −f(A2) −⟨∇f(A2), A1 −A2⟩
(104)
where f(·) is strictly convex and continuously differentiable. The Bregman Divergence, df, can be viewed
as the difference of f(A1) from the first-order approximation of f(A1) around A2. Moreover, (104) nests
some important loss functions as special cases for particular choices of f(·), e.g. when f(x) = x′Bx, df
becomes the Mahalanobis distance, which reduces to the squared norm when B = I and when f(x) =
P
i xilog xi, we obtain df as the Kullback-Leibler divergence. When one sets f(A) = −log det(A), then
∇f(A) = −A−1
2 ,21 and the Bregman Divergence takes the following familiar form for A1 = Σ−1
u
and
A2 = pΣ
−1
u
df(Σ−1
u , pΣ
−1
u ) = −log det(Σ−1
u ) + ⟨pΣu, Σ−1
u
−pΣu⟩+ c1
= −log det(Σ−1
u ) + tr(pΣuΣ−1
u ) + c2
(105)
where (105) can be viewed as the negative Gaussian log-likelihood of the data, partially maximized with
respect to the mean parameter. Adding an ℓ1-penalty on the off-diagonal elements of Σ−1
u
to (105) gives us
pΣ
−1
u
as the solution to the ℓ1-penalized Bregman Divergence
pΣ
−1
u (ρ) = arg min
Σ
−1
u ∈S++
{−log det(Σ−1
u ) + tr(pΣuΣ−1
u ) + ρ||Σ−1
u ||1},
(106)
where ρ is the tuning hyperparameter and only here ||Σ−1
u ||1:= P
i̸=j|Σ−1
u,ij| is defined to not penalize the
diagonal elements. The routine can be easily implemented in the R package glassoFast or CVglasso.
However, as noted in Janková and van de Geer (2018), there are theoretical and practical benefits to
modify (106) to the so-called weighted FGL (effectively just adaptive Lasso)
pΣ
−1
u (ρ) = arg min
Σ
−1
u ∈S++
{−log det(Σ−1
u ) + tr(pΣuΣ−1
u ) + ρ
X
i̸=j
x
Wiix
Wjj|Σ−1
u,ij|},
(107)
where x
W
2 = diag(pΣu). We suggest iterating between estimation of Σ−1
u
by optimizing (107) with the
graphical Lasso algorithm and estimation of ϕs(z, Σ−1
u ) as in (15) in Algorithm 3′ below. For each iteration,
we optimally select the penalty hyperparameter, ρ, via cross-validation.
21See Section A.4.1 of Boyd and Vandenberghe (2004) for an elegant derivation of this gradient.
56


---

We do not explore the theoretical properties of the sampling error induced by this weighted FGL estima-
tion procedure, but in some unreported Monte Carlo evidence we find that it performs well. The algorithm
below details the overidentified estimation procedure for the case when kx = 0.
Algorithm 3′ Efficient GMM-FGL for ϕs (when kx = 0):
• Step 1: Run PCA on (9) and obtain pzt = S′ p
Qry·t as the sample counterpart of (10).
• Step 2: Initialize pΣ
−1
u
= IN.
• Step 3: Estimate (21) to obtain pε, initialize x
W s = ( pZ
′
s pZs)−1 and obtain pθ
s
2SLS( pZs, pΣ
−1
u ).
• Step 4: Obtain y pE(pΣ
−1
u ).
• Step 5: Update x
W s =
´
1
T
PT
t=1 pZst pZ
′
stpu2
pEt
¯−1
, where pu pEt = y pEt −pθ
s
GMM( pZs, pΣ
−1
u )′f t and
construct pθ
s
GMM( pZs, pΣ
−1
u ) as in (22).
• Step 6: Construct the sample counterpart of (103) to update pΣ
−1
u
via (107) and update y pE(pΣ
−1
u ).
• Step 7: Iterate Step 4 through Step 6 until convergence.
Note, to obtain p
ψi in the sample counterpart of (103), we have pΛ = T −1y′
.. pη and pϕs
GMM is an element of
pθ
s
GMM. In view of Algorithm 2, Algorithm 3′ can be further extended to the case when kx > 0. However,
for brevity we omit the details.
References for Supplemental Appendices
Ahn, S. C. and A. R. Horenstein (2013). “Eigenvalue ratio test for the number of factors”. Econometrica 81.3, pp. 1203–1227.
Bai, J. and Y. Liao (2017). “Inferences in panel data with interactive effects using large covariance matrices”. Journal of Economet-
rics 200.1, pp. 59–78.
Bai, J. and S. Ng (2002). “Determining the number of factors in approximate factor models”. Econometrica 70.1, pp. 191–221.
Barigozzi, M., C. Brownlees, and G. Lugosi (2018). “Power-law partial correlation network models”. Electronic Journal of Statistics
12.2, pp. 2905–2929.
Boyd, S. and L. Vandenberghe (2004). Convex Optimization. Cambridge University Press.
Brownlees, C., E. Nualart, and Y. Sun (2018). “Realized networks”. Journal of Applied Econometrics 33.7, pp. 986–1006.
Callot, L., M. Caner, A. Ö. Önder, and E. Ula¸san (2021). “A nodewise regression approach to estimating large portfolios”. Journal
of Business & Economic Statistics 39.2, pp. 520–531.
Chamberlain, G. and M. Rothschild (1983). “Arbitrage, Factor Structure, and Mean-Variance Analysis on Large Asset Markets”.
Econometrica 51.5, pp. 1281–1304.
Darling, D. (1952). “The influence of the maximum term in the addition of independent random variables”. Transactions of the
American Mathematical Society 73.1, pp. 95–107.
Davis, R. A. and T. Hsing (1995). “Point process and partial sum convergence for weakly dependent random variables with infinite
variance”. The Annals of Probability 23.2, pp. 879–917.
Durrett, R. (2019). Probability: Theory and Examples. Vol. 49. Cambridge University Press.
57


---

Fan, J., Y. Liao, and M. Mincheva (2013). “Large covariance estimation by thresholding principal orthogonal complements”. Jour-
nal of the Royal Statistical Society. Series B, Statistical methodology 75.4.
Fan, J., H. Liu, and W. Wang (2018). “Large covariance estimation through elliptical factor models”. Annals of Statistics 46.4,
pp. 1383–1414.
Feller, W. (1971). An Introduction to Probability Theory and Its Applications Vol II. John Wiley and Sons.
Friedman, J., T. Hastie, and R. Tibshirani (2008). “Sparse inverse covariance estimation with the graphical lasso”. Biostatistics 9.3,
pp. 432–441.
Gabaix, X. (2011). “The granular origins of aggregate fluctuations”. Econometrica 79.3, pp. 733–772.
Gnedenko, B. V. and A. N. Kolmogorov (1954). Limit Distributions for Sums of Independent Random Variables.
Jakubowski, A. (1993). “Minimal conditions in p-stable limit theorems”. Stochastic Processes and Their Applications 44.2, pp. 291–
327.
—
(1997). “Minimal conditions in p-stable limit theorems—II”. Stochastic Processes and Their Applications 68.1, pp. 1–20.
Janková, J. and S. van de Geer (2018). “Inference in high-dimensional graphical models”. Handbook of Graphical Models. CRC
Press. Chap. 14, pp. 325–351.
Koike, Y. (2020). “De-biased graphical Lasso for high-frequency data”. Entropy 22.4, p. 456.
Lee, T.-H. and E. Seregina (2021). “Optimal Portfolio Using Factor Graphical Lasso”. arXiv:2011.00435.
Logan, B. F., C. Mallows, S. Rice, and L. A. Shepp (1973). “Limit distributions of self-normalized sums”. The Annals of Probability
1.5, pp. 788–809.
Malevergne, Y., P. Santa-Clara, and D. Sornette (2009). Professor Zipf goes to Wall Street. Tech. rep. National Bureau of Economic
Research.
Onatski, A. (2010). “Determining the number of factors from empirical distribution of eigenvalues”. The Review of Economics and
Statistics 92.4, pp. 1004–1016.
58
