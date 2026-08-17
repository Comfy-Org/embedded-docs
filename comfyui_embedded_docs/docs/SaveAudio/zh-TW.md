# 儲存音訊

SaveAudio 節點會將音訊資料以 FLAC 格式儲存至檔案。它接收音訊輸入，使用指定的檔名前綴將其寫入輸出目錄，並將相同的音訊作為輸出傳遞。此節點已棄用，應改用目前的 Save Audio 節點。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `audio` | 要儲存的音訊資料 | AUDIO | 是 | - |
| `filename_prefix` | 輸出檔名的前綴（預設值："audio/ComfyUI"） | STRING | 否 | - |

若 `audio` 為 None，節點會引發錯誤；這可能發生在來源影片沒有音訊軌時。

`prompt` 與 `extra_pnginfo` 參數為隱藏參數，由系統自動處理。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 與儲存至檔案的相同音訊資料 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6ac62d315f14213091cd179a05f0bbd51f1b1a5056bb5c06ca137d2b574d6017`
