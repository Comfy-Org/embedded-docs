# OpenAI GPT Image 2

透過 OpenAI 的 GPT Image 端點同步生成圖像。此節點可以根據文字提示建立新圖像，或在提供輸入圖像和可選遮罩時編輯現有圖像。它支援多種 GPT Image 模型，包括 gpt-image-1、gpt-image-1.5 和 gpt-image-2。此節點已棄用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | GPT Image 的文字提示（預設：""） | STRING | 是 | - |
| `seed` | 生成的隨機種子（預設：0）- 後端尚未實作 | INT | 否 | 0 到 2147483647 |
| `quality` | 圖像品質，影響成本與生成時間（預設："low"） | COMBO | 否 | "low"<br>"medium"<br>"high" |
| `background` | 傳回帶有或不帶背景的圖像（預設："auto"） | COMBO | 否 | "auto"<br>"opaque"<br>"transparent" |
| `size` | 圖像尺寸。選擇「Custom」以使用自訂寬度和高度（僅限 GPT Image 2）（預設："auto"） | COMBO | 否 | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `n` | 要生成的圖像數量（預設：1） | INT | 否 | 1 到 8 |
| `image` | 用於圖像編輯的選用參考圖像 | IMAGE | 否 | - |
| `mask` | 用於修復的選用遮罩（白色區域將被替換） | MASK | 否 | - |
| `model` | 要使用的 GPT Image 模型（預設："gpt-image-2"） | COMBO | 否 | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | 僅在 `size` 為「Custom」時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設：1024） | INT | 否 | 1024 到 3840 |
| `custom_height` | 僅在 `size` 為「Custom」時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設：1024） | INT | 否 | 1024 到 3840 |

**參數限制：**

- 當提供 `image` 時，節點會切換到圖像編輯模式
- 僅在提供 `image` 時才能使用 `mask`
- 使用 `mask` 時，僅支援單一圖像（批次大小必須為 1）
- `mask` 和 `image` 的大小必須相同
- 自訂解析度（`size` = "Custom"）僅由 gpt-image-2 模型支援
- 自訂寬度和高度必須是 16 的倍數
- 自訂解析度的長寬比不得超過 3:1
- 自訂解析度的總像素必須介於 655,360 到 8,294,400 之間
- gpt-image-2 模型不支援透明背景
- 大於 1536x1024 的尺寸（例如 2048x2048、3840x2160）僅由 gpt-image-2 模型支援

## 輸出

| 輸出名 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成或編輯的圖像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bf588bffced6e66536b4cb54655ef6ebb9cf988d9739e3c379a8ebda1486e20a`
