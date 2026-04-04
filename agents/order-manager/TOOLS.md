APIs:
- Shopify Admin API (order management)
- AutoDS API (fulfillment automation)
- CJDropshipping API (supplier fallback)
- GoHighLevel (customer notifications)

Monitoring:
- Shopify webhook: order/created → trigger AutoDS
- Fraud score check on every order > $100
- Inventory alert: supplier stock < 20 units

Output:
- Daily order report → output/ecommerce/daily-orders.md
- Refund log → output/ecommerce/refunds.csv
- Inventory alerts → CEO + Product Scout
