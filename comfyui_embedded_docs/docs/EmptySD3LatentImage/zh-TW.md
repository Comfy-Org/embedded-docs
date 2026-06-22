# EmptySD3LatentImage

## 概述

EmptySD3LatentImage 節點會建立一個專為 Stable Diffusion 3 模型格式化的空白潛在影像張量。它會產生一個填充為零的張量，其維度與結構符合 SD3 管線的預期。這通常用作影像生成工作流程的起點。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 輸出潛在影像的寬度（像素），預設值：1024 | INT | 是 | 16 至 MAX_RESOLUTION (步長: 16) |
| `高度` | 輸出潛在影像的高度（像素），預設值：1024 | INT | 是 | 16 至 MAX_RESOLUTION (步長: 16) |
| `批次大小` | 批次中要生成的潛在影像數量，預設值：1 | INT | 是 | 1 至 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個包含空白樣本的潛在張量，具有 SD3 相容的維度。該張量有 16 個通道，相較於輸入的寬度和高度，空間維度會縮小 8 倍。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `21eb5b6385b9b0db95d48fa2f4b85eafe44f865af11ee194945ab7ffe54b6acc`
