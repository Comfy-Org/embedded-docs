# HunyuanImageToVideo

HunyuanImageToVideo 節點使用 Hunyuan 影片模型將圖片轉換為影片潛在表示。它接收條件化輸入和可選的起始圖片，以生成可進一步由影片生成模型處理的影片潛在表示。該節點支援不同的引導類型，用於控制起始圖片如何影響影片生成過程。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導影片生成的正向條件化輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將圖片編碼到潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度（像素）（預設值：848，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 輸出影片的高度（像素）（預設值：480，步長：16） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 輸出影片的幀數（預設值：53，步長：4） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設值：1） | INT | 是 | 1 至 4096 |
| `引導類型` | 將起始圖片融入影片生成的方法（預設值："v1 (concat)"） | COMBO | 是 | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `起始影像` | 可選的起始圖片，用於初始化影片生成 | IMAGE | 否 | - |

**注意：** 當提供 `start_image` 時，節點會根據所選的 `guidance_type` 使用不同的引導方法：

- "v1 (concat)"：將圖片潛在表示與影片潛在表示連接，並應用遮罩將圖片混合到影片中
- "v2 (replace)"：用圖片潛在表示替換初始影片幀，並應用噪聲遮罩
- "custom"：將圖片用作引導的參考潛在表示

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `正向` | 當提供 start_image 時，應用圖片引導後的修改後正向條件化 | CONDITIONING |
| `潛在空間` | 準備好由影片生成模型進一步處理的影片潛在表示 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e55e935b7955b28b04014359c544a230c51ee91e21170be1ae4f50705d3e7bba`
