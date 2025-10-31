> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveFloat/zh-TW.md)

PrimitiveFloat 節點用於建立浮點數值，可在工作流程中使用。它接收單一數值輸入並輸出相同的值，讓您能在 ComfyUI 流程中的不同節點之間定義和傳遞浮點數值。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `數值` | FLOAT | 是 | -sys.maxsize 到 sys.maxsize | 要輸出的浮點數值 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | FLOAT | 輸入的浮點數值 |