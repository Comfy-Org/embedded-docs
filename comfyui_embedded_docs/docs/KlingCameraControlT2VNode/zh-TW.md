# Kling 文字轉影片相機控制節點

Kling 文字轉影片相機控制節點能將文字轉換為具有專業攝影機運鏡的電影級影片，模擬真實世界的電影攝影技巧。此節點支援控制虛擬攝影機動作，包括縮放、旋轉、平移、傾斜及第一人稱視角，同時保持對原始文字的關注。由於相機控制僅在專業模式下支援，且需使用 kling-v1-5 模型搭配 5 秒長度，因此時長、模式與模型名稱均為固定值。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `prompt` | 正向文字提示詞 | STRING | 是 | - |
| `負向提示詞` | 反向文字提示詞 | STRING | 是 | - |
| `cfg_scale` | 控制輸出結果遵循提示詞的程度（預設值：0.75） | FLOAT | 否 | 0.0-1.0 |
| `aspect_ratio` | 生成影片的畫面比例（預設值："16:9"） | COMBO | 否 | "16:8"<br>"9:16"<br>"1:1"<br>"21:9"<br>"3:4"<br>"4:3" |
| `camera_control` | 可使用 Kling 相機控制節點建立。控制影片生成過程中的攝影機運鏡與動態效果。 | CAMERA_CONTROL | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video_id` | 具有相機控制效果的生成影片 | VIDEO |
| `video_id` | 生成影片的唯一識別碼 | STRING |
| `時長` | 生成影片的時長 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlT2VNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4ebdd6af31f9e5c0816c4bcba886179b3f7d2b5030ff4fa3ddad6df25c528af7`
