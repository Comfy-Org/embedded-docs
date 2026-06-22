# HunyuanVideo15SuperResolution

## 概述

HunyuanVideo15SuperResolution 節點為影片超解析度處理準備條件化資料。它接收影片的潛在表示，並可選地接收起始影像，將其與雜訊增強和 CLIP 視覺資料打包成模型可用於生成更高解析度輸出的格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 將使用潛在資料和增強資料修改的正向條件化輸入。 | CONDITIONING | 是 | N/A |
| `negative` | 將使用潛在資料和增強資料修改的負向條件化輸入。 | CONDITIONING | 是 | N/A |
| `vae` | 用於編碼可選 `起始影像` 的 VAE。若提供 `起始影像` 則為必要。 | VAE | 否 | N/A |
| `起始影像` | 可選的起始影像，用於引導超解析度過程。若提供，將被放大並編碼到條件化潛在表示中。 | IMAGE | 否 | N/A |
| `clip_vision_output` | 可選的 CLIP 視覺嵌入，將添加到條件化資料中。 | CLIP_VISION_OUTPUT | 否 | N/A |
| `latent` | 將納入條件化資料的輸入潛在影片表示。 | LATENT | 是 | N/A |
| `雜訊增強` | 應用於條件化資料的雜訊增強強度（預設值：0.70）。 | FLOAT | 否 | 0.0 - 1.0 |

**注意：** 若您提供 `start_image`，則必須同時連接 `vae` 以進行編碼。`start_image` 將自動放大以匹配輸入 `latent` 所隱含的尺寸。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `negative` | 修改後的正向條件化資料，現包含串聯的潛在表示、雜訊增強及可選的 CLIP 視覺資料。 | CONDITIONING |
| `latent` | 修改後的負向條件化資料，現包含串聯的潛在表示、雜訊增強及可選的 CLIP 視覺資料。 | CONDITIONING |
| `latent` | 輸入的潛在表示未經修改直接傳遞。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f913327a81d034997fa8a485ca4b3691f75ba1d3c5c6e2e73ab107021b58a52a`
