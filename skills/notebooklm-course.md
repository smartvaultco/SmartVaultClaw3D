# NotebookLM Course Asset Generator

Generate a complete course asset package from an ebook using NotebookLM — audio overviews, video overviews, slide decks, quizzes, infographics, and flashcards.

## Prerequisites
- NotebookLM CLI must be authenticated (`python -m notebooklm status`)
- If not authenticated, run `python -m notebooklm login` first
- Ebook file must exist (the source content to upload)

## When triggered, ask the user:

1. **Source file:** Path to the ebook/content file (e.g., `e:/Smart-Vault-Ai/output/THE-AI-GROWTH-PLAYBOOK-FULL.md`)
2. **Course name:** What to call the notebook (e.g., "AI Growth Masterclass")
3. **Target audience:** Who are the students? (e.g., "SMB owners aged 45-60, not technical")
4. **Output folder:** Where to save downloads (default: `e:/Smart-Vault-Ai/output/course-assets/`)
5. **Which assets?** (default: ALL)
   - [ ] Audio Overview (podcast-style deep dive)
   - [ ] Video Overview (animated explainer)
   - [ ] Slide Deck (presentation for each module)
   - [ ] Quiz (test understanding)
   - [ ] Flashcards (key concepts)
   - [ ] Infographic (visual summary)
   - [ ] Study Guide (written summary)
   - [ ] Briefing Doc (executive summary — great for sales page copy)

## Then execute this pipeline:

### STEP 1: Create NotebookLM Notebook & Upload Source

```bash
# Create the notebook
python -m notebooklm create "[Course Name]" --json

# Upload the ebook as source
python -m notebooklm source add "[source-file-path]" --notebook [notebook_id] --json

# Wait for processing
python -m notebooklm source wait [source_id] -n [notebook_id] --timeout 300
```

Also upload any supplementary sources:
- Creator Brief (for voice/tone context)
- Research data file (for additional stats)
- Any KB files relevant to the topic

### STEP 2: Generate Audio Overview (Podcast)

```bash
python -m notebooklm generate audio "Create a deep-dive podcast overview of this course material. Target audience: [audience]. Cover all 10 modules/chapters. Make it conversational, engaging, and packed with specific takeaways. This will be used as a bonus course module and lead magnet." --format deep-dive --length long --notebook [notebook_id] --json
```

**Use the audio for:**
- Bonus course module ("Listen to the full overview")
- Lead magnet (free podcast episode)
- Chop into social media clips
- YouTube/Spotify content

### STEP 3: Generate Video Overview (Animated Explainer)

```bash
python -m notebooklm generate video "Create an engaging video explainer covering the key frameworks and systems taught in this course. Target audience: [audience]. Focus on the transformation: what they'll be able to do after completing the course. Make it visually compelling and easy to follow." --format explainer --notebook [notebook_id] --json
```

**Use the video for:**
- Course sales page hero video
- Social media ads
- YouTube trailer
- Thank you page content

### STEP 4: Generate Slide Deck

```bash
python -m notebooklm generate slide-deck "Create a comprehensive presentation covering all modules in this course. Each module should have 3-5 slides covering: the problem, the framework, key steps, and action items. Target audience: [audience]. Style: professional, clean, data-driven." --format detailed --notebook [notebook_id] --json
```

**Use the slides for:**
- Course video recording (screen share the slides while teaching)
- Webinar presentation
- Download as PPTX for customization in PowerPoint/Canva

### STEP 5: Generate Quiz

```bash
python -m notebooklm generate quiz --difficulty medium --quantity more --notebook [notebook_id] --json
```

**Use the quiz for:**
- End-of-module assessments in GHL/Skool
- Lead magnet ("Test your AI automation IQ")
- Email engagement content

### STEP 6: Generate Flashcards

```bash
python -m notebooklm generate flashcards --difficulty medium --quantity more --notebook [notebook_id] --json
```

**Use flashcards for:**
- Bonus course material
- Study companion
- Mobile-friendly review tool

### STEP 7: Generate Infographic

