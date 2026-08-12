# Sync pipeline: embedded-docs → Comfy-Org/docs

This directory contains the scripts that generate the `built-in-nodes/*` pages on
[docs.comfy.org](https://docs.comfy.org) from the documentation sources in this
repository (`comfyui_embedded_docs/docs/<NodeName>/{en,zh,ja,ko}.md`).

## `sync_to_docs.py`

Converts every node's `en.md` (+ `zh.md` / `ja.md` / `ko.md` when present) into an
`.mdx` page in a checkout of [Comfy-Org/docs](https://github.com/Comfy-Org/docs),
and updates the `docs.json` navigation (slug casing, category groups, locale tabs).

### Usage

```bash
# Point at a Comfy-Org/docs checkout (defaults to ../docs relative to this repo)
export TARGET_DOCS=/path/to/comfy/docs

# Dry-run (no files written)
python3 scripts/sync_to_docs.py --node Canny --dry-run

# Sync a single node
python3 scripts/sync_to_docs.py --node Canny

# Sync everything (all nodes with en.md)
python3 scripts/sync_to_docs.py --mode all
```

Optional env vars:

| Var | Purpose |
|-----|---------|
| `TARGET_DOCS` | Comfy-Org/docs checkout root (default: `../docs` next to this repo) |
| `COMFYUI_PATH` | ComfyUI source checkout, used only to extract node categories when scanner output is absent |
| `ALL_NODES_INFO` | Path to scanner output JSON (`{nodes: {name: {category, ...}}}`), enables category lookup without ComfyUI source |

### What it generates

- **Per-locale `.mdx`**: `built-in-nodes/X.mdx`, `zh/built-in-nodes/X.mdx`, `ja/...`, `ko/...`
- **Frontmatter**: title + a **concrete SEO description** extracted from the node's
  `en.md` overview first sentence (not a templated string), `sidebarTitle`, icon, wide mode
- **`docs.json` nav**: adds/updates the node slug under the right category group for
  all 4 locales, with case-corrected slugs matching the on-disk files
- **Assets**: copies referenced images to `images/built-in-nodes/<Node>/`

### MDX safety

`_normalize_mdx_content()` makes the Markdown source safe for Mintlify's MDX parser:

- Fenced code blocks are preserved byte-for-byte (never escaped)
- Whitelisted HTML tags (`video`, `source`, `p`, `br`, ...) stay raw
- Paired Mintlify components (`<Note>...</Note>`, `<Tip>`, `<Accordion>`, ...) stay raw
- Unknown tags (`<bbox>` API syntax examples) are escaped to `&lt;bbox>` in pairs
- Orphaned closing tags are escaped (avoids acorn "Unexpected closing slash" errors)
- Comparison operators in prose (`<= 3840`) are escaped

### Notes

- Node slugs in `docs.json` must match the on-disk `.mdx` filename **exactly**
  (Mintlify routing is case-sensitive). `published_node_name()` resolves the
  published name per locale against real directory entries — important on macOS,
  where `Path.is_file()` cannot distinguish `CLIPTextEncodeControlnet.mdx` from
  `ClipTextEncodeControlnet.mdx` (case-insensitive APFS).
- After syncing, a PR against Comfy-Org/docs is opened separately (the pipeline
  itself only writes files and updates `docs.json` locally).
