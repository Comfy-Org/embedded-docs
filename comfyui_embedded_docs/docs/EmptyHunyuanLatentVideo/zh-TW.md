# EmptyHunyuanLatentVideo

`EmptyHunyuanLatentVideo` 節點與 `EmptyLatentImage` 節點類似。您可以將其視為用於影片生成的空白畫布，其中寬度、高度和長度定義了畫布的屬性，而批次大小則決定了要建立的畫布數量。此節點會建立準備用於後續影片生成任務的空白畫布。

## 輸入

| 參數 | 說明 | Comfy 類型 |
| --- | --- | --- |
| `寬度` | 影片寬度，預設值 848，最小值 16，最大值 `nodes.MAX_RESOLUTION`，步進值 16。 | `INT` |
| `高度` | 影片高度，預設值 480，最小值 16，最大值 `nodes.MAX_RESOLUTION`，步進值 16。 | `INT` |
| `長度` | 影片長度，預設值 25，最小值 1，最大值 `nodes.MAX_RESOLUTION`，步進值 4。 | `INT` |
| `批次大小` | 批次大小，預設值 1，最小值 1，最大值 4096。 | `INT` |

## 輸出

| 參數 | 說明 | Comfy 類型 |
| --- | --- | --- |
| `samples` | 生成的潛在影片樣本，包含零張量，準備用於處理和生成任務。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/zh-TW.md)
