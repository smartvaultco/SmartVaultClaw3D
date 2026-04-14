# Actionable Trading Strategies for 2025-2026
*Compiled: April 2026 | For: Trading Bot Knowledge Base | Status: LIVE REFERENCE*

---

## TABLE OF CONTENTS

1. Trump Tariff Volatility Plays
2. Options Strategies for High Volatility
3. AI/Bot Algorithmic Strategies (Mean Reversion, Momentum, VWAP)
4. Polymarket Prediction Market Strategies
5. Crypto Arbitrage & Funding Rate Capture
6. Kelly Criterion Position Sizing
7. Free/Cheap Backtesting Tools
8. Verified Trader Warnings & Red Flags

---

## 1. TRUMP TARIFF VOLATILITY PLAYS

### Context (2025-2026)
- "Liberation Day" (April 2, 2025) tariffs triggered VIX spike to 55 — highest since COVID March 2020
- Markets experienced worst 2-day sell-off since COVID followed by one of the greatest single-day rallies in a single week
- Supreme Court ruled 6-3 on Feb 20, 2026 that IEEPA does not authorize tariffs, leaving only Section 232 tariffs
- Potential $150B in tariff refunds could boost retail sectors

### Strategy 1A: VIX Call Spread Hedge
**Goal:** Profit from volatility spikes around tariff announcements

| Parameter | Rule |
|-----------|------|
| **Entry** | Buy VIX call spreads when VIX drops below 14. Buy the near-ATM call, sell a call 10-20 strikes higher |
| **Expiration** | 30-60 days out (sweet spot for cost vs. time) |
| **Exit** | Close when VIX hits 23-25; take profits FAST — VIX spikes are short-lived |
| **Reverse play** | When VIX > 25, buy VIX put spreads betting on mean reversion back down |
| **Position size** | 1-3% of portfolio per spread |
| **Expected R:R** | 3:1 to 10:1 on spikes; most spreads expire worthless (low win rate ~25-35%, but outsized winners) |
| **Capital needed** | $2,000-$10,000 minimum for meaningful positions |

### Strategy 1B: Tariff Sector Rotation
**Goal:** Rotate into sectors that benefit from tariff policy, away from those hurt

| Sector | Tariff Impact | Action |
|--------|--------------|--------|
| Utilities, Healthcare, Consumer Staples | Defensive / domestic = protected | OVERWEIGHT during tariff escalation |
| AI / Semiconductors | Policy tailwind + domestic production push | OVERWEIGHT |
| Energy / Energy Security | Domestic production incentives | OVERWEIGHT |
| Industrials, Consumer Discretionary | Complex supply chains = exposed | UNDERWEIGHT |
| Import-heavy retail | Direct tariff cost hit | UNDERWEIGHT (but watch for reversal on court rulings) |

| Parameter | Rule |
|-----------|------|
| **Entry** | Rotate on tariff announcement days or within 48 hours |
| **Exit** | Reverse when tariff policy reverses or court strikes down tariffs |
| **Position size** | 10-20% of portfolio per sector tilt |
| **Win rate** | ~60% historically when following policy direction |
| **Capital needed** | $5,000+ for ETF-based rotation |

---

## 2. OPTIONS STRATEGIES FOR HIGH VOLATILITY

### Strategy 2A: Long Straddle (Pre-Event)
**Goal:** Profit from big moves in either direction around known catalysts

| Parameter | Rule |
|-----------|------|
| **Setup** | Buy ATM call + ATM put, same strike, same expiration |
| **When** | Enter BEFORE implied volatility (IV) spikes — before earnings, FOMC, tariff announcements |
| **Ideal IV Rank** | Enter when IVR < 30 (cheap premiums) |
| **Expiration** | 7-14 days for event-specific plays (minimizes theta decay) |
| **Exit** | Close immediately after the event move; do NOT hold through theta decay |
| **Stop** | Close if position loses 50% of premium paid |
| **Win rate** | ~40-45% (but winners are 2-5x) |
| **R:R** | 2:1 to 5:1 |
| **Capital needed** | $1,000-$5,000 per straddle depending on underlying |

### Strategy 2B: Short Iron Condor (Selling Premium in High IV)
**Goal:** Collect elevated premiums when IV is high, betting price stays in a range

