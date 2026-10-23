#!/usr/bin/env python3
"""
Scan ComfyUI codebase to find all nodes and identify missing documentation.

Node discovery mirrors what ComfyUI itself registers (``init_extra_nodes`` in
``nodes.py``): a module registers either as V1 (``NODE_CLASS_MAPPINGS``) or as
V3 (``comfy_entrypoint`` + ``get_node_list``), never both, so classes that are
only base classes are not nodes.

  * V1 — every ``NODE_CLASS_MAPPINGS`` key is a node type. Keys may be built in
    a loop (``NODE_CLASS_MAPPINGS[node.NodeId] = node``) and several keys may
    share one class (aliases). ``old_node_id=`` of ``io.NodeReplace`` is a
    *retired* id, never a node.
  * V3 — the node type is ``schema.node_id``, spelled as ``node_id="X"``,
    ``node_id=cls.NODE_ID``, ``schema.node_id = "X"`` after
    ``super().define_schema()``, the first positional argument of a schema
    factory (``_cloud_schema("X", ...)``), or an old-style ``NodeId = "X"``
    class attribute.
  * Legacy classes exposing ``INPUT_TYPES`` outside any registry.

Documentation folders are matched to node ids leniently (case, underscores and
spaces ignored), because a few folders were created from a sanitized spelling
(``ClipLoader`` vs ``CLIPLoader``). A folder that only differs in spelling is
reported as a mismatch, not as missing documentation.
"""

import ast
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

import runtime  # noqa: F401
from lib.node_source_extract import extract_node_class_source
from lib.paths import (
    ALL_NODES_INFO,
    CONFIG_DIR,
    MISSING_NODES_REPORT,
    NODE_VERSIONS,
    embedded_docs_dir,
    ensure_data_dir,
    load_dotenv,
)

load_dotenv()

COMFYUI_PATH = Path(os.getenv('COMFYUI_PATH', ''))
DOCS_PATH = embedded_docs_dir()

# Python file paths to scan
SCAN_PATHS = [
    COMFYUI_PATH / "nodes.py",
    COMFYUI_PATH / "comfy_extras",
    COMFYUI_PATH / "comfy_api_nodes",
]

# Documented node ids with no backend class. These are frontend virtual nodes
# (Note / Reroute / deprecated loaders) or nodes whose page is kept on purpose
# after the backend side moved on. Anything listed here is not reported as
# stale documentation.
NON_BACKEND_NODES_FILE = CONFIG_DIR / "non_backend_nodes.json"

# Attributes holding a node id on a class (V3 old style / V3 constant / V3 attribute).
ID_ATTRS = ("NodeId", "NODE_ID", "node_id")

NODE_ID_KWARG_BLOCKLIST = ("old_node_id", "new_node_id", "node_replace")


def normalize_node_name(name: str) -> str:
    """Comparison key: case, underscores, dashes and spaces are not significant."""
    return re.sub(r'[^a-z0-9]', '', name.strip().lower())


