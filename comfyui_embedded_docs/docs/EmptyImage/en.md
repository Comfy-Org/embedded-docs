The `EmptyImage` node is designed to generate blank images of specified dimensions and color. It allows for the creation of uniform color images that can serve as backgrounds or placeholders in various image processing tasks.

## Inputs

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `width`   | `INT`      | Specifies the width of the generated image. It determines how wide the image will be. |
| `height`  | `INT`      | Determines the height of the generated image. It affects the vertical size of the image. |
| `batch_size` | `INT` | Indicates the number of images to generate in a single batch. This allows for the creation of multiple images at once. |
| `color`   | `INT`      | Defines the color of the generated image using a hexadecimal value, allowing for customization of the image's appearance. This parameter enables the selection of a wide range of colors. |

## Outputs

| Parameter | Data Type | Description |
|-----------|-------------|-------------|
| `image`   | `IMAGE`    | The output is a tensor representing the generated image or images, with the specified dimensions and color. |
