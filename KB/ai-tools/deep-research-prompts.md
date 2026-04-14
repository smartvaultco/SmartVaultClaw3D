# Deep Research Prompts System
## Purpose: Reusable prompts for extracting maximum value from NotebookLM notebooks
## Usage: Run via `python -m notebooklm ask "PROMPT" --notebook ID`
## Last Updated: 2026-04-11

---

## TIER 1: Full KB Extraction (Run first on every notebook)

### Prompt: Complete Knowledge Extraction
```
Provide a complete, exhaustive summary of ALL content in this notebook. Structure as a knowledge base document covering:
1) Every key concept and definition
2) All frameworks, models, and systems mentioned
3) Every specific strategy and actionable step
4) Tools, software, and platforms referenced
5) Names, people, and organizations mentioned
6) Specific numbers, prices, percentages, and metrics
7) Key quotes and principles
8) Warnings, mistakes to avoid, and risk factors
Be thorough — extract every actionable piece of knowledge. This will train an AI agent.
```

### Prompt: Sellable Product Analysis
```
Analyze all content in this notebook as if you were a product manager. Answer:
1) What specific digital products could be created from this content? (courses, ebooks, templates, coaching programs)
2) Who is the ideal buyer? (demographics, pain points, willingness to pay)
3) What price points would this content support? ($19 tripwire vs $997 course vs $5000 coaching)
4) What unique angle or hook makes this content different from competitors?
5) What's the ONE most compelling transformation this content promises?
6) List 3 potential product names with taglines.
```

---

## TIER 2: Deep Dive Prompts (Run after Tier 1 for high-value notebooks)

### Prompt: Step-by-Step Implementation Guide
```
Convert the content of this notebook into a detailed, numbered step-by-step implementation guide. For each step include:
- What to do (specific action)
- How to do it (tools, templates, exact process)
- Common mistakes to avoid
- Expected outcome/milestone
Structure this so a complete beginner could follow it and get results.
```

### Prompt: FAQ & Objection Handler
```
Based on all content in this notebook, generate:
1) The 20 most likely questions a student/customer would ask about this material
2) Detailed answers to each question using ONLY information from these sources
3) The top 10 objections someone would have before buying a product based on this content
4) Persuasive responses to each objection using evidence from the sources
```

### Prompt: Case Studies & Proof Points
```
Extract every specific example, case study, success story, number, and proof point from this notebook. Include:
- Dollar amounts and returns mentioned
- Before/after transformations
- Specific timelines and results
- Named examples of people or companies
- Any statistics or data points
Format as a "proof bank" that could be used in sales pages and marketing.
```

### Prompt: Content Calendar Generator
```
Using the material in this notebook, create a 30-day content calendar. For each day provide:
- Platform (Twitter/X, Instagram, YouTube, TikTok, Email)
- Content type (thread, carousel, short-form video, long-form, newsletter)
- Hook/headline
- Key talking points (2-3 bullets from the source material)
- Call to action
Mix educational, inspirational, and promotional content in a 70/20/10 ratio.
```

---

## TIER 3: Specialized Extraction Prompts

### Prompt: Trading/Finance KB
```
Extract ALL trading strategies, financial frameworks, and investment rules. For each:
- Strategy name and type (bullish/bearish/neutral)
- Entry criteria (when to get in)
- Exit criteria (when to get out)
- Risk management rules
- Position sizing guidance
- Tools/platforms needed
- Example trades mentioned
Also extract all mindset principles related to money and risk.
```

### Prompt: Esoteric/Spiritual KB
```
Extract ALL spiritual concepts, metaphysical principles, and esoteric knowledge. For each:
- Concept name and tradition it belongs to
- Core teaching/principle explained simply
- Practical application (how to use it)
- Connections to other concepts mentioned
- Books or sources referenced
- Key figures and teachers mentioned
Organize by theme: consciousness, energy, history, practice, cosmology.
```

### Prompt: Business/Agency KB
```
Extract ALL business strategies and agency-building knowledge. Cover:
- Revenue models and pricing structures
- Client acquisition methods (with specific scripts/templates)
- Service delivery frameworks and SOPs
- Tech stack recommendations (specific tools + why)
- Scaling strategies (from solo to team)
- Financial targets and benchmarks
- Sales scripts and closing techniques
Include every specific dollar amount, conversion rate, and metric mentioned.
```

### Prompt: Historical/Identity KB
```
Extract ALL historical claims, genealogical information, and identity-related knowledge. For each:
- Specific historical claim or thesis
- Evidence or sources cited
- Key dates, places, and people
- Documents or records referenced
- Counter-narratives addressed
- Actionable research steps (how to verify or continue research)
Organize chronologically where possible.
```

---

## TIER 4: Cross-Notebook Synthesis (Run after extracting multiple notebooks)

### Prompt: Pattern Recognition
```
Compare the strategies and frameworks across all sources. Identify:
1) Recurring themes and principles that appear in multiple sources
2) Contradictions or disagreements between sources
3) The "meta-framework" — what's the underlying pattern?
4) Gaps — what important topics are NOT covered?
5) The single most powerful insight that connects everything
```

### Prompt: Curriculum Design
```
Using all content, design a complete curriculum structure:
- Module names and descriptions
- Logical learning sequence (what must come first)
- Prerequisites for each module
- Estimated time to complete each module
- Assessment/milestone for each module
- Which sources feed into which modules
Format as a course outline ready for a learning platform.
```

---

## AUTOMATION: Batch Processing Script

To run Tier 1 on all notebooks automatically:

```bash
# Extract KB from a notebook
PYTHONIOENCODING=utf-8 python -m notebooklm ask "Provide a complete, exhaustive summary of ALL content in this notebook..." --notebook NOTEBOOK_ID

# Run sellable product analysis
PYTHONIOENCODING=utf-8 python -m notebooklm ask "Analyze all content as if you were a product manager..." --notebook NOTEBOOK_ID
```

### Priority Order for Processing:
1. Business/Money notebooks (highest sell potential)
2. Trading notebooks (Trading Bot KB)
3. Esoteric/Spiritual notebooks (premium content series)
4. Indigenous History notebooks (book/documentary potential)
5. School notebooks (personal, low priority)
