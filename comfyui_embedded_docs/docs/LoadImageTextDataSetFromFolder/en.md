# Load Image-Text (from Folder)

This node loads a dataset of pairs of images and text captions from a specified folder and returns them as a list. Supported formats: PNG, JPG, JPEG, WEBP. For each image file, the node automatically looks for a matching `.txt` file with the same base name to use as its caption. The node also supports a folder structure where subfolder names begin with a number prefix (such as `10_folder_name`), which causes the images inside that subfolder to be repeated that many times in the output.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `folder` | The folder to load images and text captions from. The available options are the subdirectories within ComfyUI's input directory. | COMBO | Yes | *Dynamically loaded from `folder_paths.get_input_subfolders()`* |

**Note:** The node expects a specific file structure. For each image file (`.png`, `.jpg`, `.jpeg`, `.webp`), it will look for a `.txt` file with the same name to use as a caption. If a caption file is not found, an empty string is used. The node also supports a special structure where a subfolder's name begins with a number and an underscore (e.g., `5_cats`), which will cause all images inside that subfolder to be repeated that number of times in the final output list. The selected folder must be inside ComfyUI's input directory; folder names that resolve outside of it are rejected.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `images` | A list of loaded image tensors. | IMAGE |
| `texts` | A list of text captions corresponding to each loaded image. | STRING |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/en.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
