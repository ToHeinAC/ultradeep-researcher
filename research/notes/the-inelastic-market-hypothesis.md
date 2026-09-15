---
title: 'The Inelastic Market Hypothesis:'
id: the-inelastic-market-hypothesis
tags:
- apple-earnings-durability-thesis-b8b3f1
created: '2026-09-12T17:38:17.213561Z'
updated: '2026-09-15T19:32:22.084395Z'
source: https://arxiv.org/abs/2108.00242
source_domain: arxiv.org
fetched_at: '2026-09-12T17:38:17.213271Z'
fetch_provider: crawl4ai
status: review
type: note
tier: institutional
content_type: paper
deprecated: false
summary: Bouchaud's Liquidity Theory reinterpretation of the Gabaix-Koijen multiplier.
  Agrees M is of order unity (flows matter far more than efficient-market theory allows)
  but attributes it to price impact, not inelastic demand. Predicts M ~1 at a monthly
  horizon and M proportional to volatility/volume, implying SMALLER multipliers for
  high-volume mega-caps such as Apple.
raw_file: raw/the-inelastic-market-hypothesis.pdf
doi: arXiv:2108.00242
---

*Suggested by [[in-search-of-the-origins-of-financial-fluctuations-the-inelastic-markets-hypothe]] — critique/reinterpretation of the inelastic markets multiplier*

The Inelastic Market Hypothesis:
A Microstructural Interpretation
Jean-Philippe Bouchaud
Capital Fund Management, 23 rue de l’Université, 75007 Paris
Chair of Econophysics and Complex Systems,
Ecole polytechnique, 91128 Palaiseau Cedex, France
Académie des Sciences, Quai de Conti, 75006 Paris
January 2022
Abstract
We attempt to reconcile Gabaix and Koijen’s (GK) recent Inelastic Market Hypothesis (IMH) with the
order-driven view of markets that emerged within the microstructure literature in the past 20 years. We
review the most salient empirical facts and arguments that give credence to the idea that market price
ﬂuctuations are mostly due to order ﬂow, whether informed or non-informed. We show that the Latent
Liquidity Theory of price impact makes a precise prediction for GK’s multiplier M, which measures by
how many dollars, on average, the market value of a company goes up if one buys one dollar worth of
its stocks. Our central result is that M is of order unity, as found by GK, and increases with the volatility
of the stock and decreases with the fraction of the market cap. traded daily. We discuss several empirical
results suggesting that the lion’s share of volatility is due to trading activity. We argue that the IMH holds
for all asset classes, beyond the case of stock markets considered by GK.
1
Introduction
Traditionally, market prices are considered to reﬂect the fundamental value (of a stock, currency, com-
modity, etc.), up to small and short-lived mispricings. In this way, a ﬁnancial market is regarded as a
measurement apparatus that aggregates all private estimates of an asset’s true (but hidden) value and,
after a quick and efﬁcient digestion process, provides an output price. In this view, private beliefs should
only evolve because of the release of a new piece of information that objectively changes the value of
the asset. Prices are then martingales because (by deﬁnition) new information cannot be anticipated or
predicted. In this context, neither microstructural effects nor the process of trading itself can affect prices,
except perhaps on very short time scales.
This Platonian view of markets is fraught with a wide range of difﬁculties that have been the subject
of thousands of academic papers in the last 40 years. The most well-known of these puzzles is the excess-
volatility puzzle [1, 2]: prices move around too much to be explained solely in terms of ﬂuctuations of the
fundamental value. But there is also the excess-trading puzzle [3] and the trend-following puzzle (see
e.g. [4–6] and refs. therein): Investors trade far too much and price returns tend to be positively auto-
correlated on long times scales, such as weeks to months. In other words, some information about future
price moves seems to be contained in the past price changes themselves. This is in stark contradiction
with the efﬁcient market story.
Faced with these puzzles, research in the 1980s proposed to break away from the strict orthodoxy
of rational market participants, and to instead introduce a new category of uninformed agents (or noise
traders) [2, 7, 8]. Including such noise traders allows one to account for excess trading. In fact, as
illustrated by the Kyle [9] and Glosten–Milgrom [10] models, the existence of noise traders is crucial for
liquidity providers to a least break even — without them, liquidity would vanish and markets would not
even function. However, in these models, prices still do not deviate from fundamentals: noise traders
1
arXiv:2108.00242v5  [econ.GN]  11 Jan 2022


---

do participate in the price-formation process, but the impact of their trades does not contribute to price
volatility [9] – only “true” information can change prices.
After accepting the presence of non-rational agents, the next conceptual step is to accept that all trades
(informed or random, large or small) possibly contribute to long-term volatility. This corresponds to a
paradigm change: instead of fundamental value determining prices, the main driver of price changes is
the order ﬂow itself — whether informed or random, trades will move prices. This is the order-driven view
of markets, that progressively emerged in the last 20 years, motivated by several empirical facts obtained
using microstructural data [11–19], to be recalled below.
At least naively, the order-driven theory of price changes offers a solution to the excess-volatility puzzle:
if trades by themselves move prices, then excess trading could create excess volatility (see section 5). It
is also likely to be the mechanism for the universal trend-following effect mentioned above, and would
allow one to understand why self-exciting feedback effects are so prevalent in ﬁnancial markets, leading
to bursts of volatility even in the absence of any news [20–23]. In fact, calibrating – say – self-exciting
Hawkes models on data leads to the conclusion that a very large fraction (≳80%!) of market activity and
volatility is self-generated, rather than exogenous [24–26].
Ironically, although appealing to professional traders, quantitative hedge funds (like CFM) and the
layperson observing the stock market, the order-driven scenario where trade ﬂows impact prices is viewed
as “sadly illiterate” by most ﬁnancial economists. As Rich Lyons noted in his seminal book [13]: Consider
an example that clariﬁes how economist and practitioner worldviews differ. The example is the timeworn
reasoning used by practitioners to account for price movements. In the case of a price increase, practitioners
will assert “there were more buyers than sellers”. Like other economists, I smile when I hear this. I smile
because in my mind the expression is tantamount to “price had to rise to balance demand and supply”.
Yet the situation may start to shift in the wake of the rather awesome recent paper by Xavier Gabaix
and Ralph Koijen (GK), entitled “In Search of the Origins of Financial Fluctuations: The Inelastic Markets
Hypothesis” [27]. Based both on an empirical analysis of the long term price response to funds’ order ﬂow
and on an equilibrium model of the holdings of mandate-constrained investment ﬁrms, the authors argue
quite convincingly in favour of the order-driven scenario and debunk many dissenting arguments based
on the traditional lore. The central result of GK is that buying (or selling) 1$ of an individual stock on
average increases (decreases) the market capitalisation of that stock by M$ in the long run, with M ≈1
even for uninformed trades. Buying the market as a whole (i.e. the index or a basket of stocks) has an even
larger impact, with M ≈5. The multiplier M is therefore very substantial, when rational models would
predict that uninformed trades should move the price only very mildly (i.e. M ≈0.01, see [27]), if at all.
The GK story is based on global equilibrium considerations, as their “undergraduate example” illus-
trates: When an investor sells one dollar of bonds to invest in a representative asset manager with a
mandate of keeping 80 % of its investments in stocks, the price of stocks has to increase, in equilibrium,
by ﬁve dollars, corresponding to M = (1 −80%)−1 = 5. However, the actual mechanism through which
the price adjusts is left unspeciﬁed. This is where market microstructure comes into the picture. The
aim of this paper is to discuss how the price adjustment actually unfolds, and why recent measures of
price impact at the daily time scale, when correctly interpreted, are quantitatively compatible with GK’s
value of the multiplier M. We believe that our reconciliation of high frequency liquidity (i.e. the realm
of microstructure) and low frequency equilibrium (i.e. quarterly or longer, as studied by GK) is quite
remarkable and gives strong credence to the order-driven/inelastic theory of markets.
2
High Frequency Price Impact
2.1
Two Sides to the Coin
Buy trades (i.e. market orders hitting the ask) tend to push the price up and sell trades (i.e. market orders
hitting the bid) tend to push the price down. This is price impact, and is an all-too-familiar reality for
traders who need to buy or sell large quantities of an asset. To these traders, price impact is tantamount
to a cost, because the impact of their earlier trades makes the price of their subsequent trades worse on
average.
In much of the existing literature, there are two strands of interpretation for price impact, which reﬂect
the great divide between the efﬁcient-market story and the order-driven story [19]. At the two extremes
of this spectrum are the following scenarios:
2


