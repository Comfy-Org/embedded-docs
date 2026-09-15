# StartLoop

Start Loop 節點會在工作流程內啟動迴圈結構。它每次迭代執行已連接的迴圈主體一次，並可用三種方式計算迭代次數：固定重複次數（simple）、數值索引範圍（For），或清單中每個項目執行一次（List）。每次執行會提供目前索引、first/last 旗標，以及可選的攜帶值，可從一次迭代傳遞到下一次迭代。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `mode` | 迴圈迭代模式（預設："simple"）。所選模式決定顯示哪些額外參數。 | DYNAMIC_COMBO | 是 | `"simple"`<br>`"For"`<br>`"List"` |
| `cache_iterations` | 重複使用先前執行中未變更的迭代結果。停用後會再次執行每個迭代。預設：false。 | BOOLEAN | 否 | true<br>false |
| `parent_iteration` | 連接來自外層 Start Loop 的 `iteration_index` 以嵌套此迴圈。此輸入僅限強制輸入（需要連結）。 | INT | 否 | 任意整數 |
| `initial_iteration_value` | 第一次迭代時作為 `current_iteration_value` 提供的值。 | ANY (type-matched) | 否 | 任意值 |

### Simple 模式輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `num_iterations` | 執行迴圈主體的次數。預設：4。 | INT | 是 | 最小值 0 |

### For 模式輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `start_iteration_index` | 使用 For 迴圈模式時，第一次迭代的索引。預設：0。 | INT | 是 | 任意整數 |
| `max_iteration` | For 模式下 `iteration_index` 的排除停止值。預設：4。 | INT | 是 | 最大值 0xffffffffffffffff |
| `step` | 使用 For 迴圈模式時，每次迭代之間的索引步長。預設：1。 | INT | 是 | 最小值 1 |

### List 模式輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `list` | 迴圈迭代的項目清單。迴圈主體會針對每個項目執行一次。 | ANY (type-matched list item) | 是 | 任意清單 |

備註：

- 僅會顯示並使用屬於目前所選 `mode` 的參數。
- 在 Simple 模式中，迭代索引從 0 到 `num_iterations` 減 1。在 For 模式中，索引從 `start_iteration_index` 到（但不包含）`max_iteration`，每次增加 `step`。在 List 模式中，`list` 中的每個項目會執行一次迭代。
- `step` 不得為 0；值為 0 會引發錯誤。不允許低於 1 的值。
- 如果計算出的迭代次數為零，`is_last` 輸出會回報為 true，且迴圈主體不會執行。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `iteration_index` | 目前迴圈迭代的索引。 | INT |
| `is_first` | 在迴圈第一次迭代期間為 true。 | BOOLEAN |
| `is_last` | 在迴圈最後一次迭代期間為 true。 | BOOLEAN |
| `list_item` | 使用 List 模式時，來自清單的目前項目。Simple 和 For 模式下為 None。 | ANY (type-matched) |
| `current_iteration_value` | 目前迭代的迴圈攜帶值：第一次迭代時為 `initial_iteration_value`，後續每次迭代則為來自 End Loop 的 `next_iteration_value`。 | ANY (type-matched) |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StartLoop/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2584af9fd623f4762f440a043679e47aeef25ad0d571cfac11506cb513dd1b98`
