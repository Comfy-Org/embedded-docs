> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/zh-TW.md)

# Kling 唇形同步音訊轉影片節點

Kling 唇形同步音訊轉影片節點可將影片檔案中的嘴部動作與音訊檔案的語音內容進行同步。此節點會分析音訊中的語音模式，並調整影片中的臉部動作，以建立逼真的唇形同步效果。此過程需要包含清晰臉部的影片以及具有清晰可辨語音的音訊檔案。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `video` | VIDEO | 是 | - | 包含要進行唇形同步的臉部之影片檔案 |
| `audio` | AUDIO | 是 | - | 包含要與影片同步的語音之音訊檔案 |
| `voice_language` | COMBO | 是 | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` | 音訊檔案中語音的語言（預設值："en"） |

**重要限制條件：**

- 音訊檔案不得大於 5MB
- 影片檔案不得大於 100MB
- 影片尺寸的高度/寬度應在 720px 至 1920px 之間
- 影片長度應在 2 秒至 10 秒之間
- 音訊必須包含清晰可辨的語音
- 影片必須包含清晰的臉部

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 已處理完成且嘴部動作已同步的影片 |
| `video_id` | STRING | 已處理影片的唯一識別碼 |
| `duration` | STRING | 已處理影片的長度 |

---
**Source fingerprint (SHA-256):** `92b8a7a4f9508632155a5f69707ffc4a14f2f44c04e4d01bf46476a972465592`
