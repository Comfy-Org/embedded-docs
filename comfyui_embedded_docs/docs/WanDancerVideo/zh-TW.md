# WanDancerVideo

WanDancerVideo 為使用 WanDancer 模型進行影片生成，準備 conditioning 資料和一個空的 latent 張量。它接收正向與負向 conditioning，並可選擇性地將它們與起始影像、遮罩、CLIP vision 嵌入和音訊特徵結合，以控制生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向 conditioning。 | CONDITIONING | 是 |  |
| `negative` | 用於引導影片生成的負向 conditioning。 | CONDITIONING | 是 |  |
| `vae` | 用於將起始影像編碼到潛在空間的 VAE。 | VAE | 是 |  |
| `width` | 生成影片的寬度（像素）（預設值：480）。 | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `height` | 生成影片的高度（像素）（預設值：832）。 | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `length` | 生成影片的幀數。對於 WanDancer 應保持為 149（預設值：149）。 | INT | 是 | 1 to MAX_RESOLUTION (step: 4) |
| `clip_vision_output` | 用於第一幀的 CLIP vision 嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `clip_vision_output_ref` | 用於參考影像的 CLIP vision 嵌入。 | CLIP_VISION_OUTPUT | 否 |  |
| `start_image` | 要編碼的起始影像，可以是任意數量的幀。 | IMAGE | 否 |  |
| `mask` | 用於起始影像的影像 conditioning 遮罩。白色區域保留，黑色區域生成。用於局部生成。 | MASK | 否 |  |
| `audio_encoder_output` | 來自音訊編碼器的輸出，提供音訊特徵、FPS 和音訊注入比例，用於音訊條件生成。 | AUDIO_ENCODER_OUTPUT | 否 |  |

**參數限制說明：**
- 當提供 `start_image` 時，它會被調整為 `width` × `height`，限制為 `length` 幀，並編碼成一個 latent，與 concat 遮罩一起附加到兩個 conditionings 上。
- `mask` 僅在同時提供 `start_image` 時才生效。在遮罩中，白色區域保留，黑色區域生成。當未提供 `mask` 時，起始影像區域用作 conditioning 引導，其餘幀則被生成。
- `clip_vision_output_ref` 僅在提供 `clip_vision_output` 時套用。
- `audio_encoder_output` 將音訊特徵、FPS 和音訊注入比例（預設值：1.0）附加到兩個 conditionings 上。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 附加了任何額外資料（concat latent、CLIP vision、音訊）的正向 conditioning。 | CONDITIONING |
| `negative` | 附加了任何額外資料（concat latent、CLIP vision、音訊）的負向 conditioning。 | CONDITIONING |
| `latent` | 一個空的 latent 張量，其維度與指定的影片長度、高度和寬度相符。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
