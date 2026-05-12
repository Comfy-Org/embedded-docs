#!/usr/bin/env python3
"""
Sync embedded-docs (en.md / zh.md + assets) to comfy/docs as NodeName.mdx.
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
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

try:
    from dotenv import load_dotenv
    _has_dotenv = True
except ImportError:
    _has_dotenv = False

DOC_AUTOMATION_PATH = Path(__file__).parent
ALL_NODES_INFO_PATH = DOC_AUTOMATION_PATH / "all_nodes_info.json"
if _has_dotenv:
    load_dotenv(DOC_AUTOMATION_PATH.parent / ".env")

# Cache: node_name -> category (first segment). Loaded from scanner output if available.
_nodes_info_cache: Optional[Dict[str, Dict[str, Any]]] = None


def _load_all_nodes_info() -> Dict[str, Dict[str, Any]]:
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

EMBEDDED_DOCS_PATH = Path(os.getenv("EMBEDDED_DOCS_PATH", str(DOC_AUTOMATION_PATH.parent)))
COMFYUI_PATH = Path(os.getenv("COMFYUI_PATH", "/Users/linmoumou/Documents/local_env/ComfyUI"))
TARGET_DOCS = Path(os.getenv("TARGET_DOCS", "/Users/linmoumou/Documents/comfy/docs"))

DOCS_SOURCE = EMBEDDED_DOCS_PATH / "comfyui_embedded_docs" / "docs"
BUILTIN_EN = TARGET_DOCS / "built-in-nodes"
BUILTIN_ZH = TARGET_DOCS / "zh-CN" / "built-in-nodes"
IMAGES_TARGET = TARGET_DOCS / "images" / "built-in-nodes"
DOCS_JSON = TARGET_DOCS / "docs.json"

SCAN_PATHS = [
    COMFYUI_PATH / "nodes.py",
    COMFYUI_PATH / "comfy_extras",
    COMFYUI_PATH / "comfy_api_nodes",
]

# ComfyUI category (first segment) -> (EN group label, zh-CN group label) for docs.json
# If a category is not in this map, a new group is created with the category name (EN); zh-CN uses EN label when no translation.
CATEGORY_TO_GROUP = {
    "conditioning": ("Conditioning", "条件"),
    "loaders": ("Loader", "加载器"),
    "image": ("Image", "图像"),
    "latent": ("Latent", "潜变量"),
    "sampling": ("Sampling", "采样"),
    "3d": ("3D", "3D"),
    "3D": ("3D", "3D"),
    "advanced": ("Advanced", "高级"),
    "utils": ("Utils", "实用工具"),
    "utility": ("Utils", "实用工具"),
    "util": ("Utils", "实用工具"),
    "_for_testing": ("Advanced", "高级"),
    "api": ("API", "API"),
    "api node": ("API Node", "API Node"),
    "model_patches": ("Model Patches", "模型补丁"),
    "dataset": ("Image", "图像"),
    "audio": ("Audio", "Audio"),
    "basics": ("Basics", "Basics"),
    "camera": ("Camera", "Camera"),
    "context": ("Context", "Context"),
    "image generation": ("Image", "图像"),
    "image tools": ("Image", "图像"),
    "logic": ("Logic", "Logic"),
    "mask": ("Mask", "Mask"),
    "textgen": ("Textgen", "Textgen"),
    "training": ("Training", "Training"),
    "transform": ("Transform", "Transform"),
    "guidance": ("Sampling", "采样"),
}
DEFAULT_GROUP_EN = "Advanced"
DEFAULT_GROUP_ZH = "高级"

# Wrapper group inside Built-in Nodes tab — all category groups are nested here so they become collapsible
BUILTIN_WRAPPER_EN = "Nodes"
BUILTIN_WRAPPER_ZH = "节点"

# Hardcoded category fallback for nodes that the scanner cannot resolve:
# - replacement nodes in nodes_replacements.py (no category field)
# - deprecated / aliased nodes not found in current source
# - partner API nodes with flat MDX files but no scanner entry
_FALLBACK_CATEGORY: Dict[str, str] = {
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

# Reverse map: group label (EN or ZH) -> ComfyUI category root string
# Used by _restructure_group_by_category to look up which category root each group corresponds to.
_GROUP_LABEL_TO_CATEGORY_ROOT: Dict[str, str] = {}
def _build_reverse_map() -> None:
    seen_en: Dict[str, str] = {}
    seen_zh: Dict[str, str] = {}
    for cat_key, (en_label, zh_label) in CATEGORY_TO_GROUP.items():
        # Prefer the exact key that produced this label (first one wins)
        if en_label not in seen_en:
            seen_en[en_label] = cat_key
        if zh_label not in seen_zh:
            seen_zh[zh_label] = cat_key
    _GROUP_LABEL_TO_CATEGORY_ROOT.update(seen_en)
    _GROUP_LABEL_TO_CATEGORY_ROOT.update(seen_zh)
_build_reverse_map()


def _seg_to_label(seg: str) -> str:
    """Convert a path segment like 'custom_sampling' to a display label 'Custom Sampling'."""
    return seg.replace("_", " ").replace("-", " ").title()


def _category_to_group_and_sub(full_category_path: str) -> Tuple[str, str, Optional[str], Optional[str]]:
    """Return (EN group, ZH group, EN sub-group or None, ZH sub-group or None).

    Always uses the FIRST segment to determine the top-level group so that the
    hierarchy mirrors ComfyUI's node menu exactly.

    Examples:
      'conditioning'               -> ('Conditioning', '条件', None, None)
      'conditioning/controlnet'    -> ('Conditioning', '条件', 'Controlnet', 'Controlnet')
      'advanced'                   -> ('Advanced', '高级', None, None)
      'advanced/conditioning'      -> ('Advanced', '高级', 'Conditioning', 'Conditioning')
      'advanced/loaders'           -> ('Advanced', '高级', 'Loaders', 'Loaders')
      'loaders'                    -> ('Loader', '加载器', None, None)
      'loaders/video_models'       -> ('Loader', '加载器', 'Video Models', 'Video Models')
      'sampling/custom_sampling'   -> ('Sampling', '采样', 'Custom Sampling', 'Custom Sampling')
      'model_patches'              -> ('Sampling', '采样', None, None)
    """
    if not full_category_path or not full_category_path.strip():
        return DEFAULT_GROUP_EN, DEFAULT_GROUP_ZH, None, None
    raw = full_category_path.strip()
    segments = [s.strip() for s in raw.split("/") if s.strip()]
    if not segments:
        return DEFAULT_GROUP_EN, DEFAULT_GROUP_ZH, None, None
    first_lower = segments[0].lower()
    if first_lower in CATEGORY_TO_GROUP:
        en_label, zh_label = CATEGORY_TO_GROUP[first_lower]
    else:
        en_label = _seg_to_label(segments[0])
        zh_label = en_label
    if len(segments) > 1:
        sub_label = _seg_to_label(segments[1])
        return en_label, zh_label, sub_label, sub_label
    return en_label, zh_label, None, None

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


def _class_name_variants(node_name: str) -> List[str]:
    """Return possible class names in source (e.g. ClipTextEncode -> [ClipTextEncode, CLIPTextEncode])."""
    variants = [node_name]
    if node_name.startswith("Clip") and len(node_name) > 4:
        variants.append("CLIP" + node_name[4:])
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


def extract_category_full_from_comfyui(node_name: str) -> Optional[str]:
    """Extract full category string from ComfyUI source (e.g. 'api node/image/ByteDance')."""
    for base in SCAN_PATHS:
        if not base.exists():
            continue
        files = [base] if base.is_file() else list(base.rglob("*.py"))
        for path in files:
            if path.suffix != ".py":
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if node_name not in text and not any(v in text for v in _class_name_variants(node_name)):
                continue
            cat = _category_from_class_block(text, node_name, first_segment_only=False)
            if cat:
                return cat
            cat = _category_from_schema_node_id(text, node_name, first_segment_only=False)
            if cat:
                return cat
    return None


def _resolve_node_info_key(nodes: Dict[str, Dict], node_name: str) -> Optional[Dict[str, Any]]:
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
    for base in SCAN_PATHS:
        if not base.exists():
            continue
        files = [base] if base.is_file() else list(base.rglob("*.py"))
        for path in files:
            if path.suffix != ".py":
                continue
            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
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


def collect_page_keys(pages: List[Any], prefix: str = "") -> Set[str]:
    """Recursively collect all page string keys from a tab's pages."""
    out: Set[str] = set()
    for item in pages:
        if isinstance(item, str):
            out.add(item)
        elif isinstance(item, dict):
            if "pages" in item:
                out |= collect_page_keys(item["pages"], prefix)
    return out


