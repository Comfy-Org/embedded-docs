# 儲存影片

## 概述

SaveVideo 節點可將輸入的影片內容儲存至您的 ComfyUI 輸出目錄。您可以指定儲存檔案的檔名前綴、影片格式及編碼器。此節點會自動以計數器遞增方式處理檔案命名，並可將工作流程元資料包含在儲存的影片中。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要儲存的影片。 | VIDEO | 是 | - |
| `檔名前綴` | 儲存檔案的檔名前綴。可包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以納入來自節點的值（預設值："video/ComfyUI"）。 | STRING | 否 | - |
| `格式` | 儲存影片的格式（預設值："auto"）。 | COMBO | 否 | `"auto"`<br>`"mp4"`<br>`"webm"`<br>`"mkv"`<br>`"gif"` |
| `編碼器` | 用於影片的編碼器（預設值："auto"）。 | COMBO | 否 | `"auto"`<br>`"h264"`<br>`"h265"`<br>`"vp9"`<br>`"av1"`<br>`"prores"` |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| *無輸出* | 此節點不會回傳任何輸出資料。 | - |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `506ddc8820924688cccb9fd838ff9c0f5217a38f708f28f15a060be9325cea61`
