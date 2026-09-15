# LoopResult

LoopResult 是僅供開發者使用的輸出節點，用來標記迴圈區塊的結束點。它會依序收集傳入的值（命名為 `output0`、`output1` 等），並釋放由 close ID 識別的外部執行區塊。由於輸入指紋比對總是回傳 NaN，此節點會被視為總是已變更，並在每次執行時重新執行。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `close_id` | 要關閉的迴圈區塊識別碼；僅使用清單中的第一個值 | STRING | 是 | - |
| `output0`, `output1`, ... | 從迴圈區塊收集的值。此節點會接受任何額外輸入，並從 `output0` 開始依序收集，遇到第一個缺少的索引時停止 | 任意類型 | 否 | - |

注意：此節點接受所有輸入（`accept_all_inputs`）。任何超出 `close_id` 的輸入都會被視為收集到的迴圈值，且必須命名為 `output0`、`output1`、`output2` 等，中間不能有缺漏，才能納入結果中。

## 輸出

此節點不會傳回任何輸出。它只會釋放與 `close_id` 相關聯的外部執行區塊。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopResult/zh-TW.md)

---
**Source fingerprint (SHA-256):** `637f8a39b0e99e8d4453cfc482463bd14d909b710264021ac2c27fdcd68b6063`
