# EmptyAceStep1.5LatentAudio

## 概述

Empty Ace Step 1.5 Latent Audio 節點會建立一個專為音訊處理設計的空潛在張量。它會生成指定時長與批次大小的無聲音訊潛在表示，可作為 ComfyUI 中音訊生成工作流程的起點。此節點會根據輸入的秒數與固定的取樣率來計算潛在長度。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `seconds` | 要生成的音訊時長，單位為秒（預設值：120.0）。 | FLOAT | 是 | 1.0 - 1000.0 |
| `batch_size` | 批次中的潛在影像數量（預設值：1）。 | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個代表無聲音訊的空潛在張量，其類型識別碼為 "audio"。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8d2b0b8ea110362d5e43a72a27df0ff2012a8577fbaa4fef2bd7905c9c64bd6a`
