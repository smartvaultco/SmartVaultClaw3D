# The AI Growth Masterclass
## Course Modules 7-10: Full Production Scripts + Materials
### By CJ | Smart Vault HQ

---

# MODULE 7: AI Chatbots + Voice Agents: 24/7 Sales and Support on Autopilot

---

## A) VIDEO LESSON SCRIPT (18 minutes)

### INTRO (2 minutes)

**[SLIDE: Module 7 Title Card — "AI Chatbots + Voice Agents: 24/7 Sales and Support on Autopilot"]**

Hey, welcome back. This is Module 7, and we are going deep on something that, frankly, is the single biggest revenue leak I see in small businesses. And it is this: nobody is answering.

Nobody is answering the website question at 10 PM. Nobody is answering the Instagram DM on Saturday afternoon. Nobody is picking up the phone when your team is at lunch.

Harvard Business Review published a stat that still shocks me every time I say it out loud: companies that respond to leads within five minutes are one hundred times more likely to connect than those who wait thirty minutes. Not ten percent more likely. One hundred times.

And the average small business response time to a web inquiry? Forty-seven hours.

Now, back in Module 3, we introduced the concept of AI-assisted customer interactions. This module goes way deeper. We are building a full AI customer experience layer — chat, social DMs, and voice — that handles eighty percent of your inquiries without a human touching anything. And the secret sauce is that your bots are powered by YOUR business knowledge, not some generic script somebody wrote in twenty minutes.

Here is what you will learn in the next fifteen minutes: the three deployment zones every business needs, how to build an escalation protocol so the bot knows when to hand off to a human, and how your Smart Vault powers the whole thing so your bots actually know your business.

Let us get into it.

---

### TEACH (10 minutes)

**[SLIDE: "The Cost of Silence — Let's Do the Math"]**

Before we build anything, let us understand what is at stake. Say you get two hundred website visitors a day. Industry average says two to five percent want to engage — ask a question, get a quote, book a call. That is four to ten potential conversations per day.

If you are only staffed nine to five, you are missing roughly sixty percent of those windows. That is six missed conversations per day, one hundred eighty per month. If your average customer lifetime value is two thousand dollars and you close twenty percent of engaged leads, those missed conversations cost you: one hundred eighty times twenty percent times two thousand dollars — thirty-six thousand dollars per month. On the conservative side.

That is not hypothetical. That is math.

**[SLIDE: "The Three Deployment Zones"]**

Now here is the framework. We deploy your AI customer experience layer across three zones. Think of these as the three doors customers use to reach you.

**Zone 1: Website Chat Widget.** This is your digital front door. A visitor lands on your site, has a question about pricing, and your chat widget greets them within three seconds. It qualifies them — "What brought you here today?" It answers from your knowledge base. It captures their name, email, phone. It books the appointment. No human needed for eighty percent of those conversations.

We are going to set this up in GoHighLevel. GHL has a built-in chat widget that connects directly to your CRM, so when a visitor chats, the contact is automatically created. If they book, it hits your calendar. If they need follow-up, they enter your pipeline.

**[SLIDE: "Zone 2 — Social DM Agents"]**

**Zone 2: Social DMs.** Instagram, Facebook Messenger, WhatsApp. This is where your customers already are. Seventy-six percent of consumers expect brands to respond to social messages within twenty-four hours. Thirteen percent expect it within one hour. Your DM bot acknowledges immediately, identifies intent, answers from your knowledge base, and offers the next step.

Your SLA target here: four-hour response time on all DMs. The bot handles it instantly, but the four-hour SLA is your backstop for anything that needs human follow-up.

**[SLIDE: "Zone 3 — Voice and Voicemail Agents"]**

**Zone 3: Voice and Voicemail.** This is where it gets really powerful. AI voice agents can now answer your business phone, handle basic inquiries, take messages, and route calls. And they sound natural enough that most callers do not realize they are talking to AI.

You pair something like ElevenLabs with a voice agent platform, and you have an AI receptionist answering every call, twenty-four seven. Voicemail gets transcribed and sent to you instantly. Calls get routed based on intent — sales call goes to your cell, support question gets handled by the bot. After-hours, the bot can even book appointments.

For most small businesses, this single deployment eliminates the need for a dedicated receptionist. That is twenty-five hundred to four thousand dollars a month in savings.

**[SLIDE: "The Escalation Protocol — Tier 1 vs Tier 2"]**

Now, critical piece. No bot should pretend to be something it is not. Every AI customer experience layer needs clear escalation rules.

**Tier 1 — Bot Handles:** Hours, location, general info. Product and service descriptions. Pricing. Appointment booking and rescheduling. Order status. FAQ responses. Basic troubleshooting. This is the eighty percent.

**Tier 2 — Bot Flags for Human:** Complaints or negative sentiment. Refund or dispute requests over one hundred dollars. Technical issues needing account access. Custom quotes. Anything the bot cannot answer from its knowledge base. This is the twenty percent.

Here is the key rule: when the bot escalates, it collects all the context first. The human does not get a raw chat log. They get a summary — "Customer Jane Smith is requesting a refund for Order 4523, placed March 15th, amount two hundred forty-seven dollars. She says the product arrived damaged. Photos attached."

Your human response SLAs: four hours for DMs, twenty-four hours for support emails.

And here is the optimization loop that makes this whole system get smarter over time: every escalation gets logged. If the same question triggers escalation three or more times, you add the answer to your knowledge base. Over time, your Tier 1 handles more and your Tier 2 shrinks.

**[SLIDE: "Smart Vault Powers Everything"]**

Now, why does this actually work when most chatbots feel terrible? Because of the Smart Vault.

Most businesses install a generic chat widget, load it with ten canned responses, and wonder why customers hate it. The reason those bots fail is simple — they do not know your business.

Your Smart Vault in NotebookLM stores your FAQs, product details, pricing tiers, service descriptions, policies, common objections, competitor comparisons, and customer success stories. When a customer asks your bot a question, the bot does not guess. It retrieves the answer from your actual business intelligence.

You upload your top twenty FAQs into NotebookLM. You take that same content and paste it into your GHL chat widget's system prompt. Now your bot knows your business as well as your best employee.

One source of truth. Three deployment zones. All powered by the same knowledge base.

**[SLIDE: "Monthly Metrics to Track"]**

Quick metrics to monitor monthly. Bot resolution rate — target seventy to eighty percent. Response time — target under ten seconds. Escalation rate — if it is over thirty percent, your knowledge base has gaps. Customer satisfaction — one-question post-chat survey, target eighty-five percent positive. Lead capture rate — target forty percent of conversations result in a captured email or phone.

---

### DEMO (4 minutes)

**[SCREEN SHARE: GoHighLevel Dashboard]**

Alright, let me show you how to set this up. I am in GoHighLevel right now. Let me walk you through deploying a chat widget with custom responses and escalation routing.

**[Screen share — navigate to Sites > Chat Widget in GHL]**

First, we go to Sites, then Chat Widget. I am going to click "Create New Widget." Give it a name — let us call it "Main Site Chat."

Now, here is where most people stop. They put in a generic greeting and call it done. We are not doing that.

**[Screen share — configuring the bot prompt]**

