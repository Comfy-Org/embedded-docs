#!/usr/bin/env python3
"""
Sync embedded-docs (en.md / zh.md / ja.md / ko.md + assets) to comfy/docs as NodeName.mdx.
Copies images to docs/images/built-in-nodes/<NodeName>/ and updates docs.json nav.

Env:
  EMBEDDED_DOCS_PATH  - repo root (default: script parent's parent)
  COMFYUI_PATH       - ComfyUI repo for category parsing
  TARGET_DOCS        - comfy/docs root (e.g. /path/to/comfy/docs)
"""

import argparse
import json
import os
import re
import shutil
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any, Optional

import runtime  # noqa: F401
from lib.paths import ALL_NODES_INFO, default_embedded_docs_path, load_dotenv

load_dotenv()

ALL_NODES_INFO_PATH = ALL_NODES_INFO

# Cache: node_name -> category (first segment). Loaded from scanner output if available.
_nodes_info_cache: Optional[dict[str, dict[str, Any]]] = None


def _load_all_nodes_info() -> dict[str, dict[str, Any]]:
    """Load all_nodes_info.json from scanner (node_name -> { file, category?, ... })."""
    global _nodes_info_cache
    if _nodes_info_cache is not None:
        return _nodes_info_cache
    if not ALL_NODES_INFO_PATH.exists():
        _nodes_info_cache = {}
        return _nodes_info_cache
    try:
        with open(ALL_NODES_INFO_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        _nodes_info_cache = data.get("nodes", {})
        return _nodes_info_cache
    except Exception:
        _nodes_info_cache = {}
        return _nodes_info_cache

EMBEDDED_DOCS_PATH = default_embedded_docs_path()
COMFYUI_PATH = Path(os.getenv("COMFYUI_PATH", ""))
_SCRIPT_DIR = Path(__file__).resolve().parent.parent
TARGET_DOCS = Path(os.getenv("TARGET_DOCS", _SCRIPT_DIR / ".." / "docs"))

DOCS_SOURCE = EMBEDDED_DOCS_PATH / "comfyui_embedded_docs" / "docs"
BUILTIN_EN = TARGET_DOCS / "built-in-nodes"
BUILTIN_ZH = TARGET_DOCS / "zh" / "built-in-nodes"
BUILTIN_JA = TARGET_DOCS / "ja" / "built-in-nodes"
BUILTIN_KO = TARGET_DOCS / "ko" / "built-in-nodes"
IMAGES_TARGET = TARGET_DOCS / "images" / "built-in-nodes"
DOCS_JSON = TARGET_DOCS / "docs.json"

# Locale sync + docs.json navigation (language code -> config)
LOCALE_CONFIGS: list[dict[str, Any]] = [
    {
        "code": "en",
        "md_file": "en.md",
        "builtin_dir": BUILTIN_EN,
        "page_prefix": "built-in-nodes",
        "tab": "Built-in Nodes",
        "wrapper": "Nodes",
        "default_group": "Advanced",
        "lang_idx": 0,
    },
    {
        "code": "zh",
        "md_file": "zh.md",
        "builtin_dir": BUILTIN_ZH,
        "page_prefix": "zh/built-in-nodes",
        "tab": "内置节点",
        "wrapper": "节点",
        "default_group": "高级",
        "lang_idx": 1,
    },
    {
        "code": "ja",
        "md_file": "ja.md",
        "builtin_dir": BUILTIN_JA,
        "page_prefix": "ja/built-in-nodes",
        "tab": "組み込みノード",
        "wrapper": "ノード",
        "default_group": "上級",
        "lang_idx": 2,
    },
    {
        "code": "ko",
        "md_file": "ko.md",
        "builtin_dir": BUILTIN_KO,
        "page_prefix": "ko/built-in-nodes",
        "tab": "내장 노드 (Built-in Nodes)",
        "wrapper": "노드",
        "default_group": "고급",
        "lang_idx": 3,
    },
]

SCAN_PATHS = [
    COMFYUI_PATH / "nodes.py",
    COMFYUI_PATH / "comfy_extras",
    COMFYUI_PATH / "comfy_api_nodes",
]

# ComfyUI category (first segment) -> (EN, zh, ja, ko group labels) for docs.json
# If a category is not in this map, a new group is created with the category name (EN); other locales use EN when no translation.
CATEGORY_TO_GROUP = {
    "conditioning": ("Conditioning", "条件", "条件付け", "컨디셔닝"),
    "loaders": ("Loader", "加载器", "ローダー", "로더"),
    "image": ("Image", "图像", "画像", "이미지"),
    "latent": ("Latent", "潜变量", "潜在変数", "잠재 변수"),
    "sampling": ("Sampling", "采样", "サンプリング", "샘플링"),
    "3d": ("3D", "3D", "3D", "3D"),
    "3D": ("3D", "3D", "3D", "3D"),
    "advanced": ("Advanced", "高级", "上級", "고급"),
    "utils": ("Utils", "实用工具", "ユーティリティ", "유틸리티"),
    "utility": ("Utils", "实用工具", "ユーティリティ", "유틸리티"),
    "util": ("Utils", "实用工具", "ユーティリティ", "유틸리티"),
    "_for_testing": ("Advanced", "高级", "上級", "고급"),
    "api": ("API", "API", "API", "API"),
    "api node": ("API Node", "API Node", "API Node", "API Node"),
    "model_patches": ("Model Patches", "模型补丁", "モデルパッチ", "모델 패치"),
    "dataset": ("Image", "图像", "画像", "이미지"),
    "audio": ("Audio", "Audio", "Audio", "Audio"),
    "basics": ("Basics", "Basics", "Basics", "Basics"),
    "camera": ("Camera", "Camera", "Camera", "Camera"),
    "context": ("Context", "Context", "Context", "Context"),
    "image generation": ("Image", "图像", "画像", "이미지"),
    "image tools": ("Image", "图像", "画像", "이미지"),
    "logic": ("Logic", "Logic", "Logic", "Logic"),
    "mask": ("Mask", "Mask", "Mask", "Mask"),
    "textgen": ("Textgen", "Textgen", "Textgen", "Textgen"),
    "training": ("Training", "Training", "Training", "Training"),
    "transform": ("Transform", "Transform", "Transform", "Transform"),
    "guidance": ("Sampling", "采样", "サンプリング", "샘플링"),
}
DEFAULT_GROUP_EN = "Advanced"
DEFAULT_GROUP_ZH = "高级"
DEFAULT_GROUP_JA = "上級"
DEFAULT_GROUP_KO = "고급"

# Hardcoded category fallback for nodes that the scanner cannot resolve:
# - replacement nodes in nodes_replacements.py (no category field)
# - deprecated / aliased nodes not found in current source
# - partner API nodes with flat MDX files but no scanner entry
_FALLBACK_CATEGORY: dict[str, str] = {
    # Replacement nodes (nodes_replacements.py) — inherit from their original
    "BatchImagesNode": "image",
    "ConditioningAverage": "conditioning",
    "ControlNetLoader": "loaders",
    "HunyuanRefinerLatent": "conditioning",
    "HunyuanVideo15SuperResolution": "loaders",
    "ImageBatch": "image",
    "ImageScaleBy": "image/upscaling",
    "Load3D": "3d",
    "Load3DAnimation": "3d",
    "Preview3D": "3d",
    "Preview3DAnimation": "3d",
    "ResizeImageMaskNode": "image",
    "SVD_img2vid_Conditioning": "conditioning/video_models",
    "SDV_img2vid_Conditioning": "conditioning/video_models",
    "T2IAdapterLoader": "loaders",
    "wanBlockSwap": "utils",
    # Model merging
    "CLIPAdd": "advanced/model_merging",
    "CLIPSubtract": "advanced/model_merging",
    "SaveLoRANode": "advanced/model_merging",
    # Deprecated loaders
    "DeprecatedCheckpointLoader": "advanced/loaders",
    "DeprecatedDiffusersLoader": "advanced/loaders",
    # Model patches
    "EpsilonScaling": "model_patches/unet",
    # Partner API nodes (flat MDX files)
    "FluxProCannyNode": "api node/image/BFL",
    "FluxProDepthNode": "api node/image/BFL",
    "FluxProImageNode": "api node/image/BFL",
    "ByteDanceImageEditNode": "api node/image/ByteDance",
    "PikaImageToVideoNode2_2": "api node/video/Pika",
    "PikaScenesV2_2": "api node/video/Pika",
    "PikaStartEndFrameNode2_2": "api node/video/Pika",
    "PikaTextToVideoNode2_2": "api node/video/Pika",
    "Pikadditions": "api node/video/Pika",
    "Pikaffects": "api node/video/Pika",
    "Pikaswaps": "api node/video/Pika",
    # Image / dataset
    "LoadImageSetFromFolderNode": "image",
    "LoadImageSetNode": "image",
    "LoadImageTextSetFromFolderNode": "image",
    # Utils
    "MarkdownNote": "utils",
    "Note": "utils",
    "Reroute": "utils",
    "TerminalLog": "utils",
    # Sampling (renamed aliases)
    "SamplerDpmpp2mSde": "sampling/custom_sampling/samplers",
    "SamplerDpmppSde": "sampling/custom_sampling/samplers",
    # Conditioning (deprecated aliases)
    "Sd4xupscaleConditioning": "conditioning",
    "Stablezero123Conditioning": "conditioning/video_models",
    "Stablezero123ConditioningBatched": "conditioning/video_models",
    "SvdImg2vidConditioning": "conditioning/video_models",
    # _for_testing nodes with no sub-path (scanner returns just "_for_testing")
    "DifferentialDiffusion": "sampling",
    "FreSca": "advanced",
    "LatentBlend": "latent",
    "LoadLatent": "loaders",
    "LoraSave": "advanced/model_merging",
    "Mahiro": "utils",
    "PerpNeg": "conditioning",
    "PerpNegGuider": "sampling",
    "SamplerEulerCFGpp": "sampling/custom_sampling/samplers",
    "SaveLatent": "latent",
    "SelfAttentionGuidance": "sampling",
    "TorchCompileModel": "advanced",
    "VAEDecodeTiled": "latent",
    "VAEEncodeTiled": "latent",
}

def _default_group_for_lang(lang_idx: int) -> str:
    return (DEFAULT_GROUP_EN, DEFAULT_GROUP_ZH, DEFAULT_GROUP_JA, DEFAULT_GROUP_KO)[lang_idx]


def _group_label_for_category(first_segment: str, lang_idx: int) -> str:
    first_lower = first_segment.lower()
    if first_lower in CATEGORY_TO_GROUP:
        return CATEGORY_TO_GROUP[first_lower][lang_idx]
    return _seg_to_label(first_segment)


def _find_lang_entry(nav: dict[str, Any], lang_code: str) -> Optional[dict[str, Any]]:
    for entry in nav.get("navigation", {}).get("languages", []):
        if entry.get("language") == lang_code:
            return entry
    return None


def _find_tab_pages(lang_entry: dict[str, Any], tab_name: str) -> Optional[list[Any]]:
    for tab in lang_entry.get("tabs", []):
        if tab.get("tab") == tab_name and "pages" in tab:
            return tab["pages"]
    return None


def _seg_to_label(seg: str) -> str:
    """Convert a path segment like 'custom_sampling' to a display label 'Custom Sampling'.

    Preserves already-uppercase tokens (acronyms such as BFL, SDXL, API) unchanged
    instead of title-casing them into 'Sdxl' / 'Api'.
    """
    return " ".join(
        token if token.isupper() and len(token) > 1 else token.capitalize()
        for token in seg.replace("_", " ").replace("-", " ").split()
    )


def _category_to_group_and_sub(full_category_path: str, lang_idx: int = 0) -> tuple[str, Optional[str]]:
    """Return (group label, sub-group label or None) for the given locale index.

    Always uses the FIRST segment to determine the top-level group so that the
    hierarchy mirrors ComfyUI's node menu exactly.
    """
    if not full_category_path or not full_category_path.strip():
        return _default_group_for_lang(lang_idx), None
    raw = full_category_path.strip()
    segments = [s.strip() for s in raw.split("/") if s.strip()]
    if not segments:
        return _default_group_for_lang(lang_idx), None
    group_label = _group_label_for_category(segments[0], lang_idx)
    if len(segments) > 1:
        return group_label, _seg_to_label(segments[1])
    return group_label, None

# Regex for local image/asset refs and disclaimer
MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
HTML_SRC_RE = re.compile(r'<(?:img|video|audio|source)[^>]+src=["\']([^"\'>]+)["\']', re.IGNORECASE)
def is_local_link(href: str) -> bool:
    href = href.strip().split("#")[0].split("?")[0]
    return bool(href) and not (
        href.startswith("http://")
        or href.startswith("https://")
        or href.startswith("data:")
    )


def _class_name_variants(node_name: str) -> list[str]:
    """Return possible class names in source (e.g. ClipTextEncode <-> CLIPTextEncode)."""
    variants = [node_name]
    if node_name.startswith("Clip") and len(node_name) > 4:
        variants.append("CLIP" + node_name[4:])
    elif node_name.startswith("CLIP") and len(node_name) > 4:
        variants.append("Clip" + node_name[4:])
    return variants


def _category_from_class_block(text: str, node_name: str, first_segment_only: bool = True) -> Optional[str]:
    """Extract category from a class block. If first_segment_only, return first path segment."""
    for class_name in _class_name_variants(node_name):
        class_pattern = re.compile(
            r"^class\s+" + re.escape(class_name) + r"\s*[:(].*?(?=^class\s|\Z)",
            re.MULTILINE | re.DOTALL,
        )
        m = class_pattern.search(text)
        if not m:
            continue
        block = m.group(0)
        for pattern in (r"CATEGORY\s*=\s*[\"']([^\"']+)[\"']", r"category\s*=\s*[\"']([^\"']+)[\"']"):
            c = re.search(pattern, block)
            if c:
                raw = c.group(1).strip()
                return raw.split("/")[0] if first_segment_only else raw
    return None


def _category_from_schema_node_id(text: str, node_name: str, first_segment_only: bool = True) -> Optional[str]:
    """Extract category from Schema that contains node_id='NodeName'."""
    escaped = re.escape(node_name)
    idx = re.search(r'node_id\s*=\s*["\']' + escaped + r'["\']', text)
    if not idx:
        return None
    start = max(0, idx.start() - 400)
    end = min(len(text), idx.end() + 400)
    window = text[start:end]
    c = re.search(r'category\s*=\s*["\']([^"\']+)["\']', window)
    if c:
        raw = c.group(1).strip()
        return raw.split("/")[0] if first_segment_only else raw
    return None


@lru_cache(maxsize=None)
def _comfyui_source_files() -> tuple[Path, ...]:
    """Cached list of ComfyUI Python source files under SCAN_PATHS (read once)."""
    files: list[Path] = []
    for base in SCAN_PATHS:
        if not base.exists():
            continue
        files.extend([base] if base.is_file() else list(base.rglob("*.py")))
    return tuple(files)


def _read_comfyui_source(path: Path) -> str:
    """Read a ComfyUI source file, tolerating decode errors (cached per file)."""
    return path.read_text(encoding="utf-8", errors="ignore")


def extract_category_full_from_comfyui(node_name: str) -> Optional[str]:
    """Extract full category string from ComfyUI source (e.g. 'api node/image/ByteDance')."""
    for path in _comfyui_source_files():
        text = _read_comfyui_source(path)
        if node_name not in text and not any(v in text for v in _class_name_variants(node_name)):
            continue
        cat = _category_from_class_block(text, node_name, first_segment_only=False)
        if cat:
            return cat
        cat = _category_from_schema_node_id(text, node_name, first_segment_only=False)
        if cat:
            return cat
    return None


def _resolve_node_info_key(nodes: dict[str, dict], node_name: str) -> Optional[dict[str, Any]]:
    """Get node info from all_nodes_info by node_name, or by class variant, or by node_id."""
    if node_name in nodes:
        return nodes[node_name]
    for variant in _class_name_variants(node_name):
        if variant in nodes:
            return nodes[variant]
    for key, info in nodes.items():
        if info.get("node_id") == node_name:
            return info
    return None


@lru_cache(maxsize=None)
def scanner_node_key(node_name: str) -> Optional[str]:
    """Return the all_nodes_info.json dict key for this node, if known to the scanner."""
    nodes = _load_all_nodes_info()
    if node_name in nodes:
        return node_name
    for variant in _class_name_variants(node_name):
        if variant in nodes:
            return variant
    for key, info in nodes.items():
        if info.get("node_id") == node_name:
            return key
    lower = node_name.lower()
    for key in nodes:
        if key.lower() == lower:
            return key
    for key, info in nodes.items():
        class_name = (info.get("class_name") or "").strip()
        if class_name and class_name.lower() == lower:
            return key
    return None


def canonical_node_name(node_name: str) -> str:
    """Return scanner node key (ComfyUI class name); falls back to node_name if not in scanner."""
    return scanner_node_key(node_name) or node_name


def node_name_nav_aliases(node_name: str) -> set[str]:
    """All page-key basename variants that should collapse to the same scanner node."""
    canonical = canonical_node_name(node_name)
    aliases: set[str] = {node_name, canonical}
    for variant in _class_name_variants(node_name):
        aliases.add(variant)
    for variant in _class_name_variants(canonical):
        aliases.add(variant)
    lower = canonical.lower()
    for key in _load_all_nodes_info():
        if key.lower() == lower:
            aliases.add(key)
    return aliases


def _locale_code_for_page_key(page_key: str) -> str:
    """Infer locale code from a page key prefix (e.g. zh/built-in-nodes/X -> zh)."""
    for cfg in LOCALE_CONFIGS:
        if page_key.startswith(cfg["page_prefix"] + "/"):
            return cfg["code"]
    return "en"


@lru_cache(maxsize=None)
def _locale_mdx_names(builtin_dir: str) -> frozenset:
    """Cached set of published .mdx basenames (without extension) for a locale directory."""
    d = Path(builtin_dir)
    try:
        return frozenset(e[:-4] for e in os.listdir(d) if e.endswith(".mdx"))
    except OSError:
        return frozenset()


def published_node_name(node_name: str, locale_code: Optional[str] = None) -> str:
    """MDX filename and docs.json page basename — keep existing on-disk name when already published.

    macOS APFS is case-insensitive, so Path.is_file() cannot distinguish
    CLIPTextEncodeControlnet.mdx from ClipTextEncodeControlnet.mdx (same inode).
    Instead we match against the real on-disk directory entries (os.listdir names),
    which preserve the true casing/spelling committed to git. Historical spellings
    (e.g. HunyuanDit vs HunyuanDiT, Sdxl vs SDXL) are handled via casefold fallback.

    Per-locale: en/zh/ja on-disk files are uppercase CLIP..., ko is lowercase Clip...,
    so the published name must be resolved against each locale's own directory.
    """
    scanner = canonical_node_name(node_name)
    locales = [c for c in LOCALE_CONFIGS if locale_code is None or c["code"] == locale_code]
    aliases = sorted(node_name_nav_aliases(scanner), key=len, reverse=True)
    for locale in locales:
        d = locale["builtin_dir"]
        if not d.is_dir():
            continue
        mdx_names = set(_locale_mdx_names(str(d)))
        if not mdx_names:
            continue
        # 1) exact (case-sensitive) alias match against real on-disk names
        for alias in aliases:
            if alias in mdx_names:
                return alias
        # 2) casefold match: return the real on-disk spelling (covers DiT/Dit, SDXL/Sdxl, CLIP/Clip)
        folded = {n.casefold(): n for n in mdx_names}
        for alias in aliases:
            if alias.casefold() in folded:
                return folded[alias.casefold()]
    return scanner


def canonical_page_key(page_key: str) -> str:
    """Normalize a docs.json page key to the published on-disk MDX basename."""
    parts = page_key.split("/")
    if not parts:
        return page_key
    published = published_node_name(parts[-1], _locale_code_for_page_key(page_key))
    if parts[-1] == published:
        return page_key
    return "/".join([*parts[:-1], published])


def resolve_source_node(node_name: str) -> tuple[str, Path]:
    """Return (scanner canonical name, embedded-docs dir) for reading en.md / zh.md / ja.md.

    Checks the canonical name first, then the remaining nav aliases in deterministic
    sorted order (avoiding duplicate checks), then a case-insensitive fallback scan.
    """
    canonical = canonical_node_name(node_name)
    seen: set[str] = set()
    candidates: list[str] = []
    for candidate in sorted(node_name_nav_aliases(node_name)):
        if candidate in seen:
            continue
        seen.add(candidate)
        if candidate == canonical:
            candidates.insert(0, candidate)  # canonical first
        else:
            candidates.append(candidate)
    for candidate in candidates:
        node_dir = DOCS_SOURCE / candidate
        if (node_dir / "en.md").exists():
            return canonical, node_dir
    if DOCS_SOURCE.exists():
        lower = canonical.lower()
        for node_dir in sorted(DOCS_SOURCE.iterdir()):
            if node_dir.is_dir() and node_dir.name.lower() == lower and (node_dir / "en.md").exists():
                return canonical, node_dir
    return canonical, DOCS_SOURCE / canonical


def list_nodes_with_en_md() -> list[str]:
    """list embedded-docs nodes deduped by scanner canonical name."""
    seen: set[str] = set()
    nodes: list[str] = []
    for node_dir in sorted(DOCS_SOURCE.iterdir()):
        if not node_dir.is_dir() or not (node_dir / "en.md").exists():
            continue
        canonical = canonical_node_name(node_dir.name)
        if canonical in seen:
            continue
        seen.add(canonical)
        nodes.append(canonical)
    return nodes


def get_full_category_for_node(node_name: str) -> Optional[str]:
    """Get full category string for node: prefer scanner all_nodes_info.json (look up by name/variant/node_id), else extract from source."""
    nodes = _load_all_nodes_info()
    info = _resolve_node_info_key(nodes, node_name)
    if info and info.get("category"):
        raw = info["category"].strip()
        return raw if raw else None
    return extract_category_full_from_comfyui(node_name)


def get_category_for_node(node_name: str) -> Optional[str]:
    """Get category (first segment) for node: prefer scanner all_nodes_info.json, else extract from ComfyUI source."""
    full = get_full_category_for_node(node_name)
    if full:
        return full.split("/")[0]
    return extract_category_from_comfyui(node_name)


def extract_category_from_comfyui(node_name: str) -> Optional[str]:
    """Find node in ComfyUI source and extract CATEGORY/category for this node only. Returns first segment (e.g. sampling from sampling/custom_sampling)."""
    for path in _comfyui_source_files():
        text = _read_comfyui_source(path)
        if node_name not in text and not any(v in text for v in _class_name_variants(node_name)):
            continue
        # Prefer: category from the class block that defines this node
        cat = _category_from_class_block(text, node_name)
        if cat:
            return cat
        # Fallback: Schema with node_id (e.g. node_id="AddNoise" ... category="...")
        cat = _category_from_schema_node_id(text, node_name)
        if cat:
            return cat
    return None


def collect_page_keys(pages: list[Any]) -> set[str]:
    """Recursively collect all page string keys from a tab's pages."""
    out: set[str] = set()
    for item in pages:
        if isinstance(item, str):
            out.add(item)
        elif isinstance(item, dict):
            if "pages" in item:
                out |= collect_page_keys(item["pages"])
    return out


def find_group_in_pages(pages: list[Any], group_label: str) -> Optional[list[Any]]:
    """Find the top-level group with 'group' == group_label and return its 'pages' list."""
    for item in pages:
        if isinstance(item, dict) and item.get("group") == group_label and "pages" in item:
            return item["pages"]
    return None


def find_or_create_group_in_pages(pages: list[Any], group_label: str) -> list[Any]:
    """Find group with group_label in pages, or create it and append. Return that group's 'pages' list."""
    for item in pages:
        if isinstance(item, dict) and item.get("group") == group_label and "pages" in item:
            return item["pages"]
    new_group: dict[str, Any] = {"group": group_label, "pages": []}
    pages.append(new_group)
    return new_group["pages"]


def remove_page_from_pages(pages: list[Any], page_key: str) -> None:
    """Remove page_key from pages tree in place (recursive)."""
    i = 0
    while i < len(pages):
        item = pages[i]
        if isinstance(item, str):
            if item == page_key:
                pages.pop(i)
                continue
        elif isinstance(item, dict) and "pages" in item:
            remove_page_from_pages(item["pages"], page_key)
        i += 1


def _sort_pages_alphabetically(pages: list[Any], groups_first: bool = True) -> None:
    """Sort pages array in place: recursively sort nested 'pages', then sort this level.

    groups_first=True  → sub-groups before flat page strings (used inside category groups
                          so collapsible folders appear above the flat node list).
    groups_first=False → flat page strings before sub-groups (used at tab level so
                          standalone pages like 'overview' stay at the very top).
    Both labels are compared case-insensitively.
    """
    for item in pages:
        if isinstance(item, dict) and "pages" in item:
            # Inner levels always put sub-groups first
            _sort_pages_alphabetically(item["pages"], groups_first=True)
    if groups_first:
        # groups (0) before flat pages (1)
        pages.sort(key=lambda x: (0, x.get("group", "").lower()) if isinstance(x, dict) else (1, x.lower()))
    else:
        # flat pages (0) before groups (1) — keeps 'overview' at top of tab
        pages.sort(key=lambda x: (1, x.get("group", "").lower()) if isinstance(x, dict) else (0, x.lower()))


def _rebuild_wrapper_groups(
    wrapper_pages: list[Any],
    node_cat_map: dict[str, str],
    lang_idx: int = 0,
) -> None:
    """Completely rebuild all non-API groups inside wrapper_pages from scratch.

    Collects every page key (except those in API Node), then re-places each one
    using the first-segment rule that mirrors ComfyUI's node menu hierarchy.
    This corrects any historical mis-placements without requiring a full re-sync.

    lang_idx: 0 = EN, 1 = zh, 2 = ja, 3 = ko labels from CATEGORY_TO_GROUP.
    """
    # Preserve the API Node group as-is
    api_node_item: Optional[dict[str, Any]] = None
    for item in wrapper_pages:
        if isinstance(item, dict) and item.get("group") == "API Node":
            api_node_item = item
            break

    api_keys: set[str] = set(collect_page_keys(api_node_item["pages"])) if api_node_item else set()
    all_keys: set[str] = set(collect_page_keys(wrapper_pages))
    non_api_keys = {canonical_page_key(k) for k in (all_keys - api_keys)}

    # Build case-insensitive lookup for node_cat_map (handles ClipLoader → CLIPLoader mismatches)
    lower_cat_map: dict[str, str] = {k.lower(): v for k, v in node_cat_map.items()}
    # Build case-insensitive lookup for fallback map
    lower_fallback: dict[str, str] = {k.lower(): v for k, v in _FALLBACK_CATEGORY.items()}

    # Rebuild wrapper: clear everything, re-add API Node, then re-place all other keys
    wrapper_pages.clear()
    if api_node_item is not None:
        wrapper_pages.append(api_node_item)

    locale_code = LOCALE_CONFIGS[lang_idx]["code"] if 0 <= lang_idx < len(LOCALE_CONFIGS) else "en"
    for key in sorted(non_api_keys):
        key_parts = Path(key).parts  # e.g. ('built-in-nodes', 'conditioning', 'video-models', 'wan-vace-to-video')
        node_name = published_node_name(key_parts[-1], locale_code)
        if key_parts[-1] != node_name:
            key = "/".join([*key_parts[:-1], node_name])

        # If the page key has intermediate path segments (nested MDX), derive category from path
        # e.g. built-in-nodes/conditioning/video-models/foo → conditioning/video_models
        prefix_dirs = tuple(cfg["page_prefix"] for cfg in LOCALE_CONFIGS)
        path_derived_cat = ""
        for pfx in prefix_dirs:
            pfx_parts = Path(pfx).parts
            if key_parts[: len(pfx_parts)] == pfx_parts and len(key_parts) > len(pfx_parts) + 1:
                # Middle segments are the category
                mid = key_parts[len(pfx_parts) : -1]
                path_derived_cat = "/".join(mid).replace("-", "_")
                break

        # Step 1: get raw category from scanner (case-insensitive fallback included)
        scanner_cat = (
            node_cat_map.get(node_name)
            or lower_cat_map.get(node_name.lower())
            or ""
        ).strip()

        # Step 2: get explicit fallback (always takes priority over _for_testing scanner result)
        fallback_cat = (
            _FALLBACK_CATEGORY.get(node_name)
            or lower_fallback.get(node_name.lower())
            or ""
        ).strip()

        # Step 3: choose final category
        if path_derived_cat:
            # Nested MDX path (e.g. conditioning/video-models/...) — use path directly
            full_cat = path_derived_cat
        elif scanner_cat and not scanner_cat.startswith("_for_testing"):
            # Scanner returned a clean category — use it
            full_cat = scanner_cat
        elif fallback_cat:
            # Explicit fallback always wins over _for_testing scanner result
            full_cat = fallback_cat
        elif scanner_cat.startswith("_for_testing"):
            # Remap _for_testing/* to proper top-level paths
            rest = scanner_cat[len("_for_testing"):].lstrip("/")
            if not rest:
                full_cat = ""
            elif rest.startswith("custom_sampling"):
                full_cat = "sampling/" + rest
            elif rest.startswith("conditioning"):
                full_cat = rest
            elif rest.startswith("stable_cascade"):
                full_cat = "conditioning/" + rest
            else:
                full_cat = "advanced/" + rest
        else:
            full_cat = ""

        # Route nodes whose category starts with "api node" into the API Node group
        if full_cat.lower().startswith("api node"):
            if api_node_item is None:
                api_node_item = {"group": "API Node", "pages": []}
                wrapper_pages.insert(0, api_node_item)
            # Build sub-path inside API Node: segs after "api node"
            segs = [s.strip() for s in full_cat.split("/") if s.strip()][1:]
            target = api_node_item["pages"]
            for seg in segs:
                target = find_or_create_group_in_pages(target, _seg_to_label(seg))
            if key not in target:
                target.append(key)
            continue

        segs = [s.strip() for s in full_cat.split("/") if s.strip()]

        if not segs:
            group_label = _default_group_for_lang(lang_idx)
        else:
            group_label = _group_label_for_category(segs[0], lang_idx)

        target = find_or_create_group_in_pages(wrapper_pages, group_label)
        for seg in segs[1:]:
            target = find_or_create_group_in_pages(target, _seg_to_label(seg))
        if key not in target:
            target.append(key)


def _remove_empty_groups(pages: list[Any]) -> None:
    """Remove groups with empty 'pages' in place (recursive, bottom-up)."""
    i = 0
    while i < len(pages):
        item = pages[i]
        if isinstance(item, dict) and "pages" in item:
            _remove_empty_groups(item["pages"])
            if len(item["pages"]) == 0:
                pages.pop(i)
                continue
        i += 1


def _migrate_toplevel_groups_to_wrapper(pages: list[Any], wrapper_label: str) -> None:
    """Move any top-level dict groups (other than wrapper_label) inside the wrapper group.

    This ensures previously added top-level groups (3D, API Node, etc.) become nested
    inside the wrapper so Mintlify renders them as collapsible entries.
    """
    orphans: list[dict[str, Any]] = []
    i = 0
    while i < len(pages):
        item = pages[i]
        if isinstance(item, dict) and "pages" in item and item.get("group") != wrapper_label:
            orphans.append(item)
            pages.pop(i)
        else:
            i += 1
    if not orphans:
        return
    wrapper = find_or_create_group_in_pages(pages, wrapper_label)
    for orphan in orphans:
        existing = find_group_in_pages(wrapper, orphan["group"])
        if existing is not None:
            # Merge pages; avoid duplicates
            for p in orphan["pages"]:
                if p not in existing:
                    existing.append(p)
        else:
            wrapper.append(orphan)


def get_description_from_content(content: str) -> str:
    """Extract the first sentence from the first content paragraph.

    Used as the seed for the SEO meta description (see build_seo_description).
    Skips AI-generated disclaimer blockquote lines and headings.
    """
    lines = content.split("\n")
    first_para: list[str] = []
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            if first_para:
                break
            continue
        # H1 (# Title) is the page title — skip it and keep looking for the
        # first content paragraph. H2+ (## Section) ends the overview.
        if line_stripped.startswith("##"):
            break
        if line_stripped.startswith("#"):
            continue
        # Skip Markdown images and table rows — they are not prose
        if line_stripped.startswith("![") or line_stripped.startswith("|"):
            continue
        if line_stripped.startswith("> ") and (
            "AI-generated" in line_stripped
            or "AI 生成" in line_stripped
            or "AI によって生成" in line_stripped
            or "AI에 의해 생성" in line_stripped
        ):
            continue
        first_para.append(line_stripped)
    paragraph = " ".join(first_para) if first_para else ""
    # Return only the first sentence. For English, split on ". " only when the
    # next char is uppercase (avoids cutting "e.g." / "i.e." abbreviations);
    # CJK sentence ender "。" splits unconditionally.
    m = re.search(r"\.\s+(?=[A-Z])", paragraph)
    if m:
        return paragraph[: m.end()]
    idx = paragraph.find("。")
    if idx != -1:
        return paragraph[: idx + 1]
    # Align fallback truncation with the 180-char frontmatter limit
    return paragraph[:180] if paragraph else ""


def find_local_asset_refs(content: str, doc_dir: Path) -> list[tuple[str, Path]]:
    """Return list of (original_ref, resolved_absolute_path) for local assets."""
    refs: list[tuple[str, Path]] = []
    seen: set[str] = set()
    for m in MD_IMAGE_RE.finditer(content):
        href = m.group(1).strip()
        if not is_local_link(href):
            continue
        path = (doc_dir / href.split("#")[0].split("?")[0]).resolve()
        if path.exists() and path.is_file() and path not in [p for _, p in refs]:
            refs.append((href, path))
    for m in HTML_SRC_RE.finditer(content):
        href = m.group(1).strip()
        if not is_local_link(href):
            continue
        path = (doc_dir / href.split("#")[0].split("?")[0]).resolve()
        if path.exists() and path.is_file() and path not in [p for _, p in refs]:
            refs.append((href, path))
    return refs


def copy_assets_and_rewrite(
    content: str,
    doc_dir: Path,
    node_name: str,
    images_out_dir: Path,
    dry_run: bool,
) -> str:
    """Copy referenced assets to images_out_dir and rewrite refs to /images/built-in-nodes/NodeName/xxx.

    - Resolves basename collisions by prefixing the relative subdirectory when two
      distinct sources share a basename, so neither overwrites the other.
    - Rewrites only prose references: fenced code blocks are stashed first so their
      content stays byte-identical.
    """
    refs = find_local_asset_refs(content, doc_dir)
    # Stash fenced code blocks so refs inside them are never rewritten
    _stashed: list[str] = []

    def _stash_code_blocks(m: "re.Match[str]") -> str:
        _stashed.append(m.group(0))
        return f"\x00CODEBLOCK{len(_stashed) - 1}\x00"

    out = re.sub(r"```.*?```", _stash_code_blocks, content, flags=re.DOTALL)

    used_names: dict[str, Path] = {}
    for orig, abs_path in refs:
        filename = abs_path.name
        # Cross-directory relative refs (e.g. ../Load3D/asset/x.webp) resolve
        # outside doc_dir, where relative_to raises ValueError. Fall back to the
        # parent directory name so the collision prefix stays meaningful.
        try:
            rel = abs_path.relative_to(doc_dir)
        except ValueError:
            rel = Path(abs_path.parent.name) / filename
        # Deterministic destination name: include the source subdirectory on collision
        if filename in used_names and used_names[filename] != abs_path:
            stem, ext = filename.rsplit(".", 1) if "." in filename else (filename, "")
            base = f"{Path(rel).parent.name}_{stem}" if Path(rel).parent.name else stem
            candidate = f"{base}.{ext}" if ext else base
            n = 1
            while candidate in used_names:
                candidate = f"{base}_{n}.{ext}" if ext else f"{base}_{n}"
                n += 1
            filename = candidate
        used_names[filename] = abs_path
        new_ref = f"/images/built-in-nodes/{node_name}/{filename}"
        if not dry_run:
            images_out_dir.mkdir(parents=True, exist_ok=True)
            dest = images_out_dir / filename
            if abs_path != dest:
                shutil.copy2(abs_path, dest)
        # Replace in content (use orig as-is to avoid re-escaping)
        out = out.replace(orig, new_ref)

    # Restore stashed code blocks verbatim
    def _restore(m: "re.Match[str]") -> str:
        return _stashed[int(m.group(1))]

    out = re.sub(r"\x00CODEBLOCK(\d+)\x00", _restore, out)
    return out


def _escape_frontmatter_description(description: str) -> str:
    """Escape backslashes and double-quotes for YAML frontmatter (avoids parsing errors)."""
    return description.replace("\\", "\\\\").replace('"', '\\"')


def _normalize_mdx_content(content: str) -> str:
    """Apply MDX-safe normalizations: strip H1 title, self-closing tags, etc.

    Strips the leading H1 (# Title) line — the sidebar title in frontmatter
    already provides the heading, so a duplicate H1 is redundant on the page.
    """
    # Strip leading H1 (# Title) and any blank lines after it
    content = re.sub(r'^#\s+[^\n]*\n?\n*', '', content, count=1)

    # Protect fenced code blocks AND inline backtick spans from ALL escaping below:
    # inside ``` blocks (and `code`) the content must stay byte-identical
    # (CommonMark renders code verbatim, so &lt;= would show literally instead of <=).
    _code_blocks: list[str] = []
    def _stash_code(m: "re.Match[str]") -> str:
        _code_blocks.append(m.group(0))
        return f"\x00CODEBLOCK{len(_code_blocks) - 1}\x00"
    content = re.sub(r"```.*?```", _stash_code, content, flags=re.DOTALL)
    content = re.sub(r"`[^`\n]+`", _stash_code, content)

    content = content.replace("<br>", "<br />")
    content = re.sub(r"(<source\s+[^>]+)>", r"\1 />", content)
    content = re.sub(r"<(https?://[^>\s]+)>", r"[\1](\1)", content)
    # Escape comparison-style angle brackets like <1.0, <100, <= 3840 that are NOT HTML/JSX tags.
    # Must escape <= first, then <digit, then remaining bare <word (e.g. <br> already handled above).
    content = re.sub(r"<=", r"&lt;=", content)
    content = re.sub(r"<(\d)", r"&lt;\1", content)
    # Escape any remaining bare < that is not an HTML/JSX tag (e.g. "< 8,294,400").
    # Keep the original whitespace after the < (including newlines) intact.
    content = re.sub(r"<(\s)", r"&lt;\1", content)
    # Tags that appear BOTH as <Tag> and </Tag> are intentional paired components
    # (e.g. Mintlify's <Note>...</Note>, <Tip>, <Warning>) — keep them raw.
    # Only orphaned tags (opening without closing, or closing without opening) get escaped.
    _MDX_HTML_TAGS = ("br", "source", "img", "video", "audio", "a", "p", "div", "span", "table", "tr", "td", "th", "ul", "ol", "li", "code", "pre", "strong", "em", "b", "i")
    # Mintlify built-in components — must stay raw, otherwise the site renders
    # literal &lt;Note> text instead of the Note callout.
    _MINTLIFY_COMPONENTS = (
        "Accordion", "AccordionGroup", "Badge", "Card", "CardGroup", "CodeGroup",
        "FileTree", "Frame", "Icon", "Info", "Note", "Param", "RequestExample",
        "ResponseExample", "SettingsMenuContext", "Step", "Steps", "Tab", "Tabs",
        "Tip", "Update", "UpdateReminder", "Warning", "ReqHint",
    )
    _keep_raw = set(_MDX_HTML_TAGS)
    # Mintlify components stay raw ONLY when paired (opening + closing both present).
    # Orphaned </Note> (e.g. from an older escaped <Note>) must still be escaped,
    # otherwise MDX acorn fails with "Unexpected closing slash".
    # Unknown tags (e.g. <bbox> API syntax examples) are NEVER kept raw.
    _open_tags = set(re.findall(r"<([a-zA-Z_][a-zA-Z0-9]*)(?:\s|>)", content))
    _close_tags = set(re.findall(r"</([a-zA-Z_][a-zA-Z0-9]*)\s*>", content))
    _keep_raw |= set(_MINTLIFY_COMPONENTS) & _open_tags & _close_tags
    # Escape closing tags </Note> -> &lt;/Note> when not kept raw (orphaned closing tag).
    # Must run BEFORE the opening-tag rule so pairs stay consistent.
    content = re.sub(
        r"</([a-zA-Z_][a-zA-Z0-9]*)\s*>",
        lambda m: m.group(0) if m.group(1) in _keep_raw else "&lt;/" + m.group(1) + ">",
        content,
    )
    content = re.sub(r"<([a-zA-Z_][a-zA-Z0-9]*)", lambda m: m.group(0) if m.group(1) in _keep_raw else "&lt;" + m.group(1), content)

    # Escape literal curly braces in prose (MDX treats { as a JSX expression
    # boundary). Code blocks and inline code are already stashed, so they are
    # unaffected.
    content = content.replace("{", "&#123;").replace("}", "&#125;")

    # Restore code blocks verbatim
    def _restore_code(m: "re.Match[str]") -> str:
        return _code_blocks[int(m.group(1))]
    content = re.sub(r"\x00CODEBLOCK(\d+)\x00", _restore_code, content)
    return content


def build_frontmatter(node_name: str, description: str) -> str:
    """Frontmatter with a concrete, node-specific SEO description.

    `description` is the first sentence extracted from the node's en.md
    overview (see get_description_from_content). Using it instead of a
    templated string gives every node page a real, searchable summary —
    the GEO improvement that previously could only be done by hand-editing
    individual .mdx files (e.g. Comfy-Org/docs#1216).
    """
    seo_desc = (description or "").strip()
    if not seo_desc:
        seo_desc = f"Complete documentation for the {node_name} node in ComfyUI. Learn its inputs, outputs, parameters and usage."
    # Keep meta descriptions reasonably short; strip markdown/backticks noise
    seo_desc = re.sub(r"[`*_#>]", "", seo_desc)
    seo_desc = seo_desc[:180]
    seo_desc_escaped = _escape_frontmatter_description(seo_desc)
    return f"""---
title: "{node_name} - ComfyUI Built-in Node Documentation"
description: "{seo_desc_escaped}"
sidebarTitle: "{node_name}"
icon: "circle"
mode: wide
---

"""


def _normalize_category(raw: Optional[str]) -> str:
    raw = (raw or "").strip()
    raw_lower = raw.lower()
    if raw_lower.startswith("partner node"):
        raw = "api node" + raw[len("partner node"):]
    return raw


def _purge_noncanonical_nav_pages(tab_pages: list[Any]) -> None:
    """Replace noncanonical docs.json page keys with the published on-disk spelling.

    When a key's basename differs from the published name (e.g. ClipLoader vs
    CLIPLoader.mdx on disk), replace it in place at the same position with the
    canonical key rather than silently removing it. Keys whose locale has no
    matching .mdx file are left unchanged so no navigation entry is lost.
    """
    for key in sorted(collect_page_keys(tab_pages)):
        parts = key.split("/")
        if not parts:
            continue
        locale_code = _locale_code_for_page_key(key)
        published = published_node_name(parts[-1], locale_code)
        if parts[-1] == published:
            continue
        # Only rewrite when a real .mdx file exists for this locale
        locale = next((c for c in LOCALE_CONFIGS if c["code"] == locale_code), None)
        if locale is None:
            continue
        target_mdx = locale["builtin_dir"] / f"{published}.mdx"
        if not target_mdx.exists():
            continue
        # Locate the containing pages list BEFORE removing the key, then
        # re-insert the canonical spelling at the same logical position.
        target_pages = _find_tab_pages_for_key(tab_pages, key)
        remove_page_from_pages(tab_pages, key)
        canonical_key = "/".join([*parts[:-1], published])
        if target_pages is not None and canonical_key not in target_pages:
            target_pages.append(canonical_key)


def _find_tab_pages_for_key(pages: list[Any], page_key: str) -> Optional[list[Any]]:
    """Return the innermost 'pages' list containing page_key (recursive), or None."""
    for item in pages:
        if isinstance(item, str):
            if item == page_key:
                return pages
        elif isinstance(item, dict) and "pages" in item:
            if page_key in collect_page_keys(item["pages"]):
                found = _find_tab_pages_for_key(item["pages"], page_key)
                if found is not None:
                    return found
    return None


def _place_page_in_nav(
    tab_pages: list[Any],
    page_key: str,
    full_category: str,
    locale: dict[str, Any],
) -> None:
    """Insert page_key under the correct Built-in Nodes group for one locale."""
    page_key = canonical_page_key(page_key)
    raw = _normalize_category(full_category)
    raw_lower = raw.lower()
    lang_idx = locale["lang_idx"]
    wrapper = find_or_create_group_in_pages(tab_pages, locale["wrapper"])

    if raw_lower.startswith("api node"):
        parts = [p.strip() for p in raw.split("/") if p.strip()]
        type_label = _seg_to_label(parts[1]) if len(parts) >= 2 else "Other"
        provider_label = _seg_to_label(parts[2]) if len(parts) >= 3 else None
        api_pages = find_or_create_group_in_pages(wrapper, "API Node")
        if type_label:
            type_pages = find_or_create_group_in_pages(api_pages, type_label)
            if provider_label:
                provider_pages = find_or_create_group_in_pages(type_pages, provider_label)
                if page_key not in provider_pages:
                    provider_pages.append(page_key)
            elif page_key not in type_pages:
                type_pages.append(page_key)
        elif page_key not in api_pages:
            api_pages.append(page_key)
        return

    group_label, sub_label = _category_to_group_and_sub(raw, lang_idx)
    gp = find_or_create_group_in_pages(wrapper, group_label)
    if sub_label:
        sub_gp = find_or_create_group_in_pages(gp, sub_label)
        if page_key not in sub_gp:
            sub_gp.append(page_key)
    elif page_key not in gp:
        gp.append(page_key)


def sync_node(
    node_name: str,
    dry_run: bool,
) -> tuple[bool, Optional[str], list[str]]:
    """Sync one node: en.md (+ zh.md / ja.md when present) -> MDX and copy assets."""
    scanner_name, node_dir = resolve_source_node(node_name)
    en_md = node_dir / "en.md"
    if not en_md.exists():
        print(f"  Skip {node_name}: no en.md")
        return False, None, []

    published_en = published_node_name(scanner_name, "en")
    images_out = IMAGES_TARGET / published_en
    content_en = en_md.read_text(encoding="utf-8")
    description_en = get_description_from_content(content_en)
    synced_locales: list[str] = []

    for locale in LOCALE_CONFIGS:
        md_path = node_dir / locale["md_file"]
        if locale["code"] != "en" and not md_path.exists():
            continue

        # Per-locale published name: en/zh/ja on-disk files are uppercase CLIP...,
        # ko is lowercase Clip... — resolve against this locale's own directory.
        published = published_en if locale["code"] == "en" else published_node_name(scanner_name, locale["code"])

        content = md_path.read_text(encoding="utf-8")
        content = copy_assets_and_rewrite(content, node_dir, published_en, images_out, dry_run)
        content = _normalize_mdx_content(content)
        # Description: prefer the localized overview first sentence, fall back to English.
        locale_desc = get_description_from_content(content)
        if not locale_desc:
            locale_desc = description_en
        mdx = build_frontmatter(scanner_name, locale_desc or f"Documentation for {scanner_name} node.") + content

        target_mdx = locale["builtin_dir"] / f"{published}.mdx"
        if not dry_run:
            locale["builtin_dir"].mkdir(parents=True, exist_ok=True)
            target_mdx.write_text(mdx, encoding="utf-8")
        print(f"  {locale['code'].upper()}: {locale['page_prefix']}/{published}.mdx")
        synced_locales.append(locale["code"])

    full_category = get_full_category_for_node(scanner_name) if not dry_run else None
    return True, full_category, synced_locales


def main():
    parser = argparse.ArgumentParser(description="Sync embedded-docs to comfy/docs (built-in-nodes + docs.json)")
    parser.add_argument("--node", type=str, help="Sync only this node")
    parser.add_argument("--mode", choices=("all", "test"), default="test", help="all = every node with en.md; test = first N")
    parser.add_argument("--count", type=int, default=10, help="N for test mode")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files")
    parser.add_argument("--no-docs-json", action="store_true", help="Do not update docs.json")
    args = parser.parse_args()

    if not DOCS_SOURCE.exists():
        print(f"ERROR: DOCS_SOURCE not found: {DOCS_SOURCE}")
        sys.exit(1)
    if not TARGET_DOCS.exists() and not args.dry_run:
        print(f"ERROR: TARGET_DOCS not found: {TARGET_DOCS}")
        sys.exit(1)

    if args.count < 0:
        print("ERROR: --count must be >= 0")
        sys.exit(1)

    if args.node:
        _canonical, _src = resolve_source_node(args.node)
        if not (_src / "en.md").exists():
            print(f"ERROR: node '{args.node}' does not resolve to a directory containing en.md: {_src}")
            sys.exit(1)
        nodes = [_canonical]
    else:
        nodes = list_nodes_with_en_md()
        if args.mode == "test":
            nodes = nodes[: args.count]

    update_docs_json = not args.no_docs_json and not args.dry_run
    print(f"Syncing {len(nodes)} nodes to {TARGET_DOCS} (dry_run={args.dry_run}, update_docs_json={update_docs_json})")
    if update_docs_json:
        print(f"  docs.json path: {DOCS_JSON}")
        if not DOCS_JSON.exists():
            print("  WARNING: docs.json not found at above path; navigation will not be updated.")
    synced: list[tuple[str, Optional[str], list[str]]] = []
    for node_name in nodes:
        ok, category, synced_locales = sync_node(node_name, args.dry_run)
        if ok:
            synced.append((node_name, category, synced_locales))

    if synced and not args.dry_run and not args.no_docs_json:
        if not DOCS_JSON.exists():
            print("docs.json: skipped (file not found).")
        else:
            with open(DOCS_JSON, "r", encoding="utf-8") as f:
                nav = json.load(f)
            added: dict[str, list[str]] = {cfg["code"]: [] for cfg in LOCALE_CONFIGS}
            for node_name, full_category, synced_locales in synced:
                scanner_name = canonical_node_name(node_name)
                for locale in LOCALE_CONFIGS:
                    if locale["code"] not in synced_locales:
                        continue
                    published = published_node_name(scanner_name, locale["code"])
                    page_key = f"{locale['page_prefix']}/{published}"
                    lang_entry = _find_lang_entry(nav, locale["code"])
                    if lang_entry is None:
                        continue
                    tab_pages = _find_tab_pages(lang_entry, locale["tab"])
                    if tab_pages is None:
                        continue
                    for alias in node_name_nav_aliases(scanner_name):
                        remove_page_from_pages(tab_pages, f"{locale['page_prefix']}/{alias}")
                    _place_page_in_nav(tab_pages, page_key, full_category or "", locale)
                    added[locale["code"]].append(page_key)

            for locale in LOCALE_CONFIGS:
                lang_entry = _find_lang_entry(nav, locale["code"])
                if lang_entry is None:
                    continue
                tab_pages = _find_tab_pages(lang_entry, locale["tab"])
                if tab_pages is not None:
                    _purge_noncanonical_nav_pages(tab_pages)
                    _migrate_toplevel_groups_to_wrapper(tab_pages, locale["wrapper"])

            node_cat_map: dict[str, str] = {
                name: info.get("category", "")
                for name, info in _load_all_nodes_info().items()
            }
            for locale in LOCALE_CONFIGS:
                lang_entry = _find_lang_entry(nav, locale["code"])
                if lang_entry is None:
                    continue
                tab_pages = _find_tab_pages(lang_entry, locale["tab"])
                if tab_pages is None:
                    continue
                wrapper = find_group_in_pages(tab_pages, locale["wrapper"])
                if wrapper is not None:
                    _rebuild_wrapper_groups(wrapper, node_cat_map, lang_idx=locale["lang_idx"])

            for locale in LOCALE_CONFIGS:
                lang_entry = _find_lang_entry(nav, locale["code"])
                if lang_entry is None:
                    continue
                tab_pages = _find_tab_pages(lang_entry, locale["tab"])
                if tab_pages is None:
                    continue
                _purge_noncanonical_nav_pages(tab_pages)
                _remove_empty_groups(tab_pages)
                _sort_pages_alphabetically(tab_pages, groups_first=False)

            # Atomic write: serialize to a temp file in the same directory, then
            # os.replace so a failed serialization never leaves docs.json truncated.
            had_trailing_newline = False
            try:
                with open(DOCS_JSON, "r", encoding="utf-8") as f:
                    had_trailing_newline = f.read().endswith("\n")
            except Exception:
                had_trailing_newline = True
            tmp_path = DOCS_JSON.with_suffix(".json.tmp")
            try:
                with open(tmp_path, "w", encoding="utf-8") as f:
                    json.dump(nav, f, indent=2, ensure_ascii=False)
                    if had_trailing_newline:
                        f.write("\n")
                os.replace(tmp_path, DOCS_JSON)
            finally:
                if tmp_path.exists():
                    tmp_path.unlink()
            any_added = any(added[code] for code in added)
            if any_added:
                print(f"docs.json: updated {DOCS_JSON}")
                for locale in LOCALE_CONFIGS:
                    for key in added[locale["code"]]:
                        print(f"  + {locale['code'].upper()}:  {key}")
            else:
                print("docs.json: no new entries (all synced nodes already in nav).")

    print("Done.")


if __name__ == "__main__":
    main()
