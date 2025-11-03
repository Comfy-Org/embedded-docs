> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/zh-TW.md)

UNetTemporalAttentionMultiply 節點用於對時序 UNet 模型中的不同類型注意力機制施加乘法因子。該節點透過調整自注意力層和交叉注意力層的權重來修改模型，並區分結構組件和時序組件。這使得能夠微調每種注意力類型對模型輸出的影響程度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要使用注意力乘數修改的輸入模型 |
| `self_structural` | FLOAT | 否 | 0.0 - 10.0 | 自注意力結構組件的乘數（預設值：1.0） |
| `self_temporal` | FLOAT | 否 | 0.0 - 10.0 | 自注意力時序組件的乘數（預設值：1.0） |
| `cross_structural` | FLOAT | 否 | 0.0 - 10.0 | 交叉注意力結構組件的乘數（預設值：1.0） |
| `cross_temporal` | FLOAT | 否 | 0.0 - 10.0 | 交叉注意力時序組件的乘數（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 經過調整注意力權重後的修改模型 |