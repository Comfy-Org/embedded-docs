> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/en.md)

The Reve Image Edit node allows you to modify an existing image based on a text description. It uses the Reve API to interpret your instructions and apply the requested changes to the image you provide.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | - | The image to edit. |
| `edit_instruction` | STRING | Yes | - | Text description of how to edit the image. Maximum 2560 characters. |
| `model` | MODEL | Yes | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"`<br>`"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` | Model version to use for editing. The options include specific model versions and aspect ratio settings. |
| `upscale` | COMBO | No | `"disabled"`<br>`"enabled"` | Controls whether to upscale the generated image. |
| `upscale_factor` | FLOAT | No | - | The factor by which to upscale the image when upscaling is enabled. |
| `remove_background` | BOOLEAN | No | - | Controls whether to remove the background from the generated image. |
| `seed` | INT | No | 0 to 2147483647 | Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0) |

**Note:** The `upscale_factor` parameter is only relevant when the `upscale` parameter is set to `"enabled"`.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `image` | IMAGE | The edited image generated based on the instruction. |