---

1. Agents successfully forecast short-term price movements, and trade accordingly. This is the efﬁcient-
market point of view (see e.g. [12]), which asserts that a trader who believes that the price is likely
to rise will buy in anticipation of this price move, as in Kyle’s model [9]. In this framework, a noise-
induced trade that is based on no information at all can only have a short term impact on prices —
otherwise, prices would not behave as nearly perfect random walks as they do, and would end up
straying very far from their fundamental values.
By this interpretation, if the price was meant to move due to information, it would do so even
without any trades.
2. Price impact is a reaction to order-ﬂow imbalance. This is the order-driven view, which asserts that
even if a trade reﬂected no information in any reasonable sense, then price impact would still occur
and contribute to the long-term volatility.
In the ﬁrst story, trades reveal private information about the fundamental value, creating a so-called
price discovery process. In the second story, the act of trading itself impacts the price. In this case, one
should remain agnostic about the information content of the trades, and should therefore speak of price
formation rather than price discovery. But if market participants believe that the newly established price
is the “right” price and act accordingly by revising their reservation price, “information revelation” might
simply be a self-fulﬁlling prophecy. In section 5, we will discuss several empirical results which suggest that
the amount of information per trade is actually very small, strongly favouring the order-driven scenario.
2.2
The Square-Root Law
In fact, traders or trading algos do not execute large trades via single market orders, but instead split up
their trades into many small pieces. These pieces are executed incrementally, using market orders, limit
orders, or both, over a period of several minutes to several days. The collection of all such individual
orders belonging to the same trading decision is usually called a metaorder. How much does a metaorder
of total volume Q, executed over a period of duration T, affect the price on average? Naively, it might
seem intuitive that the impact of a metaorder should scale linearly in Q. Perhaps surprisingly, empirical
analysis reveals that in real markets, this scaling is not linear, but rather is approximately square-root.
2.2.1
Empirical Evidence
Since the early 1980s, a vast array of empirical studies spanning both academia and industry have con-
cluded that the impact of a metaorder scales approximately as the square-root of its size Q — see [19] for
a recent review and an extensive list of references. This result is reported by studies of different markets
(including equities, futures, FX, options, and even Bitcoin), during different epochs (including pre-2005,
when liquidity was mostly provided by market-makers, and post-2005, when electronic markets became
dominated by HFT), in different types of microstructure (including both small-tick stocks and large-tick
stocks), and for market participants that use different underlying trading strategies (including fundamen-
tal, technical, and so on) and different execution styles (including using mostly market orders, a mix of
limit orders and market orders, or mostly limit orders, as in [28]).
In all of these cases, the average (relative) price change between the beginning and the end of a
metaorder with volume Q is well-described by the “square-root law”:
I(Q, T) ≈Y σT
v
t Q
VT
,
(Q ≪VT)
(1)
where Y is a numerical coefﬁcient of order 1 (Y ≈0.5 for US stocks), σT is the contemporaneous volatility
on the time horizon T, and VT is the contemporaneous volume traded over time T. The square-root law
of metaorder impact is well-established empirically, but there are several features that make it extremely
surprising theoretically, at least at ﬁrst sight. Before we discuss these surprising aspects, let us note that as
with any empirical law, the square-root impact law holds (approximately) in the regime of intermediate
execution horizons T (not too fast nor too slow) and small enough volume fractions Q/VT, which is the
regime usually adopted by investors and execution algos in normal trading conditions (see [19] for more
on this). Different behaviours should be expected outside of these regimes, although data to probe these
regions is scarce, and the corresponding conclusions currently remain unclear.
3


---

