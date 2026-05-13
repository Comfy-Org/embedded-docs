> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPSave/en.md)

The `CLIPSave` node saves a CLIP text encoder model to disk in SafeTensors format. It is designed for advanced model merging workflows and automatically separates the CLIP model into its component parts (such as CLIP-L, CLIP-G, or T5XXL) based on the model's internal structure, saving each component as a separate file.

## Inputs

| Parameter | Data Type | Input Type | Default | Range | Description |
|-----------|-----------|------------|---------|-------|-------------|
| `clip` | CLIP | Required | - | - | The CLIP model to be saved. |
| `filename_prefix` | STRING | Required | `clip/ComfyUI` | - | The prefix path and filename for the saved file(s). The node will append a component suffix (e.g., `_clip_l`, `_clip_g`) and a counter to create unique filenames. |
| `prompt` | PROMPT | Hidden | - | - | The workflow prompt information, saved as metadata in the output file. |
| `extra_pnginfo` | EXTRA_PNGINFO | Hidden | - | - | Additional metadata, saved as key-value pairs in the output file. |

## Outputs

This node has no output connections. It saves the processed files directly to the `ComfyUI/output/` directory.

### Saved File Details

The node analyzes the CLIP model's state dictionary and saves separate SafeTensors files for each detected component. The component is identified by the prefix of its parameter keys. The following prefixes are checked:

- `clip_l.` (CLIP-L text encoder)
- `clip_g.` (CLIP-G text encoder)
- `clip_h.` (CLIP-H text encoder)
- `t5xxl.` (T5-XXL text encoder)
- `pile_t5xl.` (Pile-T5-XL text encoder)
- `mt5xl.` (mT5-XL text encoder)
- `umt5xxl.` (UMT5-XXL text encoder)
- `t5base.` (T5-Base text encoder)
- `gemma2_2b.` (Gemma 2 2B text encoder)
- `llama.` (LLaMA text encoder)
- `hydit_clip.` (Hydit CLIP text encoder)
- Empty prefix (other CLIP components)

For each detected component, the node creates a file with the name `{filename_prefix}_{counter:05}_.safetensors`, where the component prefix is appended to the filename prefix (e.g., `clip/ComfyUI_clip_l_00001_.safetensors`). The `transformer.` prefix is removed from parameter keys during saving.

---
**Source fingerprint (SHA-256):** `039b39cbfb9b04ccebc5fc885ebe75dfde14838530d38133d0a3a6311e392059`
