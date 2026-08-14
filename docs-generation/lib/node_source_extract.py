"""
Richer extraction of ComfyUI node sources for docs + hashing.

Preset “depth” (optional): **NODE_SOURCE_EXTRACTION_DEPTH**
  shallow  — preamble off; no cross-file; tiny iteration budget (still class + optional resolve off)
  standard — slim preamble + strict imports (recommended default when unset); no cross-file
  deep     — full file preamble above the class + cross-file resolution on

Fine-grained env (always wins over preset when explicitly set):

  NODE_SOURCE_PREAMBLE_MODE=none|slim|full
    none — skip same-file preamble; cross-file snippets still obey NODE_SOURCE_RESOLVE_IMPORTS
  NODE_SOURCE_IMPORT_MATCH=strict|broad
    strict — an ``import a.b.c`` is kept only if a call chain uses ``a.b.c`` or a longer prefix
      (avoids pulling every ``import comfy.*`` when only ``comfy.sd`` is used)
    broad  — legacy behaviour: any ``comfy.`` callee pulled in all top-level ``comfy.*`` imports
  NODE_SOURCE_SLIM_ITERATIONS=N (default 3, max 32) — passes expanding helper symbols in slim mode

  NODE_SOURCE_RESOLVE_IMPORTS=0|1
  NODE_SOURCE_RESOLVE_MAX_FUNCS (default 8)
  NODE_SOURCE_RESOLVE_MAX_CHARS_EACH (default 6000)
  NODE_SOURCE_MAX_CONTEXT_CHARS

Overrides: NodeSourceExtractConfig / ``prepare_ai_input`` CLI (--source-*).
"""

from __future__ import annotations

import argparse
import ast
import os
import sys
import re
from dataclasses import dataclass, fields, replace
from pathlib import Path
from typing import Any, List, Optional, Set, Tuple


EXTRACTION_DEPTH_PRESETS: dict[str, dict[str, Any]] = {
    "shallow": {
        "preamble_mode": "none",
        "resolve_imports": False,
        "slim_iterations": 1,
        "import_match": "strict",
    },
    "standard": {
        "preamble_mode": "slim",
        "resolve_imports": False,
        "slim_iterations": 3,
        "import_match": "strict",
    },
    "deep": {
        "preamble_mode": "full",
        "resolve_imports": True,
        "slim_iterations": 3,
        "import_match": "strict",
    },
}


@dataclass(frozen=True)
class NodeSourceExtractConfig:
    """Configuration for preamble + optional cross-file resolution."""

    preamble_mode: str = "slim"
    resolve_imports: bool = False
    max_context_chars: int = 200_000
    resolve_max_funcs: int = 8
    resolve_max_chars_each: int = 6000
    import_match: str = "strict"  # strict | broad
    slim_iterations: int = 3

    @classmethod
    def from_env(cls) -> "NodeSourceExtractConfig":
        depth_key = os.getenv("NODE_SOURCE_EXTRACTION_DEPTH", "").strip().lower()
        preset = EXTRACTION_DEPTH_PRESETS.get(depth_key, {})

        def env_or(key: str) -> Optional[str]:
            v = os.getenv(key)
            if v is None:
                return None
            vs = v.strip()
            return vs if vs != "" else None

        def env_int_fallback(env_key: str, fallback: int) -> int:
            raw = env_or(env_key)
            if raw is None:
                return fallback
            try:
                return int(raw)
            except ValueError:
                return fallback

        # preamble
        preamble_mode = env_or("NODE_SOURCE_PREAMBLE_MODE")
        if preamble_mode is None:
            preamble_mode = str(preset.get("preamble_mode", "slim"))
        preamble_mode = preamble_mode.strip().lower()
        if preamble_mode not in ("none", "slim", "full"):
            preamble_mode = "slim"

        ri = env_or("NODE_SOURCE_RESOLVE_IMPORTS")
        if ri is None:
            resolve_imports = bool(preset.get("resolve_imports", False))
        else:
            resolve_imports = ri == "1"

        im_raw = env_or("NODE_SOURCE_IMPORT_MATCH")
        if im_raw is None:
            import_match = str(preset.get("import_match", "strict"))
        else:
            import_match = im_raw.lower()
        if import_match not in ("strict", "broad"):
            import_match = "strict"

        si_raw = env_or("NODE_SOURCE_SLIM_ITERATIONS")
        try:
            slim_iterations = int(si_raw) if si_raw is not None else int(preset.get("slim_iterations", 3))
        except ValueError:
            slim_iterations = int(preset.get("slim_iterations", 3))

        slim_iterations = max(1, min(slim_iterations, 32))

        max_context_chars = env_int_fallback("NODE_SOURCE_MAX_CONTEXT_CHARS", 200_000)
        resolve_max_funcs = env_int_fallback("NODE_SOURCE_RESOLVE_MAX_FUNCS", 8)
        resolve_max_chars_each = env_int_fallback("NODE_SOURCE_RESOLVE_MAX_CHARS_EACH", 6000)

        return cls(
            preamble_mode=preamble_mode,
            resolve_imports=resolve_imports,
            max_context_chars=max_context_chars,
            resolve_max_funcs=resolve_max_funcs,
            resolve_max_chars_each=resolve_max_chars_each,
            import_match=import_match,
            slim_iterations=slim_iterations,
        )