2.2.2
Two Surprising Features
The ﬁrst surprising feature of Equation (1) is that metaorder impact does not scale linearly with Q — or,
said differently, that metaorder impact is not additive. Instead, one ﬁnds empirically that the second half
of a metaorder impacts the price much less than the ﬁrst half. But this can only be the case if there is some
kind of liquidity memory time Tm, such that the inﬂuence of past trades cannot be neglected for T ≪Tm
and vanishes for T ≫Tm, when all memory of past trades is lost. One therefore expects that beyond Tm,
impact must become linear in Q. This is indeed what one ﬁnds within a model describing the dynamics
of liquidity, which reproduces the square-root law at short times and a linear impact law at longer time
– see section 3 below. The memory time Tm will turn out to be very important to weld together the high
frequency regime described in this section and the low frequency regime considered by GK.
The second surprising feature of Equation (1) is that Q does not appear as a fraction of the total market
capitalization M of the asset (as might be naively anticipated) but instead as a fraction of the total volume
VT traded during the execution time T. In current equities markets, M is typically about 200 times larger
than VT for T =1 day. Therefore, the impact of a metaorder is much larger than if the ratio Q/VT in Eq.
(1) was instead Q/M.1 The square-root behaviour for Q ≪VT also substantially ampliﬁes the impact of
small metaorders: executing 1% of the daily volume moves the price (on average) by
p
1% = 10% of its
daily volatility, 10 times larger than the naive, linear estimate.
The main conclusion here is that even relatively small metaorders cause surprisingly large impact. In
fact, the GK multiplier measured in that regime would be uncannily high: taking T = 1 day, σT = 2.5% (a
typical value for single stocks, corresponding to an annual volatility of ≈40%) and Q = 1%VT = 510−5M
leads to I(Q, T) ≈1.2510−3 or M = 25. However, since impact is proportional to
p
Q and not Q, GK’s
multiplier is meaningless in the regime T ≪Tm. As we will discuss in section 4, the square-root impact
contribution is mostly transient, while the permanent part (which survives for T ≫Tm) is linear and
characterized by M of order unity, as indeed found by GK.
2.2.3
Possible Measurement Biases
The impact of a metaorder I(Q, T) can be affected by several artifacts and biases. One of the recurrent
criticism is that metaorders are not exogenous, and possibly conditioned on trading signals (see e.g. sec-
tion 3.1 below) and/or on the price moves during the execution interval T. However, several arguments
suggest that although such effects may in some cases considerably affect the measured impact curve, most
of the data analyzed in the literature can be trusted. For one thing, CFM’s proprietary data allows one to
eliminate many of these biases, since the strength of the trading signal is known and can be factored in the
regression. The fact that our own estimates of the square-root law precisely matches the ones reported
in the literature (e.g. [28, 29]), or the one that we measured using the Ancerno database containing
metaorders issued by long term investors [30, 31], is a strong argument in favour of the validity of the
square-root law.2 As noted above, the same square-root law has been reported for a large variety of ﬁnan-
cial markets, including option markets [32] or Bitcoin [34], suggesting a universal underlying mechanism
which we discuss in section 3 below. We have actually shown that the short term impact of CFM’s trades
is indistinguishable from the trades of the rest of the market [35], or, for that matter, from purely random
trades that were studied at CFM during a speciﬁcally designed experimental campaign in 2010-2011.
3
The Origin of the Square-Root Law
3.1
Early Theories
Since the mid-nineties, several stories have been proposed to account for the square-root impact law. The
ﬁrst attempt, due to the Barra Group [36] and Grinold & Kahn [37] argues that the square-root behaviour
is a consequence of market-markers being compensated for their inventory risk (see also [38]). The
1In the eighties, the lore was that trading 2% of the daily volume, i.e. 0.01% of the market cap, would maybe move the price by a
totally negligible 0.01%. The Black-Scholes Delta-hedge induced crash of October 1987 was a dour wake-up call that impact is in fact
not a small effect. See e.g. Treynor, J. L. (1988). Portfolio Insurance and Market Volatility. Financial Analysts Journal, 44(6), 71-73.
2As a further important argument, note that the square-root law does not only describe the impact of the fully executed metaorder
of volume Q, but the whole impact path I(q, t) during execution, as a function of the partially executed volume q ∈[0,Q] and
t ∈[0, T] [19, 33].
4


---

reasoning is as follows. Assume that a metaorder of volume Q is absorbed by market-makers who will
need to slowly ofﬂoad their position later on. The amplitude of a potentially adverse move of the price
during this unwinding phase is of the order of σT
p
Toff/T, where Toff is the time needed to ofﬂoad an
inventory of size Q. It is reasonable to assume that Toff is proportional to Q and inversely proportional to
the trading rate of the market VT/T, giving Toff/T = Q/VT. If market-makers respond to the metaorder
by moving the price in such a way that their proﬁt is of the same order as the risk they take, then it would
follow that I = Y σT
p
Q/VT, as found empirically. However, this story assumes no competition between
market-makers. Indeed, inventory risk is diversiﬁable over time, and in the long run averages to zero.
Charging an impact cost compensating for the inventory risk of each metaorder would lead to formidable
proﬁts and would necessarily attract competing liquidity providers, eventually leading to a Y coefﬁcient
much smaller than 1, at variance with empirical results, for which Y = O(1).
Another theory, proposed by Gabaix et al. [39], ascribes the square-root impact law to an information
revelation effect, i.e. to the fact that trades are conditioned by some short-term predictability. One can
show that in the presence of a short-term signal and linear impact, the optimal execution horizon T ⋆for
metaorders of size Q grows like T ⋆∼
p
Q (see [19], section 21.2.3 for a detailed derivation). This theory
argues that since the price is expected to move in the direction of the trade during T ⋆(as information is
revealed), the peak impact itself behaves as
p
Q. However, this scenario would imply that the impact path
is linear in the executed quantity q, whereas the full impact path in fact also behaves as a square-root of
q [19, 33]. Furthermore, most metaorders – in particular those of CFM – correspond at best to long term
predictions, with very little short term “alpha” that would move the price of times scales T ≲1 day.
More recently, Farmer et al. [40] proposed yet another theory that is very reminiscent of the Glosten–
Milgrom model, which argues that the size of the bid–ask spread is actually set competitively. The the-
ory assumes that metaorders arrive sequentially, with a volume Q distributed according to a power-law.
Market-makers attempt to guess whether the metaorder will continue or stop at the next time step, and
set the price such that it is a martingale and such that the average execution price compensates for the
information contained in the metaorder (this condition is sometimes called “fair-pricing”). If the distri-
bution of metaorder sizes behaves precisely as Q−5/2, these two conditions lead to a square-root impact
law. Although enticing, this theory has difﬁculty explaining why the square-root impact law appears to
be much more universal than the distribution of the size of metaorders or of the autocorrelation of trade
signs. For example, the square-root law holds very precisely in 2013 Bitcoin markets, where the distribu-
tion of metaorder sizes behaves as Q−2, rather than Q−5/2, and at a time where market making was much
less competitive [34].
3.2
The Latent Liquidity Theory
Finally, Tóth et al. [41] proposed an alternative theory based on a dynamical description of supply and
demand, called the Latent Liquidity Theory (LLT). This approach, developed further in several papers
[42–48], provides a natural statistical interpretation for the square-root law and its apparent universality.
It also makes further predictions, in particular concerning the decay of impact once the metaorder has
been executed [44, 46]. This is a piece of information that turns out to be crucial for recovering GK’s
multiplier at long times, about which the theories recalled above make substantially different predictions
compared to LLT.
A full discussion of the Latent Liquidity Theory is much beyond the scope of the present paper, and the
reader is referred to [19] for a detailed account and the Appendix for a short summary of its mathematical
formulation. In a nutshell, the theory assumes that each long term investor in the market has a reservation
price (to buy or to sell) that he or she updates as a function of time, due to incoming news, price changes,
noise, etc. The collection of all these trading intentions constitutes the available liquidity at any instant
of time – although most of it remains “latent”, i.e. is not immediately posted in the public order book.
When the market price hits the reservation price of a given buy (sell) investor, his/her order is executed
and becomes a sell (buy) intention, but at a price signiﬁcantly higher (lower) than the execution price.
(The theory does not consider HFT liquidity, which cannot provide much resistance to metaorders with
an execution time T longer than a few minutes).
Reservation prices remain sticky during a typical memory time Tm and, when revised, have a tendency
to distribute themselves around the new, updated market price (see [44], Appendix for a detailed dis-
cussion of this point). This assumption means that investors tend to mix their own price estimate with
the market price, which is by itself a source of information about what other investors believe. Such an
5


---

