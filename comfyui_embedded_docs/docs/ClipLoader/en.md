This node is primarily used for loading CLIP text encoder models independently.
The model files can be detected in the following paths:

- "ComfyUI/models/text_encoders/"
- "ComfyUI/models/clip/"

> If you save a model after ComfyUI has started, you'll need to refresh the ComfyUI frontend to get the latest model file path list

Supported model formats:

- `.ckpt`
- `.pt`
- `.pt2`
- `.bin`
- `.pth`
- `.safetensors`
- `.pkl`
- `.sft`

For more details on the latest model file loading, please refer to [folder_paths](https://github.com/comfyanonymous/ComfyUI/blob/master/folder_paths.py)

## Inputs

| Parameter     | Data Type     | Description |
|---------------|---------------|-------------|
| `clip_name`   | COMBO[STRING] | Specifies the name of the CLIP model to be loaded. This name is used to locate the model file within a predefined directory structure. |
| `type`        | COMBO[STRING] | Determines the type of CLIP model to load. As ComfyUI supports more models, new types will be added here. Please check the `CLIPLoader` class definition in [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py) for details. |
| `device`      | COMBO[STRING] | Choose the device for loading the CLIP model. `default` will run the model on GPU, while selecting `CPU` will force loading on CPU. |

### Device Options Explained

**When to choose "default":**

- Have sufficient GPU memory
- Want the best performance
- Let the system optimize memory usage automatically

**When to choose "cpu":**

- Insufficient GPU memory
- Need to reserve GPU memory for other models (like UNet)
- Running in a low VRAM environment
- Debugging or special purpose needs

**Performance Impact**

Running on CPU will be much slower than GPU, but it can save valuable GPU memory for other more important model components. In memory-constrained environments, putting the CLIP model on CPU is a common optimization strategy.

### Supported Combinations

| Model Type | Corresponding Encoder |
|------------|---------------------|
| stable_diffusion | clip-l |
| stable_cascade | clip-g |
| sd3 | t5 xxl/ clip-g / clip-l |
| stable_audio | t5 base |
| mochi | t5 xxl |
| cosmos | old t5 xxl |
| lumina2 | gemma 2 2B |
| wan | umt5 xxl |

As ComfyUI updates, these combinations may expand. For details, please refer to the `CLIPLoader` class definition in [node.py](https://github.com/comfyanonymous/ComfyUI/blob/master/nodes.py)

## Outputs

| Parameter | Data Type | Description |
|-----------|-----------|-------------|
| `clip`    | CLIP      | The loaded CLIP model, ready for use in downstream tasks or further processing. |

## Additional Notes

CLIP models play a core role as text encoders in ComfyUI, responsible for converting text prompts into numerical representations that diffusion models can understand. You can think of them as translators, responsible for translating your text into a language that large models can understand. Of course, different models have their own "dialects," so different CLIP encoders are needed between different architectures to complete the text encoding process.
