# 儲存音訊 (Opus)

SaveAudioOpus 節點將音訊資料儲存為 Opus 格式檔案。它接收音訊輸入，並將其匯出為壓縮的 Opus 檔案，且可配置品質設定。此節點已棄用，未來版本可能會移除。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要儲存為 Opus 檔案的音訊資料。若未提供音訊（例如來源影片沒有音訊軌），節點會引發錯誤。 | AUDIO | 是 | - |
| `filename_prefix` | 輸出檔案名稱的前綴（預設："audio/ComfyUI"） | STRING | 否 | - |
| `quality` | Opus 檔案的音訊品質（位元率）設定（預設："128k"） | COMBO | 否 | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 輸入的音訊資料，在 Opus 檔案儲存至磁碟後回傳。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
