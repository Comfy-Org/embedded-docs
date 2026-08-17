# EmptyMochiLatentVideo

The EmptyMochiLatentVideo 節點會建立具有指定維度的空潛在影片張量。它會產生一個全為零的潛在表示，可作為影片生成工作流程的起點。此節點可讓您定義潛在影片張量的寬度、高度、長度與批次大小。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `width` | 潛在影片的寬度（單位：像素，預設值：848，必須可被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `height` | 潛在影片的高度（單位：像素，預設值：480，必須可被 16 整除） | INT | 是 | 16 至 MAX_RESOLUTION |
| `length` | 潛在影片的幀數（預設值：25，必須滿足 `(length - 1)` 可被 6 整除） | INT | 是 | 7 至 MAX_RESOLUTION |
| `batch_size` | 批次中要生成的潛在影片數量（預設值：1） | INT | 否 | 1 至 4096 |

**注意：** 此節點會壓縮輸入的空間與時間維度。潛在寬度與高度分別計算為 `width / 8` 與 `height / 8`，時間維度則計算為 `((length - 1) // 6) + 1`。`length` 參數必須滿足 `(length - 1)` 可被 6 整除，也就是說有效值為 7、13、19、25 等。產生的潛在張量具有 12 個通道，最終形狀為 `(batch_size, 12, ((length - 1) // 6) + 1, height // 8, width // 8)`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples` | 具有指定維度、全部為零的空潛在影片張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
