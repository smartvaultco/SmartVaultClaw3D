# MODULE 3: "Your First AI Employee: Automating Customer Service in 30 Minutes"

---

## A) VIDEO LESSON SCRIPT (Estimated Runtime: 19 minutes)

---

### INTRO (2 minutes)

**[SLIDE: Title card -- "Module 3: Your First AI Employee"]**

Alright, Module 3. This is the one where we stop talking frameworks and start building something you can deploy today.

Here's what I want you to do right now. Go look at your inbox. Your text messages. Your DMs. Whatever channel your customers use to reach you. Count how many of the last 20 messages are questions you've already answered a hundred times.

"What are your hours?" "Do you offer financing?" "How much does this cost?" "Can I reschedule?" "Do you serve my area?"

I'll bet at least half -- probably 60-70% -- are repeat questions with repeat answers. And every single one requires someone to stop what they're doing, read it, type a response, and get back to work. Or worse, it sits unanswered for 4, 8, 24 hours while the customer moves on to your competitor.

Here's the stat that should wake you up: Harvard Business Review found that companies responding within 5 minutes are 21 times more likely to qualify a lead than companies responding after 30 minutes. Not 21 percent. Twenty-one times. And InsideSales.com found that 78% of customers buy from the first company that responds. Not the best. Not the cheapest. The first.

So what happens at your business after 5 PM when someone hits your website at 7 PM? Nothing. For 14 hours. By morning, they've already booked with someone else.

That's why your first AI employee should be a customer service bot. Not because it's sexy. Because it's the fastest win with the lowest risk and the most immediate payoff. You're going to build it in this module. And it's going to start working tonight.

---

### TEACH (10 minutes)

**[SLIDE: "Chatbot Ops -- The 3-Tier System"]**

We're going to use a three-tier system I call Chatbot Ops. You don't need to build all three tiers today. Start at Tier 1. Get it running. Upgrade as you go.

**[SLIDE: Tier 1 -- The FAQ Bot]**

**Tier 1 is the FAQ Bot.** This is the simplest and most effective starting point. It does one thing: answers the questions your team answers every single day. No AI magic required. Just a decision tree with pre-written responses.

What it handles: business hours, location, service descriptions, pricing ranges, common policies, basic eligibility questions, links to resources.

What it does NOT handle: anything requiring judgment -- complaints, disputes, custom quotes, sensitive personal information.

Where it lives: your website chat widget, your Google Business Profile, Facebook Messenger, Instagram DMs.

This alone eliminates 50-70% of repetitive inbound messages. Your team stops being a human FAQ page and starts focusing on work that actually requires a human brain.

**[SLIDE: Tier 2 -- The Lead Qualifier]**

**Tier 2 is the Lead Qualifier.** It does everything the FAQ bot does, plus it asks strategic questions to determine if this person is a real prospect.

The flow goes like this. First, a greeting with button options for your top services. Then a needs assessment -- 2-3 qualifying questions. Timeline: this week, this month, just exploring? Budget range? Location if that matters?

Then the routing decision. Based on their answers, the bot takes one of three paths:

Hot lead -- high intent, good fit? "Let me get you scheduled." Send them a booking link immediately.

Warm lead -- interested but not ready? "Let me send you some info." Drop them into a nurture sequence.

Not a fit -- outside your area, budget too low? "Thanks for your interest, here's a resource." Polite redirect. No wasted sales calls.

The result: your sales team only talks to pre-qualified leads. No more 20-minute calls that end with "Oh, I was looking for something at a tenth of your price."

**[SLIDE: Tier 3 -- The Appointment Booker]**

**Tier 3 is the Appointment Booker.** This combines FAQ handling, lead qualification, AND calendar integration. It qualifies leads AND books them directly into your calendar, sends confirmations via email and SMS, sends reminders 24 hours and 1 hour before, and if they no-show, triggers a follow-up with a rebooking link.

This replaces a receptionist at $35,000-$45,000 a year, an appointment scheduling tool, manual follow-up calls, and no-show management. And it does it at 2 AM on a Sunday.

**[SLIDE: "The Human-on-the-Loop Principle"]**

Now, critical point before we build. There are things a bot should NEVER handle without a human.

Complaints and disputes -- someone who's upset needs empathy, not a decision tree. The bot captures the issue and routes it to a human with full context. But a human closes that loop.

Refunds and financial decisions -- the bot can explain your refund policy, but a human processes exceptions.

High-value sales conversations -- if someone's about to spend $5,000+, they deserve a human. The bot's job is to qualify them and deliver them to that conversation, not to close the deal.

The principle is "human-on-the-loop," not "human-out-of-the-loop." The bot handles volume. The human handles judgment. Together, they're better than either one alone.

**[SLIDE: "Building Your Tier 1 FAQ Bot -- 30 Minutes"]**

Alright, let's build. Here's the exact process, and I'm timing it at 30 minutes.

