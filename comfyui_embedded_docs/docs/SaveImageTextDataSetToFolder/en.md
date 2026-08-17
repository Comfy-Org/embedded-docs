# Save Image-Text (to Folder)

Save Image-Text (to Folder) is an output node that saves a dataset of paired images and text captions to a folder inside ComfyUI's output directory. Each image is saved as a PNG file, and when captions are provided, a matching TXT file with the same base name is created for each image. This is useful for building organized datasets of generated images and their descriptions.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `images` | List of images to save. | IMAGE | Yes | - |
| `texts` | List of text captions to save. This input is optional. | STRING | No | - |
| `folder_name` | Name of the folder to save images to (inside output directory). (default: "dataset") | STRING | Yes | - |
| `filename_prefix` | Prefix for saved image filenames. (default: "image") | STRING | Yes | - |
| `mode` | Whether to overwrite existing files or increment filenames to avoid overwriting. (default: "overwrite") | COMBO | Yes | "overwrite"<br>"increment" |

**Note:** The `images` input is a list. The `texts` input is optional; if provided, it should be a list of text captions. Captions are paired with the images in order, and each caption is saved as a UTF-8 `.txt` file with the same base name as its paired image (for example, `image_00000.txt` for `image_00000.png`). If there are fewer captions than images, the remaining images are saved without captions; any extra captions are ignored.

Inputs with default values (`folder_name`, `filename_prefix`, `mode`) do not need to be connected; their default values are used automatically.

When `mode` is set to `overwrite` (the default), images are saved with names like `image_00000.png`, replacing any existing files with the same name. When `mode` is set to `increment`, an automatically increasing counter is added to the filenames so existing files are not overwritten.

The `folder_name` value must resolve to a location inside ComfyUI's output directory. Folder names that try to escape the output directory (for example, using `..`) are rejected.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| - | This node has no outputs. It saves files directly to the filesystem. | - |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/en.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
