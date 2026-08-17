# Conditioning (Set Area with Percentage for Video)

The ConditioningSetAreaPercentageVideo node modifies conditioning data by defining a specific area and temporal region for video generation. It allows you to set the position, size, and duration of the area where the conditioning will be applied using percentage values relative to the overall dimensions. This is useful for focusing the generation on specific parts of a video sequence.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `conditioning` | The conditioning data to be modified | CONDITIONING | Yes | - |
| `width` | The width of the area as a percentage of the total width (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `height` | The height of the area as a percentage of the total height (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `temporal` | The temporal duration of the area as a percentage of the total video length (default: 1.0) | FLOAT | Yes | 0.0 - 1.0 |
| `x` | The horizontal starting position of the area as a percentage (default: 0.0) | FLOAT | Yes | 0.0 - 1.0 |
| `y` | The vertical starting position of the area as a percentage (default: 0.0) | FLOAT | Yes | 0.0 - 1.0 |
| `z` | The temporal starting position of the area as a percentage of the video timeline (default: 0.0) | FLOAT | Yes | 0.0 - 1.0 |
| `strength` | The strength multiplier applied to the conditioning within the defined area (default: 1.0) | FLOAT | Yes | 0.0 - 10.0 |

Note: All size and position values are normalized percentages (0.0 to 1.0) relative to the overall video dimensions and timeline.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `conditioning` | The modified conditioning data with the specified area and strength settings applied | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaPercentageVideo/en.md)

---
**Source fingerprint (SHA-256):** `9c5ddae6a2b1da5907fb52ef625eefb12b0b228fd3bd52c3033b5c4226d76150`
