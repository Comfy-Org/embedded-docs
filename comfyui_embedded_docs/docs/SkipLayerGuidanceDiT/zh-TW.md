> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SkipLayerGuidanceDiT/zh-TW.md)

## 節點概述

透過使用另一組跳過層級的 CFG 負向提示來增強對細節結構的引導。這個通用版本的 SkipLayerGuidance 可用於所有 DiT 模型，靈感來自 Perturbed Attention Guidance。最初的實驗性實現是為 SD3 創建的。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用跳過層級引導的模型 |
| `double_layers` | STRING | 是 | - | 用逗號分隔的雙層區塊編號（預設值："7, 8, 9"） |
| `single_layers` | STRING | 是 | - | 用逗號分隔的單層區塊編號（預設值："7, 8, 9"） |
| `scale` | FLOAT | 是 | 0.0 - 10.0 | 引導縮放係數（預設值：3.0） |
| `start_percent` | FLOAT | 是 | 0.0 - 1.0 | 引導應用的起始百分比（預設值：0.01） |
| `end_percent` | FLOAT | 是 | 0.0 - 1.0 | 引導應用的結束百分比（預設值：0.15） |
| `rescaling_scale` | FLOAT | 是 | 0.0 - 10.0 | 重新縮放比例係數（預設值：0.0） |

**注意：** 如果 `double_layers` 和 `single_layers` 都為空（不包含任何層級編號），節點將返回原始模型而不應用任何引導。

## 輸出結果

| 輸出名稱 | 資料類型 | 輸出說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用跳過層級引導的修改後模型 |