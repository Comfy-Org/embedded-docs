## 概述

SaveAudio 節點可將音訊資料以 FLAC 格式儲存為檔案。它接收音訊輸入，並將其寫入指定的輸出目錄，並使用給定的檔案名稱前綴。該節點會自動處理檔案命名，並確保音訊正確儲存以供後續使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `音訊` | 要儲存的音訊資料 | AUDIO | 是 | - |
| `檔名前綴` | 輸出檔案名稱的前綴（預設值："audio/ComfyUI"） | STRING | 否 | - |

*注意：`prompt` 和 `extra_pnginfo` 參數為隱藏參數，由系統自動處理。*

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| *無* | 此節點不返回任何輸出資料，但會將音訊檔案儲存至輸出目錄 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `16242dfc45d0f2808a5615e9c1bfe4de4d19e2f5f6b28370f631439021dc72e5`
