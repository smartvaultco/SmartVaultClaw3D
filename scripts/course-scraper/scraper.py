"""
Smart Vault Co. - Course Scraper
Logs into Kajabi/Kartra platforms, extracts lesson content,
and saves them as structured KB markdown files.

Usage:
  python scraper.py --platform kajabi
  python scraper.py --platform flip2freedom
"""

import asyncio
import os
import re
import argparse
from pathlib import Path
from datetime import datetime
from playwright.async_api import async_playwright
import anthropic
from dotenv import load_dotenv

load_dotenv(dotenv_path="f:/Smart-Vault-Ai/.env")

#  Config 

PLATFORMS = {
    "kajabi": {
        "name": "Tony The Closer",
        "login_url": "https://ronaproof.com/login",
        "email": os.getenv("TONY_CLOSER_EMAIL"),
        "password": os.getenv("TONY_CLOSER_PASSWORD"),
        "kb_path": "f:/Smart-Vault-Ai/KB/realestate/tony-closer",
        "email_selector": 'input[type="email"], input[name="email"]',
        "password_selector": 'input[type="password"], input[name="password"]',
        "submit_selector": 'button[type="submit"], input[type="submit"]',
        "lesson_link_pattern": r"(lesson|module|course|chapter)",
        "kartra": False,
    },
    "flip2freedom": {
        "name": "Sean Terry - F2FA 30 Premium",
        "login_url": "https://www.flip2freedomacademy.com/login",
        "email": os.getenv("SEAN_TERRY_EMAIL"),
        "password": os.getenv("SEAN_TERRY_PASSWORD"),
        "kb_path": "f:/Smart-Vault-Ai/KB/realestate/sean-terry",
        "email_selector": 'input[name="email"]',
        "password_selector": 'input[name="password"], input[type="password"]',
        "submit_selector": 'button[type="submit"], input[type="submit"]',
        "lesson_link_pattern": r"(lesson|module|course|chapter|training)",
        "kartra": True,
    },
}

KB_BASE = Path("f:/Smart-Vault-Ai/KB/realestate")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

#  Claude processor 

def process_transcript_to_kb(transcript: str, lesson_title: str, course_name: str, lesson_num: int) -> str:
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    transcript = transcript.encode('ascii', errors='ignore').decode('ascii')
    lesson_title = lesson_title.encode('ascii', errors='ignore').decode('ascii')
    course_name = course_name.encode('ascii', errors='ignore').decode('ascii')

    prompt = f"""You are processing a course lesson transcript for Smart Vault Co.'s knowledge base.

Course: {course_name}
Lesson {lesson_num}: {lesson_title}

Raw transcript:
{transcript}

Convert this into a structured KB markdown file. Extract and organize:
1. Key concepts and frameworks taught
2. Exact scripts, word-for-word (quote these in blockquotes)
3. Step-by-step processes or checklists
4. Rules and non-negotiables stated
5. Examples and case studies mentioned
6. Tools or resources recommended
7. Objection handling responses (exact words if given)
8. Any formulas or calculations

Format as clean markdown with clear headers. Keep all exact scripts word-for-word. Skip filler, intros, and repetition. Only keep actionable content.

Start with:
# {lesson_title}
## Course: {course_name} | Lesson {lesson_num}
"""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )

    return message.content[0].text


#  Transcript extraction 

