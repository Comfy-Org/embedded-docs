> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/zh-TW.md)

ModelComputeDtype 節點允許您在推理過程中變更模型使用的計算資料型別。它會建立輸入模型的副本並套用指定的資料型別設定，這有助於根據您的硬體能力優化記憶體使用和效能。此功能在除錯和測試不同精度設定時特別有用。

## 輸入參數

| 參數名稱 | 資料型別 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用新計算資料型別的輸入模型 |
| `dtype` | STRING | 是 | "default"<br>"fp32"<br>"fp16"<br>"bf16" | 要套用至模型的計算資料型別 |

## 輸出結果

| 輸出名稱 | 資料型別 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用新計算資料型別的修改後模型 |