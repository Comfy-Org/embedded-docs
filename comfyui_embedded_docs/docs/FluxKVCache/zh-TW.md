> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKVCache/zh-TW.md)

Flux KV 快取節點可為 Flux 系列模型啟用鍵值（KV）快取最佳化。此最佳化透過快取特定計算來提升使用參考影像時的效能，從而加速生成過程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | | 要套用 KV 快取最佳化的模型。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `model` | MODEL | 已啟用 KV 快取最佳化的修補後模型。 |

---
**Source fingerprint (SHA-256):** `530c660ae23607d4035815826ae73cdcbebe7693ba47a3b0fe98e69f329b9e86`