**Step 1: List your top 10 questions. Five minutes.** Open your inbox, texts, DMs. Write down the 10 questions you answer most. Don't overthink it. For most businesses, this list writes itself. What services do you offer? What are your prices? Hours? Location? How do I schedule? Cancellation policy? Payment methods? How long does it take?

**Step 2: Write clear answers. Ten minutes.** For each question, write a concise, friendly answer. Under 3 sentences each. Include a next step or link when relevant. And write them in your brand voice -- not robot voice. "We're open Monday through Friday, 9 to 5" is fine. "We are pleased to inform you that our establishment maintains operational hours" is not.

**Step 3: Choose your platform. Two minutes.** If you're on GoHighLevel, use GHL's built-in chat widget -- it's already connected to your CRM and calendar. If you're not on GHL, use Zapier's chatbot feature or Make.com with a Typebot integration. If you want full control, build it in n8n with webhook triggers.

**Step 4: Build the flow. Ten minutes.** Create a welcome message with buttons for your main categories -- Services, Pricing, Scheduling, Hours, Other. Map each button to your pre-written response. And here's the critical part: add an escape hatch. At every stage, give people a way to reach a human. Nothing frustrates customers more than being trapped in a bot loop with no way out. When someone clicks "Talk to a person," collect their contact info, notify your team immediately, and set an expectation for response time.

**Step 5: Deploy and test. Three minutes.** Embed the widget, enable it on your social channels, send yourself a test message through every path, fix any dead ends, and go live.

That's it. Your first AI employee is on the clock.

---

### DEMO (5 minutes)

**[SCREEN SHARE: GHL Chat Widget Builder]**

