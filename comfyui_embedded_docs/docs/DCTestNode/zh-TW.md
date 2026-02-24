> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DCTestNode/zh-TW.md)

DCTestNode 是一個邏輯節點，它會根據使用者從動態下拉式選單中選擇的項目，返回不同類型的資料。它扮演著條件路由器的角色，所選的選項決定了哪個輸入欄位處於活動狀態，以及節點將輸出何種類型的值。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `combo` | COMBO | 是 | `"option1"`<br>`"option2"`<br>`"option3"`<br>`"option4"` | 主要選擇項目，決定哪個輸入欄位處於活動狀態以及節點將輸出什麼。 |
| `string` | STRING | 否 | - | 文字輸入欄位。此欄位僅在 `combo` 設定為 `"option1"` 時才處於活動狀態且為必填。 |
| `integer` | INT | 否 | - | 整數輸入欄位。此欄位僅在 `combo` 設定為 `"option2"` 時才處於活動狀態且為必填。 |
| `image` | IMAGE | 否 | - | 影像輸入欄位。此欄位僅在 `combo` 設定為 `"option3"` 時才處於活動狀態且為必填。 |
| `subcombo` | COMBO | 否 | `"opt1"`<br>`"opt2"` | 當 `combo` 設定為 `"option4"` 時出現的次要選擇項目。它決定哪些巢狀輸入欄位處於活動狀態。 |
| `float_x` | FLOAT | 否 | - | 小數輸入欄位。此欄位僅在 `combo` 設定為 `"option4"` 且 `subcombo` 設定為 `"opt1"` 時才處於活動狀態且為必填。 |
| `float_y` | FLOAT | 否 | - | 小數輸入欄位。此欄位僅在 `combo` 設定為 `"option4"` 且 `subcombo` 設定為 `"opt1"` 時才處於活動狀態且為必填。 |
| `mask1` | MASK | 否 | - | 遮罩輸入欄位。此欄位僅在 `combo` 設定為 `"option4"` 且 `subcombo` 設定為 `"opt2"` 時才處於活動狀態。它是可選的。 |

**參數限制條件：**

* `combo` 參數控制所有其他輸入欄位的可見性和必要性。只有與所選 `combo` 選項相關的輸入才會顯示，並且是必填的（除了可選的 `mask1`）。
* 當 `combo` 設定為 `"option4"` 時，`subcombo` 參數變為必填，並控制第二組巢狀輸入（`float_x`/`float_y` 或 `mask1`）。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `output` | ANYTYPE | 輸出取決於所選的 `combo` 選項。它可以是 STRING (`"option1"`)、INT (`"option2"`)、IMAGE (`"option3"`)，或是 `subcombo` 字典的字串表示形式 (`"option4"`)。 |