Under the bot configuration, I am going to paste in a system prompt. Watch this. I am writing: "You are a customer service representative for [our business name]. Answer questions using only the following information." And then I paste in our top twenty FAQs — the same ones sitting in our Smart Vault.

I add: "If you cannot answer from this information, say 'Let me connect you with our team' and collect their name, email, and phone number."

That last line? That is your escalation trigger. The bot knows its boundaries.

**[Screen share — setting up the qualification flow]**

Now I set the initial greeting: "Hey! Welcome to [Business Name]. What brought you here today — looking for information about our services, or do you have a question about an existing order?"

Based on their response, the bot routes them down different paths. Services questions pull from the knowledge base. Existing order questions ask for an order number. Anything the bot cannot handle gets flagged.

**[Screen share — showing escalation routing]**

Here is the escalation piece. Under Workflows, I have a trigger: "When chat conversation is escalated." The workflow sends an internal notification to my team via SMS and email, includes the full conversation summary, and assigns it in the pipeline as "Needs Human Response."

**[Screen share — showing the live widget on a test page]**

Let me pull up the test page. There is the widget in the bottom right. I click it, it greets me. I type "What are your pricing options?" and watch — it responds with our actual pricing tiers, pulled from the FAQ content we loaded. That is not a canned response. That is our business intelligence at work.

And that took us about fifteen minutes to set up. Zone 1 is live.

---

### RECAP (2 minutes)

**[SLIDE: "Module 7 — Key Takeaways"]**

Alright, let us wrap Module 7. Three key takeaways.

**One:** Deploy across three zones — website chat, social DMs, and voice. Each one plugs a different leak in your customer experience. Start with the website chat widget because it is the fastest to set up and has the most immediate ROI.

**Two:** Build a clear escalation protocol. Tier 1 is bot-handled — the eighty percent. Tier 2 is human-flagged — the twenty percent. Set your SLAs: four hours on DMs, twenty-four hours on emails. And log every escalation so you can keep making your knowledge base smarter.

**Three:** Your Smart Vault powers everything. Upload your top twenty-plus FAQs, product info, pricing, and policies into NotebookLM. That same content feeds your chat widget, your DM bots, and your voice agents. One source of truth across all three zones.

**Action items before the next module:** Map your three deployment zones. Write your escalation rules. List your top twenty FAQs and upload them to your Smart Vault.

Next up, Module 8 — we are building no-code automations that will replace forty hours of manual work this month. See you there.

---

## B) PDF WORKSHEET

### MODULE 7 WORKSHEET: AI Chatbots + Voice Agents

**Key Concepts:**
- The AI Customer Experience Layer deploys intelligent bots across three zones: website chat, social DMs, and voice/voicemail
- Bots fail when they answer from generic scripts; bots succeed when powered by YOUR knowledge base (Smart Vault)
- Escalation Protocol: Tier 1 (bot-handled, ~80%) vs. Tier 2 (human-flagged, ~20%)
- SLA targets: 4-hour response on DMs, 24-hour response on support emails
- Every repeated escalation is a gap in your knowledge base — fill it and the bot gets smarter
- Monthly metrics: bot resolution rate (70-80%), response time (<10s), escalation rate (<30%), lead capture rate (40%+)

**Fill-in-the-Blank Exercises:**

1. Companies that respond to leads within _______ minutes are 100x more likely to connect than those who wait 30 minutes.

2. The three deployment zones are: ______________, ______________, and ______________.

3. Tier 1 issues are handled by the _______. Tier 2 issues are flagged for a _______.

4. Your SLA target for social DM responses is _______ hours.

5. If the same question triggers escalation _______ or more times, you should add the answer to your ______________.

**Apply to YOUR Business:**

1. List your three deployment zones in order of priority for YOUR business. Which zone do your customers use most to reach you? Start there.
   - Zone 1 (highest priority): _________________________________
   - Zone 2: _________________________________
   - Zone 3: _________________________________

2. Write your escalation rules. What specific issues should the bot handle (Tier 1)? What should be flagged for a human (Tier 2)?
   - Tier 1 (Bot Handles): _________________________________
   - Tier 2 (Human Flags): _________________________________

3. List your top 20 FAQs — the questions your team gets asked more than twice. These will be uploaded to your Smart Vault and used to power all three deployment zones.

---

## C) ACTION CHECKLIST

### MODULE 7: Action Checklist

- [ ] Brain-dump your top 20-30 customer questions into a document and upload it to NotebookLM (your Smart Vault)
- [ ] Install a chat widget on your website using GHL — configure the system prompt with your FAQ knowledge base content
- [ ] Set up automated DM responses on your highest-traffic social platform (Instagram or Facebook) with a 4-hour SLA backstop
- [ ] Write your Tier 1 / Tier 2 escalation protocol and configure escalation routing in your GHL workflow
- [ ] Schedule a weekly review of escalation logs — every gap you fill makes every bot smarter simultaneously

---

## D) QUIZ

### MODULE 7 QUIZ

**1. What are the three deployment zones for AI customer experience?**
- A) Email, phone, fax
- B) Website chat, social DMs, voice/voicemail
- C) CRM, calendar, invoicing
- D) Facebook, Google, LinkedIn

**Correct Answer: B**

---

**2. What is the SLA target for responding to social media DMs?**
- A) 30 minutes
- B) 1 hour
- C) 4 hours
- D) 24 hours

**Correct Answer: C**

---

**3. In the escalation protocol, what should happen when the same question triggers a Tier 2 escalation three or more times?**
- A) Block the customer from chatting
- B) Remove the chat widget from that page
- C) Add the answer to your knowledge base so the bot handles it next time
- D) Hire another support rep to handle the volume

**Correct Answer: C**

---
---

# MODULE 8: The No-Code Automation Playbook: Replace 40 Hours of Work This Month

---

## A) VIDEO LESSON SCRIPT (19 minutes)

### INTRO (2 minutes)

**[SLIDE: Module 8 Title Card — "The No-Code Automation Playbook: Replace 40 Hours of Work This Month"]**

Welcome to Module 8. This is one of my favorite modules because this is where you get time back. Actual hours back in your week.

Here is the dirty secret every business owner shares: somewhere in your operation right now, a human being is copying data from one screen and pasting it into another. Every. Single. Day.

Maybe your office manager is transferring form submissions into your CRM by hand. Maybe you — at 9 PM on a Tuesday — are manually sending follow-up emails to people who booked a call. Maybe your bookkeeper is re-entering invoice data because two systems do not talk to each other.

That is not work. That is a tax on your business. And you are paying it in the most expensive currency there is: human attention.

The average small business spends twenty to forty hours per month on tasks that can be fully automated with tools that already exist, require zero coding, and cost less than a team lunch.

In this module, I am going to teach you two things. First, the Ideas-to-Income Engine — our eight-step SOP for turning any business initiative into a systemized, automated machine. Second, the five automations every business should build first, and I am going to show you how to build one of them live. Let us go.

---

### TEACH (11 minutes)

**[SLIDE: "The Real Cost of Manual Work"]**

Let me put dollars on this. If you or your team spend thirty hours a month on manual, repetitive work — data entry, appointment reminders, invoice chasing, social scheduling, review requests — and your fully loaded labor cost is thirty dollars an hour, that is nine hundred dollars a month. Ten thousand eight hundred dollars a year. On work a machine does better, faster, and without calling in sick.

