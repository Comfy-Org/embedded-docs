> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/zh-TW.md)

## 概述

LazyCache 是 EasyCache 的自製版本，提供了更簡便的實作方式。它可與 ComfyUI 中的任何模型搭配使用，並加入快取功能以減少取樣過程中的計算量。雖然其效能通常不如 EasyCache，但在某些罕見情況下可能更有效，且具有通用相容性。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 要加入 LazyCache 功能的模型。 |
| `reuse_threshold` | FLOAT | 否 | 0.0 - 3.0 | 重複使用快取步驟的閾值（預設值：0.2）。 |
| `start_percent` | FLOAT | 否 | 0.0 - 1.0 | 開始使用 LazyCache 的相對取樣步驟（預設值：0.15）。 |
| `end_percent` | FLOAT | 否 | 0.0 - 1.0 | 結束使用 LazyCache 的相對取樣步驟（預設值：0.95）。 |
| `verbose` | BOOLEAN | 否 | - | 是否記錄詳細資訊（預設值：False）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已加入 LazyCache 功能的模型。 |

---
**Source fingerprint (SHA-256):** `72a5e85b7cf517e88583fc1b75d3ab4a5d40fe8604d50c34f555e677d2ea9e51`
