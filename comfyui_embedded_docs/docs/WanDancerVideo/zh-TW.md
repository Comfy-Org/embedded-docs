WanDancerVideo 節點為使用 WanDancer 模型進行影片生成準備條件化資料和空的潛在張量。它將正向和負向條件化與可選輸入（如起始影像、遮罩、CLIP 視覺嵌入和音訊特徵）結合，以控制生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 引導影片生成的正向條件化。 | CONDITIONING | 是 |  |
| `negative` | 引導影片生成的負向條件化。 | CONDITIONING | 是 |  |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE。 | VAE | 是 |  |
| `寬度` | 生成影片的寬度（像素），預設值：480。 | INT | 是 | 16 至 MAX_RESOLUTION（步長：16） |
| `高度` | 生成影片的高度（像素），預設值：832。 | INT | 是 | 16 至 MAX_RESOLUTION（步長：16） |
| `長度` | 生成影片的幀數。對於 WanDancer 應保持為 149（預設值：149）。 | INT | 是 | 1 至 MAX_RESOLUTION（步長：4） |
| `clip_vision_output` | 第一幀的 CLIP 視覺嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `clip_vision_output_ref` | 參考影像的 CLIP 視覺嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `起始圖像` | 要編碼的初始影像。可以是任意數量的幀，最多不超過指定的 `長度`。 | IMAGE | 否 |  |
| `遮罩` | 起始影像的影像條件化遮罩。白色區域保留，黑色區域生成。用於局部生成。 | MASK | 否 |  |
| `audio_encoder_output` | 音訊編碼器的輸出，提供音訊特徵、fps 和注入比例，用於音訊條件化生成。 | AUDIO_ENCODER_OUTPUT | 否 |  |

**參數限制說明：**
- `start_image` 和 `mask` 輸入為可選，但可一起使用。當提供 `start_image` 時，它會被編碼並與潛在張量串接。如果也提供了 `mask`，則控制起始影像的哪些部分被保留（白色）以及哪些部分被重新生成（黑色）。如果未提供 `mask`，則整個起始影像區域將用作條件化引導。
- `clip_vision_output` 和 `clip_vision_output_ref` 輸入為可選，可一起使用，為第一幀和參考影像提供視覺上下文。
- `audio_encoder_output` 輸入為可選，提供音訊特徵用於音訊條件化生成。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 附加了任何額外資料（串接潛在張量、CLIP 視覺、音訊）的正向條件化。 | CONDITIONING |
| `negative` | 附加了任何額外資料（串接潛在張量、CLIP 視覺、音訊）的負向條件化。 | CONDITIONING |
| `latent` | 一個空的潛在張量，其維度與指定的影片長度、高度和寬度相符。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7ab1b4662eb8d780295ea3a3e3139c64d81e03a979a293a481f82deaf1fc2f7e`
