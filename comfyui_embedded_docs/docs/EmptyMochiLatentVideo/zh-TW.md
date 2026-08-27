# EmptyMochiLatentVideo

EmptyMochiLatentVideo 會建立一個具有您指定維度的空潛在影片張量。它會產生一個以零填充的潛在表示，可作為影片生成工作流程的起點。此節點可讓您定義潛在影片張量的寬度、高度、長度與批次大小。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `寬度` | 潛在影片的寬度（以像素為單位，預設值：848，必須能被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `高度` | 潛在影片的高度（以像素為單位，預設值：480，必須能被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `長度` | 潛在影片的幀數（預設值：25，必須滿足 `(length - 1)` 能被 6 整除） | INT | 是 | 7 至 MAX_RESOLUTION |
| `批次大小` | 批次中產生的潛在影片數量（預設值：1） | INT | 否 | 1 至 4096 |

**注意：** 實際潛在維度會以 width/8 與 height/8 計算，時間維度則以 `((length - 1) // 6) + 1` 計算，且張量具有 12 個通道。`length` 參數必須滿足 `(length - 1)` 能被 6 整除，因此有效值為 7、13、19、25 等。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 具有指定維度且全部為零的空潛在影片張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
