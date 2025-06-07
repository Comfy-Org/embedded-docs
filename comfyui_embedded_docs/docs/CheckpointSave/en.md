The CheckpointSave node is designed for saving the state of various model components, including models, CLIP, and VAE, into a checkpoint file. This functionality is crucial for preserving the training progress or configuration of models for later use or sharing.

## Inputs

| Parameter | Data Type   | Description |
|-----------|-------------|-------------|
| `model`   | `MODEL`     | The model parameter represents the primary model whose state is to be saved. It is essential for capturing the current state of the model for future restoration or analysis. |
| `clip`    | `CLIP`      | The clip parameter is intended for the CLIP model associated with the primary model, allowing its state to be saved alongside the main model. |
| `vae`     | `VAE`       | The vae parameter is for the Variational Autoencoder (VAE) model, enabling its state to be saved for future use or analysis alongside the main model and CLIP. |
| `filename_prefix` | `STRING` | This parameter specifies the prefix for the filename under which the checkpoint will be saved, providing a means to organize and identify saved checkpoints. |

## Outputs

This node will output a checkpoint file, and the corresponding output file path is `output/checkpoints/` directory
