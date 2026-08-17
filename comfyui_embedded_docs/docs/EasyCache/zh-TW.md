# EasyCache

EasyCache 節點為模型實作了原生快取系統，透過在取樣過程中重複使用先前已計算的步驟來提升效能。它為模型加入 EasyCache 功能，並可設定在取樣時間軸上開始及停止使用快取的臨界值。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要加入 EasyCache 的模型。 | MODEL | 是 | - |
| `reuse_threshold` | 重複使用已快取步驟的臨界值（預設值：0.2）。 | FLOAT | 是 | 0.0 - 3.0 |
| `start_percent` | 開始使用 EasyCache 的相對取樣步驟（預設值：0.15）。 | FLOAT | 是 | 0.0 - 1.0 |
| `end_percent` | 結束使用 EasyCache 的相對取樣步驟（預設值：0.95）。 | FLOAT | 是 | 0.0 - 1.0 |
| `verbose` | 是否記錄詳細資訊（預設值：False）。 | BOOLEAN | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `model` | 帶有 EasyCache 的模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/zh-TW.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
