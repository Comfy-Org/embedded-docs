# SaveText

## 概述

儲存文字節點將文字內容寫入輸出目錄中的檔案。它支援以 .txt、.md 或 .json 格式儲存，並在提供有效 JSON 時自動處理 JSON 美化排版。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text` | 要儲存到檔案的文字內容 | STRING | 是 | - |
| `filename_prefix` | 輸出檔案名稱的前綴（預設："ComfyUI"） | STRING | 否 | - |
| `format` | 儲存文字的檔案格式（預設："txt"） | STRING | 否 | `"txt"`<br>`"md"`<br>`"json"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `text` | 已儲存到檔案的原始文字內容 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveText/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5644d143f415773115b38d7af6d9afea20c9eadef2cea836b0384c15e0dcba6a`
