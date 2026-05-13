> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/zh-TW.md)

此節點完全停用 Flux 及類似模型的引導嵌入功能。它接收條件化資料作為輸入，並透過將引導元件設為 None 來移除該元件，從而有效關閉生成過程中的引導式條件化。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|----------|--------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 要處理並從中移除引導功能的條件化資料 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 已停用引導功能的修改後條件化資料 |

---
**Source fingerprint (SHA-256):** `37e544460d5e50542cebb451997c0320f16d822cc5695cb34825d2038866a455`
