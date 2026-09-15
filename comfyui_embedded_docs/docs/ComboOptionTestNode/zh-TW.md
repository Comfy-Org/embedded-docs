# ComboOptionTestNode

此節點接收兩個下拉式選單選項，並將它們原樣傳遞至其輸出，不進行任何變更。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `combo` | 第一個選項，從一組三個測試選項中選擇。 | COMBO | 是 | `"option1"`<br>`"option2"`<br>`"option3"` |
| `combo2` | 第二個選項，從另一組三個測試選項中選擇。 | COMBO | 是 | `"option4"`<br>`"option5"`<br>`"option6"` |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output_1` | 傳回第一個下拉式選單 (`combo`) 中選取的值，保持不變。 | COMBO |
| `output_2` | 傳回第二個下拉式選單 (`combo2`) 中選取的值，保持不變。 | COMBO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComboOptionTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fe0b6a35680de55767af2c0d8a293010ddb4c4282cfdde7f9dff7a3a11ff1e5c`
