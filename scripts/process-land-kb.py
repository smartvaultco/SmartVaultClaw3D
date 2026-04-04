"""
Smart Vault Co. — Land Flipping KB Processor
Reads all PDFs in land-flipping-raw/ and converts them to structured KB markdown.
"""

import os
import sys
from pathlib import Path
import anthropic
from dotenv import load_dotenv

# Fix Windows Unicode output
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

load_dotenv(dotenv_path="f:/Smart-Vault-Ai/.env")

RAW_DIR = Path("f:/Smart-Vault-Ai/KB/realestate/land-flipping-raw")
KB_DIR = Path("f:/Smart-Vault-Ai/KB/realestate/land-flipping")
KB_DIR.mkdir(parents=True, exist_ok=True)

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text from PDF using pdfplumber."""
    try:
        import pdfplumber
        text = ""
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                t = page.extract_text()
                if t:
                    text += t + "\n"
        return text.strip()
    except Exception as e:
        print(f"  ! pdfplumber error: {e}")
        return ""

def process_to_kb(raw_text: str, doc_name: str) -> str:
    """Send raw text to Claude Haiku → structured KB markdown."""
    prompt = f"""You are building a knowledge base for Smart Vault Co.'s Real Estate Bot and Land Flipping operations.

Document: {doc_name}

Raw content:
{raw_text[:12000]}

Convert this into a structured KB markdown file. Extract and organize:
1. Key strategies, methods, and frameworks
2. Exact scripts or templates (quote word-for-word in blockquotes)
3. Step-by-step processes and checklists
4. Legal clauses, contract language, or disclosure requirements
5. Tools, resources, or services mentioned
6. Formulas, calculations, or financial models
7. Rules, non-negotiables, or warnings

Format as clean markdown with clear headers. Focus only on actionable content the RE Bot and Closer Bot can use directly. Skip filler, bios, and promotional content.

Start with:
# {doc_name}
## Smart Vault Co. Knowledge Base — Land Flipping
"""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text

def main():
    pdfs = sorted(RAW_DIR.glob("*.pdf"))
    print(f"\nSmart Vault Co. — Land Flipping KB Processor")
    print(f"Found {len(pdfs)} PDFs to process\n")

    index_entries = []

    for i, pdf_path in enumerate(pdfs, 1):
        name = pdf_path.stem
        safe_name = name.lower().replace(" ", "-").replace("_", "-")
        out_file = KB_DIR / f"{safe_name}.md"

        if out_file.exists():
            print(f"[{i}/{len(pdfs)}] SKIP (exists): {name}")
            index_entries.append(name)
            continue

        print(f"[{i}/{len(pdfs)}] Processing: {name}")

        raw_text = extract_text_from_pdf(pdf_path)
        if len(raw_text) < 50:
            print(f"  ! Could not extract text from {name} — skipping")
            continue

        print(f"  → {len(raw_text)} chars extracted → sending to Claude...")
        kb_content = process_to_kb(raw_text, name)
        out_file.write_text(kb_content, encoding="utf-8")
        print(f"  ✓ Saved: {out_file.name} ({len(kb_content)} chars)")
        index_entries.append(name)

    # Write index
    index = f"""# Land Flipping Knowledge Base — Index
Generated from {len(pdfs)} source documents.
Used by: Real Estate Bot, Closer Bot, RE Researcher

---

## Documents

"""
    for entry in index_entries:
        safe = entry.lower().replace(" ", "-").replace("_", "-")
        index += f"- [{entry}]({safe}.md)\n"

    index += """
---

## Key Strategies Covered
- Jerry Norton wholesaling and flipping methods
- Creative financing hacks
- Cash buyer scripts and agent scripts
- Funding and investor relations
- Legal docs: NDNCA, contracts, addendums, disclosures
- Facebook/social media advertising for RE
- IRA real estate investing
- REtipster land flipping methodology

*Processed by Smart Vault Co. KB Processor*
"""
    (KB_DIR / "INDEX.md").write_text(index, encoding="utf-8")
    print(f"\n✓ INDEX.md written")
    print(f"✓ KB folder: {KB_DIR}")
    print(f"\nDone! {len(index_entries)} documents in KB.")

if __name__ == "__main__":
    main()
