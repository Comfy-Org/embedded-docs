# Get Video Components

The Get Video Components node extracts all the main elements from a video file. It separates the video into individual frames, extracts the audio track, and provides the video's framerate, bit depth, and color space information. This allows you to work with each component independently for further processing or analysis.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `video` | The video to extract components from. | VIDEO | Yes | - |

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `images` | The individual frames extracted from the video as separate images. | IMAGE |
| `audio` | The audio track extracted from the video. | AUDIO |
| `fps` | The framerate of the video in frames per second. | FLOAT |
| `bit_depth` | The bit depth of the video. | INT |
| `color_space` | The color space of the video. | COMBO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/en.md)

---
**Source fingerprint (SHA-256):** `ffe8b6c698cb9a855b8796768f068d403448cf56188ce4c5ead21bff30baff6e`
