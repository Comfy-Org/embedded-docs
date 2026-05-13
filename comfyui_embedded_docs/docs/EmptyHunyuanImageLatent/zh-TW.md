> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/zh-TW.md)

## 概述

EmptyHunyuanImageLatent 節點會建立一個具有特定維度的空潛在張量，用於 Hunyuan 影像生成模型。它會產生一個空白起始點，可透過工作流程中的後續節點進行處理。此節點允許您指定潛在空間的寬度、高度和批次大小。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `寬度` | INT | 是 | 64 至 MAX_RESOLUTION | 生成的潛在影像寬度（像素）（預設值：2048，步長：32） |
| `高度` | INT | 是 | 64 至 MAX_RESOLUTION | 生成的潛在影像高度（像素）（預設值：2048，步長：32） |
| `批次大小` | INT | 是 | 1 至 4096 | 批次中生成的潛在樣本數量（預設值：1） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `LATENT` | LATENT | 一個具有指定維度的空潛在張量，用於 Hunyuan 影像處理 |

---
**Source fingerprint (SHA-256):** `18e920527c88be2648d8cbe4255f693123be4e70a9e21dd379310088a1470834`
