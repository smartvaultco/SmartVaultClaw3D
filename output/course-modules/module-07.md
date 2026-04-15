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

**Correct Answer: B** -- The three deployment zones are website chat (your digital front door), social DMs (Instagram, Facebook, WhatsApp), and voice/voicemail agents. Each zone plugs a different leak in your customer experience.

---

**2. What is the SLA target for responding to social media DMs?**
- A) 30 minutes
- B) 1 hour
- C) 4 hours
- D) 24 hours

**Correct Answer: C** -- Your SLA target for social DM responses is four hours. The bot handles most inquiries instantly, but the four-hour window is your backstop for anything requiring human follow-up.

---

**3. In the escalation protocol, what should happen when the same question triggers a Tier 2 escalation three or more times?**
- A) Block the customer from chatting
- B) Remove the chat widget from that page
- C) Add the answer to your knowledge base so the bot handles it next time
- D) Hire another support rep to handle the volume

**Correct Answer: C** -- Every repeated escalation reveals a gap in your knowledge base. Adding the answer means the bot handles it automatically next time, continuously shrinking your Tier 2 workload.

---

## ANSWER KEY

**Fill-in-the-Blank Answers:**
1. 5 (five)
2. Website chat widget; Social DMs; Voice/voicemail
3. bot; human
4. 4 (four)
5. 3 (three); knowledge base