assumption looks very reasonable. Following Black’s intuition [7], fundamental value is so vaguely known
(only up to a factor two says Black3) that no one can really claim to know better than others, so some
realignment of beliefs around the market price must take place (statistically speaking, of course).
These are the main ingredients underpinning the LLT. On short time scales T ≪Tm, liquidity is essen-
tially static and creates barriers to price motion. But as belief realignment happens, memory of previous
intentions is erased and the impact of past trades on the price becomes permanent. Embedding these ideas
into a mathematical framework allows one to make precise predictions [19, 44], which can be summarized
as follows:
1. The impact of a metaorder of volume Q executed over some time T ≪Tm is given by the square-root
law, Eq. (1).
2. Once the metaorder is fully executed, its impact decreases with time from its peak value Eq. (1) as
a power-law of time, down to a value that depends on the information content that triggered the
trade.
3. In the absence of any information, the long-term, permanent part of the impact was explicitly com-
puted in [46] and is given by
I∞(Q, T) = 1
2σ1
p
Tm ×
Q
V1Tm
,
(2)
where the subscript “1” corresponds to 1 day and Tm is measured in days. Note that this result is
in fact independent of the execution time T, which can be large or small compared to Tm. A brief
summary of the calculation made in [46] is provided in the Appendix, where the memory time Tm
is related to the latent liquidity renewal rate ν = 1/Tm.
Hence, the permanent impact I∞(Q, T) is linear in Q, independent of T, and proportional to the
volatility on the scale of the memory time Tm, and inversely proportional to the volume traded by the
market on the same time scale, V1Tm. A simple way to understand the result of [46] is to notice that the
1/pt decay of impact, predicted in [44] and recalled in the Appendix as Eq. (13), must be interrupted
after a time ∼Tm, since any memory of the initial price is erased beyond that time. This immediately
yields Eq. (2), up to a numerical factor.
In other words, whereas the square-root impact law describes the short term, transient response of
the market to order-ﬂow, the long-term, permanent component is much smaller, and linear in Q, in agree-
ment with Almgren et al.’s early insight [29]. Note that the longer the memory time Tm, the smaller the
permanent impact. This is in line with our LLT story above: the longer market participants stick to their
beliefs, the stronger the anchor to a reference price and the smaller the long term impact. Of course, if
liquidity was inﬁnite (i.e. V1 = ∞), or if beliefs were permanent (i.e. Tm = ∞) then markets would be
perfectly elastic and transactions would not impact prices.
Finally, let us make an important remark: a very nice feature of the LLT is that any round trip incurs
a positive cost, see [44] for a proof. To wit, trading impact prices, but there is no way to construct an
arbitrage strategy out of this effect, since getting out of position would lead to a net loss.
4
The GK multiplier
We now claim that it is the long term impact, Eq. (2), that must be compared with GK’s multiplier M. As
we said above, it would not make sense to rely on Eq. (1) since (a) it is not linear in Q and (b) it only
describes the transient part of the impact, which will all but vanish on the quarterly time scale considered
by GK [27].
More precisely, assuming Q = 1%M (i.e. a total order size of 1% of the market capitalisation, but any
other number would do), the long term impact on the price expressed in percent is GK’s multiplier, hence
M = 1
2σ1
M
V1
×
v
t 1
Tm
.
(3)
3We might deﬁne an efﬁcient market as one in which price is within a factor of 2 of value, i.e., the price is more than half of value
and less than twice value. The factor of 2 is arbitrary, of course. Intuitively, though, it seems reasonable to me, in the light of sources of
uncertainty about value and the strength of the forces tending to cause price to return to value. In his introduction, Black also writes:
I recognize that most researchers [...] will regard many of my conclusions as wrong, or untestable, or unsupported by existing evidence.
[...]. In the end, my response to the skepticism of others is to make a prediction: someday, these conclusions will be widely accepted. The
inﬂuence of noise traders will become apparent.
6


---

This is the central result of the present paper. Numerically, for σ1 = 2.5% and M/V1 = 200, one ﬁnds
M = 5/
p
Tm. As noted above, the longer investors believe in their initial estimate of value and are ready
to provide liquidity at that price, the more elastic the market and the smaller the GK multiplier.
The precise value of the memory time is difﬁcult to pin down, since in fact we expect that market
participants are characterized by a broad distribution of frequencies (see Appendix). But it is plausible
that an effective value of Tm is between a few days and a few weeks, see the data analyzed in Refs.
[49, 50]. So choosing Tm = 20 (corresponding to a month of trading) seems reasonable and yields M ≈1,
as obtained by GK. But note that the innocent looking result M = O(1) turns out to be highly non-trivial,
since it results from a large factor (M/V1 ∼100) being compensated by a small factor (σ1 ∼1%)!
Our result furthermore makes falsiﬁable predictions. For example, assuming that Tm is independent
of the considered stock, we predict that the multiplier M is proportional to σ1M/V1. So one could expect
that large capitalisation stocks, for which volatility is smaller and the fraction of market caps exchanged
daily is larger, have a relatively smaller multiplier – i.e., in the language of GK, larger capitalisation stocks
are less “inelastic”.
But another plausible speciﬁcation is to posit that the memory time Tm is such that the volatility over
that time scale reaches a certain universal threshold value ∆, meaning that investors tend to realign their
beliefs when the price level has changed “appreciably”, say when ∆= 10% (corresponding to Tm = 16
days for a 2.5% daily volatility). This is tantamount to setting Tm = ∆2/σ2
1, which ﬁnally leads to4
M ∝
σ2
1
∆
M
V1
,
(4)
where ∆is now assumed to be stock independent. It would be interesting to test this prediction more
quantitatively using GK’s methodology. However, as revealed in Fig. 1, the overall range of variation
predicted by Eq. (4) turns out to be rather restricted. The multiplier M is seen to decrease by a factor
roughly equal to 2 between small cap stocks (M ∼100M$) and large cap stocks (M ∼1000B$), i.e.
when M is multiplied by 10,000. Still, with ∆= 10%, the average value of M is found to be 0.76 with a
standard deviation of 0.6, which means that the full span of variations of M is up to a factor 10, which is
consistent with the data shown in Ref. [51].
5
Discussion
5.1
Statistical Efﬁciency vs. Fundamental Efﬁciency
As is well known, asset prices are approximately martingales over time scales spanning from seconds to
weeks. Another way to state this empirical fact is to say that volatility is approximately independent of
the scale at which it is measured. In the efﬁcient market picture, this phenomenon is a consequence of
market prices only reacting to unpredictable news, and almost immediately digesting the corresponding
information content.
In practice, this explanation is hard to believe, because the fundamental value of an asset is only
known so vaguely (as Black noticed, see above) that at least some amount of short-term mispricing should
be present, even in very liquid markets. But this should induce excess short-term volatility and mean-
reversion. For example, to be compatible with observations on the S&P 500 futures contract, mispricings
must be less than 0.05% of the asset’s price and have a reversion time of only 10 minutes. How can prices
be so precise when there is so much uncertainty?
In fact, the long-range autocorrelation in order ﬂows [17, 19] is clear proof of the presence of long-lived
imbalances between supply and demand, which markets cannot immediately digest and equilibrate (as
assumed in the efﬁcient market picture) [17]. Naively, these long-lived imbalances should create trends
and mispricings. However, as argued in [19, 52, 53], these effects are mitigated by liquidity providers
who, in normal market conditions, compete to remove any exploitable price pattern and thereby buffer
these imbalances. This is essentially the content of the so-called “propagator model” [14], in which impact
decay is ﬁne-tuned to compensate the long memory of order ﬂow, and causes the price to be close to a
martingale (see also [54]). This makes prices statistically efﬁcient without necessarily being fundamentally
4Note that Eq. (4) is the result one would get from a purely dimensional analysis if one assumes that there is no particular time
scale in the problem.
7


