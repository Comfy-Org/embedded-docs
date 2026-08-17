# Load Video-Text (from Folder)

This node loads a dataset of video-text pairs from a selected subfolder in the ComfyUI input directory and returns them as two lists: videos and text captions. The video entries are lazy references, so frames are decoded only when a downstream node needs them. Supported formats are MP4, AVI, MOV, WEBM, MKV, and FLV. Captions are read from `.txt` files that share the same name as each video file.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `folder` | The folder containing video files and .txt captions. | COMBO | Yes | All subfolders inside the ComfyUI input directory (dynamic list) |

Notes:
- The selected folder must be a subfolder of the ComfyUI input directory; paths that resolve outside of it are rejected.
- If the folder contains no files with a supported video extension, the node raises an error.
- Nested folders whose name starts with a number followed by an underscore (for example `5_classname/`, as used by tools like kohya-ss/sd-scripts) are also supported: each video inside that folder is included in the dataset the number of times given by that prefix.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `videos` | Lazy video references; frames are decoded only when needed downstream. One entry per video file found in the folder. | VIDEO (list) |
| `texts` | List of text captions. One caption per video; if a video has no matching `.txt` file, its caption is an empty string. | STRING (list) |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/en.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
