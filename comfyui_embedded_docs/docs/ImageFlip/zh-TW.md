> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageFlip/zh-TW.md)

ImageFlip 節點可沿不同軸線翻轉圖像。它能沿 x 軸垂直翻轉或沿 y 軸水平翻轉圖像。該節點根據所選方法使用 torch.flip 操作來執行翻轉。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要進行翻轉的輸入圖像 |
| `flip_method` | STRING | 是 | "x-axis: vertically"<br>"y-axis: horizontally" | 要應用的翻轉方向 |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 經過翻轉處理後的輸出圖像 |