> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/zh-TW.md)

## 概述

ComboOptionTestNode 是一個邏輯節點，設計用於測試並傳遞下拉式選單的選擇結果。它接收兩個下拉式選單輸入，每個選單都有一組預定義的選項，並直接輸出選取的值而不進行任何修改。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | 是 | `"option1"`<br>`"option2"`<br>`"option3"` | 從一組三個測試選項中進行的第一個選擇。 |
| `combo2` | COMBO | 是 | `"option4"`<br>`"option5"`<br>`"option6"` | 從另一組三個測試選項中進行的第二個選擇。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output_1` | COMBO | 輸出從第一個下拉式選單（`combo`）中選取的值。 |
| `output_2` | COMBO | 輸出從第二個下拉式選單（`combo2`）中選取的值。 |

---
**Source fingerprint (SHA-256):** `2f5a73eb7c2962a983b12688159e52d4d05f569d67909f536956ab18a6cc87d7`
