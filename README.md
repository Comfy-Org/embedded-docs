# comfyui_embedded_docs

> [!NOTE]
> This is only for core nodes. For embedded custom node documentation, please see https://docs.comfy.org/custom-nodes/help-page

## Updating Documentation

Each core node should have a folder containing its node name, then a two letter locale.md, and potentially any assets along with it in the same folder.

See [FluxProUltraImageNode](https://github.com/Comfy-Org/embedded-docs/tree/main/docs/FluxProUltraImageNode) as an example.

> [!NOTE]
> A fallback is simply docs/NodeName.md, but this is discouraged.

## Publishing

The package is automatically published to PyPI when:
1. You manually trigger the workflow (Actions → Publish to PyPI → Run workflow)
2. You push changes to `pyproject.toml` on the main branch
3. A pull request that modifies `pyproject.toml` is merged to main

The publishing workflow:
1. Copies documentation from `docs/` to `comfyui_embedded_docs/docs/`
2. Builds the package using `python -m build`
3. Publishes to PyPI using the configured PYPI_TOKEN secret