def load_non_backend_nodes() -> Set[str]:
    if not NON_BACKEND_NODES_FILE.exists():
        return set()
    try:
        data = json.loads(NON_BACKEND_NODES_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    if isinstance(data, dict):
        data = data.get("nodes", [])
    return {str(n).strip() for n in data if str(n).strip()}


class NodeScanner:
    """Node scanner to identify all ComfyUI nodes"""

    def __init__(self):
        self.all_nodes: Set[str] = set()
        self.node_info: Dict[str, Dict] = {}
        self.class_mappings: Dict[str, str] = {}   # mapping_name -> class_name
        self.renames: Dict[str, str] = {}          # retired node id -> current id
        self.class_kind: Dict[str, str] = {}       # class_name -> 'new_api' | 'classic'

    # ------------------------------------------------------------------ scan
    def scan_file_for_nodes(self, file_path: Path):
        """Scan a Python file to extract node definitions"""
        try:
            content = file_path.read_text(encoding='utf-8', errors='replace')
        except OSError as e:
            print(f"❌ Failed to read file {file_path}: {e}")
            return

        rel = str(file_path.relative_to(COMFYUI_PATH))
        try:
            tree: Optional[ast.Module] = ast.parse(content)
        except SyntaxError:
            tree = None
            print(f"⚠️  Syntax error, falling back to regex: {file_path}")

        if tree is None:
            for node_id in self._regex_node_ids(content):
                self._register(node_id, rel, 'new_api', self._regex_class_name(content, node_id))
            return

        self._collect_renames(tree)
        factories = self._schema_factories(tree)
        registered = self._registered_class_names(tree)
        loop_registered = self._loop_registered_class_names(tree)

        mappings = self._extract_node_class_mappings(tree, content)
        self.class_mappings.update(mappings)

        classes: Dict[str, ast.ClassDef] = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name not in classes:
                classes[node.name] = node
        # Kind is per module: two modules may define classes with the same name.
        self.class_kind = {}
        for name in classes:
            kind = self._class_kind(name, classes)
            if kind:
                self.class_kind[name] = kind

        # V1 registry: every key is a node type, aliases included.
        if mappings:
            for mapping_name, class_name in mappings.items():
                kind = self.class_kind.get(class_name, 'classic')
                self._register(mapping_name, rel, kind, class_name, source='NODE_CLASS_MAPPINGS')
        # V1 registry built in a loop: NODE_CLASS_MAPPINGS[node.NodeId] = node
        dynamic_nodeid = bool(re.search(r'NODE_CLASS_MAPPINGS\[\s*\w+\.NodeId\s*\]', content))
        v1_module = bool(mappings) or dynamic_nodeid

        for name, cls in classes.items():
            if name.startswith('_') or name not in self.class_kind:
                continue
            node_ids, explicit = self._class_node_ids(
                name, classes, tree, factories, mappings)
            if not node_ids:
                continue
            # Gate on the module's registration style, because a class being
            # defined is not the same as being registered: nodes are disabled by
            # commenting them out of get_node_list / node_list all the time.
            if registered:
                if name not in registered:
                    continue
            elif loop_registered is not None:
                if name not in loop_registered:
                    continue
            elif v1_module:
                # Literal NODE_CLASS_MAPPINGS already registered every key above.
                continue
            elif not explicit:
                continue

            category = self._extract_category_classic(content, name)
            for node_id in node_ids:
                self._register(
                    node_id, rel, self.class_kind[name], name,
                    category=category, source='schema' if self.class_kind[name] == 'new_api' else 'INPUT_TYPES')

    def scan_directory(self, dir_path: Path):
        """Recursively scan all Python files in directory"""
        if not dir_path.exists():
            print(f"⚠️  Path does not exist: {dir_path}")
            return

        for py_file in sorted(dir_path.rglob("*.py")):
            if '__pycache__' in str(py_file) or py_file.name.startswith('test_'):
                continue
            if '_test' in py_file.stem:
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
        print(f"✅ Scan completed, found {len(self.all_nodes)} nodes"
              + (f", {len(self.renames)} retired node id(s) known" if self.renames else "")
              + "\n")

    # ----------------------------------------------------------- registration
    def _register(self, node_id: str, rel: str, node_type: str, class_name: str,
                  category: str = "", source: str = "") -> None:
        node_id = node_id.strip()
        if not node_id:
            return
        existing = self.node_info.get(node_id)
        if existing is not None:
            # Prefer the richer entry but keep the first class/category we saw.
            if not existing.get('class_name') and class_name:
                existing['class_name'] = class_name
            if not existing.get('category') and category:
                existing['category'] = category
            return
        info = {
            'file': rel,
            'type': node_type,
            'class_name': class_name or node_id,
        }
        if source:
            info['source'] = source
        if category:
            info['category'] = category
        self.all_nodes.add(node_id)
        self.node_info[node_id] = info

    # ---------------------------------------------------------- node id rules
    def _collect_renames(self, tree: ast.Module) -> None:
        """Read io.NodeReplace(new_node_id=..., old_node_id=...) declarations."""
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if self._call_name(node) != "NodeReplace":
                continue
            new_id = old_id = None
            for kw in node.keywords:
                if kw.arg == "new_node_id":
                    new_id = self._resolve_str(kw.value, tree, "")
                elif kw.arg == "old_node_id":
                    old_id = self._resolve_str(kw.value, tree, "")
            if new_id and old_id:
                self.renames[old_id] = new_id

    def _class_node_ids(self, class_name: str, classes: Dict[str, ast.ClassDef],
                        tree: ast.Module, factories: Set[str],
                        mappings: Dict[str, str]) -> Tuple[List[str], bool]:
        """Node ids for one class, most specific source first.

        Returns (ids, explicit) — explicit means ComfyUI derives the id from the
        class itself rather than from the class name.
        """
        # 1. V1 registry keys that point at this class (aliases included)
        keys = [k.strip() for k, v in mappings.items() if v == class_name]
        if keys:
            return keys, True

        # 2. the schema this class returns: GET_SCHEMA() is what nodes.py registers,
        #    so a schema id always wins over a constant on the class.
        schema_ids = self._schema_ids(class_name, classes, tree, factories)
        if schema_ids:
            return schema_ids, True

        # 3. old-style NodeId / NODE_ID / node_id class attribute (no define_schema)
        for attr in ID_ATTRS:
            value = self._class_attr(classes, class_name, attr)
            if value:
                return [value.strip()], True

        return [class_name], False

    def _schema_ids(self, class_name: str, classes: Dict[str, ast.ClassDef],
                    tree: ast.Module, factories: Set[str]) -> List[str]:
        schema_fn = self._find_define_schema(class_name, classes)
        if schema_fn is None:
            return []

        mutated: List[str] = []     # schema.node_id = "X"  (after super())
        kwargs: List[str] = []      # node_id="X" / node_id=cls.NODE_ID
        positional: List[str] = []  # _cloud_schema("X", ...) / IO.Schema("X", ...)

        for node in ast.walk(schema_fn):
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Attribute) and target.attr == "node_id":
                        value = self._resolve_str(node.value, tree, class_name)
                        if value:
                            mutated.append(value)
            elif isinstance(node, ast.Call):
                call_name = self._call_name(node)
                for kw in node.keywords:
                    if kw.arg == "node_id":
                        value = self._resolve_str(kw.value, tree, class_name)
                        if value:
                            kwargs.append(value)
                is_schema = call_name == "Schema" or call_name in factories
                if is_schema:
                    for arg in node.args:
                        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
                            positional.append(arg.value)
                            break
        # A schema is built once: a later `schema.node_id = "X"` overrides the
        # node_id the call was constructed with, and neither is additive.
        for tier in (mutated, kwargs, positional):
            if tier:
                return tier[:1]
        return []

    @staticmethod
    def _base_class_names(cls: ast.ClassDef) -> List[str]:
        """Base classes that can be resolved inside this module.

        Only plain names qualify: ``comfy.samplers.CFGGuider`` lives in another
        module and must not be resolved to a same-named class here.
        """
        return [base.id for base in cls.bases if isinstance(base, ast.Name)]

    def _class_kind(self, class_name: str, classes: Dict[str, ast.ClassDef],
                    _depth: int = 0) -> Optional[str]:
        """'new_api' / 'classic' for a class, following base classes in this file."""
        if _depth > 6:
            return None
        cls = classes.get(class_name)
        if cls is None:
            return None
        for item in cls.body:
            if isinstance(item, ast.FunctionDef) and item.name == 'define_schema':
                return 'new_api'
            if isinstance(item, ast.FunctionDef) and item.name == 'INPUT_TYPES':
                return 'classic'
        for base_name in self._base_class_names(cls):
            kind = self._class_kind(base_name, classes, _depth + 1)
            if kind:
                return kind
        return None

    def _find_define_schema(self, class_name: str,
                            classes: Dict[str, ast.ClassDef],
                            _depth: int = 0) -> Optional[ast.FunctionDef]:
        if _depth > 6:
            return None
        cls = classes.get(class_name)
        if cls is None:
            return None
        for item in cls.body:
            if isinstance(item, ast.FunctionDef) and item.name == 'define_schema':
                return item
        for base_name in self._base_class_names(cls):
            found = self._find_define_schema(base_name, classes, _depth + 1)
            if found is not None:
                return found
        return None

    def _class_attr(self, classes: Dict[str, ast.ClassDef], class_name: str,
                    attr: str, _depth: int = 0) -> Optional[str]:
        """String value of a class attribute, walking base classes in this file."""
        if _depth > 6:
            return None
        cls = classes.get(class_name)
        if cls is None:
            return None
        for item in cls.body:
            targets: List[ast.expr] = []
            value_node: Optional[ast.expr] = None
            if isinstance(item, ast.Assign):
                targets = list(item.targets)
                value_node = item.value
            elif isinstance(item, ast.AnnAssign):
                targets = [item.target]
                value_node = item.value
            for target in targets:
                if isinstance(target, ast.Name) and target.id == attr:
                    if isinstance(value_node, ast.Constant) and isinstance(value_node.value, str):
                        return value_node.value
        for base_name in self._base_class_names(cls):
            value = self._class_attr(classes, base_name, attr, _depth + 1)
            if value:
                return value
        return None

    def _resolve_str(self, node: ast.AST, tree: ast.Module, class_name: str) -> Optional[str]:
        """Resolve a string expression: literal, cls.NODE_ID, module constant."""
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Attribute) and node.attr in ID_ATTRS:
            classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}
            return self._class_attr(classes, class_name, node.attr)
        if isinstance(node, ast.Name):
            classes = {n.name: n for n in tree.body if isinstance(n, ast.ClassDef)}
            value = self._class_attr(classes, class_name, node.id)
            if value:
                return value
            for item in tree.body:
                if isinstance(item, (ast.Assign, ast.AnnAssign)):
                    targets = item.targets if isinstance(item, ast.Assign) else [item.target]
                    for target in targets:
                        if isinstance(target, ast.Name) and target.id == node.id:
                            if isinstance(item.value, ast.Constant) and isinstance(item.value.value, str):
                                return item.value.value
        return None

    @staticmethod
    def _call_name(node: ast.Call) -> str:
        func = node.func
        if isinstance(func, ast.Attribute):
            return func.attr
        if isinstance(func, ast.Name):
            return func.id
        return ""

    @staticmethod
    def _schema_factories(tree: ast.Module) -> Set[str]:
        """Module-local helpers that build an IO.Schema (e.g. _cloud_schema)."""
        factories: Set[str] = set()
        for node in tree.body:
            if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue
            returns = ast.dump(node.returns) if node.returns is not None else ""
            body = "".join(ast.dump(stmt) for stmt in node.body)
            if "Schema" in returns or "Schema" in body:
                factories.add(node.name)
        return factories

    @staticmethod
    def _registered_class_names(tree: ast.Module) -> Set[str]:
        """Class names listed by get_node_list() — the V3 registry."""
        names: Set[str] = set()
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == 'get_node_list':
                for sub in ast.walk(node):
                    if isinstance(sub, ast.Return) and isinstance(sub.value, ast.List):
                        for elt in sub.value.elts:
                            if isinstance(elt, ast.Name):
                                names.add(elt.id)
                            elif isinstance(elt, ast.Attribute):
                                names.add(elt.attr)
        return names

    @staticmethod
    def _loop_registered_class_names(tree: ast.Module) -> Optional[Set[str]]:
        """Classes covered by `for node in <list>: NODE_CLASS_MAPPINGS[node.NodeId] = node`.

        Returns None when the module has no such loop.
        """
        for node in ast.walk(tree):
            if not isinstance(node, ast.For):
                continue
            if "NODE_CLASS_MAPPINGS" not in "".join(ast.dump(stmt) for stmt in node.body):
                continue
            iterable = node.iter
            names: Optional[Set[str]] = None
            if isinstance(iterable, ast.List):
                names = {e.id for e in iterable.elts if isinstance(e, ast.Name)}
            elif isinstance(iterable, ast.Name):
                for stmt in tree.body:
                    if not isinstance(stmt, ast.Assign) or not isinstance(stmt.value, ast.List):
                        continue
                    if any(isinstance(t, ast.Name) and t.id == iterable.id for t in stmt.targets):
                        names = {e.id for e in stmt.value.elts if isinstance(e, ast.Name)}
                        break
            if names is not None:
                return names
        return None

    def _extract_node_class_mappings(self, tree: ast.Module, content: str) -> Dict[str, str]:
        """Extract NODE_CLASS_MAPPINGS (literal dict, then regex fallback)."""
        mappings: Dict[str, str] = {}
        for node in ast.walk(tree):
            if not isinstance(node, ast.Assign):
                continue
            if not any(isinstance(t, ast.Name) and t.id == 'NODE_CLASS_MAPPINGS' for t in node.targets):
                continue
            if not isinstance(node.value, ast.Dict):
                continue
            for key, value in zip(node.value.keys, node.value.values):
                if isinstance(key, ast.Constant) and isinstance(key.value, str):
                    if isinstance(value, ast.Name):
                        mappings[key.value] = value.id
                    elif isinstance(value, ast.Attribute):
                        mappings[key.value] = value.attr
        if mappings:
            return mappings

        pattern = r'^NODE_CLASS_MAPPINGS\s*=\s*\{([^}]+)\}'
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)
        if match:
            pair_pattern = r'["\']([^"\']+)["\']\s*:\s*(\w+)'
            for pair_match in re.finditer(pair_pattern, match.group(1)):
                mappings[pair_match.group(1)] = pair_match.group(2)
        return mappings

    def _regex_node_ids(self, content: str) -> List[str]:
        """Last-resort extraction for files that do not parse.

        ``node_id=`` must not be part of ``old_node_id=``/``new_node_id=``.
        """
        pattern = r'(?<![A-Za-z0-9_])node_id\s*=\s*["\']([^"\']+)["\']'
        return [m.group(1).strip() for m in re.finditer(pattern, content)]

    def _regex_class_name(self, content: str, node_id: str) -> str:
        m = re.search(r'(?<![A-Za-z0-9_])node_id\s*=\s*["\']' + re.escape(node_id) + r'["\']', content)
        if not m:
            return node_id
        return self._find_class_name(content, m.start())

    def _find_class_name(self, content: str, pos: int) -> str:
        """Find class name by searching backwards from position"""
        lines_before = content[:pos].split('\n')
        for line in reversed(lines_before):
            match = re.search(r'class\s+(\w+)', line)
            if match:
                return match.group(1)
        return "Unknown"

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
        c = re.search(r"CATEGORY\s*=\s*[\"']([^\"']+)[\"']", block)
        if c:
            return c.group(1).strip()
        c = re.search(r"category\s*=\s*[\"']([^\"']+)[\"']", block)
        if c:
            return c.group(1).strip()
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

    def save_all_nodes_info(self, output_path: Path) -> None:
        """Save node_name -> { file, type, class_name, category?, ... } for all scanned nodes (for sync script)."""
        data = {
            "total": len(self.all_nodes),
            "retired_node_ids": dict(sorted(self.renames.items())),
            "nodes": {name: self.node_info.get(name, {}) for name in sorted(self.all_nodes)},
        }
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)


