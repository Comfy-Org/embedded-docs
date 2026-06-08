## 概述

ModelSamplingSD3 節點會將 Stable Diffusion 3 的取樣參數套用至模型。它透過調整 shift 參數來修改模型的取樣行為，進而控制取樣分佈特性。此節點會建立輸入模型的修改副本，並套用指定的取樣配置。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 SD3 取樣參數的輸入模型 | MODEL | 是 | - |
| `偏移` | 控制取樣偏移參數（預設值：3.0） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 SD3 取樣參數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingSD3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aa2172d578badffb0a728308b0d3aae4d048db074336963965264d5e512a0d93`
