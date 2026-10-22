# Text Encode MOSS-Image Edit

Encodes an edit instruction together with reference images into conditioning for a MOSS-Image edit LoRA. Connect the output as the positive conditioning and run a second instance with the same references for the negative one. The references are used at the size they arrive, so scale them before connecting. This node is marked as experimental in ComfyUI.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `clip` | The CLIP model that tokenizes the instruction and encodes it. | CLIP | Yes | - |
| `prompt` | The instruction describing the edit. Supports multiline text and dynamic prompts. | STRING | Yes | Any text |
| `vae` | The VAE used to encode the reference images into reference latents. | VAE | Yes | - |
| `edit_format` | The layout the edit LoRA was trained with. It selects the reference latents method and whether the text encoder also sees the references. | COMBO | Yes | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Growable slot: connect one or more reference images (`image_1`, `image_2`, ...). Each image is used at the size it arrives, has its alpha channel dropped, and is VAE-encoded into a reference latent. | IMAGE | Yes | 1 or more images |

**Note:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"` the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `conditioning` | The encoded instruction with the reference latents and the matching reference latents method attached. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/en.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
