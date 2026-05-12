#!/usr/bin/env python3
"""
Batch translate documentation using AI
Trusts the batch list from prepare_translation.py (files already verified as missing)
"""

import argparse
import json
import os
import sys
import time
import logging
from pathlib import Path
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv
from hash_footer import strip_source_hash_footer
from update_translation_status import batch_update_translations

# Load environment variables
DOC_AUTOMATION_PATH = Path(__file__).parent
env_path = DOC_AUTOMATION_PATH.parent / '.env'
load_dotenv(env_path)

# Paths from environment variables
EMBEDDED_DOCS_PATH = Path(os.getenv('EMBEDDED_DOCS_PATH', DOC_AUTOMATION_PATH.parent))
DOCS_PATH = EMBEDDED_DOCS_PATH / "comfyui_embedded_docs" / "docs"
TRANSLATION_BATCHES_DIR = DOC_AUTOMATION_PATH / "translation_batches"
TRANSLATION_CONFIG_FILE = DOC_AUTOMATION_PATH / "translation_config.json"
LOGS_DIR = DOC_AUTOMATION_PATH / "logs"

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
DEFAULT_API_KEY = os.getenv('DEEPSEEK_API_KEY', '')
DEFAULT_BASE_URL = "https://api.deepseek.com"
DEFAULT_MODEL = "deepseek-chat"
DEFAULT_BATCH_SIZE = 5

# Custom log level for success
logging.addLevelName(25, "SUCCESS")

def create_disclaimer(target_lang, node_name, lang_config):
    """Create disclaimer header for translated document"""
    github_link = f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}/comfyui_embedded_docs/docs/{node_name}/{target_lang}.md"
    disclaimer_text = lang_config.get('disclaimer', 'This documentation was AI-generated.')
    edit_text = {
        'zh': '在 GitHub 上编辑',
        'es': 'Editar en GitHub',
        'fr': 'Modifier sur GitHub',
        'ja': 'GitHub で編集',
        'ko': 'GitHub에서 편집',
        'ru': 'Редактировать на GitHub',
        'zh-TW': '在 GitHub 上編輯',
        'ar': 'تحرير على GitHub',
        'tr': "GitHub'da Düzenle",
        'pt-BR': 'Editar no GitHub',
        'fa': 'ویرایش در GitHub'
    }.get(target_lang, 'Edit on GitHub')
    
    return f"> {disclaimer_text} [{edit_text}]({github_link})\n\n"

def remove_ai_disclaimer(content):
    """Remove any AI-generated disclaimer from content"""
    lines = content.split('\n')
    # Remove first line if it's a disclaimer
    if lines and lines[0].startswith('>'):
        # Remove disclaimer and following empty line
        if len(lines) > 1 and lines[1].strip() == '':
            return '\n'.join(lines[2:])
        return '\n'.join(lines[1:])
    return content

def replace_heading_placeholders(content, lang_config):
    """Replace placeholder headings with actual headings"""
    content = content.replace('{heading_overview}', f"## {lang_config.get('heading_overview', 'Overview')}")
    content = content.replace('{heading_inputs}', f"## {lang_config.get('heading_inputs', 'Inputs')}")
    content = content.replace('{heading_outputs}', f"## {lang_config.get('heading_outputs', 'Outputs')}")
    return content

def translate_document(node_name, target_lang, lang_config, api_key, base_url, model):
    """Translate a single document"""
    
    # Read English source document
    source_file = DOCS_PATH / node_name / "en.md"
    if not source_file.exists():
        raise FileNotFoundError(f"English source not found: {source_file}")
    
    with open(source_file, 'r', encoding='utf-8') as f:
        source_content = f.read()

    # Omit English-only source fingerprint footer (not translated into other locales)
    source_content = strip_source_hash_footer(source_content)
    
    # Build prompt using language-specific template
    prompt_template = lang_config.get('prompt_template', '')
    full_prompt = prompt_template + "\n\n" + source_content
    
    # Call AI API
    client = OpenAI(api_key=api_key, base_url=base_url)
    
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
            
            # Remove any AI-generated disclaimer
            content = remove_ai_disclaimer(content)
            
            # Replace placeholder headings with actual headings
            content = replace_heading_placeholders(content, lang_config)
            
            # Add our own disclaimer with correct link
            final_content = create_disclaimer(target_lang, node_name, lang_config) + content
            
            return final_content
            
        except Exception as e:
            if attempt < max_retries - 1:
                wait_time = (attempt + 1) * 2
                logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
                time.sleep(wait_time)
            else:
                raise

def process_node(node_name, target_lang, lang_config, api_key, base_url, model, force=False):
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
        translated_content = translate_document(node_name, target_lang, lang_config, api_key, base_url, model)
        
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

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Batch translate docs using prepared batch file")
    parser.add_argument("--lang", required=True, help="Target language code")
    parser.add_argument("--mode", choices=("test", "all"), default="all",
                        help="test = limit to --count, all = whole batch (default: all)")
    parser.add_argument("--count", type=int, default=20,
                        help="Max nodes in test mode (default: 20)")
    parser.add_argument("--force", action="store_true", help="Overwrite existing translations")
    args = parser.parse_args()
    target_lang = args.lang
    mode = args.mode
    force = args.force

    # Load translation config
    with open(TRANSLATION_CONFIG_FILE, 'r', encoding='utf-8') as f:
        translation_config = json.load(f)
    
    if target_lang not in translation_config:
        print(f"❌ Error: Unknown language '{target_lang}'")
        print(f"Available: {', '.join(translation_config.keys())}")
        sys.exit(1)
    
    lang_config = translation_config[target_lang]
    
    # Load batch file
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
    
    # Translate documents
    success_count = 0
    failed_count = 0
    skipped_count = 0
    consecutive_failures = 0
    MAX_CONSECUTIVE_FAILURES = 5
    completed_nodes = []  # Track completed nodes for batch update
    
    for idx, node_name in enumerate(nodes_to_translate, 1):
        logger.info("")
        logger.info(f"[{idx}/{len(nodes_to_translate)}] Processing node: {node_name}")
        logger.info("-" * 60)
        
        result = process_node(
            node_name,
            target_lang,
            lang_config,
            DEFAULT_API_KEY,
            DEFAULT_BASE_URL,
            DEFAULT_MODEL,
            force=force
        )
        
        if result == "success":
            success_count += 1
            consecutive_failures = 0  # Reset counter on success
            completed_nodes.append(node_name)  # Track for batch update
        elif result == "failed":
            failed_count += 1
            consecutive_failures += 1
            
            # Check if we've hit the consecutive failure limit
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
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
        elif result == "skipped":
            skipped_count += 1
            consecutive_failures = 0  # Reset counter on skip
        
        # Rate limiting
        if idx % DEFAULT_BATCH_SIZE == 0 and idx < len(nodes_to_translate):
            logger.info("⏸️  Batch rest for 2 seconds...")
            time.sleep(2)
    
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
