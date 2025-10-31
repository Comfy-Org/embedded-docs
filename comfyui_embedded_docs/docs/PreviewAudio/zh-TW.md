> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAudio/zh-TW.md)

PreviewAudio 節點會生成一個臨時音訊預覽檔案，可在介面中顯示。它繼承自 SaveAudio，但會將檔案儲存到臨時目錄並使用隨機檔案名稱前綴。這讓使用者能快速預覽音訊輸出，而無需建立永久檔案。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `音訊` | AUDIO | 是 | - | 要預覽的音訊資料 |
| `prompt` | PROMPT | 否 | - | 內部使用的隱藏參數 |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 內部使用的隱藏參數 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `ui` | UI | 在介面中顯示音訊預覽 |