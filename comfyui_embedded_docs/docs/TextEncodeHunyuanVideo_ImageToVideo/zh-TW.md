> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/zh-TW.md)

此節點透過結合文字提示與圖像嵌入來為影片生成創建條件化資料。它使用 CLIP 模型處理文字輸入和來自 CLIP 視覺輸出的視覺資訊，然後根據指定的圖像交錯設定生成融合這兩種來源的標記。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `clip` | CLIP | 是 | - | 用於標記化和編碼的 CLIP 模型 |
| `clip_vision_output` | CLIP_VISION_OUTPUT | 是 | - | 來自 CLIP 視覺模型的視覺嵌入，提供圖像上下文 |
| `提示詞` | STRING | 是 | - | 用於指導影片生成的文字描述，支援多行輸入和動態提示 |
| `影像交錯` | INT | 是 | 1-512 | 圖像相對於文字提示的影響程度。數值越高表示文字提示的影響越大。（預設值：2） |

## 輸出參數

| 輸出名稱 | 資料類型 | 參數說明 |
|-------------|-----------|-------------|
| `CONDITIONING` | CONDITIONING | 結合文字和圖像資訊的條件化資料，用於影片生成 |