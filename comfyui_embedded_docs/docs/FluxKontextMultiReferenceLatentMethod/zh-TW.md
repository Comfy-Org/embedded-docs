> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/zh-TW.md)

## 概述

FluxKontextMultiReferenceLatentMethod 節點透過設定特定的參考潛在方法來修改條件化資料。它將所選方法附加到條件化輸入中，影響後續生成步驟中參考潛在的處理方式。此節點標記為實驗性功能，屬於 Flux 條件化系統的一部分。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `conditioning` | CONDITIONING | 是 | - | 要使用參考潛在方法修改的條件化資料 |
| `reference_latents_method` | STRING | 是 | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` | 用於參考潛在處理的方法。如果選擇 "uxo" 或 "uso"，將被轉換為 "uxo"。此參數標記為進階選項。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `conditioning` | CONDITIONING | 已套用參考潛在方法的修改後條件化資料 |

---
**Source fingerprint (SHA-256):** `9d39a8fee08ae347a745b20b3dc39051ee2f4645392e769247ae32be35491048`
