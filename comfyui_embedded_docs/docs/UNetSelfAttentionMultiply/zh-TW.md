> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/zh-TW.md)

UNetSelfAttentionMultiply 節點對 UNet 模型中的自注意力機制的查詢、鍵、值和輸出組件應用乘法因子。它允許您縮放注意力計算的不同部分，以實驗注意力權重如何影響模型的行為。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要使用注意力縮放因子修改的 UNet 模型 |
| `q` | FLOAT | 否 | 0.0 - 10.0 | 查詢組件的乘法因子（預設值：1.0） |
| `k` | FLOAT | 否 | 0.0 - 10.0 | 鍵組件的乘法因子（預設值：1.0） |
| `v` | FLOAT | 否 | 0.0 - 10.0 | 值組件的乘法因子（預設值：1.0） |
| `out` | FLOAT | 否 | 0.0 - 10.0 | 輸出組件的乘法因子（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `MODEL` | MODEL | 帶有縮放注意力組件的修改後 UNet 模型 |