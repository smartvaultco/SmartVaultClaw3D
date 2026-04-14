# Options Wheel Strategy — Trading KB
## Source: Compiled from top wheel strategy educators & practitioners (2024-2026)
## Purpose: Feed this directly into the Options Bot (BOT 2) strategy

> **NOTE:** A YouTube channel specifically named "John Brown" teaching the options wheel
> strategy could not be verified to exist. This KB was compiled from the most authoritative
> wheel strategy sources available: DaysToExpiry.com, WheelStrategyOptions.com,
> OptionAlpha, SteadyOptions, Options Cafe, and other top practitioners.
> If you locate the exact channel, update this file with channel-specific rules.

---

## Core Philosophy

- **Sell premium, don't buy it.** You are the house, not the gambler. Time decay (theta) works in your favor on every single trade.
- **The wheel is a cashflow engine, not a get-rich-quick play.** Target 15-30% annualized returns consistently, not home runs.
- **Assignment is part of the process, not failure.** Getting assigned on a put just means you bought a stock you wanted at a discount. Getting called away on a covered call means you sold at a profit.
- **Only wheel stocks you genuinely want to own.** If you wouldn't hold it for 6+ months, don't sell puts on it.
- **Boring is profitable.** Blue chips and steady ETFs beat meme stocks every time in the wheel.
- **Income first, capital appreciation second.** The premium IS the return. Any stock price gains are bonus.

---

## Core Strategy: The Options Wheel (Triple Income Strategy)

### The Cycle
```
Phase 1: SELL CASH-SECURED PUT (collect premium)
    |
    +--> Put expires OTM → Keep premium → Sell another CSP (repeat Phase 1)
    |
    +--> Put assigned (you buy 100 shares) → Move to Phase 2
    
Phase 2: SELL COVERED CALL on assigned shares (collect premium)
    |
    +--> Call expires OTM → Keep premium + shares → Sell another CC (repeat Phase 2)
    |
    +--> Call assigned (shares called away at strike) → Collect profit → Back to Phase 1

BONUS: If holding shares through Phase 2, collect any dividends (3rd income stream)
```

### Three Income Streams
1. **Put premium** collected when selling CSPs
2. **Call premium** collected when selling CCs
3. **Dividends** collected while holding assigned shares (if applicable)

---

## Entry Rules

### Phase 1: Cash-Secured Puts

| Parameter | Rule | Notes |
|-----------|------|-------|
| **Delta** | -0.20 to -0.30 | ~70-80% probability of expiring OTM |
| **DTE** | 30-45 days (default: 45 DTE) | Peak theta decay zone |
| **IV Rank** | > 30% (prefer > 50%) | Higher IV = richer premiums |
| **Premium target** | 1-3% of capital deployed per month | Below 1% = not worth the risk |
| **Earnings** | NO new puts within 14 days of earnings | Earnings gaps destroy the wheel |
| **Trend** | Neutral to bullish bias on underlying | Never wheel a stock in free-fall |

**Exact entry process:**
1. Screen for stocks meeting selection criteria (see below)
2. Check IV Rank > 30%
3. Confirm no earnings within 14 days
4. Sell put at 0.25-0.30 delta, 30-45 DTE
5. Ensure you have full cash to cover assignment (strike x 100)

### Phase 2: Covered Calls (After Assignment)

| Parameter | Rule | Notes |
|-----------|------|-------|
| **Delta** | +0.20 to +0.30 (bullish: up to +0.35) | ~70-80% probability of expiring OTM |
| **DTE** | 21-30 days | Faster cycles after assignment |
| **Strike** | At or above your cost basis | NEVER sell below cost basis |
| **Earnings** | Close or roll before earnings | Same rule as puts |
| **Ex-dividend** | Hold through ex-div date if possible | Capture dividend income |

**Exact entry process:**
1. Get assigned shares from CSP
2. Calculate adjusted cost basis = strike price - premium received
3. Sell call at 0.25-0.30 delta, 21-30 DTE
4. Strike MUST be at or above adjusted cost basis
5. If stock dropped significantly, wait for a bounce or sell calls with minimal premium rather than locking in a loss

---

## Exit / Adjustment Rules

