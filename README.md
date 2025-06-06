# comfyui_embedded_docs

> [!NOTE]
> This is only for core nodes. For embedded custom node documentation, please see https://docs.comfy.org/custom-nodes/help_page

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