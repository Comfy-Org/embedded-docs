# Save Image (to Folder) (DEPRECATED)

This node saves a list of images as PNG files to a specified folder inside ComfyUI's output directory. It is deprecated: it is redundant and superseded by the existing Save Image nodes, where the target folder can be specified in the filename prefix. The node writes each received image to disk using a customizable filename prefix, and can either overwrite existing files or generate incremented filenames to avoid overwriting.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `images` | List of images to save. | IMAGE | Yes | N/A |
| `folder_name` | Name of the folder to save images to (inside output directory). The default value is "dataset". | STRING | No | N/A |
| `filename_prefix` | Prefix for saved image filenames. The default value is "image". | STRING | No | N/A |
| `mode` | Whether to overwrite existing files or increment filenames to avoid overwriting. The default value is "overwrite". | COMBO | No | "overwrite"<br>"increment" |

**Note:** The `images` input is a list, meaning it can receive and process multiple images at once. All inputs are received as lists; for `folder_name`, `filename_prefix`, and `mode`, only the first value from the connected list is used. The `folder_name` must resolve to a folder inside ComfyUI's output directory — folder names that escape it (for example by using "..", an absolute path, or a drive letter) are rejected with an error. Images are always saved in PNG format. The `filename_prefix` parameter is an advanced option.

## Outputs

This node does not have any data outputs. It is an output node that performs a save operation to the filesystem.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/en.md)

---
**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`