But the real cost is not just the labor. It is the errors. Manual data entry has a one to four percent error rate. When your employee fat-fingers a phone number, that lead is gone forever. When they forget the appointment reminder, that no-show costs you one hundred fifty to five hundred dollars. When the follow-up email goes out three days late instead of three hours late, your close rate drops by fifty percent.

Automation does not just save time. It eliminates the failure modes that bleed revenue from every manual process.

**[SLIDE: "The Ideas-to-Income Engine — 8 Steps"]**

Alright, before we talk about specific automations, you need the framework. At Smart Vault HQ, every new initiative runs through our eight-step Ideas-to-Income Engine. Write these down.

Step 1: Capture the Idea. Write it down. Voice memo. Sticky note. Whatever. But capture it before it disappears.

Step 2: Research. Validate demand. Use AnswerThePublic, competitor analysis, customer feedback. Do people actually want this?

Step 3: Build the Offer. Define what you are selling, to whom, at what price.

Step 4: Create the Creative. Ad copy, landing pages, content, emails.

Step 5: Build the Funnel. Lead capture, nurture sequence, sales process.

Step 6: Launch. Go live with a small budget. Twenty to fifty dollars a day max.

Step 7: Collect Feedback. What is working? What is not? Use data, not gut feeling.

Step 8: Scale or Kill. If ROI is there, double down. If not, kill it fast. No emotions.

Here is the key insight: every single step in this engine can be partially or fully automated. The question is not "Can I automate this?" — it is "Which step is costing me the most time right now?" Automate the thing that hurts the most first.

**[SLIDE: "The 5 Automations Every Business Should Build First"]**

Now let us get specific. I have worked with dozens of small businesses on their automation stack. Regardless of industry, these five automations deliver the highest ROI in the shortest time. Build them in this order.

**[SLIDE: "Automation #1 — Lead Notification + CRM Entry"]**

**Number 1: Lead Notification plus CRM Entry.** Someone fills out a form on your website. The notification goes to an email inbox you check twice a day. By the time you see it, the lead is cold.

The automation: Form submitted. Zapier or Make catches it instantly. Contact created in CRM. Instant SMS to you or your salesperson — "New lead: name, phone, interested in this service." Automated email to the lead — "Thanks for reaching out, here is what happens next." Lead enters your pipeline at Stage 1.

Time saved: five to ten hours a month. Setup time: thirty minutes.

**[SLIDE: "Automation #2 — Booking + Reminders"]**

**Number 2: Appointment Booking plus Reminders.** Client books via your calendar. Immediate confirmation email and SMS. Twenty-four hours before: automated reminder. One hour before: another reminder. If they no-show: automated "We missed you" message fifteen minutes after the appointment time.

Time saved: three to five hours a month. But the real impact is this — no-show rates drop from twenty-five to thirty percent down to eight to twelve percent. If you do twenty appointments a month at three hundred dollars each, that is nine hundred dollars a month saved just from fewer no-shows.

**[SLIDE: "Automation #3 — Invoice Follow-Up"]**

**Number 3: Invoice Generation plus Payment Follow-Up.** Job marked complete. Invoice auto-generated and sent. Day 3: friendly reminder if unpaid. Day 7: firmer reminder. Day 14: final notice. Payment received: automated thank-you.

Businesses that automate payment follow-ups see average days-to-payment drop from twenty-eight days to eleven days. That is cash in your account seventeen days sooner.

**[SLIDE: "Automation #4 — Social Scheduling"]**

**Number 4: Social Media Scheduling.** Batch-create content weekly using AI. Load posts into Buffer, Later, or GHL's social planner. Schedule a week of content in thirty minutes on Monday. Auto-publish across all platforms. Weekly engagement report auto-generated.

Time saved: eight to twelve hours a month. And consistent posting increases organic reach three to five times compared to sporadic posting.

**[SLIDE: "Automation #5 — Review Collection"]**

**Number 5: Review and Testimonial Collection.** Job completed, trigger from CRM. Wait twenty-four to forty-eight hours. Automated SMS: "Hey, would you mind leaving us a quick review?" with your Google review link. If no response in three days, follow-up email. If they leave a review, automated thank-you.

Businesses that systematically request reviews get three to four times more than those that do not. And every ten new Google reviews increases local search clicks by roughly twenty-five percent.

**[SLIDE: "Three Platforms — When to Use Each"]**

Now, which tools do you use? There are three platforms, and each has a sweet spot.

**Zapier — The Easy Button.** Best for simple if-then automations. Form submitted, create contact. Appointment booked, send SMS. Massive app library — over six thousand integrations. Dead-simple interface. Downside: gets expensive at scale with per-task pricing. Twenty-nine to sixty-nine dollars a month for most small businesses.

**Make.com — The Power Tool.** Best for multi-step workflows with conditional logic. If customer bought Product A, send Email Sequence B. Visual workflow builder, more flexible than Zapier, better pricing at scale. Steeper learning curve. Sixteen to twenty-nine dollars a month.

**n8n — The Heavy Lifter.** Best for heavy data processing, web scraping, multi-step AI reasoning chains. Self-hosted, so no per-task fees and unlimited executions. Requires a server — a five to ten dollar a month VPS works fine. More technical to set up initially. But once it is running, it is a beast.

**My recommendation:** Start with Zapier for your first two or three automations. Move to Make.com once you need more complex logic. Add n8n when you are doing heavy data processing or AI-powered workflows and do not want to pay per execution.

---

### DEMO (4 minutes)

**[SCREEN SHARE: Make.com Dashboard]**

Alright, let me show you how to build Automation Number 1 — lead notification plus CRM entry — live in Make.com. I am choosing Make over Zapier for this demo because I want you to see the visual workflow builder.

**[Screen share — Make.com scenario builder]**

I am in Make.com. I click "Create a new scenario." This is the visual builder — every step is a circle, and you connect them left to right.

**[Screen share — adding the trigger module]**

First module: the trigger. I search for my form tool. Let us say we are using a GHL form. I select "Watch New Form Submissions" as the trigger. I connect my GHL account — you do this once, it remembers it. I select the form I want to watch.

Now, every time someone fills out that form, this scenario fires.

**[Screen share — adding the CRM module]**

Second module: CRM entry. I add a GHL module — "Create or Update Contact." I map the form fields: first name, last name, email, phone number, the service they are interested in. These fields auto-populate from the trigger.

**[Screen share — adding the SMS notification]**

Third module: SMS notification. I add a Twilio module — "Send an SMS." The recipient is my cell number. The message body is: "New lead: [First Name] [Last Name], phone [Phone], interested in [Service]." All of those are mapped from the form data.

**[Screen share — adding the email to the lead]**

Fourth module: email to the lead. I add a Gmail or GHL email module. Subject: "Thanks for reaching out to [Business Name]!" Body: "Hi [First Name], we received your inquiry about [Service]. Here is what happens next — one of our team members will be in touch within the hour."

**[Screen share — showing the complete flow]**

There it is. Four modules, connected left to right. Form submission triggers the whole chain. CRM entry, SMS to me, email to the lead. All automatic. All instant.

