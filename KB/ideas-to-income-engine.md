# Ideas → Income Engine — Smart Vault Co.

**Source:** Internal strategy document (2026-04)
**Target:** U.S. SMB owners, 45–60, top-tier zip codes
**Services:** AI automation, AI animation, AI ads, software/apps, robotics

---

## 1 — WHO (Audience Persona: "Pat")

| Field | Value |
|-------|-------|
| Age | 45–60 |
| Location | U.S. — Top 5% zip codes |
| Business size | 3–50 employees |
| Industries | Professional services, specialty retail, high-margin local, boutique agencies |
| Pain | Repetitive ops waste, poor ad spend, low-quality content, no in-house tech team |
| Purchase triggers | ROI in months, time savings, no long onboarding, local peer case studies |
| Channels | LinkedIn, Google Search, targeted Meta, premium email, warm outreach + audit offers |
| LTV target | $6k–$30k/year (setup + recurring automation + ad management + animation) |

---

## 2 — WHAT (Core Transformation)

**Big Promise:** Turn your existing leads and workflows into automated, revenue-driving systems that run with minimal oversight — with cinematic AI creative and measurable ROI within 90 days.

**Problem:** Owners waste time on repetitive ops, poor ad spend, and low-quality content; they need plug-and-play AI systems that deliver more leads and higher close rates without hiring full teams.

**Primary Outcomes:**
- Working automation saves 20–40+ hours/month
- AI ad funnel + animated creatives increase qualified leads (benchmarked)
- Repeatable funnel: audit → paid pilot → managed service

---

## 3 — DATA SOURCES (Priority Order)

**Owned / First-Party:**
- CRM events: contacts, tags, conversation transcripts (GHL / HubSpot / Pipedrive)
- Website analytics: GA4 (pages, funnels, conversion events)
- Payments & orders: Stripe, Shopify, QuickBooks
- Ads platform data: Google Ads, Meta Ads, LinkedIn Ads
- Product usage logs (SaaS/apps/robotics telemetry)

**Community / Social Signals:**
- LinkedIn comments & messages, YouTube comments, Instagram DMs, FB groups, Discord/Telegram threads

**Market Signals & Competitive:**
- Competitor landing pages, product listings, pricing (SERP API / manual)
- Keyword volume & trends (Google Keyword Planner, Google Trends)
- Ad CPC/CPM baselines: Google Search CPC ~$2.7–$5+; Meta lead CPC lower (varies)

**AI/Creative Tools:**
- Veo3 for cinematic short-form assets and animation pipelines

---

## 4 — CORE ENGINES

### A — Intake Engine (voice/text → clarity)
**Concept:** Capture idea or client pain (voice/text DM/meeting) → structured idea card.

**Automation Flow (Make/Zapier):**
1. Trigger: New voice memo (WhatsApp/Loom) or new DM via webhook
2. Action: Auto-transcribe (AssemblyAI / Otter via API)
3. Action: POST transcript to LLM with Intake Parser prompt
4. Action: Save JSON to Notion/Sheet with tags (ai-automation, ads, animation)

**SLA:** Idea → parsed card in <30 minutes.

---

### B — Research Engine
**Concept:** Validate demand fast; gather competitive & ad signals.

**Automation Flow:**
- Trigger: Idea card status = `research`
- Actions: LLM Research Synthesizer + SERP API web-scrape + competitor landing capture
- Output: `research_card` with 3 validation tests + estimated CPC ranges

**Test budgets:** $30–$75/day per test, 3–7 days.

---

### C — Offer Engine
**Concept:** Turn validated idea → clear monetizable offer ladder for SMB buyers.

**Offer Ladder (Smart Vault):**
| Tier | Name | Price |
|------|------|-------|
| Free | 15-min AI audit | $0 (lead magnet) |
| Tripwire | Automated audit + video + checklist | $97 |
| Core | Done-With-You automation pilot (30–60 days) | $2,497 |
| Scale | Managed AI + Ads Retainer | $5k–$25k |

**Conversion angle for 45–60 SMBs:** Emphasize time saved, cashflow impact, risk minimization (guarantee), local peer case studies.

---

