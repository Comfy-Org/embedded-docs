# LatentCutToBatch

The LatentCutToBatch node splits a latent representation along a chosen dimension into multiple slices and stacks them into a new batch. This allows you to process different parts of a latent sample independently.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `samples` | The latent representation to be split and batched. | LATENT | Yes | - |
| `dim` | The dimension along which to cut the latent samples. `"t"` refers to the temporal dimension, `"x"` to the width, and `"y"` to the height. | COMBO | Yes | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | The size of each slice to cut from the specified dimension. If the dimension's size is not perfectly divisible by this value, the remainder is discarded. (default: 1) | INT | Yes | 1 to 16384 (max resolution) |

Note: If the selected dimension is the batch or channel axis, the input is returned unchanged. If `slice_size` is larger than the dimension's size, the entire dimension is used as a single slice.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | The resulting latent batch, containing the sliced and stacked samples. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/en.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
