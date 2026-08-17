# Preview Mask

The MaskPreview node shows a visual preview of mask data directly in the ComfyUI interface, so you can inspect masks during your workflow. It displays the preview without saving it to the ComfyUI output directory and passes the mask through as output.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `mask` | The mask data to be previewed | MASK | Yes | - |
| `filename_prefix` | Prefix for the output filename (default: "ComfyUI") | STRING | No | - |
| `prompt` | Prompt information for metadata (automatically provided) | PROMPT | No | - |
| `extra_pnginfo` | Additional PNG information for metadata (automatically provided) | EXTRA_PNGINFO | No | - |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `mask` | The mask data that was previewed, passed through unchanged | MASK |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/en.md)

---
**Source fingerprint (SHA-256):** `3d4ecb8cd90c3ecbe9d3cff8f782062c582c7190d9f0e0ed069cba114d4beac5`