---

Figure 1: GK’s multiplier M as predicted by Eq. (4) (with an equal sign) for 950 US stocks in 2019 and with ∆= 10%. Volatility,
average daily volume and market capitalisation are averaged over all days in 2019. With such a choice of ∆, the average value of
M is found to be 0.76 with a standard deviation of 0.6. The plain line is a cubic ﬁt as a function of log10 M, revealing a slightly
non-monotonic variation of M as a function of the market cap, perhaps increasing again for very large market caps. Note that the plot
obtained using Eq. (3) with Tm = 16 instead of Eq. (4) looks very similar.
efﬁcient. In other words, competition at high frequencies is enough to whiten the time series of returns,
but not necessarily to ensure that prices reﬂect fundamental values.
5.2
The Long Term Fate of GK’s Multiplier
Within the order-driven view of markets, high-frequency traders and market makers only seek to exploit
short term statistical arbitrage opportunities, without any long term view about fundamental value. By
doing so, such traders activity makes prices unpredictable and simply propagate the high-frequency value
of volatility to long time scales. The resulting volatility has no reason whatsoever to match the fundamen-
tal volatility. Hence, one plausible explanation for the excess-volatility puzzle is that the trading-induced
volatility is much larger than the fundamental volatility. It is only over very long time scales (several years)
that some mean reversion around the fundamental value can be observed, as surmised by Black [7] and
substantiated in [55–57]. Correspondingly, we conjecture that the very long term (> 5 years) value of
GK’s multiplier M is signiﬁcantly smaller than the one measured on monthly time scales. Unfortunately,
this long term limit will probably be very difﬁcult to measure.
5.3
Volatility Equals Spread
As argued above, no-arbitrage at high frequencies is secured by HFT/market-making activities. But since
these activities are highly competitive, one expects that the average proﬁtability of liquidity provision is
in fact close to zero. As argued in [53], this condition is enough to enforce that spread and volatility are
related. A simple framework to understand this relation is the MRR model [58], which is a bare-bone
version of the propagator model [14]. The upshot of the model is that the volatility per trade υ is given
by [19, 53]
υ2 =
1 −c2
1
4
s2 + υ2
0,
(5)
8


---

where s is the spread, c1 is the one-lag auto-correlation coefﬁcient of the sign of the trades and υ2
0 is the
news induced contribution to volatility, i.e. price changes that would occur without trades. The usual
(per unit time) volatility is then obtained as σ2
T = υ2NT, where NT is the average number of trades during
time T.
It turns out that Eq. (5) is remarkably obeyed by empirical data (see e.g. Fig. 16.6 in [19]), with
υ0 ≪υ, meaning that the lion’s share of the volatility is induced by trades, that is very little news induced
jumps (on this point, see [21, 23]). The very same conclusion is obtained within a more sophisticated
version of the propagator model, that accounts for the non-markovian nature of the order ﬂow (see e.g.
[19], Chapter 14).
The conclusion is that order ﬂow, whether informed or non informed, is the major source of volatility
in ﬁnancial markets. This is of course also the content of the inelastic market story of GK: trades move
the price, and the long term effect, measured by GK’s multiplier M, is very substantial — again, trading
1% of the market cap moves the price by 1%.
In fact, we can provide another enticing interpretation of Eq. (2), based on the relation (5) between
spread and volatility:
I∞∝
s NQ
p
Nm
,
(6)
where s is the spread, NQ the number of individual trades needed to complete the execution of the
metaorder, and Nm the total number of trades taking place within the memory time interval [0, Tm].
Naively, each trade impacts the price by an amount proportional to the spread, but most of this impact
decays as a power-law because of the autocorrelation of the sign of the trades, so on long timescales only
a fraction 1/
p
Nm of the initial impact survives in the long run.
5.4
Why Do Uninformed Trades Impact Prices To Start With?
We wish to end this section with a short discussion of the standard paradox raised by the very notion
of market impact. Since every buy trade is matched by a sell trades, why do trades impact prices at
all, except if these trades anticipate some information which is only revealed later? This is the efﬁcient
market conundrum (see again section 2.1) carefully resolved in GK’s paper, where the idea of mandate-
constrained asset managers crucially comes into play.
From a microstructural point of view, each trade can be characterized as “active” (consuming liquidity)
or “passive” (providing liquidity). This distinction breaks the symmetry at high frequencies, and allows
one to deﬁne a meaningful order imbalance, as the sum of active buy trades minus the sum of active
sell trades. It is this imbalance that reﬂects an aggregate “urge” to buy or sell and that mechanically
impacts prices, whether or not this urge is justiﬁed by a genuine piece of information about future value.
Ultimately, the GK multiplier M will turn out to be the low frequency stigma of the asymmetry between
active and passive trades.
5.5
GK’s Multiplier For Stock Indices
GK also argue that the multiplier M is 5 times larger for the market as a whole (i.e. when buying the
index) [27]. In their story, this comes from the fact that investors willing to sell stocks and substitute
them with bonds are more scarce than investors willing to substitute one stock with another. Within a
microstructure point of view, the ampliﬁcation factor comes from “cross-impact”, i.e. the fact of buying
one stock pushes the price of all correlated stocks by a small, but measurable amount [59]. Intriguingly,
it turns out that this small cross-impact, when multiplied by the number of stocks in the index, recovers
precisely the factor 5 suggested by GK (see [59], their Fig. 8 and the discussion thereafter). We again
ﬁnd this agreement quite remarkable, as it bolsters our claim that the mechanism underlying the inelastic
hypothesis has a natural microstructural origin. Note however that the LLT has not yet been generalized
to account for cross-impact, which is an important open problem.
5.6
GK’s Multiplier For Futures Markets
Whereas GK’s story chieﬂy concerns stock markets, our microstructural interpretation suggests a much
broader applicability, in particular to commodity futures or foreign exchange. The only subtlety is to
deﬁne the analogue of the market cap to obtain an a-dimensional “multiplier”. One possibility is to use
9


---

