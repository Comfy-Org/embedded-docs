> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/zh-TW.md)

SamplerEulerAncestral 節點建立了一個用於生成影像的 Euler Ancestral 取樣器。此取樣器採用特定的數學方法，結合了歐拉積分與祖先取樣技術來產生影像變化。該節點允許您透過調整控制生成過程中隨機性和步長大小的參數來配置取樣行為。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程的步長大小和隨機性（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 100.0 | 控制取樣過程中添加的噪聲量（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已配置的 Euler Ancestral 取樣器，可在取樣管線中使用 |