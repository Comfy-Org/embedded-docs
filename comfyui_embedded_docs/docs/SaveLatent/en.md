# Save Latent

The SaveLatent node saves latent samples to disk as .latent files for later use or sharing. It writes the latent tensor data to the output folder using the specified filename prefix, and embeds optional metadata such as prompt information. The node also returns the original latent samples unchanged, so the workflow can continue using them.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `samples` | The latent samples to be saved to disk | LATENT | Yes | - |
| `filename_prefix` | The prefix used to generate the output filename and subfolder path (default: "latents/ComfyUI") | STRING | Yes | - |
| `prompt` | The workflow prompt data, stored as JSON metadata in the saved file (hidden input, supplied automatically) | PROMPT | No | - |
| `extra_pnginfo` | Additional workflow metadata, stored as JSON in the saved file (hidden input, supplied automatically) | EXTRA_PNGINFO | No | - |

Note: Metadata is written to the saved .latent file unless ComfyUI is started with the `--disable-metadata` argument. The saved file is named using the pattern `{filename}_{5-digit counter}_.latent`, for example `ComfyUI_00001_.latent`.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | The original latent samples, returned unchanged | LATENT |
| `ui` | File location details (filename, subfolder, and output type) for the saved latent file | UI |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/en.md)

---
**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`
