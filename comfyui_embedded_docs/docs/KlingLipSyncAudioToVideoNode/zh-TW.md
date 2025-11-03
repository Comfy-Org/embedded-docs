> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/zh-TW.md)

Kling Lip Sync Audio to Video Node 可將影片檔案中的嘴部動作與音訊檔案的內容進行同步。此節點會分析音訊中的語音模式，並調整影片中的臉部動作，以創造出逼真的唇形同步效果。此過程需要一個包含清晰臉部的影片檔案和一個具有明顯可辨識人聲的音訊檔案。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 包含需要進行唇形同步的臉部之影片檔案 |
| `audio` | AUDIO | 是 | - | 包含需要與影片同步之人聲的音訊檔案 |
| `voice_language` | COMBO | 否 | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` | 音訊檔案中人聲的語言（預設值："en"） |

**重要限制：**

- 音訊檔案大小不應超過 5MB
- 影片檔案大小不應超過 100MB
- 影片尺寸的高度/寬度應在 720px 至 1920px 之間
- 影片長度應在 2 秒至 10 秒之間
- 音訊必須包含清晰可辨的人聲
- 影片必須包含清晰可辨的臉部

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 經過處理並具有唇形同步嘴部動作的影片 |
| `video_id` | STRING | 已處理影片的唯一識別碼 |
| `duration` | STRING | 已處理影片的持續時間 |