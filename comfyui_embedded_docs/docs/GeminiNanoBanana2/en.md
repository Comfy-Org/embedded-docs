# Nano Banana 2

This node generates or edits images synchronously using Google's Vertex AI Gemini model (Nano Banana 2 / Gemini 3.1 Flash Image). It sends a text prompt, along with optional reference images or files, to the API and returns the generated image, any accompanying text, and optionally an image from the model's thinking process.

## Inputs

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Text prompt describing the image to generate or the edits to apply. Include any constraints, styles, or details the model should follow. Must contain at least one non-whitespace character. | STRING | Yes | N/A |
| `model` | The specific Gemini model to use for image generation. The only available option maps to the `gemini-3.1-flash-image-preview` model. | COMBO | Yes | `"Nano Banana 2 (Gemini 3.1 Flash Image)"` |
| `seed` | When the seed is fixed to a specific value, the model makes a best effort to provide the same response for repeated requests. Deterministic output isn't guaranteed. Also, changing the model or parameter settings, such as the temperature, can cause variations in the response even when you use the same seed value. By default, a random seed value is used. (default: 42) | INT | Yes | 0 to 18446744073709551615 |
| `aspect_ratio` | If set to 'auto', matches your input image's aspect ratio; if no image is provided, a 16:9 square is usually generated. (default: "auto") | COMBO | Yes | `"auto"`<br>`"1:1"`<br>`"2:3"`<br>`"3:2"`<br>`"3:4"`<br>`"4:3"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"16:9"`<br>`"21:9"` |
| `resolution` | Target output resolution. For 2K/4K the native Gemini upscaler is used. | COMBO | Yes | `"1K"`<br>`"2K"`<br>`"4K"` |
| `response_modalities` | Determines the type of content the model returns: `IMAGE` returns the image only, `IMAGE+TEXT` also returns the model's reasoning text. (advanced) | COMBO | Yes | `"IMAGE"`<br>`"IMAGE+TEXT"` |
| `thinking_level` | Controls the depth of the model's reasoning process. | COMBO | Yes | `"MINIMAL"`<br>`"HIGH"` |
| `images` | Optional reference image(s). To include multiple images, use the Batch Images node (up to 14). | IMAGE | No | Up to 14 images |
| `files` | Optional file(s) to use as context for the model. Accepts inputs from the Gemini Generate Content Input Files node. | GEMINI_INPUT_FILES | No | N/A |
| `system_prompt` | Foundational instructions that dictate an AI's behavior. (default: built-in instructions that require the model to always produce an image) (advanced) | STRING | No | N/A |

**Note:** The `images` input accepts a maximum of 14 images; providing more raises an error. When more than 10 reference images are provided, the first 10 are sent as file URLs and the remaining images are sent as inline data. The `prompt` must not be empty after removing whitespace. This node is marked as deprecated.

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image` | The primary image generated or edited by the model. | IMAGE |
| `string` | Any text content returned by the model. | STRING |
| `thought_image` | First image from the model's thinking process. Only available with thinking_level HIGH and IMAGE+TEXT modality. | IMAGE |

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNanoBanana2/en.md)

---
**Source fingerprint (SHA-256):** `d781c92f04d420985f8a5a593eb5f28f1f7b2af13abd11f2a7f6f285edcd9900`
