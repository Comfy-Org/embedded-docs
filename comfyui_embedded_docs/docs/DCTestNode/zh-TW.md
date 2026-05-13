> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/zh-TW.md)

## 概述

DCTestNode 是一個邏輯節點，可根據使用者從動態組合框中選擇的項目返回不同類型的資料。它作為一個條件路由器，所選的選項決定了哪個輸入欄位處於啟用狀態，以及節點將輸出何種類型的值。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | 是 | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` | 主要選擇，決定哪個輸入欄位處於啟用狀態以及節點將輸出什麼。 |
| `string` | STRING | 否 | - | 文字輸入欄位。僅當 `combo` 設定為 `"option1"` 時，此欄位才會啟用並成為必要欄位。 |
| `integer` | INT | 否 | - | 整數輸入欄位。僅當 `combo` 設定為 `"option2"` 時，此欄位才會啟用並成為必要欄位。 |
| `image` | IMAGE | 否 | - | 影像輸入欄位。僅當 `combo` 設定為 `"option3"` 時，此欄位才會啟用並成為必要欄位。 |
| `subcombo` | COMBO | 否 | `"opt1"`<br>`"opt2"` | 當 `combo` 設定為 `"option4"` 時出現的次要選擇。它決定哪些巢狀輸入欄位處於啟用狀態。 |
| `float_x` | FLOAT | 否 | - | 小數輸入欄位。僅當 `combo` 設定為 `"option4"` 且 `subcombo` 設定為 `"opt1"` 時，此欄位才會啟用並成為必要欄位。 |
| `float_y` | FLOAT | 否 | - | 小數輸入欄位。僅當 `combo` 設定為 `"option4"` 且 `subcombo` 設定為 `"opt1"` 時，此欄位才會啟用並成為必要欄位。 |
| `mask1` | MASK | 否 | - | 遮罩輸入欄位。僅當 `combo` 設定為 `"option4"` 且 `subcombo` 設定為 `"opt2"` 時，此欄位才會啟用。此欄位為選填。 |

**參數限制：**

* `combo` 參數控制所有其他輸入欄位的可見性與必要性。僅與所選 `combo` 選項相關聯的輸入欄位才會顯示並成為必要欄位（`mask1` 除外，此欄位為選填）。
* 當 `combo` 設定為 `"option4"` 時，`subcombo` 參數會成為必要欄位，並控制第二組巢狀輸入（`float_x`/`float_y` 或 `mask1`）。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | ANYTYPE | 輸出取決於所選的 `combo` 選項。它可以是 STRING（`"option1"`）、INT（`"option2"`）、IMAGE（`"option3"`），或是 `subcombo` 字典的字串表示形式（`"option4"`）。 |

---
**Source fingerprint (SHA-256):** `98c4ca2100a27594df360935cc1507960480fe75a76ca0df2af75925d399be00`
