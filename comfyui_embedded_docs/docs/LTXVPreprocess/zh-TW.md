> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVPreprocess/zh-TW.md)

LTXVPreprocess 節點對影像進行壓縮預處理。它接收輸入影像並以指定的壓縮等級進行處理，輸出已應用壓縮設定的處理後影像。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `影像` | IMAGE | 是 | - | 待處理的輸入影像 |
| `img_compression` | INT | 否 | 0-100 | 應用於影像的壓縮程度（預設值：35） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output_image` | IMAGE | 已應用壓縮處理後的輸出影像 |