open interest, but it is not clear that such a choice is always meaningful. In any case, the LLT predicts that
the medium term impact of buying one contract of any tradable asset is given by Eq. (2), with Q = 1 and
V1 measured in number contracts traded daily.
6
Conclusion
The aim of this paper was to relate Gabaix and Koijen’s Inelastic Market Hypothesis [27] to the order-
driven view of markets that emerged within the microstructure literature in the past 20 years. We reviewed
the most salient empirical facts and arguments that give credence to the idea that market price ﬂuctuations
are mostly due to order ﬂow, whether informed or non-informed: trades impact prices, even on the long
run. We focused in particular on the Latent Liquidity Theory (LLT) of price impact, and argued that the
underlying mechanism for what GK call inelasticity is the dynamics of private estimates of asset value,
which tend to realign around the market price over some ﬁnite memory time that we called Tm. LLT in fact
makes a precise prediction for GK’s multiplier M, which measures the long term impact of transactions:
if a trading ﬁrm buys X$ of a company, the market capitalisation of that company increases by MX$. Our
central result is given by Eq. (3), which relates M to the daily volatility of the asset, the fraction of its
market capitalisation that is traded daily, and the memory time Tm. Although trades permanently impact
prices, there is no possibility of “mechanical” arbitrage within LLT.
The macro-ﬁnance implications of the inelastic market hypothesis are important and have been thor-
oughly discussed in GK’s paper [27], in particular the idea that governments could buoy the stock market
by investing in equities [60]. From our point of view, the order-driven view of markets allows one to
understand many of the puzzles of asset pricing theory, in particular the excess-volatility puzzle and the
existence of long-lived bubbles and market rallies, fueled by a continuous inﬂow of buy orders, with the
recent episode of Reddit meme stocks as a case in point [61]. Note that the LLT theory is not restricted to
stock, and predicts that similar effects also hold for any traded asset, see section 5.6 above.
If order ﬂow is the dominant cause of price changes, “information” is chieﬂy about correctly antici-
pating the behaviour of others, as Keynes envisioned long ago, and not about fundamental value. The
notion of information should then be replaced by the notion of correlation with future returns, induced
by future ﬂows. For example, when all market participants interpret a positive piece of news as negative
and sell accordingly, the correct move for an arbitrageur is to interpret the news as negative, even if doing
so does not make economic sense. Of course, if all market participants are rational and make trading
decisions based on their best guess of the fundamental value, order ﬂow will just reﬂect deviations from
fundamentals and the efﬁcient market picture is recovered.
The idea that it is the order-ﬂow that must be predicted, even if uninformed, resonates well with the
intuition of ﬁnance professionals and allows one to understand why statistical regularities might exist
and be exploited by quant ﬁrms. Indeed, ﬂow data is quite popular among statistical arbitrage funds. The
order-driven paradigm also allows one to resolve some paradoxes, like for example that it is surprisingly
easier to ﬁnd predictive signals for large cap. stocks than for small cap. stocks, probably because the
former are more actively traded and that the order ﬂow reveals more statistical regularities. The 2007
quant crunch and other recurrent deleveraging spirals are also extreme consequences of the impact of
order ﬂow on prices [62–64].
In conclusion, we hope that the present reformulation of the Inelastic Market Hypothesis in terms
of mechanistic and measurable microstructural effects will shed a complementary light on the origin of
ﬁnancial market ﬂuctuations, and possibly hammer a ﬁnal nail into the cofﬁn of the Efﬁcient Market
Hypothesis.
Acknowledgments
I want to warmly thank M. Benzaquen (with whom Eq. (2) was derived), X. Gabaix, R. Koijen, I. Mas-
tromatteo, D. Thesmar, B. Tóth and Ph. van der Beck for many discussions around these speciﬁc topics,
and Y. Lempérière for providing the data used in Fig. 1. Many of the ideas expressed in this paper were
originally formulated in our book [19] and I want to thank J. Bonart, J. Donier and M. Gould for a terriﬁc
collaboration.
10


---

Appendix: Permanent Impact within LLT
We here brieﬂy recall the main ingredients of the LLT as presented in [44], see also [19]. In the continuous
limit we deﬁne the latent volume densities of limit orders in the order book as: ϕb(x, t) (buy) and ϕs(x, t)
(sell). The latter evolve according to the following set of partial differential equations:
∂tϕb
=
σ2
1∂x xϕb −νϕb + λΘ(xt −x) −R(x)
(7a)
∂tϕs
=
σ2
1∂x xϕs −νϕs + λΘ(x −xt) −R(x) ,
(7b)
where the different contributions on the right hand side respectively represent (from left to right): small
random changes of agents’ reservation prices (diffusion terms), cancellations with rate ν (death terms),
arrivals of new intentions with intensity λ (deposition terms), and ﬁnally matching of buy/sell intentions R
(reaction terms). The cancellation of orders corresponds to memory erasure and realignment of intentions
around the current price, so the rate ν corresponds to the inverse of the memory time Tm considered in
the present paper:
ν = 1
Tm
.
In the limit where R →∞(corresponding to continuous double auction markets), buy and sell inten-
tions cannot coexist and the market price xt therefore obeys ϕb(xt, t) = ϕs(xt, t) = 0. A crucial remark
is that in that limit φ(x, t) = ϕb(x, t) −ϕs(x, t) solves a linear equation [43]:
∂tφ = σ2
1∂x xφ −νφ + s(x, t) ,
(8)
where the deposition term reads s(x, t) = λ sign(xt −x). The stationary order book was computed by
Donier et al. [44] as: φst(x) = −(λ/ν) sign(x)[1 −exp(−p|x|)] where p =
Æ
ν/σ2
1 denotes the typical
length scale below which the order book can be considered as linear: φst(x) = −L x where L = λ/
Æ
νσ2
1
is a measure of liquidity, related to the volume traded per unit time V1 through V1 = σ2
1L .
Donier et al. [44] focused on the inﬁnite memory linear order book limit, namely ν,λ →0 (while
keeping the liquidity L ∼λν−1/2 constant), for which the impact of a metaorder asymptotically decays to
zero, because agents never forget their initial beliefs. In [46], we have extended the calculation to small
but non-zero ν (i.e. long memory time), for which some residual long-term impact is expected.
The general solution of Eq. (8) is given by:
φ(x, t) = (Gν ∗φ0)(x, t) +
Z
dy
Z ∞
0
dτGν(x −y, t −τ)s(y,τ) ,
(9)
where φ0(x) = φ(x,0) denotes the initial condition, and
Gν(x, t) = max(t,0)
exp
h
−
x2
4σ2
1 t −νt
i
Æ
4πσ2
1t
.
(10)
Following Donier et al. [44], we introduce a buy (sell) meta-order as an extra point-like source of buy
(sell) particles with intensity rate m = Q/T, where Q is the volume of the metaorder and T the execution
time, such that the source term in Eq. (8) becomes: s(x, t) = mδ(x −xt) · 1[0,T] + λ sign(xt −x).
Performing the integral over space in Eq. (9) and setting φ0(x) = φst(x) yields:
φ(x, t) = φst(x)e−νt + m
Z t∧T
0
dτGν(x −xτ, t −τ) −λ
Z t
0
dτerf

x −xτ
p
4D(t −τ)

e−ν(t−τ) .
(11)
The price xt solves the integral equation:
φ(xt, t) = 0 .
(12)
For λ,ν →0 and for t > T, one immediately recovers Eq. (16) of [44]:
xt = x0
t = m
L
Z T
0
dτG0(xt −xτ, t −τ),
(13)
11


---

