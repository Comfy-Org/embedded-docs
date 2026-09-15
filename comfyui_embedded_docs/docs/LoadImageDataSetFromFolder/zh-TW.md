# 從資料夾載入圖片資料集

此節點會從 ComfyUI 主輸入目錄中所選的子資料夾載入多張影像，並將它們以清單形式傳回。它會掃描所選資料夾中 PNG、JPG、JPEG 或 WEBP 格式的影像檔案，因此適合用於批次處理或準備影像資料集。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `資料夾` | 要從中載入影像的資料夾。選項為 ComfyUI 主輸入目錄中存在的子資料夾。 | COMBO | 是 | 多個選項可用 |

注意：所選資料夾必須是 ComfyUI 主輸入目錄的子資料夾；任何解析後位於該目錄之外的值（例如使用 `..`、絕對路徑、磁碟機代號或符號連結）都會被拒絕。只有副檔名為 .png、.jpg、.jpeg 或 .webp 的檔案會被載入，且副檔名檢查不分大小寫。載入的影像會轉換為 RGB，並縮放到 0 到 1 的範圍。如果所選資料夾中沒有有效影像檔案，此節點會引發錯誤。此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `images` | 已載入影像的清單。此節點會載入所選資料夾中找到的所有有效影像檔案（PNG、JPG、JPEG、WEBP）。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
