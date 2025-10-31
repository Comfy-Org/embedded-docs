> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageOutput/zh-TW.md)

{heading_overview}

LoadImageOutput 節點從輸出資料夾載入圖片。當您點擊重新整理按鈕時，它會更新可用圖片清單並自動選取第一張圖片，讓您可以輕鬆地瀏覽生成的圖片。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `影像` | COMBO | 是 | 多個選項可用 | 從輸出資料夾載入圖片。包含上傳選項和重新整理按鈕，用於更新圖片清單。 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `影像` | IMAGE | 從輸出資料夾載入的圖片 |
| `mask` | MASK | 與載入圖片相關聯的遮罩 |