# Save Image (Advanced)

The **Save Image (Advanced)** node saves the input images to your ComfyUI output directory with advanced control over file format, bit depth, and color space. It supports saving as PNG or EXR files and can embed workflow metadata into the saved files.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `images` | The images to save. | IMAGE | Yes | - |
| `filename_prefix` | The prefix for the file to save. May include formatting tokens such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%`. (default: "ComfyUI") | STRING | Yes | - |
| `format` | The file format in which to save the image. Selecting a format reveals additional options for that format. | DYNAMIC_COMBO | Yes | `"png"`<br>`"exr"` |

### PNG Inputs

These options appear when `format` is set to `"png"`.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `bit_depth` | The bit depth for the saved PNG file. (default: "8-bit") | COMBO | Yes (conditional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | Colorspace of the input tensor. Only sRGB is available for PNG format. (default: "sRGB") | COMBO | Yes (conditional) | `"sRGB"` |

### EXR Inputs

These options appear when `format` is set to `"exr"`.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `bit_depth` | The bit depth for the saved EXR file. (default: "32-bit float") | COMBO | Yes (conditional) | `"32-bit float"` |
| `input_color_space` | Colorspace of the input tensor. The EXR is always written as scene-linear in the matching gamut.<br>`"sRGB"` — input is sRGB-encoded Rec.709; the inverse sRGB EOTF is applied.<br>`"HDR"` — input is HLG-encoded Rec.2020 (BT.2100); the inverse HLG OETF is applied to get scene-linear light.<br>`"linear"` — input is already scene-linear (Rec.709 primaries); written through unchanged. Use this for renderer/compositor output. (default: "sRGB") | COMBO | Yes (conditional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notes on Parameter Dependencies:**
- The `bit_depth` and `input_color_space` parameters are only available when a specific `format` is selected.
- For PNG format, only "8-bit" and "16-bit" bit depths are available, and only "sRGB" color space.
- For EXR format, only "32-bit float" bit depth is available, with "sRGB", "HDR", or "linear" color spaces.
- Images must have 1 (grayscale), 3 (RGB), or 4 (RGBA) channels; other channel counts are not supported and raise an error.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `images` | The input images, passed through unchanged. The node's UI output provides a list of saved image results, each containing the filename, subfolder, and type ("output"). | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/en.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
