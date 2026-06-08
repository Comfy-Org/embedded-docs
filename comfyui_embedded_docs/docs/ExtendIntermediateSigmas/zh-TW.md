## 概述

ExtendIntermediateSigmas 節點會取得現有的 sigma 值序列，並在其中插入額外的中間 sigma 值。您可以指定要添加的額外步驟數量、插值的間距方法，以及可選的起始與結束 sigma 邊界，以控制擴展在 sigma 序列中發生的位置。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `sigmas` | 要擴展中間值的輸入 sigma 序列 | SIGMAS | 是 | - |
| `步驟數` | 在現有 sigma 之間插入的中間步驟數量（預設值：2） | INT | 是 | 1 至 100 |
| `起始 sigma` | 擴展的上限 sigma 邊界 - 僅擴展低於此值的 sigma（預設值：-1.0，表示無限大） | FLOAT | 是 | -1.0 至 20000.0 |
| `結束 sigma` | 擴展的下限 sigma 邊界 - 僅擴展高於此值的 sigma（預設值：12.0） | FLOAT | 是 | 0.0 至 20000.0 |
| `間距` | 用於間隔中間 sigma 值的插值方法（預設值："linear"） | COMBO | 是 | `"linear"`<br>`"cosine"`<br>`"sine"` |

**注意：** 此節點僅在現有 sigma 配對中插入中間 sigma，且該配對的當前 sigma 必須同時小於或等於 `start_at_sigma`，以及大於或等於 `end_at_sigma`。當 `start_at_sigma` 設為 -1.0 時，會被視為無限大，表示僅適用 `end_at_sigma` 的下限邊界。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 已插入額外中間值的擴展 sigma 序列 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExtendIntermediateSigmas/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f51ed433fc38365334ff8e4072174dc04982a8a00770d07f544320a6863577c4`
