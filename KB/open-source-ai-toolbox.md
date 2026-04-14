# Money-Saving AI Toolbox — Smart Vault Co. LLC
## Cut Paid Subscriptions with HuggingFace, OpenRouter, Open-Source & Self-Hosted Tools
## Last Updated: 2026-04-12

---

## Current Paid Stack (What We're Replacing)

| Tool | Monthly Cost | What It Does |
|------|-------------|--------------|
| ChatGPT Plus | $20/mo | Text generation, brainstorming |
| Midjourney | $10-60/mo | AI image generation |
| ElevenLabs | $5-99/mo | Text-to-speech, voice cloning |
| Otter AI / AssemblyAI | $10-30/mo | Transcription |
| Google Veo 3 / Luma | $20-50/mo | Video generation |
| Mailchimp | $13-350/mo | Email marketing |
| Calendly | $12-20/mo | Scheduling |
| DocuSign | $15-65/mo | Document signing |
| Buffer | $6-120/mo | Social media scheduling |
| **Estimated Total** | **$130-800+/mo** | |

---

## SECTION 1: TEXT GENERATION (Replace ChatGPT Plus — Save $20/mo)

### Option A: OpenRouter (Recommended — Use Today)

OpenRouter is a single API gateway that routes to 300+ models from every major provider. One API key, one billing account, pay-per-token only for what you use.

**Why it matters:** Instead of paying $20/mo for ChatGPT Plus (whether you use it or not), you pay only for actual tokens consumed. Most Smart Vault workflows will cost $2-8/mo.

| Model | Input/1M Tokens | Output/1M Tokens | Best For |
|-------|----------------|------------------|----------|
| Claude Sonnet 4.6 | $3.00 | $15.00 | Strategy, complex reasoning, boss agents |
| Claude Haiku 4.5 | ~$0.80 | ~$4.00 | Worker agents, fast tasks |
| DeepSeek V3.2 | $0.14 | $0.28 | Bulk writing, ebook chapters, email sequences |
| DeepSeek R1 | FREE | FREE | Research, brainstorming (rate limited) |
| Llama 4 Maverick | $0.15 | $0.60 | General writing, ad copy |
| Gemma 3 | FREE | FREE | Light tasks, summaries |
| Qwen 3 | ~$0.20 | ~$0.60 | Multilingual content, code |

**Setup (5 minutes):**
1. Go to https://openrouter.ai — sign up
2. Add $10 credits (lasts weeks for most use cases)
3. Get your API key
4. Use in n8n HTTP Request nodes, or any OpenAI-compatible client
5. Endpoint: `https://openrouter.ai/api/v1/chat/completions`

**Best models by Smart Vault use case:**
- Ebook chapter writing: DeepSeek V3.2 ($0.14/1M in) — write a full chapter for under $0.01
- Ad copy generation: Llama 4 Maverick or Claude Haiku 4.5
- Email sequences: DeepSeek V3.2 (bulk) or Claude Sonnet (quality)
- Code generation: Claude Sonnet 4.6 or Claude Opus 4.6
- Research summaries: DeepSeek R1 (FREE)

**Status: READY TODAY** | Savings: ~$15-18/mo vs ChatGPT Plus

---

### Option B: HuggingFace Inference API (Free Tier)

HuggingFace offers free inference for thousands of models. Rate-limited but functional for testing and light use.

**Top free models on HuggingFace:**
- `meta-llama/Llama-3.3-70B-Instruct` — strong general-purpose
- `Qwen/Qwen3-72B` — excellent for structured outputs
- `mistralai/Mixtral-8x22B-Instruct-v0.1` — fast, good for bulk tasks

**Setup:** Sign up at https://huggingface.co, get a free API token, call the Inference API.

**Status: READY TODAY** | Cost: $0 (rate limited)

---

## SECTION 2: IMAGE GENERATION (Replace Midjourney — Save $10-60/mo)

### Option A: FLUX (Best Quality — Recommended)

