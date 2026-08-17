# Run Frame Interpolation Model

The Frame Interpolate node creates new frames between existing ones in a sequence of images, effectively increasing the frame rate. It uses an AI model to predict what the intermediate frames should look like, which can be used to create smooth slow-motion effects or to increase the smoothness of a video. For each consecutive pair of frames, the node generates `multiplier - 1` new frames and inserts them between the originals.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `interp_model` | The frame interpolation model to use for generating intermediate frames (for example, RIFE or FILM models) | INTERP_MODEL | Yes | - |
| `images` | A batch of consecutive images (frames) to interpolate between. Requires at least 2 images; if fewer are provided, the node returns the input images unchanged. | IMAGE | Yes | - |
| `multiplier` | The factor by which to multiply the frame count. For example, a multiplier of 2 doubles the number of frames. (default: 2) | INT | Yes | 2 to 16 |

Note: The input image batch must contain at least 2 frames, because interpolation happens between consecutive frame pairs. The total number of frames in the output is `(number of input frames - 1) * multiplier + 1`.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `IMAGE` | A new batch of images with the interpolated frames inserted between the original frames, resulting in a smoother sequence. The total number of output frames is `(number of input frames - 1) * multiplier + 1`. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FrameInterpolate/en.md)

---
**Source fingerprint (SHA-256):** `e0b9dd6ec3b09e665bcc0f95d2b7a0209d9045ba9b96828e46f126e6914f049c`