I click "Run Once" to test it. I go fill out the form on my website. Come back to Make — there it is, all four modules show green check marks. My phone buzzes with the SMS notification. The lead got their email. The contact is in my CRM.

Setup time: about fifteen minutes. And this will run every time someone fills out that form, twenty-four seven, forever. No human needed.

---

### RECAP (2 minutes)

**[SLIDE: "Module 8 — Key Takeaways"]**

Alright, Module 8 recap. Three takeaways.

**One:** Use the Ideas-to-Income Engine as your eight-step SOP for systemizing any business initiative. Every step can be automated. Start with the step that costs you the most time.

**Two:** Build the five core automations in order — lead notification, booking reminders, invoice follow-up, social scheduling, review collection. These alone will reclaim twenty to forty hours a month.

**Three:** Start with Zapier for simplicity, graduate to Make.com for power, and use n8n when you need heavy lifting or unlimited executions. You do not need all three on day one.

**Action items:** Audit your manual tasks this week. Rank them by time wasted. Build your first automation — lead notification plus CRM entry — today. It takes thirty minutes, and you will never manually enter a lead again.

Next up, Module 9 — we are talking about the Build versus Buy versus Hire decision. How to choose the right path for getting AI working in YOUR business without wasting time or money. See you there.

---

## B) PDF WORKSHEET

### MODULE 8 WORKSHEET: The No-Code Automation Playbook

**Key Concepts:**
- The average small business wastes 20-40 hours/month on manual, repetitive tasks that can be automated with zero coding
- Ideas-to-Income Engine: 8-step SOP (Capture, Research, Build Offer, Create Creative, Build Funnel, Launch, Collect Feedback, Scale or Kill)
- Top 5 automations to build first: lead notification, booking + reminders, invoice follow-up, social scheduling, review collection
- Three platforms: Zapier (easy, $29-69/mo), Make.com (powerful, $16-29/mo), n8n (heavy/self-hosted, free + $5-10/mo VPS)
- Automate the thing that hurts the most first — do not try to automate everything on day one

**Fill-in-the-Blank Exercises:**

1. The eight steps of the Ideas-to-Income Engine are: Capture, _______, Build Offer, Create Creative, _______, Launch, Collect Feedback, and _______.

2. Businesses that automate payment follow-ups see average days-to-payment drop from _______ days to _______ days.

3. _______ is best for simple if-then automations, _______ is best for multi-step workflows, and _______ is best for heavy data processing.

4. Automated appointment reminders can reduce no-show rates from 25-30% down to _______%.

5. Every ten new Google reviews increases local search clicks by roughly _______%.

**Apply to YOUR Business:**

1. List every repetitive task you or your team does weekly. Estimate time spent on each. Circle the top 3 time-wasters:

   | Task | Time/Week | Could Be Automated? |
   |------|-----------|-------------------|
   |      |           |                   |
   |      |           |                   |
   |      |           |                   |
   |      |           |                   |
   |      |           |                   |

2. Which of the 5 core automations would save YOUR business the most time right now? Rank them 1-5 for your situation:
   - ___ Lead notification + CRM entry
   - ___ Appointment booking + reminders
   - ___ Invoice follow-up
   - ___ Social media scheduling
   - ___ Review collection

3. Based on your technical comfort level and budget, which platform should YOU start with? (Circle one: Zapier / Make.com / n8n) — Why?

---

## C) ACTION CHECKLIST

### MODULE 8: Action Checklist

- [ ] List every repetitive task you or your team does weekly — time each one and circle the top 3 time-wasters
- [ ] Sign up for Zapier (free tier) or Make.com and build Automation #1: lead notification + CRM entry (30 minutes)
- [ ] Build Automation #2: appointment booking with automated reminders — then track your no-show rate for 30 days
- [ ] Build all 5 core automations within 30 days and track total hours saved with a simple spreadsheet
- [ ] Create a rule: every time you catch yourself doing the same manual task for the third time, stop and automate it

---

## D) QUIZ

### MODULE 8 QUIZ

**1. What is the correct order of the first three steps in the Ideas-to-Income Engine?**
- A) Launch, Research, Build Offer
- B) Capture the Idea, Research, Build the Offer
- C) Build the Funnel, Create Creative, Launch
- D) Research, Capture the Idea, Scale or Kill

**Correct Answer: B**

---

**2. Which automation platform is best for simple if-then automations with the largest app library?**
- A) n8n
- B) Make.com
- C) Zapier
- D) GoHighLevel

**Correct Answer: C**

---

**3. When should you use n8n instead of Zapier or Make.com?**
- A) When you want the simplest possible setup with no learning curve
- B) When you only need one or two basic automations
- C) When you need heavy data processing, AI chains, or unlimited executions without per-task fees
- D) When you want to avoid using a server

**Correct Answer: C**

---
---

# MODULE 9: Build vs. Buy vs. Hire: How to Get AI Working in Your Business

---

## A) VIDEO LESSON SCRIPT (17 minutes)

### INTRO (2 minutes)

**[SLIDE: Module 9 Title Card — "Build vs. Buy vs. Hire: How to Get AI Working in Your Business"]**

Welcome to Module 9. This is the module that will save you the most money — not because I am teaching you a tool, but because I am teaching you how to avoid the most expensive mistake business owners make with AI.

Here is the conversation I have at least three times a week. Someone says: "CJ, I am convinced AI can help my business. I have seen the demos. But I do not know where to start. Do I hire someone? Do I buy software? Do I try to figure it out myself?"

Sound familiar?

The mistake is not picking the wrong tool. It is picking the wrong implementation path. I have seen owners spend six months trying to DIY something a professional could set up in two weeks. I have seen owners write a fifteen-thousand-dollar check to an agency that delivers a pretty dashboard and zero results. I have seen someone pay eight thousand dollars for a "custom AI chatbot" that was a white-labeled version of a forty-nine-dollar-a-month tool.

The cost of choosing wrong is not just the money. It is three to six months of lost momentum. Your competitors who chose right are already generating leads on autopilot while you are still in discovery mode.

Today I am going to give you the framework for making this decision with clarity: the three paths, the green and red flags for evaluating providers, and the Diagnostic Gatekeeper model that protects you from investing in the wrong thing.

---

### TEACH (10 minutes)

**[SLIDE: "Three Paths to AI Implementation"]**

There are three paths. Your job is to pick the one that matches your budget, timeline, and technical comfort level.

**[SLIDE: "Path 1 — DIY (Do It Yourself)"]**

**Path 1: DIY — Do It Yourself.** Best for budget-conscious owners with some technical aptitude. You are the kind of person who built your own website on Squarespace or set up your own QuickBooks.

What it looks like: you use this course and the playbook as your roadmap. You set up your own Smart Vault. You build automations yourself using Zapier, Make, and GHL. You learn by doing.

Timeline: sixty to ninety days to full implementation. Cost: two hundred to five hundred dollars a month in tools. You are paying with time instead of money.

Pros: cheapest path, under five thousand dollars for the first year. You understand every piece because you built it. No vendor dependency.

Cons: slowest path. You will spend ten to twenty hours per week in the first month on setup and learning. You will make mistakes a professional would avoid. And if something breaks at 2 AM, you are the one fixing it.

