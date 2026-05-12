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

  # === Translation (other languages) ===
  python3 main.py --translate --lang <LANG> [--mode MODE] [--count N] [--force]

  # Translate to one language (test: 20 nodes)
  python3 main.py --translate --lang zh --count 10
  python3 main.py --translate --lang pt-BR --mode all

  # Translate to all supported languages
  python3 main.py --translate --all-languages --count 10
  python3 main.py --translate --all-languages --mode all

  # Force retranslate existing docs
  python3 main.py --translate --lang zh --mode all --force

  # Supported languages: zh, zh-TW, es, fr, ja, ko, ru, ar, tr, pt-BR, fa

Options
-------
  --mode       test | all | resume | node | changed | regenerate-all  (default: test)
  --count      N nodes in test mode         (default: 20)
  --node       Node name (required with --mode node)
  --force      Overwrite existing docs/translations
  --prepare-limit  Only with --mode regenerate-all: prepare & regenerate first N nodes
  --also-translate-all  Only with --mode regenerate-all: after English, run all-languages translation (mode=all, force)
  --translate  Run translation workflow instead of generation
  --lang       Target language (required with --translate)
  --all-languages  Translate to all 11 languages

  # Interactive mode (no args, or --interactive): menu-driven
  python3 main.py
  python3 main.py --interactive
