# FluxKontext 多重參考潛在方法

FluxKontextMultiReferenceLatentMethod 節點透過設定特定的參考潛在變數方法（reference latents method）來修改 conditioning 資料。它會將所選方法附加到 conditioning 輸入，影響後續生成步驟中參考潛在變數的處理方式。此節點標記為實驗性功能，並屬於 Flux conditioning 系統的一部分。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `conditioning` | 要使用參考潛在變數方法修改的 conditioning 資料 | CONDITIONING | 是 | - |
| `reference_latents_method` | 用於參考潛在變數處理的方法。如果選取了「uxo」或「uso」，會轉換為「uxo」。此參數標記為進階選項。 | COMBO | 是 | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `conditioning` | 已套用參考潛在變數方法並修改後的 conditioning 資料 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
