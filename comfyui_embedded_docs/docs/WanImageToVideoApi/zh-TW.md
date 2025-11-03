> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/zh-TW.md)

{heading_overview}

Wan Image to Video 節點從單一輸入圖像和文字提示開始生成影片內容。它透過根據提供的描述延伸初始畫面來創建影片序列，並提供控制影片品質、持續時間和音訊整合的選項。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | "wan2.5-i2v-preview"<br>"wan2.5-i2v-preview" | 使用的模型（預設："wan2.5-i2v-preview"） |
| `image` | IMAGE | 是 | - | 作為影片生成第一幀的輸入圖像 |
| `prompt` | STRING | 是 | - | 用於描述元素和視覺特徵的提示，支援英文/中文（預設：空） |
| `negative_prompt` | STRING | 否 | - | 用於指導應避免內容的負向文字提示（預設：空） |
| `resolution` | COMBO | 否 | "480P"<br>"720P"<br>"1080P" | 影片解析度品質（預設："480P"） |
| `duration` | INT | 否 | 5-10 | 可用持續時間：5 和 10 秒（預設：5） |
| `audio` | AUDIO | 否 | - | 音訊必須包含清晰、響亮的聲音，無雜音、背景音樂 |
| `seed` | INT | 否 | 0-2147483647 | 用於生成的種子值（預設：0） |
| `generate_audio` | BOOLEAN | 否 | - | 如果沒有音訊輸入，是否自動生成音訊（預設：False） |
| `prompt_extend` | BOOLEAN | 否 | - | 是否使用 AI 輔助增強提示（預設：True） |
| `watermark` | BOOLEAN | 否 | - | 是否在結果中添加「AI 生成」浮水印（預設：True） |

**限制條件：**

- 影片生成需要恰好一張輸入圖像
- 持續時間參數僅接受 5 或 10 秒的值
- 當提供音訊時，其持續時間必須在 3.0 到 29.0 秒之間

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | VIDEO | 基於輸入圖像和提示生成的影片 |