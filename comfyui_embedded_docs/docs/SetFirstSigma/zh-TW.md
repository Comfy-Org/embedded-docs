> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetFirstSigma/zh-TW.md)

SetFirstSigma 節點透過將序列中的第一個 sigma 值替換為自定義值，來修改 sigma 值序列。它接收現有的 sigma 序列和一個新的 sigma 值作為輸入，然後返回一個新的 sigma 序列，其中僅第一個元素被更改，而所有其他 sigma 值保持不變。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | 是 | - | 待修改的輸入 sigma 值序列 |
| `sigma` | FLOAT | 是 | 0.0 至 20000.0 | 要設定為序列中第一個元素的新 sigma 值（預設值：136.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 經修改的 sigma 序列，其中第一個元素已被自定義 sigma 值替換 |