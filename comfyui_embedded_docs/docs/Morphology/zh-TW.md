> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/zh-TW.md)

Morphology 節點對影像套用各種形態學操作，這些是基於數學運算的影像處理技術，用於分析和處理影像中的形狀結構。該節點可執行多種操作，包括侵蝕、膨脹、開運算、閉運算等，並可透過自定義的核大小來控制效果強度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `image` | IMAGE | 是 | - | 要進行處理的輸入影像 |
| `operation` | STRING | 是 | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | 要套用的形態學操作類型 |
| `kernel_size` | INT | 否 | 3-999 | 結構元素核的大小（預設值：3） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `image` | IMAGE | 套用形態學操作後處理完成的影像 |