> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/zh-TW.md)

VideoTriangleCFGGuidance 節點對影片模型應用三角形分類器自由引導縮放模式。它使用在最小 CFG 值和原始條件縮放值之間振盪的三角波函數，隨時間調整條件縮放。這種動態引導模式有助於提升影片生成的一致性和品質。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用三角形 CFG 引導的影片模型 |
| `min_cfg` | FLOAT | 是 | 0.0 - 100.0 | 三角形模式的最小 CFG 縮放值（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用三角形 CFG 引導的修改後模型 |