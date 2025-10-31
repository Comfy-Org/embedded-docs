> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGLB/zh-TW.md)

{heading_overview}

SaveGLB 節點將 3D 網格資料儲存為 GLB 檔案，這是一種常見的 3D 模型格式。它接收網格資料作為輸入，並將其匯出到輸出目錄，使用指定的檔案名稱前綴。如果輸入包含多個網格物件，該節點可以儲存多個網格，並在啟用元資料時自動為檔案添加元資料。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `mesh` | MESH | 是 | - | 要儲存為 GLB 檔案的 3D 網格資料 |
| `檔名前綴` | STRING | 否 | - | 輸出檔案名稱的前綴（預設值："mesh/ComfyUI"） |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `ui` | UI | 在使用者介面中顯示已儲存的 GLB 檔案，包含檔案名稱和子資料夾資訊 |