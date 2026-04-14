# GHL Workflow AI Prompt — Automated Reputation Management
# Paste this into GHL Workflow AI to create the workflow

---

Create a workflow called "Auto Review Request" with these exact specs:

TRIGGER: Contact Tag Added = "job-completed"

Action 1: Wait 2 hours after trigger.

Action 2: Send SMS. Message: "Hey {{contact.first_name}}! Thank you so much for choosing {{contact.company_name}}. We'd love to hear how your experience was. Would you mind leaving us a quick Google review? It only takes 30 seconds and helps us out a ton: {{custom_values.google_review_link}} — Thank you! {{contact.company_name}}"

Action 3: Wait until contact clicks the review link OR 1 day passes, whichever comes first.

Action 4: If/Else. Condition: contact clicked link or replied.
YES branch: Add tag "review-left", send internal notification "{{contact.first_name}} left a review!", end workflow.
NO branch: Go to Action 5.

Action 5: Send SMS. Message: "Hey {{contact.first_name}}, just a friendly reminder — if you have 30 seconds, we'd really appreciate a quick review: {{custom_values.google_review_link}} Thank you!"

Action 6: Wait 2 days.

Action 7: If/Else. Condition: contact clicked or replied.
YES branch: Add tag "review-left", notify owner, end workflow.
NO branch: Add tag "review-not-left", end workflow.

Use default SMS sender. Keep it friendly and short.
