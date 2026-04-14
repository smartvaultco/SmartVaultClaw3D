# GHL Workflow AI Prompt — Database Reactivation (DBR) Campaign
# Paste this into GHL Workflow AI to create the workflow

---

Create a workflow called "Database Reactivation Campaign" with these exact specs:

TRIGGER: Contact Tag Added = "dbr-reactivation"

Action 1: Send SMS. Message: "Hey {{contact.first_name}}! It's been a while since we've seen you at {{contact.company_name}}. We miss you! To welcome you back, here's an exclusive 50% off your next visit. Just reply YES to claim it before it expires this Friday. — {{contact.company_name}}"

Action 2: Wait until contact replies to SMS OR 1 day passes, whichever comes first.

Action 3: If/Else. Condition: contact replied.
YES branch: Go to Action 4.
NO branch: Go to Action 7.

Action 4: Add Tag "dbr-responded"

Action 5: Send Internal Notification to owner: "DBR Lead! {{contact.first_name}} ({{contact.phone}}) replied to reactivation SMS"

Action 6: Send SMS reply: "Awesome {{contact.first_name}}! Your 50% off is locked in. Here's the link to book your appointment: {{custom_values.booking_link}} — See you soon!"

Then end workflow.

Action 7: Send Email. Subject: "We saved something for you". Body: "Hey {{contact.first_name}}, We noticed it's been a while since your last visit and wanted to reach out personally. As a thank you for being a past customer, we're offering you an exclusive 50% off your next appointment. This offer expires this Friday. Click here to book: {{custom_values.booking_link}} We'd love to see you again! — {{contact.company_name}}"

Action 8: Wait until contact replies OR 2 days pass, whichever comes first.

Action 9: If/Else. Condition: contact replied.
YES branch: Add tag "dbr-responded", send internal notification "DBR Lead! {{contact.first_name}} responded to reactivation email", send booking link SMS, end workflow.
NO branch: Go to Action 10.

Action 10: Send SMS. Message: "Last chance {{contact.first_name}}! Your 50% off at {{contact.company_name}} expires tomorrow. Reply YES or book here: {{custom_values.booking_link}}"

Action 11: Wait until contact replies OR 1 day passes.

Action 12: If/Else. Condition: contact replied.
YES branch: Add tag "dbr-responded", send internal notification, send booking confirmation, end workflow.
NO branch: Add tag "dbr-no-response", end workflow.

Use default SMS and email sender. This must be a branching tree with If/Else after every wait.