"""

import sys
import subprocess
from pathlib import Path
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
        self.script_dir = Path(__file__).parent
        self.scan_script = self.script_dir / "scan_missing_nodes.py"
        self.prepare_script = self.script_dir / "prepare_ai_input.py"
        self.generate_script = self.script_dir / "batch_generate_docs.py"
        self.prepare_translation_script = self.script_dir / "prepare_translation.py"
        self.translate_script = self.script_dir / "batch_translate_docs.py"
        self.update_params_script = self.script_dir / "update_param_translations.py"
        self.sync_frontend_script = self.script_dir / "sync_frontend_translations.py"
        self.sync_to_comfy_docs_script = self.script_dir / "sync_to_comfy_docs.py"
        
        # Default frontend path - can be overridden
        self.frontend_path = self.script_dir.parent.parent / "comfy" / "ComfyUI_frontend"
    
    def run_command(self, script: Path, args: list, description: str) -> bool:
        """Run a Python script with arguments"""
        print(f"\n{'=' * 80}")
        print(f"🚀 {description}")
        print(f"{'=' * 80}\n")
        
        cmd = ["python3", str(script)] + args
        result = subprocess.run(cmd, cwd=self.script_dir)
        
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
    
    def prepare_translation(self, lang: str, mode: str, count: int = None) -> bool:
        """Prepare translation batch for a specific language"""
        args = ["--lang", lang, "--mode", mode]
        
        if mode == "test" and count:
            args.extend(["--count", str(count)])
        
        return self.run_command(
            self.prepare_translation_script,
            args,
            f"Preparing {lang} translation batch ({mode} mode)"
        )
    
    def translate_docs(self, lang: str, mode: str, count: int = None, force: bool = False) -> bool:
        """Translate documentation to a specific language"""
        args = ["--lang", lang, "--mode", mode]
        
        if mode == "test" and count:
            args.extend(["--count", str(count)])
        
        if force:
            args.append("--force")
        
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
    
    def run_translation_workflow(self, lang: str, mode: str = "test", count: int = 10, force: bool = False, skip_initial_scan: bool = False, skip_frontend_sync: bool = False):
        """Run translation workflow for a specific language"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("\n" + "=" * 80)
        print("ComfyUI Documentation Translation - Main Workflow")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        print(f"Target language: {lang}")
        print(f"Mode: {mode}")
        if mode == "test":
            print(f"Count: {count} nodes")
        print(f"Force retranslate: {force}")
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
        
        # Step 1: Prepare translation batch (reads from JSON, verifies files)
        print(f"\n🔧 Step 1: Preparing {lang} translation batch from JSON...")
        if not self.prepare_translation(lang, mode, count):
            print("\n❌ Translation workflow failed at Step 1: Prepare")
            return False
        
        # Step 2: Translate documents (trusts batch list, updates JSON incrementally)
        print(f"\n🤖 Step 2: Translating to {lang}...")
        if not self.translate_docs(lang, mode, count, force):
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
    
    def run_all_languages_translation(self, mode: str = "test", count: int = 10, force: bool = False):
        """Run translation workflow for all supported languages"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        languages = ['zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']
        
        print("\n" + "=" * 80)
        print("ComfyUI Documentation Translation - ALL LANGUAGES")
        print("=" * 80)
        print(f"Started at: {timestamp}")
        print(f"Languages: {', '.join(languages)}")
        print(f"Mode: {mode}")
        if mode == "test":
            print(f"Count per language: {count} nodes")
        print(f"Force retranslate: {force}")
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
            success = self.run_translation_workflow(lang, mode, count, force, skip_initial_scan=True, skip_frontend_sync=True)
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
    
    def run_changed_workflow(self, force: bool = False):
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
        print("\n🤖 Step 3: Generating documentation for changed nodes...")
        if not self.generate_docs("changed", force=True):
            print("\n❌ Workflow failed at Step 3: Generate")
            return False

        # Step 4: Final scan to update reports
        print("\n🔄 Step 4: Final scan to update all reports...")
        if not self.scan_nodes():
            print("\n❌ Workflow failed at Step 4: Final Update")
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

        If ``translate_all_languages`` is True, runs the same all-languages translation pass as the
        interactive shortcut (``mode=all``, ``force=True``) after English regeneration.

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
            print("\n🌐 Step 5: Translate ALL languages (mode=all, force=True; long + many API calls)...")
            if not self.run_all_languages_translation(mode="all", count=20, force=True):
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
    print("  ComfyUI 文档自动化 - 交互式菜单")
    print("  Documentation Automation - Interactive Menu")
    print("=" * 60)

    while True:
        print("\n请选择操作 / Choose action:")
        print("  1) 仅扫描 (Scan only)")
        print("  2) 生成英文文档 (Generate English docs)")
        print("  3) 翻译 (Translate to other languages)")
        print("  4) 生成缺失文档并全部翻译 (Generate missing + translate all)")
        print("  5) 同步到 Comfy 文档 (Sync to Comfy docs)")
        print("  6) 更新变更节点文档 (Regenerate docs for changed nodes)")
        print("  7) 全量重跑英文（可选随后全语言翻译）(FULL en.md; optional all-lang translate)")
        print("  0) 退出 (Exit)")
        choice = _prompt("选项 / Choice", "0").strip()

        if choice == "0":
            print("Bye.")
            return True

        if choice == "1":
            ok = workflow.scan_nodes()
            if ok and _prompt_yes_no("继续操作? (Continue?)", False):
                continue
            return ok

        if choice == "2":
            print("\n--- 生成模式 ---")
            print("  1) test  - 生成指定数量的缺失节点 (default 20)")
            print("  2) all   - 生成所有缺失节点")
            print("  3) node  - 仅生成单个节点")
            sub = _prompt("模式 (1/2/3)", "1").strip()
            if sub == "2":
                mode = "all"
                count = 20
                node_name = None
            elif sub == "3":
                mode = "node"
                node_name = _prompt("节点名称 (Node name)").strip()
                if not node_name:
                    print("  未输入节点名，已取消。")
                    continue
                count = None
            else:
                mode = "test"
                count = _prompt_int("生成数量 (Count)", 20)
                node_name = None
            force = _prompt_yes_no("是否覆盖已有文档 (Force overwrite)?", False)
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
            if ok and _prompt_yes_no("继续操作? (Continue?)", False):
                continue
            return ok

        if choice == "3":
            print("\n--- 翻译 ---")
            print("  1) 单语言 (One language)")
            print("  2) 全部语言 (All languages)")
            tr_choice = _prompt("1 或 2", "1").strip()
            if tr_choice == "2":
                print("  1) 全部缺失 (all) - 一次性翻译完每种语言的所有缺失，推荐")
                print("  2) 指定数量 (test) - 每种语言只翻译前 N 条")
                all_or_count = _prompt("1 或 2", "1").strip()
                if all_or_count == "2":
                    count = _prompt_int("每种语言处理数量 (Count per language)", 20)
                    force = _prompt_yes_no("是否覆盖已有翻译 (Force overwrite)?", False)
                    return workflow.run_all_languages_translation(mode="test", count=count, force=force)
                force = _prompt_yes_no("是否覆盖已有翻译 (Force overwrite)?", False)
                return workflow.run_all_languages_translation(mode="all", count=20, force=force)
            print("\n可选语言:")
            for i, lang in enumerate(LANGUAGES, 1):
                print(f"  {i:2}) {lang}  {LANG_NAMES.get(lang, '')}")
            lang_idx = _prompt_int("语言编号 (1-11)", 1)
            if not (1 <= lang_idx <= len(LANGUAGES)):
                print("  无效编号。")
                continue
            lang = LANGUAGES[lang_idx - 1]
            print("\n  1) test - 翻译指定数量 (默认 20)")
            print("  2) all  - 翻译全部缺失")
            tm = _prompt("模式 (1/2)", "1").strip()
            mode = "all" if tm == "2" else "test"
            count = _prompt_int("数量 (test 时)", 20) if mode == "test" else 20
            force = _prompt_yes_no("是否覆盖已有翻译 (Force overwrite)?", False)
            print()
            ok = workflow.run_translation_workflow(lang=lang, mode=mode, count=count, force=force)
            if ok and _prompt_yes_no("继续操作? (Continue?)", False):
                continue
            return ok

        if choice == "4":
            print("\n--- 生成缺失文档并全部翻译（一次性跑完，中间不再确认）---")
            print("  1) test - 先生成指定数量的缺失英文文档，再对全部语言翻译同样数量")
            print("  2) all  - 先生成所有缺失英文文档，再对全部语言翻译所有缺失（推荐，一次性完成）")
            sub = _prompt("模式 (1/2)", "2").strip()
            if sub == "2":
                gen_mode, gen_count = "all", 20
                tr_mode, tr_count = "all", 10
            else:
                gen_mode = "test"
                gen_count = _prompt_int("生成数量 (Count)", 20)
                tr_mode = "test"
                tr_count = gen_count
            force_gen = _prompt_yes_no("是否覆盖已有英文文档 (Force overwrite)?", False)
            force_tr = _prompt_yes_no("是否覆盖已有翻译 (Force overwrite)?", False)
            print("\n将一次性执行：先生成英文文档 → 再全部语言翻译，中间不再询问。")
            print("[Step 1/2] 生成英文文档...")
            if not workflow.run_full_workflow(mode=gen_mode, count=gen_count, force=force_gen):
                print("  生成失败，已取消。")
                if _prompt_yes_no("继续操作? (Continue?)", False):
                    continue
                return False
            print("\n[Step 2/2] 全部语言翻译（自动连续执行）...")
            ok = workflow.run_all_languages_translation(mode=tr_mode, count=tr_count, force=force_tr)
            if ok and _prompt_yes_no("继续操作? (Continue?)", False):
                continue
            return ok

        if choice == "5":
            print("\n--- 同步到 Comfy 文档 ---")
            print("  将 embedded-docs 的 en.md/zh.md 与图片同步到 comfy/docs (built-in-nodes)。")
            print("  1) test - 同步前 N 个节点 (默认 10)")
            print("  2) all  - 同步所有有 en.md 的节点")
            sub = _prompt("模式 (1/2)", "1").strip()
            mode = "all" if sub == "2" else "test"
            count = _prompt_int("数量 (test 时)", 10) if mode == "test" else 10
            dry = _prompt_yes_no("仅预览不写入 (Dry run)?", False)
            no_json = _prompt_yes_no("不更新 docs.json (No docs.json)?", False)
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
            if ok and _prompt_yes_no("继续操作? (Continue?)", False):
                continue
            return ok

        if choice == "6":
            print("\n--- 更新变更节点文档 ---")
            print("  扫描源码变更 → 重新生成有变动节点的英文文档。")
            force = _prompt_yes_no("是否强制覆盖已有文档 (Force overwrite)?", True)
            print()
            ok = workflow.run_changed_workflow(force=force)
            if ok and _prompt_yes_no("继续操作? (Continue?)", False):
                continue
            return ok

        if choice == "7":
            print("\n--- 全量英文文档重生 ---")
            print("  会：扫描 → 对所有已扫描节点跑 prepare_ai_input → batch_generate_docs all --force。")
            print("  ⚠️  耗时长；会重写每个节点的 en.md 并占用大量 API。")
            print("  默认会在英文完成后继续全语言翻译；若只在交互里改了英文不想动翻译，选 n（或 CLI 仅用 --mode regenerate-all 不加翻译）。")
            also_tr = _prompt_yes_no(
                "英文完成后是否继续「全语言翻译」（mode=all + 强制覆盖翻译）? (Also translate all langs?)",
                True,
            )
            if not _prompt_yes_no("确认继续？", False):
                print("  已取消。")
                continue
            lim_raw = _prompt("仅先做前 N 个节点（调试，留空=全部）Prepare limit / Enter for all").strip()
            prepare_limit = int(lim_raw) if lim_raw else None
            if prepare_limit is not None and prepare_limit <= 0:
                print("  无效数量。")
                continue
            print()
            ok = workflow.run_regenerate_all_workflow(
                prepare_limit=prepare_limit,
                translate_all_languages=also_tr,
            )
            if ok and _prompt_yes_no("继续操作? (Continue?)", False):
                continue
            return ok

        print("  请输入 0、1、2、3、4、5、6 或 7。")


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
        '''
    )
    
    parser.add_argument(
        '--mode',
        choices=['test', 'all', 'resume', 'node', 'changed', 'regenerate-all'],
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
            'chain the same full multi-language translation pass afterwards (mode=all, force).'
        )
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
            'Only with --mode regenerate-all: after regenerating all English docs, run the same '
            'all-languages translation pass as --translate --all-languages (mode=all, force).'
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
        '--interactive', '-i',
        action='store_true',
        help='Show interactive menu (default when no other args)'
    )

    args = parser.parse_args()

    if args.prepare_limit is not None and args.mode != "regenerate-all":
        print("⚠️  Note: --prepare-limit only applies with --mode regenerate-all; ignoring this flag.")

    if args.also_translate_all and args.mode != "regenerate-all":
        print("⚠️  Note: --also-translate-all only applies with --mode regenerate-all; ignoring this flag.")

    # No args or --interactive: run interactive menu
    if args.interactive or len(sys.argv) == 1:
        workflow = DocumentationWorkflow()
        success = run_interactive(workflow)
        sys.exit(0 if success else 1)

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
    
    # Run translation workflow
    if args.translate:
        if args.mode == "regenerate-all":
            print("❌ Error: do not combine --translate with --mode regenerate-all. Use --also-translate-all instead.")
            sys.exit(1)
        if args.also_translate_all:
            print("❌ Error: do not combine --translate with --also-translate-all.")
            sys.exit(1)
        if args.all_languages:
            # Translate all languages
            success = workflow.run_all_languages_translation(
                mode=args.mode if args.mode != 'node' else 'test',
                count=args.count,
                force=args.force
            )
        else:
            # Translate single language
            success = workflow.run_translation_workflow(
                lang=args.lang,
                mode=args.mode if args.mode != 'node' else 'test',
                count=args.count,
                force=args.force
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
        success = workflow.run_changed_workflow(force=args.force)
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

