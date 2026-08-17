# Save Video

The SaveVideo node saves an input video to your ComfyUI output directory. It lets you choose the filename prefix, the video format, and the codec, and it automatically creates a unique file name by adding a counter. By default, the node also stores workflow metadata in the saved video.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `codec` | The codec to use for the video. Selecting `h264` reveals additional encoding options (default: "auto"). | DYNAMIC_COMBO | Yes | "auto"<br>"h264" |
| `video` | The video to save. | VIDEO | Yes | - |
| `filename_prefix` | The prefix for the file to save. This may include formatting information such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%` to include values from nodes (default: "video/ComfyUI"). | STRING | Yes | - |
| `format` | The format to save the video as. This determines the file extension of the saved video (default: "auto"). | COMBO | Yes | "auto"<br>"mp4"<br>"webm"<br>"mkv"<br>"gif" |

### h264 Inputs

These inputs appear when `codec` is set to `h264`.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `encoding` | The encoding mode for H.264. Automatic preserves compatible H.264 streams. Re-encode applies a custom CRF (default: "auto"). | DYNAMIC_COMBO | No | "auto"<br>"re-encode" |
| `crf` | Lower values produce higher quality and larger files. Only available when `encoding` is set to `re-encode` (default: 23.0). | FLOAT | Yes (only when `encoding` is `re-encode`) | 0.0 to 51.0 (step: 1.0) |

Note: If the `filename_prefix` includes folders, for example `video/ComfyUI`, the video is saved inside that subfolder of the output directory. The file name is created from the prefix with an added counter, for example `ComfyUI_00001_.mp4`, so existing files are not overwritten.

Note: When metadata is enabled, the node embeds the workflow prompt and extra metadata in the saved video. Metadata can be disabled by starting ComfyUI with the `--disable-metadata` argument.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `video` | The video that was saved, passed through from the input. | VIDEO |
| `ui` | A preview of the saved video file, including the file path and subfolder information for display in the UI. | PREVIEW_VIDEO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/en.md)

---
**Source fingerprint (SHA-256):** `c1fd5ac1043f0811951136b2d09cd59840b0c542079da9ed04c17cca7c02562b`