def register_source_extract_cli_args(parser: argparse.ArgumentParser) -> None:
    """Optional flags shared by prepare_ai_input (and tooling that uses the same parser)."""
    parser.add_argument(
        "--source-depth",
        choices=list(EXTRACTION_DEPTH_PRESETS.keys()),
        default=None,
        help=(
            "shallow|standard|deep bundle (CLI): maps to preamble / resolve / iterations / import_match. "
            "Runs after env; narrower --source-* flags override individual fields.",
        ),
    )
    parser.add_argument(
        "--source-preamble",
        choices=["none", "slim", "full"],
        default=None,
        help="same-file preamble: none | slim | full. Default NODE_SOURCE_PREAMBLE_MODE / depth preset.",
    )
    parser.add_argument(
        "--source-resolve",
        choices=["0", "1"],
        default=None,
        help="cross-file snippets (1=on). Default: NODE_SOURCE_RESOLVE_IMPORTS.",
    )
    parser.add_argument(
        "--source-max-context-chars",
        type=int,
        default=None,
        help="max assembled extract length (default NODE_SOURCE_MAX_CONTEXT_CHARS / 200000).",
    )
    parser.add_argument(
        "--source-resolve-max-funcs",
        type=int,
        default=None,
        help="max resolved callee snippets (NODE_SOURCE_RESOLVE_MAX_FUNCS).",
    )
    parser.add_argument(
        "--source-resolve-max-chars-each",
        type=int,
        default=None,
        help="max chars per resolved snippet (NODE_SOURCE_RESOLVE_MAX_CHARS_EACH).",
    )
    parser.add_argument(
        "--source-import-match",
        choices=["strict", "broad"],
        default=None,
        help=(
            "slim preamble import filter: strict (prefix-realistic) vs broad (legacy). "
            "NODE_SOURCE_IMPORT_MATCH."
        ),
    )
    parser.add_argument(
        "--source-slim-iterations",
        type=int,
        default=None,
        help="slim preamble expansion passes (1–32). NODE_SOURCE_SLIM_ITERATIONS.",
    )


