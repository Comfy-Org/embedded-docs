> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/en.md)

The LTXV Audio VAE Loader node loads a pre-trained Audio Variational Autoencoder (VAE) model from a checkpoint file. It reads the specified checkpoint, loads its weights and metadata, and prepares the model for use in audio generation or processing workflows within ComfyUI.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `ckpt_name` | STRING | Yes | All files in the `checkpoints` folder.<br>*Example: `"audio_vae.safetensors"`* | Audio VAE checkpoint to load. This is a dropdown list populated with all the files found in your ComfyUI `checkpoints` directory. |

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `Audio VAE` | VAE | The loaded Audio Variational Autoencoder model, ready to be connected to other audio processing nodes. |

---
**Source fingerprint (SHA-256):** `44e79f694eed796a83f3ac25c56946baaa12b016568bd8824eb179bf79e50588`
