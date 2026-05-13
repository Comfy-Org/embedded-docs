> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/en.md)

The LatentCutToBatch node splits a latent representation along a chosen dimension into multiple slices and stacks them into a new batch. This allows you to process different parts of a latent sample independently.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `samples` | LATENT | Yes | - | The latent representation to be split and batched. |
| `dim` | COMBO | Yes | `"t"`<br>`"x"`<br>`"y"` | The dimension along which to cut the latent samples. `"t"` refers to the temporal dimension, `"x"` to the width, and `"y"` to the height. |
| `slice_size` | INT | Yes | 1 to 16384 | The size of each slice to cut from the specified dimension. If the dimension's size is not perfectly divisible by this value, the remainder is discarded. (default: 1) |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `samples` | LATENT | The resulting latent batch, containing the sliced and stacked samples. |

---
**Source fingerprint (SHA-256):** `38d0ace3ef91e47e3f047aa7057c61e09b6534702526b34691b4bc239c933cd3`
