# GHL Workflow AI Prompt — 14-Day AI Trial Onboarding
# Paste this into GHL Workflow AI after a prospect says YES

---

Create a workflow called "AI Trial Onboarding - 14 Day" with these exact specs:

TRIGGER: Contact Tag Added = "ai-trial-started"

Action 1: Send Email immediately. Subject: "Your AI assistant is live!" Body: "Hey {{contact.first_name}}, Great news — your AI assistant for {{contact.company_name}} is now live and ready to go! Here's what it's doing for you right now: - Answering your DMs and website chats 24/7 - Qualifying leads and booking appointments on your calendar - Following up with cold leads automatically You don't need to do anything. Just let it run and watch the leads come in. I'll check in with you in a few days to see how it's going. — CJ, Smart Vault Co."

Action 2: Wait 3 days.

Action 3: Send SMS. Message: "Hey {{contact.first_name}}! Quick check-in — your AI assistant has been live for 3 days. How's it going? Any leads or bookings come through? Let me know if you want me to tweak anything. — CJ"

Action 4: Wait until contact replies OR 2 days pass.

Action 5: If/Else. Condition: contact replied.
YES branch: Add tag "trial-engaged", send internal notification "Trial user {{contact.first_name}} replied to day 3 check-in", end workflow.
NO branch: Continue.

Action 6: Wait 4 more days (now day 10 of trial).

Action 7: Send Email. Subject: "Your trial results so far". Body: "Hey {{contact.first_name}}, Your 14-day trial is about 70% done. Here's what I've noticed — your AI assistant has been handling inquiries around the clock, and most businesses at this point have seen a significant uptick in booked appointments and response times. I wanted to give you a heads up: your trial wraps up in 4 days. After that, the AI goes offline and you'll be back to handling everything manually. If you want to keep it running, I can lock you in at $497/mo — no setup fee since you're already live. Just reply YES and I'll keep it on. — CJ, Smart Vault Co."

Action 8: Wait until contact replies OR 3 days pass.

Action 9: If/Else. Condition: contact replied.
YES branch: Add tag "trial-converted", send internal notification "SALE! {{contact.first_name}} from {{contact.company_name}} wants to keep AI assistant — $497/mo", end workflow.
NO branch: Continue.

Action 10: Send SMS (Day 14 — final). Message: "Hey {{contact.first_name}}, your AI trial ends today. After midnight, the AI goes offline and leads go back to manual. Want to keep it running? Reply YES and you're locked in. Last chance — CJ"

Action 11: Wait until contact replies OR 1 day pass.

Action 12: If/Else. Condition: contact replied.
YES branch: Add tag "trial-converted", send internal notification "SALE! {{contact.first_name}} converted from trial", end workflow.
NO branch: Add tag "trial-expired", send internal notification "Trial expired — {{contact.first_name}} from {{contact.company_name}} did not convert", end workflow.

Use default email and SMS sender. Branching tree structure with If/Else after every wait.
