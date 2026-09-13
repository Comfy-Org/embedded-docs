# 儲存音訊 (Opus)

SaveAudioOpus 節點會將音訊資料以 Opus 格式儲存到檔案，讓你選擇編碼品質（位元率）以及匯出檔案的檔名前綴。此節點已棄用，未來版本可能會移除。

## 輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要儲存為 Opus 檔案的音訊資料。若此值為 None（例如來源影片沒有音軌），會引發 ValueError。 | AUDIO | 是 | - |
| `filename_prefix` | 用於輸出檔名的前綴（預設值："audio/ComfyUI"）。 | STRING | 否 | - |
| `quality` | 用於編碼 Opus 檔案的位元率；數值越高品質越好，但檔案也越大（預設值："128k"）。 | COMBO | 否 | `"64k"`<br>`"96k"`<br>`"128k"`<br>`"192k"`<br>`"320k"` |

## 輸出

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `audio` | 已儲存到 Opus 檔案的音訊資料。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a2f585f45299759738fa85f6b73f51680d4e86da57d3fc9c2236e66114fa3d6c`