FLUX by Black Forest Labs (the team behind Stable Diffusion) produces photorealistic images that rival or beat Midjourney. Open-source, no subscription, no Discord required.

**Models:**
- **FLUX.1 [schnell]** — Fast generation (4.5 sec), free, open-source
- **FLUX.1 [dev]** — Higher quality, free for non-commercial, open weights
- **FLUX.1 [pro]** — Best quality, API access via BFL or third parties

**How to access:**
1. **HuggingFace Spaces** (free, browser-based): Search "FLUX" on huggingface.co/spaces
2. **ComfyUI locally** (free, unlimited): Install ComfyUI + download FLUX model weights
3. **Replicate/fal.ai API** (~$0.003/image): For n8n integration
4. **Myjourney.so** ($3/mo for 100 images vs Midjourney's $10/mo)

**Quality:** Handles hands, eyes, and text in images better than Midjourney V6. In 2026, people regularly cannot tell FLUX output from real photography.

**Status: READY TODAY** | Savings: $10-57/mo vs Midjourney

### Option B: Stable Diffusion 3.5 (Full Local Control)

Completely free, runs on your own GPU (8GB+ VRAM needed). No usage limits. SDXL and SD 3.5 produce images that rival Midjourney with the right settings and LoRA models.

**Setup:** Install via ComfyUI, Automatic1111, or Fooocus (easiest).

**Status: READY TODAY (if GPU available)** | Cost: $0

---

## SECTION 3: VOICE & TTS (Replace ElevenLabs — Save $5-99/mo)

### Option A: Chatterbox (Best Quality — Recommended)

Open-source TTS that **wins blind tests against ElevenLabs** (63.8% listener preference). MIT licensed. Clones any voice from 5 seconds of audio. Supports 17 languages.

**Setup:**
```bash
pip install chatterbox-tts
# Clone a voice from a 5-second sample, generate speech
```

**Status: READY TODAY** | Cost: $0

### Option B: Qwen3-TTS

Alibaba's latest TTS model. Full voice cloning, voice design, high-quality synthesis. Available in 0.6B and 1.7B sizes. 10 languages including English.

**Access:** HuggingFace model hub — `Qwen/Qwen3-TTS-1.7B`

**Status: READY TODAY** | Cost: $0

### Option C: Kokoro (Lightweight)

Only 82M parameters but delivers quality comparable to much larger models. Fast, efficient, runs on minimal hardware.

**Best for:** Real-time TTS in chatbots, voice agents, course narration.

**Status: READY TODAY** | Cost: $0

### Option D: Fish Speech 1.6

Ranks #1 on TTS-Arena blind tests. Open-source self-hosted option available. Also has a paid cloud tier at a fraction of ElevenLabs pricing.

**Status: READY TODAY** | Cost: $0 (self-hosted) or low-cost cloud

### Additional Options:
- **Bark** — Best for expressive/emotional speech with natural laughter, hesitations
- **Coqui XTTS v2.5** — Gold standard for voice cloning with 6-second reference audio
- **Piper** — Fastest, runs on Raspberry Pi, ideal for edge deployment
- **StyleTTS2** — Most natural prosody for audiobook narration

---

## SECTION 4: TRANSCRIPTION (Replace Otter AI — Save $10-30/mo)

### OpenAI Whisper (Self-Hosted)

Open-source (MIT license), 95%+ accuracy, supports 99 languages. Runs completely offline for maximum privacy.

**Models (pick based on your hardware):**
| Model | Size | VRAM | Accuracy |
|-------|------|------|----------|
| tiny | 39M | ~1GB | Good for drafts |
| base | 74M | ~1GB | Decent |
| small | 244M | ~2GB | Good |
| medium | 769M | ~5GB | Great |
| large-v3 | 1.5B | ~10GB | Best (95%+) |

**Setup:**
```bash
pip install openai-whisper
whisper audio.mp3 --model medium --output_format txt
```

**For a GUI experience:** Use **Whispering** (free, open-source desktop app) or **OpenWispr** (cross-platform).

**Limitation:** No built-in speaker diarization or AI summaries. For meeting notes, pair Whisper transcription with a DeepSeek summary via OpenRouter.

**n8n Integration:** Run Whisper in a Docker container, trigger via n8n webhook when audio files land in a folder.

**Status: READY TODAY** | Cost: $0 | Savings: $10-30/mo

---

## SECTION 5: VIDEO GENERATION (Replace Paid Video Tools — Save $20-50/mo)

### Tier 1: Seedance 2.0 (Best Quality — ByteDance)

ByteDance's flagship video model. Ranked #1 on Artificial Analysis (Elo 1,269), beating Google Veo 3, OpenAI Sora 2, and Runway Gen-4.5.

**Capabilities:**
- Text-to-video, image-to-video, video-to-video
- Accepts up to 12 input assets (text, images, audio, video) in a single generation
- Cinematic multi-shot video with native audio sync
- Consistent characters across shots
- Realistic physics simulation

**How to access (April 2026):**
1. **CapCut** — Seedance 2.0 is integrated into CapCut (ByteDance's editor). Limited free tier.
2. **Higgsfield.ai** — Log in, select Seedance 2.0, generate immediately. Plans start low.
3. **fal.ai API** — Seedance 2.0 API live as of April 9, 2026. Pay-per-generation.
4. **Official API** — Global launch expected Q2 2026 for production pipelines.
5. **HuggingFace** — ByteDance-Seed organization page exists; check for open weights.

**Use cases for Smart Vault:**
- Ad creative (30-45 sec promo clips)
- Course promos and testimonial-style videos
- Social media content (TikTok, Reels, Shorts)
- Product demos for e-commerce

**Status: AVAILABLE NOW (via CapCut, Higgsfield, fal.ai)** | Cost: Pay-per-use, much cheaper than Runway/Sora subscriptions

### Tier 2: Wan Video 2.2 (Best Open-Source)

Most cinematic open-source video model available. Mixture-of-Experts diffusion backbone. Fully open weights on HuggingFace.

**Access:** Download from HuggingFace, run via ComfyUI or Diffusers library.
**Requirement:** Needs a beefy GPU (24GB+ VRAM recommended).

**Status: READY TODAY (if GPU available)** | Cost: $0

### Tier 3: CogVideoX-5B (Reliable Open-Source)

Generates 6-10 second clips at 720p. Solid quality, well-documented, easy HuggingFace integration.

**Access:** `huggingface.co/THUDM/CogVideoX-5b` — load with Diffusers in a few lines of Python.

**Status: READY TODAY** | Cost: $0

### Cloud GPU Option (No Local GPU)

If you lack a local GPU, use RunPod or Vast.ai to rent GPU time:
- ~$0.20-0.50/hr for an A100 — generate dozens of videos per hour
- Much cheaper than Runway ($15-76/mo) or Sora ($20-200/mo)

---

## SECTION 6: SELF-HOSTED TOOLS (Replace SaaS Subscriptions)

### 6A. Listmonk — Replace Mailchimp (Save $13-350/mo)

High-performance, self-hosted email marketing. Single binary, handles 100K+ subscribers on a $5/mo VPS.

**Features:**
- Single and double opt-in lists
- SQL-based subscriber segmentation
- Multi-threaded, multi-SMTP email queues
- Built-in analytics (opens, clicks, bounces)
- Campaign scheduling
- Template system (HTML, Markdown, Go templates)

**Setup:**
```bash
# Docker (recommended)
docker run -p 9000:9000 listmonk/listmonk
# Connect to PostgreSQL, configure SMTP (Amazon SES = $0.10/1000 emails)
```

**Limitation:** No drag-and-drop visual editor. Use HTML templates or Markdown.

**Pair with Amazon SES:** $0.10 per 1,000 emails. Sending 10,000 emails/mo = $1.00 vs Mailchimp's $100+/mo.

**Status: READY TODAY** | Setup: 1-2 hours | Savings: $13-350/mo

---

### 6B. Cal.com — Replace Calendly (Save $12-20/mo)

Open-source scheduling platform. More features on the free tier than Calendly's paid plan.

**Free tier includes:**
- Unlimited bookings
- Unlimited calendar connections
- Integrations (Google Calendar, Zoom, etc.)
- Custom booking pages
- API access

**Self-hosting:** Full code on GitHub, deploy with Docker. White-label ready.
**Cloud free tier:** cal.com offers a generous free plan if you don't want to self-host.

**Status: READY TODAY** | Setup: 30 min (cloud) or 1-2 hours (self-hosted) | Savings: $12-20/mo

---

### 6C. DocuSeal — Replace DocuSign (Save $15-65/mo)

Open-source document signing. Create, fill, and sign digital documents.

**Features:**
- Step-by-step signing forms (works on any device)
- API and webhook integration
- Embeddable signing forms for websites
- Self-hosted with Docker (SQLite, PostgreSQL, or MySQL)

**Setup:**
```bash
docker run -p 3000:3000 docuseal/docuseal
```

**Status: READY TODAY** | Setup: 30 min | Savings: $15-65/mo

---

### 6D. Ghost — Blog + Newsletter Platform (Replace WordPress + Mailchimp Combo)

Professional open-source publishing with built-in newsletters, memberships, and Stripe payments.

**Features:**
- Blog posts + email newsletters in one platform
- Native Stripe integration for paid memberships (free, paid monthly, paid annual tiers)
- Content gating, member segmentation
- SEO-optimized, loads in 200-500ms (vs WordPress 800-2000ms)
- Built-in analytics

**Self-hosting:** Docker compose, or deploy on a $5-10/mo VPS.

**Status: READY TODAY** | Setup: 1-2 hours | Potential savings: Replaces WordPress hosting + newsletter tool

---

### 6E. Plausible Analytics — Replace/Supplement GA4

Lightweight, cookie-free, GDPR-compliant web analytics. No cookie consent banner needed.

**Self-hosting:** Plausible Community Edition (free, AGPL licensed). Docker deployment.

**Note:** GA4 is free, so this is about simplicity and privacy rather than cost savings. Plausible's dashboard is dramatically simpler and faster than GA4.

**Status: READY TODAY** | Setup: 1 hour | Cost: $0 (self-hosted)

---

### 6F. n8n — Already Using (Keep It)

You already self-host n8n for complex automation logic. This is your automation backbone. No changes needed.

**Reminder:** n8n can integrate with ALL the tools in this document via HTTP Request nodes:
- OpenRouter API for text generation
- Whisper Docker container for transcription
- FLUX via Replicate/fal.ai API for image generation
- Listmonk API for email campaigns
- Cal.com API for booking management

---

## SECTION 7: TOTAL SAVINGS BREAKDOWN

| Paid Tool | Monthly Cost | Free/Cheaper Alternative | New Cost | Monthly Savings |
|-----------|-------------|-------------------------|----------|-----------------|
| ChatGPT Plus | $20 | OpenRouter (pay-per-token) | ~$3-5 | **$15-17** |
| Midjourney | $10-60 | FLUX (HuggingFace/local) | $0-3 | **$10-57** |
| ElevenLabs | $5-99 | Chatterbox / Qwen3-TTS | $0 | **$5-99** |
| Otter AI | $10-30 | Whisper (local) | $0 | **$10-30** |
| Video tools (Runway/Sora) | $20-76 | Seedance 2.0 (fal.ai) + Wan 2.2 | $0-10 | **$10-66** |
| Mailchimp | $13-350 | Listmonk + Amazon SES | $1-6 | **$12-344** |
| Calendly | $12-20 | Cal.com (free tier or self-host) | $0 | **$12-20** |
| DocuSign | $15-65 | DocuSeal | $0 | **$15-65** |
| | | | | |
| **TOTAL RANGE** | **$105-720/mo** | | **$4-24/mo** | **$89-698/mo** |

**Conservative estimate: Save $150-300/mo ($1,800-3,600/yr)**
**Aggressive estimate: Save $400-700/mo ($4,800-8,400/yr)**

---

## SECTION 8: IMPLEMENTATION PRIORITY

### Phase 1 — Do This Week (No Setup Required)
1. **Sign up for OpenRouter** — add $10 credits, start routing LLM calls through it
2. **Try FLUX on HuggingFace Spaces** — free, browser-based, test image quality
3. **Sign up for Cal.com free tier** — replace Calendly immediately
4. **Try Seedance 2.0 via CapCut or Higgsfield** — test video generation quality

### Phase 2 — This Month (Light Setup)
5. **Install Whisper locally** — `pip install openai-whisper`, start transcribing
6. **Install Chatterbox TTS** — test voice cloning quality against ElevenLabs
7. **Deploy Listmonk** — Docker container + Amazon SES SMTP setup
8. **Deploy DocuSeal** — single Docker command

### Phase 3 — When Needed (Heavier Setup)
9. **Set up ComfyUI locally** — unlimited FLUX + Stable Diffusion image generation
10. **Deploy Ghost** — if building a blog/newsletter platform for Smart Vault HQ
11. **Run Wan 2.2 / CogVideoX locally** — requires 24GB+ VRAM GPU
12. **Deploy Plausible Analytics** — when privacy-first analytics becomes a priority

---

## SECTION 9: QUICK REFERENCE — WHERE TO FIND EVERYTHING

| Tool | URL | Type |
|------|-----|------|
| OpenRouter | https://openrouter.ai | API gateway (300+ models) |
| HuggingFace | https://huggingface.co | Models, Spaces, datasets |
| FLUX | https://huggingface.co/black-forest-labs | Image generation |
| Chatterbox TTS | https://github.com/resemble-ai/chatterbox | Voice synthesis |
| Qwen3-TTS | https://huggingface.co/Qwen/Qwen3-TTS-1.7B | Voice synthesis |
| Kokoro TTS | https://huggingface.co/hexgrad/Kokoro-82M | Lightweight TTS |
| Fish Speech | https://github.com/fishaudio/fish-speech | Voice synthesis |
| Whisper | https://github.com/openai/whisper | Transcription |
| Seedance 2.0 | https://fal.ai/seedance-2.0 | Video generation (API) |
| Seedance 2.0 | https://higgsfield.ai/seedance/2.0 | Video generation (UI) |
| Wan 2.2 | https://huggingface.co/Wan-AI | Video generation (open) |
| CogVideoX | https://huggingface.co/THUDM/CogVideoX-5b | Video generation (open) |
| Listmonk | https://listmonk.app | Email marketing |
| Cal.com | https://cal.com | Scheduling |
| DocuSeal | https://docuseal.com | Document signing |
| Ghost | https://ghost.org | Blog + newsletter |
| Plausible | https://plausible.io | Web analytics |
| ComfyUI | https://github.com/comfyanonymous/ComfyUI | Local AI image/video UI |

---

## SECTION 10: n8n INTEGRATION PATTERNS

These tools plug directly into your existing n8n automation backbone:

**Pattern 1: Content Engine**
Whisper (transcribe pillar video) → OpenRouter/DeepSeek (generate blog post, email, social posts) → Listmonk (send newsletter) → Buffer API (schedule social)

**Pattern 2: Ad Creative Pipeline**
OpenRouter/Claude (write ad copy) → FLUX via fal.ai API (generate visuals) → Seedance 2.0 via fal.ai (generate video ad) → Chatterbox (add voiceover) → Output to Meta/TikTok ad manager

**Pattern 3: Lead Nurture Automation**
Cal.com webhook (new booking) → OpenRouter (personalize follow-up) → Listmonk (send nurture sequence) → DocuSeal (send contract for signing)

**Pattern 4: Course Production**
Whisper (transcribe lecture) → OpenRouter/DeepSeek (generate chapters, summaries, quizzes) → Chatterbox (narrate written content) → CogVideoX/Wan (generate supplemental video clips)

---

*This document is a living reference. Update pricing and model recommendations quarterly as the open-source landscape moves fast.*
