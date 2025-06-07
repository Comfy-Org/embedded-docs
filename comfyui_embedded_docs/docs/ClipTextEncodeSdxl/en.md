This node is designed to encode text inputs using the CLIP model specifically tailored for the SDXL architecture. It focuses on converting textual descriptions into a format that can be effectively utilized for generating or manipulating images, leveraging the capabilities of the CLIP model to understand and process text in the context of visual content.

## Inputs

| Parameter | Data Type | Description |
| --- | --- | --- |
| `clip` | `CLIP` | The CLIP model instance used for encoding the text. It plays a vital role in processing the text input and converting it into a format suitable for image generation or manipulation tasks. |
| `width` | `INT` | Specifies the width of the image in pixels. It determines the dimensions of the output image generated or manipulated. |
| `height` | `INT` | Specifies the height of the image in pixels. It determines the dimensions of the output image generated or manipulated. |
| `crop_w` | `INT` | Defines the width of the crop area in pixels. This parameter is used to crop the image to a specific width before processing. |
| `crop_h` | `INT` | Defines the height of the crop area in pixels. This parameter is used to crop the image to a specific height before processing. |
| `target_width` | `INT` | The target width for the output image after processing. It allows for resizing the image to a desired width. |
| `target_height` | `INT` | The target height for the output image after processing. It allows for resizing the image to a desired height. |
| `text_g` | `STRING` | The global textual description to be encoded. This input is crucial for generating the corresponding visual representations and understanding the content described. |
| `text_l` | `STRING` | The local textual description to be encoded. This input provides additional detail or context to the global description, enhancing the specificity of the generated or manipulated image. |

## Outputs

| Parameter | Data Type | Description |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | The output of the node, which includes the encoded text along with additional information necessary for image generation or manipulation tasks. |
