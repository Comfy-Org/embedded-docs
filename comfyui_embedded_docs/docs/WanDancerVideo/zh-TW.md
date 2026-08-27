# WanDancerVideo

WanDancerVideo 節點為使用 WanDancer 模型進行影片生成準備條件資料和空的潛在張量。它將可選的起始影像、遮罩、CLIP 視覺嵌入和音訊特徵附加到正向和負向條件上，以便它們引導生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向條件。 | CONDITIONING | 是 |  |
| `negative` | 用於引導影片生成的負向條件。 | CONDITIONING | 是 |  |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE。 | VAE | 是 |  |
| `寬度` | 生成的影片寬度（像素）。預設值：480。 | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `高度` | 生成的影片高度（像素）。預設值：832。 | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `長度` | 生成的影片幀數。對於 WanDancer 應保持為 149（預設值：149）。 | INT | 是 | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | 第一幀的 CLIP 視覺嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `clip_vision_output_ref` | 參考影像的 CLIP 視覺嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `起始圖像` | 要編碼的初始影像，可以是任意數量的幀。 | IMAGE | 否 |  |
| `遮罩` | 起始影像的影像條件遮罩。白色區域保留，黑色區域生成。用於局部生成。 | MASK | 否 |  |
| `audio_encoder_output` | 音訊編碼器輸出，提供音訊特徵、幀率和注入比例值；當提供時，會附加到條件上。 | AUDIO_ENCODER_OUTPUT | 否 |  |

### 參數行為說明

- `start_image` 是可選的。當提供時，它會被調整為 `width` 和 `height` 指定的大小，由 `vae` 編碼，並附加到正向和負向條件上。如果 `start_image` 的幀數多於 `length`，多餘的幀會被丟棄。如果少於 `length`，缺少的幀會以零值填充。
- `mask` 只有在同時提供 `start_image` 時才有效。白色區域被保留，黑色區域被生成。
- `clip_vision_output_ref` 只有在同時提供 `clip_vision_output` 時才有效。
- 當提供 `audio_encoder_output` 時，它會將音訊嵌入、幀率和注入比例附加到正向和負向條件上。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 帶有任何附加起始影像潛在、遮罩、CLIP 視覺或音訊資料的正向條件。 | CONDITIONING |
| `negative` | 帶有任何附加起始影像潛在、遮罩、CLIP 視覺或音訊資料的負向條件。 | CONDITIONING |
| `latent` | 一個空的潛在張量，大小符合請求的影片長度、高度和寬度。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
