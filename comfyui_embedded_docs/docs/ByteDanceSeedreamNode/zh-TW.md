> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNode/zh-TW.md)

ByteDance Seedream 4 節點提供統一的文字生成圖像功能，以及高達 4K 解析度的精確單句編輯能力。它可以根據文字提示建立新圖像，或使用文字指令編輯現有圖像。該節點支援單一圖像生成以及多個相關圖像的連續生成。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | COMBO | "seedream-4-0-250828" | ["seedream-4-0-250828"] | 模型名稱 |
| `prompt` | STRING | STRING | "" | - | 用於建立或編輯圖像的文字提示。 |
| `image` | IMAGE | IMAGE | - | - | 用於圖像到圖像生成的輸入圖像。用於單一或多參考生成的 1-10 張圖像列表。 |
| `size_preset` | STRING | COMBO | RECOMMENDED_PRESETS_SEEDREAM_4 中的第一個預設值 | RECOMMENDED_PRESETS_SEEDREAM_4 中的所有標籤 | 選擇推薦尺寸。選擇 Custom 以使用下方的寬度和高度。 |
| `width` | INT | INT | 2048 | 1024-4096 (步長 64) | 圖像的自訂寬度。僅在 `size_preset` 設定為 `Custom` 時生效 |
| `height` | INT | INT | 2048 | 1024-4096 (步長 64) | 圖像的自訂高度。僅在 `size_preset` 設定為 `Custom` 時生效 |
| `sequential_image_generation` | STRING | COMBO | "disabled" | ["disabled", "auto"] | 群組圖像生成模式。'disabled' 生成單一圖像。'auto' 讓模型決定是否生成多個相關圖像（例如，故事場景、角色變體）。 |
| `max_images` | INT | INT | 1 | 1-15 | 當 sequential_image_generation='auto' 時要生成的最大圖像數量。總圖像數（輸入 + 生成）不能超過 15。 |
| `seed` | INT | INT | 0 | 0-2147483647 | 用於生成的種子值。 |
| `watermark` | BOOLEAN | BOOLEAN | True | - | 是否在圖像上添加「AI 生成」浮水印。 |
| `fail_on_partial` | BOOLEAN | BOOLEAN | True | - | 如果啟用，當任何請求的圖像缺失或返回錯誤時，將中止執行。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 根據輸入參數和提示生成的圖像 |