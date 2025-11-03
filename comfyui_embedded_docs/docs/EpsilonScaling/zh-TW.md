> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/zh-TW.md)

此節點實作來自研究論文《闡明擴散模型中的曝光偏差》的 Epsilon Scaling 方法。該方法透過在取樣過程中縮放預測噪聲來提升樣本品質。它使用統一排程來減輕擴散模型中的曝光偏差問題。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用 epsilon scaling 的模型 |
| `scaling_factor` | FLOAT | 否 | 0.5 - 1.5 | 用於縮放預測噪聲的係數（預設值：1.005） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用 epsilon scaling 的模型 |