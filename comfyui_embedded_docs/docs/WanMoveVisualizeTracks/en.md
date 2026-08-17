# WanMoveVisualizeTracks

The WanMoveVisualizeTracks node draws motion tracking data onto a sequence of images or video frames. It places a circle at the current position of each tracked point and draws a fading path line showing where the point has moved over recent frames. If no track data is provided, the input images are returned unchanged.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `images` | The sequence of input images or video frames on which the tracks will be visualized. | IMAGE | Yes | - |
| `tracks` | The motion tracking data containing point positions and visibility information. If not provided, the input images pass through unchanged. | TRACKS | No | - |
| `line_resolution` | The number of previous frames to use when drawing the trailing path line for each track (default: 24). | INT | Yes | 1 - 1024 |
| `circle_size` | The size of the circle drawn at the current position of each tracked point (default: 12). | INT | Yes | 1 - 128 |
| `opacity` | The opacity of the drawn track overlays (default: 0.75). | FLOAT | Yes | 0.0 - 1.0 |
| `line_width` | The width of the lines used to draw the track paths (default: 16). | INT | Yes | 1 - 128 |

**Note:** If the number of input images does not match the number of frames in the provided `tracks` data, the input image sequence is repeated to align with the track data.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `IMAGE` | The sequence of images with the motion tracking data drawn as overlays. If no `tracks` were provided, the original input images are returned unchanged. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveVisualizeTracks/en.md)

---
**Source fingerprint (SHA-256):** `d94bfde28dfdad682edcc81b1c63408f1352e0dbc94af4d043d750e8cd4c099b`