which boils down, at large t, to
x0
t ≈Q
L
1
Æ
4πσ2
1t
=
σ1
p
4πt
Q
V1
.
(14)
Setting t = Tm in this equation immediately leads to Eq. (2), up to a numerical prefactor.
In order to compute the long term impact exactly, the main idea of the calculation is to expand the
price trajectory xt in powers of pν, i.e.
xt = x0
t + pνx1
t + O(ν),
(15)
where x0
t and x1
t respectively denote the 0th order and 1st order contributions. In the limit of short
execution times (T ≪Tm) and small meta-order volumes Q ≪Vm, where Vm = V1Tm is the total volume
traded during the memory time Tm, one can look for a solution of the form x1
t = F(νt). In the long time
limit t ≫T, using the zero-th order solution Eq. 14 and setting u = νt, Eq. (11) boils down to
0 = F(u) + β
Z u
0
dv
pv −pu
p
πuv(u −v)
ev +
Z u
0
dv F(u) −F(v)
p
π(u −v)
ev ,
(16)
where β depends on the fast/slow nature of the execution (see [46] for more details). The solution of
this equation for u ≫1 can is found to be
F(u) = F∞−β
pu

1 −e−u
,
(17)
where F∞= 1
2σ1Q/V1 is completely independent of the trading speed. Since x0
t tends to zero at long
times, the long term impact is given by the asymptotic value of x t
1 = pνF∞, which is the result given
in Eq. (2). Simply stated, Eq. (2) means that the long-term impact is a fraction of the price volatility
over time scale Tm, where this fraction is given by the ratio of the volume of the metaorder Q to the total
volume traded on the same time scale V1Tm. We believe that this intuitive result should be valid much
beyond the speciﬁc set of hypotheses on which the above calculation is based.
As it is further discussed in [46], the assumption of a single memory time Tm is not realistic, since
investors with very different trading horizons co-exist in the market. If instead one assumes a distribution
of memory times ϱ(Tm), the long-time impact is rather given by [46]:
I∞(Q) = 1
2σ1
Q
V1
Z ∞
0
dx ϱ(x)
px ,
(18)
where memory times x are expressed in days, like the volatility σ1 and the average daily volume V1.
12


---

References
[1] Shiller, R. J. (1980). Do stock prices move too much to be justiﬁed by subsequent changes in divi-
dends? American Economic Review, 71, 421-436.
[2] Summers, L. H. (1986). Does the stock market rationally reﬂect fundamental values?. The Journal of
Finance, 41(3), 591-601.
[3] Barber, B. M., & Odean, T. (1999). Do investors trade too much?. American Economic Review, 89(5),
1279-1298.
[4] Jegadeesh, N., & Titman, S. (2011). Momentum. Annu. Rev. Financ. Econ., 3(1), 493-509.
[5] Moskowitz, T. J., Ooi, Y. H., & Pedersen, L. H. (2012). Time series momentum. Journal of Financial
Economics, 104(2), 228-250.
[6] Lempérière, Y., Deremble, C., Seager, P., Potters, M., & Bouchaud, J. P. (2014). Two centuries of trend
following. Journal of Investing Strategies 3, 41-61, (2014)
[7] Black, F. (1986). Noise. The Journal of Finance, 41(3), 528-543.
[8] Shleifer, A., & Summers, L. H. (1990). The noise trader approach to ﬁnance. The Journal of Economic
Perspectives, 4(2), 19-33.
[9] Kyle, A. S. (1985). Continuous auctions and insider trading. Econometrica: Journal of the Economet-
ric Society, 1315-1335.
[10] Glosten, L. R., & Milgrom, P. R. (1985). Bid, ask and transaction prices in a specialist market with
heterogeneously informed traders. Journal of Financial Economics, 14(1), 71-100.
[11] Madhavan, A. (2000). Market microstructure: A survey. Journal of Financial Markets, 3(3), 205-
258.
[12] Hasbrouck, J. (2007). Empirical market microstructure: The institutions, economics, and econo-
metrics of securities trading. Oxford University Press.
[13] Lyons, R. (2001). The microstructure approach to Foreign Exchange rates, MIT Press, Cambridge
MA.
[14] Bouchaud, J. P., Gefen, Y., Potters, M., & Wyart, M. (2004). Fluctuations and response in ﬁnancial
markets: the subtle nature of ‘random’ price changes. Quantitative ﬁnance, 4(2), 176-190.
[15] Farmer, J. D., Patelli, P., & Zovko, I. I. (2005). The predictive power of zero intelligence in ﬁnancial
markets. Proceedings of the national academy of sciences of the united states of America, 102(6),
2254-2259.
[16] Hopman, C. (2007). Do supply and demand drive stock prices? Quantitative Finance, 7, 37-53.
[17] Bouchaud, J. P., Farmer, J. D., & Lillo, F. (2009). How markets slowly digest changes in supply and
demand. Handbook of Financial Markets: Dynamics and Evolution, North-Holland, Elsevier.
[18] Deuskar, P., & Johnson, T. C. (2011). Market liquidity and ﬂow-driven risk. The Review of Financial
Studies, 24(3), 721-753.
[19] Bouchaud, J. P., Bonart, J., Donier, J., & Gould, M. (2018). Trades, quotes and prices: ﬁnancial
markets under the microscope. Cambridge University Press.
[20] Cutler, D. M., Poterba, J. M., & Summers, L. H. (1989). What moves stock prices?. The Journal of
Portfolio Management, 15(3), 4-12.
[21] Joulin, A., Lefevre, A., Grunberg, D., & Bouchaud, J. P. (2008). Stock price jumps: news and volume
play a minor role. Wilmott Magazine, Sept/Oct, 1-7.
13


---