| Parameter | Rule |
|-----------|------|
| **Setup** | Sell OTM put + buy further OTM put (bull put spread) AND sell OTM call + buy further OTM call (bear call spread) |
| **When** | IV Rank > 50 (premiums are inflated) |
| **Strike selection** | Short strikes at 1 standard deviation (68% probability OTM); wing width = $5-$10 |
| **Expiration** | 30-45 DTE (optimal theta decay) |
| **Exit** | Close at 50% of max profit OR if tested (price within $1 of short strike) |
| **Max loss** | Wing width minus credit received |
| **Win rate** | ~65-75% when entered at IVR > 50 |
| **R:R** | 1:2 to 1:3 (small wins, larger potential losses — managed by 50% profit target) |
| **Capital needed** | $2,000-$10,000 (buying power reduction per condor) |

### Strategy 2C: VIX Reverse Collar (Tactical Hedge)
**Goal:** Hedge equity portfolio against tail risk events

| Parameter | Rule |
|-----------|------|
| **Setup** | Buy slightly OTM VIX calls + sell slightly OTM VIX puts, same expiration |
| **Target expiration** | 90-120 days out |
| **Entry** | When VIX < 15 and major policy events upcoming |
| **Exit** | Close VIX calls when VIX > 30; let puts expire |
| **Cost** | Near zero (put premium offsets call cost) |
| **Portfolio allocation** | 2-5% of portfolio value in notional hedge |
| **Capital needed** | $3,000-$15,000 depending on portfolio size |

---

## 3. AI/BOT ALGORITHMIC STRATEGIES

### Strategy 3A: Mean Reversion (Bollinger Band + RSI)
**Goal:** Fade overextended moves, profit from snapback to the mean

| Parameter | Rule |
|-----------|------|
| **Indicators** | 20-period SMA Bollinger Bands (2 std dev) + RSI(14) + ATR(14) for stops |
| **Long entry** | Price closes below lower BB AND RSI < 30 (aggressive: < 35). Enter at open of next candle |
| **Short entry** | Price closes above upper BB AND RSI > 70 (aggressive: > 65). Enter at open of next candle |
| **Conservative filter** | RSI < 25 for longs, RSI > 75 for shorts (fewer signals, higher win rate) |
| **Exit** | Price returns to middle BB (20 SMA). Optional: scale out 50% at middle BB, 50% at opposite BB |
| **Stop loss** | 1.5-2x ATR beyond the entry candle extreme |
| **Position size** | Risk 1-2% of account per trade |
| **Win rate** | 55-65% (conservative filter), 45-55% (aggressive) |
| **R:R** | 1:1 to 1.5:1 |
| **Best timeframes** | 15min, 1hr, 4hr |
| **Best markets** | Range-bound stocks, forex pairs, ETFs. AVOID trending markets |
| **Capital needed** | $5,000+ for stocks, $1,000+ for forex/crypto |
| **DANGER** | Catastrophic when fading a real breakout. ALWAYS use stops. Never increase size on a losing reversion trade |

### Strategy 3B: Momentum / Trend Following
**Goal:** Ride strong directional moves — "buy high, sell higher"

| Parameter | Rule |
|-----------|------|
| **Indicators** | 9 EMA / 21 EMA crossover + ADX(14) > 25 + Volume > 1.5x 20-bar average |
| **Long entry** | 9 EMA crosses above 21 EMA AND ADX > 25 AND volume confirms |
| **Short entry** | 9 EMA crosses below 21 EMA AND ADX > 25 AND volume confirms |
| **Exit** | 9 EMA crosses back through 21 EMA OR ADX drops below 20 |
| **Stop loss** | Below the most recent swing low (longs) or above swing high (shorts) |
| **Trailing stop** | Move stop to breakeven after 1R profit; trail at 2x ATR |
| **Position size** | Risk 1-2% of account per trade |
| **Win rate** | 35-45% (low win rate, high payoff) |
| **R:R** | 2:1 to 5:1+ (let winners run) |
| **Best timeframes** | 1hr, 4hr, Daily |
| **Best markets** | Trending stocks, crypto, futures. Strong in volatile macro regimes |
| **Capital needed** | $5,000+ for stocks, $500+ for crypto |
| **Edge** | Retail bots can actually compete here — institutions can't move size fast enough on intraday trends |

### Strategy 3C: VWAP Breakout
**Goal:** Capture strong intraday directional moves using institutional price level

