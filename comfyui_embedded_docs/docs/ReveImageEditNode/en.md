# Reve Image Edit

The Reve Image Edit node allows you to modify an existing image based on a text description. It uses the Reve API to interpret your instructions and apply the requested changes to the image you provide.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `image` | The image to edit. | IMAGE | Yes | - |
| `edit_instruction` | Text description of how to edit the image. Maximum 2560 characters. (default: "") | STRING | Yes | 1 to 2560 characters |
| `model` | Model version to use for editing. | DYNAMIC_COMBO | Yes | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Upscale the generated image. May add additional cost. (default: "disabled") | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `remove_background` | Remove the background from the generated image. May add additional cost. (default: false) | BOOLEAN | No | `true`<br>`false` |
| `seed` | Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0) | INT | No | 0 to 2147483647 |

### Model Inputs

Shared by the `reve-edit@20250915` and `reve-edit-fast@20251030` models.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model.aspect_ratio` | Aspect ratio of the output image. When set to `"auto"`, the aspect ratio is determined automatically. (default: "auto") | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Higher values produce better images but cost more credits. (default: 1) | INT | No | 1 to 5 |

### Upscale Inputs

Shown when `upscale` is set to `"enabled"`.

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | Upscale factor (2x, 3x, or 4x). (default: 2) | INT | No | 2 to 4 |

**Note:** The `upscale.upscale_factor` parameter only appears when `upscale` is set to `"enabled"`.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image` | The edited image generated based on the instruction. | IMAGE |

**Note:** This node is marked as deprecated.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/en.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
