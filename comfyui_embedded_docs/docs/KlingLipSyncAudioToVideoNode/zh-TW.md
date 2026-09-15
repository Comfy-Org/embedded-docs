# Kling 影音口型同步

Kling Lip Sync Audio to Video 節點會同步影片檔案中的嘴部動作，使其符合音訊檔案的音訊內容。此節點會分析音訊中的人聲模式，並調整影片中的臉部動作，以建立逼真的唇形同步。此流程需要包含清晰可辨人臉的影片，以及具有清晰可辨人聲的音訊檔案。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 包含要進行唇形同步之人臉的影片檔案 | VIDEO | 是 | - |
| `音訊` | 包含要與影片同步之人聲的音訊檔案 | AUDIO | 是 | - |
| `語音語言` | 音訊檔案中語音所使用的語言（預設值："en"） | COMBO | 是 | `"en"`<br>`"zh"`<br>`"es"`<br>`"fr"`<br>`"de"`<br>`"it"`<br>`"pt"`<br>`"pl"`<br>`"tr"`<br>`"ru"`<br>`"nl"`<br>`"cs"`<br>`"ar"`<br>`"ja"`<br>`"hu"`<br>`"ko"` |

**重要限制：**

- 音訊檔案不應大於 5MB
- 影片檔案不應大於 100MB
- 影片的高度/寬度應介於 720px 與 1920px 之間
- 影片長度應介於 2 秒與 10 秒之間
- 音訊必須包含清晰可辨的人聲
- 影片必須包含清晰可辨的人臉

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 已處理的影片，其嘴部動作已進行唇形同步 | VIDEO |
| `video_id` | 已處理影片的唯一識別碼 | STRING |
| `duration` | 已處理影片的長度 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2f88af3191ac4f9c5c9fa1aaa5b744a12620b66e55a1fe0ab16b8b3b61110128`
