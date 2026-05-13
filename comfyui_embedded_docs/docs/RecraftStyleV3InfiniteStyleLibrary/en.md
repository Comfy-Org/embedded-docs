> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/en.md)

This node allows you to select a style from Recraft's Infinite Style Library using a preexisting UUID. It retrieves the style information based on the provided style identifier and returns it for use in other Recraft nodes.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `style_id` | STRING | Yes | Any valid UUID | UUID of style from Infinite Style Library. |

**Note:** The `style_id` input cannot be empty. If an empty string is provided, the node will raise an exception.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `recraft_style` | STYLEV3 | The selected style object from Recraft's Infinite Style Library |

---
**Source fingerprint (SHA-256):** `37d7d9eff1232cc17912c6fca908dc5b8c404c0b6cf0a36e8fecc837ff2a1eea`
