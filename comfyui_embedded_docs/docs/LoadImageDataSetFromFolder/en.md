# Load Image (from Folder)

This node loads a dataset of images from a selected folder and returns them as a list. The folder must be a subfolder inside ComfyUI's main input directory. Supported image formats are PNG, JPG, JPEG, and WEBP.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `folder` | The folder to load images from. The available options are the subfolders present in ComfyUI's main input directory. Values that resolve outside this directory (for example, using "..") are rejected. | COMBO | Yes | *Multiple options available* — the subfolders present in ComfyUI's input directory |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `images` | List of loaded images. The node loads every valid image file (PNG, JPG, JPEG, WEBP) found in the selected folder and returns them as a list. If the folder contains no supported image files, an error is raised. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/en.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