def flatten_builtin_pages(pages: List[Any], key_prefix: str) -> List[str]:
    """
    Recursively collect built-in-nodes page keys (e.g. built-in-nodes/NodeName or zh-CN/built-in-nodes/NodeName)
    and return a sorted flat list. Used for flat/collapsed sidebar (no groups).
    """
    keys: Set[str] = set()
    for item in pages:
        if isinstance(item, str) and (item == key_prefix or item.startswith(key_prefix + "/")):
            keys.add(item)
        elif isinstance(item, dict) and "pages" in item:
            keys |= set(flatten_builtin_pages(item["pages"], key_prefix))
    return sorted(keys)


def find_group_in_pages(pages: List[Any], group_label: str) -> Optional[List[Any]]:
    """Find the top-level group with 'group' == group_label and return its 'pages' list."""
    for item in pages:
        if isinstance(item, dict) and item.get("group") == group_label and "pages" in item:
            return item["pages"]
    return None


def find_or_create_group_in_pages(pages: List[Any], group_label: str) -> List[Any]:
    """Find group with group_label in pages, or create it and append. Return that group's 'pages' list."""
    for item in pages:
        if isinstance(item, dict) and item.get("group") == group_label and "pages" in item:
            return item["pages"]
    new_group: Dict[str, Any] = {"group": group_label, "pages": []}
    pages.append(new_group)
    return new_group["pages"]


