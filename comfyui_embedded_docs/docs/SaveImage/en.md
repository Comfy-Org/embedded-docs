# Save Image

The SaveImage node saves the images it receives to your `ComfyUI/output` directory. It saves each image as a PNG file and can embed workflow metadata, such as the prompt, into the saved file for future reference.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `images` | The images to save. | IMAGE | Yes | - |
| `filename_prefix` | The prefix for the file to save. This may include formatting information such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%` to include values from nodes (default: "ComfyUI"). | STRING | Yes | - |
| `prompt` | Hidden input, provided automatically by ComfyUI: the prompt data embedded as metadata in the saved PNG file. | PROMPT | No | - |
| `extra_pnginfo` | Hidden input, provided automatically by ComfyUI: additional workflow information embedded as metadata in the saved PNG file. | EXTRA_PNGINFO | No | - |

Each image is saved as a PNG file. In the saved filename, `%batch_num%` in the prefix is replaced with the image's batch number, and a zero-padded counter is appended.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `images` | The same images that were saved, passed through so they can be used by other nodes. | IMAGE |
| `ui` | UI result containing a list of the saved images with their filenames, subfolders, and type, displayed in the ComfyUI interface. | UI_RESULT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/en.md)

---
**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`
