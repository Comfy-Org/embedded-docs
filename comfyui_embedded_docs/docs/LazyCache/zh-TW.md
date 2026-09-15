# 懶快取

LazyCache 是 EasyCache 的實驗性、自製版本，會在取樣期間加入快取以減少運算。它設計為可與 ComfyUI 中的模型通用相容，不過其表現通常不如 EasyCache，且可能僅在少數情況下運作得更好。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要加入 LazyCache 的模型。 | MODEL | 是 | - |
| `重複使用閾值` | 重複使用快取步驟的閾值。預設：0.2。 | FLOAT | 是 | 0.0 - 3.0 （步進值：0.01） |
| `起始百分比` | 開始使用 LazyCache 的相對取樣進度。預設：0.15。 | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `結束百分比` | 結束使用 LazyCache 的相對取樣進度。預設：0.95。 | FLOAT | 是 | 0.0 - 1.0 （步進值：0.01） |
| `詳細模式` | 是否記錄詳細資訊。預設：False。 | BOOLEAN | 是 | - |

注意：`reuse_threshold`、`start_percent`、`end_percent` 和 `verbose` 被標記為進階輸入。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已加入 LazyCache 功能的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LazyCache/zh-TW.md)

---
**Source fingerprint (SHA-256):** `78f9c13473567e068fc2be35b2f8f5aa459d43d3f13300a6ea858af98d3e2a44`
