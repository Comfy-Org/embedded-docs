# LumaRay32VideoReframeNode

此節點使用 Luma Ray 3.2 變更現有影片的長寬比，並以生成的內容填補新曝光的畫布區域。來源影片最長可達 30 秒，計費方式為按輸出秒數計算。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 要重新構圖的來源影片。最長 30 秒。 | VIDEO | 是 | - |
| `prompt` | 描述新曝光的畫布區域應如何填補。 | STRING | 是 | - |
| `aspect_ratio` | 重新構圖後影片的目標長寬比（預設值："16:9"）。 | STRING | 是 | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4"<br>"21:9" |
| `resolution` | 重新構圖後影片的輸出解析度（預設值："720p"）。 | STRING | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `seed` | 用於可重現生成的隨機種子。 | INT | 是 | - |

**注意：** 重新構圖時，`1080p` 解析度不適用於垂直長寬比（`9:16` 和 `3:4`）。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 具有新長寬比和已填補畫布區域的重新構圖影片。 | VIDEO |
| `generation_id` | 生成請求的唯一識別碼。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32VideoReframeNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d35ff5b63a850e4e44a40857188918ab5cde00b9159e3720a189a81807cfa7cb`
