# ComfyUI Embedded Docs — Documentation Pipeline

This directory contains the automation pipeline that keeps
[Comfy-Org/embedded-docs](https://github.com/Comfy-Org/embedded-docs) and the
`built-in-nodes/*` pages on [docs.comfy.org](https://docs.comfy.org) in sync with
the ComfyUI source code.

The pipeline scans the ComfyUI codebase for new/changed nodes, generates and
translates node documentation into 11 languages, and publishes it.

## Layout

```
pipeline/
├── main.py                     # CLI entry point (full workflows)
├── scripts/
│   ├── scan_missing_nodes.py   # Scan ComfyUI source: find new/changed nodes
│   ├── prepare_ai_input.py     # Build AI input bundles (source + meta + prompt)
│   ├── batch_generate_docs.py  # Generate en.md via LLM
│   ├── batch_translate_docs.py # Translate en.md → 11 languages via LLM
│   ├── update_param_translations.py  # Sync parameter names from frontend i18n
│   ├── sync_to_comfy_docs.py   # embedded-docs → Comfy-Org/docs (.mdx + docs.json)
│   ├── sync_frontend_translations.py # Export frontend param translations
│   ├── version_tracker.py      # Node version hash tracking
│   └── ...                     # maintenance / fixup helpers
├── lib/                        # shared modules (paths, extract, titles, hashes)
├── config/                     # generation rules + translation prompts
├── data/                       # scan results, version DB (gitignored, generated)
└── ai_input/                   # AI input bundles (gitignored, generated)
```

## Setup

```bash
cd pipeline
cp env.example .env
# edit .env: COMFYUI_PATH, LLM_API_KEY, etc.
pip install -r requirements.txt
```

## Weekly workflow

```bash
# 1. Pull latest ComfyUI source first (required!)
cd /path/to/ComfyUI && git fetch origin master && git rebase origin/master

# 2. Scan + regenerate changed node docs (never skip, even if scan says "no changes")
cd /path/to/embedded-docs/pipeline
python3 main.py --mode changed

# 3. Generate docs for new nodes
python3 main.py --mode all --force

# 4. Translate all languages (11 locales) + update param translations
python3 main.py --translate --all-languages --mode all

# 5. Sync to Comfy-Org/docs (built-in-nodes .mdx + docs.json nav)
TARGET_DOCS=/path/to/comfy/docs python3 scripts/sync_to_comfy_docs.py --mode all

# 6. Commit in embedded-docs, open PR; commit in docs, open PR
```

## Scripts overview

| Script | Purpose |
|--------|---------|
| `scan_missing_nodes.py` | Scan ComfyUI source; report new nodes, changed nodes (source hash), possibly deprecated docs. Outputs to `data/`. |
| `prepare_ai_input.py` | Build AI input bundles (source code + metadata + prompt) for new/changed nodes. |
| `batch_generate_docs.py` | Generate `en.md` from AI input bundles via the configured LLM (OpenAI-compatible API). |
| `batch_translate_docs.py` | Translate `en.md` into 11 languages (zh, zh-TW, es, fr, ja, ko, ru, ar, tr, pt-BR, fa). |
| `update_param_translations.py` | Reconcile parameter/output name translations against the ComfyUI frontend i18n. |
| `sync_frontend_translations.py` | Export the frontend's parameter translations for use by the above. |
| `sync_to_comfy_docs.py` | Generate `built-in-nodes/*.mdx` + update `docs.json` navigation in a Comfy-Org/docs checkout. |
| `version_tracker.py` | Track per-node source SHA-256 hashes; detects changed nodes. |

## Sync details (`sync_to_comfy_docs.py`)

- Generates per-locale `.mdx` (`built-in-nodes/X.mdx`, `zh/...`, `ja/...`, `ko/...`)
- Frontmatter `description` is a **concrete summary extracted from the node's
  `en.md` overview first sentence**, not a templated string
- Node slugs in `docs.json` are resolved per-locale against real on-disk file
  names (case-sensitive) — prevents the case-mismatch 404s that occurred when
  macOS's case-insensitive filesystem hid slug/filename differences
- MDX-safe normalization: code blocks preserved verbatim, whitelisted HTML and
  paired Mintlify components (`<Note>`/`<Tip>`/...) kept raw, unknown tags and
  orphaned closing tags escaped

## Env vars

See `env.example`. Key ones:

| Var | Required | Purpose |
|-----|----------|---------|
| `COMFYUI_PATH` | yes (scan/generate) | ComfyUI source checkout |
| `LLM_API_KEY` | yes (LLM steps) | OpenAI-compatible API key (any provider; `DEEPSEEK_API_KEY` also accepted for back-compat) |
| `API_BASE_URL` / `API_MODEL` | no | OpenAI-compatible endpoint + model (defaults: DeepSeek) |
| `EMBEDDED_DOCS_PATH` | no | embedded-docs repo root (defaults to repo root) |
| `TARGET_DOCS` | sync step | Comfy-Org/docs checkout |
| `COMFYUI_FRONTEND_PATH` | param-translation step | ComfyUI frontend repo |

## Notes

- **Never commit `.env`**, `data/`, or `ai_input/` (gitignored).
- The AI content pipeline uses an OpenAI-compatible chat API; configure provider
  via `API_BASE_URL` / `API_MODEL` / key.
- Replacement nodes (aliases in `nodes_replacements.py`) have no standalone
  class; the scanner reports them but they need no docs.
