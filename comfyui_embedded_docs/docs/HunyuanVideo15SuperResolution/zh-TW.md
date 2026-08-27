# HunyuanVideo15SuperResolution

HunyuanVideo15SuperResolution 節點為影片超解析度過程準備 conditioning 資料。它接收影片的潛在表示（latent representation），以及可選的起始影像，並將它們與雜訊增強和 CLIP 視覺資料一起封裝成可供模型用來生成更高解析度輸出的格式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 要使用潛在表示與增強資料修改的正向 conditioning 輸入。 | CONDITIONING | 是 | N/A |
| `negative` | 要使用潛在表示與增強資料修改的負向 conditioning 輸入。 | CONDITIONING | 是 | N/A |
| `vae` | 用於對可選的 `start_image` 進行編碼的 VAE。若提供了 `start_image`，則此為必填。 | VAE | 否 | N/A |
| `起始影像` | 可選的起始影像，用於引導超解析度。若提供，該影像會被放大並編碼到 conditioning 潛在表示中。 | IMAGE | 否 | N/A |
| `clip_vision_output` | 可選的 CLIP 視覺嵌入，用於添加到 conditioning 中。 | CLIP_VISION_OUTPUT | 否 | N/A |
| `latent` | 輸入的潛在影片表示，會併入 conditioning 中。 | LATENT | 是 | N/A |
| `雜訊增強` | 要套用於 conditioning 的雜訊增強強度（預設值：0.70）。這是一個進階參數。 | FLOAT | 否 | 0.0 - 1.0 (step 0.01) |

**注意：** 若您提供 `start_image`，則必須同時連接 `vae` 以便進行編碼。`start_image` 會自動放大至輸入 `latent` 空間尺寸（寬與高）的 16 倍，然後編碼並放入 conditioning 潛在表示中。編碼時僅使用 `start_image` 的 RGB 通道。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向 conditioning，現在包含串接後的潛在表示、雜訊增強，以及可選的 CLIP 視覺資料。 | CONDITIONING |
| `negative` | 修改後的負向 conditioning，現在包含串接後的潛在表示、雜訊增強，以及可選的 CLIP 視覺資料。 | CONDITIONING |
| `latent` | 輸入的潛在表示會原封不動地傳遞出去。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