```bash
python -m notebooklm generate infographic "Create a visual summary of the complete course framework. Show the 10 modules as a journey/roadmap. Include key stats and frameworks from each module. Target audience: [audience]." --orientation portrait --detail detailed --style professional --notebook [notebook_id] --json
```

**Use the infographic for:**
- Lead magnet (shareable on social)
- Course sales page visual
- Print handout for workshops
- Pinterest content

### STEP 8: Generate Study Guide & Briefing Doc

```bash
# Study guide (for students)
python -m notebooklm generate report --format study-guide --append "Target audience: [audience]. Organize by module/chapter. Include key takeaways, action items, and tool recommendations for each section." --notebook [notebook_id] --json

# Briefing doc (for sales page copy)
python -m notebooklm generate report --format briefing-doc --append "Write this as if briefing a potential student on what they'll learn and why it matters. Focus on transformation, ROI, and specific outcomes." --notebook [notebook_id] --json
```

### STEP 9: Wait for All Artifacts & Download

Use background agents to wait for each artifact:

```bash
# Check status of all artifacts
python -m notebooklm artifact list --notebook [notebook_id] --json

# Wait and download each (run as background tasks)
python -m notebooklm artifact wait [artifact_id] -n [notebook_id] --timeout 1200

# Downloads
python -m notebooklm download audio ./[output-folder]/audio-overview.mp3 -n [notebook_id]
python -m notebooklm download video ./[output-folder]/video-overview.mp4 -n [notebook_id]
python -m notebooklm download slide-deck ./[output-folder]/slides.pptx --format pptx -n [notebook_id]
python -m notebooklm download quiz ./[output-folder]/quiz.md --format markdown -n [notebook_id]
python -m notebooklm download flashcards ./[output-folder]/flashcards.md --format markdown -n [notebook_id]
python -m notebooklm download infographic ./[output-folder]/infographic.png -n [notebook_id]
python -m notebooklm download report ./[output-folder]/study-guide.md -n [notebook_id]
```

### STEP 10: Generate Data Table (Frameworks Reference)

```bash
python -m notebooklm generate data-table "Extract all frameworks, tools, and systems mentioned in the course. Columns: Framework Name, Chapter/Module, What It Does, Key Steps, Tools Needed" --notebook [notebook_id] --json

python -m notebooklm download data-table ./[output-folder]/frameworks-reference.csv -n [notebook_id]
```

## Output Summary

When complete, print:

| Asset | File | Use For |
|-------|------|---------|
| Audio Overview | audio-overview.mp3 | Bonus module, lead magnet, podcast |
| Video Overview | video-overview.mp4 | Sales page, ads, YouTube |
| Slide Deck | slides.pptx | Course videos, webinars |
| Quiz | quiz.md | Module assessments, lead magnet |
| Flashcards | flashcards.md | Bonus material, mobile review |
| Infographic | infographic.png | Social media, sales page, print |
| Study Guide | study-guide.md | Course companion, bonus PDF |
| Briefing Doc | briefing-doc.md | Sales page copy, email sequences |
| Frameworks Table | frameworks-reference.csv | Course reference sheet, cheat sheet |

## Integration with GHL/Skool Course:
- Upload audio as bonus Module 0 lesson
- Embed video on course sales page
- Use slides as screen-share content when recording module videos
- Import quiz questions into GHL quiz builder or Skool
- Offer flashcards + study guide as downloadable course bonuses
- Use briefing doc as source material for sales page copy
- Use infographic on landing page and as social share asset

## Super Prompt for NotebookLM Chat (After Sources Are Loaded):

When the notebook is set up and sources are ready, use this prompt in NotebookLM to generate custom content:

```
You are a course content architect. Based on all sources in this notebook, 
I need you to:

1. Identify the 10 most important concepts/frameworks taught
2. For each concept, provide:
   - A clear 2-sentence definition
   - The specific problem it solves
   - 3 actionable steps to implement it
   - 1 real stat or data point that proves it works
   - The tools needed
3. Flag any concepts that are underdeveloped or need more depth
4. Suggest 3 additional topics the audience would expect that aren't covered
5. Write a "course promise" statement: "After completing this course, you will be able to ___"

Target audience: [audience description]
Voice: Direct, no-fluff, systems-oriented. Back everything with data.
```
