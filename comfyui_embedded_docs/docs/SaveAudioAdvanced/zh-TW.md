# 儲存音訊（進階）

將輸入的音訊儲存至您的 ComfyUI 輸出目錄。此節點允許您以多種格式匯出音訊，包括 FLAC、MP3 和 Opus，並可設定品質參數。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要儲存的音訊。 | AUDIO | 是 | - |
| `filename_prefix` | 要儲存檔案的前綴。可包含格式化標記，例如 %date:yyyy-MM-dd%。（預設值："audio/ComfyUI"） | STRING | 是 | - |
| `format` | 儲存音訊的檔案格式。 | COMBO | 是 | "flac"<br>"mp3"<br>"opus" |

當選擇 "mp3" 作為格式時，將提供一個 `quality` 子參數，選項如下："V0"、"128k"、"320k"（預設值："V0"）。

當選擇 "opus" 作為格式時，將提供一個 `quality` 子參數，選項如下："64k"、"96k"、"128k"、"192k"、"320k"（預設值："128k"）。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `ui` | 包含已儲存音訊檔案資訊的 UI 輸出。 | UI |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `98314263dd84c562e7c02ba89f3d10551fcb898ac784af2aa397ca8357e4aae8`
