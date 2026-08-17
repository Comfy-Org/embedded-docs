# WanInfiniteTalkToVideo

The WanInfiniteTalkToVideo node generates a talking-head video clip from audio. It conditions a video diffusion model on audio features from one or two speakers, optionally uses a start image or previous frames as context, and returns a patched model, conditioning, and a latent video for sampling.

## Inputs

### Common Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `mode` | The audio mode. Selecting `"single_speaker"` uses one audio input. Selecting `"two_speakers"` adds the second speaker inputs listed below. | DYNAMIC_COMBO | Yes | `"single_speaker"`<br>`"two_speakers"` |
| `model` | The base video diffusion model to patch. | MODEL | Yes | - |
| `model_patch` | The model patch containing the audio projection layers. | MODELPATCH | Yes | - |
| `positive` | The positive conditioning used to guide video generation. | CONDITIONING | Yes | - |
| `negative` | The negative conditioning used to guide video generation. | CONDITIONING | Yes | - |
| `vae` | The VAE used to encode images and previous frames into latent space. | VAE | Yes | - |
| `width` | The width of the generated video in pixels, in steps of 16. (default: 832) | INT | Yes | 16 - MAX_RESOLUTION (step 16) |
| `height` | The height of the generated video in pixels, in steps of 16. (default: 480) | INT | Yes | 16 - MAX_RESOLUTION (step 16) |
| `length` | The number of frames to generate. (default: 81) | INT | Yes | 1 - MAX_RESOLUTION (step 4) |
| `audio_encoder_output_1` | The audio encoder output for the first speaker, containing the audio features used for conditioning. | AUDIOENCODEROUTPUT | Yes | - |
| `start_image` | Optional starting image used to initialize the beginning of the video. It is resized to `width` and `height`. | IMAGE | No | - |
| `clip_vision_output` | Optional CLIP vision output added to both positive and negative conditioning. | CLIPVISIONOUTPUT | No | - |
| `motion_frame_count` | Number of previous frames to use as motion context. (default: 9) | INT | Yes | 1 - 33 (step 1) |
| `audio_scale` | Scaling factor applied to the audio conditioning. (default: 1.0) | FLOAT | Yes | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | Optional previous video frames used to extend an existing sequence. The node uses the last `motion_frame_count` frames as motion context. | IMAGE | No | - |

### Single Speaker Inputs

Selecting `single_speaker` does not add any additional inputs.

### Two Speakers Inputs

These inputs are available when `mode` is `"two_speakers"`.

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | The audio encoder output for the second speaker. When supplied, `mask_1` and `mask_2` must also be supplied. | AUDIOENCODEROUTPUT | No | - |
| `mask_1` | Mask for the first speaker, required if using two audio inputs. | MASK | No | - |
| `mask_2` | Mask for the second speaker, required if using two audio inputs. | MASK | No | - |

**Parameter Constraints:**

- If `audio_encoder_output_2` is provided, both `mask_1` and `mask_2` must also be provided.
- If both `mask_1` and `mask_2` are provided, `audio_encoder_output_2` must also be provided.
- If `previous_frames` is provided, it must contain at least as many frames as specified by `motion_frame_count`.

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `model` | The patched model with audio conditioning and sampling wrappers applied. | MODEL |
| `positive` | The positive conditioning, potentially modified with start image or CLIP vision context. | CONDITIONING |
| `negative` | The negative conditioning, potentially modified with start image or CLIP vision context. | CONDITIONING |
| `latent` | A zero-initialized latent tensor representing the video to be generated. | LATENT |
| `trim_image` | The number of frames to trim from the start when extending from previous frames; 0 when starting a new sequence. | INT |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/en.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