async def extract_transcript_from_page(page) -> str:
    transcript = ""

    transcript_selectors = [
        ".transcript", "#transcript", "[data-transcript]",
        ".lesson-transcript", ".video-transcript",
        ".kjb-text-content", ".kj-lesson-content",
        "[class*='transcript']", "[id*='transcript']",
    ]
    for selector in transcript_selectors:
        try:
            el = await page.query_selector(selector)
            if el:
                text = await el.inner_text()
                if len(text) > 200:
                    print(f"  Found transcript via selector: {selector}")
                    return text.strip()
        except Exception:
            pass

    print("  No transcript element found. Attempting caption capture...")

    video_selectors = ["video", "iframe[src*='wistia']", "iframe[src*='vimeo']",
                       "iframe[src*='youtube']", "iframe[src*='loom']",
                       ".wistia_embed", "[class*='video']"]

    for selector in video_selectors:
        try:
            el = await page.query_selector(selector)
            if el:
                print(f"  Video found via: {selector}")
                break
        except Exception:
            pass

    print("  Extracting all lesson text content...")
    try:
        content = await page.evaluate("""() => {
            const remove = ['nav', 'header', 'footer', '.sidebar', '.navigation',
                           '[class*="nav"]', '[class*="header"]', '[class*="footer"]'];
            remove.forEach(sel => {
                document.querySelectorAll(sel).forEach(el => el.remove());
            });
            const main = document.querySelector('main, .main, #main, article, .lesson-content, .course-content, [class*="content"]');
            if (main) return main.innerText;
            return document.body ? document.body.innerText : '';
        }""")

        if content and len(content) > 100:
            transcript = content.strip()
            print(f"  Extracted {len(transcript)} characters of lesson content")

    except Exception as e:
        print(f"  Content extraction error: {e}")

    return transcript


#  Kartra: next-button walk mode 

async def scrape_kartra(page, config, kb_path, index_entries, processed_ref, skipped_ref):
    processed = 0
    skipped = 0

    print("\n  >> KARTRA MODE")
    print("  >> In Chromium: navigate to the FIRST lesson of your course.")
    print("  >> Paste the lesson URL here (or press Enter to use current page):")
    first_url = input().strip()
    if first_url:
        try:
            await page.goto(first_url, wait_until="networkidle")
            await page.wait_for_timeout(3000)
        except Exception as e:
            print(f"  Could not navigate to URL: {e}")

    lesson_num = 0
    print(f"\n[3/4] Processing lessons (Kartra next-button mode)...")
    print("  Type 'done' at any prompt to stop.\n")

    while True:
        lesson_num += 1
        current_url = page.url

        try:
            title = await page.evaluate("""() => {
                const candidates = [
                    document.querySelector('h1'),
                    document.querySelector('h2'),
                    document.querySelector('.lesson-title'),
                    document.querySelector('[class*="title"]'),
                ];
                for (const el of candidates) {
                    if (el && el.innerText.trim().length > 2) return el.innerText.trim();
                }
                return document.title || '';
            }""")
        except Exception:
            title = f"Lesson {lesson_num}"

        title = title.encode('ascii', errors='ignore').decode('ascii').strip()
        if not title:
            title = f"Lesson {lesson_num}"

        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
        safe_title = re.sub(r'\s+', '-', safe_title).lower()
        filename = f"{lesson_num:02d}-{safe_title[:60]}.md"
        filepath = kb_path / filename

        print(f"  [Lesson {lesson_num}] {title[:60]}")
        print(f"  URL: {current_url[:80]}")

        if filepath.exists():
            print(f"  SKIP (already exists)\n")
            skipped += 1
        else:
            raw_content = await extract_transcript_from_page(page)

            if len(raw_content) < 100:
                print(f"  ! Insufficient content ({len(raw_content)} chars) - saving placeholder")
                kb_content = f"# {title}\n## Course: {config['name']} | Lesson {lesson_num}\n\n*Transcript not available - add manually.*\n\nURL: {current_url}\n"
            else:
                print(f"  Sending {len(raw_content)} chars to Claude...")
                kb_content = process_transcript_to_kb(raw_content, title, config["name"], lesson_num)
                print(f"  KB file generated ({len(kb_content)} chars)")

            filepath.write_text(kb_content, encoding="utf-8")
            print(f"  Saved: {filename}\n")
            index_entries.append({"lesson": lesson_num, "title": title, "file": filename, "chars": len(kb_content)})
            processed += 1

        # Try Next button
        next_clicked = False
        try:
            next_clicked = await page.evaluate("""() => {
                const candidates = Array.from(document.querySelectorAll('a, button'));
                const next = candidates.find(el => {
                    const t = (el.innerText || '').trim().toLowerCase();
                    return t === 'next' || t === 'next lesson' || t === 'next video' || t === '>';
                });
                if (next) { next.click(); return true; }
                return false;
            }""")
        except Exception:
            pass

        if next_clicked:
            await page.wait_for_timeout(3000)
            try:
                await page.wait_for_load_state("networkidle", timeout=10000)
            except Exception:
                pass
            if page.url != current_url:
                continue

        print("  >> No Next button found or page did not change.")
        print("  >> Manually navigate to the next lesson in Chromium, then press Enter.")
        print("  >> Or type 'done' to finish:")
        user_input = input().strip().lower()
        if user_input == 'done':
            break
        await page.wait_for_timeout(2000)

    processed_ref[0] = processed
    skipped_ref[0] = skipped