**[SLIDE: "Path 2 — DWY (Done With You)"]**

**Path 2: DWY — Done With You.** Best for owners who want to move faster but still want to understand and own their systems. You want a guide, not a crutch.

A consultant walks you through the setup. They build the architecture, you learn how it works. You own everything when it is done. No vendor lock-in.

Timeline: thirty to forty-five days. Cost: two thousand to seventy-five hundred dollars one-time.

Our DWY Pilot at Smart Vault HQ is twenty-four ninety-seven. That includes a Precision Audit of your operations, a custom AI Blueprint, hands-on setup of your first three to five automations, Smart Vault configuration, thirty days of support after launch, and training so you can manage everything yourself.

This is the sweet spot for most business owners. You get professional guidance without giving up control.

**[SLIDE: "Path 3 — DFY (Done For You)"]**

**Path 3: DFY — Done For You.** Best for owners with budget and urgency but zero desire to learn the technical details. You want results. You do not care how the engine works. You just want to drive the car.

An agency handles everything. They build your systems, run your ads, manage your automations. You get reports and results.

Timeline: fourteen to thirty days to initial launch. Cost: five thousand to twenty-five thousand dollars per month retainer.

Pros: fastest path. Zero learning curve for you. Continuous optimization.

Cons: most expensive. You are dependent on the agency. Hard to evaluate quality until you are already paying. And watch out for vendor lock-in — if they build on THEIR accounts instead of yours, you are a hostage.

DFY makes sense if your revenue is north of five hundred thousand dollars annually and your time is genuinely more valuable spent on high-level strategy.

**[SLIDE: "Green Flags — Signs of a Legitimate Provider"]**

Now, whether you go DWY or DFY, you need to know how to evaluate providers. Let me give you the green flags and red flags.

Green flags — signs of a legitimate provider:

They show ROI projections before you buy. Not vague promises — actual math. "Based on your current numbers, here is what we project."

They offer a pilot period. They are willing to prove value before you commit long-term.

They have transparent pricing. No hidden fees, no "customized pricing" that magically appears after a sales call.

They build on YOUR accounts. Your GHL, your ad accounts, your domains. If you part ways, you keep everything.

They have kill rules for ads. They know exactly when to shut down an underperforming campaign. If CTR is below point seven percent and zero leads at seventy-two hours, they kill it.

They provide case studies with real numbers. Not "we helped a business grow" — "we reduced cost per lead from forty-seven dollars to twelve dollars in sixty days for a plumbing company in Dallas."

**[SLIDE: "Red Flags — Run Away"]**

Red flags — run the other direction:

They promise overnight results. Legitimate AI implementation takes thirty to ninety days to optimize.

They have no case studies. If they cannot show evidence, they are experimenting on your dime.

Vague deliverables. "We will optimize your digital presence" means nothing.

No kill rules for ads. They will happily burn your budget while collecting their retainer.

They build on THEIR accounts. When you leave, you lose everything.

Long-term contracts with no performance clauses. A twelve-month contract is fine if it includes benchmarks and an exit clause if they miss targets.

They cannot explain what they do in plain English. If you leave the meeting more confused than when you arrived, that is smoke, not sophistication.

**[SLIDE: "The Diagnostic Gatekeeper — Always Start Here"]**

Now here is the model that protects you no matter which path you choose: the Diagnostic Gatekeeper. Never buy anything without an audit first.

Level 1 is a Strategy Session — one hundred fifty to four hundred ninety-nine dollars. A sixty to ninety-minute deep dive. Where are you spending time? Where are you losing money? You walk away with a prioritized list of opportunities.

Level 2 is a Precision Audit and AI Blueprint — twenty-five hundred to seventy-five hundred dollars. Comprehensive analysis. Tech stack audit, marketing funnel analysis, competitive intelligence, customer journey mapping. You get a detailed blueprint with specific recommendations, projected ROI, and an implementation timeline.

The key: the diagnostic fee is credited toward any core build. If you invest twenty-five hundred in a Precision Audit and then move forward with a ten-thousand-dollar implementation, you have already paid twenty-five hundred of it. The audit is not an expense. It is a deposit on clarity.

**[SLIDE: "The Waived Fee Close"]**

One more concept. The "Waived Fee" close. Here is how smart providers — including us — structure deals.

The setup fee covers the real work — five to fifteen thousand dollars for building your automation stack, configuring your Smart Vault, deploying chatbots, setting up ads, training your team.

The retainer covers ongoing optimization — twenty-two fifty a month for monitoring, weekly optimization, ad management, system maintenance.

The close: "We will waive the ten-thousand-dollar setup fee if you commit to a thirteen-month AI Command Center retainer."

Why thirteen months? Because it gives the system ninety days to optimize and ten months to compound. Most AI systems hit their stride at month three or four. By month six, the returns make the retainer feel like a rounding error.

This is not a pressure tactic. It is alignment. The provider is betting on their ability to deliver results. If they are not confident enough to waive the setup fee, that tells you something about their confidence in their own work.

---

### DEMO (3 minutes)

**[SCREEN SHARE: Sample Precision Audit Deliverable]**

Let me show you what a Precision Audit actually looks like as a deliverable, so you know what to expect — whether you work with us or someone else.

**[Screen share — open a sample audit PDF or presentation]**

This is a real Precision Audit we delivered. Names and numbers have been changed, but the format is exactly what you would get.

Page one: Executive Summary. Two paragraphs. Here is where you are. Here is where you could be. Here is the gap in dollars.

**[Screen share — scroll to tech stack analysis]**

Page two: Current Tech Stack Audit. We map every tool they are using — CRM, email platform, payment processor, social tools, ad accounts. We identify overlap, gaps, and tools they are paying for but not using. In this case, they were paying for three different email tools. Three. We consolidated to one and saved them one hundred forty dollars a month immediately.

**[Screen share — scroll to opportunity matrix]**

Pages three and four: Opportunity Matrix. This is a ranked list of automation and AI opportunities. Each one shows: what it is, estimated time saved per month, estimated revenue impact, implementation difficulty on a one to five scale, and recommended tool.

In this example, the top opportunity was lead notification automation — estimated twelve hours saved per month and fifteen thousand dollars in recovered revenue from faster response times.

**[Screen share — scroll to blueprint and timeline]**

Pages five and six: The AI Blueprint and Implementation Timeline. This is the step-by-step build plan. Week one, build this. Week two, build that. Week three, launch and test. Week four, optimize.

And at the bottom: the investment. The audit fee — in this case, twenty-four ninety-seven — is credited toward the build. So if they move forward, they have already made their first payment.

That is the Diagnostic Gatekeeper in action. You know exactly what you are getting before you commit a dollar to implementation.

---

### RECAP (2 minutes)

**[SLIDE: "Module 9 — Key Takeaways"]**

Module 9 recap. Three takeaways.

**One:** Three paths — DIY, DWY, DFY. Choose based on your budget, timeline, and technical comfort. For most business owners, DWY is the sweet spot — professional guidance without giving up control.

**Two:** Evaluate providers ruthlessly. Use the green flags and red flags checklist. Non-negotiables: transparent pricing, real case studies, kill rules for ads, and building on YOUR accounts. If any of those are missing, walk away.

