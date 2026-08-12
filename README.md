# comfyui_embedded_docs

> [!NOTE]
> This is only for core nodes. For embedded custom node documentation, please see <https://docs.comfy.org/custom-nodes/help_page>

## Updating Documentation

Each core node should have a folder containing its node name, then a two letter locale.md, and potentially any assets along with it in the same folder.

See [FluxProUltraImageNode](https://github.com/Comfy-Org/embedded-docs/tree/main/docs/FluxProUltraImageNode) as an example.

> [!NOTE]
> A fallback is simply docs/NodeName.md, but this is discouraged.

## Previewing Changes Locally

To preview your documentation changes in ComfyUI:

1. **Install editable version (optional but recommended):**

   ```bash
   # If you have one, activate your ComfyUI virtual environment first
   pip uninstall comfyui-embedded-docs  # Remove existing PyPI version
   pip install -e /path/to/embedded-docs/  # Install editable version
   ```

2. **Launch and preview:**
   - Start ComfyUI
   - Refresh the frontend tab after making documentation changes

> [!TIP]
> The editable installation allows you to see changes immediately after copying files, without reinstalling the package.

## Publishing

The package is automatically published to PyPI when:

1. You manually trigger the workflow (Actions → Publish to PyPI → Run workflow)
2. You push changes to `pyproject.toml` on the main branch
3. A pull request that modifies `pyproject.toml` is merged to main

The publishing workflow:

1. Builds the package using `python -m build`
2. Publishes to PyPI using the configured PYPI_TOKEN secret

## Syncing to Comfy docs

The `docs-generation` pipeline syncs embedded-docs (en.md, zh.md, ja.md, ko.md, and assets) to the [Comfy-Org/docs](https://github.com/Comfy-Org/docs) repository as built-in node MDX files and updates the navigation (`docs.json`).

The pipeline lives in [`docs-generation/`](docs-generation/README.md) and includes:

- `docs-generation/scripts/scan_missing_nodes.py` – scan the ComfyUI codebase, detect new/changed nodes
- `docs-generation/scripts/batch_generate_docs.py` + `batch_translate_docs.py` – LLM-based doc generation and 11-language translation
- `docs-generation/scripts/update_param_translations.py` – reconcile parameter names with the ComfyUI frontend i18n
- `docs-generation/scripts/sync_to_comfy_docs.py` – generate `built-in-nodes/*.mdx` + update `docs.json` navigation
- `docs-generation/scripts/version_tracker.py` – per-node source hash tracking

See [docs-generation/README.md](docs-generation/README.md) for full setup and workflow.

**Environment variables (optional):**

- `EMBEDDED_DOCS_PATH` – Path to this repo (default: the repo this pipeline lives in)
- `COMFYUI_PATH` – Path to the ComfyUI repo (used to read node category from source)
- `TARGET_DOCS` – Path to the comfy/docs root (e.g. `/path/to/comfy/docs`)

**Category mapping:** The sync script uses each node's ComfyUI category to put it in the right docs.json group. For the most complete categories (including API nodes and nodes that get category from a base class), run the node scanner once so it can write `docs-generation/data/all_nodes_info.json`; the sync script will prefer that file when present.

```sh
# Optional: run scanner first to build all_nodes_info.json (better category coverage)
python docs-generation/scripts/scan_missing_nodes.py
```

**Run from repo root:**

```sh
# Test mode: sync first 10 nodes (dry run: no writes)
TARGET_DOCS=/path/to/comfy/docs python docs-generation/scripts/sync_to_comfy_docs.py --mode test --count 10 --dry-run

# Sync all nodes with en.md and update docs.json
TARGET_DOCS=/path/to/comfy/docs python docs-generation/scripts/sync_to_comfy_docs.py --mode all

# Sync a single node
TARGET_DOCS=/path/to/comfy/docs python docs-generation/scripts/sync_to_comfy_docs.py --node Load3D
```

You can also use the interactive menu: run `python docs-generation/main.py` and choose option **5) Sync to Comfy docs**.

## Linting

To ensure minimal consistency across nodes documentation, it is recommended to follow the Markdown linting principles. Some of the linting issues can be fixed automatically with the shell script below. Note this requires to install `markdownlint-cli`.

```sh
# Install markdownlint-cli
# If you encounter the error npm.ps1 cannot be loaded because running scripts is disabled on this system
# Run this command: Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
npm install -g markdownlint-cli

# Fix linting issues in all markdown files under docs directory，using shell script (Linux)
bash fix_markdown.sh

# Fix linting issues for a specific node's documentation
bash fix_markdown.sh ClipLoader  # This will only check files in comfyui_embedded_docs/docs/ClipLoader/

# Or fix linting issues in markdown files, using powershell script (Windows)
powershell -ExecutionPolicy Bypass -File fix_markdown.ps1
```