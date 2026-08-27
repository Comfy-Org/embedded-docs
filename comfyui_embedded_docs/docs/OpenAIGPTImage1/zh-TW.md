# OpenAI GPT Image 2

透過 OpenAI 的 GPT Image 端點同步生成影像。此節點可以根據文字提示建立新影像，或在提供輸入影像和選用遮罩時編輯現有影像。它支援 gpt-image-1、gpt-image-1.5 和 gpt-image-2 模型，並標記為已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | GPT Image 的文字提示（預設值：""） | STRING | 是 | - |
| `種子值` | 用於生成的隨機種子（預設值：0）— 後端尚未實作 | INT | 否 | 0 至 2147483647 |
| `品質` | 影像品質，影響成本和生成時間（預設值："low"） | COMBO | 否 | "low"<br>"medium"<br>"high" |
| `背景` | 回傳帶有或沒有背景的影像（預設值："auto"） | COMBO | 否 | "auto"<br>"opaque"<br>"transparent" |
| `尺寸` | 影像尺寸。選擇「Custom」以使用自訂寬度和高度（僅限 GPT Image 2）（預設值："auto"） | COMBO | 否 | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `數量` | 要生成的影像數量（預設值：1） | INT | 否 | 1 至 8 |
| `參考影像` | 用於影像編輯的選用參考影像 | IMAGE | 否 | - |
| `遮罩` | 用於修復的選用遮罩（白色區域將被替換） | MASK | 否 | - |
| `model` | 要使用的 GPT Image 模型（預設值："gpt-image-2"） | COMBO | 否 | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | 僅在 `size` 為「Custom」時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設值：1024） | INT | 否 | 1024 至 3840, step 16 |
| `custom_height` | 僅在 `size` 為「Custom」時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設值：1024） | INT | 否 | 1024 至 3840, step 16 |

**參數約束：**

- 當提供 `image` 時，節點會切換到影像編輯模式。
- 只有在提供 `image` 時才能使用 `mask`。
- 使用 `mask` 時，僅支援單張影像（批次大小必須為 1）。
- `mask` 和 `image` 必須具有相同尺寸。
- 自訂解析度（`size` = "Custom"）僅由 gpt-image-2 模型支援。
- 自訂寬度和高度必須是 16 的倍數。
- 自訂解析度的長寬比不得超過 3:1。
- 自訂解析度的總像素數必須介於 655,360 和 8,294,400 之間。
- gpt-image-2 模型不支援透明背景。
- 大於 1536x1024 的尺寸（例如 2048x2048、3840x2160）僅由 gpt-image-2 模型支援。
- `gpt-image-1` 和 `gpt-image-1.5` 模型僅支援 `auto`、`1024x1024`、`1024x1536` 和 `1536x1024` 尺寸。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成或編輯後的影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
