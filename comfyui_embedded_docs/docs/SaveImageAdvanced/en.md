# Save Image (Advanced)

The **SaveImageAdvanced** node saves images to your ComfyUI output directory with advanced control over file format, bit depth, and color space. It supports saving as PNG or EXR files and can embed workflow metadata into the saved files.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | The images to save. | IMAGE | Yes | - |
| `filename_prefix` | The prefix for the file to save. May include formatting tokens such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%`. (default: "ComfyUI") | STRING | Yes | - |
| `format` | The file format in which to save the image. Selecting a format reveals additional options for that format. | DYNAMIC_COMBO | Yes | `"png"`<br>`"exr"` |

### PNG Inputs

These inputs are shown when `format` is set to `"png"`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | The bit depth used when saving the image. (default: "8-bit") | COMBO | Yes (conditional) | `"8-bit"`<br>`"16-bit"` |
| `input_color_space` | The color space of the input tensor. (default: "sRGB") | COMBO | Yes (conditional) | `"sRGB"` |

### EXR Inputs

These inputs are shown when `format` is set to `"exr"`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `bit_depth` | The bit depth used when saving the image. (default: "32-bit float") | COMBO | Yes (conditional) | `"32-bit float"` |
| `input_color_space` | Colorspace of the input tensor. The EXR is always written as scene-linear in the matching gamut. (default: "sRGB") | COMBO | Yes (conditional) | `"sRGB"`<br>`"HDR"`<br>`"linear"` |

**Notes on Parameter Dependencies and File Behavior:**

- `bit_depth` and `input_color_space` only appear when their parent `format` is selected.
- For PNG format, only `"8-bit"` and `"16-bit"` bit depths are available, and only the `"sRGB"` color space. The color space selection does not modify PNG pixels — PNG files are always saved as sRGB-encoded images.
- For EXR format, only `"32-bit float"` bit depth is available, with `"sRGB"`, `"HDR"`, or `"linear"` color spaces.
- The `input_color_space` parameter for EXR determines how the input tensor is interpreted before saving:
  - `"sRGB"` — input is sRGB-encoded Rec.709; the inverse sRGB EOTF is applied.
  - `"HDR"` — input is HLG-encoded Rec.2020 (BT.2100); the inverse HLG OETF is applied to get scene-linear light.
  - `"linear"` — input is already scene-linear (Rec.709 primaries); written through unchanged. Use this for renderer/compositor output.
- Workflow metadata (prompt and extra PNG info) is embedded into saved PNG and EXR files unless metadata writing is disabled with the `--disable-metadata` command-line argument.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | The images that were saved (the same images passed to the `images` input). The node's UI result includes a list of the saved files, each reported with its filename, subfolder, and type ("output"). | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageAdvanced/en.md)

---
**Source fingerprint (SHA-256):** `b03a822a90cf50d30fbf4397ab280393951f08d2339dd48c0dbaf75d9c415bca`
