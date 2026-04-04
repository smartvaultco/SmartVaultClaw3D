---
name: remotion
description: Professional motion graphics video production workflow using React and Remotion. Creates promotional videos, product demos, social media content, and animated explainers with AI voiceover, captions, and Cloudflare tunnel for live preview.
triggers:
  - /remotion
  - create a video
  - make a video
  - remotion video
  - motion graphics
---

# Video Generator (Remotion)

## Default Workflow (MANDATORY SEQUENCE)

1. **Scrape brand data** via Firecrawl (if featuring a product)
2. **Create project** in `output/<project-name>/`
3. **Build all scenes** with motion graphics
4. **Install dependencies** with `npm install`
5. **Fix package.json scripts** to use `npx remotion` (not `bun`)
6. **Start Remotion Studio** as background process
7. **Expose via Cloudflare tunnel** for public access
8. **Send user the public URL**

Rendering happens only when the user explicitly requests export.

## Quick Start Setup

Manual scaffolding (avoiding interactive CLI blocking):

```bash
mkdir -p output/my-video/src/scenes output/my-video/public/audio output/my-video/public/images
cd output/my-video
```

Create `package.json` with Remotion 4.0.293, React 19, and dependencies like lucide-react.

```bash
npm install
npm run dev
bash skills/cloudflare-tunnel/scripts/tunnel.sh start 3000
```

## Brand Data Collection with Firecrawl

**Mandatory when featuring products:** Scrape websites for brandName, tagline, colors, logos, screenshots, and copy before design.

```bash
bash scripts/firecrawl.sh "https://example.com"
```

Downloads assets to `public/images/brand/` directory.

## Core Architecture

### Scene Management with Timing

Define scene durations in a record structure:

```
intro: 3s, problem: 4s, solution: 3.5s, features: 5s, cta: 3s
```

### Video Structure Pattern

Use `AbsoluteFill`, `Sequence`, and interpolation for motion. Place background music and persistent layers outside sequence blocks. Audio uses `staticFile()` references.

## Motion Graphics Principles

### AVOID
- Fading to black between scenes
- Centered text on solid backgrounds
- Linear animations
- Static screens
- Emoji icons (use Lucide React instead)
- Preset transitions like slideLeft or crossDissolve

### PURSUE
- Overlapping transitions (next starts before current ends)
- Layered compositions (background/midground/foreground)
- Spring physics for organic motion
- Varied timing (2-5s scenes with mixed rhythms)
- Continuous visual elements across scenes
- Custom transitions (morph, wipe, zoom-through, clip-path reveal, perspective flip)
- Lucide React icons exclusively

## Transition Techniques

1. **Morph/Scale** — Element scales to fill, becomes next background
2. **Wipe** — Shape sweeps revealing next scene
3. **Zoom-through** — Camera pushes into element, emerges into new scene
4. **Clip-path reveal** — Circle/polygon grows from point
5. **Persistent anchor** — One element stays while surroundings change
6. **Directional flow** — Scene exits right, next enters from right
7. **Split/unfold** — Screen divides, panels slide apart
8. **Perspective flip** — Scene rotates on Y-axis in 3D

## Animation Timing Reference

- **Micro:** 0.1–0.2s (small shifts)
- **Snappy:** 0.2–0.4s (entrances, position changes)
- **Standard:** 0.5–0.8s (transitions, reveals)
- **Dramatic:** 1.0–1.5s (hero moments, cinematic)

Spring configs vary: snappy (stiffness 400, damping 30), bouncy (300, 15), smooth (120, 25).

## Visual Style Guidelines