### D — Funnel Engine
**Concept:** One-click micro-launch funnels built from templates (GHL + Stripe + analytics).

**Core Funnel Templates:**
1. Audit funnel (lead magnet → tripwire → book audit)
2. AI Audit → Paid Pilot → Retainer funnel
3. Animated case study funnel (video-led) for premium prospects

**Auto-Deploy Workflow (Make):**
1. Trigger: Offer status = `ready`
2. Create GHL funnel (page copy + form), Stripe product, GHL email sequence, Trello asset tasks, UTM/pixel snippet

**Quick Checklist:** Landing hero, 3-email nurture, checkout, thank-you upsell, 1 ad creative set (3 sizes), analytics (GA4 + Meta pixel).

---

### E — Asset Creation Engine
**Concept:** AI factory that produces copy, animated demos, short ads, voiceovers, and UX assets.

**Production Stack:**
- LLMs → script + copy
- Veo3 → cinematic shorts
- ElevenLabs/Suno → voiceover + audio
- Midjourney/Leonardo → stills
- Canva/Canva API → thumbnails

**Two Creative Styles:**
1. "Executive Explainer" — polished, short (for LinkedIn/Google)
2. "Case Study Story" — animation-led (for Meta retargeting, premium prospects)

---

### F — Execution Engine
**Concept:** Ops + launch playbook that runs the funnel, ad sets, and fulfillment.

**Roles:**
- AI agent: Drafts all assets & ad copy
- Creative lead: QA & produce final assets
- Growth lead: Launch ads, monitor budgets
- Ops lead: Connect payments, schedule client onboarding

**Auto-scale rule:** If CPL < target AND conversion rate > target for 72 hours → increase budget +30% (automated rule in Ads Manager or via API).

**Onboarding:** Hybrid call within 72 hours; 30–60 day pilot with weekly cadence + KPI dashboards.

---

### G — Feedback Engine
**Concept:** Turn first-100 buyers into insight for improvements — automated surveys + LLM analysis.

**Data In:** Ad performance, funnel drop-offs, NPS / post-purchase short survey, one-on-one call transcriptions.

**Decision cadence:** Review after 7 days of live test or after 50 leads.

**Feedback captures:** Quick ROI figure at week-1 and week-4 to show client impact.

---

## 5 — 8-STEP SOP (Repeatable)

1. Capture idea → Intake Parser
2. Research Synthesizer → 3 tests recommended
3. Choose 1 test → Offer Architect builds ladder
4. Creative Pack Generator → assets created
5. Funnel Auto-Deploy → GHL + Stripe + email
6. Launch small paid traffic ($30–75/day per audience)
7. After 7 days / 50 leads → Feedback Analyst
8. Decision: scale / optimize / kill. Archive iterations with tags.

---

## 6 — MEASUREMENT & BUDGET

**Initial micro-test budget:** $150–$350 total per idea (3–7 days) across Google + Meta + LinkedIn.

**Platform guidance:**
- LinkedIn: expensive but high intent for SMBs
- Meta/IG: cheaper for retargeting
- Google Search: highest purchase intent

**Key KPIs:** CPL, landing CVR, trial conversion rate, first-month revenue per client, payback period (ROI ≤90 days).

---

## 7 — 14-DAY QUICK LAUNCH PLAN

| Days | Tasks |
|------|-------|
| 0–3 | Connect transcription & intake webhook (Otter/AssemblyAI → Notion). Create Notion Idea HQ. Build prompt library. |
| 4–7 | Create 3 funnel templates in GHL + Stripe products for tripwires. Build one Offer Ladder (AI Audit → Pilot → Retainer). |
| 8–10 | Run test idea: Intake → Research → Offer → Creative Pack → deploy funnel. Launch ads $30/day x 3 audiences for 5 days. |
| 11–14 | Run Feedback Analyst; decide scale/pivot/kill. Package learnings into SOP. |

---

## 8 — TEMPLATES TO BUILD ONCE

- Notion Idea HQ with statuses & fields
- 3 GHL funnel templates (Audit, Audit→Pilot, Animated Case Study)
- Prompt library (7 prompts — see `prompts/ideas-income-prompt-library.md`)
- Ad test spreadsheet template (audiences, creatives, metrics)
