# OpenAI GPT Image 2

透過 OpenAI 的 GPT Image 端點同步生成影像。它可以從文字提示詞建立新影像，或在提供輸入影像和選用遮罩時編輯現有影像。此節點支援 `gpt-image-1`、`gpt-image-1.5` 和 `gpt-image-2` 模型，並標記為已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | GPT Image 的文字提示詞（預設值：""） | STRING | 是 | - |
| `種子值` | 用於生成的隨機種子；後端尚未實作（預設值：0） | INT | 否 | 0 至 2147483647 |
| `品質` | 影像品質，會影響成本和生成時間（預設值："low"） | COMBO | 否 | "low"<br>"medium"<br>"high" |
| `背景` | 回傳的影像是否包含背景（預設值："auto"） | COMBO | 否 | "auto"<br>"opaque"<br>"transparent" |
| `尺寸` | 影像尺寸。選擇 "Custom" 以使用自訂寬度和高度（僅限 GPT Image 2）（預設值："auto"） | COMBO | 否 | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024"<br>"2048x2048"<br>"2048x1152"<br>"1152x2048"<br>"3840x2160"<br>"2160x3840"<br>"Custom" |
| `數量` | 要生成多少張影像（預設值：1） | INT | 否 | 1 至 8 |
| `參考影像` | 用於影像編輯的選用參考影像 | IMAGE | 否 | - |
| `遮罩` | 用於修補的選用遮罩（白色區域將被替換） | MASK | 否 | - |
| `model` | 要使用的 GPT Image 模型（預設值："gpt-image-2"） | COMBO | 否 | "gpt-image-1"<br>"gpt-image-1.5"<br>"gpt-image-2" |
| `custom_width` | 僅當 `size` 為 "Custom" 時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設值：1024） | INT | 否 | 1024 至 3840，步進值 16 |
| `custom_height` | 僅當 `size` 為 "Custom" 時使用。必須是 16 的倍數（僅限 GPT Image 2）（預設值：1024） | INT | 否 | 1024 至 3840，步進值 16 |

**參數限制：**

- 提供 `image` 時，節點會使用影像編輯端點。
- 只有在提供 `image` 時才能使用 `mask`。
- 使用 `mask` 時，僅支援單張影像（批次大小必須為 1）。
- `mask` 和 `image` 必須大小相同。
- 自訂解析度（`size` = "Custom"）僅由 `gpt-image-2` 模型支援。
- 自訂寬度和高度必須是 16 的倍數。
- 自訂解析度的最長邊必須為 3840 或更小。
- 自訂解析度的長寬比不得超過 3:1。
- 自訂解析度的總像素數必須介於 655,360 和 8,294,400 之間。
- `gpt-image-1` 和 `gpt-image-1.5` 模型僅支援 `auto`、`1024x1024`、`1024x1536` 和 `1536x1024` 尺寸。其他尺寸僅由 `gpt-image-2` 模型支援。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 生成或編輯後的影像。多張影像會以批次方式回傳；若回傳的影像尺寸不同，會調整大小以符合第一張影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f0f0db7fd2cdf8efd2155522b289aa8f3f939fa79a6e9060b0ffbb2dd20efa1e`