class DocumentationChecker:
    """Documentation checker"""

    def __init__(self, docs_path: Path):
        self.docs_path = docs_path
        self.documented_nodes: Set[str] = set()
        self.by_normalized: Dict[str, List[str]] = {}

    def scan_existing_docs(self):
        """Scan existing documentation folders"""
        print("📚 Scanning existing documentation...")

        if not self.docs_path.exists():
            print(f"❌ Documentation path does not exist: {self.docs_path}")
            return

        for item in self.docs_path.iterdir():
            if item.is_dir() and not item.name.startswith('.'):
                self.documented_nodes.add(item.name)
                self.by_normalized.setdefault(normalize_node_name(item.name), []).append(item.name)

        print(f"✅ Found {len(self.documented_nodes)} existing documentation\n")

    def match(self, node_id: str, loose: bool = True) -> List[str]:
        """Doc folders that document this node, whatever spelling they use."""
        if node_id in self.documented_nodes:
            return [node_id]
        if not loose:
            return []
        return sorted(self.by_normalized.get(normalize_node_name(node_id), []))

    def collisions(self, node_ids) -> Set[str]:
        """Normalized keys shared by more than one node id."""
        seen: Dict[str, int] = {}
        for node_id in node_ids:
            key = normalize_node_name(node_id)
            seen[key] = seen.get(key, 0) + 1
        return {key for key, count in seen.items() if count > 1}

    def check_doc_completeness(self, node_name: str) -> Dict[str, bool]:
        """Check documentation completeness for a single node"""
        node_dir = self.docs_path / node_name
        languages = ['en', 'zh', 'zh-TW', 'es', 'fr', 'ja', 'ko', 'ru', 'ar', 'tr', 'pt-BR', 'fa', 'de', 'he', 'it']

        completeness = {}
        for lang in languages:
            doc_file = node_dir / f"{lang}.md"
            completeness[lang] = doc_file.exists()

        return completeness


