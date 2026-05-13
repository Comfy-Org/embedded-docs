> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/zh-TW.md)

## 概述

EmptyLTXVLatentVideo 節點用於建立一個空的潛在張量以進行影片處理。它會生成一個具有指定維度的空白起始點，可作為影片生成工作流程的輸入。此節點會產生一個以零填充的潛在表示，並包含設定的寬度、高度、長度與批次大小。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `width` | INT | 是 | 64 至 MAX_RESOLUTION | 潛在影片張量的寬度（預設值：768，步長：32） |
| `height` | INT | 是 | 64 至 MAX_RESOLUTION | 潛在影片張量的高度（預設值：512，步長：32） |
| `length` | INT | 是 | 1 至 MAX_RESOLUTION | 潛在影片中的影格數量（預設值：97，步長：8） |
| `batch_size` | INT | 否 | 1 至 4096 | 批次中要生成的潛在影片數量（預設值：1） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `samples` | LATENT | 生成的空白潛在張量，在指定維度中數值皆為零 |

---
**Source fingerprint (SHA-256):** `c3ee9374210e100a074b238ce7ac8b5d2d2d415efd3318c9a6a7c8f7e20bda84`
