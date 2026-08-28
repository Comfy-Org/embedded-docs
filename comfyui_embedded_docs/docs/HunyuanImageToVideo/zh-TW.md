# HunyuanImageToVideo

HunyuanImageToVideo 節點使用 Hunyuan 影片模型將影像轉換為影片潛在表示。它接受條件輸入和可選的起始影像，以產生可供影片生成模型進一步處理的影片潛在。此節點支援不同的引導類型，用於控制起始影像如何影響影片生成過程。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導影片生成的正面條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）（預設值：848，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）（預設值：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 輸出影片的幀數（預設值：53，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `引導類型` | 將起始影像納入影片生成的方法（預設值：「v1 (concat)」）。進階選項 | COMBO | 是 | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `起始影像` | 可選的起始影像（或影像序列），用於初始化影片生成。僅使用前 `length` 幀和前 3 個色彩通道 | IMAGE | 否 | - |

**注意：** 當提供 `start_image` 時，節點會根據選取的 `guidance_type` 使用不同的引導方法：

- "v1 (concat)"：將影像潛在與影片潛在串接，並套用遮罩將影像混合到影片中。
- "v2 (replace)"：以影像潛在取代初始影片幀，並套用雜訊遮罩。
- "custom"：將影像用作引導的參考潛在。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `正向` | 在提供 `start_image` 時，套用影像引導後的修改版正面條件 | CONDITIONING |
| `潛在空間` | 可供影片生成模型進一步處理的影片潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
