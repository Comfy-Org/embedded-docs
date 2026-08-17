#!/usr/bin/env python3
"""
Main control script for ComfyUI node documentation automation.
Orchestrates: scan -> prepare -> generate/translate -> update reports.

Usage
-----

  # === Interactive (default when no args) ===
  python3 main.py
  python3 main.py --interactive
  # Then choose: Scan / Generate docs / Translate from the menu.

  # === Document generation (English, non-interactive) ===
  python3 main.py --mode test [--count N] [--force]

  # Generate default number of nodes (test mode, 20 nodes)
  python3 main.py --mode test

  # Generate N nodes (test mode)
  python3 main.py --count 50

  # Generate all missing nodes
  python3 main.py --mode all

  # Full refresh: English only unless you opt in to translation on CLI:
  python3 main.py --mode regenerate-all
  python3 main.py --mode regenerate-all --also-translate-all
  # Interactive menu 7) defaults to running full translation after English; CLI needs the flag above.

  # Generate/force-regenerate a single node
  python3 main.py --mode node --node <NodeName> [--force]

  # Update an existing node doc (re-reads source, sends current doc as reference so
  # the AI updates params/outputs while preserving manual edits)
  python3 main.py --mode node --node <NodeName> --force

  # Only scan, no generation
  python3 main.py --scan-only

  # === Fix existing docs (no AI) ===
  python3 main.py --mode fix --fix-action doc-titles
  python3 main.py --mode fix --fix-action doc-titles --hash-mode preserve --dry-run
  python3 main.py --mode fix --fix-action doc-titles --hash-mode update
  python3 main.py --mode fix --fix-action doc-titles --node KSampler --lang zh

  # === Translation (other languages) ===
  python3 main.py --translate --lang <LANG> [--mode MODE] [--count N] [--force]

  # Translate to one language (test: 20 nodes)
  python3 main.py --translate --lang zh --count 10
  python3 main.py --translate --lang pt-BR --mode all

  # Translate a single node (one language, or all languages)
  python3 main.py --translate --lang zh --mode node --node KSampler
  python3 main.py --translate --all-languages --mode node --node KSampler

  # Translate to all supported languages
  python3 main.py --translate --all-languages --count 10
  python3 main.py --translate --all-languages --mode all

  # Force retranslate ALL locales for EVERY node that has en.md (ignores missing report)
  python3 main.py --retranslate-all-languages
  python3 main.py --translate --all-languages --mode all --force --force-all-translation-nodes

  # Force retranslate existing docs (batches from missing report unless --force-all-translation-nodes)
  python3 main.py --translate --lang zh --mode all --force

  # Supported languages: zh, zh-TW, es, fr, ja, ko, ru, ar, tr, pt-BR, fa

Options
-------
  --mode       test | all | resume | node | changed | regenerate-all | fix  (default: test)
  --fix-action doc-titles  (with --mode fix; default doc-titles)
  --fix-scope  test | all  (with --mode fix; default all)
  --hash-mode  preserve | update  (with --mode fix; default preserve)
  --dry-run    With --mode fix: preview title fixes without writing files
  --count      N nodes in test mode         (default: 20)
  --node       Node name (required with --mode node)
  --force      Overwrite existing docs/translations
  --prepare-limit  Only with --mode regenerate-all: prepare & regenerate first N nodes
  --also-translate-all  Only with --mode regenerate-all: after English, run all-languages translation (mode=all, force)
  --translate  Run translation workflow instead of generation
  --lang       Target language (required with --translate)
  --all-languages  Translate to all 11 languages
  --force-all-translation-nodes  Only with --translate: batch every node with en.md (prepare_translation --force-all-nodes)
  --retranslate-all-languages    Shorthand: all langs + mode all + force + force-all-translation-nodes

  Translated *.md files append the same English SHA footer line as en.md (trace English source version).

  # Interactive mode (no args, or --interactive): menu-driven
  python3 main.py
  python3 main.py --interactive
"""

import os
import sys
import subprocess
from pathlib import Path

from lib.paths import REPO_ROOT, load_dotenv

load_dotenv()
from datetime import datetime

# Supported languages for translation
LANGUAGES = ['zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']
LANG_NAMES = {
    'zh': '简体中文', 'zh-TW': '繁體中文', 'es': 'Español', 'fr': 'Français',
    'ja': '日本語', 'ko': '한국어', 'ru': 'Русский', 'ar': 'العربية',
    'tr': 'Türkçe', 'pt-BR': 'Português (BR)', 'fa': 'فارسی',
}


