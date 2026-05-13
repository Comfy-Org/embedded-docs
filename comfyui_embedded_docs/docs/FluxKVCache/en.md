> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/en.md)

The Flux KV Cache node enables a Key-Value (KV) Cache optimization for Flux family models. This optimization improves performance when using reference images by caching certain computations, which can speed up the generation process.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | Yes | | The model to apply KV Cache optimization on. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `model` | MODEL | The patched model with KV Cache optimization enabled. |

---
**Source fingerprint (SHA-256):** `530c660ae23607d4035815826ae73cdcbebe7693ba47a3b0fe98e69f329b9e86`
