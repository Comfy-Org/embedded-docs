> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImage1/zh-TW.md)

透過 OpenAI 的 GPT Image 1 端點同步生成圖像。此節點可根據文字提示建立新圖像，或在提供輸入圖像和可選遮罩時編輯現有圖像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | GPT Image 1 的文字提示 (預設值: "") |
| `seed` | INT | 否 | 0 至 2147483647 | 生成用的隨機種子 (預設值: 0) - 後端尚未實作此功能 |
| `quality` | COMBO | 否 | "low"<br>"medium"<br>"high" | 圖像品質，影響成本和生成時間 (預設值: "low") |
| `background` | COMBO | 否 | "opaque"<br>"transparent" | 返回的圖像是否包含背景 (預設值: "opaque") |
| `size` | COMBO | 否 | "auto"<br>"1024x1024"<br>"1024x1536"<br>"1536x1024" | 圖像尺寸 (預設值: "auto") |
| `n` | INT | 否 | 1 至 8 | 要生成的圖像數量 (預設值: 1) |
| `image` | IMAGE | 否 | - | 用於圖像編輯的可選參考圖像 (預設值: None) |
| `mask` | MASK | 否 | - | 用於修補的可選遮罩 (白色區域將被替換) (預設值: None) |

**參數限制條件：**

- 當提供 `image` 時，節點會切換到圖像編輯模式
- 只有在提供 `image` 時才能使用 `mask`
- 使用 `mask` 時，僅支援單一圖像 (批次大小必須為 1)
- `mask` 和 `image` 必須具有相同尺寸

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 生成或編輯後的圖像 |