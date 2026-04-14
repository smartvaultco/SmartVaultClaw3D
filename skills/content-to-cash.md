# Content-to-Cash: Ebook + Course Autopilot

Automate the full pipeline from topic idea to sellable ebook + course + GHL funnel.

## When triggered, ask the user:

1. **Topic:** What's the subject? (e.g., "AI automation for dentists", "crypto trading for beginners")
2. **Target audience:** Who's buying? (age, income, industry, pain points)
3. **Brand:** Which brand/colors? (default: Smart Vault HQ — Navy #0A0E1A, Cyan #00D4FF, Gold #FFD700, Green #00FF88)
4. **Price points:** Ebook price, course price, upsell price? (defaults: $29 / $197 / $497)

## Then execute this 7-step pipeline automatically:

### STEP 1: Creator Brief
Generate an LLM-ready Creator Brief for the topic using the template at `e:/Smart-Vault-Ai/KB/creator-brief.md` as reference. Include: who you are, what you do, who it's for, positioning, frameworks, voice/tone, tech stack. Save to `e:/Smart-Vault-Ai/output/[topic-slug]/creator-brief.md`.

### STEP 2: Market Research
Run web searches for the topic on:
- AnswerThePublic-style queries (what/how/why/can/which questions)
- Reddit, YouTube titles, Quora top questions
- Ad library competitor research angles

Collect the top 10 demand-validated questions. Save to `e:/Smart-Vault-Ai/output/[topic-slug]/top-10-questions.md`.

### STEP 3: Write the Ebook
For each of the 10 questions, write a full chapter (2,500-4,000 words) using this structure:
- Opening hook (address the reader's exact pain point)
- Why This Matters (cost of NOT solving this)
- The Framework/Approach (your IP/system for solving this)
- Step-by-Step Breakdown (practical, numbered)
- Tools You Need (specific recommendations)
- Action Items (3-5 things to do TODAY)
- Chapter Summary (3 bullets)

Run deep web research for real statistics, case studies, and benchmarks. Inject cited data into every chapter.

Add front matter (About, Who This Is For, How to Use) and back matter (Tool Reference, Framework Guide, CTAs).

Use parallel agents — batch chapters 1-3, 4-6, 7-10 simultaneously for speed.

Save to `e:/Smart-Vault-Ai/output/[topic-slug]/EBOOK-FULL.md`.

### STEP 4: QA the Ebook
If NotebookLM is authenticated, upload the ebook and run QA for contradictions, gaps, weak arguments, unsupported claims, and repetitive content. Apply fixes.

If NotebookLM is not available, use Claude to self-review against the same criteria.

Save QA report to `e:/Smart-Vault-Ai/output/[topic-slug]/qa-review.md`.

### STEP 5: Generate Course Modules
For each of the 10 chapters, generate:
- **Video lesson script** (15-20 min): Intro (2 min), Teach (8-12 min), Demo with [SLIDE:] and [SCREEN SHARE:] cues (3-5 min), Recap (2 min)
- **PDF worksheet** (1 page): Key concepts, fill-in-the-blank exercises, apply-to-your-business prompts
- **Action checklist** (5 items with checkboxes)
- **Quiz** (3 multiple choice questions with answer key)

Run in parallel — batch modules 1-3, 4-6, 7-10 simultaneously.

Save to `e:/Smart-Vault-Ai/output/[topic-slug]/COURSE-FULL.md`.

### STEP 6: Build GHL Funnel Spec
Generate the complete GHL funnel blueprint using the template at `e:/Smart-Vault-Ai/output/ghl-funnel-build-spec.md` as reference. Include:
- 6 pages: Lead Magnet, Thank You + Tripwire, Ebook Sales, Course Sales, Audit Booking, Confirmation
- GHL AI prompts for each page (ready to paste into GHL)
- 4 automations: Nurture sequence, Ebook delivery, Course onboarding, Audit reminders
- 7-day email nurture sequence (day-by-day with subjects and content)
- Stripe products, GHL tags, pipeline stages
- Course hosting setup in GHL membership area (module structure, drip schedule, worksheet attachments)

Save to `e:/Smart-Vault-Ai/output/[topic-slug]/ghl-funnel-spec.md`.

### STEP 7: Design Assets
Generate via Canva MCP (if available):
- Ebook cover (poster format with brand colors)
- Ebook document (doc format with full chapter structure)

If Canva MCP not available, output design specs for manual Canva build.

Save links/specs to `e:/Smart-Vault-Ai/output/[topic-slug]/design-assets.md`.

## Output Summary
When complete, print a summary table:
| Asset | File | Word Count | Status |
|-------|------|-----------|--------|

And list the next manual steps:
1. Design ebook in Canva (paste text from EBOOK-FULL.md)
2. Record course videos (use scripts from COURSE-FULL.md)
3. Build GHL funnel (paste prompts from ghl-funnel-spec.md into GHL AI)
4. Upload course to GHL membership area
5. Start organic content (chop ebook chapters into social posts)
6. Launch paid ads after 50+ organic leads

## Reference Files
- Pipeline system: `e:/Smart-Vault-Ai/KB/content-to-cash-pipeline.md`
- Autopilot workflow: `e:/Smart-Vault-Ai/KB/autopilot-workflow.md`
- GHL playbook: `e:/Smart-Vault-Ai/KB/ghl-funnel-traffic-playbook.md`
- ATP research guide: `e:/Smart-Vault-Ai/KB/atp-research-guide.md`
- Open-source toolbox: `e:/Smart-Vault-Ai/KB/open-source-ai-toolbox.md`
- Creator brief template: `e:/Smart-Vault-Ai/KB/creator-brief.md`