def extract_config_from_parsed_args(namespace: argparse.Namespace) -> NodeSourceExtractConfig:
    """Merge NODE_SOURCE_* env with optional CLI overrides (for testing without editing .env)."""
    cfg = NodeSourceExtractConfig.from_env()

    sd = getattr(namespace, "source_depth", None)
    if sd:
        preset = EXTRACTION_DEPTH_PRESETS.get(sd.strip().lower())
        if preset:
            cfg = replace(
                cfg,
                preamble_mode=str(preset.get("preamble_mode", cfg.preamble_mode)),
                resolve_imports=bool(preset.get("resolve_imports", cfg.resolve_imports)),
                slim_iterations=max(
                    1,
                    min(int(preset.get("slim_iterations", cfg.slim_iterations)), 32),
                ),
                import_match=str(preset.get("import_match", cfg.import_match)),
            )

    replacements: dict[str, Any] = {}

    pm = getattr(namespace, "source_preamble", None)
    if pm is not None:
        replacements["preamble_mode"] = pm.strip().lower()

    sr = getattr(namespace, "source_resolve", None)
    if sr is not None:
        replacements["resolve_imports"] = sr == "1"

    smcc = getattr(namespace, "source_max_context_chars", None)
    if smcc is not None:
        replacements["max_context_chars"] = smcc

    srmf = getattr(namespace, "source_resolve_max_funcs", None)
    if srmf is not None:
        replacements["resolve_max_funcs"] = srmf

    srme = getattr(namespace, "source_resolve_max_chars_each", None)
    if srme is not None:
        replacements["resolve_max_chars_each"] = srme

    sim = getattr(namespace, "source_import_match", None)
    if sim is not None:
        replacements["import_match"] = sim.strip().lower()

    ssi = getattr(namespace, "source_slim_iterations", None)
    if ssi is not None:
        try:
            replacements["slim_iterations"] = max(1, min(int(ssi), 32))
        except (TypeError, ValueError):
            pass

    return replace(cfg, **replacements) if replacements else cfg


def merge_extract_config_overrides(base: Optional[NodeSourceExtractConfig] = None, **kw: Any) -> NodeSourceExtractConfig:
    """Build config from optional base + explicit overrides (None = omit)."""
    b = base or NodeSourceExtractConfig.from_env()
    replacements: dict[str, Any] = {}
    for f in fields(NodeSourceExtractConfig):
        k = f.name
        if k in kw and kw[k] is not None:
            replacements[k] = kw[k]
    return replace(b, **replacements)


def _is_registered_comfy_node_class(c: ast.ClassDef) -> bool:
    for item in c.body:
        if not isinstance(item, ast.FunctionDef):
            continue
        if item.name in ("INPUT_TYPES", "define_schema"):
            return True
    return False


def _stmt_source_lines(lines: List[str], stmt: ast.stmt) -> str:
    return "\n".join(lines[stmt.lineno - 1 : stmt.end_lineno])


def _attr_to_dotted(node: Optional[ast.AST]) -> Optional[str]:
    if node is None:
        return None
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        inner = _attr_to_dotted(node.value)
        if inner is None:
            return None
        return f"{inner}.{node.attr}"
    return None


def _collect_usage_from_class(class_node: ast.ClassDef) -> Tuple[Set[str], Set[str]]:
    bare: Set[str] = set()
    dotted: Set[str] = set()
    skip = frozenset(
        {"self", "cls", "Optional", "List", "Dict", "Set", "Tuple", "Union", "Any", "TypeVar"}
    )

    for node in ast.walk(class_node):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            if node.id not in skip and not node.id.startswith("_"):
                bare.add(node.id)

        if isinstance(node, ast.Call):
            ch = _attr_to_dotted(node.func)
            if ch:
                dotted.add(ch)
            elif isinstance(node.func, ast.Name):
                bare.add(node.func.id)
    return bare, dotted


def _import_top_bind(alias: ast.alias) -> str:
    name = alias.asname or alias.name
    return name.split(".")[0]


def _import_prefix_used_by_dotted(prefix: str, dotted: Set[str]) -> bool:
    """True if some attribute access / call chain equals or extends ``prefix`` (dot-separated)."""
    p = prefix.strip()
    if not p:
        return False
    for d in dotted:
        if d == p or d.startswith(p + "."):
            return True
    return False


