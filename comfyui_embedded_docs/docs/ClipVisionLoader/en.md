This node will detect models located in the `ComfyUI/models/clip_vision` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder.

The CLIPVisionLoader node is designed for loading CLIP Vision models from specified paths. It abstracts the complexities of locating and initializing CLIP Vision models, making them readily available for further processing or inference tasks.

## Inputs

| Field       | Comfy dtype | Description                                                                       |
|-------------|-------------|-----------------------------------------------------------------------------------|
| `clip_name` | `COMBO[STRING]` | Specifies the name of the CLIP Vision model to be loaded, used to locate the model file within a predefined directory structure. |

## Outputs

| Field          | Comfy dtype     | Description                                                              |
|----------------|-----------------|--------------------------------------------------------------------------|
| `clip_vision`  | `CLIP_VISION`   | The loaded CLIP Vision model, ready for use in encoding images or performing other vision-related tasks. |
