# 數值轉換

Number Convert 節點會將各種輸入資料類型轉換為數值。它接受單一輸入，類型為 INT、FLOAT、STRING 或 BOOLEAN，並產生兩個輸出：浮點數與整數。這對於將文字或邏輯值轉換為工作流程中其他數學或處理節點可使用的格式很有用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `數值` | 要轉換為數值輸出的值。可接受整數、浮點數、文字字串或 true/false 布林值。 | INT, FLOAT, STRING, BOOLEAN | 是 | N/A |

**注意：** 當輸入為字串時，它不得為空，且必須包含有效的數字表示形式（例如 `"123"`、`"3.14"`）。對於空字串、無法解析為數字的文字，或非有限值（例如 `"inf"` 或 `"nan"`），此節點會引發錯誤。對於布林值輸入，`true` 會轉換為 1.0（FLOAT）和 1（INT），而 `false` 會轉換為 0.0（FLOAT）和 0（INT）。對於 FLOAT 輸入以及包含小數的數字的字串，整數輸出會透過截斷小數部分來取得。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `FLOAT` | 輸入值轉換為浮點數。 | FLOAT |
| `INT` | 輸入值轉換為整數。對於 FLOAT 輸入和小數字串，這會執行截斷。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
