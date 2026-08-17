# Load Latent Upscale Model

The LatentUpscaleModelLoader node loads a specialized model designed for upscaling latent representations. It reads a model file from the system's designated folder and automatically detects its type (720p, 1080p, or other) to instantiate and configure the correct internal model architecture. The loaded model is then ready to be used by other nodes for latent space super-resolution tasks.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `model_name` | The name of the latent upscale model file to load. The available options are dynamically populated from the files present in your ComfyUI's `latent_upscale_models` directory. | COMBO | Yes | All files in the `latent_upscale_models` folder |

Note: The node automatically detects the model architecture from the file contents. Models containing 720p HunyuanVideo super-resolution layers are loaded as 720p models, models with 1080p-style upsampling layers are loaded as 1080p models, and models with other layer structures are loaded as LatentUpsampler models.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The loaded latent upscale model, configured and ready for use. | LATENT_UPSCALE_MODEL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/en.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
