# Autopilot Workflow — NotebookLM + Claude Production System
## Step 4: Automate Ebook + Course Creation for Any Topic

**Last Updated:** 2026-04-12
**Purpose:** Repeatable system so every future book/course runs on autopilot. No Manus subscription needed.

---

## THE STACK (Zero Extra Subscriptions)

| Role | Tool | Cost |
|------|------|------|
| Research Brain | NotebookLM (Google, free) | $0 |
| Writing Engine | Claude Code / Claude.ai | Already paying |
| Course Hosting | GoHighLevel | Already paying |
| Design | Canva (free tier or Pro) | $0-13/mo |
| Audio/Video | ElevenLabs + screen recording | Free tier works |
| Delivery | GHL + Gumroad or Stripe | Already paying |

**Total extra cost: $0**

---

## THE 7-STEP AUTOPILOT PROCESS

### STEP 1: Create the Smart Vault (NotebookLM)
**Time:** 20-30 minutes
**Who does it:** You (CJ) — one-time per topic

1. Go to NotebookLM (notebooklm.google.com)
2. Create a new notebook named: `[Topic] Smart Vault`
3. Upload these sources:
   - Your **Creator Brief** (creator-brief.md)
   - Your **ATP Research** data (screenshots, exports, or pasted text)
   - 3-5 **competitor ebooks/blog posts** on the same topic (PDF or pasted)
   - Your **existing KB files** relevant to the topic
   - Any **Reddit threads, Quora answers, YouTube transcripts** from research
4. Let NotebookLM index everything

**Output:** A queryable knowledge base with all your research in one place.

---

### STEP 2: Generate Chapter Outlines via NotebookLM
**Time:** 15-20 minutes
**Who does it:** NotebookLM

Prompt NotebookLM with:

```
Based on all sources in this notebook, I need to write a 10-chapter ebook 
for small business owners (ages 45-60, 3-50 employees) about [TOPIC].

Each chapter answers one of these questions:
1. [Top 10 question from ATP research]
2. [...]
...
10. [...]

For each chapter, give me:
- A compelling chapter title
- 3-5 key points to cover (pulled from the sources)
- 1 specific data point or case study from the sources
- 1 framework or system I should teach
- The transformation the reader gets from this chapter
```

**Output:** 10 detailed chapter outlines grounded in real research.

---

### STEP 3: Write Each Chapter with Claude
**Time:** 2-4 hours (all 10 chapters)
**Who does it:** Claude Code or Claude.ai

For each chapter, feed Claude this prompt:

```
You are ghostwriting Chapter [#] of an ebook for Smart Vault HQ.

CONTEXT:
[Paste the Creator Brief — or the key sections]

CHAPTER OUTLINE:
[Paste the NotebookLM outline for this chapter]

AUDIENCE: SMB owners, 45-60, overwhelmed by tech, want ROI fast.

VOICE: Direct, no-fluff, action-oriented. "Systems over sweat." 
Back every claim with data. Use frameworks, not motivational fluff.

STRUCTURE:
- Opening hook (address the reader's exact pain point)
- Why this matters (cost of NOT solving this)
- The Smart Vault approach (your framework)
- Step-by-step breakdown (practical, numbered)
- Real numbers (data, benchmarks, case studies)
- Tools you need (specific recommendations)
- Action items (3-5 things to do TODAY)
- Chapter summary (3 bullets)

LENGTH: 2,500-4,000 words.
TONE: Like a smart friend who's already figured this out and is walking you through it.

Write the full chapter now.
```

**Output:** Complete chapter draft. Repeat 10x.

**Pro tip:** Run chapters in parallel — open multiple Claude.ai conversations or use Claude Code to batch them.

---

### STEP 4: Generate Course Scripts from Chapters
**Time:** 1-2 hours
**Who does it:** Claude

For each chapter, prompt Claude:

