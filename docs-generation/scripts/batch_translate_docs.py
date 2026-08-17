#!/usr/bin/env python3
"""
Batch translate documentation using AI
Trusts the batch list from prepare_translation.py (files already verified as missing)
"""

import argparse
import json
import os
import re
import sys
import time
import logging
from pathlib import Path
from datetime import datetime

import runtime  # noqa: F401
from lib.doc_disclaimer import (
    compose_document,
    create_translated_disclaimer,
    strip_ai_disclaimer,
)
from lib.doc_title import ensure_doc_title, strip_leading_h1
from lib.hash_footer import (
    extract_english_source_fingerprint_hex,
    format_source_hash_footer,
    load_node_source_sha256,
    strip_source_hash_footer,
    strip_trailing_fingerprint_section,
)
from lib.paths import (
    LOGS_DIR,
    TRANSLATION_BATCHES_DIR,
    TRANSLATION_CONFIG,
    default_embedded_docs_path,
    load_dotenv,
)
from update_translation_status import batch_update_translations

load_dotenv()

DOCS_PATH = default_embedded_docs_path() / "comfyui_embedded_docs" / "docs"
TRANSLATION_CONFIG_FILE = TRANSLATION_CONFIG

# GitHub repository info
GITHUB_REPO = "Comfy-Org/embedded-docs"
GITHUB_BRANCH = "main"

# Ensure logs directory exists
LOGS_DIR.mkdir(exist_ok=True)

# Setup logging
log_file = LOGS_DIR / f"translation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# AI Configuration
DEFAULT_API_KEY = os.getenv('LLM_API_KEY') or os.getenv('DEEPSEEK_API_KEY', '')
DEFAULT_BASE_URL = os.getenv('API_BASE_URL', '').strip()
DEFAULT_MODEL = os.getenv('API_MODEL', '').strip()
DEFAULT_BATCH_SIZE = 5

# Custom log level for success

def replace_heading_placeholders(content, lang_config):
    """Replace placeholder headings with actual headings.
    Handles both bare placeholders and AI-generated '## {heading_xxx}' patterns
    to avoid doubled heading markers (e.g. '## ## 输入')."""
    # First, strip any leading '## ' or '# ' from lines containing placeholders
    for placeholder in ('{heading_overview}', '{heading_inputs}', '{heading_outputs}'):
        pattern = re.compile(r'^#{1,2}\s+' + re.escape(placeholder) + r'\s*$', re.MULTILINE)
        content = pattern.sub(placeholder, content)

    content = content.replace('{heading_overview}', f"## {lang_config.get('heading_overview', 'Overview')}")
    content = content.replace('{heading_inputs}', f"## {lang_config.get('heading_inputs', 'Inputs')}")
    content = content.replace('{heading_outputs}', f"## {lang_config.get('heading_outputs', 'Outputs')}")
    return content


# Multi-language preamble patterns — AI sometimes prepends "Here is the translation..."
# before the actual node description. These patterns detect and strip that paragraph.
# Each entry is a regex that matches the first sentence of a preamble paragraph.
_PREAMBLE_PATTERNS: dict[str, list[str]] = {
    'zh': [r'^以下是为您翻译', r'^以下是翻译结果', r'^这是.*?翻译'],
    'zh-TW': [r'^以下是为您翻譯', r'^以下是翻譯結果', r'^這是.*?翻譯'],
    'ja': [r'^以下が翻訳', r'^翻訳結果'],
    'ko': [r'^다음은.*?번역', r'^번역 결과'],
    'ru': [r'^Вот перевод', r'^Перевод документаци'],
    'es': [r'^Aquí está la traducción', r'^Esta es la traducción', r'^Traducción de'],
    'fr': [r'^Voici la traduction', r'^Voici le document', r'^Traduction de'],
    'ar': [r'^هذه هي الترجمة', r'^إليك الترجمة', r'^أنت خبير في الترجمة', r'^هذا هو المستند'],
    'tr': [r'^İşte çeviri', r'^Çeviri sonucu'],
    'pt-BR': [r'^Aqui está a tradução', r'^Esta é a tradução'],
    'fa': [r'^این ترجمه', r'^در زیر ترجمه'],
}


