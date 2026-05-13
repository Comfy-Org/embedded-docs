> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/en.md)

The ByteDance Seedance 2.0 Reference to Video node uses the Seedance 2.0 AI model to create, edit, or extend videos based on your text prompt and provided reference materials. It can use images, videos, and audio as references to guide the generation process, supporting tasks like video editing and extension.

## Inputs

| Parameter | Data Type | Required | Range | Description |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | Yes | `"Seedance 2.0"`<br>`"Seedance 2.0 Fast"` | The AI model to use. Seedance 2.0 is for maximum quality, while Seedance 2.0 Fast is optimized for speed. Selecting a model reveals additional required inputs for `prompt`, `resolution`, `duration`, `ratio`, `generate_audio`, and optional inputs for `reference_images`, `reference_videos`, `reference_audios`, `reference_assets`, and `auto_downscale`. |
| `seed` | INT | No | 0 to 2147483647 | A number used to control whether the node should re-run. The results are non-deterministic regardless of the seed value (default: 0). |
| `watermark` | BOOLEAN | No | `True` / `False` | Whether to add a watermark to the generated video (default: False). |

**Important Constraints:**
*   At least one reference image or video (provided via the `reference_images`, `reference_videos`, or `reference_assets` inputs) is required for the node to work.
*   A maximum of 9 reference images can be used in total (including those from `reference_images` and `reference_assets`).
*   A maximum of 3 reference videos can be used in total (including those from `reference_videos` and `reference_assets`).
*   A maximum of 3 reference audio clips can be used in total (including those from `reference_audios` and `reference_assets`).
*   Each reference video must be at least 1.8 seconds long. The combined duration of all reference videos cannot exceed 15.1 seconds.
*   Each reference audio clip must be at least 1.8 seconds long. The combined duration of all reference audio cannot exceed 15.1 seconds.

## Outputs

| Output Name | Data Type | Description |
|-------------|-----------|-------------|
| `video` | VIDEO | The generated video file. |

---
**Source fingerprint (SHA-256):** `72c8a2f821b9fb9853a4d0428785c432d0852ae562080292817f8a7d52967c7f`