**Three:** Always start with a diagnostic. The Precision Audit is not an expense — it is a deposit on clarity. The fee gets credited toward your build. You never invest in the wrong thing because you have the blueprint before you write the big check.

**Action items:** Honestly assess which path fits your situation right now. If you are leaning DWY or DFY, shortlist three providers and run them through the green flags checklist. And before you buy anything from anyone — get a diagnostic first.

Next up, Module 10 — the capstone. We are building your Smart Vault live. Everything from the last nine modules comes together. See you there.

---

## B) PDF WORKSHEET

### MODULE 9 WORKSHEET: Build vs. Buy vs. Hire

**Key Concepts:**
- Three implementation paths: DIY ($200-500/mo, 60-90 days), DWY ($2,000-7,500 one-time, 30-45 days), DFY ($5K-25K/mo, 14-30 days)
- Choose based on three factors: budget, timeline, and technical comfort level
- Green flags: ROI projections, pilot periods, transparent pricing, builds on YOUR accounts, kill rules for ads, real case studies
- Red flags: overnight promises, no case studies, vague deliverables, builds on THEIR accounts, no kill rules, jargon-heavy pitches
- Diagnostic Gatekeeper: always audit before you buy — fee is credited toward the build
- Waived Fee Close: setup fee waived in exchange for 13-month retainer commitment

**Fill-in-the-Blank Exercises:**

1. The three implementation paths are _______ (cheapest, slowest), _______ (sweet spot for most owners), and _______ (fastest, most expensive).

2. A legitimate provider will always build on _______ accounts, not _______ accounts.

3. The Diagnostic Gatekeeper fee is _______ toward any core build, making it a deposit on _______, not an expense.

4. The "Waived Fee" close uses a _______-month retainer because AI systems hit their stride at month _______.

5. If a provider has no _______ for ads, they will burn your budget while collecting their retainer.

**Apply to YOUR Business:**

1. Score your readiness for each path:

   | Factor | Your Score (1-10) |
   |--------|------------------|
   | Budget available for AI implementation | |
   | Time available to learn and build | |
   | Technical comfort level | |
   | Urgency (how fast do you need results?) | |

   Based on your scores, which path fits best? _______________

2. Use the Green/Red Flag checklist to evaluate a provider you are considering (or have used in the past):

   | Green Flag | Present? (Y/N) |
   |------------|----------------|
   | Shows ROI projections with real math | |
   | Offers a pilot period | |
   | Transparent pricing | |
   | Builds on YOUR accounts | |
   | Has kill rules for ads | |
   | Case studies with real numbers | |

   | Red Flag | Present? (Y/N) |
   |----------|----------------|
   | Promises overnight results | |
   | No case studies | |
   | Vague deliverables | |
   | Builds on THEIR accounts | |
   | Long contract, no performance clause | |
   | Cannot explain in plain English | |

3. What would you want a Precision Audit to examine in YOUR business? List your top 3 areas of concern:

---

## C) ACTION CHECKLIST

### MODULE 9: Action Checklist

- [ ] Honestly assess your budget, timeline, and technical comfort level — determine which path (DIY, DWY, or DFY) fits your situation right now
- [ ] If leaning DWY or DFY, make a shortlist of 3 providers and run each through the green flags / red flags checklist
- [ ] Before buying anything, get a diagnostic — even a $150 strategy session saves thousands by ensuring you invest in the right things first
- [ ] Verify that any provider you hire will build on YOUR accounts (CRM, ad accounts, domains, knowledge base) — never be a hostage
- [ ] If going DIY, commit to following the playbook chapters in order, one per week — in 10 weeks, all 10 systems will be live

---

## D) QUIZ

### MODULE 9 QUIZ

**1. Which implementation path is described as the "sweet spot for most business owners"?**
- A) DIY (Do It Yourself)
- B) DWY (Done With You)
- C) DFY (Done For You)
- D) Hiring a full-time CTO

**Correct Answer: B**

---

**2. Which of the following is a RED flag when evaluating an AI service provider?**
- A) They offer a 30-60 day pilot period
- B) They show ROI projections with real math before you buy
- C) They build your systems on THEIR accounts, not yours
- D) They have kill rules for underperforming ad campaigns

**Correct Answer: C**

---

**3. What is the Diagnostic Gatekeeper model?**
- A) A firewall tool that protects your business data from AI providers
- B) An audit-first approach where the diagnostic fee is credited toward any core build, ensuring you never invest without a blueprint
- C) A 13-month retainer that includes unlimited AI services
- D) A chatbot that screens service providers automatically

**Correct Answer: B**

---
---

# MODULE 10: The Smart Vault Method: Build Your AI Business Brain in 20 Minutes

---

## A) VIDEO LESSON SCRIPT (20 minutes)

### INTRO (2 minutes)

**[SLIDE: Module 10 Title Card — "The Smart Vault Method: Build Your AI Business Brain in 20 Minutes"]**

Welcome to Module 10. The capstone. This is where everything from the last nine modules comes together.

Here is the truth that every chapter in the playbook has pointed you toward, and I am going to say it directly: the businesses that win with AI are not the ones with the best tools. They are the ones with the best information.

Think about it. The same ChatGPT, the same Claude, the same ad platforms are available to your competitor down the street. The tools are commodities. What is not a commodity is YOUR data — your customer insights, your pricing logic, your competitive advantages, your years of hard-won knowledge about what works in your market.

The problem? That knowledge lives in your head. Or scattered across emails, Google Docs, old proposals, sticky notes, and the brains of employees who might leave tomorrow.

The Smart Vault fixes this. In the next twenty minutes, you are going to build an AI business brain that stores everything your company knows, answers questions from YOUR data instead of the internet's generic noise, and makes every AI tool you use dramatically smarter.

This is not theoretical. I have used this exact method to analyze four hundred forty competitor websites in twelve minutes and generate twelve full ad campaigns in four hours. Work that would take a human team three to four weeks.

Let us build it.

---

### TEACH (12 minutes)

**[SLIDE: "Why Generic AI Falls Short"]**

Let me set the stage for why this matters.

You want to launch a new ad campaign. You Google "best Facebook ad strategies for your industry." You get fifty articles written by people who have never worked in your industry, stuffed with generic advice like "know your audience."

Or you ask ChatGPT for help. It gives you a competent but generic answer based on the entire internet's training data. The advice is not wrong exactly. It is just not right for YOU.

Now imagine this instead. You open your Smart Vault and ask: "Based on our last six months of ad performance, our customer demographics, and our competitor analysis, what should our next campaign focus on?"

And it answers specifically, from YOUR data: "Your highest-performing audience segment is homeowners aged forty-five to sixty in zip codes with household incomes above one hundred fifty thousand. Your best ad angle was the time-savings message at a two point three percent click-through rate versus point nine for cost savings. Your competitor just launched a spring promotion. I recommend a campaign targeting the same demographic with a time-savings angle, differentiated by your twenty-four-seven AI support capability, which they do not offer."

That is not generic internet advice. That is a strategic recommendation backed by your accumulated intelligence. That is the Smart Vault difference.

**[SLIDE: "What Is the Smart Vault?"]**

The Smart Vault is built on Google's NotebookLM — a free tool that lets you upload documents and query them conversationally. Think of it as ChatGPT, but it only knows what you tell it.