### Early Close Rules
| Condition | Action |
|-----------|--------|
| Position hits **50% of max profit** | Close for profit, redeploy capital |
| Position hits **75% of max profit** with < 14 DTE | Close — diminishing returns vs. gamma risk |
| **21 DTE reached** regardless of P/L | Close or roll — never hold into expiration week |
| **Delta exceeds 0.50** (>50% ITM probability) | Decide: close, roll, or accept assignment |
| **IV drops sharply** after entry | Close for profit — premium has already decayed |

### Rolling Rules — Cash-Secured Puts
| Condition | Action |
|-----------|--------|
| Stock drops < 5% below strike, fundamentals intact | **Roll down and out** for a net credit |
| Stock drops > 10% below strike | **Take assignment** or exit entirely |
| Already rolled once | Roll ONE more time max, then take assignment |
| Can't roll for a net credit | Do NOT roll — take assignment or close at loss |
| Fundamentals deteriorated | **Close position immediately** — do not roll |

### Rolling Rules — Covered Calls
| Condition | Action |
|-----------|--------|
| Stock rallies > 5% above strike | **Roll up and out** for a credit if possible |
| Effective sale price > 5% above cost basis | **Let shares get called away** — take the win |
| Stock stagnant near strike at expiration | Roll out to next month at same strike |
| Already rolled twice | Let it go — accept assignment and restart cycle |

### Hard Rules
- **Never roll more than twice** on the same position
- **Every roll must be for a net credit** — rolling for a debit is paying to lose slower
- **"If rolling only delays discomfort, it probably isn't helping"**

---

## Position Sizing & Capital Management

| Rule | Specification |
|------|---------------|
| **Max single position** | 10-20% of total account |
| **Hard max** | No single stock > 30% of wheeling capital |
| **Cash reserve** | Always keep 20% of account in cash (for opportunities/margin of safety) |
| **Simultaneous positions** | 3-8 wheels running at once |
| **Staggered entry** | Open new positions every 2-4 weeks (not all at once) |
| **Minimum account size** | $10,000-$25,000 to start (1-2 positions) |
| **Ideal account size** | $50,000+ (diversified across 4-6 positions) |
| **Buying power limit** | Never use more than 80% of buying power |

### Per-Position Sizing
- Strike price x 100 = capital required per CSP
- Example: $50 stock = $5,000 per wheel position
- In a $50K account: run 4-6 positions at $5,000-$8,000 each, keep $10K cash

---

## Stock / ETF Selection Criteria

### Screening Filters (Must Pass ALL)

| Filter | Requirement |
|--------|-------------|
| **Market cap** | > $5 billion (large cap preferred) |
| **Average daily volume** | > 1 million shares |
| **Options open interest** | > 1,000 contracts on target strikes |
| **Bid-ask spread** | < 5% of option price (tight = liquid) |
| **IV Percentile** | > 30% (prefer 30-60% range) |
| **Price range** | $20-$200 per share (sweet spot: $30-$80) |
| **Fundamentals** | Profitable, manageable debt, not distressed |
| **Sector** | Diversify — don't wheel 5 tech stocks |
| **You'd own it** | Would you hold 100 shares for 6 months? If no, skip it. |

### Avoid List
- Meme stocks (GME, AMC, etc.) — huge premiums, huge risk
- Biotech with binary catalysts — gap risk destroys the wheel
- Stocks with earnings within 14 days
- Any stock down > 20% in past month without clear support
- Penny stocks / anything under $10
- Stocks with IV > 100% (unless you deeply understand the name)

### Recommended Tickers by Sector

**Technology:** AAPL, MSFT, GOOGL, ADBE (2-3% monthly premium at 0.30 delta)

**Financials:** JPM, BAC, GS, WFC (2-3% monthly on puts)

**Industrials:** CAT, HON, UNP (1.5-2.5% monthly)

**Energy:** XOM, CVX, XLE ETF (2.5-4% monthly — higher IV)

**Healthcare:** JNJ, PFE, UNH, ABBV (1.5-2% monthly)

**Consumer:** KO, PG, WMT, COST (lower premium but rock-solid)

**ETFs:** SPY, QQQ, IWM, XLF, XLE (excellent for beginners — no single-stock risk)

**Small Account Starters ($3K-$10K):** F, T, BAC, PFE, INTC (low share prices, liquid options)

---

## Market Condition Rules

