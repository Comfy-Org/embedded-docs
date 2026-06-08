The CLIPAdd node combines two CLIP models by merging their key patches. It creates a copy of the first CLIP model and then adds most of the key patches from the second model, excluding position IDs and logit scale parameters. This allows you to blend features from different CLIP models while preserving the structure of the first model.

## Inputs

| Parameter | Description | Data Type | Input Type | Default | Range |
| --- | --- | --- | --- | --- | --- |
| `clip1` | The primary CLIP model that will be used as the base for merging | CLIP | Required | - | - |
| `clip2` | The secondary CLIP model that provides additional patches to be added | CLIP | Required | - | - |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `CLIP` | Returns a merged CLIP model combining features from both input models | CLIP |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/en.md)

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
