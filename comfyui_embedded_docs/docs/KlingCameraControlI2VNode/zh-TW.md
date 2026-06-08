# Kling 圖片轉影片攝影機控制節點

Kling 圖片轉影片攝影機控制節點能將靜態圖片轉換為具有專業攝影機運鏡的電影級影片。這個專門的圖片轉影片節點讓您能夠控制虛擬攝影機動作，包括縮放、旋轉、平移、傾斜和第一人稱視角，同時保持對原始圖片的關注。攝影機控制目前僅在專業模式下支援，需使用 kling-v1-5 模型並設定為 5 秒鐘時長。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `start_frame` | 參考圖片 - URL 或 Base64 編碼字串，不得超過 10MB，解析度不低於 300x300px，長寬比介於 1:2.5 至 2.5:1 之間。Base64 不應包含 data:image 前綴。 | IMAGE | 是 | - |
| `prompt` | 正向文字提示，描述期望的影片內容 | STRING | 是 | - |
| `負向提示詞` | 負向文字提示，描述在生成影片中應避免的內容 | STRING | 是 | - |
| `cfg_scale` | 控制文字引導的強度。數值越高，輸出結果越貼近提示內容（預設值：0.75） | FLOAT | 否 | 0.0 至 1.0 |
| `aspect_ratio` | 生成影片的長寬比（預設值："16:9"） | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `camera_control` | 可使用 Kling 攝影機控制節點建立。控制影片生成過程中的攝影機移動和動態。 | CAMERA_CONTROL | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video_id` | 生成的影片輸出 | VIDEO |
| `時長` | 生成影片的唯一識別碼 | STRING |
| `duration` | 生成影片的時長 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingCameraControlI2VNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a2965975cd484768298f4c7e504423f782ea032dfb5ef304579715be9c27cb79`