def extract_en_footer_hash(node_name: str) -> Optional[str]:
    """Read the SHA-256 source fingerprint from a node's en.md footer.

    The footer records the source hash at doc-generation time, so it serves
    as a baseline for change detection even when node_versions.json has no
    entry for this node (e.g. docs generated before version tracking existed).
    Returns None when the doc has no footer (legacy docs).
    """
    en_path = DOCS_PATH / node_name / "en.md"
    if not en_path.exists():
        return None
    try:
        content = en_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None
    m = re.search(r"SHA-256\)[:\uff1a]\s*\**\s*`([a-f0-9]{64})`", content)
    return m.group(1) if m else None


def classify_extra_docs(extra_docs: Set[str], scanner: NodeScanner,
                        doc_checker: DocumentationChecker,
                        non_backend: Set[str]) -> List[Dict]:
    """Explain why a documentation folder has no matching node.

    reason:
      duplicate   — the same node is already documented under its canonical folder
      renamed     — the node still exists under another id and has no canonical folder yet
      non_backend — documented frontend-only node (see config/non_backend_nodes.json)
      retired     — no node and no rename: candidate for archival
    """
    node_by_norm: Dict[str, List[str]] = {}
    for node_id in scanner.all_nodes:
        node_by_norm.setdefault(normalize_node_name(node_id), []).append(node_id)
    node_by_class: Dict[str, List[str]] = {}
    for node_id, info in scanner.node_info.items():
        node_by_class.setdefault(info.get('class_name', ''), []).append(node_id)

    rows = []
    for doc in sorted(extra_docs):
        row = {"name": doc, "reason": "retired", "target": None}
        key = normalize_node_name(doc)
        candidates = node_by_norm.get(key, []) if len(node_by_norm.get(key, [])) == 1 else []
        if candidates:
            target = sorted(candidates)[0]
            reason = "duplicate" if target in doc_checker.documented_nodes else "renamed"
            row.update(reason=reason, target=target)
        elif doc in scanner.renames:
            row.update(reason="renamed", target=scanner.renames[doc])
        elif doc in node_by_class:
            row.update(reason="renamed", target=sorted(node_by_class[doc])[0])
        elif doc in non_backend:
            row.update(reason="non_backend")
        else:
            key = normalize_node_name(doc)
            kin = [n for n in scanner.all_nodes
                   if normalize_node_name(n).startswith(key[:max(4, len(key) - 3)])]
            if kin:
                row["successor_hint"] = sorted(kin, key=len)[0]
        rows.append(row)
    return rows


