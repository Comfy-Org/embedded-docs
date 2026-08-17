# 自訂組合

Custom Combo 節點可讓您建立自訂下拉式選單，並使用您自己的文字選項清單。這是一個以前端為主的節點，提供後端表示以確保與您的工作流程相容。當您從下拉式選單中選擇一個選項時，節點會輸出該文字字串及其索引位置。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `choice` | 從自訂下拉式選單中選取的文字選項。可用選項清單由使用者在此節點的前端介面中定義。 | COMBO | 是 | User-defined |
| `index` | 可用於指定索引的整數值。預設值：0。 | INT | 否 | Any integer |

**注意：** 此節點輸入的驗證功能已被刻意停用。這可讓您在前端定義任何想要的自訂文字選項，而後端不會檢查您的選取是否來自預先定義的清單。此節點被標記為實驗性。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `STRING` | 從自訂下拉式方塊中選取之選項的文字字串。 | STRING |
| `INDEX` | 所選選項在下拉式選單中的索引位置。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CustomCombo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `143eafcf32de7ebaf72b5387537154b5deee7d3e3a520a0b2c12ac4fb67890f8`
