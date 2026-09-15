# EmptyHunyuanImageLatent

EmptyHunyuanImageLatent 節點會為 Hunyuan 圖像生成模型建立一個全為零的空白潛空間。它會依據給定的 `width`、`height` 與批次大小產生一個空的起始潛空間，之後可傳遞至工作流程中的下游節點。此潛空間張量包含 64 個通道，且每個空間維度等於對應的像素維度除以 32。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `寬度` | 產生的潛空間圖像寬度（以像素為單位，預設值：2048，步長：32） | INT | 是 | 64 至 MAX_RESOLUTION |
| `高度` | 產生的潛空間圖像高度（以像素為單位，預設值：2048，步長：32） | INT | 是 | 64 至 MAX_RESOLUTION |
| `批次大小` | 單一批次中要產生的潛空間樣本數量（預設值：1） | INT | 是 | 1 至 4096 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `LATENT` | 一個空的潛空間張量，包含 64 個通道，且維度為高度 ÷ 32 乘以寬度 ÷ 32，可供 Hunyuan 圖像處理使用 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