def _preamble_stmt_used(stmt: ast.stmt, bare: Set[str], dotted: Set[str], import_match: str) -> bool:
    if isinstance(stmt, ast.Import):
        for al in stmt.names:
            mod_full = al.name or ""
            top = mod_full.split(".")[0] if mod_full else ""

            if al.asname:
                if al.asname in bare:
                    return True
            else:
                # Only ``import pkg`` (no dotted path) attaches the root symbol itself.
                # For ``import comfy.sd``, the bare Name ``comfy`` also appears inside attribute
                # chains (comfy.sd...) and must NOT pull every ``import comfy.*`` line.
                if top and top in bare and "." not in mod_full:
                    return True

            if import_match == "broad":
                bind = _import_top_bind(al)
                first = mod_full.split(".")[0] if mod_full else ""
                if bind in bare:
                    return True
                if any(x.startswith(bind + ".") or x.startswith(first + ".") for x in dotted):
                    return True
            elif mod_full and _import_prefix_used_by_dotted(mod_full, dotted):
                return True
        return False

    if isinstance(stmt, ast.ImportFrom):
        pkg = stmt.module or ""
        pkg0 = pkg.split(".")[0] if pkg else ""

        if import_match == "broad" and pkg:
            if any(d.startswith(pkg + ".") or (pkg0 and d.startswith(pkg0 + ".")) for d in dotted):
                return True
        elif pkg and _import_prefix_used_by_dotted(pkg, dotted):
            return True

        for al in stmt.names:
            if al.name == "*":
                return True
            bn = al.asname or al.name
            if bn in bare or al.name in bare:
                return True
            if pkg:
                fq = f"{pkg}.{al.name}"
                if fq in dotted or _import_prefix_used_by_dotted(fq, dotted):
                    return True

        return False

    if isinstance(stmt, (ast.Assign, ast.AnnAssign, ast.AugAssign)):
        targets = []
        if isinstance(stmt, ast.Assign):
            targets.extend(stmt.targets)
        elif isinstance(stmt, ast.AnnAssign):
            targets.append(stmt.target)
        else:
            targets.append(stmt.target)
        ids = []
        for t in targets:
            if isinstance(t, ast.Name):
                ids.append(t.id)
        return any(name in bare for name in ids)

    if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return stmt.name in bare
    if isinstance(stmt, ast.ClassDef):
        return stmt.name in bare
    return False


def _helper_absorb_bare(funcs: List[ast.FunctionDef | ast.AsyncFunctionDef], bare: Set[str]) -> Set[str]:
    out = set(bare)
    for hf in funcs:
        if hf.name not in out:
            continue
        for node in ast.walk(hf):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                if node.id not in ("self", "cls"):
                    out.add(node.id)
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                out.add(node.func.id)
    return out


def _deepen_helpers(preamble_stmts: List[ast.stmt], bare: Set[str]) -> Set[str]:
    hfs = [
        x
        for x in preamble_stmts
        if isinstance(x, (ast.FunctionDef, ast.AsyncFunctionDef)) and x.name in bare
    ]
    return _helper_absorb_bare(hfs, bare)


def _build_slim_preamble(
    preamble_stmts: List[ast.stmt],
    lines_list: List[str],
    bare0: Set[str],
    dotted0: Set[str],
    *,
    slim_iterations: int,
    import_match: str,
) -> str:
    bare = _deepen_helpers(preamble_stmts, set(bare0))
    dotted = set(dotted0)
    n_pass = max(1, min(slim_iterations, 32))
    for _ in range(n_pass):
        sel = [st for st in preamble_stmts if _preamble_stmt_used(st, bare, dotted, import_match)]
        nb = set(bare)
        for st in sel:
            if isinstance(st, (ast.FunctionDef, ast.AsyncFunctionDef)):
                for n in ast.walk(st):
                    if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Load):
                        nid = n.id
                        if nid not in ("self", "cls") and not nid.startswith("__"):
                            nb.add(nid)
        if nb <= bare:
            break
        bare = nb | bare
        bare = _deepen_helpers(preamble_stmts, bare)
    chunks = [
        _stmt_source_lines(lines_list, st)
        for st in preamble_stmts
        if _preamble_stmt_used(st, bare, dotted, import_match)
    ]
    return "\n\n".join(c for c in chunks if c.strip())


