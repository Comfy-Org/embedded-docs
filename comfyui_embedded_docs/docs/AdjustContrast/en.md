> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/en.md)

The Adjust Contrast node modifies the contrast level of an input image. It works by adjusting the difference between the light and dark areas of the image. A factor of 1.0 leaves the image unchanged, values below 1.0 reduce contrast, and values above 1.0 increase it.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The input image to have its contrast adjusted. |
| `factor` | FLOAT | No | 0.0 - 2.0 | Contrast factor. 1.0 = no change, <1.0 = less contrast, >1.0 = more contrast. (default: 1.0) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The resulting image with adjusted contrast. |

---
**Source fingerprint (SHA-256):** `01148cdd9d951e78c712c1c3159c5562a680a5147bd4a76e33d91543d5245854`
