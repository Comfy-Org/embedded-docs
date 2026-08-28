# Laplace 排程器

LaplaceScheduler 節點會依照拉普拉斯分布產生一系列 sigma 值，用於擴散取樣。它會建立一個從最大值逐漸遞減至最小值的雜訊等級排程，並使用拉普拉斯分布參數來控制進程。此排程器常用於自訂取樣工作流程中，用以定義擴散模型的雜訊排程。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `步驟數` | 排程中的取樣步數（預設值：20） | INT | 是 | 1 至 10000 |
| `最大 sigma` | 排程開始時的最大 sigma 值（預設值：14.614642） | FLOAT | 是 | 0.0 至 5000.0 |
| `最小 sigma` | 排程結束時的最小 sigma 值（預設值：0.0291675） | FLOAT | 是 | 0.0 至 5000.0 |
| `mu` | 拉普拉斯分布的平均值參數（預設值：0.0） | FLOAT | 是 | -10.0 至 10.0 |
| `beta` | 拉普拉斯分布的尺度參數（預設值：0.5） | FLOAT | 是 | 0.0 至 10.0 |

注意：`sigma_max`、`sigma_min`、`mu` 與 `beta` 為進階參數。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `SIGMAS` | 依照拉普拉斯分布排程的一系列 sigma 值 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LaplaceScheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8e5ca00f4797f863a2cf8b9b115ec27beb7f65981cbb04eb036150402fc19389`