def _resolve_module_file(comfy_root: Path, mod_dotted: str) -> Optional[Path]:
    comfy_root = comfy_root.resolve()
    parts = mod_dotted.split(".")
    if len(parts) == 1:
        fp = comfy_root / f"{parts[0]}.py"
        if fp.is_file():
            return fp
        init_py = comfy_root / parts[0] / "__init__.py"
        return init_py if init_py.is_file() else None
    dpath = comfy_root.joinpath(*parts)
    cand = dpath.with_suffix(".py")
    if cand.is_file():
        return cand
    init_py = dpath / "__init__.py"
    return init_py if init_py.is_file() else None


def _slice_named_block(mod_file: Path, remainder: List[str]) -> Optional[str]:
    """remainder: ['load_checkpoint_guess_config'] or nested ['Class','meth']."""
    try:
        text = mod_file.read_text(encoding="utf-8")
        tree = ast.parse(text)
    except (SyntaxError, OSError):
        return None

    if len(remainder) == 1:
        tgt = remainder[0]
        for stmt in ast.walk(tree):
            if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if stmt.name == tgt and stmt.lineno is not None and stmt.end_lineno is not None:
                    chunk = "\n".join(text.split("\n")[stmt.lineno - 1 : stmt.end_lineno])
                    return chunk
        for stmt in tree.body:
            if isinstance(stmt, ast.Assign):
                for t in stmt.targets:
                    if isinstance(t, ast.Name) and t.id == tgt and stmt.lineno and stmt.end_lineno:
                        return "\n".join(text.split("\n")[stmt.lineno - 1 : stmt.end_lineno])
        return None

    body = tree.body
    cur: Optional[ast.ClassDef | ast.FunctionDef | ast.AsyncFunctionDef] = None
    for i, part in enumerate(remainder[:-1]):
        found_cls = None
        for stmt in body:
            if isinstance(stmt, ast.ClassDef) and stmt.name == part:
                found_cls = stmt
                break
        if found_cls is None:
            return None
        body = found_cls.body
        cur = found_cls

    last = remainder[-1]
    for stmt in body:
        if isinstance(stmt, (ast.FunctionDef, ast.AsyncFunctionDef)) and stmt.name == last:
            assert stmt.lineno and stmt.end_lineno
            return "\n".join(text.split("\n")[stmt.lineno - 1 : stmt.end_lineno])
    return None


def _try_resolve_dotted(dotted_call: str, comfy_root: Path, resolve_max_chars_each: int) -> Optional[str]:
    parts = dotted_call.split(".")
    if len(parts) < 2:
        return None
    cap_n = resolve_max_chars_each
    for depth in range(len(parts) - 1, 0, -1):
        mod_dots = ".".join(parts[:depth])
        remainder = parts[depth:]
        if not remainder:
            continue
        mf = _resolve_module_file(comfy_root, mod_dots)
        if mf is None or not mf.is_file():
            continue
        sn = _slice_named_block(mf, remainder)
        if sn:
            try:
                rel = mf.relative_to(comfy_root)
            except ValueError:
                rel = mf.name
            cap = sn[:cap_n]
            if len(sn) > cap_n:
                cap += "\n# ... truncated (resolve_max_chars_each) ..."
            return f"# module: {mod_dots}  file: {rel}\n{cap}"
    return None


def _cross_file_section(comfy_root: Path, dotted: Set[str], config: NodeSourceExtractConfig) -> str:
    if not (config.resolve_imports and comfy_root.is_dir()):
        return ""

    comfy_root = comfy_root.resolve()

    chunks: List[str] = []
    n = 0
    for call in sorted(dotted):
        if n >= config.resolve_max_funcs:
            break
        got = _try_resolve_dotted(call, comfy_root, config.resolve_max_chars_each)
        if got:
            chunks.extend([f"\n# --- resolved call chain: {call} ---", got])
            n += 1
    if not chunks:
        return ""
    hdr = "# --- cross-file context (NODE_SOURCE_RESOLVE_IMPORTS=1, under COMFYUI_PATH) ---"
    return "\n".join([hdr] + chunks) + "\n"


