> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/zh-TW.md)

## 概述

根據文字提示修改現有影像。此節點會將您的影像和文字描述發送至 Grok API，該 API 會根據您的指示編輯影像並回傳結果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `提示詞` | STRING | 是 | 不適用 | 用於生成影像的文字提示。去除空白後長度必須至少為 1 個字元。 |
| `模型` | MODEL | 是 | 請參閱說明 | 要使用的 Grok 影像模型。此參數在選取模型後會顯示多個子選項。可用模型：`grok-imagine-image-quality`、`grok-imagine-image-pro`、`grok-imagine-image`。每個模型具有不同的功能（請參閱下方備註）。 |
| `種子` | INT | 是 | 0 至 2147483647 | 決定節點是否應重新執行的種子；無論種子為何，實際結果皆為非確定性。（預設值：0） |

**關於 `model` 參數限制的備註：**
- `model` 參數是一個動態組合，包含 `resolution`、`number_of_images`、`images` 和 `aspect_ratio` 等子選項。
- **`grok-imagine-image-quality`**：支援最多 3 張輸入影像，並允許自訂長寬比。
- **`grok-imagine-image-pro`**：僅支援 1 張輸入影像，不允許自訂長寬比。
- **`grok-imagine-image`**：支援最多 3 張輸入影像，並允許自訂長寬比。
- **編輯時至少需要一張輸入影像**。若未提供任何影像，節點將會報錯。
- **自訂長寬比**（`aspect_ratio` 子選項）僅在有多張影像連接到影像輸入時才允許使用。若僅提供一張影像，長寬比必須設為 "auto"。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Grok API 回傳的已編輯影像。若生成單張影像，則直接回傳；若生成多張影像，則會拼接成單一批量張量。 |

---
**Source fingerprint (SHA-256):** `b041b40bb5712a67b09dcb0c841f00cbdd9ef77b9e4f3fdc6b2c4038be447ba5`