| Parameter | Rule |
|-----------|------|
| **Indicators** | Session VWAP + Volume (20-bar avg comparison) |
| **Long entry** | Price breaks decisively above VWAP with full-bodied bullish candle + volume >= 120% of 20-bar average. Safer: buy on 1-min micro-pullback after breakout |
| **Short entry** | Price breaks below VWAP with large bearish candle + volume surge >= 120% of 20-bar average |
| **VWAP slope filter** | Only trade in direction of VWAP slope (rising = longs only, falling = shorts only) |
| **Stop loss** | Just below VWAP for longs, just above VWAP for shorts |
| **Take profit** | Target 1: 1:2 R:R. Target 2: 1:3 R:R. Or trail with VWAP as dynamic stop |
| **Position size** | Risk 1% of account per trade |
| **Win rate** | 50-55% with volume confirmation |
| **R:R** | 2:1 to 3:1 |
| **Best timeframes** | 1min, 5min, 15min (intraday only — VWAP resets daily) |
| **Best markets** | Liquid stocks (SPY, QQQ, AAPL, TSLA), ES/NQ futures |
| **Capital needed** | $2,000+ for stocks, $5,000+ for futures |
| **Stocks under $20** | Use 10% profit target as exit |

### Strategy 3D: Opening Range Breakout (ORB) + VWAP Filter
**Goal:** Trade the first decisive move of the session

| Parameter | Rule |
|-----------|------|
| **Setup** | Define opening range = first 5, 15, or 30 minutes of session (high and low) |
| **Long entry** | Price breaks above opening range high AND price is above VWAP AND volume surges |
| **Short entry** | Price breaks below opening range low AND price is below VWAP AND volume surges |
| **Stop loss** | Opposite side of the opening range |
| **Take profit** | 1.5x the opening range width, or trail with VWAP |
| **Position size** | Risk 1% of account |
| **Win rate** | 50-60% with VWAP confirmation |
| **R:R** | 1.5:1 to 3:1 |
| **Best markets** | ES, NQ futures, high-volume stocks |
| **Capital needed** | $5,000+ for futures |

---

## 4. POLYMARKET PREDICTION MARKET STRATEGIES

### Context
- $40M+ in arbitrage profits extracted from Polymarket between April 2024 and April 2025 (academic research, IMDEA Networks Institute)
- Bot traders with 85%+ win rates generating $206K+ profits
- Human traders using similar strategies capture roughly half of bot profits

### Strategy 4A: Dutch-Book Arbitrage (Within-Market)
**Goal:** Lock in risk-free profit when Yes + No prices sum to less than $1.00

| Parameter | Rule |
|-----------|------|
| **Entry** | Buy both YES and NO positions when combined cost < $0.97 (need 3% margin for fees) |
| **Exit** | Hold until market resolves — guaranteed profit regardless of outcome |
| **Expected return** | 0.5-3% per trade |
| **Win rate** | ~100% (true arbitrage) |
| **Speed required** | Opportunities close in seconds — requires bot automation |
| **Capital needed** | $5,000+ to make meaningful returns at 1-3% per trade |
| **Tools** | Polymarket API, custom bot, low-latency execution |

### Strategy 4B: Cross-Platform Arbitrage (Polymarket vs. Kalshi)
**Goal:** Exploit price differences between prediction markets

| Parameter | Rule |
|-----------|------|
| **Entry** | When Polymarket prices an event at X% and Kalshi prices it at Y%, and the spread > 3% (to cover fees on both platforms) |
| **Example** | Polymarket: YES = 60 cents, Kalshi: NO = 45 cents (YES implied = 55 cents). Buy YES on Kalshi, buy NO on Polymarket. Total cost = $1.05? No — buy YES on the cheaper platform, NO on the more expensive one. Spread must net positive after fees |
| **Exit** | Hold until resolution |
| **Win rate** | ~100% if executed correctly |
| **Fees to account for** | Kalshi charges on expected earnings + maker fees; Polymarket has gas fees |
| **Minimum spread** | 2.5-3% after all fees |
| **Capital needed** | $5,000+ split across both platforms |

### Strategy 4C: Information Edge Trading
**Goal:** Trade on real-time data faster than market updates

