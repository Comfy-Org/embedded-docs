> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pikadditions/zh-TW.md)

Pikadditions 節點可讓您在影片中添加任何物件或圖像。您只需上傳影片並指定要添加的內容，即可創建無縫融合的結果。此節點使用 Pika API 將圖像插入影片中，實現自然逼真的融合效果。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 要添加圖像的原始影片。 |
| `image` | IMAGE | 是 | - | 要添加到影片中的圖像。 |
| `prompt_text` | STRING | 是 | - | 描述要添加到影片中內容的文字說明。 |
| `negative_prompt` | STRING | 是 | - | 描述要避免在影片中出現內容的文字說明。 |
| `seed` | INT | 是 | 0 到 4294967295 | 用於可重現結果的隨機種子值。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 已插入圖像的處理後影片。 |