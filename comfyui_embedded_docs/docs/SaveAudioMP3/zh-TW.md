> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/zh-TW.md)

SaveAudioMP3 節點將音訊資料儲存為 MP3 檔案。它接收音訊輸入，並將其匯出到指定的輸出目錄，同時支援自訂檔案名稱和品質設定。該節點會自動處理檔案命名和格式轉換，以建立可播放的 MP3 檔案。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | - | 要儲存為 MP3 檔案的音訊資料 |
| `filename_prefix` | STRING | 否 | - | 輸出檔名的前綴詞（預設值："audio/ComfyUI"） |
| `quality` | STRING | 否 | "V0"<br>"128k"<br>"320k" | MP3 檔案的音訊品質設定（預設值："V0"） |
| `prompt` | PROMPT | 否 | - | 內部提示資料（由系統自動提供） |
| `extra_pnginfo` | EXTRA_PNGINFO | 否 | - | 額外的 PNG 資訊（由系統自動提供） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| *無* | - | 此節點不會回傳任何輸出資料，但會將音訊檔案儲存到輸出目錄 |