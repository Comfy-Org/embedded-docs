> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerCFGpp/zh-TW.md)

SamplerEulerCFGpp 節點提供了一種用於生成輸出的 Euler CFG++ 採樣方法。此節點提供兩種不同實作版本的 Euler CFG++ 採樣器，可根據使用者偏好進行選擇。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `版本` | STRING | 是 | `"regular"`<br>`"alternative"` | 要使用的 Euler CFG++ 採樣器實作版本 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已配置的 Euler CFG++ 採樣器實例 |