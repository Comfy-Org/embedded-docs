# HunyuanImageToVideo

HunyuanImageToVideo 節點會使用 Hunyuan 影片模型將影像轉換為影片潛在表徵。此節點接收條件輸入與選用的起始影像，以生成可供影片生成模型進一步處理的影片潛在表徵。此節點支援不同的引導類型，以控制起始影像影響影片生成流程的方式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `正向` | 用於引導影片生成的正向條件輸入 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `寬度` | 輸出影片的寬度，以像素為單位（預設：848，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 輸出影片的高度，以像素為單位（預設：480，步長：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 輸出影片的影格數（預設：53，步長：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 同時生成的影片數量（預設：1） | INT | 是 | 1 至 4096 |
| `引導類型` | 將起始影像納入影片生成的方法（預設："v1 (concat)"）。進階選項 | COMBO | 是 | "v1 (concat)"<br>"v2 (replace)"<br>"custom" |
| `起始影像` | 選用的起始影像（或影像序列），用於初始化影片生成。只會使用前 `length` 個影格以及前 3 個色彩通道 | IMAGE | 否 | - |

**注意：** 當提供 `start_image` 時，節點會根據所選的 `guidance_type` 使用不同的引導方法：

- "v1 (concat)"：將影像潛在表徵與影片潛在表徵串接，並套用遮罩將影像混合到影片中
- "v2 (replace)"：以影像潛在表徵取代初始影片影格，並套用雜訊遮罩
- "custom"：使用影像作為引導用的參考潛在表徵

若未提供 `start_image`，則不會加入引導條件，且會以全零區塊的形式傳回該潛在表徵。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 修改後的正向條件；當提供 `start_image` 時會套用影像引導 | CONDITIONING |
| `latent` | 可供影片生成模型進一步處理的影片潛在表徵 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0ed00d59513492f31760a18ce3b0edf10b64cad848ba52c4e47d5f61fae9accc`
