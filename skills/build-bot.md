# Build Trading Bot Script

Scaffold a Python trading bot script for Smart Vault Co.

Ask the user:
1. Which bot? (Polymarket / Options Wheel / VWAP / Commodities EMA / ARCrypto)
2. Paper trading or live? (default: paper until told otherwise)
3. Any specific parameters to adjust from the MASTER-PLAN.md defaults?

Then generate a complete Python bot script with:
- API connection setup (using env variables from .env)
- Strategy logic as documented in the KB
- Position sizing (Kelly Criterion or fixed %)
- Entry + exit rules
- Daily loss limit check
- Trade logging to CSV
- Error handling + restart on crash
- PM2-compatible (handles SIGTERM gracefully)

Save to: `e:/Smart-Vault-Ai/output/bots/[bot-name].py`
Print instructions to run with PM2.
