> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/zh-TW.md)

ModelSamplingFlux 節點透過根據圖像尺寸計算偏移參數，將 Flux 模型採樣應用於指定模型。它會建立一個專門的採樣配置，根據指定的寬度、高度和偏移參數調整模型行為，然後返回應用新採樣設定的修改後模型。

## 輸入參數

| 參數名稱 | 資料類型 | 是否必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用 Flux 採樣的模型 |
| `max_shift` | FLOAT | 是 | 0.0 - 100.0 | 採樣計算的最大偏移值（預設值：1.15） |
| `base_shift` | FLOAT | 是 | 0.0 - 100.0 | 採樣計算的基礎偏移值（預設值：0.5） |
| `width` | INT | 是 | 16 - MAX_RESOLUTION | 目標圖像的寬度（單位：像素，預設值：1024） |
| `height` | INT | 是 | 16 - MAX_RESOLUTION | 目標圖像的高度（單位：像素，預設值：1024） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 Flux 採樣配置的修改後模型 |