```
Convert this ebook chapter into a 15-20 minute video lesson script.

CHAPTER CONTENT:
[Paste the full chapter]

FORMAT:
- INTRO (2 min): State the problem, why it matters, what they'll learn
- TEACH (8-12 min): Core framework + step-by-step (visual-friendly, 
  reference slides/screen share moments)
- DEMO (3-5 min): "Let me show you" walkthrough notes 
  (what to screen-record)
- RECAP (2 min): 3 key takeaways + action items + tease next module

Also generate:
1. A 1-page PDF worksheet (key concepts + fill-in exercises)
2. An action checklist (5 items max)
3. 3 quiz questions (multiple choice) to test understanding

Write in a conversational, teaching tone — like you're on a Zoom call 
walking them through it.
```

**Output:** Video script + worksheet + checklist + quiz for each module.

---

### STEP 5: Produce the Assets
**Time:** 1-2 days
**Who does it:** You + AI tools

| Asset | Tool | Notes |
|-------|------|-------|
| Ebook PDF layout | Canva (ebook template) | Drop in chapter text, add branding |
| Ebook cover | Canva or Midjourney | Professional, clean, bold title |
| Course videos | Screen recording + talking head | Loom, OBS, or phone camera |
| Voiceover (optional) | ElevenLabs | Clone your voice or use stock |
| Worksheets | Canva or Google Docs → PDF | One per module |
| Slide decks | Canva (presentation template) | For video lesson visuals |

---

### STEP 6: Upload to NotebookLM for QA
**Time:** 30 minutes
**Who does it:** NotebookLM

1. Upload the complete ebook draft back into NotebookLM
2. Ask: "Review this ebook for contradictions, gaps, weak arguments, or unsupported claims. List every issue."
3. Fix issues with Claude
4. Ask: "What questions would a skeptical SMB owner have after reading this that aren't answered?"
5. Add a FAQ section or strengthen weak chapters

**Output:** QA'd, gap-checked final draft.

---

### STEP 7: Package and Deploy
**Time:** 2-4 hours
**Who does it:** You + GHL

1. **Ebook:** Export from Canva as PDF → Upload to GHL product / Gumroad / Stripe
2. **Course:** Upload videos to GHL membership area, attach worksheets
3. **Lead Magnet:** Extract Chapter 1 (or a checklist) as free PDF
4. **Email Sequence:** Claude writes 7-day nurture sequence
5. **Sales Page:** Built in GHL (see funnel playbook)

---

## AUTOPILOT REUSE — NEW TOPIC CHECKLIST

When you want to create a NEW ebook + course on a different topic:

```
[ ] 1. Pick topic + run 10 ATP keyword searches
[ ] 2. Collect data from Reddit, YouTube, Quora, Ad Libraries
[ ] 3. Create new NotebookLM notebook, upload all research + Creator Brief
[ ] 4. Generate 10 chapter outlines via NotebookLM
[ ] 5. Write 10 chapters via Claude (use chapter prompt template)
[ ] 6. Generate 10 course scripts via Claude (use module prompt template)
[ ] 7. Design ebook in Canva, record course videos
[ ] 8. QA via NotebookLM upload
[ ] 9. Deploy to GHL (product + membership + funnel + email sequence)
[ ] 10. Launch with organic + ads (see traffic playbook)
```

**Estimated time per new product:** 3-5 days from research to live.
**Estimated cost per new product:** $0 (using tools you already have).

---

## NOTEBOOKLM POWER MOVES

### Audio Overview (Podcast-Style)
NotebookLM can generate a podcast-style audio overview of your entire notebook. Use this as:
- A **bonus module** in your course
- A **lead magnet** (free podcast episode)
- **Content repurposing** — chop into social clips

### Study Guide Generation
Ask NotebookLM to generate a study guide from your ebook — instant course companion material.

### FAQ Generation
Upload customer questions/objections → NotebookLM generates answered FAQs grounded in your content.

### Briefing Doc
Ask for a "briefing document" — this becomes your sales page copy or webinar script.
