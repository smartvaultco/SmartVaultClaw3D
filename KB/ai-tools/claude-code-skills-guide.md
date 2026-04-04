# Claude Code Free Skills — How to Use for Smart Vault Co.

## What the PDF Points To

Three libraries of pre-built Claude Code skills you can install right now:

| Library | Count | Link |
|---------|-------|------|
| Awesome Agent Skills | 380+ skills | github.com/ghostdevv/awesome-agent-skills |
| Claude Command Suite | 148 commands + 54 agents | github.com — search "claude command suite" |
| Production-Ready Commands | 57 commands | github.com — search "claude code production commands" |
| Browse all | awesomeclaude.ai | awesomeclaude.ai |

---

## How Skills Work in Claude Code

A "skill" is a `.md` file you drop into `.claude/commands/` in your project.
When you type `/skill-name` in Claude Code, it executes that skill as a full prompt with context.

They run INSIDE this VS Code session — meaning I (Claude) execute them, not a separate process.

---

## Skills That Directly Help Smart Vault Co.

### For the trading bots:
- `/backtest-strategy` — analyze a trading strategy before coding it
- `/code-review` — review bot code for bugs before going live
- `/write-tests` — auto-generate tests for trading bot logic
- `/security-audit` — check bot code for vulnerabilities

### For the agent system:
- `/create-agent` — scaffold a new OpenClaw agent with all required files
- `/write-plan` → `/execute-plan` — plan a complex build, then execute step by step
- `/brainstorm` — generate ideas for new income streams or products

### For the KB and research:
- `/summarize` — paste any YouTube transcript or article → get structured KB file
- `/extract-insights` — pull actionable points from any document
- `/research-report` — generate a deep research brief on any topic

### For SBTLC and agency work:
- `/write-copy` — generate ad copy, emails, social posts for client
- `/seo-audit` — audit a webpage for SEO issues
- `/email-sequence` — generate full nurture sequence

### For development:
- `/debug` — paste an error, get the fix
- `/refactor` — clean up existing code
- `/api-integration` — scaffold API connection code (Alpaca, Shopify, GHL, etc.)

---

## How to Install Skills (2 minutes)

```bash
# In your project root (f:/Smart-Vault-Ai/):
mkdir -p .claude/commands

# Download a skill (example):
# Go to awesomeclaude.ai → find skill → copy the .md content → save to:
# f:/Smart-Vault-Ai/.claude/commands/skill-name.md

# Then in Claude Code, type:
/skill-name
```

That's it. Claude Code picks up any `.md` file in `.claude/commands/` automatically.

---

## Priority Skills to Install First

1. `/create-agent` — speeds up adding new bots to the team
2. `/summarize` — paste Sean Terry/Tony/Gaven transcripts → instant KB files
3. `/write-plan` + `/execute-plan` — plan complex bot builds before coding
4. `/api-integration` — scaffold the Alpaca, Shopify, GHL connections fast
5. `/debug` — for when bot code breaks

---

## The Summarize Skill — Your Biggest Leverage Point

Every YouTube video you watch (Sean Terry, John Brown, Gaven, Pace Morby, Alex Hormozi) can be turned into a permanent KB file in 60 seconds:

1. Get the transcript (YouTube → ... → Show Transcript → copy)
2. Type `/summarize` in Claude Code
3. Paste the transcript
4. Get a structured KB file saved to the right folder automatically

This is how the bots get smarter over time — every video CJ watches becomes a knowledge file the bots can reference.