**[Recording note: Open GoHighLevel's Conversation AI or chat widget builder. Have a pre-started bot ready to demonstrate.]**

Let me walk you through this in GHL so you can see exactly what it looks like.

**[Recording note: Show the welcome message configuration -- the greeting text and the button options for Services, Pricing, Scheduling, Hours/Location, Talk to Someone.]**

Here's my welcome message. "Hi! Thanks for reaching out to [Business Name]. I can help with most questions right away. What would you like to know about?" Then I've got five buttons. Let me click through one path.

**[Recording note: Click "Pricing" and show how the response is configured. Show the pre-written pricing answer appearing.]**

When someone clicks Pricing, they get this response. Notice it's conversational, gives a range, and ends with a next step -- "Want me to help figure out which option fits best?"

**[Recording note: Show the "Talk to Someone" path -- the contact info collection and team notification setup.]**

Now here's the escape hatch. "Talk to our team" collects name, email, phone. Then it triggers an instant notification to my team and tells the customer, "Someone will reach out within one business hour."

**[Recording note: Show the Tier 2 lead qualifier flow -- the qualifying questions and the branching paths for hot, warm, and not-a-fit leads.]**

And here's Tier 2 in action. After the initial greeting, I ask timeline and budget. If they say "this week" and their budget is in our range -- hot lead path -- they get sent straight to the calendar. If they say "just exploring" -- nurture path -- I capture their email and drop them into a drip sequence. If they're outside our service area, I give them a helpful resource and wish them well.

**[Recording note: Open the live preview of the chat widget and click through the full flow as a customer would experience it.]**

Let me preview the full experience. I land on the website, the widget pops up... I click "Learn about our service"... I answer the qualifying questions... and I'm looking at available calendar slots. That entire journey took about 45 seconds. No phone call. No email wait. No human required until the actual appointment.

**[Recording note: Show the bot conversation log in GHL -- how you can review interactions weekly.]**

And here's where you monitor. Every conversation is logged. Every Friday, spend 15 minutes reviewing: What questions came up that the bot couldn't answer? Where did people drop off? What's your bot-to-booking conversion rate? You improve it every week with real data.

---

### RECAP (2 minutes)

**[SLIDE: "3 Key Takeaways"]**

Module 3 takeaways.

**Number one: Speed of response beats everything.** 78% of customers buy from the first company that responds. A chatbot responds in under 3 seconds, 24/7/365. If you're not available after hours, you're losing $78,000+ a year in missed leads based on conservative math.

**Number two: Use the three-tier system and start at Tier 1.** The FAQ Bot handles 50-70% of repetitive messages and takes 30 minutes to build. Don't try to build a complex AI assistant on day one. Get Tier 1 running today, add Tier 2 lead qualification next week, scale to Tier 3 appointment booking when you're ready.

**Number three: Automate the predictable, humanize the emotional.** Your bot handles volume -- hours, pricing, scheduling, qualification. Humans handle judgment -- complaints, disputes, high-value sales, anything requiring empathy. That's human-on-the-loop, and it's how you get the best of both.

Your worksheet includes a plug-and-play chatbot script template. Customize it, build it, and deploy it today. You should have your first AI employee working by tonight.

In the next module, we're going to tackle content creation at scale -- how to produce a month's worth of social media, email, and ad content in a single afternoon using AI. See you there.

---

## B) PDF WORKSHEET -- Module 3

---

### MODULE 3 WORKSHEET: Build Your First AI Employee

**Key Concepts:**

- Companies responding within 5 minutes are 21x more likely to qualify a lead; 78% of customers buy from the first responder
- Chatbot Ops uses a 3-tier system: Tier 1 (FAQ Bot), Tier 2 (Lead Qualifier), Tier 3 (Appointment Booker)
- The FAQ Bot eliminates 50-70% of repetitive inbound messages and takes 30 minutes to deploy
- The Lead Qualifier routes prospects into three paths: Hot Lead (book immediately), Warm Lead (nurture sequence), Not a Fit (polite redirect)
- Human-on-the-Loop principle: automate the predictable, humanize the emotional -- bots handle volume, humans handle judgment

---

**Fill in the Blanks:**

1. Companies responding to leads within ______ minutes are 21 times more likely to qualify that lead. ______% of customers buy from the first company that responds.

2. The three tiers of Chatbot Ops are: Tier 1 (____________), Tier 2 (____________), and Tier 3 (____________).

3. The FAQ Bot eliminates ______-______% of repetitive inbound messages by answering the questions your team answers every day.

4. The Lead Qualifier routes prospects into three paths: ______________ leads get sent to the booking calendar, ______________ leads enter a nurture sequence, and ______________ leads get a polite redirect.

5. The Human-on-the-Loop principle says: automate the ______________, humanize the ______________. Bots should never handle complaints, refunds, or high-value sales conversations without human oversight.

---

**Apply to YOUR Business:**

1. **Write YOUR Bot's Top 10 FAQ Answers.** List your 10 most frequently asked questions and write concise, friendly answers for each.

| # | Question | Your Answer (under 3 sentences) |
|---|----------|-------------------------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |
| 7 | | |
| 8 | | |
| 9 | | |
| 10 | | |

2. **Design Your Lead Qualifier Flow.** Fill in the blanks for YOUR business:

**Welcome message:** "Hi! Thanks for reaching out to ______________. I can help you get started. What are you looking for today?"

**Button options:**
- Learn about ______________
- Learn about ______________
- Get pricing info
- Book an appointment
- Talk to our team

**Qualifying questions:**
- Timeline question: "What's your timeline? ______________ / ______________ / Just exploring"
- Budget question: "What's your budget range? Under $______ / $______-$______ / $______+ / Not sure yet"

**Hot lead criteria (book immediately):** Timeline = ______________ AND Budget = ______________

3. **Identify Your Human-Only Scenarios.** List 3-5 situations that should ALWAYS be routed to a human at your business:

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## C) ACTION CHECKLIST -- Module 3

---

- [ ] **List your top 10 most-asked customer questions** by reviewing your inbox, texts, and DMs from the past 30 days.
- [ ] **Write concise, brand-voice answers** for each question (under 3 sentences each, with a next step or link).
- [ ] **Build and deploy your Tier 1 FAQ Bot today** using GHL, Zapier, or your chosen platform. Set a 30-minute timer and get it live.
- [ ] **Test every path** by sending yourself messages through the bot. Fix any dead ends, missing answers, or broken links.
- [ ] **Schedule a 15-minute weekly review** (every Friday) to check bot conversations, add new questions, fix drop-off points, and track your bot-to-booking conversion rate.

---

## D) QUIZ -- Module 3

---

**Question 1:** What does the Tier 2 Lead Qualifier do that the Tier 1 FAQ Bot does NOT?

A) Answer frequently asked questions
B) Operate 24/7 on your website
C) Ask strategic qualifying questions and route leads based on fit, intent, and budget
D) Connect to your CRM

**Correct Answer: C)** -- The Tier 1 FAQ Bot answers pre-set questions. The Tier 2 Lead Qualifier adds strategic questioning (timeline, budget, needs) and routes prospects into hot, warm, or not-a-fit paths based on their answers.

---

**Question 2:** According to the Human-on-the-Loop principle, which of these should a chatbot NEVER handle without human oversight?

A) Business hours and location questions
B) Customer complaints and disputes
C) Service descriptions and pricing ranges
D) Appointment scheduling and reminders

**Correct Answer: B) Customer complaints and disputes** -- Someone who's upset needs empathy and judgment, not a decision tree. The bot can capture the complaint and route it to a human with full context, but a human must close that loop.

---

**Question 3:** A potential customer messages your business at 8 PM on a Tuesday. You don't have a chatbot. Based on the data in this module, what is the most likely outcome?

A) They'll wait patiently until morning for your team to respond
B) They'll leave a voicemail and call back tomorrow
C) They'll contact a competitor who responds immediately, and 78% of the time, buy from that competitor instead
D) They'll bookmark your website and return next week

**Correct Answer: C)** -- Research shows 78% of customers buy from the first company that responds. A 14-hour response gap means your competitors with chatbots or after-hours response systems capture those leads first.

---

## ANSWER KEY

**Fill-in-the-Blank Answers:**
1. 5; 78
2. FAQ Bot; Lead Qualifier; Appointment Booker
3. 50; 70
4. Hot; Warm; Not-a-fit
5. predictable; emotional