def extract_node_source_with_context(
    file_path: Path,
    class_name: str,
    *,
    node_type_hint: Optional[str] = None,
    comfy_root: Optional[Path] = None,
    config: Optional[NodeSourceExtractConfig] = None,
) -> str:
    del node_type_hint
    cfg = config or NodeSourceExtractConfig.from_env()
    max_chars = cfg.max_context_chars
    if comfy_root is not None:
        root = comfy_root
    else:
        _cu = Path(os.getenv("COMFYUI_PATH", ""))
        root = _cu if _cu.is_dir() else Path()

    path = Path(file_path)
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return ""

    lines_list = content.split("\n")

    try:
        tree = ast.parse(content)
    except SyntaxError:
        return _fallback_class_only_regex(content, lines_list, class_name)

    target: Optional[ast.ClassDef] = None
    preamble_stmts: List[ast.stmt] = []

    for stmt in tree.body:
        if isinstance(stmt, ast.ClassDef) and stmt.name == class_name:
            target = stmt
            break
        if isinstance(stmt, ast.ClassDef) and _is_registered_comfy_node_class(stmt):
            continue
        preamble_stmts.append(stmt)

    if target is None:
        return _fallback_class_only_regex(content, lines_list, class_name)

    class_src_lines = lines_list[target.lineno - 1 : target.end_lineno]
    class_src = "\n".join(class_src_lines)

    MARK_PRE = "# --- preceding context (same-file, AST-filtered unless PREAMBLE_MODE=full) ---"
    MARK_CLS = "# --- node class ---"

    bare, dotted = _collect_usage_from_class(target)

    preamble_mode = (cfg.preamble_mode or "slim").strip().lower()
    if preamble_mode == "full":
        pre_segs = [_stmt_source_lines(lines_list, st) for st in preamble_stmts]
        preamble_joined = "\n\n".join(s for s in pre_segs if s.strip())
    elif preamble_mode == "none":
        preamble_joined = ""
    else:
        preamble_joined = _build_slim_preamble(
            preamble_stmts,
            lines_list,
            bare,
            dotted,
            slim_iterations=cfg.slim_iterations,
            import_match=cfg.import_match,
        )

    ext = _cross_file_section(root, dotted, cfg) if root.is_dir() else ""

    # Order: preamble (slim/full) → cross-file → node class

    blocks: List[str] = []
    if preamble_joined.strip():
        blocks.append(MARK_PRE + "\n" + preamble_joined)
    if ext.strip():
        blocks.append(ext.strip())
    blocks.append(MARK_CLS + "\n" + class_src)

    out = "\n\n".join(blocks)

    cls_block_only = MARK_CLS + "\n" + class_src
    note = "# --- preamble trimmed (max_context_chars cap) ---\n\n"

    if len(out) <= max_chars:
        return out

    # Drop cross-file first, then preamble tail, keeping full classSrc
    slack = max_chars - len(cls_block_only) - 48
    if slack <= 0:
        return cls_block_only[:max_chars]

    if ext.strip():
        ext_short = ext
        cand = ("\n\n".join([MARK_PRE + "\n" + preamble_joined, ext_short.strip(), cls_block_only]) if preamble_joined.strip() else ("\n\n".join([ext_short.strip(), cls_block_only])))
        if len(cand) <= max_chars:
            return cand
        cand2 = MARK_CLS + "\n" + class_src
        if preamble_joined.strip():
            preamble_reduced = note + preamble_joined.strip()[- (slack // 2) :]
            return (MARK_PRE + "\n" + preamble_reduced + "\n\n" + cls_block_only)[:max_chars]
        return cls_block_only[:max_chars]

    if preamble_joined.strip():
        pre = preamble_joined.strip()
        if len(pre) > slack:
            pre = note + pre[-slack:]
        return (MARK_PRE + "\n" + pre + "\n\n" + cls_block_only)[:max_chars]
    return cls_block_only[:max_chars]


def _fallback_class_only_regex(content: str, lines_list: List[str], class_name: str) -> str:
    pattern = rf"class\s+{re.escape(class_name)}\b.*?(?=\n(?:class\s|\Z|async def comfy_entrypoint))"
    match = re.search(pattern, content, re.DOTALL)
    if match:
        return "# --- node class (fallback extract) ---\n" + match.group(0).rstrip()
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return ""
    cand: Optional[ast.ClassDef] = None
    for stmt in tree.body:
        if isinstance(stmt, ast.ClassDef) and stmt.name == class_name:
            cand = stmt
            break
    if cand is None:
        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef) and node.name == class_name:
                cand = node
                break
    if cand is None:
        return ""
    return "# --- node class (fallback extract) ---\n" + "\n".join(
        lines_list[cand.lineno - 1 : cand.end_lineno]
    )


_FALLBACK_MARK = "# --- node class (fallback extract) ---\n"


def extract_node_class_source(file_path: Path, class_name: str) -> str:
    """Return only the node's `class` definition from the real source file (no preamble / cross-file bundle).

    Used for version fingerprints: contextual extracts can change when resolved callees or imports
    shift, but the registered node class is the stable contract for "did this node change?"
    """
    path = Path(file_path)
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return ""

    lines_list = content.split("\n")
    try:
        tree = ast.parse(content)
    except SyntaxError:
        return _strip_fallback_class_banner(_fallback_class_only_regex(content, lines_list, class_name))

    target: Optional[ast.ClassDef] = None
    for stmt in tree.body:
        if isinstance(stmt, ast.ClassDef) and stmt.name == class_name:
            target = stmt
            break

    if target is None:
        return _strip_fallback_class_banner(_fallback_class_only_regex(content, lines_list, class_name))

    return "\n".join(lines_list[target.lineno - 1 : target.end_lineno])


def class_source_from_contextual_bundle(text: str) -> str:
    """If `text` is a contextual bundle (preamble + optional cross-file + node class), return class part only."""
    marker = "# --- node class ---"
    if marker in text:
        return text.split(marker, 1)[1].lstrip("\n")
    if text.startswith(_FALLBACK_MARK):
        return text[len(_FALLBACK_MARK) :].lstrip("\n")
    return text


def _strip_fallback_class_banner(text: str) -> str:
    if text.startswith(_FALLBACK_MARK):
        return text[len(_FALLBACK_MARK) :]
    return text


def extract_node_source_code(
    file_path: Path,
    class_name: str,
    node_type: str,
    *,
    comfy_root: Optional[Path] = None,
    config: Optional[NodeSourceExtractConfig] = None,
) -> str:
    _ = node_type  # compat
    if comfy_root is not None:
        cr_opt = comfy_root if comfy_root.is_dir() else None
    else:
        comfy = Path(os.getenv("COMFYUI_PATH", ""))
        cr_opt = comfy if comfy.is_dir() else None
    return extract_node_source_with_context(
        file_path, class_name, comfy_root=cr_opt, config=config
    )


def extract_node_source_code_with_root(
    file_path: Path,
    class_name: str,
    node_type: str,
    *,
    comfy_root: Path,
    config: Optional[NodeSourceExtractConfig] = None,
) -> str:
    return extract_node_source_code(
        file_path, class_name, node_type, comfy_root=comfy_root, config=config
    )


def _cli_main(argv: Optional[List[str]] = None) -> int:
    """
    Smoke-test extractor without modifying env:
      python node_source_extract.py \\
        --py /abs/path/nodes.py --class CheckpointLoader \\
        [--comfy-root /path/to/ComfyUI] [--source-preamble slim|full] [--source-resolve 0|1]
    """
    p = argparse.ArgumentParser(description="Print extracted node source to stdout.")
    p.add_argument("--py", "--file", dest="py_file", type=Path, required=True)
    p.add_argument("--class", dest="class_name", required=True, help="Python class name to extract.")
    register_source_extract_cli_args(p)
    p.add_argument("--comfy-root", type=Path, default=None, help="ComfyUI root (default COMFYUI_PATH).")
    args = p.parse_args(argv)
    cfg = extract_config_from_parsed_args(args)
    root = args.comfy_root
    if root is None:
        c = Path(os.getenv("COMFYUI_PATH", ""))
        root = c if c.is_dir() else None
    txt = extract_node_source_code(
        Path(args.py_file),
        args.class_name,
        "cli",
        comfy_root=root,
        config=cfg,
    )
    if not txt:
        return 1
    sys.stdout.write(txt)
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli_main())
