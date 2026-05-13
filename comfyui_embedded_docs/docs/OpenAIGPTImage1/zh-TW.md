> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/zh-TW.md)

# OpenAI GPT Image 節點

透過 OpenAI 的 GPT Image 端點同步生成影像。此節點可以根據文字提示建立新影像，或在提供輸入影像和可選遮罩時編輯現有影像。它支援多種 GPT Image 模型，包括 gpt-image-1、gpt-image-1.5 和 gpt-image-2。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | GPT Image 的文字提示（預設：""） |
| `seed` | INT | 否 | 0 至 2147483647 | 生成用的隨機種子（預設：0）- 後端尚未實作 |
| `quality` | COMBO | 否 | "low"<br>"medium"<br>"high" | 影像品質，影響成本和生成時間（預設："low"） |
| `background` | COMBO | 否 | "auto"<br>"opaque"<br>"transparent" | 回傳有或無背景的影像（預設："auto"） |
| `size` | COMBO | 否 | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" | 影像尺寸。選擇"Custom"以使用自訂寬度和高度（僅限 GPT Image 2）（預設："auto"） |
| `n` | INT | 否 | 1 至 8 | 要生成的影像數量（預設：1） |
| `image` | IMAGE | 否 | - | 用於影像編輯的選用參考影像 |
| `mask` | MASK | 否 | - | 用於局部重繪的選用遮罩（白色區域將被替換） |
| `model` | COMBO | 否 | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" | 要使用的 GPT Image 模型（預設："gpt-image-2"） |
| `custom_width` | INT | 否 | 1024 至 3840 | 僅在 `size` 為"Custom"時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設：1024） |
| `custom_height` | INT | 否 | 1024 至 3840 | 僅在 `size` 為"Custom"時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設：1024） |

**參數限制：**

- 當提供 `image` 時，節點切換到影像編輯模式
- `mask` 僅能在提供 `image` 時使用
- 使用 `mask` 時，僅支援單張影像（批次大小必須為 1）
- `mask` 和 `image` 必須具有相同尺寸
- 自訂解析度（`size` = "Custom"）僅由 gpt-image-2 模型支援
- 自訂寬度和高度必須是 16 的倍數
- 自訂解析度的長寬比不得超過 3:1
- 自訂解析度的總像素必須在 655,360 至 8,294,400 之間
- gpt-image-2 模型不支援透明背景
- 大於 1536x1024 的尺寸（例如 2048x2048、3840x2160）僅由 gpt-image-2 模型支援

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 生成或編輯後的影像 |

---
**Source fingerprint (SHA-256):** `44b258d6afcb388db3836427abdd5a7cb5c09a0328efceef7e114dd61a38eae1`
