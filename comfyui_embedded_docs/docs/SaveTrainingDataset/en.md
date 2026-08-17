# Save Training Dataset

This node saves a prepared training dataset to your computer's hard drive. It takes encoded data, which includes image latents and their corresponding text conditioning, and organizes them into multiple smaller files called shards for easier management. The node automatically creates a folder in the datasets directory and saves both the shard data files and a metadata file describing the dataset.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `latents` | List of latent dicts from MakeTrainingDataset. | LATENT | Yes | N/A |
| `conditioning` | List of conditioning lists from MakeTrainingDataset. | CONDITIONING | Yes | N/A |
| `folder_name` | Name of folder to save the dataset into, inside the datasets directory. Subfolders like 'project/run1' are allowed. (default: "training_dataset") | STRING | Yes | N/A |
| `shard_size` | Number of samples per shard file. (default: 1000) | INT | Yes | 1 to 100000 |

**Note:** The number of items in the `latents` list must exactly match the number of items in the `conditioning` list. The node raises an error if these counts do not match. The `folder_name` must name a subfolder of the datasets directory: the root datasets folder itself, as well as any path that escapes it (such as '..' or an absolute path), is rejected.

## Outputs

This node does not produce any output data. It saves the dataset as numbered shard files (for example `shard_0000.pkl`) and a `metadata.json` file inside the chosen folder in the datasets directory.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/en.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
