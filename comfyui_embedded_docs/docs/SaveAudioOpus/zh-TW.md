# 儲存音訊 (Opus)

SaveAudioOpus 節點將音訊資料儲存為 Opus 格式的檔案。它接收音訊輸入並將其匯出為壓縮的 Opus 檔案，且可設定品質參數。此節點已棄用，未來版本可能會移除。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要儲存為 Opus 檔案的音訊資料。若此值為 None（例如，當來源影片沒有音訊軌時），會引發 ValueError。 | AUDIO | 是 | - |
| `filename_prefix` | 輸出檔案名稱的字首（預設值："audio/ComfyUI"） | STRING | 否 | - |
| `quality` | 用於編碼 Opus 檔案的位元率；數值愈高，品質愈好但檔案愈大（預設值："128k"） | COMBO | 否 | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 已儲存至 Opus 檔案的音訊資料 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
