> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAudioOpus/zh-TW.md)

## 概述

SaveAudioOpus 節點可將音訊資料儲存為 Opus 格式檔案。它接收音訊輸入，並以可設定的品質設定將其匯出為壓縮的 Opus 檔案。該節點會自動處理檔案命名，並將輸出儲存至指定的輸出目錄。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | - | 要儲存為 Opus 檔案的音訊資料 |
| `filename_prefix` | STRING | 否 | - | 輸出檔案名稱的前綴（預設值："audio/ComfyUI"） |
| `quality` | COMBO | 否 | "64k"<br>"96k"<br>"128k"<br>"192k"<br>"320k" | Opus 檔案的音訊品質設定（預設值："128k"） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| - | - | 此節點不返回任何輸出值。其主要功能是將音訊檔案儲存至磁碟。 |

---
**Source fingerprint (SHA-256):** `87c3b1b85ca51b79d43c8486eeb2de7b074faa11c4da2bff7b8931a3049560e2`
