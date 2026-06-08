## 概述

ModelSamplingAuraFlow 節點將專門的取樣配置應用於擴散模型，專為 AuraFlow 模型架構設計。它透過應用調整取樣分佈的偏移參數來修改模型的取樣行為。此節點繼承自 SD3 模型取樣框架，並提供對取樣過程的精細控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 AuraFlow 取樣配置的擴散模型 | MODEL | 是 | - |
| `偏移` | 套用於取樣分佈的偏移值（預設值：1.73） | FLOAT | 是 | 0.0 - 100.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用 AuraFlow 取樣配置的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingAuraFlow/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f49367534032fb2d697d16e8197c16dc761678a5e39990993bdc864bfccea314`
