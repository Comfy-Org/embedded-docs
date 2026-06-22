# LoadImageTextSetFromFolderNode

從指定目錄載入一批影像及其對應的文字標題，用於訓練目的。此節點會自動搜尋影像檔案及其關聯的標題文字檔，根據指定的調整大小設定處理影像，並使用提供的 CLIP 模型對標題進行編碼。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `folder` | 要載入影像的資料夾。 | STRING | 是 | - |
| `clip` | 用於編碼文字的 CLIP 模型。 | CLIP | 是 | - |
| `resize_method` | 調整影像大小的方法（預設值："None"）。 | COMBO | 否 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |
| `width` | 調整影像的目標寬度。設為 -1 表示使用原始寬度（預設值：-1）。 | INT | 否 | -1 至 10000 |
| `height` | 調整影像的目標高度。設為 -1 表示使用原始高度（預設值：-1）。 | INT | 否 | -1 至 10000 |

**注意：** CLIP 輸入必須有效且不能為 None。如果 CLIP 模型來自檢查點載入節點，請確保檢查點包含有效的 CLIP 或文字編碼器模型。

**關於資料夾結構的注意事項：** 此節點支援 kohya-ss/sd-scripts 資料夾結構。如果子資料夾的名稱以數字開頭並後接底線（例如 `5_myclass`），則該數字會用作重複計數，該子資料夾內的影像將被載入相應次數。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 已載入並處理完成的影像批次。 | IMAGE |
| `CONDITIONING` | 從文字標題編碼而來的條件資料。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`
