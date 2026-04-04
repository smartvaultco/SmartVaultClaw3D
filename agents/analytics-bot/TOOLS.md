Data Sources:
- Alpaca API (trading P&L)
- Tastytrade API (options P&L)
- IBKR API (commodities P&L)
- Shopify Analytics API (e-commerce revenue)
- Gumroad API (digital product sales)
- GoHighLevel Reports API (pipeline + email metrics)
- Meta Ads API (ROAS, spend)
- Google Analytics (website traffic)

Reporting:
- Daily scorecard → output/reports/daily-YYYY-MM-DD.md
- Weekly summary → output/reports/weekly/
- Monthly P&L → output/reports/monthly/
- SBTLC client report → output/reports/sbtlc/

Dashboard:
- Looker Studio (visual dashboard — connects to all data sources)
- GHL reporting dashboard

Alerts (send to CEO):
- Any metric drops >20% vs prior week
- Any bot has 3 consecutive losing days
- Any product has >5% refund rate
- Monthly revenue misses target by >20%
