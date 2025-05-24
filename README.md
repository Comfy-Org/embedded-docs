# comfyui_embedded_docs

## Updating Documentation

Documentation files are stored in the `docs/` directory. Each node has its own subdirectory containing:
- `en.md` - English documentation
- `assets/` - Images and other assets used in the documentation

To update documentation, simply add or edit the relevant markdown files in the `docs/` directory.

## Publishing

The package is automatically published to PyPI when:
1. You manually trigger the workflow (Actions → Publish to PyPI → Run workflow)
2. You push changes to `pyproject.toml` on the main branch
3. A pull request that modifies `pyproject.toml` is merged to main

The publishing workflow:
1. Copies documentation from `docs/` to `comfyui_embedded_docs/docs/`
2. Builds the package using `python -m build`
3. Publishes to PyPI using the configured PYPI_TOKEN secret