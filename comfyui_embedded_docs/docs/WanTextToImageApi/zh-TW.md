> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/zh-TW.md)

Wan Text to Image 節點根據文字描述生成圖像。它使用 AI 模型從文字提示創建視覺內容，支援英文和中文文字輸入。該節點提供各種控制項來調整輸出圖像的尺寸、品質和風格偏好。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | "wan2.5-t2i-preview" | 要使用的模型（預設："wan2.5-t2i-preview"） |
| `prompt` | STRING | 是 | - | 用於描述元素和視覺特徵的提示，支援英文/中文（預設：空） |
| `negative_prompt` | STRING | 否 | - | 負向文字提示，用於指導應避免的內容（預設：空） |
| `width` | INT | 否 | 768-1440 | 圖像寬度（像素）（預設：1024，步長：32） |
| `height` | INT | 否 | 768-1440 | 圖像高度（像素）（預設：1024，步長：32） |
| `seed` | INT | 否 | 0-2147483647 | 用於生成的種子值（預設：0） |
| `prompt_extend` | BOOLEAN | 否 | - | 是否使用 AI 輔助增強提示（預設：True） |
| `watermark` | BOOLEAN | 否 | - | 是否在結果中添加「AI 生成」浮水印（預設：True） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 基於文字提示生成的圖像 |