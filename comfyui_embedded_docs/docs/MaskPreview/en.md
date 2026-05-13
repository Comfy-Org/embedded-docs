> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/en.md)

The MaskPreview node saves mask data as a preview image to your ComfyUI output directory, allowing you to visually inspect mask data during workflow execution. It converts the input mask into a format suitable for image display and saves it with a configurable filename prefix.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `mask` | MASK | Yes | - | The mask data to be previewed and saved as an image |
| `filename_prefix` | STRING | No | - | Prefix for the output filename (default: "ComfyUI") |
| `prompt` | PROMPT | No | - | Prompt information for metadata (automatically provided) |
| `extra_pnginfo` | EXTRA_PNGINFO | No | - | Additional PNG information for metadata (automatically provided) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `ui` | DICT | Contains the preview image information and metadata for display in the UI |

---
**Source fingerprint (SHA-256):** `9f64adf4a0130368618fc1ca3655192686815ab10b4153f9552ef23149928e3f`
