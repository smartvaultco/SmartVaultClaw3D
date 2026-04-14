# Smart Vault Co. — Claude Code Skills Reference

These are custom slash commands for Claude Code that automate complex workflows. Type `/skill-name` in any Claude Code session within this project to activate.

Skills live in `.claude/commands/` within each project directory. This folder is a backup + reference copy.

---

## Skills Index

| # | Skill | Command | What It Does |
|---|-------|---------|-------------|
| 1 | **Content-to-Cash** | `/content-to-cash` | Full autopilot pipeline: topic idea → market research → 10-chapter ebook → 10-module course → GHL funnel spec → design assets. Runs parallel agents for speed. Outputs everything to `output/[topic-slug]/`. |
| 2 | **NotebookLM Course** | `/notebooklm-course` | Uploads ebook to NotebookLM and generates all course assets: audio podcast, video overview, slide deck, quiz, flashcards, infographic, study guide, briefing doc. Downloads everything locally. |
| 3 | **Create Agent** | `/create-agent` | Scaffolds a complete OpenClaw agent workspace with all required files (SOUL.md, IDENTITY.md, USER.md, AGENTS.md, TOOLS.md, MEMORY.md, HEARTBEAT.md, auth-profiles.json, sessions/, memory/, skills/). Adds agent to openclaw.json. |
| 4 | **Build Bot** | `/build-bot` | Generates a Python trading bot script (Polymarket, Options Wheel, VWAP, Commodities EMA, or ARCrypto). Includes API setup, strategy logic, Kelly Criterion sizing, loss limits, CSV logging, PM2 compatibility. |
| 5 | **Summarize to KB** | `/summarize-to-kb` | Converts any content (YouTube transcript, article, podcast, course) into a structured Knowledge Base markdown file. Extracts key concepts, frameworks, scripts, tools. Saves to the correct KB subfolder. |
| 6 | **Smart Vault Social** | `/smart-vault-social` | AI Social Media Architect for Smart Vault Co. + CJ brand. Generates platform-specific copy (LinkedIn, Instagram, Facebook, TikTok) with visual prompts (Higgsfield motion + Midjourney stills) and dispatches to n8n webhook for GHL publishing. |

---

## How to Use

### In Claude Code (any project):
```
/content-to-cash
```
Claude will ask for the topic, audience, brand, and pricing — then run the full pipeline.

### Install a skill in a new project:
```bash
mkdir -p .claude/commands
cp skills/content-to-cash.md .claude/commands/
```

### Skill locations across projects:

| Project | Path | Skills Installed |
|---------|------|-----------------|
| Smart Vault AI (E:) | `e:/Smart-Vault-Ai/.claude/commands/` | All 5 core skills |
| Smart Vault AI (F:) | `F:/Smart-Vault-Ai/.claude/commands/` | All 5 core skills |
| AI Social Media Manager | `e:/Ai-Social-Media-manager/.claude/commands/` | smart-vault-social |

---

## Skill Details

### 1. `/content-to-cash` — The Money Printer
**Input:** A topic idea + target audience
**Output:** Complete product suite ready to sell

Pipeline steps:
1. Creator Brief (brand voice, positioning, frameworks)
2. Market Research (top 10 demand-validated questions)
3. Ebook (10 chapters, 25,000+ words, cited stats)
4. QA Review (via NotebookLM or Claude self-review)
5. Course (10 modules with video scripts, worksheets, checklists, quizzes)
6. GHL Funnel Spec (6 pages, 4 automations, 7-day email nurture)
7. Design Assets (Canva specs or MCP generation)

**Reference files:**
- `KB/content-to-cash-pipeline.md`
- `KB/autopilot-workflow.md`
- `KB/ghl-funnel-traffic-playbook.md`
- `KB/atp-research-guide.md`
- `KB/creator-brief.md`

---

### 2. `/notebooklm-course` — Course Asset Factory
**Input:** An ebook/content file + course name
**Output:** 9 course assets downloaded locally

Assets generated:
- Audio Overview (podcast, .mp3)
- Video Overview (animated, .mp4)
- Slide Deck (.pptx)
- Quiz (markdown)
- Flashcards (markdown)
- Infographic (.png)
- Study Guide (markdown)
- Briefing Doc (markdown — great for sales page copy)
- Frameworks Reference Table (.csv)

**Prerequisite:** `python -m notebooklm login` (Google auth)

---

### 3. `/create-agent` — OpenClaw Agent Builder
**Input:** Agent name, department, type (boss/worker), reporting structure
**Output:** Complete agent workspace with 11 files + openclaw.json update

Creates:
- SOUL.md (personality, rules, workflows)
- IDENTITY.md (name, emoji, vibe)
- USER.md (CJ context)
- AGENTS.md (job description)
- TOOLS.md (API cheat sheet)
- MEMORY.md (starting facts)
- HEARTBEAT.md (tiny — avoids token burn)
- auth-profiles.json, sessions/, memory/, skills/

---

### 4. `/build-bot` — Trading Bot Generator
**Input:** Bot type (Polymarket/Options/VWAP/Commodities/Crypto), paper or live
**Output:** Complete Python bot script

Includes:
- API connection (env variables)
- Strategy logic from KB docs
- Position sizing (Kelly Criterion)
- Entry/exit rules
- Daily loss limit
- CSV trade logging
- PM2-compatible graceful shutdown

---

### 5. `/summarize-to-kb` — Knowledge Ingestion
**Input:** Any content (paste transcript, article, course notes)
**Output:** Structured KB markdown file in the correct subfolder

Extracts: key concepts, actionable steps, scripts, frameworks, rules, tools
Categories: trading / crypto / real estate / business / ai-tools

---

### 6. `/smart-vault-social` — Social Media Command Center
**Input:** A post topic or brief
**Output:** Multi-platform post copy + visual prompts + n8n webhook dispatch

Dual brand voice:
- **Smart Vault Co.** — Professional, data-driven, authority (50+ business owners)
- **CJ** — Mystic, futurist, empowering, educational (next-gen digital architects)

Platforms: LinkedIn, Instagram, Facebook, TikTok
Visual APIs: Higgsfield (motion), Midjourney (stills)
Dispatch: n8n webhook → GHL publishing
Logging: Appends to `posts-log.md`

---

## Future Skills (Planned)
- `/audit-client` — Run a full AI readiness audit for a prospect
- `/proposal-gen` — Generate a Done-With-You proposal from audit results
- `/weekly-report` — Auto-generate weekly analytics summary from GHL data
- `/ad-creative` — Generate Meta/YouTube ad creative sets with A/B variants
