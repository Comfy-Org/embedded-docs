# EndLoop

End Loop 標誌著迴圈區塊的結束。它會收集迴圈主體中最後一個節點產生的值，並根據 `accumulate` 設定，只傳回最終迭代的值或每一次迭代的值，同時也會將值傳回 Start Loop，以便開始下一次迭代。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `output_value` | 由 End Loop 傳回的值。它會根據 `accumulate` 傳回最終迭代的值或所有迭代的值。 | ANY | 否 | 任意值類型 |
| `next_iteration_value` | 由 End Loop 傳回 Start Loop 的值，用於下一次迭代。 | ANY | 否 | 任意值類型 |
| `accumulate` | 啟用時，從每次迭代傳回 `output_value`；否則只傳回最終迭代的值。 | BOOLEAN | 否 | `true`<br>`false`（預設：`false`） |
| `terminations` | 連接必須在每次迭代中執行的輸出。這些值不會被傳回。可增長的插槽，命名為 `termination_1`、`termination_2`，依此類推。 | ANY | 否 | 0 到 50 個插槽 |

注意：`terminations` 是一個可增長的插槽清單，最少 0 個、最多 50 個連接。連接至此的值會強制在每次迭代中執行，但不屬於傳回結果的一部分。

注意：此節點是輸入清單節點，因此其輸入會接收來自每次迴圈迭代所收集的值。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `outputs` | 最終迭代的 `output_value`，或啟用 `accumulate` 時跨迭代累積的值。 | ANY (list) |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/zh-TW.md)

---
**Source fingerprint (SHA-256):** `142840dca7f238eb00c72074d265478c548ad5c047e05744d0c3715e452f795a`