def remove_page_from_pages(pages: List[Any], page_key: str) -> None:
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


def _remove_group_from_pages(pages: List[Any], group_label: str) -> None:
    """Remove the first top-level group with given label from pages (in place)."""
    for i, item in enumerate(pages):
        if isinstance(item, dict) and item.get("group") == group_label:
            pages.pop(i)
            return


def _sort_pages_alphabetically(pages: List[Any], groups_first: bool = True) -> None:
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
    wrapper_pages: List[Any],
    node_cat_map: Dict[str, str],
    lang_idx: int = 0,
) -> None:
    """Completely rebuild all non-API groups inside wrapper_pages from scratch.

    Collects every page key (except those in API Node), then re-places each one
    using the first-segment rule that mirrors ComfyUI's node menu hierarchy.
    This corrects any historical mis-placements without requiring a full re-sync.

    lang_idx: 0 = use EN labels from CATEGORY_TO_GROUP, 1 = use ZH labels.
    """
    # Preserve the API Node group as-is
    api_node_item: Optional[Dict[str, Any]] = None
    for item in wrapper_pages:
        if isinstance(item, dict) and item.get("group") == "API Node":
            api_node_item = item
            break

    api_keys: Set[str] = set(collect_page_keys(api_node_item["pages"])) if api_node_item else set()
    all_keys: Set[str] = set(collect_page_keys(wrapper_pages))
    non_api_keys = all_keys - api_keys

    # Build case-insensitive lookup for node_cat_map (handles ClipLoader → CLIPLoader mismatches)
    lower_cat_map: Dict[str, str] = {k.lower(): v for k, v in node_cat_map.items()}
    # Build case-insensitive lookup for fallback map
    lower_fallback: Dict[str, str] = {k.lower(): v for k, v in _FALLBACK_CATEGORY.items()}

    # Rebuild wrapper: clear everything, re-add API Node, then re-place all other keys
    wrapper_pages.clear()
    if api_node_item is not None:
        wrapper_pages.append(api_node_item)

    for key in sorted(non_api_keys):
        key_parts = Path(key).parts  # e.g. ('built-in-nodes', 'conditioning', 'video-models', 'wan-vace-to-video')
        node_name = key_parts[-1]

        # If the page key has intermediate path segments (nested MDX), derive category from path
        # e.g. built-in-nodes/conditioning/video-models/foo → conditioning/video_models
        prefix_dirs = ("built-in-nodes", "zh-CN/built-in-nodes")
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
            group_label = DEFAULT_GROUP_EN if lang_idx == 0 else DEFAULT_GROUP_ZH
        else:
            first_lower = segs[0].lower()
            if first_lower in CATEGORY_TO_GROUP:
                group_label = CATEGORY_TO_GROUP[first_lower][lang_idx]
            else:
                group_label = _seg_to_label(segs[0])

        target = find_or_create_group_in_pages(wrapper_pages, group_label)
        for seg in segs[1:]:
            target = find_or_create_group_in_pages(target, _seg_to_label(seg))
        if key not in target:
            target.append(key)


