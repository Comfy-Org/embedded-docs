# Load Diffusers Model (DEPRECATED)

The DiffusersLoader node is deprecated. It loads pre-trained models saved in the Hugging Face diffusers format and returns the three standard components needed by the pipeline: MODEL, CLIP, and VAE. The node automatically scans the configured diffusers folders for valid model directories (folders containing a `model_index.json` file) and lets you choose which one to load.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `model_path` | The path to the diffusers model directory to load. The node scans the configured diffusers folders and lists every directory that contains a `model_index.json` file. | COMBO | Yes | Auto-populated from the configured diffusers folders (every subdirectory containing a `model_index.json` file) |

Note: the selected path is validated against the list of discovered models. Loading fails with an error if the path is no longer in the list or if the model directory cannot be found.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `MODEL` | The loaded model component from the diffusers format | MODEL |
| `CLIP` | The loaded CLIP text-encoding model component from the diffusers format | CLIP |
| `VAE` | The loaded VAE (Variational Autoencoder) component from the diffusers format | VAE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffusersLoader/en.md)

---
**Source fingerprint (SHA-256):** `75238342d05eac7528f981a2d4544accb6053891cd078a77751cc838054225d4`