Why NotebookLM and not just ChatGPT or Claude? Because general-purpose AI models answer from the entire internet. That is powerful for general questions, but it is a liability for business decisions. NotebookLM answers ONLY from the documents you upload. No hallucinations from random training data. No generic advice. Just your information, organized and queryable.

**[SLIDE: "The Diamond Standard AI Growth Model — 5 Phases"]**

Now, the Smart Vault is the container. The Diamond Standard is the framework for what goes into it and how you turn that intelligence into revenue. Five phases, each building on the last.

**Phase 1: Articulate Your Business Foundation.**

Before AI can help you grow, it needs to understand what you are growing. Document these clearly: your mission — what problem do you solve, for whom. Your audience — demographics, psychographics, pain points, desires. Your revenue model — how you make money, average deal size, customer lifetime value. Your differentiator — why someone should choose you over the ten other businesses that do what you do.

Upload all of this to your Smart Vault. This becomes the lens through which every recommendation is filtered.

**[SLIDE: "Phase 2 — Deep Research (Shadow Work)"]**

**Phase 2: Deep Research — what I call Shadow Work.**

Take your business foundation and feed it to multiple AI models. But do not ask for validation. Ask them to challenge you.

Use this prompt: "Here is my business plan. Act as a skeptical business consultant. What are the three biggest weaknesses in my strategy? What assumptions am I making that might be wrong? What opportunities am I missing?"

Run this through Claude, ChatGPT, Perplexity, Gemini, and Grok. This is the "Multitude of Counselors" principle. No single AI has perfect judgment. But when four out of five flag the same weakness, pay attention.

Upload every insight back into your Vault. Your business brain just got smarter.

**[SLIDE: "Phase 3 — External Data Collection"]**

**Phase 3: External Data Collection.**

Now you go wide. Collect intelligence from outside your business.

AnswerThePublic — what questions is your market asking? Export the full dataset.

Meta Ad Library — what ads are your competitors running? Note the angles, offers, creative formats.

Google Trends — is demand growing or shrinking? In which regions?

Perplexity Deep Research — I had Perplexity scrape and summarize four hundred forty websites in twelve minutes. Intelligence that would take a human researcher two weeks.

Review mining — read your competitors' one-star and five-star reviews. Their one-star reviews reveal what their customers hate — that is your opportunity. Their five-star reviews reveal what they do well — that is your benchmark.

Upload everything to the Vault.

**[SLIDE: "Phase 4 — Populate and Organize"]**

**Phase 4: Populate and Organize.**

By now, your Vault contains your business plan, customer data, competitor intelligence, market research, ad performance history, and AI-generated strategic recommendations.

Organize it into clear categories. You might even create separate notebooks: Core Business Intelligence, Customer Intelligence, Competitive Intelligence, Marketing Intelligence, Product Intelligence.

**[SLIDE: "Phase 5 — Generate Targeting Parameters"]**

**Phase 5: Generate Targeting Parameters.** This is where the Smart Vault starts printing money.

Ask your Vault: "Based on all our customer data and market research, define our top three audience segments with specific demographics, interests, and behaviors for Facebook ad targeting."

"Generate five ad campaign concepts for our upcoming promotion, each targeting a different audience segment, using messaging angles that have performed best historically."

"What content topics should we focus on this month based on what our audience is searching for and what our competitors are ignoring?"

The Vault generates targeting parameters, campaign concepts, and content strategies grounded in YOUR data. Not guesswork. Your accumulated intelligence, organized and activated.

**[SLIDE: "How the Vault Connects to Every Module"]**

Now here is the capstone insight. Once your Vault is built, it becomes the engine behind every system in this course:

Modules 1 and 2, Research and Strategy — query the Vault instead of starting from scratch.

Modules 3 and 4, Ads and Teams — generate ad copy and creative briefs from your Vault's competitive intelligence.

Modules 5 and 6, Lead Gen and ROI — use Vault data to project ROI and build targeting parameters.

Module 7, Chatbots — your bots answer from the same knowledge base. One source of truth.

Module 8, Automations — your automation priorities are informed by Vault insights on what to fix first.

Module 9, Build, Buy, or Hire — your audit data lives in the Vault. Any new provider gets up to speed instantly.

Everything connects. Everything compounds. The more you feed your Vault, the smarter every system becomes.

---

### DEMO (5 minutes)

**[SCREEN SHARE: NotebookLM]**

Alright. Let us build a Smart Vault right now, live. I am going to walk you through the full setup — create the notebook, upload sources, and run queries. This is the twenty-minute setup I keep talking about.

**[Screen share — open notebooklm.google.com]**

Step 1: Go to notebooklm.google.com. Click "New Notebook." I am naming it "Smart Vault Demo — [Business Name]."

Done. That took ten seconds. You now have the container.

**[Screen share — uploading documents]**

Step 2: Upload your sources. I click "Add Source." I have got five documents ready to go.

First, a two-page business summary — mission, services, pricing, target market. Uploading now.

Second, our FAQ document — forty-two questions and answers. This is the same document from Module 7 that powers our chatbots. Double duty.

Third, product and service descriptions with pricing tiers. Detailed features and benefits.

Fourth, competitor research — I ran a Perplexity deep dive on our top five competitors last week. That export goes in here.

Fifth, our last ninety days of ad performance data — exported from Meta as a CSV.

**[Screen share — all five sources uploaded]**

All five sources are uploaded. The green check marks show NotebookLM has processed them. Total time: about three minutes, depending on file size.

**[Screen share — running queries]**

Step 3: Now I query it. Watch this. This is the moment that makes jaws drop.

I type: "What are the top five objections our customers raise, and how should we handle each one?"

**[Screen share — showing the response]**

Look at this response. It is pulling directly from our FAQ document and our sales process notes. It is not giving me generic objection-handling advice. It is telling me OUR specific objections — pricing concerns from our actual customer base, timeline questions about our actual services — and recommending responses based on how WE have handled them successfully.

Let me try another one. "Based on our ad performance data and competitor research, what should our next campaign focus on?"

**[Screen share — showing the response]**

There it is. It analyzed our Meta ad data, identified that our top-performing angle was the time-savings message, cross-referenced it with our competitor analysis showing that none of our competitors are emphasizing AI-powered support, and recommended a specific campaign angle targeting homeowners in our highest-performing zip codes.

That recommendation would have taken a marketing consultant hours to develop. It took the Vault about eight seconds.

One more. "Write a Facebook ad targeting small business owners who need our services, using the messaging angles that have worked best in our past campaigns."

**[Screen share — showing the generated ad copy]**

And there is a full ad — headline, body copy, call to action — all grounded in our actual performance data and our actual competitive advantages. Not generic "grow your business" copy. Specific, data-backed creative.

**[Screen share — showing how this connects to ad campaigns]**

Now I take this output and plug it into Module 4 — ad creation. Or I feed it to my chatbot configuration from Module 7. Or I use the targeting parameters for my lead gen funnels from Module 5. Everything connects back to the Vault.

Total setup time: about twelve minutes for this demo. With your full document library, budget twenty minutes.

---

### RECAP (2 minutes)

**[SLIDE: "Module 10 — Key Takeaways"]**

