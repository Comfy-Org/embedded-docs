> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/zh-TW.md)

{heading_overview}

LoadImageSetFromFolderNode 從指定的資料夾目錄載入多張影像，用於訓練目的。它會自動偵測常見的影像格式，並可選擇性地在將影像作為批次傳回之前，使用不同的方法調整影像大小。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `folder` | STRING | 是 | 多個選項可用 | 要從中載入影像的資料夾。 |
| `resize_method` | STRING | 否 | "None"<br>"Stretch"<br>"Crop"<br>"Pad" | 用於調整影像大小的方法（預設值："None"）。 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | 已載入的影像批次，作為單一張量。 |