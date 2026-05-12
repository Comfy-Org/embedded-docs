> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/zh-TW.md)

## 概述

根據文字提示修改現有圖片。此節點將您的圖片和文字描述發送至 Grok API，該 API 會根據您的指示編輯圖片並返回結果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 不適用 | 用於生成圖片的文字提示。去除空白字元後長度至少需為 1 個字元。 |
| `model` | MODEL | 是 | 請參閱說明 | 要使用的 Grok 圖片模型。此參數包含多個子選項，會在選取模型後顯示。可用模型：`grok-imagine-image-quality`、`grok-imagine-image-pro`、`grok-imagine-image`。每個模型具有不同的功能（請參閱下方備註）。 |
| `seed` | INT | 是 | 0 至 2147483647 | 用於決定節點是否應重新執行的種子；無論種子為何，實際結果皆為非確定性。（預設值：0） |

**關於 `model` 參數限制的備註：**
- `model` 參數是一個動態組合，包含 `resolution`、`number_of_images`、`images` 和 `aspect_ratio` 等子選項。
- **`grok-imagine-image-quality`**：最多支援 3 張輸入圖片，並允許自訂長寬比。
- **`grok-imagine-image-pro`**：僅支援 1 張輸入圖片，不允許自訂長寬比。
- **`grok-imagine-image`**：最多支援 3 張輸入圖片，並允許自訂長寬比。
- **編輯時至少需要一張輸入圖片**。若未提供任何圖片，節點將引發錯誤。
- **自訂長寬比**（`aspect_ratio` 子選項）僅在圖片輸入連接多張圖片時允許使用。若僅提供一張圖片，長寬比必須設為 "auto"。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Grok API 返回的已編輯圖片。若生成單張圖片，則直接返回；若生成多張圖片，則會拼接成單一批次張量。 |