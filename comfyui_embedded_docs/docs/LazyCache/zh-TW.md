# 懶快取

LazyCache 是 EasyCache 的自製版本，提供了更簡便的實作方式。它可與 ComfyUI 中的任何模型搭配使用，並加入快取功能以減少取樣期間的計算量。雖然其整體效能通常不如 EasyCache，但在某些罕見情況下可能更為有效，且具備通用相容性。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要加入 LazyCache 的模型。 | MODEL | 是 | - |
| `重複使用閾值` | 重複使用快取步驟的閾值（預設值：0.2）。 | FLOAT | 否 | 0.0 - 3.0 |
| `起始百分比` | 開始使用 LazyCache 的相對取樣步驟（預設值：0.15）。 | FLOAT | 否 | 0.0 - 1.0 |
| `結束百分比` | 結束使用 LazyCache 的相對取樣步驟（預設值：0.95）。 | FLOAT | 否 | 0.0 - 1.0 |
| `詳細模式` | 是否記錄詳細資訊（預設值：False）。 | BOOLEAN | 否 | - |

注意：`reuse_threshold`、`start_percent`、`end_percent` 和 `verbose` 是選用的進階選項。

## 輸出

| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `model` | 已添加 LazyCache 功能的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/zh-TW.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
