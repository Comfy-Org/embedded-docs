> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/zh-TW.md)

{heading_overview}

Hunyuan3Dv2ConditioningMultiView 節點處理多視角 CLIP 視覺嵌入以用於 3D 影片生成。它接收可選的前視圖、左視圖、後視圖和右視圖嵌入，並將它們與位置編碼結合，為影片模型創建條件資料。該節點輸出來自組合嵌入的正向條件資料，以及帶有零值的負向條件資料。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `front` | CLIP_VISION_OUTPUT | 否 | - | 前視圖的 CLIP 視覺輸出 |
| `left` | CLIP_VISION_OUTPUT | 否 | - | 左視圖的 CLIP 視覺輸出 |
| `back` | CLIP_VISION_OUTPUT | 否 | - | 後視圖的 CLIP 視覺輸出 |
| `right` | CLIP_VISION_OUTPUT | 否 | - | 右視圖的 CLIP 視覺輸出 |

**注意：** 必須至少提供一個視圖輸入，節點才能正常運作。該節點僅會處理包含有效 CLIP 視覺輸出資料的視圖。

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `positive` | CONDITIONING | 包含帶有位置編碼的組合多視角嵌入的正面條件資料 |
| `negative` | CONDITIONING | 帶有零值的負面條件資料，用於對比學習 |