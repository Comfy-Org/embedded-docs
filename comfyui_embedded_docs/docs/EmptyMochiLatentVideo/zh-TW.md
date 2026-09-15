# EmptyMochiLatentVideo

EmptyMochiLatentVideo 會建立一個具有你所指定維度的空白潛在影片張量。它會產生一個以零填充的潛在表示，可作為影片生成工作流程的起點。此節點讓你定義潛在影片張量的寬度、高度、長度與批次大小。

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `寬度` | 潛在影片的寬度（以像素為單位，預設值：848，數值以 16 為級距遞增） | INT | 是 | 16 to MAX_RESOLUTION |
| `高度` | 潛在影片的高度（以像素為單位，預設值：480，數值以 16 為級距遞增） | INT | 是 | 16 to MAX_RESOLUTION |
| `長度` | 潛在影片的影格數（預設值：25，數值以 6 為級距遞增，從 7 開始） | INT | 是 | 7 to MAX_RESOLUTION |
| `批次大小` | 單一批次中要生成的潛在影片數量（預設值：1） | INT | 否 | 1 至 4096 |

**注意：** 實際的潛在維度計算方式為 width/8 與 height/8，時間維度計算方式為 `((length - 1) // 6) + 1`，且該張量具有 12 個通道。由於 `length` 從 7 開始以 6 為級距遞增，因此有效值為 7、13、19、25，依此類推。

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `samples` | 一個具有指定維度的空白潛在影片張量，內容全為零 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
