#!/usr/bin/env python3
"""
Batch generate node documentation using AI API
"""

import os
import sys
import json
import time
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime
from openai import OpenAI

import runtime  # noqa: F401
from lib.doc_disclaimer import compose_document, create_en_disclaimer, strip_ai_disclaimer
from lib.doc_title import ensure_doc_title, strip_leading_h1
from lib.hash_footer import (
    format_source_hash_footer,
    load_node_source_sha256,
    strip_source_hash_footer,
)
from lib.paths import (
    AI_INPUT_DIR,
    LOGS_DIR,
    REPO_ROOT,
    SCRIPTS_DIR,
    default_embedded_docs_path,
    load_dotenv,
)

load_dotenv()

# Configuration
API_KEY = os.getenv('LLM_API_KEY') or os.getenv('DEEPSEEK_API_KEY')
API_BASE_URL = os.getenv('API_BASE_URL', '').strip()
API_MODEL = os.getenv('API_MODEL', '').strip()
BATCH_SIZE = int(os.getenv('BATCH_SIZE', '5'))
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))
DELAY_BETWEEN_REQUESTS = int(os.getenv('DELAY_BETWEEN_REQUESTS', '2'))


def _extract_signature(text: str) -> dict:
    """Extract structural facts from a doc: params, types, required flags, ranges, outputs.

    Two versions of a doc with the same signature convey the same factual content;
    differing prose is only wording. Used to detect rewording-only churn.
    """
    import re as _re
    sig = {"rows": [], "note_facts": set()}
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and not _re.match(r"^\|[\s:`\-]+\|$", s):
            cells = [c.strip().strip("`") for c in s.split("|")[1:-1]]
            if not cells:
                continue
            first = cells[0]
            if _re.match(r"^(参数|パラメータ|파라미터|Param|Parameter|Parámetro|Paramètre|Параметр|معامل|매개변수)$", first, _re.I):
                continue  # header
            if all(set(c) <= {"-", ":", " "} for c in cells):
                continue  # separator
            # row signature: name + type + required + range (description excluded)
            sig["rows"].append(tuple(cells[:1] + cells[2:4] if len(cells) >= 4 else cells))
    return sig


def _is_rewording_only(old_text: str, new_text: str) -> bool:
    """True when new_text has identical structure/params/types/required/ranges
    as old_text but different prose (pure rewording churn)."""
    old_sig = _extract_signature(old_text)
    new_sig = _extract_signature(new_text)
    if not old_sig["rows"] or old_sig["rows"] != new_sig["rows"]:
        return False
    # headings must match too
    def heads(t):
        return [l.strip() for l in t.splitlines() if l.strip().startswith("#") and not l.strip().startswith("# ")]
    # ignore H1 title differences only if identical otherwise; require all ## headings equal
    def h2(t):
        return [l.strip() for l in t.splitlines() if l.startswith("## ")]
    if h2(old_text) != h2(new_text):
        return False
    return True


def _strip_markdown_output_fence(text: str) -> str:
    """Remove an outer ```markdown ... ``` fence that some LLMs wrap around
    the entire generated document (sometimes right after the H1). Only strips
    when the closing fence is the last standalone fence with balanced content
    inside; leaves genuine inner code fences untouched."""
    lines = text.split('\n')
    open_idx = None
    for i, line in enumerate(lines):
        if line.strip() == '```markdown':
            open_idx = i
            break
    if open_idx is None:
        return text
    # find the matching closing fence: the LAST standalone ``` in the file
    close_idx = None
    for i in range(len(lines) - 1, open_idx, -1):
        if lines[i].strip() == '```':
            close_idx = i
            break
    if close_idx is None or close_idx - open_idx < 2:
        return text
    inner = lines[open_idx + 1:close_idx]
    # sanity: inner must not contain unbalanced ``` (would mean a real inner fence)
    if sum(1 for l in inner if l.strip().startswith('```')) % 2 != 0:
        return text
    return '\n'.join(lines[:open_idx] + inner + lines[close_idx + 1:])
DELAY_BETWEEN_REQUESTS = int(os.getenv('DELAY_BETWEEN_REQUESTS', '2'))

