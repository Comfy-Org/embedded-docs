The `Save Checkpoint` node is designed to save a complete Stable Diffusion model (including UNet, CLIP, and VAE components) as a **.safetensors** format checkpoint file.

The Save Checkpoint is primarily used in model merging workflows. After creating a new merged model through nodes like `ModelMergeSimple`, `ModelMergeBlocks`, etc., you can use this node to save the result as a reusable checkpoint file.

## Inputs

| Parameter | Data Type | Description |
|-----------|-----------|-------------|
| `model` | MODEL | The model parameter represents the primary model whose state is to be saved. It is essential for capturing the current state of the model for future restoration or analysis. |
| `clip` | CLIP | The clip parameter is intended for the CLIP model associated with the primary model, allowing its state to be saved alongside the main model. |
| `vae` | VAE | The vae parameter is for the Variational Autoencoder (VAE) model, enabling its state to be saved for future use or analysis alongside the main model and CLIP. |
| `filename_prefix` | STRING | This parameter specifies the prefix for the filename under which the checkpoint will be saved. |

Additionally, the node has two hidden inputs for metadata:

**prompt (PROMPT)**: Workflow prompt information
**extra_pnginfo (EXTRA_PNGINFO)**: Additional PNG information

## Outputs

This node will output a checkpoint file, and the corresponding output file path is `output/checkpoints/` directory

## Architecture Compatibility

- Currently fully supported: SDXL, SD3, SVD and other mainstream architectures, see [source code](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L176-L189)
- Basic support: Other architectures can be saved but without standardized metadata information

## Related Links

Related source code: [nodes_model_merging.py#L227](https://github.com/comfyanonymous/ComfyUI/blob/master/comfy_extras/nodes_model_merging.py#L227)
