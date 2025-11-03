> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/zh-TW.md)

ModelSamplingAuraFlow 節點對擴散模型應用專用的採樣配置，特別針對 AuraFlow 模型架構設計。它透過應用調整採樣分佈的偏移參數來修改模型的採樣行為。此節點繼承自 SD3 模型採樣框架，並提供對採樣過程的細緻控制。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要應用 AuraFlow 採樣配置的擴散模型 |
| `shift` | FLOAT | 是 | 0.0 - 100.0 | 應用於採樣分佈的偏移值（預設值：1.73） |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `model` | MODEL | 已應用 AuraFlow 採樣配置的修改後模型 |