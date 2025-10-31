> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/zh-TW.md)

{heading_overview}

Load Video 節點從輸入目錄載入視訊檔案，使其可在工作流程中進行處理。它從指定的輸入資料夾讀取視訊檔案，並將其輸出為可連接至其他視訊處理節點的視訊資料。

{heading_inputs}

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `檔案` | STRING | 是 | 提供多個選項 | 要從輸入目錄載入的視訊檔案 |

**注意：** `file` 參數的可用選項是根據輸入目錄中現有的視訊檔案動態生成的。僅會顯示支援內容類型的視訊檔案。

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `video` | VIDEO | 已載入的視訊資料，可傳遞至其他視訊處理節點 |