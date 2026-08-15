"""Shared helpers for fetching and saving frontend nodeDefs translations.

Used by scripts/sync_frontend_translations.py and
scripts/update_param_translations.py so the remote source and the write
strategy live in exactly one place.
"""

import json
import os
import urllib.request

REMOTE_REPO = "Comfy-Org/ComfyUI_frontend"
REMOTE_BRANCH = "master"
REMOTE_BASE = f"https://raw.githubusercontent.com/{REMOTE_REPO}/{REMOTE_BRANCH}/src/locales"


def fetch_remote_translations(langs):
    """Fetch nodeDefs.json for the given languages from GitHub raw.

    Returns {lang: data}; languages whose fetch failed map to {}.
    """
    out = {}
    for lang in langs:
        url = f"{REMOTE_BASE}/{lang}/nodeDefs.json"
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "docs-generation"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                out[lang] = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"⚠️  Warning: failed to fetch {lang} from GitHub ({url}): {e}")
            out[lang] = {}
    return out


def save_translations(path, new_data, merge=True):
    """Write translations to ``path`` without destroying previous good data.

    - merge=True (default): non-empty languages in ``new_data`` are merged
      over the existing file, so a failed fetch never erases what was there
      (e.g. the 'en' key that lib/doc_title.py depends on).
    - The file is written atomically via a same-directory temp file, so a
      crash mid-write cannot leave truncated JSON behind.

    Returns the dict that was written.
    """
    merged = {}
    if merge and path.exists():
        try:
            with open(path, 'r', encoding='utf-8') as f:
                merged = json.load(f)
        except (json.JSONDecodeError, OSError):
            merged = {}
    for lang, lang_data in new_data.items():
        if lang_data or not merge:
            merged[lang] = lang_data
    tmp_path = path.with_name(path.name + '.tmp')
    with open(tmp_path, 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    os.replace(tmp_path, path)
    return merged
