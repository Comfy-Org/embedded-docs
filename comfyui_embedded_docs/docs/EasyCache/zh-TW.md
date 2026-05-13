> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/zh-TW.md)

## 概述

EasyCache 節點為模型實現了原生快取系統，透過在取樣過程中重複使用先前計算的步驟來提升效能。它為模型添加 EasyCache 功能，並可設定在取樣時間軸上開始與停止使用快取的閾值。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `模型` | MODEL | 是 | - | 要添加 EasyCache 功能的模型。 |
| `重用閾值` | FLOAT | 否 | 0.0 - 3.0 | 重複使用快取步驟的閾值（預設值：0.2）。 |
| `起始百分比` | FLOAT | 否 | 0.0 - 1.0 | 開始使用 EasyCache 的相對取樣步驟（預設值：0.15）。 |
| `結束百分比` | FLOAT | 否 | 0.0 - 1.0 | 結束使用 EasyCache 的相對取樣步驟（預設值：0.95）。 |
| `詳細模式` | BOOLEAN | 否 | - | 是否記錄詳細資訊（預設值：False）。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `模型` | MODEL | 已添加 EasyCache 功能的模型。 |

---
**Source fingerprint (SHA-256):** `e9d9bf5ecae8034b562f1a27acf528d1f3241d7d28621beba149d3e9bd66a247`