| Market Environment | Wheel Adjustment |
|-------------------|-----------------|
| **Bull market (steady uptrend)** | Sell puts at 0.25-0.30 delta. Sell calls at 0.30-0.35 delta (capture more upside). Best environment for wheeling. |
| **Neutral / sideways** | Sell puts at 0.20-0.25 delta. Sell calls at 0.25-0.30 delta. Ideal — pure premium income. |
| **High volatility / pullback** | Widen to 0.15-0.20 delta on puts. Use longer DTE (45-60). Premiums are fat — be patient. |
| **Bear market / crash** | STOP selling new CSPs. Manage existing positions. Sell CCs on assigned shares to lower cost basis. Wait for stabilization. |
| **Low IV environment** | Skip new entries — premiums aren't worth the risk. Wait for IV to expand. Minimum IV Rank > 30%. |
| **Earnings season** | Close or roll positions BEFORE earnings. Never open new wheels through earnings. |
| **High IV Rank (> 60%)** | Aggressively sell premium — this is the best time for new CSP entries. |

---

## Risk Management Rules

1. **Never wheel money you can't afford to lose.** The wheel can lose 20-30% of position value in a crash.
2. **Diversify across 3-5 sectors minimum.** One sector blowup shouldn't crater your whole account.
3. **Keep 20% cash reserve at all times.** Opportunity fund + margin of safety.
4. **Define exit rules BEFORE entering.** Write them down. Follow them.
5. **Track every trade in a journal/spreadsheet.** Log: entry date, ticker, strike, premium, delta, DTE, outcome, lessons.
6. **Never chase premium.** If a stock offers 8% monthly premium, ask WHY. The answer is usually "because it might go to zero."
7. **Cost basis is your anchor.** Always know your adjusted cost basis on assigned shares. Never sell calls below it.
8. **Accept small losses to prevent large ones.** Closing a losing put at 21 DTE for a $200 loss beats getting assigned and watching the stock drop another 30%.
9. **Wash sale rule awareness.** If you close a position at a loss and reopen within 30 days on the same underlying, the loss is disallowed for tax purposes.
10. **All premium income is short-term capital gains.** Plan for taxes — set aside 25-35% of premium income.

---

## Key Lessons & Common Mistakes

### What NOT To Do
1. **Don't wheel stocks just because the premium is high.** High premium = high risk. Period.
2. **Don't sell puts on stocks you wouldn't want to own.** You WILL get assigned eventually.
3. **Don't sell covered calls below your cost basis.** You're locking in a guaranteed loss.
4. **Don't hold through earnings.** Earnings gaps can wipe out months of premium income in one session.
5. **Don't wheel with money you need in < 12 months.** Capital can get tied up in assigned positions.
6. **Don't roll endlessly.** Two rolls max. If it's still going against you, cut it.
7. **Don't start with 10 positions.** Start with 1-2, learn the mechanics, then scale.
8. **Don't ignore the Greeks.** Delta, theta, and IV are your three most important numbers.
9. **Don't panic when assigned.** Assignment is the strategy working as designed.
10. **Don't compare to S&P returns in a raging bull market.** The wheel trades income for reduced risk. It will underperform in strong bull runs and outperform in flat/choppy markets.

### Key Lessons
- **The wheel works best on stocks that go sideways or slowly up.** Violent moves in either direction hurt.
- **Consistency beats intensity.** 1-2% per month, every month, for years = wealth.
- **Paper trade for at least 1 month before going live.** Learn the mechanics with no money at risk.
- **The first drawdown is the hardest.** Stick to the rules and it recovers.
- **Give it 6-12 months before evaluating.** One bad month doesn't mean the strategy is broken.
- **Transaction costs matter.** Each roll costs commissions. Factor this into your minimum premium threshold.
- **The best wheel traders are boring.** Same stocks, same deltas, same DTE, over and over.

---

## Expected Returns

| Scenario | Monthly | Annualized | Notes |
|----------|---------|------------|-------|
| Conservative (0.20 delta, blue chips) | 1-1.5% | 12-18% | Lowest risk, very few assignments |
| Moderate (0.25-0.30 delta, mixed) | 1.5-2.5% | 18-30% | Standard approach, some assignments |
| Aggressive (0.30-0.40 delta, higher IV) | 2.5-4% | 30-48% | More assignments, more management |

**Realistic expectation for a disciplined wheeler: 15-25% annualized.**
This includes losses on assigned positions, rolling costs, and taxes.

