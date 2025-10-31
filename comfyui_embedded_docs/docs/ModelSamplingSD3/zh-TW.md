> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/zh-TW.md)

ModelSamplingSD3 節點將 Stable Diffusion 3 採樣參數應用至模型。它透過調整控制採樣分佈特性的位移參數來修改模型的採樣行為。該節點會建立輸入模型的修改副本，並套用指定的採樣配置。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要套用 SD3 採樣參數的輸入模型 |
| `偏移` | FLOAT | 是 | 0.0 - 100.0 | 控制採樣位移參數（預設值：3.0） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已套用 SD3 採樣參數的修改後模型 |