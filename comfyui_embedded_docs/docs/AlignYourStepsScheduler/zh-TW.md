> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AlignYourStepsScheduler/zh-TW.md)

AlignYourStepsScheduler 節點根據不同的模型類型生成去噪過程所需的 sigma 值。它會計算採樣過程每個步驟的適當噪聲水平，並根據去噪參數調整總步數。這有助於使採樣步驟與不同擴散模型的特定要求對齊。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model_type` | STRING | COMBO | - | SD1, SDXL, SVD | 指定用於 sigma 計算的模型類型 |
| `步驟數` | INT | INT | 10 | 1-10000 | 要生成的採樣步驟總數 |
| `去雜訊強度` | FLOAT | FLOAT | 1.0 | 0.0-1.0 | 控制圖像的去噪程度，1.0 表示使用所有步驟，較低值則使用較少步驟 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sigmas` | SIGMAS | 返回為去噪過程計算出的 sigma 值 |