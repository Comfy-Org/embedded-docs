> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/en.md)

The Flux KV Cache node applies a Key-Value (KV) Cache optimization to Flux family models. This optimization is specifically designed to improve performance when using reference images by caching certain computations, which can speed up the generation process.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Yes | | The model to use KV Cache on. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `model` | MODEL | The patched model with KV Cache enabled. |