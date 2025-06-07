The CLIPLoader node is designed for loading CLIP models, supporting different types such as stable diffusion and stable cascade. It abstracts the complexities of loading and configuring CLIP models for use in various applications, providing a streamlined way to access these models with specific configurations.

## Inputs

| Parameter     | Data Type | Description |
|---------------|--------------|-------------|
| `clip_name`   | `COMBO[STRING]` | Specifies the name of the CLIP model to be loaded. This name is used to locate the model file within a predefined directory structure. |
| `type`        | `COMBO[STRING]` | Determines the type of CLIP model to load, offering options between 'stable_diffusion' and 'stable_cascade'. This affects how the model is initialized and configured. |

## Outputs

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `clip`    | `CLIP`      | The loaded CLIP model, ready for use in downstream tasks or further processing. |
