"""Central path configuration for the docs-generation pipeline."""

from __future__ import annotations

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

LIB_DIR = REPO_ROOT / "lib"
SCRIPTS_DIR = REPO_ROOT / "scripts"
CONFIG_DIR = REPO_ROOT / "config"
DATA_DIR = REPO_ROOT / "data"
DOCS_DIR = REPO_ROOT / "docs"
AI_INPUT_DIR = REPO_ROOT / "ai_input"
LOGS_DIR = REPO_ROOT / "logs"
TRANSLATION_BATCHES_DIR = REPO_ROOT / "translation_batches"

ENV_FILE = REPO_ROOT / ".env"
TRANSLATION_CONFIG = CONFIG_DIR / "translation_config.json"
DOC_RULES = CONFIG_DIR / "doc_rules.txt"

ALL_NODES_INFO = DATA_DIR / "all_nodes_info.json"
NODE_VERSIONS = DATA_DIR / "node_versions.json"
NODE_TRANSLATIONS = DATA_DIR / "node_translations.json"
MISSING_NODES_REPORT = DATA_DIR / "missing_nodes_report.json"


def ensure_data_dir() -> Path:
    """Create data/ if missing (scanner and version DB write here)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    return DATA_DIR


def default_embedded_docs_path() -> Path:
    env = os.getenv("EMBEDDED_DOCS_PATH")
    if env:
        return Path(env)
    sibling = REPO_ROOT.parent / "embedded-docs"
    if (sibling / "comfyui_embedded_docs" / "docs").is_dir():
        return sibling
    return REPO_ROOT.parent


def embedded_docs_dir() -> Path:
    return default_embedded_docs_path() / "comfyui_embedded_docs" / "docs"


def load_dotenv() -> None:
    from dotenv import load_dotenv as _load

    _load(ENV_FILE)
