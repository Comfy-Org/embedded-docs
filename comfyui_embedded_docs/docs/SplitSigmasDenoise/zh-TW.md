> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitSigmasDenoise/zh-TW.md)

此節點根據去噪強度參數將一系列 sigma 值分成兩部分。它將輸入的 sigma 分割為高 sigma 序列和低 sigma 序列，其中分割點是透過將總步數乘以去噪因子來確定的。這允許將噪聲調度分離為不同強度範圍以進行專門處理。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `sigmas` | SIGMAS | 是 | - | 代表噪聲調度的輸入 sigma 值序列 |
| `去雜訊強度` | FLOAT | 是 | 0.0 - 1.0 | 決定在何處分割 sigma 序列的去噪強度因子 (預設值: 1.0) |

## 輸出參數

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `低 sigmas` | SIGMAS | 包含較高 sigma 值的 sigma 序列第一部分 |
| `low_sigmas` | SIGMAS | 包含較低 sigma 值的 sigma 序列第二部分 |