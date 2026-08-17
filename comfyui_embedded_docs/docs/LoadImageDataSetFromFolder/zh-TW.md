# 從資料夾載入圖片資料集

此節點會從選取的資料夾載入影像資料集，並以清單形式傳回。該資料夾必須是 ComfyUI 主輸入目錄內的一個子資料夾。支援的影像格式為 PNG、JPG、JPEG 和 WEBP。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `folder` | 要從中載入影像的資料夾。可用選項為 ComfyUI 主輸入目錄中存在的子資料夾。解析到該目錄之外的值（例如使用「..」）會被拒絕。 | COMBO | Yes | *提供多個選項* — ComfyUI 輸入目錄中存在的子資料夾 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 已載入影像的清單。此節點會載入選取資料夾中找到的所有有效影像檔案（PNG、JPG、JPEG、WEBP），並以清單形式傳回。如果資料夾中沒有任何支援的影像檔案，則會拋出錯誤。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