#  Main scraper 

async def scrape_course(platform_key: str):
    config = PLATFORMS[platform_key]
    kb_path = Path(config["kb_path"])
    kb_path.mkdir(parents=True, exist_ok=True)

    print(f"\n{'='*60}")
    print(f"Smart Vault Co. - Course Scraper")
    print(f"Course: {config['name']}")
    print(f"Platform: {platform_key}")
    print(f"KB Output: {kb_path}")
    print(f"{'='*60}\n")

    if not config["email"] or not config["password"]:
        print(f"ERROR: Missing credentials in .env")
        return

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            args=["--enable-features=LiveCaption"]
        )
        context = await browser.new_context(
            viewport={"width": 1280, "height": 800},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        )
        page = await context.new_page()

        #  Step 1: Login 
        print(f"[1/4] Logging in to {config['login_url']}...")
        await page.goto(config["login_url"], wait_until="networkidle")
        await page.wait_for_timeout(2000)

        try:
            await page.fill(config["email_selector"], config["email"])
            await page.fill(config["password_selector"], config["password"])
            await page.click(config["submit_selector"])
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(3000)
            print(f"  Logged in - current URL: {page.url}")
        except Exception as e:
            print(f"  Login error (auto-fill failed): {e}")
            print("  >> Browser is open - log in manually, then press Enter to continue...")
            input()
            await page.wait_for_load_state("networkidle")
            await page.wait_for_timeout(3000)

        index_entries = []
        processed_ref = [0]
        skipped_ref = [0]

        #  Kartra mode 
        if config.get("kartra"):
            await scrape_kartra(page, config, kb_path, index_entries, processed_ref, skipped_ref)
            processed = processed_ref[0]
            skipped = skipped_ref[0]
            total = processed + skipped

        #  Kajabi / standard link-scan mode 
        else:
            print(f"\n[2/4] Finding course lessons...")
            await page.wait_for_timeout(2000)

            lesson_links = await page.evaluate(f"""() => {{
                const links = Array.from(document.querySelectorAll('a[href]'));
                const pattern = /{config['lesson_link_pattern']}/i;
                return links
                    .filter(a => pattern.test(a.href) || pattern.test(a.innerText))
                    .map(a => ({{ href: a.href, text: a.innerText.trim() }}))
                    .filter(l => l.href && l.text && l.text.length > 2)
                    .filter((l, i, arr) => arr.findIndex(x => x.href === l.href) === i);
            }}""")

            if len(lesson_links) < 3:
                lesson_links = await page.evaluate("""() => {
                    const links = Array.from(document.querySelectorAll(
                        '.kjb-lesson, .lesson-item, [class*="lesson"], [class*="module"] a, .course-player a'
                    ));
                    return links
                        .map(el => ({
                            href: el.href || el.querySelector('a')?.href,
                            text: el.innerText.trim()
                        }))
                        .filter(l => l.href && l.text)
                        .filter((l, i, arr) => arr.findIndex(x => x.href === l.href) === i);
                }""")

            print(f"  Found {len(lesson_links)} lessons")

            if len(lesson_links) == 0:
                print("  No lessons found automatically.")
                print("  >> Browser is open. Navigate to the course curriculum page.")
                print("  >> Press Enter when you're on the page with all lesson links...")
                input()
                lesson_links = await page.evaluate("""() => {
                    return Array.from(document.querySelectorAll('a[href]'))
                        .map(a => ({ href: a.href, text: a.innerText.trim() }))
                        .filter(l => l.text.length > 3 && l.href.includes(window.location.hostname));
                }""")
                print(f"  Found {len(lesson_links)} links after manual navigation")

            print("\n  Lessons found:")
            for i, lesson in enumerate(lesson_links[:20], 1):
                print(f"    {i}. {lesson['text'][:60]} -- {lesson['href'][:60]}")
            if len(lesson_links) > 20:
                print(f"    ... and {len(lesson_links) - 20} more")

            print(f"\n[3/4] Processing lessons...")
            processed = 0
            skipped = 0

            for i, lesson in enumerate(lesson_links, 1):
                title = lesson["text"].strip()
                url = lesson["href"]

                safe_title = re.sub(r'[^\w\s-]', '', title).strip()
                safe_title = re.sub(r'\s+', '-', safe_title).lower()
                filename = f"{i:02d}-{safe_title[:60]}.md"
                filepath = kb_path / filename

                if filepath.exists():
                    print(f"  [{i}/{len(lesson_links)}] SKIP (exists): {title[:50]}")
                    skipped += 1
                    continue

                print(f"\n  [{i}/{len(lesson_links)}] Processing: {title[:50]}")

                try:
                    await page.goto(url, wait_until="networkidle")
                    await page.wait_for_timeout(3000)

                    raw_content = await extract_transcript_from_page(page)

                    if len(raw_content) < 100:
                        print(f"  ! Insufficient content ({len(raw_content)} chars) - saving placeholder")
                        kb_content = f"# {title}\n## Course: {config['name']} | Lesson {i}\n\n*Transcript not available - add manually.*\n\nURL: {url}\n"
                    else:
                        print(f"  Sending {len(raw_content)} chars to Claude for processing...")
                        kb_content = process_transcript_to_kb(raw_content, title, config["name"], i)
                        print(f"  KB file generated ({len(kb_content)} chars)")

                    filepath.write_text(kb_content, encoding="utf-8")
                    print(f"  Saved: {filename}")

                    index_entries.append({
                        "lesson": i,
                        "title": title,
                        "file": filename,
                        "chars": len(kb_content)
                    })
                    processed += 1
                    await page.wait_for_timeout(2000)

                except Exception as e:
                    print(f"  ! Error on lesson {i}: {e}")
                    continue

            total = len(lesson_links)

        #  Step 4: Generate index file 
        print(f"\n[4/4] Generating course index...")

        index_content = f"# {config['name']} - Course Knowledge Base Index\n"
        index_content += f"Generated: {datetime.now().strftime('%Y-%m-%d')}\n"
        index_content += f"Processed: {processed} | Skipped: {skipped}\n\n---\n\n## Lesson Index\n\n"

        for entry in index_entries:
            index_content += f"- [{entry['lesson']:02d}. {entry['title']}]({entry['file']})\n"

        index_content += "\n---\n\n## How Bots Use This KB\n\n"
        index_content += "- **Closer Bot** - references scripts, objection handling, BANT framework\n"
        index_content += "- **Real Estate Bot** - references deal flow, offer strategies, outreach sequences\n"
        index_content += "- **RE Researcher** - uses as baseline, continuously updates with new findings\n\n"
        index_content += "*All files auto-generated by Smart Vault Co. Course Scraper*\n"

        index_file = kb_path / "INDEX.md"
        index_file.write_text(index_content, encoding="utf-8")

        print(f"\n{'='*60}")
        print(f"COMPLETE - {config['name']} course")
        print(f"  Processed: {processed} lessons")
        print(f"  Skipped:   {skipped} (already existed)")
        print(f"  KB folder: {kb_path}")
        print(f"  Index:     {index_file}")
        print(f"{'='*60}\n")

        await browser.close()


#  Entry point 

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Smart Vault Co. Course Scraper")
    parser.add_argument(
        "--platform",
        choices=list(PLATFORMS.keys()),
        required=True,
        help="Which course platform to scrape"
    )
    args = parser.parse_args()

    asyncio.run(scrape_course(args.platform))
