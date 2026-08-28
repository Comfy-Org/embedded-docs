# EmptyLTXVLatentVideo

EmptyLTXVLatentVideo 節點會建立一個用於影片處理的空潛在張量。它會產生一個具備指定寬度、高度、長度與批次大小的空白起點，可作為影片生成工作流程的輸入。此節點會產生一個以零填充的潛在表示，其空間維度為所設定寬度與高度的 32 分之一，幀數則壓縮為原本的 8 分之一。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 潛在影片張量的寬度（預設值：768，步長：32） | INT | 是 | 64 至 MAX_RESOLUTION |
| `高度` | 潛在影片張量的高度（預設值：512，步長：32） | INT | 是 | 64 至 MAX_RESOLUTION |
| `長度` | 潛在影片中的幀數（預設值：97，步長：8） | INT | 是 | 1 至 MAX_RESOLUTION |
| `批次大小` | 一個批次中要生成的潛在影片數量（預設值：1） | INT | 是 | 1 至 4096 |

注意：與輸入維度相比，潛在影片經過壓縮：空間維度（寬度與高度）會除以 32，幀數（長度）會除以 8 並無條件進位至最接近的整數。寬度、高度與長度的步長值有助於讓這些除法保持整除。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `samples` | 生成的空白潛在張量，在指定維度上數值皆為零，空間下採樣比率為 32 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
