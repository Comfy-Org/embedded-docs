# 從資料夾載入圖片資料集

此節點從 ComfyUI 主輸入目錄中選定的子文件夾載入多個圖像，並將它們作為清單返回。它會掃描所選文件夾中的 PNG、JPG、JPEG 或 WEBP 格式圖像檔案，這使其適用於批次處理或準備圖像資料集。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `資料夾` | 要從其中載入圖像的資料夾。選項為 ComfyUI 主輸入目錄中存在的子資料夾。 | COMBO | 是 | 有多個選項可用 |

注意：所選資料夾必須是 ComfyUI 主輸入目錄的子資料夾；任何解析到該目錄之外的值都將被拒絕。僅載入副檔名為 .png、.jpg、.jpeg 或 .webp 的檔案，且副檔名檢查不區分大小寫。如果所選資料夾中沒有有效的圖像檔案，節點將引發錯誤。此節點標記為實驗性。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `圖片` | 已載入圖像的清單。節點會載入所選資料夾中找到的所有有效圖像檔案（PNG、JPG、JPEG、WEBP）。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
