APIs:
- Alpaca (stocks/options): REST + WebSocket
- Tastytrade (options wheel): REST API
- Interactive Brokers (commodities): TWS API / IB Gateway
- Kraken Pro (crypto): REST + WebSocket
- Polymarket (prediction): CLOB API via MetaMask wallet

Data Feeds:
- Yahoo Finance (free price data fallback)
- Alpaca market data (real-time bars)
- CoinGecko (crypto prices)

Libraries (Python):
- alpaca-trade-api
- ib_insync (IBKR)
- py-clob-client (Polymarket)
- pandas, numpy (data processing)
- ta-lib (technical indicators)

Output:
- Daily P&L report → output/trading/daily-report.md
- Trade log → output/trading/trade-log.csv
- Alert to CEO on: daily loss limit hit / new all-time high / bot error
