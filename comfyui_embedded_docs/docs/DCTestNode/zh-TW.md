# DCTestNode

DCTestNode 是一個邏輯節點，會根據使用者從動態下拉式方塊中選取的選項，傳回不同類型的資料。它作為一個條件路由節點，所選的選項會決定哪個輸入欄位處於啟用狀態，以及節點將輸出什麼類型的值。

## 輸入

此節點使用動態下拉式選擇器：`combo` 參數始終可見，其他輸入欄位僅在選取對應選項時才會出現。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `combo` | 主要選擇，決定哪個輸入欄位處於啟用狀態，以及節點將輸出什麼內容。 | DYNAMIC_COMBO | 是 | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` |

### option1 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `string` | 文字輸入欄位。僅當 `combo` 設為 `"option1"` 時，此欄位才會啟用且為必填。 | STRING | 是 | - |

### option2 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `integer` | 整數輸入欄位。僅當 `combo` 設為 `"option2"` 時，此欄位才會啟用且為必填。 | INT | 是 | - |

### option3 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 影像輸入欄位。僅當 `combo` 設為 `"option3"` 時，此欄位才會啟用且為必填。 | IMAGE | 是 | - |

### option4 輸入

當 `combo` 設為 `"option4"` 時，節點會顯示第二個動態下拉式選擇器（`subcombo`），用以控制一組巢狀輸入欄位。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `subcombo` | 當 `combo` 設為 `"option4"` 時出現的次要動態下拉式選擇器。它會決定哪些巢狀輸入欄位處於啟用狀態。 | DYNAMIC_COMBO | 是 | `"opt1"`<br>`"opt2"` |
| `float_x` | 浮點數輸入欄位。僅當 `combo` 設為 `"option4"` 且 `subcombo` 設為 `"opt1"` 時，此欄位才會啟用且為必填。 | FLOAT | 是 | - |
| `float_y` | 浮點數輸入欄位。僅當 `combo` 設為 `"option4"` 且 `subcombo` 設為 `"opt1"` 時，此欄位才會啟用且為必填。 | FLOAT | 是 | - |
| `mask1` | 遮罩輸入欄位。僅當 `combo` 設為 `"option4"` 且 `subcombo` 設為 `"opt2"` 時，此欄位才會啟用。此欄位為選填。 | MASK | 否 | - |

**參數約束：**

* `combo` 參數控制所有其他輸入欄位的可見性與必填狀態。只有與所選 `combo` 選項關聯的輸入欄位會被顯示並為必填（`mask1` 除外，它為選填）。
* 當 `combo` 設為 `"option4"` 時，`subcombo` 參數會變為必填，並控制第二組巢狀輸入（`float_x`/`float_y` 或 `mask1`）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 輸出取決於所選的 `combo` 選項。它可以是 STRING（`"option1"`）、INT（`"option2"`）、IMAGE（`"option3"`），或是 `subcombo` 字典的字串表示（`"option4"`）。 | ANYTYPE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9dd616a427a56eddb78b48d6eea6f71419b7097d417afae5557132b333641e69`
