> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetImageSize/zh-TW.md)

{heading_overview}

GetImageSize 節點從輸入圖像中提取尺寸和批次資訊。它會返回圖像的寬度、高度和批次大小，同時在節點介面上以進度文字顯示此資訊。原始圖像數據會保持不變地通過。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要從中提取尺寸資訊的輸入圖像 |
| `unique_id` | UNIQUE_ID | 否 | - | 用於顯示進度資訊的內部識別碼 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `width` | INT | 輸入圖像的寬度（以像素為單位） |
| `height` | INT | 輸入圖像的高度（以像素為單位） |
| `batch_size` | INT | 批次中的圖像數量 |