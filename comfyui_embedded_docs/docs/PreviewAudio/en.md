# Preview Audio

The PreviewAudio node lets you preview audio directly in the interface without saving it to the ComfyUI output directory. It takes audio data as input and displays an audio player widget you can use to listen to the result. If the input audio is None, the node raises an error, which can happen when the source video has no audio track.

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `audio` | The audio data to preview. The node raises an error if the audio is None, which can happen when the source video has no audio track. | AUDIO | Yes | - |

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `audio` | The audio data that was passed through the node. An audio player widget is displayed in the interface for previewing the audio. | AUDIO |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/en.md)

---
**Source fingerprint (SHA-256):** `ccbf9873a16bf1578fe25d178454d782f4f9b37ad5721721bef0aee3ff374f9f`