class DocumentationWorkflow:
    """Main workflow controller for documentation generation"""
    
    def __init__(self):
        self.repo_root = REPO_ROOT
        self.script_dir = self.repo_root / "scripts"
        self.scan_script = self.script_dir / "scan_missing_nodes.py"
        self.prepare_script = self.script_dir / "prepare_ai_input.py"
        self.generate_script = self.script_dir / "batch_generate_docs.py"
        self.prepare_translation_script = self.script_dir / "prepare_translation.py"
        self.translate_script = self.script_dir / "batch_translate_docs.py"
        self.update_params_script = self.script_dir / "update_param_translations.py"
        self.sync_frontend_script = self.script_dir / "sync_frontend_translations.py"
        self.sync_to_comfy_docs_script = self.script_dir / "sync_to_comfy_docs.py"
        self.fix_doc_titles_script = self.script_dir / "fix_doc_titles.py"

        fp = os.getenv("COMFYUI_FRONTEND_PATH", "").strip()
        self.frontend_path = Path(fp) if fp else Path("")
    
    def run_command(self, script: Path, args: list, description: str) -> bool:
        """Run a Python script with arguments"""
        print(f"\n{'=' * 80}")
        print(f"🚀 {description}")
        print(f"{'=' * 80}\n")
        
        cmd = ["python3", str(script)] + args
        env = os.environ.copy()
        prefix = str(self.repo_root)
        env["PYTHONPATH"] = prefix + (os.pathsep + env["PYTHONPATH"] if env.get("PYTHONPATH") else "")
        result = subprocess.run(cmd, cwd=self.repo_root, env=env)
        
        if result.returncode != 0:
            print(f"\n❌ Failed: {description}")
            return False
        
        print(f"\n✅ Completed: {description}")
        return True
    
    def scan_nodes(self) -> bool:
        """Step 1: Scan for missing nodes"""
        return self.run_command(
            self.scan_script,
            [],
            "Step 1: Scanning for missing node documentation"
        )
    
    def prepare_nodes(self, mode: str, count: int = None, node_name: str = None) -> bool:
        """Step 2: Prepare AI input for nodes"""
        args = [mode]
        
        if mode == "test" and count:
            args.append(str(count))
        elif mode == "node" and node_name:
            args.append(node_name)
        
        return self.run_command(
            self.prepare_script,
            args,
            f"Step 2: Preparing AI input ({mode} mode)"
        )
    
    def generate_docs(self, mode: str, count: int = None, node_name: str = None, force: bool = False) -> bool:
        """Step 3: Generate documentation with AI"""
        args = [mode]

        if mode == "test" and count:
            args.extend(["--count", str(count)])
        elif mode == "node" and node_name:
            args.extend(["--node", node_name])
        # "changed" mode: batch_generate_docs.py reads batch_nodes.json prepared by prepare_ai_input.py

        if force:
            args.append("--force")

        return self.run_command(
            self.generate_script,
            args,
            f"Step 3: Generating documentation ({mode} mode)"
        )
    
    def update_reports(self) -> bool:
        """Step 4: Update all reports"""
        print(f"\n{'=' * 80}")
        print("🔄 Step 4: Updating reports")
        print(f"{'=' * 80}\n")
        
        # Re-scan to update missing_nodes_report.json
        if not self.run_command(
            self.scan_script,
            [],
            "Updating missing_nodes_report.json"
        ):
            return False
        
        print(f"\n✅ All reports updated successfully")
        return True
    
    def prepare_translation(self, lang: str, mode: str, count: int = None, force_all_nodes: bool = False) -> bool:
        """Prepare translation batch for a specific language"""
        args = ["--lang", lang, "--mode", mode]

        if mode == "test" and count:
            args.extend(["--count", str(count)])

        if force_all_nodes:
            args.append("--force-all-nodes")

        return self.run_command(
            self.prepare_translation_script,
            args,
            f"Preparing {lang} translation batch ({mode} mode{' + force-all-nodes' if force_all_nodes else ''})"
        )
    
    def translate_docs(self, lang: str, mode: str, count: int = None, force: bool = False, node_name: str = None, concurrency: int = 1) -> bool:
        """Translate documentation to a specific language"""
        args = ["--lang", lang, "--mode", mode]

        if mode == "test" and count:
            args.extend(["--count", str(count)])

        if node_name:
            # Single-node translation: bypass the batch file entirely
            args.extend(["--node-list", node_name])

        if force:
            args.append("--force")

        if concurrency > 1:
            args.extend(["--concurrency", str(concurrency)])

        return self.run_command(
            self.translate_script,
            args,
            f"Translating to {lang} ({mode} mode)"
        )
    
    def sync_frontend_translations(self) -> bool:
        """Sync and export frontend translations to node_translations.json"""
        if not self.frontend_path.exists():
            print(f"⚠️  Warning: Frontend path not found: {self.frontend_path}")
            print("   Skipping frontend translation sync")
            return True  # Don't fail if frontend not found
        
        return self.run_command(
            self.sync_frontend_script,
            [str(self.frontend_path), "--export"],
            "Syncing frontend translations"
        )
    
    def update_param_translations(self, lang: str) -> bool:
        """Update parameter translations from frontend for a specific language"""
        return self.run_command(
            self.update_params_script,
            ["--lang", lang],
            f"Updating parameter translations for {lang}"
        )
    
    def run_translation_workflow(
        self,
        lang: str,
        mode: str = "test",
        count: int = 10,
        force: bool = False,
        skip_initial_scan: bool = False,
        skip_frontend_sync: bool = False,
        force_all_nodes: bool = False,
        node_name: str = None,
        concurrency: int = 1,
    ):
        """Run translation workflow for a specific language"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n" + "=" * 80)
        print("ComfyUI Documentation Translation - Main Workflow")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        print(f"Target language: {lang}")
        print(f"Mode: {mode}")
        if node_name:
            print(f"Node: {node_name}")
        if mode == "test" and not node_name:
            print(f"Count: {count} nodes")
        print(f"Force retranslate: {force}")
        print(f"Prepare batch from all nodes with en.md: {force_all_nodes}")
        print("=" * 80)

        # Step 0a: Sync frontend translations (unless skipped for multi-language)
        if not skip_frontend_sync:
            print(f"\n🔄 Step 0a: Syncing frontend translations...")
            if not self.sync_frontend_translations():
                print("\n⚠️  Warning: Frontend translation sync failed, but continuing...")

        # Step 0b: Scan to update missing_nodes_report.json (unless skipped for multi-language)
        if not skip_initial_scan:
            print(f"\n📊 Step 0b: Scanning to update missing translations...")
            if not self.scan_nodes():
                print("\n❌ Translation workflow failed at Step 0b: Scan")
                return False

        # Step 1: Prepare translation batch (missing report or every node with en.md)
        # Skipped for single-node translation: --node-list is passed straight to the translator.
        if node_name:
            print(f"\n🔧 Step 1: Single node '{node_name}' — batch preparation skipped.")
        else:
            print(f"\n🔧 Step 1: Preparing {lang} translation batch...")
            if not self.prepare_translation(lang, mode, count, force_all_nodes=force_all_nodes):
                print("\n❌ Translation workflow failed at Step 1: Prepare")
                return False

        # Step 2: Translate documents (trusts batch list, updates JSON incrementally)
        print(f"\n🤖 Step 2: Translating to {lang}...")
        if not self.translate_docs(lang, mode, count, force, node_name=node_name, concurrency=concurrency):
            print("\n❌ Translation workflow failed at Step 2: Translate")
            return False
        
        # Step 3: Update parameter translations from frontend
        print(f"\n🔄 Step 3: Updating parameter names with frontend translations...")
        if not self.update_param_translations(lang):
            print("\n⚠️  Warning: Parameter translation update failed, but continuing...")
            # Don't fail the workflow if parameter update fails
        
        # Success summary
        end_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 80)
        print("✅ Translation Workflow Completed!")
        print("=" * 80)
        print(f"Started:  {timestamp}")
        print(f"Finished: {end_timestamp}")
        print(f"Language: {lang}")
        print("\nNote: missing_nodes_report.json updated incrementally")
        print("      Parameter names updated with frontend translations")
        print("=" * 80 + "\n")
        
        return True
    
    def run_all_languages_translation(self, mode: str = "test", count: int = 10, force: bool = False, force_all_nodes: bool = False, node_name: str = None, concurrency: int = 1):
        """Run translation workflow for all supported languages"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        languages = ['zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']

        print("\n" + "=" * 80)
        print("ComfyUI Documentation Translation - ALL LANGUAGES")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        print(f"Languages: {', '.join(languages)}")
        print(f"Mode: {mode}")
        if node_name:
            print(f"Node: {node_name}")
        if mode == "test" and not node_name:
            print(f"Count per language: {count} nodes")
        print(f"Force retranslate: {force}")
        print(f"Prepare batch from all nodes with en.md: {force_all_nodes}")
        print("=" * 80)
        
        # Sync frontend translations first
        print("\n🔄 Syncing frontend translations...")
        if not self.sync_frontend_translations():
            print("\n⚠️  Warning: Frontend translation sync failed, but continuing...")
        
        # Initial scan to populate missing_nodes_report.json
        print("\n📊 Initial scan to identify missing translations...")
        if not self.scan_nodes():
            print("\n❌ Scan failed")
            return False
        
        results = {}
        
        for lang in languages:
            print(f"\n{'=' * 80}")
            print(f"🌐 Processing language: {lang}")
            print(f"{'=' * 80}")
            
            # Skip initial scan and frontend sync for each language (already done once)
            success = self.run_translation_workflow(
                lang,
                mode,
                count,
                force,
                skip_initial_scan=True,
                skip_frontend_sync=True,
                force_all_nodes=force_all_nodes,
                node_name=node_name,
                concurrency=concurrency,
            )
            results[lang] = success
            
            if not success:
                print(f"\n⚠️  Warning: Translation failed for {lang}, continuing with next language...")
        
        # Final scan to update complete status
        print("\n🔄 Final scan to ensure all data is current...")
        self.scan_nodes()
        
        # Final summary
        end_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 80)
        print("📊 ALL LANGUAGES TRANSLATION SUMMARY")
        print("=" * 80)
        print(f"Started:  {timestamp}")
        print(f"Finished: {end_timestamp}")
        print("\nResults:")
        for lang, success in results.items():
            status = "✅ Success" if success else "❌ Failed"
            print(f"  {lang}: {status}")
        
        successful = sum(1 for s in results.values() if s)
        print(f"\nTotal: {successful}/{len(languages)} languages completed successfully")
        print("=" * 80 + "\n")
        
        return all(results.values())

    def run_fix_doc_titles_workflow(
        self,
        mode: str = "all",
        count: int = 20,
        node_name: str = None,
        lang: str = None,
        dry_run: bool = False,
        sync_frontend: bool = True,
        hash_mode: str = "preserve",
    ) -> bool:
        """Fix H1 titles in existing docs (missing / duplicate / frontend mismatch). No AI."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n" + "=" * 80)
        print("ComfyUI Documentation Fix — Document Titles")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        print(f"Scope: {mode}" + (f" (first {count} files)" if mode == "test" else ""))
        print(f"Dry run: {dry_run}")
        print(f"Hash mode: {hash_mode}")
        print(f"Sync frontend first: {sync_frontend}")
        if node_name:
            print(f"Node: {node_name}")
        if lang:
            print(f"Language: {lang}")
        print("=" * 80)

        if sync_frontend:
            print("\n🔄 Step 1: Syncing frontend translations...")
            if not self.sync_frontend_translations():
                print("\n⚠️  Frontend sync failed; continuing with existing node_translations.json")

        args = ["--mode", mode]
        if mode == "test":
            args.extend(["--count", str(count)])
        if node_name:
            args.extend(["--node", node_name])
        if lang:
            args.extend(["--lang", lang])
        if dry_run:
            args.append("--dry-run")
        args.extend(["--hash-mode", hash_mode])

        ok = self.run_command(
            self.fix_doc_titles_script,
            args,
            "Fix document titles (frontend display_name)",
        )

        end_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 80)
        if ok:
            print("✅ Fix Titles Workflow Completed!")
        else:
            print("❌ Fix Titles Workflow Failed")
        print("=" * 80)
        print(f"Started:  {timestamp}")
        print(f"Finished: {end_timestamp}")
        print("=" * 80 + "\n")
        return ok
    
    def _load_changed_nodes_from_scan(self) -> list[str]:
        """Load the list of changed nodes from the latest scan report."""
        import json
        scan_report = self.repo_root / "data" / "missing_nodes_report.json"
        if not scan_report.exists():
            print("  ⚠️  No scan report found (missing_nodes_report.json)")
            return []
        try:
            with open(scan_report, "r", encoding="utf-8") as f:
                report = json.load(f)
            changed = report.get("changed_nodes", [])
            print(f"  📋 Found {len(changed)} changed nodes in scan report")
            return changed
        except (json.JSONDecodeError, OSError) as e:
            print(f"  ⚠️  Could not read scan report: {e}")
            return []

    def run_changed_workflow(self, force: bool = False, concurrency: int = 1):
        """Run workflow for nodes with changed source code"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n" + "=" * 80)
        print("ComfyUI Documentation Automation - Changed Nodes Workflow")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        print(f"Force regenerate: {force}")
        print("=" * 80)

        # Step 1: Scan to detect changed nodes
        print("\n📊 Step 1: Scanning to identify changed nodes...")
        if not self.scan_nodes():
            print("\n❌ Workflow failed at Step 1: Scan")
            return False

        # Step 2: Prepare AI input for changed nodes
        print("\n🔧 Step 2: Preparing AI input for changed nodes...")
        if not self.run_command(
            self.prepare_script,
            ["changed"],
            "Step 2: Preparing changed nodes"
        ):
            print("\n❌ Workflow failed at Step 2: Prepare")
            return False

        # Step 3: Generate documentation (force=True so existing docs get overwritten)
        # ⚠️ Save changed nodes BEFORE generation because batch_generate_docs.py
        # re-runs scan_missing_nodes.py in _update_reports(), which overwrites
        # the changed_nodes field in the scan report to empty.
        changed_nodes = self._load_changed_nodes_from_scan()
        print("\n🤖 Step 3: Generating documentation for changed nodes...")
        if not self.generate_docs("changed", force=True):
            print("\n❌ Workflow failed at Step 3: Generate")
            return False

        # Step 4: Re-translate changed nodes for all languages
        # Use the saved list from before generation (Step 3's batch_generate_docs
        # re-runs scan and overwrites the changed_nodes field in the report)
        if changed_nodes:
            print(f"\n🌐 Step 4: Re-translating {len(changed_nodes)} changed nodes for all languages...")
            node_list_str = ",".join(n["name"] if isinstance(n, dict) else n for n in changed_nodes)
            languages = ['zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']

            # Sync frontend translations first
            print("\n🔄 Syncing frontend translations...")
            self.sync_frontend_translations()

            for lang in languages:
                print(f"\n{'=' * 60}")
                print(f"🌐 Translating changed nodes to {lang}...")
                print(f"{'=' * 60}")
                tr_args = ["--lang", lang, "--node-list", node_list_str, "--force"]
                if concurrency > 1:
                    tr_args.extend(["--concurrency", str(concurrency)])
                self.run_command(
                    self.translate_script,
                    tr_args,
                    f"Re-translating changed nodes to {lang}"
                )
                # Same post-translation correction as the regular translation
                # workflow (Step 3 there): sync param/output names from the
                # frontend i18n so re-translated docs match the UI labels.
                if not self.update_param_translations(lang):
                    print(f"\n⚠️  Warning: Parameter translation update failed for {lang}, but continuing...")
            print(f"\n✅ Step 4 complete: {len(changed_nodes)} changed nodes re-translated across {len(languages)} languages.")
        else:
            print("\n⏭️  Step 4: No changed nodes to re-translate (skipping).")

        # Step 5: Final scan to update reports
        print("\n🔄 Step 5: Final scan to update all reports...")
        if not self.scan_nodes():
            print("\n❌ Workflow failed at Step 5: Final Update")
            return False

        end_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 80)
        print("✅ Changed Nodes Workflow Completed!")
        print("=" * 80)
        print(f"Started:  {timestamp}")
        print(f"Finished: {end_timestamp}")
        print("=" * 80 + "\n")

        return True

    def run_regenerate_all_workflow(self, prepare_limit=None, translate_all_languages: bool = False) -> bool:
        """Scan → prepare AI input for every node from all_nodes_info.json → regenerate all English docs with --force.

        Use ``prepare_limit`` for a capped dry run (first N nodes by name).

        If ``translate_all_languages`` is True, runs an all-languages translation pass after English regeneration
        (``mode=all``, ``force=True``, ``force_all_nodes=True`` so every ``en.md`` is re-translated).

        Intended for extractor / pipeline changes or policy updates that require rewriting every ``en.md``,
        not for day-to-day use (heavy on disk, API quota, and time).
        """
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\n" + "=" * 80)
        print("ComfyUI Documentation Automation — FULL REGENERATE (all nodes)")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        lim_msg = str(prepare_limit) if prepare_limit is not None else "none (full tree)"
        print(f"Prepare limit: {lim_msg}")
        print(f"Follow with all-language translation: {'yes' if translate_all_languages else 'no'}")
        print("=" * 80)

        print("\n📊 Step 1: Scan (refresh all_nodes_info + reports)...")
        if not self.scan_nodes():
            print("\n❌ Failed at Step 1: Scan")
            return False

        prep_args = ["regenerate-all"]
        if prepare_limit is not None:
            prep_args.append(str(prepare_limit))

        print("\n🔧 Step 2: Prepare AI input for ALL scanned nodes (may take long)...")
        if not self.run_command(
            self.prepare_script,
            prep_args,
            "Step 2: prepare_ai_input.py regenerate-all",
        ):
            print("\n❌ Failed at Step 2: Prepare")
            return False

        print("\n🤖 Step 3: Regenerate ALL English docs (batch_generate_docs all --force)...")
        if not self.generate_docs("all", force=True):
            print("\n❌ Failed at Step 3: Generate")
            return False

        print("\n🔄 Step 4: Final scan...")
        if not self.scan_nodes():
            print("\n❌ Failed at Step 4: Final scan")
            return False

        if translate_all_languages:
            print("\n🌐 Step 5: Translate ALL languages (mode=all, force=True, force-all-nodes; long + many API calls)...")
            if not self.run_all_languages_translation(mode="all", count=20, force=True, force_all_nodes=True):
                print("\n❌ Failed at Step 5: All-languages translation")
                return False
            print("\n🔄 Step 6: Final scan after translations...")
            if not self.scan_nodes():
                print("\n❌ Failed at Step 6: Final scan")
                return False

        end = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 80)
        print("✅ Full regenerate workflow finished.")
        print("=" * 80)
        print(f"Started: {timestamp}")
        print(f"Finished: {end}")
        if not translate_all_languages:
            print("(Translations unchanged. Use --also-translate-all with regenerate-all, or run translate separately with --force.)")
        print("=" * 80 + "\n")
        return True

    def run_full_workflow(self, mode: str = "test", count: int = 20, force: bool = False):
        """Run the complete workflow"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("\n" + "=" * 80)
        print("ComfyUI Documentation Automation - Main Workflow")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        print(f"Mode: {mode}")
        if mode == "test":
            print(f"Count: {count} nodes")
        print(f"Force regenerate: {force}")
        print("=" * 80)
        
        # Step 1: Always scan first to get latest missing nodes
        print("\n📊 Step 1: Scanning to identify missing documentation...")
        if not self.scan_nodes():
            print("\n❌ Workflow failed at Step 1: Scan")
            return False
        
        # Step 2: Prepare AI input (will read from fresh missing_nodes_report.json)
        print("\n🔧 Step 2: Preparing AI input for missing nodes...")
        if not self.prepare_nodes(mode, count):
            print("\n❌ Workflow failed at Step 2: Prepare")
            return False
        
        # Step 3: Generate documentation (only for newly prepared nodes)
        print("\n🤖 Step 3: Generating documentation with AI...")
        if not self.generate_docs(mode, count, force=force):
            print("\n❌ Workflow failed at Step 3: Generate")
            return False
        
        # Step 4: Final scan to update reports with new status
        print("\n🔄 Step 4: Final scan to update all reports...")
        if not self.scan_nodes():
            print("\n❌ Workflow failed at Step 4: Final Update")
            return False
        
        # Success summary
        end_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print("\n" + "=" * 80)
        print("✅ Workflow Completed Successfully!")
        print("=" * 80)
        print(f"Started:  {timestamp}")
        print(f"Finished: {end_timestamp}")
        print("\nAll reports are up to date:")
        print("  - missing_nodes_report.json")
        print("  - node_versions.json")
        print("=" * 80 + "\n")
        
        return True


def _prompt(text: str, default: str = None) -> str:
    """Prompt for input; return default if user presses Enter and default is set."""
    if default is not None:
        prompt = f"{text} [{default}]: "
    else:
        prompt = f"{text}: "
    value = input(prompt).strip()
    return value if value else (default or "")


def _prompt_int(text: str, default: int = None) -> int:
    """Prompt for integer; retry until valid."""
    while True:
        raw = _prompt(text, str(default) if default is not None else None)
        if not raw and default is not None:
            return default
        try:
            return int(raw)
        except ValueError:
            print("  Please enter a number.")


def _prompt_yes_no(text: str, default: bool = False) -> bool:
    """Prompt for y/n; default when Enter with no input."""
    d = "Y" if default else "n"
    while True:
        raw = _prompt(f"{text} (y/n)", d).strip().lower() or d.lower()
        if raw in ("y", "yes"):
            return True
        if raw in ("n", "no"):
            return False
        print("  Enter y or n.")


def run_interactive(workflow: DocumentationWorkflow) -> bool:
    """Run interactive menu-driven workflow."""
    print("\n" + "=" * 60)
    print("  ComfyUI Documentation Automation - Interactive Menu")
    print("  Documentation Automation - Interactive Menu")
    print("=" * 60)

    while True:
        print("\nChoose an action:")
        print("  1) Scan only")
        print("  2) Generate English docs")
        print("  3) Translate (submenu: one language / all languages; force full re-translate option)")
        print("      (Translate: one lang / all langs; submenu includes force-retranslate-all)")
        print("  4) Generate missing docs + translate all")
        print("  5) Sync to Comfy docs")
        print("  6) Regenerate docs for changed nodes")
        print("  7) Full en.md regeneration (optional all-lang translate)")
        print("  8) Force full re-translate of all nodes (all en.md -> 11 languages; same as CLI --retranslate-all-languages)")
        print("      (Force-retranslate ALL langs for EVERY node with en.md; API-heavy)")
        print("  9) Fix existing docs (no AI)")
        print("  0) Exit")
        choice = _prompt("Choice", "0").strip()

        if choice == "0":
            print("Bye.")
            return True

        if choice == "1":
            ok = workflow.scan_nodes()
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "2":
            print("\n--- Generation Mode ---")
            print("  1) test - generate N missing nodes (default 20)")
            print("  2) all - generate all missing nodes")
            print("  3) node - generate a single node")
            sub = _prompt("Mode (1/2/3)", "1").strip()
            if sub == "2":
                mode = "all"
                count = 20
                node_name = None
            elif sub == "3":
                mode = "node"
                node_name = _prompt("Node name").strip()
                if not node_name:
                    print("  No node name entered; cancelled.")
                    continue
                count = None
            else:
                mode = "test"
                count = _prompt_int("Count", 20)
                node_name = None
            force = _prompt_yes_no("Force overwrite existing docs?", False)
            print()
            if mode == "node":
                ok = (
                    workflow.scan_nodes()
                    and workflow.prepare_nodes("node", node_name=node_name)
                    and workflow.generate_docs("node", node_name=node_name, force=force)
                    and workflow.update_reports()
                )
            else:
                ok = workflow.run_full_workflow(mode=mode, count=count, force=force)
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "3":
            print("\n--- Translation ---")
            print("  1) One language")
            print("  2) All languages")
            tr_choice = _prompt("1 or 2", "1").strip()
            if tr_choice == "2":
                print("  1) all - translate all currently missing per the report")
                print("  2) test - translate the first N missing per language")
                print("  3) Force full re-translate - overwrite all languages for every node with en.md (CLI: --retranslate-all-languages)")
                all_or_count = _prompt("1 / 2 / 3", "1").strip()
                if all_or_count == "3":
                    return workflow.run_all_languages_translation(mode="all", count=20, force=True, force_all_nodes=True)
                if all_or_count == "2":
                    count = _prompt_int("Count per language", 20)
                    force = _prompt_yes_no("Force overwrite existing translations?", False)
                    return workflow.run_all_languages_translation(mode="test", count=count, force=force)
                force = _prompt_yes_no("Force overwrite existing translations?", False)
                return workflow.run_all_languages_translation(mode="all", count=20, force=force)
            print("\nAvailable languages:")
            for i, lang in enumerate(LANGUAGES, 1):
                print(f"  {i:2}) {lang}  {LANG_NAMES.get(lang, '')}")
            lang_idx = _prompt_int("Language number (1-11)", 1)
            if not (1 <= lang_idx <= len(LANGUAGES)):
                print("  Invalid number.")
                continue
            lang = LANGUAGES[lang_idx - 1]
            print("\n  1) test - translate N (default 20)")
            print("  2) all - translate all missing")
            tm = _prompt("Mode (1/2)", "1").strip()
            mode = "all" if tm == "2" else "test"
            count = _prompt_int("Count (for test)", 20) if mode == "test" else 20
            force = _prompt_yes_no("Force overwrite existing translations?", False)
            print()
            ok = workflow.run_translation_workflow(lang=lang, mode=mode, count=count, force=force)
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "4":
            print("\n--- Generate missing docs + translate all (runs to completion) ---")
            print("  1) test - generate N missing English docs, then translate the same count for all languages")
            print("  2) all - generate all missing English docs, then translate all missing for every language (recommended)")
            sub = _prompt("Mode (1/2)", "2").strip()
            if sub == "2":
                gen_mode, gen_count = "all", 20
                tr_mode, tr_count = "all", 10
            else:
                gen_mode = "test"
                gen_count = _prompt_int("Count", 20)
                tr_mode = "test"
                tr_count = gen_count
            force_gen = _prompt_yes_no("Force overwrite existing English docs?", False)
            force_tr = _prompt_yes_no("Force overwrite existing translations?", False)
            print("\nThis will run end-to-end: generate English docs, then translate all languages, without further prompts.")
            print("[Step 1/2] Generating English docs...")
            if not workflow.run_full_workflow(mode=gen_mode, count=gen_count, force=force_gen):
                print("  Generation failed; cancelled.")
                if _prompt_yes_no("Continue?", False):
                    continue
                return False
            print("\n[Step 2/2] Translating all languages (automatic)...")
            ok = workflow.run_all_languages_translation(mode=tr_mode, count=tr_count, force=force_tr)
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "5":
            print("\n--- Sync to Comfy docs ---")
            print("  Sync embedded-docs en.md/zh.md and images to comfy/docs (built-in-nodes).")
            print("  1) test - sync first N nodes (default 10)")
            print("  2) all - sync all nodes with en.md")
            sub = _prompt("Mode (1/2)", "1").strip()
            mode = "all" if sub == "2" else "test"
            count = _prompt_int("Count (for test)", 10) if mode == "test" else 10
            dry = _prompt_yes_no("Dry run (no writes)?", False)
            no_json = _prompt_yes_no("Skip docs.json update?", False)
            args = ["--mode", mode]
            if mode == "test":
                args.extend(["--count", str(count)])
            if dry:
                args.append("--dry-run")
            if no_json:
                args.append("--no-docs-json")
            print()
            ok = workflow.run_command(
                workflow.sync_to_comfy_docs_script,
                args,
                "Sync to Comfy docs (built-in-nodes + docs.json)"
            )
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "6":
            print("\n--- Update changed node docs ---")
            print("  Scan source changes -> regenerate English docs for changed nodes.")
            force = _prompt_yes_no("Force overwrite existing docs?", True)
            print()
            ok = workflow.run_changed_workflow(force=force)
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "7":
            print("\n--- Full English docs regeneration ---")
            print("  Runs: scan -> prepare_ai_input for all scanned nodes -> batch_generate_docs all --force.")
            print("  Warning: long-running; rewrites every node en.md and consumes significant API quota.")
            print("  By default continues with all-language translation after English; choose n to skip (or use CLI --mode regenerate-all without translation).")
            also_tr = _prompt_yes_no(
                "Also translate all languages after English (mode=all + force overwrite)?",
                True,
            )
            if not _prompt_yes_no("Confirm to continue?", False):
                print("  Cancelled.")
                continue
            lim_raw = _prompt("Limit to first N nodes (debug, empty=all) Prepare limit / Enter for all").strip()
            prepare_limit = int(lim_raw) if lim_raw else None
            if prepare_limit is not None and prepare_limit <= 0:
                print("  Invalid count.")
                continue
            print()
            ok = workflow.run_regenerate_all_workflow(
                prepare_limit=prepare_limit,
                translate_all_languages=also_tr,
            )
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "8":
            print("\n--- Force full re-translate of all nodes ---")
            print("  Overwrites translations for every node with en.md across all 11 languages (ignores missing report).")
            print("  Warning: heavy API and time usage; equivalent to: python3 main.py --retranslate-all-languages")
            if not _prompt_yes_no("Confirm execution?", False):
                print("  Cancelled.")
                continue
            print()
            ok = workflow.run_all_languages_translation(
                mode="all", count=20, force=True, force_all_nodes=True
            )
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        if choice == "9":
            print("\n--- Fix existing docs ---")
            print("  1) Doc titles - missing / duplicated / mismatched with frontend display_name")
            print("     (Doc titles from frontend nodeDefs; no AI)")
            sub = _prompt("Option (1)", "1").strip()
            if sub != "1":
                print("  Only option 1 (doc titles) is supported.")
                continue
            print("\n  Hash handling / SHA footer:")
            print("  1) preserve - keep original disclaimer + SHA (recommended when translations are aligned)")
            print("  2) update - rewrite SHA from en.md / ai_input (and rewrite disclaimer)")
            hash_choice = _prompt("Hash (1/2)", "1").strip()
            hash_mode = "update" if hash_choice == "2" else "preserve"
            print("\n  1) test - scan first N files (default 20)")
            print("  2) all - scan all existing .md files")
            scope = _prompt("Scope (1/2)", "2").strip()
            fix_mode = "all" if scope == "2" else "test"
            fix_count = _prompt_int("File count (for test)", 20) if fix_mode == "test" else 20
            dry_run = _prompt_yes_no("Dry run (no writes)?", True)
            sync_fe = _prompt_yes_no("Sync frontend nodeDefs translations first?", True)
            node_name = _prompt("Single node only (empty = all) Node name").strip() or None
            lang_raw = _prompt("Single language code en/zh/... (empty = all) Lang").strip() or None
            if lang_raw and lang_raw not in (["en"] + LANGUAGES):
                print(f"  Invalid language: {lang_raw}")
                continue
            print()
            ok = workflow.run_fix_doc_titles_workflow(
                mode=fix_mode,
                count=fix_count,
                node_name=node_name,
                lang=lang_raw,
                dry_run=dry_run,
                sync_frontend=sync_fe,
                hash_mode=hash_mode,
            )
            if ok and _prompt_yes_no("Continue?", False):
                continue
            return ok

        print("  Please enter 0-9.")


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(
        description='ComfyUI Documentation Automation - Main Controller',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Generate 20 nodes (default)
  python3 main.py
  
  # Generate 50 nodes
  python3 main.py --count 50
  
  # Generate all missing nodes
  python3 main.py --mode all

  # Full refresh: rebuild ai_input for every scanned node → regenerate ALL en.md (API-heavy)
  python3 main.py --mode regenerate-all
  python3 main.py --mode regenerate-all --prepare-limit 50
  python3 main.py --mode regenerate-all --also-translate-all

  # Generate single node (new doc)
  python3 main.py --mode node --node AudioEncoderEncode

  # Update an existing node doc based on latest source code
  # (sends current en.md as reference so the AI keeps manual edits)
  python3 main.py --mode node --node TrainLoraNode --force

  # Force regenerate existing docs (batch)
  python3 main.py --count 10 --force
  
  # Only scan (no generation)
  python3 main.py --scan-only
  
  # Translation workflow
  python3 main.py --translate --lang zh --count 10
  python3 main.py --translate --lang zh --mode all
  python3 main.py --translate --lang es --count 20 --force
  
  # Translate all languages at once (zh, zh-TW, es, fr, ja, ko, ru, ar, tr, pt-BR, fa)
  # This will automatically sync frontend translations and update parameter names
  python3 main.py --translate --all-languages --count 10
  python3 main.py --translate --all-languages --mode all
  python3 main.py --retranslate-all-languages

  # Fix existing doc titles (no AI)
  python3 main.py --mode fix --fix-action doc-titles --dry-run
  python3 main.py --mode fix --fix-action doc-titles
        '''
    )
    
    parser.add_argument(
        '--mode',
        choices=['test', 'all', 'resume', 'node', 'changed', 'regenerate-all', 'fix'],
        default='test',
        help=(
            'Generation mode (default: test). '
            '"node" generates or updates a single node (requires --node). '
            'Pair with --force to update an existing doc: re-reads source code and '
            'sends the current en.md as reference so the AI updates params/outputs '
            'while preserving manual edits. '
            'Use "changed" to regenerate docs for nodes with updated source code. '
            '"regenerate-all" scans then prepares EVERY node from all_nodes_info.json and runs '
            'batch_generate_docs all --force (see --prepare-limit). Add --also-translate-all to '
            'retranslate every locale for every node with en.md afterwards (mode=all, force, force-all-nodes). '
            'Use "fix" with --fix-action doc-titles to repair H1 titles in existing docs (no AI).'
        )
    )

    parser.add_argument(
        '--fix-action',
        choices=['doc-titles'],
        default=None,
        help='With --mode fix: which repair to run (default: doc-titles)',
    )

    parser.add_argument(
        '--fix-scope',
        choices=['test', 'all'],
        default='all',
        help='Only with --mode fix: scan first N files (test) or all docs (all, default)',
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='With --mode fix: preview title fixes without writing files',
    )

    parser.add_argument(
        '--hash-mode',
        choices=['preserve', 'update'],
        default='preserve',
        help=(
            'With --mode fix: preserve original disclaimer+SHA (default) or '
            'update SHA from en.md/ai_input and rewrite disclaimer'
        ),
    )

    parser.add_argument(
        '--prepare-limit',
        type=int,
        default=None,
        metavar='N',
        help=(
            'Only with --mode regenerate-all: prepare and regenerate English docs only for '
            'the first N nodes (sorted by name). Omit for entire tree.'
        ),
    )

    parser.add_argument(
        '--also-translate-all',
        action='store_true',
        help=(
            'Only with --mode regenerate-all: after regenerating all English docs, run '
            'all-languages translation (mode=all, force, force-all-nodes).'
        ),
    )

    parser.add_argument(
        '--count',
        type=int,
        default=20,
        help='Number of nodes to generate/translate in test mode (default: 20)'
    )
    
    parser.add_argument(
        '--node',
        type=str,
        help='Node name for single node mode'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force regenerate/retranslate existing documentation'
    )
    
    parser.add_argument(
        '--scan-only',
        action='store_true',
        help='Only run scan, skip generation/translation'
    )
    
    parser.add_argument(
        '--translate',
        action='store_true',
        help='Run translation workflow instead of generation workflow'
    )
    
    parser.add_argument(
        '--lang',
        type=str,
        choices=['zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa'],
        help='Target language for translation (required with --translate)'
    )
    
    parser.add_argument(
        '--all-languages',
        action='store_true',
        help='Translate to all supported languages (zh, zh-TW, es, fr, ja, ko, ru, ar, tr, pt-BR, fa)'
    )

    parser.add_argument(
        '--force-all-translation-nodes',
        action='store_true',
        help=(
            'Only with --translate: include every folder under docs that has en.md in prepare_translation '
            '(sorted by name), not only nodes listed as missing. Use with --force so translations are overwritten.'
        ),
    )

    parser.add_argument(
        '--retranslate-all-languages',
        action='store_true',
        help=(
            'Force-retranslate all supported languages for every node that has en.md. Equivalent to '
            '--translate --all-languages --mode all --force --force-all-translation-nodes.'
        ),
    )

    parser.add_argument(
        '--concurrency',
        type=int,
        default=1,
        metavar='N',
        help=(
            'Parallel translation workers (default: 1 = sequential). Applies to --translate '
            'and to the re-translation step of --mode changed. Use with care: raises API '
            'request rate proportionally.'
        ),
    )

    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Show interactive menu (default when no other args)'
    )

    args = parser.parse_args()

    if args.retranslate_all_languages:
        args.translate = True
        args.all_languages = True
        args.force = True
        args.mode = 'all'
        args.force_all_translation_nodes = True

    if getattr(args, 'force_all_translation_nodes', False) and not args.translate:
        print("⚠️  Note: --force-all-translation-nodes only applies with --translate; ignoring.")

    if args.prepare_limit is not None and args.mode != "regenerate-all":
        print("⚠️  Note: --prepare-limit only applies with --mode regenerate-all; ignoring this flag.")

    if args.also_translate_all and args.mode != "regenerate-all":
        print("⚠️  Note: --also-translate-all only applies with --mode regenerate-all; ignoring this flag.")

    if args.dry_run and args.mode != "fix":
        print("⚠️  Note: --dry-run only applies with --mode fix; ignoring this flag.")

    if args.hash_mode != "preserve" and args.mode != "fix":
        print("⚠️  Note: --hash-mode only applies with --mode fix; ignoring this flag.")

    if args.fix_action and args.mode != "fix":
        print("⚠️  Note: --fix-action only applies with --mode fix; ignoring this flag.")

    # No args or --interactive: run interactive menu
    if args.interactive or len(sys.argv) == 1:
        workflow = DocumentationWorkflow()
        success = run_interactive(workflow)
        sys.exit(0 if success else 1)

    if args.concurrency < 1:
        print("❌ Error: --concurrency must be >= 1")
        sys.exit(1)

    if args.concurrency > 1 and not (args.translate or args.mode == 'changed'):
        print("⚠️  Note: --concurrency only applies to translation; ignoring it.")

    # Validate arguments
    if args.mode == 'node' and not args.node:
        print("❌ Error: --node is required when using --mode node")
        parser.print_help()
        sys.exit(1)
    
    if args.translate and not args.lang and not args.all_languages:
        print("❌ Error: --lang or --all-languages is required when using --translate")
        print("Available languages: zh, zh-TW, es, fr, ja, ko, ru, ar, tr, pt-BR, fa")
        parser.print_help()
        sys.exit(1)
    
    # Create workflow controller
    workflow = DocumentationWorkflow()
    
    # Run scan-only mode
    if args.scan_only:
        success = workflow.scan_nodes()
        sys.exit(0 if success else 1)

    # Run fix workflow (no AI)
    if args.mode == 'fix':
        if args.translate:
            print("❌ Error: --translate cannot be combined with --mode fix.")
            sys.exit(1)
        fix_action = args.fix_action or 'doc-titles'
        if fix_action != 'doc-titles':
            print(f"❌ Error: unknown --fix-action {fix_action!r}")
            sys.exit(1)
        success = workflow.run_fix_doc_titles_workflow(
            mode=args.fix_scope,
            count=args.count,
            node_name=args.node,
            lang=args.lang,
            dry_run=args.dry_run,
            hash_mode=args.hash_mode,
        )
        sys.exit(0 if success else 1)
    
    # Run translation workflow
    if args.translate:
        if args.mode == "regenerate-all":
            print("❌ Error: do not combine --translate with --mode regenerate-all. Use --also-translate-all instead.")
            sys.exit(1)
        if args.also_translate_all:
            print("❌ Error: do not combine --translate with --also-translate-all.")
            sys.exit(1)
        if args.mode not in ("test", "all", "node"):
            print(f"❌ Error: --translate only supports --mode test/all/node (got '{args.mode}').")
            sys.exit(1)
        if args.mode == "node" and not args.node:
            print("❌ Error: --node is required when using --translate --mode node")
            sys.exit(1)
        if args.node and args.mode != "node":
            print("⚠️  Note: --node only applies with --mode node; ignoring it.")
        if args.all_languages:
            # Translate all languages
            success = workflow.run_all_languages_translation(
                mode=args.mode,
                count=args.count,
                force=args.force,
                force_all_nodes=args.force_all_translation_nodes,
                node_name=args.node if args.mode == "node" else None,
                concurrency=args.concurrency,
            )
        else:
            # Translate single language
            success = workflow.run_translation_workflow(
                lang=args.lang,
                mode=args.mode,
                count=args.count,
                force=args.force,
                force_all_nodes=args.force_all_translation_nodes,
                node_name=args.node if args.mode == "node" else None,
                concurrency=args.concurrency,
            )
        sys.exit(0 if success else 1)
    
    # Run generation workflow
    if args.mode == 'node':
        # Single node workflow
        success = (
            workflow.scan_nodes() and
            workflow.prepare_nodes('node', node_name=args.node) and
            workflow.generate_docs('node', node_name=args.node, force=args.force) and
            workflow.update_reports()
        )
    elif args.mode == 'changed':
        # Changed nodes workflow
        success = workflow.run_changed_workflow(force=args.force, concurrency=args.concurrency)
    elif args.mode == 'regenerate-all':
        success = workflow.run_regenerate_all_workflow(
            prepare_limit=args.prepare_limit,
            translate_all_languages=args.also_translate_all,
        )
    else:
        # Batch workflow
        success = workflow.run_full_workflow(
            mode=args.mode,
            count=args.count,
            force=args.force
        )
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()

