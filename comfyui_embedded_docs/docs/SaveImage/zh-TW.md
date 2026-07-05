# 儲存圖片

## 概述

SaveImage 節點會將接收到的影像儲存至您的 `ComfyUI/output` 目錄。它會將每張影像儲存為 PNG 檔案，並可將工作流程元資料（例如提示詞）嵌入到儲存的檔案中，以供日後參考。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `影像` | 要儲存的影像。 | IMAGE | 是 | - |
| `檔名前綴` | 儲存檔案的檔案名稱前綴。這可能包含格式化資訊，例如 `%date:yyyy-MM-dd%` 或 `%Empty Latent Image.width%`，以包含來自節點的值（預設值："ComfyUI"）。 | STRING | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `images` | 此節點輸出一個 UI 結果，其中包含已儲存影像的清單及其檔案名稱和子資料夾。它不會輸出用於連接到其他節點的資料。 | UI_RESULT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fa88c26e5e03f788dcc545434a54124c5e9d03b559da67f0857b52faec0e97e7`
