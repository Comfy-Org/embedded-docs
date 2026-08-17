# Load LTXV Audio VAE

The LTXV Audio VAE Loader node loads a pre-trained Audio Variational Autoencoder (VAE) model from a checkpoint file. It reads the specified checkpoint, loads its weights and metadata, and prepares the model for use in audio generation or processing workflows within ComfyUI.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Audio VAE checkpoint to load. This is a dropdown list populated with all the files found in your ComfyUI `checkpoints` directory. | COMBO | Yes | All files in the `checkpoints` folder (populated dynamically).<br>*Example: `"audio_vae.safetensors"`* |

Note: The node raises an error if the selected checkpoint file cannot be found or does not contain a valid audio VAE.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `Audio VAE` | The loaded Audio Variational Autoencoder model, ready to be connected to other audio processing nodes. | VAE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/en.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
