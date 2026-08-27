# EmptyCosmosLatentVideo

EmptyCosmosLatentVideo 會建立一個具有指定維度的空潛在影片張量。它會產生一個零填充的潛在表示，可作為影片生成工作流程的起點，並具有可設定的寬度、高度、長度和批次大小參數。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `寬度` | 潛在影片的寬度（像素）（預設：1280，增量為 16） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 潛在影片的高度（像素）（預設：704，增量為 16） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 潛在影片的影格數（預設：121，增量為 8） | INT | 是 | 1 to MAX_RESOLUTION |
| `批次大小` | 批次中要生成的潛在影片數量（預設：1） | INT | 否 | 1 至 4096 |

注意：潛在張量在高度和寬度上均以 8 倍因子進行空間下採樣，並包含 16 個通道。潛在時間影格數的計算方式為 `((length - 1) // 8) + 1`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `samples` | 生成的空潛在影片張量，內含零值 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