[22] Fosset, A., Bouchaud, J. P., & Benzaquen, M. (2020). Endogenous liquidity crises. Journal of Statis-
tical Mechanics: Theory and Experiment, 2020(6), 063401.
[23] Marcaccioli, R., Bouchaud, J. P., & Benzaquen, M. (2021). Exogenous and Endogenous Price Jumps
Belong to Different Dynamical Classes. https://ssrn.com/abstract=3866131.
[24] Filimonov, V., & Sornette, D. (2012). Quantifying reﬂexivity in ﬁnancial markets: Toward a predic-
tion of ﬂash crashes. Physical Review E, 85(5), 056108.
[25] Hardiman, S., Bercot, N., & Bouchaud, J. P. (2013). Critical reﬂexivity in ﬁnancial markets: a Hawkes
process analysis. Eur. Phys. J. B 86: 442-447.
[26] Bacry, E., Mastromatteo, I., & Muzy, J. F. (2015). Hawkes processes in ﬁnance. Market Microstructure
and Liquidity, 1(01), 1550005.
[27] Gabaix, X., & Koijen, R. S. (2021). In search of the origins of ﬁnancial ﬂuctuations: The inelastic
markets hypothesis (No. w28967). National Bureau of Economic Research.
[28] Frazzini, A., Israel, R., & Moskowitz, T. J. (2018). Trading costs. Available at SSRN 3229719.
[29] Almgren, R., Thum, C., Hauptmann, E., & Li, H. (2005). Direct estimation of equity market impact.
Risk, 18(7), 58-62.
[30] Zarinelli, E., Treccani, M., Farmer, J. D., & Lillo, F. (2015). Beyond the square root: Evidence for
logarithmic dependence of market impact on size and participation rate. Market Microstructure and
Liquidity, 1(02), 1550004.
[31] Bucci, F., Mastromatteo, I., Eisler, Z., Lillo, F., Bouchaud, J. P., & Lehalle, C. A. (2020). Co-impact:
Crowding effects in institutional trading activity. Quantitative Finance, 20(2), 193-205.
[32] Tóth, B., Eisler, Z., & Bouchaud, J. P. (2016). The Square-Root Impace Law Also Holds for Option
Markets. Wilmott, 2016(85), 70-73.
[33] Moro, E., Vicente, J., Moyano, L. G., Gerig, A., Farmer, J. D., Vaglica, G., Lillo, F. & Mantegna, R.
N. (2009). Market impact and trading proﬁle of hidden orders in stock markets. Physical Review E,
80(6), 066102.
[34] Donier, J., & Bonart, J. (2015). A million metaorder analysis of market impact on the Bitcoin. Market
Microstructure and Liquidity, 1(02), 1550008.
[35] Tóth, B., Eisler, Z. & Bouchaud, J.-P. (2017). The Short-Term Price Impact of Trades is Universal.
https://ssrn.com/abstract=2924029.
[36] Torre, N., Ferrari, M. (1997). Market impact model Handbook, BARRA Inc., Berkeley (1997), avail-
able at http://www.barra.com/newsletter/nl166/miminl166.asp
[37] Grinold, R. C., & Kahn, R. N. (2000). Active Portfolio Management. McGraw-Hill.
[38] Zhang, Y. C. (1999). Toward a theory of marginally efﬁcient markets. Physica A: Statistical Mechanics
and its Applications, 269(1), 30-44.
[39] Gabaix, X., Gopikrishnan, P., Plerou, V., & Stanley, H. E. (2003). A theory of power-law distributions
in ﬁnancial market ﬂuctuations. Nature, 423(6937), 267-270.
[40] Farmer, J. D., Gerig, A., Lillo, F., & Waelbroeck, H. (2013). How efﬁciency shapes market impact.
Quantitative Finance, 13(11), 1743-1758.
[41] Tóth, B., Lemperiere, Y., Deremble, C., De Lataillade, J., Kockelkoren, J., & Bouchaud, J. P. (2011).
Anomalous price impact and the critical nature of liquidity in ﬁnancial markets. Physical Review X,
1(2), 021006.
[42] Mastromatteo, I., Tóth, B., & Bouchaud, J. P. (2014). Agent-based models for latent liquidity and
concave price impact. Physical Review E, 89(4), 042805.
14


---

[43] Mastromatteo, I., Tóth, B., & Bouchaud, J. P. (2014). Anomalous impact in reaction-diffusion ﬁnan-
cial models. Physical review letters, 113(26), 268701.
[44] Donier, J., Bonart, J., Mastromatteo, I., & Bouchaud, J. P. (2015). A fully consistent, minimal model
for non-linear market impact. Quantitative ﬁnance, 15(7), 1109-1121.
[45] Donier, J., & Bouchaud, J. P. (2016). From Walras’ auctioneer to continuous time double auctions:
A general dynamic theory of supply and demand. Journal of Statistical Mechanics: Theory and Exper-
iment, 2016(12), 123406.
[46] Benzaquen, M., & Bouchaud, J. P. (2018). Market impact with multi-timescale liquidity. Quantitative
Finance, 18(11), 1781-1790.
[47] Dall’Amico, L., Fosset, A., Bouchaud, J. P., & Benzaquen, M. (2019). How does latent liquidity get
revealed in the limit order book?. Journal of Statistical Mechanics: Theory and Experiment, 2019(1),
013404.
[48] Bucci, F., Mastromatteo, I., Benzaquen, M., & Bouchaud, J. P. (2019). Impact is not just volatility.
Quantitative Finance, 19(11), 1763-1766.
[49] Brokmann, X., Serie, E., Kockelkoren, J., & Bouchaud, J. P. (2015). Slow decay of impact in equity
markets. Market Microstructure and Liquidity, 1(02), 1550007.
[50] Bucci, F., Benzaquen, M., Lillo, F., & Bouchaud, J. P. (2018). Slow decay of impact in equity markets:
insights from the ANcerno database. Market Microstructure and Liquidity, 4(03n04), 1950006.
[51] van der Beck, P., Flow-Driven ESG Returns. Swiss Finance Institute Research Paper No. 21-71, Avail-
able at SSRN: https://ssrn.com/abstract=3929359
[52] Bouchaud, J. P., Kockelkoren, J., & Potters, M. (2006). Random walks, liquidity molasses and critical
response in ﬁnancial markets. Quantitative ﬁnance, 6(02), 115-123.
[53] Wyart, M., Bouchaud, J. P., Kockelkoren, J., Potters, M., & Vettorazzo, M. (2008). Relation between
bid–ask spread, impact and volatility in order-driven markets. Quantitative Finance, 8(1), 41-57.
[54] Farmer, J. D., Gerig, A., Lillo, F., & Mike, S. (2006). Market efﬁciency and the long-memory of supply
and demand: Is price impact variable and permanent or ﬁxed and temporary?. Quantitative ﬁnance,
6(02), 107-112.
[55] Bouchaud, J. P., Ciliberti, S., Lemperiere, Y., Majewski, A., Seager, P., & Sin Ronia, K. (2018).
Black was right:
Price is within a factor 2 of Value. Available at https://www.risk.net/cutting-
edge/investments/6004766/black-was-right-price-is-within-a-factor-2-of-value
[56] Majewski, A. A., Ciliberti, S., & Bouchaud, J. P. (2020). Co-existence of trend and value in ﬁnancial
markets: Estimating an extended Chiarella model. Journal of Economic Dynamics and Control, 112,
103791.
[57] Schmidhuber, C. (2021). Trends, reversion, and critical phenomena in ﬁnancial markets. Physica A:
Statistical Mechanics and its Applications, 566, 125642.
[58] Madhavan, A., Richardson, M., & Roomans, M. (1997). Why do security prices change?
A
transaction-level analysis of NYSE stocks. Review of Financial Studies, 10(4), 1035-1064.
[59] Benzaquen, M., Mastromatteo, I., Eisler, Z., & Bouchaud, J. P. (2017). Dissecting cross-impact
on stock markets: An empirical analysis. Journal of Statistical Mechanics: Theory and Experiment,
2017(2), 023406.
[60] Farmer, R., Expectations, Employment and Prices, Oxford University Press, 2010.
[61] van der Beck, P., & Jaunin, C. (2021). The equity market implications of the retail investment boom.
Available at SSRN 3776421.
15


---

[62] Khandani, A. E., & Lo, A. W. (2011). What happened to the quants in August 2007?: Evidence from
factors and transactions data. Journal of Financial Markets, 14(1), 1-46.
[63] Brunnermeier, M. K., & Pedersen, L. H. (2009). Market liquidity and funding liquidity. The review
of ﬁnancial studies, 22(6), 2201-2238.
[64] Kyle,
A.
S.,
&
Obizhaeva,
A.
A.
(2016).
Large
bets
and
stock
market
crashes.
https://ssrn.com/abstract=2023776
16
