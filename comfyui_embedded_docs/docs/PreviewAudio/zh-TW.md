> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/zh-TW.md)

{heading_overview}

PreviewAudio 節點會生成一個臨時音訊預覽檔案，可在介面中顯示。它繼承自 SaveAudio，但會將檔案儲存到臨時目錄並使用隨機檔案名稱前綴。這讓使用者能夠快速預覽音訊輸出，而無需建立永久檔案。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | - | 要預覽的音訊資料 |
| `prompt` | PROMPT | 否 | - | 內部使用的隱藏參數 |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 內部使用的隱藏參數 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `ui` | UI | 在介面中顯示音訊預覽 |