def _remove_empty_groups(pages: List[Any]) -> None:
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


def _migrate_toplevel_groups_to_wrapper(pages: List[Any], wrapper_label: str) -> None:
    """Move any top-level dict groups (other than wrapper_label) inside the wrapper group.

    This ensures previously added top-level groups (3D, API Node, etc.) become nested
    inside the wrapper so Mintlify renders them as collapsible entries.
    """
    orphans: List[Dict[str, Any]] = []
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
    first_para: List[str] = []
    for line in lines:
        line_stripped = line.strip()
        if not line_stripped:
            if first_para:
                break
            continue
        if line_stripped.startswith("##") or line_stripped.startswith("#"):
            break
        if line_stripped.startswith("> ") and ("AI-generated" in line_stripped or "AI 生成" in line_stripped):
            continue
        first_para.append(line_stripped)
    paragraph = " ".join(first_para) if first_para else ""
    # Return only the first sentence (up to first ". " or end of paragraph)
    for sep in (". ", "。"):
        idx = paragraph.find(sep)
        if idx != -1:
            return paragraph[: idx + 1]
    return paragraph[:160] if paragraph else ""


def find_local_asset_refs(content: str, doc_dir: Path) -> List[Tuple[str, Path]]:
    """Return list of (original_ref, resolved_absolute_path) for local assets."""
    refs: List[Tuple[str, Path]] = []
    seen: Set[str] = set()
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
    """Copy referenced assets to images_out_dir and rewrite refs to /images/built-in-nodes/NodeName/xxx."""
    refs = find_local_asset_refs(content, doc_dir)
    out = content
    for orig, abs_path in refs:
        filename = abs_path.name
        new_ref = f"/images/built-in-nodes/{node_name}/{filename}"
        if not dry_run:
            images_out_dir.mkdir(parents=True, exist_ok=True)
            dest = images_out_dir / filename
            if abs_path != dest:
                shutil.copy2(abs_path, dest)
        # Replace in content (use orig as-is to avoid re-escaping)
        out = out.replace(orig, new_ref)
    return out


def _escape_frontmatter_description(description: str) -> str:
    """Escape backslashes and double-quotes for YAML frontmatter (avoids parsing errors)."""
    return description.replace("\\", "\\\\").replace('"', '\\"')