| Parameter | Rule |
|-----------|------|
| **Edge** | Monitor live data feeds (election results, sports scores, economic releases) and trade before order book updates |
| **Entry** | Place order immediately when off-chain data confirms outcome direction |
| **Exit** | Hold until resolution or sell when price adjusts to new information |
| **Risk** | Execution speed; other bots competing for same edge |
| **Win rate** | 60-80% depending on data feed speed |
| **Capital needed** | $2,000+ |
| **Requirements** | API access, real-time data feeds, automated execution |

### Strategy 4D: Market Making (Low Liquidity Markets)
**Goal:** Capture bid-ask spread in newly launched or thin markets

| Parameter | Rule |
|-----------|------|
| **Entry** | Place limit orders on both sides of the book in low-liquidity Polymarket markets |
| **Spread target** | Maintain 3-5% spread between bid and ask |
| **Exit** | Rebalance when inventory becomes one-sided |
| **Risk** | Getting filled one-sided just before resolution |
| **Win rate** | ~70% of fills are profitable spreads |
| **Capital needed** | $5,000-$20,000 for sufficient order book depth |

---

## 5. CRYPTO ARBITRAGE & FUNDING RATE CAPTURE

### Strategy 5A: Funding Rate Arbitrage (Delta-Neutral)
**Goal:** Collect funding payments while remaining market-neutral

| Parameter | Rule |
|-----------|------|
| **Setup** | Buy spot crypto (e.g., BTC on Binance) + short same amount in perpetual futures on same or different exchange |
| **When** | Funding rate is positive (longs pay shorts). Rate was positive 92% of Q3 2025 |
| **Funding settlement** | Every 8 hours on Binance/Bybit/OKX (00:00, 08:00, 16:00 UTC). Some pairs: 4-hour or 1-hour |
| **Entry** | When annualized funding rate > 15% (worth the operational overhead) |
| **Exit** | Close both positions when funding turns negative or drops below 5% annualized |
| **Stop** | If funding reverses direction for 3+ consecutive periods, close out |
| **Position size** | 20-30% of capital (need margin for futures + spot) |
| **Expected return** | 15-20% APR average (2025 data: 19.26% avg); up to 115.9% in 6 months during extreme bull markets |
| **Max drawdown** | Under 2% historically (delta-neutral) |
| **Win rate** | ~90%+ (structural positive bias in funding) |
| **Capital needed** | $5,000+ minimum for meaningful returns after fees |
| **Exchanges** | Binance, Bybit, OKX (lowest fees, most liquid perpetuals) |
| **Tools** | CoinGlass (coinglass.com/FundingRate), Loris Tools (loris.tools), ArbitrageScanner (arbitragescanner.io) |

### Strategy 5B: CEX-to-CEX Price Arbitrage
**Goal:** Exploit price differences for same asset across exchanges

| Parameter | Rule |
|-----------|------|
| **Entry** | When price spread > transfer fees + trading fees + slippage (typically need > 0.3% spread) |
| **Execution** | Pre-fund both exchanges. Buy on cheap exchange, sell on expensive exchange simultaneously |
| **Exit** | Immediate — both legs execute at once |
| **Risk** | Price moving during transfer if not pre-funded; exchange withdrawal delays |
| **Win rate** | ~85-90% when pre-funded |
| **Expected return** | 0.1-0.5% per trade, multiple times daily |
| **Best pairs** | Altcoins on regional exchanges (Southeast Asia, Africa, South America have wider spreads) |
| **Capital needed** | $10,000+ split across 2-4 exchanges |

### Strategy 5C: DEX-CEX Arbitrage
**Goal:** Exploit pricing differences between decentralized and centralized exchanges

| Parameter | Rule |
|-----------|------|
| **Entry** | When DEX price deviates > 0.5% from CEX price (must exceed gas + swap fees) |
| **Networks** | Optimism, Arbitrum, Base (low gas fees) vs. Binance/OKX |
| **Execution** | Buy on cheaper venue, sell on more expensive venue |
| **Risk** | Smart contract risk, bridge delays, gas spikes |
| **Capital needed** | $3,000+ |

---

## 6. KELLY CRITERION POSITION SIZING

### The Formula
```
Kelly % = W - [(1 - W) / R]

Where:
W = Win rate (probability of winning)
R = Win/Loss ratio (average win / average loss)
```

### Example Calculations

