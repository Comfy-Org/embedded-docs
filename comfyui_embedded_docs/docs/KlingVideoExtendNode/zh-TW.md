> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoExtendNode/zh-TW.md)

# Kling 影片擴展節點

Kling 影片擴展節點允許您擴展由其他 Kling 節點建立的影片。它會接收一個由影片 ID 識別的現有影片，並根據您的文字提示生成額外內容。此節點透過將您的擴展請求發送到 Kling API 來運作，並返回擴展後的影片及其新 ID 和時長。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 否 | - | 用於引導影片擴展的正面文字提示 |
| `負向提示詞` | STRING | 否 | - | 用於指定擴展影片中應避免元素的負面文字提示 |
| `cfg_scale` | FLOAT | 否 | 0.0 - 1.0 | 控制提示引導的強度（預設值：0.5） |
| `video_id` | STRING | 是 | - | 要擴展的影片 ID。支援由文字轉影片、圖片轉影片以及先前的影片擴展操作生成的影片。擴展後的總時長不得超過 3 分鐘。 |

**注意：** `video_id` 必須引用由其他 Kling 節點建立的影片，且擴展後的總時長不得超過 3 分鐘。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video_id` | VIDEO | 由 Kling API 生成的擴展影片 |
| `時長` | STRING | 擴展影片的唯一識別碼 |
| `duration` | STRING | 擴展影片的時長 |

---
**Source fingerprint (SHA-256):** `ecef4aedffe83bf384f2f9c3d8840f3fcab4b8c21e6e9afb36e177abb6f069fd`
