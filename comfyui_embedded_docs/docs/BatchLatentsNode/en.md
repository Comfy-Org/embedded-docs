# Batch Latents

The Batch Latents node combines multiple latent inputs into a single batch. It takes a variable number of latent samples and merges them along the batch dimension, allowing them to be processed together in subsequent nodes. This is useful for generating or processing multiple images in a single operation.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `latents` | A set of latent samples to be combined into a single batch. You must provide at least one latent, and you can add up to 50. The node automatically creates input slots as you connect more latents. | LATENT | Yes | 1 to 50 inputs |

**Note:** You must provide at least one latent input for the node to function. The node will automatically create input slots as you connect more latents, up to a maximum of 50.

All input latents are reshaped to match the spatial dimensions of the first latent before being combined. Each latent's `batch_index` metadata is carried over to the output; an input without a `batch_index` gets a default sequence starting at 0.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `output` | A single latent output containing all the input latents combined into one batch. | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/en.md)

---
**Source fingerprint (SHA-256):** `38df5e6cfa391e054c663af1cc55728d115cebfbb804e1c2c51dfc2aab37df47`
