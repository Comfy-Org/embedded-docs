# Load Background Removal Model

Loads a background removal model from a file and makes it ready for other nodes to use when removing backgrounds from images. The model file is selected from the available files in the background removal folder.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | The model used to remove backgrounds from images. | COMBO | Yes | List of available model files (sorted list of files in the background_removal folder) |

**Note:** The node raises an error if the selected file does not contain a valid background removal model.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `bg_model` | The loaded background removal model, ready to be used by other nodes for processing images. | BACKGROUND_REMOVAL |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/en.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
