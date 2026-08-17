# Load Latent

The LoadLatent node loads latent representations that were previously saved as .latent files in the input directory. It reads the latent tensor data from the selected file and applies any necessary scaling adjustments before returning the results for use in other nodes.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `latent` | Selects which .latent file to load from the available files in the input directory | COMBO | Yes | All .latent files in the input directory |

Note: For .latent files that do not contain the `latent_format_version_0` marker, the loaded latent tensor is multiplied by 1/0.18215 so that its scaling matches the format expected by other nodes.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `LATENT` | Returns the loaded latent representation data from the selected file | LATENT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/en.md)

---
**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`
