> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/zh-TW.md)

此節點從 ComfyUI 輸入目錄內的指定子資料夾載入多張圖片。它會掃描所選資料夾中的常見圖片檔案類型，並將其作為清單返回，這對於批次處理或資料集準備非常有用。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | 是 | *提供多個選項* | 要從中載入圖片的資料夾。選項為 ComfyUI 主輸入目錄中存在的子資料夾。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `images` | IMAGE | 已載入的圖片清單。此節點會載入在所選資料夾中找到的所有有效圖片檔案（PNG、JPG、JPEG、WEBP）。 |
