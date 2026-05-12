> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/zh-TW.md)

## 概述

此節點使用 OpenAI 的 GPT 圖片 API 來生成圖片。它支援多種模型，允許您提供輸入圖片進行編輯，並可使用遮罩來指定要修改的圖片區域。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 不適用 | GPT 圖片的文字提示（預設：""）。 |
| `model` | COMBO | 是 | `"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` | 要使用的 OpenAI GPT 圖片模型。選擇模型會顯示該模型特有的額外參數。 |
| `model.size` | COMBO | 是 | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` | 圖片尺寸。選擇「Custom」以使用自訂寬度和高度（預設："auto"）。僅適用於 `gpt-image-2`。 |
| `model.custom_width` | INT | 否 | 1024 至 3840 | 僅在 `size` 設定為「Custom」時使用。必須為 16 的倍數（預設：1024）。僅適用於 `gpt-image-2`。 |
| `model.custom_height` | INT | 否 | 1024 至 3840 | 僅在 `size` 設定為「Custom」時使用。必須為 16 的倍數（預設：1024）。僅適用於 `gpt-image-2`。 |
| `model.background` | COMBO | 是 | `"auto"`<br>`"opaque"` | 返回帶有或不帶有背景的圖片（預設："auto"）。僅適用於 `gpt-image-2`。 |
| `model.quality` | COMBO | 是 | `"standard"`<br>`"hd"` | 生成圖片的品質。僅適用於 `gpt-image-2`。 |
| `model.images` | IMAGE | 否 | 不適用 | 用於編輯的輸入圖片。僅適用於 `gpt-image-2`。 |
| `model.mask` | MASK | 否 | 不適用 | 用於指定輸入圖片中要編輯區域的遮罩。僅適用於 `gpt-image-2`。 |
| `n` | INT | 是 | 1 至 8 | 要生成的圖片數量（預設：1）。 |
| `seed` | INT | 是 | 0 至 2147483647 | 用於可重現性的種子（預設：0）。注意：後端尚未實作此功能。 |

**參數限制與注意事項：**

- 使用 `gpt-image-2` 且 `model.size` 設定為「Custom」時，`custom_width` 和 `custom_height` 必須為 16 的倍數，最大邊長必須 <= 3840，長寬比不得超過 3:1，且總像素數必須介於 655,360 至 8,294,400 之間。
- 如果提供了 `mask`，則需要提供輸入圖片（`model.images`）。沒有輸入圖片時無法使用遮罩。
- 遮罩不能與多個輸入圖片同時使用。
- 當提供遮罩時，遮罩尺寸必須與輸入圖片尺寸相符。
- `seed` 參數目前無效。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 生成的單張或多張圖片。 |