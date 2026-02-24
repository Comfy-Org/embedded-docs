> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/zh-TW.md)

此節點透過調整圖像尺寸來重新調整圖像大小，使較短邊的長度符合指定的目標值。它會計算新的尺寸以維持原始圖像的長寬比，並返回調整後的圖像。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 需要調整大小的輸入圖像。 |
| `shorter_edge` | INT | 否 | 1 至 8192 | 較短邊的目標長度。（預設值：512） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `image` | IMAGE | 調整大小後的圖像。 |
