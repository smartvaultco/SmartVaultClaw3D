# OpenClaw Multi-Agent Architecture Builder Skill

> **Trigger:** Use this skill whenever building, configuring, debugging, or extending OpenClaw multi-agent bot systems. This includes creating agent configs, writing SOUL.md files, setting up bot-to-bot communication, configuring openclaw.json, designing delegation flows, or scaling from single-agent to multi-agent architectures.

---

## Core Concept: What OpenClaw Is

OpenClaw is a **config-driven multi-agent framework** that runs AI bots as real, persistent, specialized workers — not disposable sub-agents. Every agent is a fully configured bot with its own personality, memory, tools, and identity files. The system uses a **Gateway Router** (Port 18789) that receives messages from Telegram/WhatsApp/Discord and routes them to the correct agent based on `openclaw.json` config.

**Message Flow Pipeline:**
```
User Input → Gateway Router → Routing Logic (openclaw.json) → Agent Initialization (SOUL.md → personality, USER.md → user context, memory/ → long-term memory) → AI Model Call (Claude) → Tool Execution (skills/) → Response Delivery → Sent to User
```

This is a deterministic, config-driven pipeline — no black boxes, full observability.

---

## File System Reference — What Each File Does

| File | Purpose | Real-World Analogy |
|---|---|---|
| `openclaw.json` | Master config defining agents, bindings, channels, models, tools | Building floor plan |
| `SOUL.md` | Bot personality, tone, rules, boundaries in plain English | Job description + personality brief |
| `USER.md` | Context about the human owner — preferences, job, timezone | PA file on their boss |
| `AGENTS.md` | Additional operational instructions for the agent | Operations manual |
| `IDENTITY.md` | Bot name, emoji, vibe — created during bootstrap ritual | Name badge + style guide |
| `TOOLS.md` | Personal notes about local tools and conventions | Cheat sheet pinned to the desk |
| `MEMORY.md` | Curated long-term memory, decisions, preferences, durable facts | Personal journal of key decisions |
| `HEARTBEAT.md` | Sticky note for background check-ins | Keep it tiny to avoid token burn |
| `auth-profiles.json` | Authentication credentials for the agent | Keychain of passwords |
| `sessions/` | Chat logs and session history | Chat logs |
| `memory/` | Long-term memory folder | Notebook your assistant keeps |
| `skills/` | Tool integrations and skill scripts | Apps on a phone |

**Every file has purpose — no magic, just intentionality, structure, and human-readable design.**

---

## The Four Structure Pathway

Each structure scales autonomy without sacrificing clarity or control. Always start at Structure 1 and scale up as needed.

### Structure 1: Single Agent Default
- **Pattern:** One bot, one brain, one Telegram bot
- **Best for:** Solo founders — one bot helping you run your store
- **Architecture:** Telegram → Gateway (Port 18789) → Single Business Bot (id: "main")
- **Model:** anthropic/claude-sonnet-4-5
- **Config:**
```json
{
  "agents": [
    { "id": "main", "default": true, "name": "Store Assistant" }
  ],
  "workspace": "../openclaw/workspace",
  "model": "anthropic/claude-sonnet-4-5",
  "channels": {
    "telegram": {
      "enabled": true,
      "botToken": "******",
      "dmpolicy": "pairing"
    }
  }
}
```

### Structure 2: Adjacent Team
- **Pattern:** Multiple equal agents, each with own Telegram bot, personality, memory
- **Best for:** Separating support/ops/marketing into dedicated bots
- Each agent fully isolated by default
- Optional agentToAgent via openclaw.json

### Structure 3: Boss + Workers Hierarchy
- **Pattern:** One boss you talk to — delegates to workers via `sessions_spawn()`
- **Boss Model:** Sonnet 4.5 or Opus (needs judgment/coordination)
- **Worker Models:** Sonnet/Gemini Flash (saves 50-80% on API costs)
- **Safety:** maxPingPongTurns = 5

### Structure 4: Hybrid Org Chart (Most Powerful)
- **Pattern:** Multiple bosses, each with dedicated worker teams
- **Complete isolation by default** — cross-talk only via explicit openclaw.json bindings
- Boss relationship = who can send tasks to whom, NOT what they share

---

## Why NOT Built-In Sub-Agents

| Feature | Disposable Sub-Agent | Full Worker Agent (OpenClaw) |
|---|---|---|
| Identity | No SOUL.md, USER.md, IDENTITY.md | Own SOUL.md — persistent personality |
| Memory | No memory folder | Own memory/ — remembers past work |
| Lifespan | Auto-archive ~60 min | Permanent — no timeout, no reset |
| Delegation | Cannot spawn sub-agents | Can delegate further |

**OpenClaw Pattern:** ALL agents — bosses AND workers — are full top-level entries in the agents list. Hierarchy via config — not inheritance.

---

## Enabling Bot-to-Bot Communication

Default: ISOLATED. Enable explicitly:
```json
{
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": ["marketing", "ops", "cx"],
      "maxPingPongTurns": 5
    }
  }
}
```

- `sessions_send` — Blocking direct message (waits for reply, max 5 turns)
- `sessions_spawn` — Fire-and-forget background task (parallel, non-blocking)

---

## Implementation Rules

1. Create ALL required files per agent: SOUL.md, USER.md, AGENTS.md, IDENTITY.md, TOOLS.md, MEMORY.md, HEARTBEAT.md, auth-profiles.json, sessions/, memory/, skills/
2. Write SOUL.md in plain English — personality, tone, rules, boundaries
3. Keep HEARTBEAT.md tiny to avoid token burn
4. Default to isolation — only enable agentToAgent when needed
5. Use cheaper models for workers, reserve Sonnet 4.5/Opus for bosses
6. Set maxPingPongTurns = 5 always
7. Config is king — all behavior changes through openclaw.json
8. Test via Telegram DM first
9. Workers are real persistent bots — not disposable sub-agents
