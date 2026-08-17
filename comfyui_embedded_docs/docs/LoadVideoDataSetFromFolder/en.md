# Load Video (from Folder)

Loads all supported video files from a selected folder inside the ComfyUI input directory and returns them as a list of video references. This node returns lazy video references, so frames are decoded only when another node actually needs them. Supported formats: MP4, AVI, MOV, WEBM, MKV, and FLV.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `folder` | The folder containing video files. Select from available subfolders inside the ComfyUI input directory. | COMBO | Yes | All subfolders available in the ComfyUI input directory |

**Note:** The selected folder must contain at least one supported video file. Supported extensions are MP4, AVI, MOV, WEBM, MKV, and FLV. If no supported video files are found, the node raises an error. The folder must resolve to a location inside the ComfyUI input directory; folder names that try to escape it (for example with "..") are rejected with an error.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `videos` | A list of lazy video references, one for each video file in the selected folder. Frames are decoded only when the output is consumed by another node. | VIDEO (list) |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/en.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
