# 隨機雜訊

## 概述

RandomNoise 節點會根據種子值生成隨機噪聲模式。它會建立可重現的噪聲，可用於各種影像處理與生成任務。相同的種子值將始終產生相同的噪聲模式，確保多次執行結果一致。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `noise_seed` | 用於生成隨機噪聲模式的種子值（預設值：0）。相同的種子值將始終產生相同的噪聲輸出。 | INT | 是 | 0 至 18446744073709551615 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `noise` | 根據提供的種子值生成的隨機噪聲模式。 | NOISE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RandomNoise/zh-TW.md)

---
**Source fingerprint (SHA-256):** `893d3eefdef78592ba3cc403ec1e4bf3a672607abe79f05db1b65078d6b9ea20`