# Path configuration
AI_INPUT_PATH = AI_INPUT_DIR
DOCS_OUTPUT_PATH = default_embedded_docs_path() / "comfyui_embedded_docs" / "docs"
LOG_PATH = LOGS_DIR

# Create necessary directories
LOG_PATH.mkdir(parents=True, exist_ok=True)


class DocGenerationLogger:
    """Documentation generation logger"""
    
    def __init__(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_file = LOG_PATH / f"generation_{timestamp}.log"
        self.success_count = 0
        self.failed_count = 0
        self.skipped_count = 0
        self.failed_nodes = []
    
    def log(self, message: str, level: str = "INFO"):
        """Log a message"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] [{level}] {message}"
        print(log_entry)
        
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry + '\n')
    
    def log_success(self, node_name: str):
        """Log a successful generation"""
        self.success_count += 1
        self.log(f"✅ Successfully generated: {node_name}", "SUCCESS")
    
    def log_failure(self, node_name: str, error: str):
        """Log a failed generation"""
        self.failed_count += 1
        self.failed_nodes.append({'node': node_name, 'error': error})
        self.log(f"❌ Generation failed: {node_name} - {error}", "ERROR")
    
    def log_skip(self, node_name: str, reason: str):
        """Log a skipped node"""
        self.skipped_count += 1
        self.log(f"⏭️  Skipped: {node_name} - {reason}", "SKIP")
    
    def summary(self):
        """Output generation summary"""
        self.log("=" * 80)
        self.log("📊 Generation Summary")
        self.log("=" * 80)
        self.log(f"✅ Success: {self.success_count}")
        self.log(f"❌ Failed: {self.failed_count}")
        self.log(f"⏭️  Skipped: {self.skipped_count}")
        self.log(f"📁 Log file: {self.log_file}")
        
        if self.failed_nodes:
            self.log("\nFailed nodes:")
            for item in self.failed_nodes:
                self.log(f"  - {item['node']}: {item['error']}")


class AIDocGenerator:
    """AI documentation generator"""
    
    def __init__(self):
        if not API_KEY:
            raise ValueError("❌ LLM_API_KEY not found, please configure it in .env file")
        if not API_BASE_URL or not API_MODEL:
            raise ValueError(
                "❌ API_BASE_URL / API_MODEL not configured. Point them at your "
                "OpenAI-compatible provider (e.g. DeepSeek, OpenAI, OpenRouter, "
                "local vLLM/Ollama) in .env."
            )
        
        self.client = OpenAI(
            api_key=API_KEY,
            base_url=API_BASE_URL
        )
        self.logger = DocGenerationLogger()
    
    def generate_doc(self, node_name: str, prompt: str, retry_count: int = 0) -> Optional[str]:
        """Generate a single document using AI"""
        try:
            self.logger.log(f"🤖 Generating documentation: {node_name}")
            
            response = self.client.chat.completions.create(
                model=API_MODEL,
                messages=[
                    {"role": "system", "content": "You are a technical documentation expert specializing in ComfyUI nodes. Generate clear, accurate, and factual documentation based on source code."},
                    {"role": "user", "content": prompt}
                ],
                stream=False,
                temperature=0.3  # Lower temperature for more consistent output
            )
            
            content = response.choices[0].message.content

            # Strip LLM output fence: some models (glm-4-flash etc.) wrap the whole
            # document in ```markdown ... ``` which renders the doc as a code block.
            fence_stripped = _strip_markdown_output_fence(content)
            if fence_stripped != content:
                self.logger.log("Stripped markdown output fence from generated doc")
                content = fence_stripped

            # Validate generated content
            if not content or len(content) < 100:
                raise ValueError("Generated documentation too short")
            
            # Check for required sections (updated to match new structure)
            if "## Inputs" not in content or "## Outputs" not in content:
                raise ValueError("Missing required documentation sections (Inputs/Outputs)")
            
            return content
            
        except Exception as e:
            if retry_count < MAX_RETRIES:
                self.logger.log(f"⚠️  Retrying ({retry_count + 1}/{MAX_RETRIES}): {node_name}", "RETRY")
                time.sleep(DELAY_BETWEEN_REQUESTS * 2)
                return self.generate_doc(node_name, prompt, retry_count + 1)
            else:
                raise e
    
    def save_doc(self, node_name: str, content: str, original_doc: str | None = None) -> bool:
        """Save generated documentation with disclaimer at the bottom of the file."""
        try:
            # Create node documentation directory
            doc_dir = DOCS_OUTPUT_PATH / node_name
            doc_dir.mkdir(parents=True, exist_ok=True)

            disclaimer = create_en_disclaimer(node_name)

            src_hash = load_node_source_sha256(node_name)
            if src_hash:
                footer = format_source_hash_footer(src_hash)
            else:
                footer = ""
                self.logger.log(
                    f"⚠️  No fingerprint for {node_name}: missing ai_input basic_info/source — en.md saved without hash footer",
                    "SKIP",
                )

            body = ensure_doc_title(strip_leading_h1(content), node_name, "en")
            final_content = compose_document(body, disclaimer, footer)
            
            # Churn guard (update mode only): if the AI rewrite carries the same
            # params/types/required/ranges as the existing doc and only rewords prose,
            # keep the original file. Wording-only churn creates 100s of wasted diff
            # lines and translation debt (2026-09 Loop-node refresh lesson).
            if original_doc is not None:
                old_final = compose_document(
                    ensure_doc_title(strip_leading_h1(original_doc), node_name, "en"),
                    disclaimer, footer)
                if final_content != old_final and _is_rewording_only(old_final, final_content):
                    final_content = old_final
                    self.logger.log(
                        f"🔇 {node_name}: AI output was rewording-only; kept existing en.md",
                        "SKIP")
            
            # Save English documentation
            doc_file = doc_dir / "en.md"
            with open(doc_file, 'w', encoding='utf-8') as f:
                f.write(final_content)
            
            self.logger.log(f"💾 Saved: {doc_file}")
            return True
            
        except Exception as e:
            self.logger.log(f"❌ Save failed: {node_name} - {e}", "ERROR")
            return False
    
    def build_update_prompt(self, base_prompt: str, existing_doc: str) -> str:
        """Wrap the base prompt with existing doc context for incremental update."""
        return (
            base_prompt
            + "\n\n"
            + "## Existing Documentation (for reference)\n\n"
            + "The following is the **current en.md** for this node. "
            + "It may contain manual edits, extra context, or sections that go beyond what the source code alone implies. "
            + "**Preserve all such content unless the updated source code directly contradicts it.**\n\n"
            + "Your job is to produce an updated en.md that:\n"
            + "1. Reflects any parameter additions, removals, or type changes visible in the new source code above.\n"
            + "2. Keeps all human-written descriptions, notes, and extra sections that are still accurate.\n"
            + "3. Does NOT discard or rewrite content just because it was not derived from the source code — "
            + "only remove content that is factually incorrect given the new source.\n"
            + "4. MINIMAL DIFF IS MANDATORY: copy the existing en.md verbatim as your starting point and change ONLY "
            + "the specific lines that the new source code requires. Do NOT rephrase, reorder, or 'improve' any "
            + "sentence whose meaning is unchanged. Do NOT restructure headings, tables, or sections. Do NOT "
            + "unify terminology or change wording style. A line with unchanged meaning must appear byte-identical "
            + "in your output. Rewording-only changes are treated as pipeline defects.\n\n"
            + "```markdown\n"
            + existing_doc
            + "\n```\n"
        )

    def process_node(self, node_name: str, force: bool = False) -> bool:
        """Process a single node"""
        doc_file = DOCS_OUTPUT_PATH / node_name / "en.md"
        if doc_file.exists() and not force:
            self.logger.log_skip(node_name, "Documentation already exists")
            return True

        # Read AI prompt
        prompt_file = AI_INPUT_PATH / node_name / "ai_prompt.txt"
        if not prompt_file.exists():
            self.logger.log_skip(node_name, "AI prompt file not found")
            return False

        try:
            with open(prompt_file, 'r', encoding='utf-8') as f:
                prompt = f.read()

            # If an existing doc is present and we are force-regenerating, send it
            # to the AI as context so human edits are preserved.
            if force and doc_file.exists():
                with open(doc_file, 'r', encoding='utf-8') as f:
                    existing_doc = strip_ai_disclaimer(strip_source_hash_footer(f.read()))
                self.logger.log(f"📄 Existing doc found — using update prompt to preserve edits: {node_name}")
                prompt = self.build_update_prompt(prompt, existing_doc)

            content = self.generate_doc(node_name, prompt)

            if content:
                if self.save_doc(node_name, content, original_doc=existing_doc if force else None):
                    self.logger.log_success(node_name)
                    return True

            return False

        except Exception as e:
            self.logger.log_failure(node_name, str(e))
            return False
    
    def batch_process(self, node_names: List[str], force: bool = False):
        """Batch process nodes"""
        total = len(node_names)
        self.logger.log("=" * 80)
        self.logger.log(f"🚀 Starting batch documentation generation")
        self.logger.log(f"📊 Total: {total} nodes")
        self.logger.log(f"🔧 API: {API_MODEL}")
        self.logger.log(f"⚙️  Batch size: {BATCH_SIZE}")
        self.logger.log("=" * 80)
        self.logger.log("")
        
        consecutive_failures = 0
        MAX_CONSECUTIVE_FAILURES = 5
        
        for idx, node_name in enumerate(node_names, 1):
            self.logger.log(f"\n[{idx}/{total}] Processing node: {node_name}")
            self.logger.log("-" * 60)
            
            success = self.process_node(node_name, force)
            
            # Track consecutive failures
            if success:
                consecutive_failures = 0  # Reset on success or skip
            else:
                # Only increment if it was a real failure (not a skip)
                doc_file = DOCS_OUTPUT_PATH / node_name / "en.md"
                if not doc_file.exists():  # Real failure, not a skip
                    consecutive_failures += 1
                    
                    if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                        self.logger.log("")
                        self.logger.log("=" * 80, "ERROR")
                        self.logger.log(f"❌ Consecutive failures reached {MAX_CONSECUTIVE_FAILURES}, terminating", "ERROR")
                        self.logger.log("=" * 80, "ERROR")
                        self.logger.log(f"Success: {self.logger.success_count}, Failed: {self.logger.failed_count}, Skipped: {self.logger.skipped_count}", "ERROR")
                        self.logger.log("Please check:", "ERROR")
                        self.logger.log("  1. API key is correctly configured", "ERROR")
                        self.logger.log("  2. Network connection is stable", "ERROR")
                        self.logger.log("  3. API has sufficient balance", "ERROR")
                        self.logger.log("=" * 80, "ERROR")
                        sys.exit(1)
                else:
                    consecutive_failures = 0  # Reset if it was a skip
            
            # Delay requests to avoid API rate limits
            if idx < total and idx % BATCH_SIZE == 0:
                self.logger.log(f"⏸️  Batch completed, waiting {DELAY_BETWEEN_REQUESTS} seconds...")
                time.sleep(DELAY_BETWEEN_REQUESTS)
        
        # Output summary
        self.logger.log("")
        self.logger.summary()
        
        # Update reports if any documents were generated
        if self.logger.success_count > 0:
            self.logger.log("")
            self.logger.log("=" * 80)
            self.logger.log("🔄 Updating reports...")
            self.logger.log("=" * 80)
            self._update_reports()
    
    def _update_reports(self):
        """Update missing_nodes_report.json after generation"""
        try:
            import subprocess
            
            # Re-run scan_missing_nodes.py to update the report
            scan_script = SCRIPTS_DIR / "scan_missing_nodes.py"
            
            self.logger.log(f"📊 Running scan to update missing_nodes_report.json...")
            result = subprocess.run(
                ["python3", str(scan_script)],
                capture_output=True,
                text=True,
                cwd=REPO_ROOT
            )
            
            if result.returncode == 0:
                self.logger.log("✅ missing_nodes_report.json updated successfully")
                # Extract summary from output
                for line in result.stdout.split('\n'):
                    if 'Missing' in line or 'nodes' in line.lower():
                        self.logger.log(f"   {line.strip()}")
            else:
                self.logger.log(f"⚠️  Failed to update report: {result.stderr}", "WARN")
        
        except Exception as e:
            self.logger.log(f"⚠️  Error updating reports: {e}", "WARN")


def main():
    """Main function"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Batch generate node documentation using AI API')
    parser.add_argument('mode', choices=['test', 'all', 'node', 'resume', 'changed'],
                        help='Run mode: test(test), all(all), node(single node), resume(continue unfinished), changed(regenerate changed nodes)')
    parser.add_argument('--count', type=int, default=5, 
                        help='Number of nodes to generate in test mode (default: 5)')
    parser.add_argument('--node', type=str, 
                        help='Node name for single node mode')
    parser.add_argument('--force', action='store_true', 
                        help='Force regenerate existing documentation')
    
    args = parser.parse_args()
    
    # Check AI input directory
    if not AI_INPUT_PATH.exists():
        print("❌ ai_input directory not found, please run prepare_ai_input.py first")
        return
    
    # Get all prepared nodes from ai_input directory
    prepared_nodes = [d.name for d in AI_INPUT_PATH.iterdir() 
                     if d.is_dir() and (d / "ai_prompt.txt").exists()]
    
    if not prepared_nodes:
        print("❌ No prepared nodes found, please run prepare_ai_input.py first")
        return
    
    # Filter to only nodes without documentation (unless force mode)
    if not args.force:
        nodes_without_docs = [
            node for node in prepared_nodes 
            if not (DOCS_OUTPUT_PATH / node / "en.md").exists()
        ]
    else:
        nodes_without_docs = prepared_nodes
    
    nodes_to_process = []

    print(f"📊 AI input bundles on disk (folders with ai_prompt.txt): {len(prepared_nodes)}")

    # Select nodes to process based on mode
    if args.mode == 'changed':
        # Read the batch_nodes.json written by prepare_ai_input.py changed mode
        batch_file = AI_INPUT_PATH / "batch_nodes.json"
        if not batch_file.exists():
            print("❌ batch_nodes.json not found, please run prepare_ai_input.py changed first")
            return
        with open(batch_file, 'r', encoding='utf-8') as f:
            batch_nodes = json.load(f)
        nodes_to_process = [
            n['node_name']
            for n in batch_nodes
            if (AI_INPUT_PATH / n['node_name'] / "ai_prompt.txt").exists()
        ]
        print(
            f"🔄 Changed mode: {len(nodes_to_process)} node(s) in this batch (from batch_nodes.json).\n"
            f"   (Scan compares live ComfyUI class-body hash vs node_versions.json 'current_hash'.)\n"
            f"   The {len(prepared_nodes)} bundles above include older runs — only the batch list is regenerated."
        )
    else:
        if not args.force:
            print(f"📝 Missing en.md (among bundles): {len(nodes_without_docs)}")
        else:
            print(
                f"📝 --force: regenerate pool = all {len(nodes_without_docs)} bundles "
                "(not \"missing docs\" — every bundle is eligible for the chosen mode)."
            )

        if args.mode == 'test':
            nodes_to_process = nodes_without_docs[:args.count]
            print(f"💡 Test mode: Generate first {len(nodes_to_process)} nodes with missing documentation")

        elif args.mode == 'all':
            nodes_to_process = nodes_without_docs
            print(f"🚀 Full mode: Generate all {len(nodes_to_process)} nodes with missing documentation")

        elif args.mode == 'node':
            if not args.node:
                print("❌ Please specify node name using --node")
                return
            if args.node in prepared_nodes:
                nodes_to_process = [args.node]
            else:
                print(f"❌ Node not found: {args.node}")
                return

        elif args.mode == 'resume':
            nodes_to_process = nodes_without_docs
            print(f"🔄 Resume mode: Generate remaining {len(nodes_to_process)} nodes")

    if not nodes_to_process:
        print("✅ All nodes already have documentation!")
        return
    
    # Show summary
    print(f"\nPreparing to generate documentation for {len(nodes_to_process)} nodes")
    print(f"API: {API_MODEL}")
    print(f"Output directory: {DOCS_OUTPUT_PATH}")
    print(f"Mode: {'Force regenerate' if args.force else 'Skip existing documentation'}")
    print()
    
    # Start generation
    generator = AIDocGenerator()
    generator.batch_process(nodes_to_process, args.force)


if __name__ == "__main__":
    main()

