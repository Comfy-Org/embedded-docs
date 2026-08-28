# FluxDisableGuidance

此節點完全停用 Flux 及類似 Flux 模型上的 guidance embed。它接收 conditioning 資料作為輸入，並透過將 guidance 元件設為 None 來移除它，從而有效地關閉生成過程中基於 guidance 的 conditioning。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `條件設定` | 要處理並從中移除 guidance 的 conditioning 資料 | CONDITIONING | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 已停用 guidance 的修改後 conditioning 資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxDisableGuidance/zh-TW.md)

---
**Source fingerprint (SHA-256):** `da3286194f9f5e7e49dd7047d6b0a0c97bb2570eaa9281abbd3992a743302fbf`
