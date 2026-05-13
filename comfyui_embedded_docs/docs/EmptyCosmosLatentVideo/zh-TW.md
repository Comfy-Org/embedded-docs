> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/zh-TW.md)

EmptyCosmosLatentVideo 節點會建立一個具有指定維度的空潛在影片張量。它會生成一個填充為零的潛在表示，可作為影片生成工作流程的起點，並可設定寬度、高度、長度與批次大小參數。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `寬度` | INT | 是 | 16 至 MAX_RESOLUTION | 潛在影片的寬度（單位：像素，預設值：1280，必須能被 16 整除） |
| `高度` | INT | 是 | 16 至 MAX_RESOLUTION | 潛在影片的高度（單位：像素，預設值：704，必須能被 16 整除） |
| `長度` | INT | 是 | 1 至 MAX_RESOLUTION | 潛在影片的幀數（預設值：121，必須能被 8 整除） |
| `批次大小` | INT | 否 | 1 至 4096 | 單一批次中生成的潛在影片數量（預設值：1） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `samples` | LATENT | 生成的空潛在影片張量，其值皆為零 |

---
**Source fingerprint (SHA-256):** `f473820af3faf7cb6992ff1959089801e333df395b4007abeb9b504962bfc73b`
