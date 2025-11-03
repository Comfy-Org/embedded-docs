> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/zh-TW.md)

此節點會完全停用 Flux 及類似模型的引導嵌入功能。它接收條件化資料作為輸入，並透過將引導組件設為 None 來移除該組件，從而有效關閉生成過程中基於引導的條件化。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 要處理並移除引導功能的條件化資料 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 已停用引導功能的修改後條件化資料 |