#!/bin/bash
# Smart Vault Co. — Register all agents with OpenClaw Gateway
export NVM_DIR="$HOME/.nvm"
. "$NVM_DIR/nvm.sh"

BASE="/mnt/f/Smart-Vault-Ai/agents"

echo "=== Smart Vault Co. — Registering 22 Agents ==="
echo ""

# Boss Tier 1
openclaw agents add ceo --workspace "$BASE/CEO" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: ceo" || echo "SKIP: ceo (exists)"

# Boss Tier 2
openclaw agents add trading-bot --workspace "$BASE/trading-bot" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: trading-bot" || echo "SKIP: trading-bot"
openclaw agents add real-estate-bot --workspace "$BASE/real-estate-bot" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: real-estate-bot" || echo "SKIP: real-estate-bot"
openclaw agents add rd-director --workspace "$BASE/rd-director" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: rd-director" || echo "SKIP: rd-director"

# Workers - Sonnet (need judgment)
openclaw agents add research --workspace "$BASE/research" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: research" || echo "SKIP: research"
openclaw agents add closer --workspace "$BASE/closer" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: closer" || echo "SKIP: closer"
openclaw agents add ad-creator --workspace "$BASE/ad-creator" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: ad-creator" || echo "SKIP: ad-creator"
openclaw agents add automation-bot --workspace "$BASE/automation-bot" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: automation-bot" || echo "SKIP: automation-bot"

# Workers - Haiku (speed + cost)
openclaw agents add hustle-bot --workspace "$BASE/hustle-bot" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: hustle-bot" || echo "SKIP: hustle-bot"
openclaw agents add product-scout --workspace "$BASE/product-scout" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: product-scout" || echo "SKIP: product-scout"
openclaw agents add content-builder --workspace "$BASE/content-builder" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: content-builder" || echo "SKIP: content-builder"
openclaw agents add social-media-bot --workspace "$BASE/social-media-bot" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: social-media-bot" || echo "SKIP: social-media-bot"
openclaw agents add email-bot --workspace "$BASE/email-bot" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: email-bot" || echo "SKIP: email-bot"
openclaw agents add designer --workspace "$BASE/designer" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: designer" || echo "SKIP: designer"
openclaw agents add order-manager --workspace "$BASE/order-manager" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: order-manager" || echo "SKIP: order-manager"
openclaw agents add customer-service --workspace "$BASE/customer-service" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: customer-service" || echo "SKIP: customer-service"
openclaw agents add analytics-bot --workspace "$BASE/analytics-bot" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: analytics-bot" || echo "SKIP: analytics-bot"

# R&D Researchers
openclaw agents add trading-researcher --workspace "$BASE/trading-researcher" --model "anthropic/claude-sonnet-4-6" --non-interactive --json 2>/dev/null && echo "OK: trading-researcher" || echo "SKIP: trading-researcher"
openclaw agents add crypto-researcher --workspace "$BASE/crypto-researcher" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: crypto-researcher" || echo "SKIP: crypto-researcher"
openclaw agents add realestate-researcher --workspace "$BASE/realestate-researcher" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: realestate-researcher" || echo "SKIP: realestate-researcher"
openclaw agents add ai-tech-researcher --workspace "$BASE/ai-tech-researcher" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: ai-tech-researcher" || echo "SKIP: ai-tech-researcher"
openclaw agents add business-researcher --workspace "$BASE/business-researcher" --model "anthropic/claude-haiku-4-5" --non-interactive --json 2>/dev/null && echo "OK: business-researcher" || echo "SKIP: business-researcher"

echo ""
echo "=== Listing all agents ==="
openclaw agents list
echo ""
echo "=== Done! ==="