def main():
    """Main function"""
    print("=" * 80)
    print("ComfyUI Node Documentation Missing Scanner")
    print("=" * 80)
    print()

    ensure_data_dir()

    # 1. Scan all nodes
    scanner = NodeScanner()
    scanner.scan_all()

    # Save full node info (including category) for sync script
    all_nodes_path = ALL_NODES_INFO
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

    # Two different node ids can normalize to the same key (`Foo_Bar` / `FooBar`);
    # such a key proves nothing, so those ids only accept an exact folder match.
    collisions = doc_checker.collisions(scanner.all_nodes)

    missing_nodes: Set[str] = set()
    folder_mismatches: Dict[str, List[str]] = {}
    matched_folders: Set[str] = set()
    for node_id in sorted(scanner.all_nodes):
        folders = doc_checker.match(node_id, loose=normalize_node_name(node_id) not in collisions)
        matched_folders.update(folders)
        if not folders:
            missing_nodes.add(node_id)
        elif node_id not in folders:
            folder_mismatches[node_id] = folders
            # Let change detection use the node's source for these pages.
            for folder in folders:
                scanner.node_info.setdefault(folder, dict(scanner.node_info.get(node_id, {}), alias_of=node_id))

    extra_docs = doc_checker.documented_nodes - scanner.all_nodes - matched_folders
    non_backend = load_non_backend_nodes()
    extra_detail = classify_extra_docs(extra_docs, scanner, doc_checker, non_backend)
    stale_docs = [row for row in extra_detail if row["reason"] == "retired"]

    print(f"🔢 Statistics:")
    print(f"   - Total nodes in code: {len(scanner.all_nodes)}")
    print(f"   - Nodes with documentation: {len(doc_checker.documented_nodes)}")
    print(f"   - Nodes missing documentation: {len(missing_nodes)}")
    print(f"   - Documented under a different spelling: {len(folder_mismatches)}")
    dup_count = len([r for r in extra_detail if r["reason"] == "duplicate"])
    ren_count = len([r for r in extra_detail if r["reason"] == "renamed"])
    nb_count = len([r for r in extra_detail if r["reason"] == "non_backend"])
    print(f"   - Extra documentation: {len(extra_docs)} "
          f"({len(stale_docs)} retired, {dup_count} duplicate, {ren_count} renamed, {nb_count} non-backend)")
    print()

    # 4. Output missing nodes list
    if missing_nodes:
        print("❌ Nodes missing documentation:")
        print("-" * 80)

        nodes_by_file = {}
        for node in sorted(missing_nodes):
            file_path = scanner.node_info.get(node, {}).get('file', 'unknown')
            nodes_by_file.setdefault(file_path, []).append(node)

        for file_path, nodes in sorted(nodes_by_file.items()):
            print(f"\n📄 {file_path}")
            for node in sorted(nodes):
                info = scanner.node_info.get(node, {})
                print(f"   - {node} ({info.get('type', 'unknown')}, "
                      f"class {info.get('class_name', '?')}, from {info.get('source', '?')})")
        print()
    else:
        print("✅ Great! All nodes have documentation!")
        print()

    # 5. Documented under a different spelling
    if folder_mismatches:
        print("⚠️  Documentation folder spelling differs from the node id "
              "(matched, no doc needed; rename if the folder name should follow the node id):")
        print("-" * 80)
        for node, folders in sorted(folder_mismatches.items()):
            print(f"   - node {node}  →  docs/{folders[0]}/")
        print()

    # 6. Extra documentation
    if extra_docs:
        duplicates = [row for row in extra_detail if row["reason"] == "duplicate"]
        renamed = [row for row in extra_detail if row["reason"] == "renamed"]
        if duplicates:
            print("♻️  Duplicate documentation folders (the canonical folder already exists — delete these):")
            print("-" * 80)
            for row in duplicates:
                print(f"   - docs/{row['name']}/  ==  docs/{row['target']}/")
            print()
        kept = [row for row in extra_detail if row["reason"] == "non_backend"]
        if renamed:
            print("🔁 Documentation for a renamed / aliased node (move the folder to the node id):")
            print("-" * 80)
            for row in renamed:
                print(f"   - docs/{row['name']}/  →  {row['target']}")
            print()
        if kept:
            print(f"🎨 Documented frontend / non-backend nodes ({len(kept)}): "
                  f"listed in {NON_BACKEND_NODES_FILE.relative_to(Path(__file__).resolve().parents[1])}")
            print()
        if stale_docs:
            print(f"⚠️  {len(stale_docs)} documentation folder(s) with no node in code "
                  f"(retired nodes / removed partner nodes) — archive or delete:")
            print("-" * 80)
            for row in stale_docs:
                hint = f"  (successor? {row['successor_hint']})" if row.get("successor_hint") else ""
                print(f"   - {row['name']}{hint}")
            print()

    # 7. Check completeness of existing documentation
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
        for node, missing_langs in sorted(incomplete_docs)[:10]:
            langs_str = ", ".join(missing_langs)
            print(f"   - {node}: Missing {langs_str}")

        if len(incomplete_docs) > 10:
            print(f"   ... and {len(incomplete_docs) - 10} more nodes")
        print()
    else:
        print("✅ Among existing docs: all contain all 7 language versions!")
        print("   (The nodes missing documentation above still need en.md generated first.)")
        print()

    # 8. Detect changed nodes (documented nodes whose source hash differs from recorded)
    print("=" * 80)
    print("🔄 Checking for changed nodes (source code hash comparison)")
    print("=" * 80)
    print("   Note: Extracting latest source code directly from ComfyUI to detect changes")
    print()

    version_db_path = NODE_VERSIONS
    version_db = {}
    if version_db_path.exists():
        with open(version_db_path, 'r', encoding='utf-8') as f:
            version_db = json.load(f).get("nodes", {})

    changed_nodes = []
    unverified_nodes = []
    extraction_failed = []

    for doc_name in sorted(doc_checker.documented_nodes):
        node_name = scanner.node_info.get(doc_name, {}).get("alias_of", doc_name)
        recorded_hash = extract_en_footer_hash(doc_name)
        source_baseline = "en.md footer"
        if not recorded_hash and node_name in version_db:
            recorded_hash = version_db[node_name].get("current_hash")
            source_baseline = "node_versions.json"
        if not recorded_hash:
            unverified_nodes.append(doc_name)
            continue

        info = scanner.node_info.get(node_name, {})
        if not info:
            continue

        file_path = COMFYUI_PATH / info.get('file', '')
        if not file_path.exists():
            extraction_failed.append(doc_name)
            continue

        class_name = info.get('class_name', node_name)
        current_class_src = extract_node_class_source(file_path, class_name)
        if not current_class_src:
            extraction_failed.append(doc_name)
            continue

        current_hash = hashlib.sha256(current_class_src.encode('utf-8')).hexdigest()
        if current_hash != recorded_hash:
            changed_nodes.append({
                "name": doc_name,
                "node_id": node_name,
                "file": info.get('file', 'unknown'),
                "type": info.get('type', 'classic'),
                "class_name": class_name,
                "old_hash": recorded_hash[:16] + "...",
                "new_hash": current_hash[:16] + "...",
                "baseline": source_baseline,
            })

    if changed_nodes:
        print(f"⚠️  Found {len(changed_nodes)} node(s) with changed source code:")
        for n in changed_nodes:
            target = f"  [docs/{n['name']} ← node {n['node_id']}]" if n['name'] != n['node_id'] else ""
            print(f"   - {n['name']}  ({n['old_hash']} → {n['new_hash']})  "
                  f"[baseline: {n['baseline']}]{target}")
        print()
    else:
        print("✅ No source code changes detected among documented nodes\n")

    if unverified_nodes:
        print(f"⚠️  {len(unverified_nodes)} node(s) have NO change-detection baseline "
              f"(no en.md footer, no node_versions.json entry):")
        print("   These are legacy docs — changes to their source will NOT be detected.")
        print("   Re-generate them once (--mode all --force) to add a footer baseline.")
        for name in sorted(unverified_nodes)[:10]:
            print(f"   - {name}")
        if len(unverified_nodes) > 10:
            print(f"   ... and {len(unverified_nodes) - 10} more")
        print()

    if extraction_failed:
        print(f"⚠️  Failed to extract source for {len(extraction_failed)} node(s):")
        for name in extraction_failed[:5]:
            print(f"   - {name}")
        if len(extraction_failed) > 5:
            print(f"   ... and {len(extraction_failed) - 5} more")
        print()

    # 9. Save results to JSON file
    output_file = MISSING_NODES_REPORT
    report = {
        "scan_time": str(Path(__file__).stat().st_mtime),
        "total_nodes": len(scanner.all_nodes),
        "documented_nodes": len(doc_checker.documented_nodes),
        "missing_count": len(missing_nodes),
        "folder_mismatch_count": len(folder_mismatches),
        "changed_count": len(changed_nodes),
        "missing_nodes": [
            {
                "name": node,
                "file": scanner.node_info.get(node, {}).get('file', 'unknown'),
                "type": scanner.node_info.get(node, {}).get('type', 'unknown'),
                "class_name": scanner.node_info.get(node, {}).get('class_name', 'unknown'),
                "source": scanner.node_info.get(node, {}).get('source', 'unknown'),
            }
            for node in sorted(missing_nodes)
        ],
        "folder_mismatches": {node: folders for node, folders in sorted(folder_mismatches.items())},
        "changed_nodes": changed_nodes,
        "unverified_nodes": sorted(unverified_nodes),
        "extra_docs": sorted(list(extra_docs)),
        "extra_docs_detail": extra_detail,
        "retired_node_ids": dict(sorted(scanner.renames.items())),
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
