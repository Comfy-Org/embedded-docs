This node specializes in refining the encoding of text inputs using CLIP models, enhancing the conditioning for generative tasks by incorporating aesthetic scores and dimensions.

## Inputs

| Parameter | Data Type | Description |
| --- | --- | --- |
| `clip` | `CLIP` | A CLIP model instance used for text tokenization and encoding, central to generating the conditioning. |
| `ascore` | `FLOAT` | The aesthetic score parameter influences the conditioning output by providing a measure of aesthetic quality. |
| `width` | `INT` | Specifies the width of the output conditioning, affecting the dimensions of the generated content. |
| `height` | `INT` | Determines the height of the output conditioning, influencing the dimensions of the generated content. |
| `text` | `STRING` | The text input to be encoded, serving as the primary content descriptor for conditioning. |

## Outputs

| Parameter | Data Type | Description |
| --- | --- | --- |
| `CONDITIONING` | CONDITIONING | The refined conditioning output, enriched with aesthetic scores and dimensions for enhanced content generation. |