### Typography
- One display + one body font maximum
- Massive headlines with tight tracking
- Mix weights for hierarchy
- Keep text SHORT (viewers can't pause)

### Colors
- Use brand colors from Firecrawl scrape as primary palette
- Avoid purple/indigo gradients unless brand-appropriate
- Simple, clean backgrounds (single dark tone or subtle gradient)
- Intentional accent colors pulled from brand

### Layout
- Asymmetric layouts, off-center type
- Edge-aligned elements create tension
- Generous whitespace as design element
- Subtle depth (backdrop blur or single gradient, not stacked textures)

## Remotion Essentials

### Interpolation
```tsx
const opacity = interpolate(frame, [0, 30], [0, 1], {
  extrapolateLeft: "clamp",
  extrapolateRight: "clamp",
});

const scale = spring({
  frame,
  fps,
  from: 0.8,
  to: 1,
  durationInFrames: 30,
  config: { damping: 12 },
});
```

### Sequence Overlap
Start next sequence before current ends for smooth transitions.

### Cross-Scene Continuity
Place persistent elements outside Sequence blocks and animate their properties based on current scene state.

## Quality Tests Before Delivery

- **Mute test:** Story follows visually without sound?
- **Squint test:** Hierarchy visible when squinting?
- **Timing test:** Motion feels natural?
- **Consistency test:** Similar elements behave similarly?
- **Slideshow test:** Does NOT look like PowerPoint?
- **Loop test:** Video loops smoothly?

## Implementation Steps (Complete Pipeline)

1. Firecrawl brand scrape (if product-focused)
2. Director's treatment (vibe, camera style, emotional arc)
3. Visual direction (colors, fonts, animation style)
4. Scene breakdown (each scene with description, duration, text, transitions)
5. Define scene durations (vary pacing)
6. Create `styles.ts` (unified type scale, colors, fonts—prevents sizing inconsistency)
7. Build persistent layer (animated background outside scenes)
8. Build scenes (with enter/exit animations, 3-5 timed moments each)
9. Start Remotion Studio (`npm run dev`, expose via tunnel, send URL)
10. Iterate with user (edit source, hot-reload)
11. Generate voiceover (Gemini TTS)
12. Add transcription (timed captions)
13. Sync audio-visual (match timings to voiceover duration)
14. Render (only when user exports: `npx remotion render CompositionName out/video.mp4`)

## File Structure

```
my-video/
├── src/
│   ├── Root.tsx
│   ├── index.ts
│   ├── styles.ts (CRITICAL - shared colors, fonts, type scale)
│   ├── MyVideo.tsx (main composition)
│   ├── Transcription.tsx (timed captions)
│   └── scenes/ (one file per scene)
├── public/
│   ├── images/brand/ (Firecrawl assets)
│   └── audio/ (voiceover.wav)
├── out/ (rendered output, gitignored)
├── remotion.config.ts
└── package.json
```

## AI Voiceover with Gemini TTS

Available models: `gemini-2.5-flash-preview-tts` (fast, good) and `gemini-2.5-pro-preview-tts` (best quality).

Standard Gemini models do NOT support audio output—use dedicated `-tts` models only.

Voice options: Orus, Kore, Puck, Charon, Fenrir, Leda, Aoede, Zephyr. Best for narration: Orus (warm, authoritative) or Kore (clear, friendly).

### Generation Script
```bash
export GEMINI_API_KEY="your-key"

curl -s "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-pro-preview-tts:generateContent?key=$GEMINI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [{"parts": [{"text": "Your narration script here..."}]}],
    "generationConfig": {
      "response_modalities": ["AUDIO"],
      "speech_config": {
        "voiceConfig": {
          "prebuiltVoiceConfig": { "voiceName": "Orus" }
        }
      }
    }
  }' | python3 -c "
import json, sys, base64
r = json.load(sys.stdin)
audio = r['candidates'][0]['content']['parts'][0]['inlineData']['data']
sys.stdout.buffer.write(base64.b64decode(audio))
" > voiceover_raw.pcm

ffmpeg -f s16le -ar 24000 -ac 1 -i voiceover_raw.pcm public/audio/voiceover.wav
rm voiceover_raw.pcm

ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 public/audio/voiceover.wav
```

Gemini outputs s16le PCM at 24kHz, mono. Convert to WAV format with ffmpeg.

## Audio-Visual Sync

Add small offset so visuals appear before voice starts:

```tsx
const AUDIO_OFFSET = 15; // 0.5s at 30fps

<Sequence from={AUDIO_OFFSET}>
  <Audio src={staticFile("audio/voiceover.wav")} volume={0.9} />
</Sequence>
```

Calculate total frames: `Math.ceil(duration * fps) + AUDIO_OFFSET`

## Transcription Overlay

Add timed captions synced to voiceover with adaptive fade:

```tsx
const LINES: { start: number; end: number; text: string }[] = [
  { start: 20, end: 140, text: "First caption line." },
  { start: 155, end: 230, text: "Second caption line." },
];

export const Transcription: React.FC = () => {
  const frame = useCurrentFrame();
  const activeLine = LINES.find((l) => frame >= l.start && frame <= l.end);
  if (!activeLine) return null;

  const dur = activeLine.end - activeLine.start;
  const fade = Math.min(10, Math.floor(dur / 3));

  const opacity = interpolate(
    frame,
    [
      activeLine.start,
      activeLine.start + fade,
      activeLine.end - fade,
      activeLine.end,
    ],
    [0, 1, 1, 0],
    { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
  );

  return (
    <div style={{
      position: "absolute",
      bottom: 56,
      left: 0,
      right: 0,
      display: "flex",
      justifyContent: "center",
      opacity,
      pointerEvents: "none",
    }}>
      <div style={{
        padding: "14px 36px",
        borderRadius: 14,
        background: "rgba(0,0,0,0.6)",
        backdropFilter: "blur(16px)",
      }}>
        <span style={{ fontSize: 26, fontWeight: 500, color: "#fff" }}>
          {activeLine.text}
        </span>
      </div>
    </div>
  );
};
```

## Unified Type Scale (CRITICAL)

**ALWAYS define shared type scale in `styles.ts`**—never set font sizes inline.

```tsx
// styles.ts
export const colors = {
  bg: "#0a0a0f",
  textPrimary: "rgba(255,255,255,0.95)",
  textSecondary: "rgba(255,255,255,0.55)",
  textDim: "rgba(255,255,255,0.3)",
};

export const fonts = {
  sans: "Inter, system-ui, sans-serif",
  mono: "'JetBrains Mono', monospace",
};

export const type = {
  hero: { fontSize: 96, fontWeight: 700, letterSpacing: "-0.04em", lineHeight: 1.05 },
  h1: { fontSize: 68, fontWeight: 700, letterSpacing: "-0.035em", lineHeight: 1.1 },
  h2: { fontSize: 48, fontWeight: 600, letterSpacing: "-0.025em", lineHeight: 1.2 },
  body: { fontSize: 28, fontWeight: 400, letterSpacing: "-0.01em", lineHeight: 1.5 },
  bodyLg: { fontSize: 34, fontWeight: 400, letterSpacing: "-0.015em", lineHeight: 1.4 },
  stat: { fontSize: 86, fontWeight: 800, letterSpacing: "-0.04em", lineHeight: 1 },
  label: { fontSize: 18, fontWeight: 600, letterSpacing: "0.08em", textTransform: "uppercase" },
  mono: { fontSize: 22, fontWeight: 500, fontFamily: "'JetBrains Mono', monospace" },
};
```

## Tunnel Management

```bash
bash skills/cloudflare-tunnel/scripts/tunnel.sh start 3000
bash skills/cloudflare-tunnel/scripts/tunnel.sh status 3000
bash skills/cloudflare-tunnel/scripts/tunnel.sh list
bash skills/cloudflare-tunnel/scripts/tunnel.sh stop 3000
```
