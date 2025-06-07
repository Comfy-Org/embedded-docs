
**Node Function:** The `Save Image` node is mainly used to save images to the **output** folder in ComfyUI. If you only want to preview the image during the intermediate process rather than saving it, you can use the `Preview Image` node.
Default save location: `ComfyUI/output/`

## Inputs

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `images` | `IMAGE` | The images to be saved. This parameter is crucial as it directly contains the image data that will be processed and saved to disk. |
| `filename_prefix` | STRING   | The filename prefix for images saved to the `ComfyUI/output/` folder. The default is `ComfyUI`, but you can customize it. |

## Right-click Menu Options

After the image generation is complete, right-clicking on the corresponding menu provides the following node-specific options and functions:

| Option Name | Function |
|-------------|----------|
| `Save Image` | Save the image locally |
| `Copy Image` | Copy the image to clipboard |
| `Open Image` | Open the image in a new browser tab |

The saved images are generally in PNG format and include all the image generation data. If you want to use the corresponding workflow for regeneration, you can simply load the corresponding image into ComfyUI to load the workflow.
