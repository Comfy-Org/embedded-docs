# 模型取樣 Flux

## 概述

ModelSamplingFlux 節點透過根據影像尺寸計算偏移參數，將 Flux 模型取樣應用於給定的模型。它會建立一個專門的取樣配置，根據指定的寬度、高度和偏移參數調整模型的行為，然後傳回已套用新取樣設定的修改後模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 Flux 取樣的模型 | MODEL | 是 | - |
| `最大偏移` | 取樣計算的最大偏移值（預設值：1.15） | FLOAT | 是 | 0.0 - 100.0 |
| `基礎偏移` | 取樣計算的基礎偏移值（預設值：0.5） | FLOAT | 是 | 0.0 - 100.0 |
| `寬度` | 目標影像的寬度（像素為單位）（預設值：1024） | INT | 是 | 16 - MAX_RESOLUTION |
| `高度` | 目標影像的高度（像素為單位）（預設值：1024） | INT | 是 | 16 - MAX_RESOLUTION |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 Flux 取樣配置的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingFlux/zh-TW.md)

---
**Source fingerprint (SHA-256):** `35733ab0cd032884ceada13715cf51e626586844e8e575471a5ba7cf8a1e5e49`
