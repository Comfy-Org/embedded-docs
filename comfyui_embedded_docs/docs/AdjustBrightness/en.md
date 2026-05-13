> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/en.md)

The Adjust Brightness node modifies the brightness of an input image. It works by multiplying each pixel's value by a specified factor, then clamping the resulting values to stay within a valid range. A factor of 1.0 leaves the image unchanged, values below 1.0 make it darker, and values above 1.0 make it brighter.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to adjust. |
| `factor` | FLOAT | No | 0.0 - 2.0 | Brightness factor. 1.0 = no change, <1.0 = darker, >1.0 = brighter. (default: 1.0) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The output image with adjusted brightness. |

---
**Source fingerprint (SHA-256):** `c8f2fbb5fa149812a2ecd1ff9fce7bd6d29bf4c48b929e9ebc0a95c9e46ec65e`
