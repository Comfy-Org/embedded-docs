> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchLatentsNode/en.md)

The Batch Latents node combines multiple latent inputs into a single batch. It takes a variable number of latent samples and merges them along the batch dimension, allowing them to be processed together in subsequent nodes. This is useful for generating or processing multiple images in a single operation.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `latents` | LATENT | Yes | 2 to 50 inputs | A set of latent samples to be combined into a single batch. You must provide at least two latents, and you can add up to 50. The node automatically creates input slots as you connect more latents. |

**Note:** You must provide at least two latent inputs for the node to function. The node will automatically create input slots as you connect more latents, up to a maximum of 50.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `output` | LATENT | A single latent output containing all the input latents combined into one batch. |