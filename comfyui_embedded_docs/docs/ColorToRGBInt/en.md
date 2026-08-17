# Color Picker

The **ColorToRGBInt** node converts a color specified in hexadecimal format (like `#FF5733`) into a single RGB integer value. It takes the red, green, and blue components from the color string and combines them into one integer, and returns the hexadecimal representation. Colors with an alpha channel (`#RRGGBBAA`) are also supported, and the alpha value is returned separately.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `color` | A color value in the hexadecimal format `#RRGGBB` or `#RRGGBBAA`. Must be exactly 7 or 9 characters long and start with `#`. | COLOR | Yes | `#RRGGBB`<br>`#RRGGBBAA` |

**Note:** The input `color` string must follow the format `#RRGGBB` or `#RRGGBBAA` exactly. If the string is not 7 or 9 characters long, does not start with `#`, or contains characters that are not valid hexadecimal digits, the node raises an error.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `rgb_int` | The calculated RGB integer value, derived from the formula: `(Red * 65536) + (Green * 256) + Blue`. | INT |
| `hex` | The hexadecimal color string in `#RRGGBB` format. If the input includes an alpha channel, it is removed from this output. | COLOR |
| `alpha` | The alpha (opacity) value as a number from 0.0 to 1.0. For input colors with an alpha channel (`#RRGGBBAA`), it is the two-digit alpha value divided by 255. For colors without an alpha channel, it is 1.0. | FLOAT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorToRGBInt/en.md)

---
**Source fingerprint (SHA-256):** `4e64616d168beee73bca4364d47e2a089418b5046a76bfcfa061dfab9a5e49ed`
