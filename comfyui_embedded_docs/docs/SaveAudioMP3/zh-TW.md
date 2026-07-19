# 儲存音訊 (MP3)

SaveAudioMP3 節點可將音訊資料儲存為 MP3 檔案。它接收音訊輸入，並將其匯出至指定的輸出目錄，同時提供可自訂的檔案名稱與品質設定。此節點會自動處理檔案命名與格式轉換，以建立可播放的 MP3 檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要儲存為 MP3 檔案的音訊資料 | AUDIO | 是 | - |
| `filename_prefix` | 輸出檔案名稱的前綴（預設值："audio/ComfyUI"） | STRING | 否 | - |
| `quality` | MP3 檔案的音訊品質設定（預設值："V0"） | STRING | 否 | "V0"<br>"128k"<br>"320k" |
| `prompt` | 內部提示資料（由系統自動提供） | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的 PNG 資訊（由系統自動提供） | EXTRA_PNGINFO | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| *無* | 此節點不返回任何輸出資料，但會將音訊檔案儲存至輸出目錄 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `70b960cc9c86ad9a4c98e643f40e6caaafdeb9840ac72a5f8e59533fd6120e3e`
