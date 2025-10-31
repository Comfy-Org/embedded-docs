> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Morphology/zh-TW.md)

Morphology 節點對影像套用各種形態學運算，這些是用於處理和分析影像中形狀的數學運算。它可以使用可自訂的核大小來執行侵蝕、膨脹、開運算、閉運算等操作，以控制效果強度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `影像` | IMAGE | 是 | - | 要處理的輸入影像 |
| `操作` | STRING | 是 | `"erode"`<br>`"dilate"`<br>`"open"`<br>`"close"`<br>`"gradient"`<br>`"bottom_hat"`<br>`"top_hat"` | 要套用的形態學運算 |
| `核心大小` | INT | 否 | 3-999 | 結構元素核的大小（預設值：3） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `影像` | IMAGE | 套用形態學運算後處理過的影像 |