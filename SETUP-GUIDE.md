# SMART VAULT CO. — FULL SETUP GUIDE
## Telegram + Discord + 24/7 Operation

---

## STEP 1: CREATE YOUR TELEGRAM BOTS (10 minutes)

You need 3 bots — one for each boss agent you talk to directly.

### Open Telegram → Search @BotFather → Start

**Bot 1 — CEO Bot (main interface)**
```
Send: /newbot
Name: Smart Vault CEO
Username: smartvaultceo_bot  (must end in _bot, must be unique)
→ BotFather gives you a token. Copy it.
→ Paste into .env: TELEGRAM_CEO_BOT_TOKEN=your_token_here
```

**Bot 2 — Trading Bot**
```
Send: /newbot
Name: Smart Vault Trading
Username: smartvaulttrading_bot
→ Copy token
→ Paste into .env: TELEGRAM_TRADING_BOT_TOKEN=your_token_here
```

**Bot 3 — Real Estate Bot**
```
Send: /newbot
Name: Smart Vault RE
Username: smartvaultre_bot
→ Copy token
→ Paste into .env: TELEGRAM_RE_BOT_TOKEN=your_token_here
```

**Then in BotFather:**
```
/setprivacy → select your bot → Disable
(This allows the bot to read messages in groups, not just DMs)
```

**Start each bot:**
- Search the bot username in Telegram
- Press Start
- The bot is now ready to receive your messages

---

## STEP 2: CREATE YOUR DISCORD BOT (optional — for alerts + group visibility)

### Go to discord.com/developers/applications

1. Click "New Application" → Name it "Smart Vault Gateway"
2. Go to "Bot" tab → Click "Add Bot"
3. Under Token → Click "Reset Token" → Copy the token
4. Paste into .env: `DISCORD_BOT_TOKEN=your_token_here`
5. Under "Privileged Gateway Intents" → Enable:
   - Message Content Intent ✅
   - Server Members Intent ✅
6. Go to "OAuth2" → "URL Generator"
   - Scopes: bot
   - Permissions: Send Messages, Read Messages, Use Slash Commands, Embed Links
7. Copy the generated URL → Paste in browser → Add to your Discord server
8. Paste your server ID into .env: `DISCORD_SERVER_ID=your_server_id`
9. Create channels in Discord:
   - #ceo-channel
   - #trading-alerts
   - #real-estate-alerts
   - #hustle-opportunities
   - #analytics-daily
   - #system-logs

---

## STEP 3: INSTALL OPENCLAW GATEWAY

The OpenClaw gateway is the Node.js server that listens on port 18789 and connects your bots to Claude.

### Clone the Claw3D repo:
```bash
cd F:/
git clone https://github.com/iamlukethedev/Claw3D
cd Claw3D
npm install
```

### Link your config:
```bash
# Copy your Smart Vault config into Claw3D
cp f:/Smart-Vault-Ai/openclaw.json F:/Claw3D/openclaw.json
cp f:/Smart-Vault-Ai/.env F:/Claw3D/.env
```

### Test it runs:
```bash
npm start
# Should show: Gateway listening on port 18789
# Should show: Connected to Telegram — CEO bot
# Should show: Connected to Telegram — Trading bot
# Should show: Connected to Telegram — RE bot
```

### Send a test message:
- Open Telegram → your smartvaultceo_bot → send "hello"
- CEO bot should respond

---

## STEP 4: RUN 24/7 WITH PM2 (Windows)

PM2 is a process manager that keeps your bots running even after you close the terminal or restart your PC.

### Install PM2:
```bash
npm install -g pm2
npm install -g pm2-windows-startup
```

### Create the PM2 config:
File: `F:/Claw3D/ecosystem.config.js` (already created — see below)

### Start with PM2:
```bash
cd F:/Claw3D
pm2 start ecosystem.config.js
pm2 save                      # Save process list
pm2-startup install           # Auto-start on Windows boot
```

### Useful PM2 commands:
```bash
pm2 status                    # See all running bots
pm2 logs smart-vault-gateway  # View live logs
pm2 restart smart-vault-gateway
pm2 stop smart-vault-gateway
pm2 monit                     # Dashboard view
```

---

## STEP 5: CLOUD DEPLOYMENT (True 24/7 — Recommended)

Running on your local PC means bots stop when PC sleeps. For real 24/7, deploy to cloud.

### Option A: Railway (Easiest — free to start)
1. Go to railway.app → New Project → Deploy from GitHub repo
2. Select Claw3D repo
3. Add environment variables (paste from .env)
4. Railway auto-deploys on every git push
5. Always on — $5/month after free tier

### Option B: DigitalOcean Droplet ($5/month)
```bash
# On DigitalOcean — create Ubuntu 22.04 droplet ($5/month)
# SSH in:
ssh root@your_droplet_ip

# Install Node.js:
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
apt install -y nodejs

# Clone + install:
git clone https://github.com/iamlukethedev/Claw3D
cd Claw3D
npm install

# Add your .env (paste keys)
nano .env

# Start with PM2:
npm install -g pm2
pm2 start ecosystem.config.js
pm2 save
pm2 startup systemd
```

### Option C: Render (Free tier — may sleep after inactivity)
1. render.com → New Web Service → Connect GitHub
2. Build command: `npm install`
3. Start command: `npm start`
4. Add env vars → Deploy

---

## STEP 6: VERIFY EVERYTHING WORKS

### Checklist:
- [ ] Telegram CEO bot responds to messages
- [ ] Telegram Trading bot responds to trading questions
- [ ] Telegram RE bot responds to real estate questions
- [ ] Discord bot is in your server and posts to #system-logs on startup
- [ ] PM2 shows `online` status for smart-vault-gateway
- [ ] After PC restart: bots still running (PM2 startup worked)
- [ ] Hustle Bot posts opportunity report every 6 hours to Discord #hustle-opportunities
- [ ] Analytics Bot posts daily scorecard at 6AM to Discord #analytics-daily

---

## STEP 7: ADD TELEGRAM CHANNEL IDs TO .env

After starting the bots, you need to tell each bot which Telegram chat to send proactive messages to.

1. Open each bot in Telegram → Send it any message
2. Go to: `https://api.telegram.org/bot{YOUR_TOKEN}/getUpdates`
3. Find "chat":{"id": XXXXXXXXX} — that's your chat ID
4. Add to .env:
```
TELEGRAM_CEO_CHAT_ID=        # Your chat ID with CEO bot
TELEGRAM_TRADING_CHAT_ID=    # Your chat ID with Trading bot
TELEGRAM_RE_CHAT_ID=         # Your chat ID with RE bot
```

These IDs let bots proactively message you (daily reports, alerts, opportunities).

---

## TROUBLESHOOTING

**Bot not responding:**
- Check TELEGRAM_*_BOT_TOKEN is correct in .env
- Check ANTHROPIC_API_KEY is set
- Run `pm2 logs` and check for errors

**Port 18789 already in use:**
- `netstat -ano | findstr 18789`
- `taskkill /PID [pid_number] /F`

**Bot crashes after a few messages:**
- Usually API rate limit — check Anthropic API dashboard
- Or missing .env variable — check pm2 logs for "undefined" errors

**Bots work locally but not on cloud:**
- Make sure all .env vars are added to cloud platform (Railway/DigitalOcean)
- Check cloud platform logs for startup errors
