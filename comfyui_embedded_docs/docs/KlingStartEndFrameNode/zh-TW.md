# Kling 起始-結束影格轉影片節點

Kling 起始-結束影格轉影片節點會建立一個在您提供的起始和結束影像之間進行轉場的影片序列。它會生成中間的所有影格，以產生從第一個影格到最後一個影格的平滑轉變。此節點會呼叫影像轉影片 API，但僅支援與 `image_tail` 請求欄位搭配使用的輸入選項。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `start_frame` | 參考影像 - URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300*300px，長寬比介於 1:2.5 ~ 2.5:1 之間。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `end_frame` | 參考影像 - 結束影格控制。URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300*300px。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `prompt` | 正向文字提示 | STRING | 是 | - |
| `負向提示詞` | 負向文字提示 | STRING | 是 | - |
| `cfg_scale` | 控制提示引導的強度（預設值：0.5） | FLOAT | 否 | 0.0-1.0 |
| `aspect_ratio` | 生成影片的長寬比（預設值："16:9"） | COMBO | 否 | "16:8"<br>"9:16"<br>"1:1" |
| `mode` | 用於影片生成的配置，格式為：模式 / 時長 / 模型名稱。（預設值：可用模式中的第七個選項） | COMBO | 否 | 提供多個選項 |

**影像限制：**

- 必須同時提供 `start_frame` 和 `end_frame`，且兩者檔案大小不得超過 10MB
- 兩張影像的最低解析度：300×300 像素
- `start_frame` 的長寬比必須介於 1:2.5 到 2.5:1 之間
- Base64 編碼的影像不應包含 "data:image" 前綴

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video_id` | 生成的影片序列 | VIDEO |
| `video_id` | 生成影片的唯一識別碼 | STRING |
| `時長` | 生成影片的時長 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1df5820b4f41ccd5afec8e2701888d90c940f164c433c7f81397b41e8fc333c6`
