> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/zh-TW.md)

從指定目錄載入一批影像及其對應的文字描述，用於訓練目的。此節點會自動搜尋影像檔案及其關聯的文字描述檔案，根據指定的調整大小設定處理影像，並使用提供的 CLIP 模型對文字描述進行編碼。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | 是 | - | 要載入影像的來源資料夾。 |
| `clip` | CLIP | 是 | - | 用於文字編碼的 CLIP 模型。 |
| `resize_method` | COMBO | 否 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | 用於調整影像大小的方法（預設值："None"）。 |
| `width` | INT | 否 | -1 至 10000 | 要調整影像的目標寬度。-1 表示使用原始寬度（預設值：-1）。 |
| `height` | INT | 否 | -1 至 10000 | 要調整影像的目標高度。-1 表示使用原始高度（預設值：-1）。 |

**注意：** CLIP 輸入必須有效且不能為 None。如果 CLIP 模型來自檢查點載入器節點，請確保檢查點包含有效的 CLIP 或文字編碼器模型。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 已載入並處理完成的影像批次。 |
| `CONDITIONING` | CONDITIONING | 從文字描述編碼而來的條件化資料。 |