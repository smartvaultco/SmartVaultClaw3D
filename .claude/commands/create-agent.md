# Create New OpenClaw Agent

Create a complete new OpenClaw agent for Smart Vault Co. with ALL required files.

When invoked, ask the user:
1. Agent name and ID (e.g., "id: seo-bot, name: SEO Bot")
2. Department (Finance / Media / Operations / R&D / Real Estate / Sales / Infrastructure)
3. Type: boss or worker
4. Reports to: which agent
5. Main job in one sentence
6. Key tools/APIs needed

Then create the full agent workspace at `f:/Smart-Vault-Ai/agents/[id]/` with:
- SOUL.md (full personality, rules, workflows)
- IDENTITY.md (name, emoji, vibe)
- USER.md (CJ's context)
- AGENTS.md (job description / operations manual)
- TOOLS.md (APIs and tools cheat sheet)
- MEMORY.md (durable facts to start with)
- HEARTBEAT.md (one-line reminder — keep tiny)
- auth-profiles.json (empty — {})
- sessions/ folder
- memory/ folder
- skills/ folder

Then add the agent to openclaw.json agents list and tools.agentToAgent.allow list.

Confirm completion with a summary of what was created.
