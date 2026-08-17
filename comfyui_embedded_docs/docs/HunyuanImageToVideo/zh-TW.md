# HunyuanImageToVideo

HunyuanImageToVideo 節點使用 Hunyuan 影片模型將影像轉換為影片潛在表示。它接收 conditioning 輸入與可選的起始影像，以產生可供影片生成模型進一步處理的影片潛在變數。此節點支援不同的引導類型，用以控制起始影像如何影響影片生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向 conditioning 輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片的寬度（像素）（預設值：848，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `height` | 輸出影片的高度（像素）（預設值：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `length` | 輸出影片的幀數（預設值：53，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `batch_size` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `guidance_type` | 將起始影像納入影片生成的方法（預設值："v1 (concat)"） | COMBO | 是 | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `start_image` | 用於初始化影片生成的可選起始影像 | IMAGE | 否 | - |

**注意：** 當提供了 `start_image` 時，節點會根據所選的 `guidance_type` 使用不同的引導方法：

- "v1 (concat)"：將影像潛在變數與影片潛在變數串接，並套用遮罩以將影像混合至影片中
- "v2 (replace)"：以影像潛在變數取代初始影片幀，並套用雜訊遮罩
- "custom"：將影像用作引導的參考潛在變數

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 當提供 `start_image` 時，已套用影像引導的修改後正向 conditioning | CONDITIONING |
| `latent` | 可交由影片生成模型進一步處理的影片潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