Alright. Module 10, the capstone. Let me give you the three takeaways and then we are going to wrap the whole course.

**One:** The Smart Vault is your personalized NotebookLM knowledge base. It stores everything your business knows and makes every AI tool you use smarter — because it answers from YOUR data, not the internet's generic noise. Build it in twenty minutes. Feed it continuously. It compounds.

**Two:** The Diamond Standard AI Growth Model is your five-phase framework: Articulate your foundation, Research with multiple AI counselors, Collect external data, Populate and organize your Vault, and Generate targeting parameters and campaign strategies. Every phase builds on the last.

**Three:** The Vault is not a standalone tool. It is the engine behind every system in this course. Your chatbots answer from it. Your ad campaigns are generated from it. Your automations are prioritized by it. Your providers get up to speed from it. One source of truth powering everything.

**[SLIDE: "Your Next Steps"]**

Here is what I want you to do.

Right now, today, in the next twenty minutes: open NotebookLM, create your Smart Vault, upload your business plan, FAQs, and product descriptions. Ask it one question. Watch it answer from YOUR data.

This week: run the Shadow Work exercise. Feed your business plan to Claude, ChatGPT, and Perplexity. Ask each to challenge your assumptions.

This month: complete all five phases of the Diamond Standard. By the end, your Vault has enough intelligence to generate ad campaigns, content strategies, and targeting parameters on demand.

And here are your next-level options.

If you want hands-on help implementing all ten systems, book your free fifteen-minute AI Audit at SmartVaultHQ.com/audit. We will tell you exactly where AI can save you the most time and money in the next ninety days.

If you want a community of business owners doing this together, join the Smart Vault community. Link is in the resources section below this video.

If you are ready for someone to build it all for you, ask about our DWY Pilot or our DFY retainer. The Precision Audit fee gets credited toward any build.

**[SLIDE: "Final Slide — Smart Vault HQ Logo + CTAs"]**

You now have the complete playbook. Ten systems. All the tools. All the frameworks. The question is not whether AI works. The question is whether you are going to build the system or keep doing everything by hand.

Start your Smart Vault today. It takes twenty minutes. And those twenty minutes will change how you run your business forever.

I am CJ from Smart Vault HQ. Thank you for going through this course with me. Now go build something.

---

## B) PDF WORKSHEET

### MODULE 10 WORKSHEET: The Smart Vault Method

**Key Concepts:**
- The Smart Vault is a personalized NotebookLM knowledge base that answers from YOUR data only — no hallucinations, no generic advice
- Diamond Standard AI Growth Model (5 phases): Articulate, Research, Collect, Populate, Generate
- "Multitude of Counselors" principle: run your business plan through Claude, ChatGPT, Perplexity, Gemini, and Grok for diverse perspectives
- The Vault powers every system: chatbots (Module 7), ads (Modules 3-4), lead gen (Module 5), automations (Module 8), provider onboarding (Module 9)
- Real results: 440 sites analyzed in 12 minutes, 12 campaigns generated in 4 hours
- 20-minute setup: create notebook, upload docs, start querying

**Fill-in-the-Blank Exercises:**

1. The five phases of the Diamond Standard AI Growth Model are: _______, _______, _______, _______, and _______.

2. NotebookLM answers ONLY from the _______ you upload, unlike general-purpose AI that answers from _______.

3. The "Multitude of Counselors" principle means running your business plan through _______ AI models to get diverse perspectives.

4. Phase 2 is called "_______ _______" because you are pressure-testing your assumptions, not seeking validation.

5. In Phase 5, you ask your Vault to generate _______ _______, campaign concepts, and content strategies grounded in your actual data.

**Apply to YOUR Business:**

1. Build your Smart Vault upload checklist. What documents and data do you have (or need to create) for each category?

   | Category | Documents You Have | Documents You Need to Create |
   |----------|-------------------|------------------------------|
   | Business plan / one-pager | | |
   | Customer FAQs | | |
   | Product/service descriptions | | |
   | Competitor research | | |
   | Ad performance data | | |
   | Customer reviews/feedback | | |
   | Sales process docs | | |
   | Industry research | | |

2. Write 5 queries you would ask your Smart Vault once it is loaded:
   1. _______________________________________________
   2. _______________________________________________
   3. _______________________________________________
   4. _______________________________________________
   5. _______________________________________________

3. How does your Smart Vault connect to the other systems you have built in this course? List one specific use for each:
   - Chatbots (Module 7): _______________________________________________
   - Automations (Module 8): _______________________________________________
   - Ad campaigns (Modules 3-4): _______________________________________________

---

## C) ACTION CHECKLIST

### MODULE 10: Action Checklist

- [ ] Open NotebookLM, create your Smart Vault notebook, and upload your business plan, FAQs, and product descriptions — ask it one question and confirm it answers from YOUR data (20 minutes)
- [ ] Run the "Shadow Work" exercise: feed your business plan to Claude, ChatGPT, and Perplexity — ask each to challenge your assumptions — upload all insights back into the Vault
- [ ] Use Perplexity to research your top 5 competitors, then upload findings and ask the Vault: "What do we do better, and where are we vulnerable?"
- [ ] Complete all 5 phases of the Diamond Standard within 30 days — your Vault should be generating ad campaigns, targeting parameters, and content strategies on demand
- [ ] Book your free 15-minute AI Audit at SmartVaultHQ.com/audit OR commit to feeding the Vault with every new piece of business data (ad results, customer feedback, sales notes) on an ongoing basis

---

## D) QUIZ

### MODULE 10 QUIZ

**1. What are the five phases of the Diamond Standard AI Growth Model, in order?**
- A) Research, Collect, Articulate, Generate, Populate
- B) Articulate, Research, Collect, Populate, Generate
- C) Generate, Populate, Collect, Research, Articulate
- D) Collect, Articulate, Research, Generate, Populate

**Correct Answer: B**

---

**2. What should you upload to your Smart Vault as priority documents?**
- A) Only your business plan
- B) Random internet articles about your industry
- C) Business plan, customer FAQs, product descriptions, competitor research, ad performance data, and customer feedback
- D) Your competitors' internal documents

**Correct Answer: C**

---

**3. Why does the Smart Vault use NotebookLM instead of general-purpose AI like ChatGPT?**
- A) NotebookLM is faster than ChatGPT
- B) NotebookLM is more expensive and therefore better quality
- C) NotebookLM answers ONLY from your uploaded documents, avoiding generic advice and hallucinations from internet training data
- D) NotebookLM can run automations that ChatGPT cannot

**Correct Answer: C**

---
---

# COURSE MODULES 7-10: COMPLETE

**Total Materials Delivered:**
- 4 full video lesson scripts (15-20 minutes each, production-ready with slide/screen share cues)
- 4 PDF worksheets with key concepts, fill-in-the-blank exercises, and business application prompts
- 4 action checklists with 5 specific items each (20 total action items)
- 4 quizzes with 3 multiple-choice questions each (12 total quiz questions)

**Production Notes:**
- All slide cues are marked with **[SLIDE:]** tags
- All screen share segments are marked with **[SCREEN SHARE:]** tags
- Demo sections include step-by-step narration for screen recording
- Module 10 includes course-closing CTAs (audit booking, community, retainer)
