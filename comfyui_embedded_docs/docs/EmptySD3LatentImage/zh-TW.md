# EmptySD3LatentImage

EmptySD3LatentImage 建立一個專為 Stable Diffusion 3 模型格式化的空白潛在影像張量。它會產生一個充滿零的張量，其維度與結構符合 SD3 流程的預期。這通常用作影像生成工作流程的起點。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 輸出潛在影像的寬度（以像素為單位）（預設值：1024） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `高度` | 輸出潛在影像的高度（以像素為單位）（預設值：1024） | INT | 是 | 16 to MAX_RESOLUTION (step: 16) |
| `批次大小` | 批次中產生的潛在影像數量（預設值：1） | INT | 是 | 1 至 4096 |

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `LATENT` | 一個包含空白樣本的潛在張量，具有與 SD3 相容的維度。該張量有 16 個通道，與輸入寬度和高度相比，空間尺寸縮小為原來的 1/8。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
