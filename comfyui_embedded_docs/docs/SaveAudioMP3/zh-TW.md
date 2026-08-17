# 儲存音訊 (MP3)

SaveAudioMP3 節點會將音訊資料儲存為 MP3 檔案。它接收音訊輸入，並以可自訂的檔案名稱前置詞與品質設定，將其寫入輸出目錄。此節點已棄用，可能會在未來版本中移除。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要另存為 MP3 檔案的音訊資料 | AUDIO | 是 | - |
| `filename_prefix` | 輸出檔案名稱的前置詞（預設值："audio/ComfyUI"） | STRING | 否 | - |
| `quality` | MP3 編碼品質設定（預設值："V0"）。V0 使用可變位元率以獲得高品質；128k 和 320k 使用固定位元率，分別為 128 和 320 kbps | COMBO | 否 | `"V0"`<br>`"128k"`<br>`"320k"` |
| `prompt` | 內部提示資料，由系統自動提供 | PROMPT | 否 | - |
| `extra_pnginfo` | 額外的 PNG 資訊，由系統自動提供 | EXTRA_PNGINFO | 否 | - |

**注意：** 如果 `audio` 輸入為 None（例如，當來源影片沒有音訊軌時），此節點會引發 ValueError。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
|-------------|-------------|-----------|
| `audio` | 已另存為 MP3 檔案的音訊資料 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioMP3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7d3b439dfd7cb211dd6568f6b5124bb225909dcf0ae150addc4ca226d947a4f0`