def strip_ai_preamble(content: str, lang: str) -> str:
    """Remove translation preamble that the AI sometimes prepends.

    The AI sometimes adds a sentence like 'Here is the translation into Russian:'
    before the actual node description. This function detects and removes it.

    The preamble is expected to be the first paragraph after the H1 title
    (which is already stripped by strip_leading_h1 before this is called).
    """
    patterns = _PREAMBLE_PATTERNS.get(lang, [])
    if not patterns:
        return content

    lines = content.split('\n')
    # Find the first non-empty line
    first_content_idx = 0
    while first_content_idx < len(lines) and not lines[first_content_idx].strip():
        first_content_idx += 1

    if first_content_idx >= len(lines):
        return content

    first_line = lines[first_content_idx].strip()
    for pat in patterns:
        if re.search(pat, first_line):
            # Remove the preamble line and any following blank lines up to actual content
            del lines[first_content_idx]
            # Remove trailing blank lines after preamble
            while first_content_idx < len(lines) and not lines[first_content_idx].strip():
                del lines[first_content_idx]
            break

    return '\n'.join(lines)

def _extract_table_data_rows(table_text: str) -> list[str]:
    """Return the data rows of a markdown table (lines starting with '|'),
    excluding the header row and the |---| separator row."""
    table_lines = [line for line in table_text.split('\n') if line.strip().startswith('|')]
    data_rows = []
    for i, line in enumerate(table_lines):
        if i == 0:
            continue  # header row
        if re.match(r'^\|[\s:|-]+\|?$', line.strip()):
            continue  # separator row
        data_rows.append(line)
    return data_rows


def _fix_output_names_in_translation(translated_content: str, full_en: str) -> str:
    """Parse the English en.md Outputs table and force output names in translated content
    to match the English original by row index. This prevents the AI from translating
    distinct output names (e.g. 'positive'/'negative') into the same translated word.

    Works by:
    1. Extracting output names from en.md Outputs table in order (row by row).
    2. Extracting output data rows from translated content (rows whose first cell
       is a backtick-wrapped name).
    3. Replacing the first column (output name) of each row with its English counterpart.
    """
    # Extract English output names
    en_outputs_match = re.search(
        r'##\s+(?:Outputs|输出|輸出|出力|출력|Выходы|Salidas|Sorties|المخرجات|Çıktılar|خروجی‌ها)\s*\n(.*?)(?=\n##|\Z)',
        full_en, re.DOTALL
    )
    if not en_outputs_match:
        return translated_content  # No outputs table in English doc, nothing to fix

    en_output_names = []
    for line in _extract_table_data_rows(en_outputs_match.group(1)):
        m = re.match(r'^\|\s*`([^`]+)`', line.strip())
        if m:
            en_output_names.append(m.group(1).strip())

    if not en_output_names:
        return translated_content

    # Now find and fix the Outputs table in translated content
    # Match any known heading for "Outputs" in any language
    # (includes pt-BR "Saídas"; heading values come from translation_config.json)
    tr_outputs_match = re.search(
        r'##\s+(?:输出|輸出|出力|출력|Выходы|Salidas|Sorties|Saídas|Outputs|المخرجات|Çıktılar|خروجی‌ها)\s*\n(.*?)(?=\n##|\Z)',
        translated_content, re.DOTALL
    )
    if not tr_outputs_match:
        return translated_content

    tr_table = tr_outputs_match.group(1)
    tr_lines = tr_table.split('\n')

    # Build new table lines with English names enforced. Only rows whose first
    # cell holds a backtick-wrapped name count as data rows, so the row index
    # cannot drift when blank/intro lines appear inside the section.
    header_seen = False
    new_lines = list(tr_lines)
    data_row_idx = 0
    for i, line in enumerate(tr_lines):
        stripped = line.strip()
        if not stripped.startswith('|'):
            continue
        if not header_seen:
            header_seen = True  # first table line is the header row
            continue
        if re.match(r'^\|[\s:|-]+\|?$', stripped):
            continue  # separator row
        orig_name_match = re.match(r'^\|(\s*`[^`]*`\s*)\|', stripped)
        if not orig_name_match:
            continue  # not a data row; do not advance the EN row index
        if data_row_idx < len(en_output_names):
            en_name = en_output_names[data_row_idx]
            # Replace the backtick-wrapped name in the first column of the
            # ORIGINAL line (preserves leading whitespace and cell padding)
            new_lines[i] = re.sub(
                r'^(\s*\|\s*)`[^`]*`(\s*\|)',
                lambda m: f"{m.group(1)}`{en_name}`{m.group(2)}",
                line,
                count=1,
            )
        data_row_idx += 1

    new_table = '\n'.join(new_lines)
    translated_content = translated_content[:tr_outputs_match.start(1)] + new_table + translated_content[tr_outputs_match.end(1):]
    return translated_content