def _normalize_mdx_content(content: str) -> str:
    """Apply MDX-safe normalizations: self-closing tags, angle-bracket URLs -> markdown links.

    Also escapes bare `<digit` sequences (e.g. <1.0) which MDX would try to parse as
    JSX tag names (invalid since tag names cannot start with a digit).
    """
    content = content.replace("<br>", "<br />")
    content = re.sub(r"(<source\s+[^>]+)>", r"\1 />", content)
    content = re.sub(r"<(https?://[^>\s]+)>", r"[\1](\1)", content)
    # Escape comparison-style angle brackets like <1.0 or <100 that are NOT HTML/JSX tags
    content = re.sub(r"<(\d)", r"&lt;\1", content)
    return content


def build_frontmatter(node_name: str, description: str) -> str:
    # Pure template description — avoids duplicating any content visible on the page
    seo_desc = f"Complete documentation for the {node_name} node in ComfyUI. Learn its inputs, outputs, parameters and usage."
    seo_desc_escaped = _escape_frontmatter_description(seo_desc)
    return f"""---
title: "{node_name} - ComfyUI Built-in Node Documentation"
description: "{seo_desc_escaped}"
sidebarTitle: "{node_name}"
icon: "circle"
mode: wide
---
"""


def sync_node(
    node_name: str,
    dry_run: bool,
) -> Tuple[bool, Optional[str]]:
    """Sync one node: en.md (+ zh.md) -> MDX, copy assets, optionally update docs.json."""
    node_dir = DOCS_SOURCE / node_name
    en_md = node_dir / "en.md"
    if not en_md.exists():
        print(f"  Skip {node_name}: no en.md")
        return False, None

    target_mdx_en = BUILTIN_EN / f"{node_name}.mdx"
    target_mdx_zh = BUILTIN_ZH / f"{node_name}.mdx"
    images_out = IMAGES_TARGET / node_name

    content_en = en_md.read_text(encoding="utf-8")
    description = get_description_from_content(content_en)
    content_en = copy_assets_and_rewrite(content_en, node_dir, node_name, images_out, dry_run)
    content_en = _normalize_mdx_content(content_en)
    mdx_en = build_frontmatter(node_name, description or f"Documentation for {node_name} node.") + content_en

    if not dry_run:
        BUILTIN_EN.mkdir(parents=True, exist_ok=True)
        target_mdx_en.write_text(mdx_en, encoding="utf-8")
    print(f"  EN: {node_name}.mdx")

    zh_md = node_dir / "zh.md"
    if zh_md.exists():
        content_zh = zh_md.read_text(encoding="utf-8")
        content_zh = copy_assets_and_rewrite(content_zh, node_dir, node_name, images_out, dry_run)
        content_zh = _normalize_mdx_content(content_zh)
        # Use same description for zh-CN frontmatter (or could extract from zh first para)
        mdx_zh = build_frontmatter(node_name, description or f"Documentation for {node_name} node.") + content_zh
        if not dry_run:
            BUILTIN_ZH.mkdir(parents=True, exist_ok=True)
            target_mdx_zh.write_text(mdx_zh, encoding="utf-8")
        print(f"  ZH: zh-CN/built-in-nodes/{node_name}.mdx")

    full_category = get_full_category_for_node(node_name) if not dry_run else None
    return True, full_category


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

    if args.node:
        nodes = [args.node] if (DOCS_SOURCE / args.node / "en.md").exists() else []
    else:
        nodes = sorted(
            d.name for d in DOCS_SOURCE.iterdir()
            if d.is_dir() and (d / "en.md").exists()
        )
        if args.mode == "test":
            nodes = nodes[: args.count]

    update_docs_json = not args.no_docs_json and not args.dry_run
    print(f"Syncing {len(nodes)} nodes to {TARGET_DOCS} (dry_run={args.dry_run}, update_docs_json={update_docs_json})")
    if update_docs_json:
        print(f"  docs.json path: {DOCS_JSON}")
        if not DOCS_JSON.exists():
            print(f"  WARNING: docs.json not found at above path; navigation will not be updated.")
    synced: List[Tuple[str, Optional[str]]] = []
    for node_name in nodes:
        ok, category = sync_node(node_name, args.dry_run)
        if ok:
            synced.append((node_name, category))

    if synced and not args.dry_run and not args.no_docs_json:
        if not DOCS_JSON.exists():
            print("docs.json: skipped (file not found).")
        else:
            with open(DOCS_JSON, "r", encoding="utf-8") as f:
                nav = json.load(f)
            added_en: List[str] = []
            added_zh: List[str] = []
            api_node_top_en = "API Node"
            api_node_top_zh = "API Node"
            for node_name, full_category in synced:
                en_key = f"built-in-nodes/{node_name}"
                zh_key = f"zh-CN/built-in-nodes/{node_name}"
                # Remove from current place so we can re-add under correct group
                for tab in nav["navigation"]["languages"][0]["tabs"]:
                    if tab.get("tab") == "Built-in Nodes":
                        remove_page_from_pages(tab["pages"], en_key)
                        break
                for tab in nav["navigation"]["languages"][1]["tabs"]:
                    if tab.get("tab") == "内置节点":
                        remove_page_from_pages(tab["pages"], zh_key)
                        break
                raw = (full_category or "").strip()
                raw_lower = raw.lower()

                # Normalise "partner node/..." -> "api node/..." so both map to the same group
                if raw_lower.startswith("partner node"):
                    raw = "api node" + raw[len("partner node"):]
                    raw_lower = raw.lower()

                # API / partner nodes: 3-level hierarchy
                # e.g. "api node/image/ByteDance" -> API Node > Image > Bytedance
                if raw_lower.startswith("api node"):
                    parts = [p.strip() for p in raw.split("/") if p.strip()]
                    # parts[0] == "api node", parts[1] == type, parts[2] == provider
                    type_label = _seg_to_label(parts[1]) if len(parts) >= 2 else "Other"
                    provider_label = _seg_to_label(parts[2]) if len(parts) >= 3 else None
                    for tab in nav["navigation"]["languages"][0]["tabs"]:
                        if tab.get("tab") != "Built-in Nodes":
                            continue
                        wrapper = find_or_create_group_in_pages(tab["pages"], BUILTIN_WRAPPER_EN)
                        api_pages = find_or_create_group_in_pages(wrapper, api_node_top_en)
                        if type_label:
                            type_pages = find_or_create_group_in_pages(api_pages, type_label)
                            if provider_label:
                                provider_pages = find_or_create_group_in_pages(type_pages, provider_label)
                                provider_pages.append(en_key)
                            else:
                                type_pages.append(en_key)
                        else:
                            api_pages.append(en_key)
                        break
                    for tab in nav["navigation"]["languages"][1]["tabs"]:
                        if tab.get("tab") != "内置节点":
                            continue
                        wrapper = find_or_create_group_in_pages(tab["pages"], BUILTIN_WRAPPER_ZH)
                        api_pages = find_or_create_group_in_pages(wrapper, api_node_top_zh)
                        if type_label:
                            type_pages = find_or_create_group_in_pages(api_pages, type_label)
                            if provider_label:
                                provider_pages = find_or_create_group_in_pages(type_pages, provider_label)
                                provider_pages.append(zh_key)
                            else:
                                type_pages.append(zh_key)
                        else:
                            api_pages.append(zh_key)
                        break
                    added_en.append(en_key)
                    added_zh.append(zh_key)
                else:
                    # Regular nodes: support 2-level (group + optional sub-group)
                    # e.g. sampling/custom_sampling -> Sampling > Custom Sampling
                    group_en, group_zh, sub_en, sub_zh = _category_to_group_and_sub(raw)
                    for tab in nav["navigation"]["languages"][0]["tabs"]:
                        if tab.get("tab") != "Built-in Nodes":
                            continue
                        wrapper = find_or_create_group_in_pages(tab["pages"], BUILTIN_WRAPPER_EN)
                        gp = find_or_create_group_in_pages(wrapper, group_en)
                        if sub_en:
                            sub_gp = find_or_create_group_in_pages(gp, sub_en)
                            sub_gp.append(en_key)
                        else:
                            gp.append(en_key)
                        added_en.append(en_key)
                        break
                    for tab in nav["navigation"]["languages"][1]["tabs"]:
                        if tab.get("tab") != "内置节点":
                            continue
                        wrapper = find_or_create_group_in_pages(tab["pages"], BUILTIN_WRAPPER_ZH)
                        gp = find_or_create_group_in_pages(wrapper, group_zh)
                        if sub_zh:
                            sub_gp = find_or_create_group_in_pages(gp, sub_zh)
                            sub_gp.append(zh_key)
                        else:
                            gp.append(zh_key)
                        added_zh.append(zh_key)
                        break
            # Migrate any existing top-level groups (outside the wrapper) into the wrapper so they become collapsible
            for tab in nav["navigation"]["languages"][0]["tabs"]:
                if tab.get("tab") == "Built-in Nodes" and "pages" in tab:
                    _migrate_toplevel_groups_to_wrapper(tab["pages"], BUILTIN_WRAPPER_EN)
            for tab in nav["navigation"]["languages"][1]["tabs"]:
                if tab.get("tab") == "内置节点" and "pages" in tab:
                    _migrate_toplevel_groups_to_wrapper(tab["pages"], BUILTIN_WRAPPER_ZH)

            # Build node_name -> full_category lookup for restructuring
            node_cat_map: Dict[str, str] = {
                name: info.get("category", "")
                for name, info in _load_all_nodes_info().items()
            }
            # Rebuild all non-API groups from scratch so every node is placed in the
            # correct group/sub-group matching ComfyUI's category hierarchy.
            for tab in nav["navigation"]["languages"][0]["tabs"]:
                if tab.get("tab") == "Built-in Nodes" and "pages" in tab:
                    wrapper = find_group_in_pages(tab["pages"], BUILTIN_WRAPPER_EN)
                    if wrapper is not None:
                        _rebuild_wrapper_groups(wrapper, node_cat_map, lang_idx=0)
            for tab in nav["navigation"]["languages"][1]["tabs"]:
                if tab.get("tab") == "内置节点" and "pages" in tab:
                    wrapper = find_group_in_pages(tab["pages"], BUILTIN_WRAPPER_ZH)
                    if wrapper is not None:
                        _rebuild_wrapper_groups(wrapper, node_cat_map, lang_idx=1)

            for tab in nav["navigation"]["languages"][0]["tabs"]:
                if tab.get("tab") == "Built-in Nodes" and "pages" in tab:
                    _remove_empty_groups(tab["pages"])
                    # Tab level: flat pages (overview) stay before groups; inside groups: groups first
                    _sort_pages_alphabetically(tab["pages"], groups_first=False)
            for tab in nav["navigation"]["languages"][1]["tabs"]:
                if tab.get("tab") == "内置节点" and "pages" in tab:
                    _remove_empty_groups(tab["pages"])
                    _sort_pages_alphabetically(tab["pages"], groups_first=False)
            with open(DOCS_JSON, "w", encoding="utf-8") as f:
                json.dump(nav, f, indent=2, ensure_ascii=False)
            if added_en or added_zh:
                print(f"docs.json: updated {DOCS_JSON}")
                for k in added_en:
                    print(f"  + EN:  {k}")
                for k in added_zh:
                    print(f"  + ZH:  {k}")
            else:
                print("docs.json: no new entries (all synced nodes already in nav).")

    print("Done.")


if __name__ == "__main__":
    main()
