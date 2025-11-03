> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/zh-TW.md)

SamplerEulerAncestralCFGPP 節點建立了一個專門的取樣器，使用 Euler Ancestral 方法搭配分類器自由引導來生成影像。此取樣器結合了祖先取樣技術與引導條件化，能在保持連貫性的同時產生多樣的影像變化。它允許透過控制噪聲和步長調整的參數來微調取樣過程。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `eta` | FLOAT | 是 | 0.0 - 1.0 | 控制取樣過程中的步長，數值越高代表更新越積極（預設值：1.0） |
| `s_noise` | FLOAT | 是 | 0.0 - 10.0 | 調整取樣過程中添加的噪聲量（預設值：1.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `sampler` | SAMPLER | 返回一個已配置的取樣器物件，可在影像生成流程中使用 |