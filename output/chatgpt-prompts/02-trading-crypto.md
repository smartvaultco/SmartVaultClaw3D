# PASTE THIS ENTIRE MESSAGE INTO CHATGPT (GPT-4o or Deep Research)

---

You are a senior quantitative analyst and trading strategist. I'm giving you my complete trading knowledge base. Analyze everything, supplement with current 2026 market data and your own expertise, and produce a comprehensive research document.

## CONTEXT

I'm CJ, building automated trading bots for Smart Vault Co. LLC. I trade options (wheel strategy, spreads), crypto (DeFi leverage, liquidity pools), prediction markets (Polymarket), and am developing algo strategies (VWAP, mean reversion, ORB). Budget: starting $2K-$10K per strategy.

## MY TRADING KB (Key Strategies)

### The Wheel Strategy (Options)
- Cash-Secured Put → Assignment → Covered Call → Called Away → Repeat
- Triple income: put premium + call premium + dividends
- Target: 30-45 DTE, 0.25-0.35 delta, IVR > 30
- Exit at 50-75% max profit, roll at 21 DTE
- 10-15 positions, max 5% per position
- Win rate: 70-85% historically
- Best tickers: AAPL, AMD, MSFT, NVDA, PLTR, SOFI, TSLA, SPY, QQQ, IWM

### Jason Brown / Power Trades System
- 3P System: Power Charts + Power Trades + Power Profits
- Top-Down: Market → Sector → Stock
- 5-Year Millionaire Plan: $4K start, 10% monthly, compound to $1M
- 30-stock focus list, 7/10 paper trade success before going live
- Strategies: bull call spreads, bear put spreads, iron condors, straddles, strangles
- Key rules: never risk >2% per trade, always have an exit before entry

### ARCrypto DeFi Strategy
- 3x leverage on BTC/ETH with "bullet" system for protection
- Bullets = pre-funded reserves (equal to initial investment) deployed to lower liquidation price
- Liquidity pool farming (stETH/ETH on Pendle/Aave)
- Funding rate arbitrage: long spot + short perps when funding > 0.03%
- Never leverage altcoins, only BTC/ETH
- Tools: GMX, Aave, Pendle, Lido, 1inch, DeFi Llama, Nansen

### Algo Strategies
- **VWAP**: Buy at VWAP support, sell at upper band. 70-75% S/R hit rate
- **Mean Reversion**: RSI <30 + price below lower Bollinger = buy. RSI >70 + upper = sell
- **Opening Range Breakout (ORB)**: Trade breakout of first 15-30 min range
- **Commodities EMA Crossover**: 9/21 EMA cross on gold, oil, nat gas futures
- **Polymarket Dutch-Book**: Buy YES+NO when combined < $1.00 for risk-free profit

### Risk Management
- Kelly Criterion: Kelly% = W - [(1-W)/R], use half-Kelly in practice
- Max 2% risk per trade, 6% max daily drawdown
- Correlation check before adding positions
- Cash reserve: always keep 30-40% in cash/stablecoins

### Position Sizing by Strategy
| Strategy | Kelly% | Half-Kelly | Max Position |
|----------|--------|------------|-------------|
| Wheel CSP | 47% | 23% | 5% of portfolio |
| Bull Call Spread | 30% | 15% | 2% risk |
| DeFi 3x Leverage | 23% | 12% | 10% of crypto allocation |
| VWAP Scalp | 38% | 19% | 2% risk |
| Polymarket Arb | 90%+ | 45% | 10% of bankroll |

---

## YOUR ASSIGNMENT

Produce a comprehensive research document with these 5 sections:

### SECTION 1: Strategy Validation & Gaps
- Which of my strategies are well-structured? Which have holes?
- What risk management improvements would you recommend?
- Are my Kelly Criterion calculations reasonable for each strategy?
- What strategies am I missing that fit my risk profile and capital?
- What's my biggest blind spot as a trader?

### SECTION 2: 2026 Market Conditions
- Current options market conditions (VIX, IV environment, wheel viability)
- Crypto market state (BTC/ETH price action, DeFi yields, leverage environment)
- Polymarket volume, liquidity, and regulatory status
- Best sectors/tickers for wheel strategy right now
- Any regime changes that affect my strategies?

### SECTION 3: Bot Architecture Recommendations
- Best tech stack for each trading bot in 2026
- APIs: which brokers/exchanges have the best API for automation?
- Backtesting frameworks (Backtrader, QuantConnect, Zipline, etc.)
- Real-time data feeds and their costs
- Hosting/execution environment (cloud vs local, latency considerations)

### SECTION 4: Sellable Products from This Knowledge
- What trading courses/tools could I sell based on this KB?
- For each: name, format, price, target buyer
- What's the market for trading education in 2026?
- How do I differentiate from the 10,000 other "trading gurus"?

### SECTION 5: Risk Scenarios & Stress Tests
- What happens to each strategy in a crash (2008-style, COVID-style)?
- What happens in a prolonged sideways/low-IV market?
- What happens if Polymarket gets regulated/shut down?
- What's my max drawdown scenario across all strategies simultaneously?
- What circuit breakers should I build into my bots?

---

## OUTPUT FORMAT
- Use clear headers and data tables
- Include specific tickers, numbers, and current prices where relevant
- Be quantitative — no vague advice
- Cite sources and include URLs where possible
- Target: 3,000-5,000 words
