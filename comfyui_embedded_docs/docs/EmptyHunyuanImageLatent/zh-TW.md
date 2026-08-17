# EmptyHunyuanImageLatent

EmptyHunyuanImageLatent 節點會建立一個具有特定維度的空潛在張量，供 Hunyuan 影像生成模型使用。它會產生一個空白起點，可供工作流程中的後續節點處理。此節點可讓您指定潛在空間的寬度、高度和批次大小。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `width` | 生成的潛在影像寬度（像素）（預設值：2048，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `height` | 生成的潛在影像高度（像素）（預設值：2048，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `batch_size` | 批次中生成的潛在樣本數量（預設值：1） | INT | 是 | 1 to 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `LATENT` | 一個空潛在張量，具有用於 Hunyuan 影像處理的指定維度。該張量有 64 個通道，其空間維度是請求寬度和高度的三十二分之一（1/32）。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
