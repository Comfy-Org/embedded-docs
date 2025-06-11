Right-click on the node and select **Open in MaskEditor** from the menu to open the mask editor for the loaded image.

> Official mask editor tutorial: [https://docs.comfy.org/interface/maskeditor](https://docs.comfy.org/interface/maskeditor)

> Uploaded images are uploaded to the *ComfyUI/input* folder by default, and images are loaded from the **input** folder by default.

The Load Image node is designed to load and preprocess images from a specified path. It handles image formats with multiple frames, applies necessary transformations such as rotation based on EXIF data, normalizes pixel values, and optionally generates a mask for images with an alpha channel.

## Usage Steps

1. Drag and drop image files into the ComfyUI interface, or manually copy them to the `ComfyUI/input` folder
2. Add the Load Image node to your workflow
3. Select the image file to load from the `IMAGE` dropdown menu in the node
4. Connect the outputs to subsequent nodes (such as VAEEncode, etc.)

## Supported File Formats

- Common image formats: PNG, JPG, JPEG, BMP, TIFF, WEBP
- Supports images with alpha channels (PNG, TIFF, etc.)
- Supports multi-frame image sequences (GIF, TIFF, etc.)

## Inputs

| Parameter | Data Type | Description |
|-----------|--------------|-------------|
| `IMAGE`   | COMBO[STRING] | The `IMAGE` parameter specifies the identifier of the image to be loaded and processed. It is crucial for determining the path to the image file and subsequently loading the image for transformation and normalization. |

## Outputs

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `IMAGE`   | IMAGE     | The processed image, with pixel values normalized and transformations applied as necessary. It is ready for further processing or analysis. |
| `MASK`    | MASK      | (Optional) Provides a mask for the image, useful when the image includes an alpha channel for transparency. |

## Mask Output Details

- **With Alpha Channel**: Automatically extracts transparency information as a mask
- **Palette mode with transparency**: Converts to RGBA and extracts the mask
- **No transparency**: Generates a default 64x64 empty mask
- Mask value range: 0-1 (0 = transparent, 1 = opaque)

## File Update Mechanism

- The node automatically detects file content changes (via SHA256 hash)
- After replacing a file with the same name, the workflow will reload automatically
- No need to restart ComfyUI to use the updated image