| Strategy | Win Rate (W) | Win/Loss Ratio (R) | Full Kelly % | Half Kelly % | Recommendation |
|----------|-------------|-------------------|-------------|-------------|----------------|
| Mean Reversion | 60% | 1.2:1 | 26.7% | 13.3% | Use Half Kelly (13%) |
| Momentum | 40% | 3:1 | 20.0% | 10.0% | Use Half Kelly (10%) |
| VWAP Breakout | 52% | 2:1 | 28.0% | 14.0% | Use Quarter Kelly (7%) for volatile markets |
| Iron Condor | 70% | 0.5:1 | 10.0% | 5.0% | Use Full Kelly (10%) — already conservative |
| Funding Rate Arb | 90% | 2:1 | 85.0% | 42.5% | Use Quarter Kelly (21%) — high conviction but limit exposure |

### Practical Rules for Volatile Markets

1. **NEVER use Full Kelly** in live trading. Half Kelly achieves ~75% of Full Kelly's growth rate while cutting variance in half
2. **Quarter Kelly** (divide Full Kelly by 4) is recommended for high-volatility regimes (VIX > 25)
3. **Volatility-adjusted Kelly**: Reduce Kelly fraction by ATR ratio. If current ATR is 2x the 50-day average ATR, use Half Kelly instead of Full Kelly
4. **Hard cap**: Never risk more than 5% of account on a single trade regardless of Kelly output
5. **Regime switching**: Use Full Kelly in calm markets (VIX < 15), Half Kelly in normal (VIX 15-25), Quarter Kelly in crisis (VIX > 25)

### ATR-Based Position Sizing (Alternative)
```
Position Size = (Account Risk Per Trade) / (ATR-based Stop Distance x Point Value)

Example:
- Account: $50,000
- Risk per trade: 1% = $500
- ATR(14) = $2.50
- Stop = 2x ATR = $5.00
- Position Size = $500 / $5.00 = 100 shares
```

---

## 7. FREE/CHEAP BACKTESTING TOOLS

### Tier 1: Free, Production-Ready

| Tool | Language | Best For | Data | Live Trading | Notes |
|------|----------|----------|------|-------------|-------|
| **QuantConnect (LEAN)** | Python, C# | Multi-asset algo trading | 400TB+ built-in (free) | Yes (20+ brokers) | Cloud-based IDE, free backtesting, $60/mo for live. Best for serious algo development |
| **Backtrader** | Python | Quick local prototyping | BYO data | Limited | Free, Pythonic, local-only. Less maintained but excellent for learning |
| **TradingView (Pine Script)** | Pine Script | Visual strategy testing | Built-in | Via webhooks | Free tier: 3 indicators/chart. Paid from $15/mo. Best for visual traders |
| **MetaTrader 5** | MQL5 | Forex/CFD strategies | Built-in | Yes | Free, powerful Strategy Tester. Best for forex algo trading |

### Tier 2: Free with Limitations

| Tool | Best For | Notes |
|------|----------|-------|
| **BacktestingMax** | Free web-based backtesting | Professional tools, 1-min data |
| **Traders Casa** | Beginners | Free forever, 500K+ users |
| **ProRealTime** | Visual backtesting | Free web version, ProBacktest engine |
| **TrendSpider** | No-code strategies | Pattern recognition, code-free backtesting |

### Recommended Stack for Trading Bot Development
1. **Prototype**: Backtrader (local Python, fast iteration)
2. **Validate**: QuantConnect (professional-grade data, realistic fills)
3. **Visualize**: TradingView (chart overlays, Pine Script alerts)
4. **Deploy**: QuantConnect LEAN or custom Python bot via Alpaca/CCXT

---

## 8. VERIFIED TRADER WARNINGS & RED FLAGS

### What "Verified" Actually Means
- **CFTC warning**: Fraudsters use "AI trading bot" language to run Ponzi schemes. Fixed guaranteed returns with no strategy explanation = SCAM
- **95% of "AI" bots** are marketing gimmicks wrapping moving average crossover logic in a $29 indicator
- **Any bot that won't show backtesting, paper trading, AND live trading validation is hiding something**
- Reddit/Twitter P&L screenshots are trivially fakeable. One Redditor claimed 100% win rate over 18 trades using ChatGPT — completely unverifiable