---

## Extracted Bot Rules

```
STRATEGY: OPTIONS_WHEEL (CSP → ASSIGNMENT → CC → CALLED_AWAY → REPEAT)

ENTRY_CSP:
  delta: -0.25 to -0.30
  dte: 30-45 (default 45)
  iv_rank_min: 30
  iv_rank_preferred: 50+
  premium_min_monthly: 1.0%
  earnings_buffer_days: 14
  trend: NEUTRAL_OR_BULLISH

ENTRY_CC:
  delta: +0.25 to +0.30
  dte: 21-30
  strike_floor: adjusted_cost_basis
  earnings_buffer_days: 14

EXIT_PROFIT:
  close_at: 50% of max premium
  close_aggressive: 75% of max premium if DTE < 14

EXIT_TIME:
  hard_close_dte: 21
  never_hold_to_expiration: true

EXIT_LOSS:
  csp_roll_if_down: < 5%
  csp_assign_if_down: > 10%
  max_rolls: 2
  roll_must_be_net_credit: true
  close_if_fundamentals_deteriorate: true

POSITION_SIZE:
  max_single_position: 20% of account
  max_sector_exposure: 30%
  cash_reserve: 20% of account
  simultaneous_positions: 3-8
  stagger_entry_weeks: 2-4

UNIVERSE:
  market_cap_min: 5B
  avg_daily_volume_min: 1M
  option_oi_min: 1000
  price_range: $20-$200
  bid_ask_spread_max: 5%
  
PREFERRED_TICKERS:
  tech: [AAPL, MSFT, GOOGL, ADBE]
  finance: [JPM, BAC, GS, WFC]
  industrial: [CAT, HON, UNP]
  energy: [XOM, CVX]
  healthcare: [JNJ, PFE, UNH, ABBV]
  consumer: [KO, PG, WMT, COST]
  etf: [SPY, QQQ, IWM, XLF, XLE]
  small_account: [F, T, BAC, PFE, INTC]

AVOID:
  meme_stocks: true
  biotech_binary: true
  iv_above: 100%
  price_below: $10
  down_20pct_30days: true

MARKET_CONDITIONS:
  bull: {put_delta: -0.30, call_delta: +0.35}
  neutral: {put_delta: -0.25, call_delta: +0.30}
  high_vol: {put_delta: -0.15, call_delta: +0.25, dte: 45-60}
  bear: {pause_new_csp: true, sell_cc_only: true}
  low_iv: {pause_entries: true, iv_rank_min: 30}

FILTERS:
  no_earnings_within: 14 days
  iv_rank_above: 30
  fundamentals: profitable, low_debt
  diversify: min 3 sectors
```

---

## Reference Sources

- [DaysToExpiry.com — Wheel Strategy Guide](https://www.daystoexpiry.com/blog/wheel-strategy-guide)
- [DaysToExpiry.com — Best Stocks for Wheel Strategy](https://www.daystoexpiry.com/blog/best-stocks-wheel-strategy)
- [DaysToExpiry.com — Complete DTE Playbook](https://www.daystoexpiry.com/blog/wheel-options-trading-strategy-complete-dte-playbook)
- [WheelStrategyOptions.com — Advanced DTE, Delta & Exit Tactics](https://wheelstrategyoptions.com/blog/optimizing-the-wheel-strategy-advanced-dte-delta-and-trade-exit-tactics/)
- [WheelStrategyOptions.com — DTE Optimization](https://wheelstrategyoptions.com/blog/optimizing-dte-for-the-wheel-strategy-weekly-vs-30-45-day-options-and-strategic-rolling/)
- [Option Alpha — Wheel Strategy Guide](https://optionalpha.com/blog/wheel-strategy)
- [Options Cafe — Complete Guide with Real Results](https://options.cafe/blog/wheel-options-strategy-complete-guide/)
- [SteadyOptions — Wheel Strategy Explained](https://steadyoptions.com/articles/wheel-strategy-options-master-wheel-trading-explained-r632/)
- [Johnny Africa — Ultimate Wheel Strategy Guide](https://johnnyafrica.com/option-wheel-strategy/)
- [Charles Schwab — Three Things About the Wheel](https://www.schwab.com/learn/story/three-things-to-know-about-wheel-strategy)
