> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/en.md)

Create a Recraft color by specifying individual red, green, and blue values. This node takes RGB integer values (0-255) and converts them into a Recraft color format that can be used in other Recraft operations. You can also optionally provide an existing Recraft color chain to extend it with the new color.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `r` | INT | Yes | 0-255 | Red value of color (default: 0) |
| `g` | INT | Yes | 0-255 | Green value of color (default: 0) |
| `b` | INT | Yes | 0-255 | Blue value of color (default: 0) |
| `recraft_color` | COLOR | No | - | Optional existing Recraft color chain to extend with the new RGB color |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `recraft_color` | COLOR | The created Recraft color object containing the specified RGB values, or the extended color chain if an existing one was provided |

---
**Source fingerprint (SHA-256):** `8c3503632d085fa4c1771f92f17008b7b051e9604d9e7d1e7d352cbbbd22dddc`
