> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/zh-TW.md)

SaveAudioOpus 節點將音訊資料儲存為 Opus 格式檔案。它接收音訊輸入並將其匯出為具有可配置品質設定的壓縮 Opus 檔案。該節點會自動處理檔案命名，並將輸出儲存到指定的輸出目錄。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | - | 要儲存為 Opus 檔案的音訊資料 |
| `filename_prefix` | STRING | 否 | - | 輸出檔案名稱的前綴（預設值："audio/ComfyUI"） |
| `quality` | COMBO | 否 | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" | Opus 檔案的音訊品質設定（預設值："128k"） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| - | - | 此節點不會傳回任何輸出值，其主要功能是將音訊檔案儲存至磁碟。 |