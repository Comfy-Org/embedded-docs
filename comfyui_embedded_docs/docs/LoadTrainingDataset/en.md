# Load Training Dataset

This node loads an encoded training dataset (latents and conditioning) from disk for use in training. After you select a previously saved dataset folder, it reads all shard files inside it and returns the combined latent vectors and conditioning data.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `folder_name` | Saved dataset to load, from the datasets directory. | COMBO | Yes | Dynamically populated with all dataset folders found in the registered datasets directories. Only folders containing a `metadata.json` file or `.safetensors` files are listed. |

**Note:** The selected dataset folder must be a subfolder of a registered datasets directory and must contain at least one shard file named `shard_*.pkl`; otherwise the node raises an error.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `latents` | List of latent dicts loaded from the dataset shards, each containing a `samples` tensor. | LATENT |
| `conditioning` | List of conditioning lists loaded from the dataset shards, one per sample. | CONDITIONING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/en.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
