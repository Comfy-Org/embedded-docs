# EmptyHunyuanImageLatent

EmptyHunyuanImageLatent 節點會為 Hunyuan 影像生成模型建立空的（填零）潛在空間。它會根據指定的寬度、高度與批次大小，生成一個空白的起始潛在變量，可傳遞給工作流程中的下游節點。此潛在張量具有 64 個通道，其空間維度為寬度與高度各除以 32。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `寬度` | 生成的潛在影像寬度（以像素為單位）（預設值：2048，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `高度` | 生成的潛在影像高度（以像素為單位）（預設值：2048，步長：32） | INT | 是 | 64 to MAX_RESOLUTION |
| `批次大小` | 批次中要生成的潛在樣本數量（預設值：1） | INT | 是 | 1 至 4096 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `LATENT` | 一個空的潛在張量，具有 64 個通道，維度為高度 ÷ 32 × 寬度 ÷ 32，已準備好供 Hunyuan 影像處理使用 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/zh-TW.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
