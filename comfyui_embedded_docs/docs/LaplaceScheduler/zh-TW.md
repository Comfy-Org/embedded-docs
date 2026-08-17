# Laplace 排程器

LaplaceScheduler 節點會產生一組遵循拉普拉斯分佈的 sigma 值序列，用於擴散採樣。它建立一個噪音水平排程，從最大值逐漸下降到最小值，並使用拉普拉斯分佈參數來控制進程。此排程器常用於自訂採樣工作流程中，以定義擴散模型的噪音排程。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `steps` | 排程中的採樣步驟數（預設值：20） | INT | 是 | 1 to 10000 |
| `sigma_max` | 排程開始時的最大 sigma 值（預設值：14.614642） | FLOAT | 是 | 0.0 to 5000.0 |
| `sigma_min` | 排程結束時的最小 sigma 值（預設值：0.0291675） | FLOAT | 是 | 0.0 to 5000.0 |
| `mu` | 拉普拉斯分佈的平均值參數（預設值：0.0） | FLOAT | 是 | -10.0 to 10.0 |
| `beta` | 拉普拉斯分佈的尺度參數（預設值：0.5） | FLOAT | 是 | 0.0 to 10.0 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `SIGMAS` | 遵循拉普拉斯分佈排程的 sigma 值序列 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
