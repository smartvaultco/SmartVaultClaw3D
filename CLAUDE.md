# CLAUDE.md — OpenClaw Multi-Agent Architecture Reference

## Project Context

This project uses **OpenClaw** — a config-driven multi-agent framework for building persistent, specialized AI bot teams. Bots communicate via Telegram, run through a Gateway Router (Port 18789), and are configured entirely through JSON and markdown files.

**Owner:** Smart Vault Co. LLC
**Primary Dev Environment:** VS Code + Claude Code
**Framework:** OpenClaw Multi-Agent System
**Bot Interface:** Telegram (primary), WhatsApp/Discord (supported)
**AI Models:** Anthropic Claude (Sonnet 4.5 for bosses, Sonnet/Haiku for workers)
**GitHub:** https://github.com/iamlukethedev/Claw3D

---

## Quick Reference: OpenClaw Architecture

### Message Flow
```
User (Telegram) → Gateway Router (Port 18789) → Routing Logic (openclaw.json)
→ Agent Init (SOUL.md + USER.md + memory/) → Claude API Call → Tool Exec (skills/) → Response → User
```

### Required Files Per Agent (ALL of these — incomplete agents malfunction)
- `SOUL.md` — Personality, tone, rules, boundaries (plain English)
- `USER.md` — Context about CJ (the human owner)
- `AGENTS.md` — Job description / operational instructions
- `IDENTITY.md` — Name, emoji, vibe
- `TOOLS.md` — Notes about local tools and APIs (cheat sheet)
- `MEMORY.md` — Long-term memory, durable facts, key decisions
- `HEARTBEAT.md` — Background check-in notes (KEEP TINY — avoid token burn)
- `auth-profiles.json` — Authentication credentials
- `sessions/` — Chat history per session
- `memory/` — Persistent long-term memory folder
- `skills/` — Tool integrations and skill scripts

### Model Assignments
| Role | Model | Why |
|------|-------|-----|
| Boss agents (CEO, Trading Bot, RE Bot) | `anthropic/claude-sonnet-4-6` | Judgment + coordination |
| Worker agents | `anthropic/claude-haiku-4-5` | Speed + cost (50-80% savings) |
| Ad Creator, Closer, Automation Bot | `anthropic/claude-sonnet-4-6` | Strategy quality required |

---

## Four Structures — Choose Based on Scale

### Structure 1: Single Agent (Start Here)
One bot, one brain, one Telegram bot. One openclaw.json, one workspace.

### Structure 2: Adjacent Team
Multiple equal agents, each with own Telegram bot + workspace. Fully isolated by default.

### Structure 3: Boss + Workers
One boss you talk to → delegates via `sessions_spawn()`. Workers run parallel, boss combines, replies once.

### Structure 4: Hybrid Org Chart (This Project — Smart Vault Co.)
Multiple bosses (CEO, Trading Bot, RE Bot) each with dedicated workers.
You chat directly with each boss via Telegram. Workers route through bosses only.
Complete isolation by default — cross-talk only via explicit openclaw.json bindings.

---

## openclaw.json Structure (Smart Vault Co. — Structure 4)

```json
{
  "agents": [ /* ALL agents declared equally here */ ],
  "workspace": "f:/Smart-Vault-Ai/agents",
  "model": "anthropic/claude-sonnet-4-6",
  "channels": {
    "ceobot": { "enabled": true, "botToken": "${TELEGRAM_CEO_BOT_TOKEN}", "dmpolicy": "pairing" },
    "tradingbot": { "enabled": true, "botToken": "${TELEGRAM_TRADING_BOT_TOKEN}", "dmpolicy": "pairing" },
    "rebot": { "enabled": true, "botToken": "${TELEGRAM_RE_BOT_TOKEN}", "dmpolicy": "pairing" }
  },
  "bindings": [
    { "agentId": "ceo", "channel": "telegram", "accountId": "ceobot" },
    { "agentId": "trading-bot", "channel": "telegram", "accountId": "tradingbot" },
    { "agentId": "real-estate-bot", "channel": "telegram", "accountId": "rebot" }
  ],
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": [ /* all agent IDs */ ],
      "maxPingPongTurns": 5
    }
  }
}
```

---

## Bot-to-Bot Communication

**Default: ISOLATED.** Enable explicitly:
```json
{
  "tools": {
    "agentToAgent": {
      "enabled": true,
      "allow": ["ceo", "trading-bot", "real-estate-bot", "research", "hustle-bot", "..."],
      "maxPingPongTurns": 5
    }
  }
}
```

- `sessions_send` — Blocking (waits for reply, max 5 turns) — use for data you need before continuing
- `sessions_spawn` — Fire-and-forget (parallel, non-blocking) — use for background tasks

---

## Critical Rules (Never Break These)

1. **Workers are real bots** — not disposable sub-agents. They have SOUL.md, memory, identity. They persist forever.
2. **Config is king** — all behavior changes through openclaw.json, not code
3. **Zero trust by default** — agents cannot communicate unless explicitly allowed
4. **maxPingPongTurns = 5** — always set, prevents infinite loops
5. **HEARTBEAT.md must stay tiny** — one or two lines max, avoid token burn
6. **Test via Telegram DM first** — validate single agent before scaling
7. **All agents are top-level** in the agents list — hierarchy via config bindings only
8. **Each workspace is self-contained** — no shared state unless explicitly configured
9. **Every agent needs ALL required files** — incomplete agents malfunction
10. **Model routing matters** — bosses get Sonnet 4.5/Opus, workers get Haiku/Flash

---

## Smart Vault Co. Agent Registry

| ID | Name | Type | Telegram Bot | Model |
|----|------|------|-------------|-------|
| ceo | Clawbot CEO | Boss T1 | ✅ ceobot | Sonnet |
| trading-bot | Trading Bot | Boss T2 | ✅ tradingbot | Sonnet |
| real-estate-bot | Real Estate Bot | Boss T2 | ✅ rebot | Sonnet |
| research | Research Bot | Worker | ❌ | Sonnet |
| hustle-bot | Hustle Bot | Worker | ❌ | Haiku |
| closer | Closer Bot | Worker | ❌ | Sonnet |
| product-scout | Product Scout | Worker | ❌ | Haiku |
| content-builder | Content Builder | Worker | ❌ | Haiku |
| social-media-bot | Social Media Bot | Worker | ❌ | Haiku |
| email-bot | Email Bot | Worker | ❌ | Haiku |
| designer | Designer Bot | Worker | ❌ | Haiku |
| ad-creator | Ad Creator | Worker | ❌ | Sonnet |
| order-manager | Order Manager | Worker | ❌ | Haiku |
| customer-service | CS Bot | Worker | ❌ | Haiku |
| analytics-bot | Analytics Bot | Worker | ❌ | Haiku |
| automation-bot | Automation Bot | Worker | ❌ | Sonnet |

---

## Development Workflow

1. Define agent purpose and role
2. Create workspace directory with ALL required files
3. Write SOUL.md first (personality drives everything)
4. Configure openclaw.json (agent entry + channel binding + model)
5. Test via Telegram DM in Structure 1
6. Scale to Structure 4 when delegation is needed
7. Enable agentToAgent only when required
8. Monitor via sessions/ logs and memory/ folder
