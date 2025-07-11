The `CLIPSave` node is designed for saving CLIP text encoder models in SafeTensors format. This node is part of advanced model merging workflows and is typically used in conjunction with nodes like `CLIPMergeSimple` and `CLIPMergeAdd`. The saved files use the SafeTensors format to ensure security and compatibility.

## Inputs

| Parameter | Data Type | Required | Default Value | Description |
|-----------|-----------|----------|---------------|-------------|
| clip | CLIP | Yes | - | The CLIP model to be saved |
| filename_prefix | STRING | Yes | "clip/ComfyUI" | The prefix path for the saved file |
| prompt | PROMPT | Hidden | - | Workflow prompt information (for metadata) |
| extra_pnginfo | EXTRA_PNGINFO | Hidden | - | Additional PNG information (for metadata) |

## Outputs

This node has no defined output types. It saves the processed files to the `ComfyUI/output/` folder.

### Multi-file Saving Strategy

The node saves different components based on the CLIP model type:

| Prefix Type | File Suffix | Description |
|------------|-------------|-------------|
| `clip_l.` | `_clip_l` | CLIP-L text encoder |
| `clip_g.` | `_clip_g` | CLIP-G text encoder |
| Empty prefix | No suffix | Other CLIP components |

## Usage Notes

1. **File Location**: All files are saved in the `ComfyUI/output/` directory
2. **File Format**: Models are saved in SafeTensors format for security
3. **Metadata**: Includes workflow information and PNG metadata if available
4. **Naming Convention**: Uses the specified prefix plus appropriate suffixes based on model type
