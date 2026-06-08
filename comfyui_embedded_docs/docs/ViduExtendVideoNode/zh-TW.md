ViduExtendVideoNode 會生成額外的影格來延長現有影片的長度。它使用指定的 AI 模型，根據來源影片和可選的文字提示來建立無縫的延續內容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片延伸的 AI 模型。選擇模型後會顯示其特定的持續時間和解析度設定。 | COMBO | 是 | `"viduq2-pro"`<br>`"viduq2-turbo"` |
| `model.duration` | 延伸後影片的持續時間（秒），預設值為 4。此設定在選擇模型後出現。 | INT | 是 | 1 至 7 |
| `model.resolution` | 輸出影片的解析度。此設定在選擇模型後出現。 | COMBO | 是 | `"720p"`<br>`"1080p"` |
| `video` | 要延伸的來源影片。 | VIDEO | 是 | - |
| `prompt` | 可選的文字提示，用於引導延伸影片的內容（最多 2000 個字元，預設為空）。 | STRING | 否 | - |
| `seed` | 用於控制生成隨機性的種子值（預設值為 1）。 | INT | 否 | 0 至 2147483647 |
| `end_frame` | 可選的圖片，用作延伸的目標結束影格。如果提供，其長寬比必須介於 1:4 和 4:1 之間，且尺寸至少為 128x128 像素。 | IMAGE | 否 | - |

**注意：** 來源 `video` 的持續時間必須在 4 到 55 秒之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 新生成的影片檔案，包含延伸後的片段。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduExtendVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `44b942413c8aed2fc0049386a31c441f6f870ba4220b0c439dfc436079229446`
