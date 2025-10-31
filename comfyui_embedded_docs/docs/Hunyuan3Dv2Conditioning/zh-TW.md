> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/zh-TW.md)

{heading_overview}

Hunyuan3Dv2Conditioning 節點處理 CLIP 視覺輸出，為影片模型生成條件化資料。它從視覺輸出中提取最後隱藏狀態嵌入，並創建正向和負向條件化對。正向條件化使用實際嵌入，而負向條件化則使用相同形狀的零值嵌入。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `clip_vision_output` | CLIP_VISION_OUTPUT | 是 | - | 來自 CLIP 視覺模型的輸出，包含視覺嵌入 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含 CLIP 視覺嵌入的正向條件化資料 |
| `negative` | CONDITIONING | 包含與正向嵌入形狀匹配的零值嵌入的負向條件化資料 |