def translate_document(node_name, target_lang, lang_config, client, model):
    """Translate a single document"""
    
    # Read English source document
    source_file = DOCS_PATH / node_name / "en.md"
    if not source_file.exists():
        raise FileNotFoundError(f"English source not found: {source_file}")
    
    with open(source_file, 'r', encoding='utf-8') as f:
        full_en = f.read()

    # Same hex as en.md footer when present; fallback matches pipeline / English doc generation.
    src_fp_hex = extract_english_source_fingerprint_hex(full_en) or load_node_source_sha256(node_name)

    # Omit footer, disclaimer, and H1 title from LLM input; title is injected from frontend after translate.
    source_content = strip_leading_h1(strip_ai_disclaimer(strip_source_hash_footer(full_en)))
    
    # Build prompt using language-specific template
    prompt_template = lang_config.get('prompt_template', '')
    full_prompt = prompt_template + "\n\n" + source_content

    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "user", "content": full_prompt}
                ],
                temperature=0.3,
                stream=False
            )
            
            content = response.choices[0].message.content
            
            content = strip_ai_disclaimer(content)

            # Strip AI preamble ("Here is the translation...") in the target language
            content = strip_ai_preamble(content, target_lang)

            # Replace placeholder headings with actual headings
            content = replace_heading_placeholders(content, lang_config)

            # Localized node title from frontend display_name (not AI-translated)
            content = ensure_doc_title(strip_leading_h1(content), node_name, target_lang)

            # Drop any model-added localized fingerprint block; keep one English footer for traceability.
            content = strip_trailing_fingerprint_section(content)

            # Post-process: enforce English output names.  The AI sometimes translates output names
            # (e.g. 'positive' translated to the same word as 'negative') causing duplicates in the Outputs table.
            # We parse the en.md Outputs table and force the first column to match.
            content = _fix_output_names_in_translation(content, full_en)

            disclaimer = create_translated_disclaimer(target_lang, node_name, lang_config)
            footer = format_source_hash_footer(src_fp_hex) if src_fp_hex else ""
            final_content = compose_document(content, disclaimer, footer)
            if not src_fp_hex:
                logger.warning(
                    "No source fingerprint for %s; translated file has no SHA footer "
                    "(add footer to en.md or ensure ai_input/%s/basic_info.json has source_hash).",
                    node_name,
                    node_name,
                )

            return final_content
            
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise

def process_node(node_name, target_lang, lang_config, client, model, force=False):
    """
    Process a single node translation.
    When force=False, skips if target file already exists (do not overwrite).
    """
    output_file = DOCS_PATH / node_name / f"{target_lang}.md"
    if output_file.exists() and not force:
        logger.info(f"⏭️  Skip (already exists): {node_name}")
        return "skipped"

    try:
        logger.info(f"🤖 Translating: {node_name}")

        # Translate document
        translated_content = translate_document(node_name, target_lang, lang_config, client, model)
        
        # Save translated document
        output_dir = DOCS_PATH / node_name
        output_dir.mkdir(exist_ok=True)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(translated_content)
        
        logger.info(f"💾 Saved: {output_file}")
        logger.log(25, f"✅ Successfully translated: {node_name}")
        
        return "success"
        
    except Exception as e:
        logger.error(f"❌ Translation failed {node_name}: {e}")
        return "failed"


def translate_nodes_concurrently(nodes, concurrency, process_fn, max_consecutive_failures=5):
    """Translate nodes with a thread pool.

    ``process_fn(node_name)`` must return "success" | "failed" | "skipped".
    Returns (results_dict, aborted) where results_dict maps each outcome to a
    list of node names in COMPLETION order (nondeterministic for
    concurrency > 1), and ``aborted`` is True when the circuit breaker tripped
    (remaining not-yet-started tasks are cancelled).

    Breaker rule: with workers running in parallel, completions interleave, so
    a completion-order "consecutive failures" counter is meaningless — it can
    trip on unrelated failures during a mostly-healthy run, or stay silent
    during a real outage because one interleaved success resets it. Instead we
    trip on an aggregate condition that is independent of interleaving:
    at least ``max_consecutive_failures`` failures AND failures are at least
    half of everything completed so far (i.e. the API is mostly failing).
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    results = {"success": [], "failed": [], "skipped": []}
    aborted = False

    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        # Submit in order, consume in completion order
        future_to_node = {pool.submit(process_fn, n): n for n in nodes}
        for fut in as_completed(future_to_node):
            node_name = future_to_node[fut]
            if fut.cancelled():
                continue  # cancelled by the circuit breaker; not tallied
            try:
                result = fut.result()
            except Exception as e:  # defensive; process_node already catches
                logger.error(f"❌ Translation crashed {node_name}: {e}")
                result = "failed"
            if result not in results:
                result = "failed"
            results[result].append(node_name)
            logger.info(f"[{sum(len(v) for v in results.values())}/{len(nodes)}] {node_name}: {result}")

            completed = sum(len(v) for v in results.values())
            failed = len(results["failed"])
            if failed >= max_consecutive_failures and failed * 2 >= completed:
                for other in future_to_node:
                    other.cancel()  # no-op for already-running futures
                aborted = True
                break

    return results, aborted

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Batch translate docs using prepared batch file")
    parser.add_argument("--lang", required=True, help="Target language code")
    parser.add_argument("--mode", choices=("test", "all"), default="all",
                        help="test = limit to --count, all = whole batch (default: all)")
    parser.add_argument("--count", type=int, default=20,
                        help="Max nodes in test mode (default: 20)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing translations")
    parser.add_argument("--node-list", type=str, default=None,
                        help="Comma-separated list of node names to translate (overrides batch file)")
    parser.add_argument("--node-list-file", type=str, default=None,
                        help="Path to JSON file with {'nodes': ['NodeA', 'NodeB']} (overrides batch file)")
    parser.add_argument("--concurrency", type=int, default=1,
                        help="Parallel translation workers (default: 1 = sequential, with the "
                             "usual every-5-nodes rest). >1 uses a thread pool and skips the "
                             "periodic rest; retries/backoff still apply per request.")
    args = parser.parse_args()
    target_lang = args.lang
    mode = args.mode
    force = args.force
    MAX_CONCURRENCY = 32
    if args.concurrency > MAX_CONCURRENCY:
        print(f"⚠️  Warning: --concurrency {args.concurrency} is too high; capping at {MAX_CONCURRENCY} to avoid API rate-limit storms.")
    concurrency = max(1, min(args.concurrency, MAX_CONCURRENCY))

    # Load translation config
    with open(TRANSLATION_CONFIG_FILE, 'r', encoding='utf-8') as f:
        translation_config = json.load(f)
    
    if target_lang not in translation_config:
        print(f"❌ Error: Unknown language '{target_lang}'")
        print(f"Available: {', '.join(translation_config.keys())}")
        sys.exit(1)
    
    lang_config = translation_config[target_lang]

    # Determine which nodes to translate
    nodes_to_translate: list[str] = []

    if args.node_list:
        # Direct node list from CLI argument
        nodes_to_translate = [n.strip() for n in args.node_list.split(",") if n.strip()]
        print(f"📋 Using CLI node list: {len(nodes_to_translate)} nodes")
    elif args.node_list_file:
        # Node list from JSON file
        nl_path = Path(args.node_list_file)
        if not nl_path.exists():
            print(f"❌ Error: Node list file not found: {nl_path}")
            sys.exit(1)
        with open(nl_path, 'r', encoding='utf-8') as f:
            nl_data = json.load(f)
        nodes_to_translate = nl_data.get('nodes', [])
        print(f"📋 Using node list file: {len(nodes_to_translate)} nodes")
    else:
        # Load batch file (default behavior)
        batch_file = TRANSLATION_BATCHES_DIR / f"batch_{target_lang}.json"
        if not batch_file.exists():
            print(f"❌ Error: Batch file not found: {batch_file}")
            print(f"   Please run: python3 prepare_translation.py --lang {target_lang}")
            sys.exit(1)

        with open(batch_file, 'r', encoding='utf-8') as f:
            batch_data = json.load(f)

        nodes_to_translate = batch_data.get('nodes', [])
        if mode == "test":
            nodes_to_translate = nodes_to_translate[:args.count]

        print(f"📊 Batch prepared: {batch_data.get('total', 0)} nodes")
    print(f"💡 {'Test' if mode == 'test' else 'Full'} mode: Translating {len(nodes_to_translate)} nodes")
    print()
    print(f"Target language: {lang_config['name']} ({target_lang})")
    print(f"API: {DEFAULT_MODEL}")
    print(f"Output: {DOCS_PATH}")
    print(f"Mode: {'Force retranslate (overwrite)' if force else 'Normal (skip existing, do not overwrite)'}")
    print()
    
    logger.info("=" * 80)
    logger.info("🚀 Batch Translation Started")
    logger.info(f"📊 Total: {len(nodes_to_translate)} nodes")
    logger.info(f"🌐 Language: {lang_config['name']} ({target_lang})")
    logger.info(f"🔧 API: {DEFAULT_MODEL}")
    logger.info(f"⚙️  Batch size: {DEFAULT_BATCH_SIZE}")
    logger.info("=" * 80)
    logger.info("")

    # Create the API client once and reuse it for every node in the batch.
    # Imported lazily so the module's pure post-processing helpers stay
    # importable (and testable) without the openai package installed.
    from openai import OpenAI
    # base_url=None lets the SDK fall back to OPENAI_BASE_URL or its default
    # endpoint when API_BASE_URL is unset (an empty string would not).
    client = OpenAI(api_key=DEFAULT_API_KEY, base_url=DEFAULT_BASE_URL or None)

    # Translate documents
    success_count = 0
    failed_count = 0
    skipped_count = 0
    consecutive_failures = 0
    MAX_CONSECUTIVE_FAILURES = 5
    completed_nodes = []  # Track completed nodes for batch update

    def _tally(result, node_name):
        """Update counters for one finished node; return True if the
        consecutive-failure circuit breaker tripped."""
        nonlocal success_count, failed_count, skipped_count, consecutive_failures
        if result == "success":
            success_count += 1
            consecutive_failures = 0  # Reset counter on success
            completed_nodes.append(node_name)  # Track for batch update
        elif result == "failed":
            failed_count += 1
            consecutive_failures += 1
        elif result == "skipped":
            skipped_count += 1
            consecutive_failures = 0  # Reset counter on skip
        return consecutive_failures >= MAX_CONSECUTIVE_FAILURES

    def _abort_with_failure_summary():
        logger.error("")
        logger.error("=" * 80)
        logger.error(f"❌ Consecutive failures reached {MAX_CONSECUTIVE_FAILURES}, terminating")
        logger.error("=" * 80)
        logger.error(f"Success: {success_count}, Failed: {failed_count}, Skipped: {skipped_count}")
        logger.error("Please check:")
        logger.error("  1. API key is correctly configured")
        logger.error("  2. Network connection is stable")
        logger.error("  3. API has sufficient balance")
        logger.error("=" * 80)
        print()
        print("=" * 80)
        print(f"❌ Consecutive failures: {MAX_CONSECUTIVE_FAILURES}, terminated automatically")
        print(f"Success: {success_count}, Failed: {failed_count}, Skipped: {skipped_count}")
        print(f"📁 Log: {log_file}")
        print("=" * 80)
        sys.exit(1)

    aborted = False

    if concurrency > 1 and len(nodes_to_translate) > 1:
        # Concurrent path: thread pool over the shared client (httpx-based,
        # thread-safe). The periodic every-5-nodes rest is skipped here;
        # per-request retry/backoff in translate_document still applies.
        logger.info(f"⚡ Concurrency: {concurrency} workers")
        results, aborted = translate_nodes_concurrently(
            nodes_to_translate,
            concurrency,
            lambda n: process_node(n, target_lang, lang_config, client, DEFAULT_MODEL, force=force),
            max_consecutive_failures=MAX_CONSECUTIVE_FAILURES,
        )
        success_count = len(results["success"])
        failed_count = len(results["failed"])
        skipped_count = len(results["skipped"])
        completed_nodes = results["success"]
    else:
        # Sequential path (default): identical to the original behavior.
        for idx, node_name in enumerate(nodes_to_translate, 1):
            logger.info("")
            logger.info(f"[{idx}/{len(nodes_to_translate)}] Processing node: {node_name}")
            logger.info("-" * 60)

            result = process_node(
                node_name,
                target_lang,
                lang_config,
                client,
                DEFAULT_MODEL,
                force=force
            )

            if _tally(result, node_name):
                aborted = True
                break

            # Rate limiting
            if idx % DEFAULT_BATCH_SIZE == 0 and idx < len(nodes_to_translate):
                logger.info("⏸️  Batch rest for 2 seconds...")
                time.sleep(2)

    if aborted:
        _abort_with_failure_summary()
    
    logger.info("")
    logger.info("=" * 80)
    logger.info("📊 Translation Summary")
    logger.info("=" * 80)
    logger.info(f"✅ Success: {success_count}")
    logger.info(f"❌ Failed: {failed_count}")
    logger.info(f"⏭️  Skipped: {skipped_count}")
    logger.info(f"📁 Log file: {log_file}")
    logger.info("")
    
    # Update translation status in JSON
    if completed_nodes:
        logger.info("=" * 80)
        logger.info("🔄 Updating translation status in JSON...")
        logger.info("=" * 80)
        batch_update_translations({target_lang: completed_nodes})
        logger.info(f"✅ Removed {target_lang} from {len(completed_nodes)} nodes' missing languages")
        logger.info("")
    
    print()
    print("=" * 80)
    print(f"✅ Translation completed! Success: {success_count}, Failed: {failed_count}, Skipped: {skipped_count}")
    if completed_nodes:
        print(f"📝 Updated missing_nodes_report.json ({len(completed_nodes)} nodes)")
    print(f"📁 Log: {log_file}")
    print("=" * 80)

if __name__ == "__main__":
    main()
