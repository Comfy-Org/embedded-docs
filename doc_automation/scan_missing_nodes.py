#!/usr/bin/env python3
"""
Scan ComfyUI codebase to find all nodes and identify missing documentation
"""

import os
import re
import ast
import hashlib
from pathlib import Path
from typing import Set, Dict, List
import json
try:
    from dotenv import load_dotenv
    _has_dotenv = True
except ImportError:
    _has_dotenv = False

from node_source_extract import extract_node_class_source

# Load environment variables
if _has_dotenv:
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(env_path)

# Get paths from environment variables
COMFYUI_PATH = Path(os.getenv('COMFYUI_PATH', '/Users/linmoumou/Documents/local_env/ComfyUI'))
EMBEDDED_DOCS_PATH = Path(os.getenv('EMBEDDED_DOCS_PATH', '/Users/linmoumou/Documents/local_env/embedded-docs'))
DOCS_PATH = EMBEDDED_DOCS_PATH / "comfyui_embedded_docs" / "docs"

# Python file paths to scan
SCAN_PATHS = [
    COMFYUI_PATH / "nodes.py",
    COMFYUI_PATH / "comfy_extras",
    COMFYUI_PATH / "comfy_api_nodes",
]


class NodeScanner:
    """Node scanner to identify all ComfyUI nodes"""
    
    def __init__(self):
        self.all_nodes: Set[str] = set()
        self.node_info: Dict[str, Dict] = {}
        self.class_mappings: Dict[str, str] = {}  # mapping_name -> class_name
        
    def scan_file_for_nodes(self, file_path: Path):
        """Scan a Python file to extract node definitions"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract NODE_CLASS_MAPPINGS first (this is the authoritative source)
            mappings = self._extract_node_class_mappings(content)
            self.class_mappings.update(mappings)
            
            # Method 1: Find new API nodes with io.Schema node_id
            schema_pattern = r'node_id\s*=\s*["\']([^"\']+)["\']'
            for match in re.finditer(schema_pattern, content):
                node_id = match.group(1)
                class_name = self._find_class_name(content, match.start())
                category = self._extract_category_near_position(content, match.start(), window=2000)
                if not category and class_name != "Unknown":
                    category = self._extract_category_classic(content, class_name)
                # Use NODE_CLASS_MAPPINGS name if available, otherwise use node_id
                node_name = node_id
                for mapping_name, mapped_class in mappings.items():
                    if mapped_class == class_name:
                        node_name = mapping_name
                        break
                self.all_nodes.add(node_name)
                info = {
                    'file': str(file_path.relative_to(COMFYUI_PATH)),
                    'type': 'new_api',
                    'class_name': class_name,
                    'node_id': node_id
                }
                if category:
                    info['category'] = category
                self.node_info[node_name] = info
            
            # Method 2: Find classic nodes with INPUT_TYPES method
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        # Check if class has INPUT_TYPES method
                        has_input_types = any(
                            isinstance(item, ast.FunctionDef) and item.name == "INPUT_TYPES"
                            for item in node.body
                        )
                        if has_input_types:
                            class_name = node.name
                            # Skip base classes and abstract classes
                            if not class_name.startswith('_') and class_name not in ['ComfyNode', 'Base', 'ComfyNodeABC']:
                                # Use NODE_CLASS_MAPPINGS name if available
                                node_name = class_name
                                for mapping_name, mapped_class in mappings.items():
                                    if mapped_class == class_name:
                                        node_name = mapping_name
                                        break
                                
                                self.all_nodes.add(node_name)
                                category = self._extract_category_classic(content, class_name)
                                info = {
                                    'file': str(file_path.relative_to(COMFYUI_PATH)),
                                    'type': 'classic',
                                    'class_name': class_name
                                }
                                if category:
                                    info['category'] = category
                                self.node_info[node_name] = info
            except SyntaxError:
                print(f"⚠️  Syntax error, skipping AST parsing: {file_path}")
                
        except Exception as e:
            print(f"❌ Failed to read file {file_path}: {e}")
    
    def _find_class_name(self, content: str, pos: int) -> str:
        """Find class name by searching backwards from position"""
        lines_before = content[:pos].split('\n')
        for line in reversed(lines_before):
            match = re.search(r'class\s+(\w+)', line)
            if match:
                return match.group(1)
        return "Unknown"

    def _extract_category_near_position(self, content: str, pos: int, window: int = 2000) -> str:
        """Extract category= or CATEGORY = from content near position (Schema or class block).

        For Schema-style nodes the layout is always:
            IO.Schema(
                node_id="NodeName",
                category="...",   ← comes AFTER node_id in the same call
            )
        So we search in a small window AFTER pos first to avoid picking up
        category= values from neighbouring nodes that appear before pos.
        Only fall back to the full bidirectional window if nothing is found after.
        """
        # Priority: search after pos (catches Schema-style nodes reliably)
        after_block = content[pos:min(len(content), pos + 600)]
        m = re.search(r'category\s*=\s*["\']([^"\']+)["\']', after_block)
        if m:
            return m.group(1).strip()
        # Fallback: full bidirectional window (classic CATEGORY = "..." may come before)
        start = max(0, pos - window)
        end = min(len(content), pos + window)
        block = content[start:end]
        m = re.search(r'CATEGORY\s*=\s*["\']([^"\']+)["\']', block)
        if m:
            return m.group(1).strip()
        return ""

    def _extract_category_classic(self, content: str, class_name: str) -> str:
        """Extract CATEGORY from classic node class block (and optionally from base class in same file)."""
        class_pattern = re.compile(
            r"^class\s+" + re.escape(class_name) + r"\s*[:(].*?(?=^class\s|\Z)",
            re.MULTILINE | re.DOTALL,
        )
        m = class_pattern.search(content)
        if not m:
            return ""
        block = m.group(0)
        # CATEGORY = "..."
        c = re.search(r"CATEGORY\s*=\s*[\"']([^\"']+)[\"']", block)
        if c:
            return c.group(1).strip()
        # Schema-style in same block
        c = re.search(r"category\s*=\s*[\"']([^\"']+)[\"']", block)
        if c:
            return c.group(1).strip()
        # Base class: get parent and look for category in base's block (e.g. ImageProcessingNode)
        base_m = re.search(r"^class\s+" + re.escape(class_name) + r"\s*\(\s*(\w+)", content, re.MULTILINE)
        if base_m:
            base_name = base_m.group(1)
            if base_name not in ("ComfyNode", "io.ComfyNode", "IO.ComfyNode"):
                base_pattern = re.compile(
                    r"^class\s+" + re.escape(base_name) + r"\s*[:(].*?(?=^class\s|\Z)",
                    re.MULTILINE | re.DOTALL,
                )
                b = base_pattern.search(content)
                if b:
                    base_block = b.group(0)
                    bc = re.search(r"category\s*=\s*[\"']([^\"']+)[\"']", base_block)
                    if bc:
                        return bc.group(1).strip()
                    bc = re.search(r"CATEGORY\s*=\s*[\"']([^\"']+)[\"']", base_block)
                    if bc:
                        return bc.group(1).strip()
        return ""

    def _extract_node_class_mappings(self, content: str) -> Dict[str, str]:
        """Extract NODE_CLASS_MAPPINGS dictionary from file content"""
        mappings = {}
        
        # Find NODE_CLASS_MAPPINGS = { ... }
        pattern = r'NODE_CLASS_MAPPINGS\s*=\s*\{([^}]+)\}'
        match = re.search(pattern, content, re.DOTALL)
        
        if match:
            mappings_content = match.group(1)
            # Extract "key": ClassName pairs
            pair_pattern = r'["\']([^"\']+)["\']\s*:\s*(\w+)'
            for pair_match in re.finditer(pair_pattern, mappings_content):
                mapping_name = pair_match.group(1)
                class_name = pair_match.group(2)
                mappings[mapping_name] = class_name
        
        return mappings
    
    def scan_directory(self, dir_path: Path):
        """Recursively scan all Python files in directory"""
        if not dir_path.exists():
            print(f"⚠️  Path does not exist: {dir_path}")
            return
            
        for py_file in dir_path.rglob("*.py"):
            # Skip some special files
            if '__pycache__' in str(py_file) or py_file.name.startswith('test_'):
                continue
            self.scan_file_for_nodes(py_file)
    
    def scan_all(self):
        """Scan all configured paths"""
        print("🔍 Starting to scan ComfyUI nodes...")
        
        for path in SCAN_PATHS:
            if path.is_file():
                print(f"📄 Scanning file: {path.name}")
                self.scan_file_for_nodes(path)
            elif path.is_dir():
                print(f"📁 Scanning directory: {path.name}")
                self.scan_directory(path)
        
        print(f"✅ Scan completed, found {len(self.all_nodes)} nodes\n")

    def save_all_nodes_info(self, output_path: Path) -> None:
        """Save node_name -> { file, type, class_name, category?, ... } for all scanned nodes (for sync script)."""
        data = {
            "total": len(self.all_nodes),
            "nodes": {name: self.node_info.get(name, {}) for name in sorted(self.all_nodes)},
        }
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


class DocumentationChecker:
    """Documentation checker"""
    
    def __init__(self, docs_path: Path):
        self.docs_path = docs_path
        self.documented_nodes: Set[str] = set()
        
    def scan_existing_docs(self):
        """Scan existing documentation folders"""
        print("📚 Scanning existing documentation...")
        
        if not self.docs_path.exists():
            print(f"❌ Documentation path does not exist: {self.docs_path}")
            return
        
        for item in self.docs_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                self.documented_nodes.add(item.name)
        
        print(f"✅ Found {len(self.documented_nodes)} existing documentation\n")
    
    def check_doc_completeness(self, node_name: str) -> Dict[str, bool]:
        """Check documentation completeness for a single node"""
        node_dir = self.docs_path / node_name
        languages = ['en', 'zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa']
        
        completeness = {}
        for lang in languages:
            doc_file = node_dir / f"{lang}.md"
            completeness[lang] = doc_file.exists()
        
        return completeness


def main():
    """Main function"""
    print("=" * 80)
    print("ComfyUI Node Documentation Missing Scanner")
    print("=" * 80)
    print()
    
    # 1. Scan all nodes
    scanner = NodeScanner()
    scanner.scan_all()

    # Save full node info (including category) for sync script
    all_nodes_path = Path(__file__).parent / "all_nodes_info.json"
    scanner.save_all_nodes_info(all_nodes_path)
    print(f"💾 All nodes info (with category) saved to: {all_nodes_path}\n")

    # 2. Scan existing documentation
    doc_checker = DocumentationChecker(DOCS_PATH)
    doc_checker.scan_existing_docs()
    
    # 3. Comparison analysis
    print("=" * 80)
    print("📊 Analysis Results")
    print("=" * 80)
    print()
    
    missing_nodes = scanner.all_nodes - doc_checker.documented_nodes
    extra_docs = doc_checker.documented_nodes - scanner.all_nodes
    
    print(f"🔢 Statistics:")
    print(f"   - Total nodes in code: {len(scanner.all_nodes)}")
    print(f"   - Nodes with documentation: {len(doc_checker.documented_nodes)}")
    print(f"   - Nodes missing documentation: {len(missing_nodes)}")
    print(f"   - Extra documentation: {len(extra_docs)} (possibly deprecated nodes)")
    print()
    
    # 4. Output missing nodes list
    if missing_nodes:
        print("❌ Nodes missing documentation:")
        print("-" * 80)
        
        # Group by file
        nodes_by_file = {}
        for node in sorted(missing_nodes):
            if node in scanner.node_info:
                file_path = scanner.node_info[node]['file']
                if file_path not in nodes_by_file:
                    nodes_by_file[file_path] = []
                nodes_by_file[file_path].append(node)
        
        for file_path, nodes in sorted(nodes_by_file.items()):
            print(f"\n📄 {file_path}")
            for node in sorted(nodes):
                info = scanner.node_info.get(node, {})
                node_type = info.get('type', 'unknown')
                print(f"   - {node} ({node_type})")
        
        print()
    else:
        print("✅ Great! All nodes have documentation!")
        print()
    
    # 5. Output extra documentation list
    if extra_docs:
        print("⚠️  Possibly deprecated documentation (no corresponding node found in code):")
        print("-" * 80)
        for doc in sorted(extra_docs):
            print(f"   - {doc}")
        print()

    # 6. Check completeness of existing documentation (only for nodes that already have docs)
    print("=" * 80)
    print("📋 Checking language completeness of existing documentation")
    print("=" * 80)
    print(f"   (Only nodes that already have an en.md are checked. The {len(missing_nodes)} missing above have no doc yet.)")
    print()
    
    incomplete_docs = []
    for node in doc_checker.documented_nodes:
        completeness = doc_checker.check_doc_completeness(node)
        missing_langs = [lang for lang, exists in completeness.items() if not exists]
        if missing_langs:
            incomplete_docs.append((node, missing_langs))
    
    if incomplete_docs:
        print(f"⚠️  Found {len(incomplete_docs)} document(s) missing certain language versions:")
        print()
        for node, missing_langs in sorted(incomplete_docs)[:10]:  # Show only first 10
            langs_str = ", ".join(missing_langs)
            print(f"   - {node}: Missing {langs_str}")
        
        if len(incomplete_docs) > 10:
            print(f"   ... and {len(incomplete_docs) - 10} more nodes")
        print()
    else:
        print("✅ Among existing docs: all contain all 7 language versions!")
        print("   (The nodes missing documentation above still need en.md generated first.)")
        print()
    
    # 7. Detect changed nodes (documented nodes whose source hash differs from recorded)
    print("=" * 80)
    print("🔄 Checking for changed nodes (source code hash comparison)")
    print("=" * 80)
    print("   Note: Extracting latest source code directly from ComfyUI to detect changes")
    print()

    version_db_path = Path(__file__).parent / "node_versions.json"
    version_db = {}
    if version_db_path.exists():
        with open(version_db_path, 'r', encoding='utf-8') as f:
            version_db = json.load(f).get("nodes", {})

    changed_nodes = []
    extraction_failed = []

    for node_name in sorted(doc_checker.documented_nodes):
        if node_name not in version_db:
            continue
        recorded_hash = version_db[node_name].get("current_hash")
        if not recorded_hash:
            continue

        # Extract current source DIRECTLY from ComfyUI source code (not from cache)
        # This ensures we detect changes even if ai_input cache is stale
        info = scanner.node_info.get(node_name, {})
        if not info:
            continue

        file_path = COMFYUI_PATH / info.get('file', '')
        if not file_path.exists():
            extraction_failed.append(node_name)
            continue

        node_type = info.get('type', 'classic')
        class_name = info.get('class_name', node_name)

        # Class-only fingerprint: hash must not move when only contextual/cross-file extraction changes.
        current_class_src = extract_node_class_source(file_path, class_name)
        if not current_class_src:
            extraction_failed.append(node_name)
            continue

        current_hash = hashlib.sha256(current_class_src.encode('utf-8')).hexdigest()
        if current_hash != recorded_hash:
            changed_nodes.append({
                "name": node_name,
                "file": info.get('file', 'unknown'),
                "type": node_type,
                "class_name": class_name,
                "old_hash": recorded_hash[:16] + "...",
                "new_hash": current_hash[:16] + "...",
            })

    if changed_nodes:
        print(f"⚠️  Found {len(changed_nodes)} node(s) with changed source code:")
        for n in changed_nodes:
            print(f"   - {n['name']}  ({n['old_hash']} → {n['new_hash']})")
        print()
    else:
        print("✅ No source code changes detected among documented nodes\n")

    if extraction_failed:
        print(f"⚠️  Failed to extract source for {len(extraction_failed)} node(s):")
        for name in extraction_failed[:5]:
            print(f"   - {name}")
        if len(extraction_failed) > 5:
            print(f"   ... and {len(extraction_failed) - 5} more")
        print()

    # 8. Save results to JSON file
    output_file = Path(__file__).parent / "missing_nodes_report.json"
    report = {
        "scan_time": str(Path(__file__).stat().st_mtime),
        "total_nodes": len(scanner.all_nodes),
        "documented_nodes": len(doc_checker.documented_nodes),
        "missing_count": len(missing_nodes),
        "changed_count": len(changed_nodes),
        "missing_nodes": [
            {
                "name": node,
                "file": scanner.node_info.get(node, {}).get('file', 'unknown'),
                "type": scanner.node_info.get(node, {}).get('type', 'unknown'),
                "class_name": scanner.node_info.get(node, {}).get('class_name', 'unknown'),
            }
            for node in sorted(missing_nodes)
        ],
        "changed_nodes": changed_nodes,
        "extra_docs": sorted(list(extra_docs)),
        "incomplete_docs": [
            {"node": node, "missing_languages": langs}
            for node, langs in sorted(incomplete_docs)
        ]
    }

    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    print("=" * 80)
    print(f"💾 Detailed report saved to: {output_file}")
    print("=" * 80)


if __name__ == "__main__":
    main()

