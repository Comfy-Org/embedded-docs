# 懶快取

LazyCache 是 EasyCache 的自行修改版本，提供更簡便的實作方式。它可與 ComfyUI 中的任何模型搭配使用，並加入快取功能以減少取樣期間的計算量。雖然整體效能通常不如 EasyCache，但在某些罕見情況下可能更有效，且具備通用相容性。

## 輸入

| 參數 | 說明 | 資料型態 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用 LazyCache 的模型。 | MODEL | 是 | - |
| `reuse_threshold` | 重複使用已快取步驟的門檻值（預設值：0.2）。 | FLOAT | 否 | 0.0 - 3.0 |
| `start_percent` | 開始使用 LazyCache 的相對取樣步驟（預設值：0.15）。 | FLOAT | 否 | 0.0 - 1.0 |
| `end_percent` | 結束使用 LazyCache 的相對取樣步驟（預設值：0.95）。 | FLOAT | 否 | 0.0 - 1.0 |
| `verbose` | 是否記錄詳細資訊（預設值：False）。 | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料型態 |
| --- | --- | --- |
| `model` | 已加入 LazyCache 功能的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/zh-TW.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
