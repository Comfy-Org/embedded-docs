# ComboOptionTestNode

ComboOptionTestNode 是一個邏輯節點，旨在測試並傳遞下拉式選單的選取項目。它接受兩個下拉式選單輸入，每個輸入都有一組預先定義的選項，並直接輸出所選值而不做任何修改。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `combo` | 從三個測試選項中進行的第一個選取。 | COMBO | 是 | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | 從另一組三個測試選項中進行的第二個選取。 | COMBO | 是 | `"option4"`<br>`"option5"`<br>`"option6"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output_1` | 輸出從第一個下拉式選單（`combo`）中選取的值。 | COMBO |
| `output_2` | 輸出從第二個下拉式選單（`combo2`）中選取的值。 | COMBO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
