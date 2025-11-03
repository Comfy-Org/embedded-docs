> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleFastNode/zh-TW.md)

快速透過 Stability API 呼叫將影像放大至原始尺寸的 4 倍。此節點專門用於將低品質或壓縮影像發送至 Stability AI 的快速放大服務進行影像放大。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 需要進行放大的輸入影像 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | IMAGE | 從 Stability AI API 返回的放大後影像 |