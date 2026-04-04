Primary Platforms:
- Make.com (primary automation — 1,000+ app integrations)
- GoHighLevel (CRM automations, pipeline triggers, webhooks)
- Zapier (fallback when Make.com gaps exist)

Integration Stack:
- Shopify ↔ AutoDS (order fulfillment trigger)
- GHL ↔ all bots (lead routing, notifications)
- Gumroad ↔ GHL (buyer list sync)
- Trading bots ↔ Analytics Bot (P&L feed)
- Content Builder ↔ Social Media Bot (publish queue)
- Real Estate Bot ↔ GHL CRM (lead pipeline)

Webhook Tools:
- Webhook.site (testing)
- ngrok (local endpoint testing)
- Make.com webhooks (production)

Documentation:
- All scenarios documented → output/automations/
- Naming: [BOT]-[TRIGGER]-[ACTION].md

Monitoring:
- Make.com execution logs
- Error notifications → CEO via Discord webhook
- Monthly automation audit (kill unused scenarios)
