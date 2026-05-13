> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/en.md)

This node creates a personal image asset for ByteDance's Seedance 2.0 service. It uploads an input image and registers it within a specified asset group. If no group ID is provided, it will initiate a real-person authentication process in your browser to create a new group before adding the asset.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | Yes | | The image to be registered as a personal asset. |
| `group_id` | STRING | No | | Reuse an existing Seedance asset group ID to skip repeated human verification for the same person. Leave empty to run real-person authentication in the browser and create a new group (default: empty). |

**Image Constraints:**
*   The image width must be between 300 and 6000 pixels.
*   The image height must be between 300 and 6000 pixels.
*   The image aspect ratio must be between 0.4:1 and 2.5:1.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `asset_id` | STRING | The unique identifier for the newly created image asset. |
| `group_id` | STRING | The identifier for the asset group. This will be the provided `group_id` or a newly created one. |

---
**Source fingerprint (SHA-256):** `b8b7b4cbbc16a8bb0102982757496ad4e8140bd87155902668c0be0d8b4d3d98`
