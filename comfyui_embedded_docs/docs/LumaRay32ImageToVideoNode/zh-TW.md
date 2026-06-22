# LumaRay32ImageToVideoNode

使用 Luma 的 Ray 3.2 模型從起始及/或結束影格生成影片。以影像錨定的生成內容長度固定為 5 秒。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 影片生成的文字提示。 | STRING | 是 | 1 至 6000 個字元 |
| `resolution` | 生成影片的輸出解析度（預設值："720p"）。 | COMBO | 是 | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `loop` | 使影片無縫循環播放。當設定了結束影格時無法使用此選項。 | BOOLEAN | 是 | True<br>False |
| `seed` | 用於可重複生成的種子值。 | INT | 是 | 0 至 2147483647 |
| `start_frame` | 生成影片的第一個影格。 | IMAGE | 否 | - |
| `end_frame` | 生成影片的最後一個影格。 | IMAGE | 否 | - |

**注意：** 必須至少提供 `start_frame` 或 `end_frame` 其中之一。若兩者皆提供，生成的影片將從起始影格過渡到結束影格。當設定了 `end_frame` 時，無法啟用 `loop` 選項。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 生成的影片輸出。 | VIDEO |
| `generation_id` | 生成請求的唯一識別碼。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32ImageToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ff479c196f10153ffa09af6acfb4e286d1934aa28a5e9b413613097a2cfb5f2a`
