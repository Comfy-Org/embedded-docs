This node will detect models located in the `ComfyUI/models/checkpoints` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** (shortcut 'R') to allow it to read the model files from the corresponding folder.


The CheckpointLoaderSimple node is designed for loading model checkpoints without the need for specifying a configuration. It simplifies the process of checkpoint loading by requiring only the checkpoint name, making it more accessible for users who may not be familiar with the configuration details.
## Input types

| Field     | Comfy dtype | Description                                                                       |
|-----------|-------------|-----------------------------------------------------------------------------------|
| `ckpt_name`| `COMBO[STRING]` | Specifies the name of the checkpoint to be loaded, determining which checkpoint file the node will attempt to load and affecting the node's execution and the model that is loaded. |

## Output types

| Field | Comfy dtype | Description                                                              |
|-------|-------------|--------------------------------------------------------------------------|
| `model` | `MODEL` | Returns the loaded model, allowing it to be used for further processing or inference. |
| `clip`  | `CLIP`     | Returns the CLIP model associated with the loaded checkpoint, if available. |
| `vae`   | `VAE`      | Returns the VAE model associated with the loaded checkpoint, if available. |
