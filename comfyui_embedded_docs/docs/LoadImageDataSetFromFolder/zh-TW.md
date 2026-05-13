> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/zh-TW.md)

此節點從 ComfyUI 輸入目錄中的指定子資料夾載入多張圖片。它會掃描所選資料夾中常見的圖片檔案類型，並將其作為列表返回，這對於批次處理或資料集準備非常有用。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `資料夾` | STRING | 是 | *提供多個選項* | 要從中載入圖片的資料夾。可選項目為 ComfyUI 主輸入目錄中存在的子資料夾。 |

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `images` | IMAGE | 已載入圖片的列表。此節點會載入在所選資料夾中找到的所有有效圖片檔案（PNG、JPG、JPEG、WEBP）。 |

---
**Source fingerprint (SHA-256):** `0f6e1b3d159f7d7c0c9530350ee057118a2618796f149586bae925253ecc8cf0`