### Verification Checklist Before Trusting Any Strategy
1. Does it show backtested results over 3-5+ years including bear markets?
2. Does it show paper trading results (forward test)?
3. Does it show live trading results with actual account statements (not screenshots)?
4. Does it explain exact entry/exit rules (not vague "buy the dip" advice)?
5. Does it acknowledge drawdowns and losing streaks?
6. Does it have a logical edge explanation (WHY does this work)?

### Red Flags
- "100% win rate" or "never loses"
- "Guaranteed returns" or "risk-free"
- Requires large upfront payment before revealing strategy
- Uses vague language: "proprietary AI" with no explanation
- Only shows winning trades
- No drawdown data
- Pressure to deposit money quickly

### Where to Find Legitimate Strategy Discussion
- **r/algotrading** — Skeptical community, demands backtests
- **r/options** — Experienced traders, realistic expectations
- **QuantConnect community forums** — Algorithm sharing with code
- **Alpaca community** — Python-based algo trading discussion
- **Collective2** — Audited track records (paid)

---

## SOURCES

- [J.P. Morgan: US Tariffs Impact](https://www.jpmorgan.com/insights/global-research/current-events/us-tariffs)
- [Tax Foundation: Trump Tariffs Tracker](https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/)
- [Morgan Stanley: Trump Tariffs 2025 Guide](https://www.morganstanley.com/articles/trump-tariffs-2025-investing-guide)
- [CNBC: Liberation Day One Year On](https://www.cnbc.com/2026/04/02/liberation-day-1-year-on-investors-are-rethinking-us-assets.html)
- [ChartsWatcher: Volatility Trading Strategies](https://chartswatcher.com/pages/blog/7-advanced-volatility-trading-strategies-for-2025)
- [DayTrading.com: Options Strategies High Volatility](https://www.daytrading.com/options-strategies-high-volatility)
- [OptionAlpha: Iron Condor Strategy](https://optionalpha.com/strategies/iron-condor)
- [OptionAlpha: VIX Portfolio Hedging](https://optionalpha.com/blog/vix-portfolio-hedging-strategy)
- [QuantVPS: Top 20 Trading Bot Strategies 2026](https://www.quantvps.com/blog/trading-bot-strategies)
- [Power Trading Group: Trading Bots 2026](https://www.powertrading.group/options-trading-blog/trading-bots-2026-what-works)
- [ChartsWatcher: VWAP Strategies](https://chartswatcher.com/pages/blog/6-powerful-vwap-trading-strategies-for-2025)
- [LuxAlgo: Mean Reversion Strategies](https://www.luxalgo.com/blog/mean-reversion-strategies-for-algorithmic-trading/)
- [Yahoo Finance: Arbitrage Bots on Polymarket](https://finance.yahoo.com/news/arbitrage-bots-dominate-polymarket-millions-100000888.html)
- [PANews: Polymarket Arbitrage Strategies](https://www.panewslab.com/en/articles/c9232541-9c0b-483d-8beb-f90cd7903f48)
- [arXiv: Prediction Market Arbitrage Research](https://arxiv.org/abs/2508.03474)
- [Zipmex: Funding Rate Analysis Guide](https://zipmex.com/blog/how-to-analyze-funding-rates-in-crypto/)
- [BingX: Funding Rate Arbitrage Guide](https://bingx.com/en/learn/article/what-is-funding-rate-arbitrage-guide-for-futures-traders)
- [Bitget: Funding Rate Arbitrage Decoded](https://www.bitget.com/news/detail/12560604395607)
- [CoinGlass: Live Funding Rates](https://www.coinglass.com/FundingRate)
- [ScienceDirect: Funding Rate Arbitrage Risk/Return](https://www.sciencedirect.com/science/article/pii/S2096720925000818)
- [TradersPost: Kelly Criterion Position Sizing](https://blog.traderspost.io/article/kelly-criterion-position-sizing-automated-trading)
- [Medium: Kelly Criterion for Crypto](https://medium.com/@tmapendembe_28659/kelly-criterion-for-crypto-traders-a-modern-approach-to-volatile-markets-a0cda654caa9)
- [QuantConnect: Open Source Platform](https://www.quantconnect.com/)
- [NewTrading: Backtesting Software 2026](https://www.newtrading.io/backtesting-software/)
- [Schwab: Trading the VIX](https://www.schwab.com/learn/story/trading-vix-strategies-fear-index)
