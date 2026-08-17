# 儲存音訊（進階）

將輸入的音訊儲存至您的 ComfyUI 輸出目錄。您可以將音訊匯出為 FLAC、MP3 或 Opus 格式，並可為 MP3 與 Opus 檔案選擇品質設定。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `format` | 儲存音訊時所使用的檔案格式。 | DYNAMIC_COMBO | 是 | "flac"<br>"mp3"<br>"opus" |
| `audio` | 要儲存的音訊。 | AUDIO | 是 | - |
| `filename_prefix` | 要儲存檔案的檔案名稱前綴。可包含格式化記號，例如 %date:yyyy-MM-dd%。（預設值："audio/ComfyUI"） | STRING | 是 | - |

### flac 輸入

`flac` 格式不需要任何額外設定。

### mp3 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `quality` | MP3 檔案的編碼品質。（預設值："V0"） | COMBO | 是 | "V0"<br>"128k"<br>"320k" |

### opus 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `quality` | Opus 檔案的編碼品質。（預設值："128k"） | COMBO | 是 | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" |

**注意：** 只有在 `format` 為 `mp3` 或 `opus` 時，`quality` 設定才會顯示。若未提供 `quality` 值，音訊會以所選格式的預設品質儲存。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `audio` | 輸入的音訊，在儲存後原樣傳遞。 | AUDIO |
| `ui` | 包含已儲存音訊檔案資訊的 UI 輸出。 | UI |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioAdvanced/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5f3af49670b485bbd31f0ed0c5667c12e9b9b23014cadcf64442a486255d0e6d`
