> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/zh-TW.md)

# ComfyMathExpression 節點

ComfyMathExpression 節點使用一組輸入值來評估數學公式。您可以編寫使用變數名稱（如 `a`、`b`、`c`）的表達式，節點將計算結果。它支援根據計算需求動態添加任意數量的輸入值。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `運算式` | STRING | 是 | 不適用 | 要評估的數學公式。您可以使用對應於輸入值的變數名稱（預設值："a + b"）。 |
| `數值` | FLOAT, INT, BOOLEAN | 否 | 不適用 | 一組可動態添加的數值或布林值輸入。每個輸入會被分配一個字母（a、b、c...），以便在表達式中作為變數使用。 |

**參數限制：**
*   `expression` 參數不能為空或僅包含空白字元。
*   表達式必須評估為有限的數值結果（INT 或 FLOAT）。布林值或其他非數值結果將導致錯誤。
*   `values` 參數的輸入值可以是數字（INT 或 FLOAT）或布林值（TRUE/FALSE）。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `FLOAT` | FLOAT | 數學表達式的結果，以浮點數形式呈現。 |
| `BOOL` | INT | 數學表達式的結果，以整數形式呈現。 |
| `BOOL` | BOOLEAN | 數學表達式的結果，以布林值形式呈現。 |

---
**Source fingerprint (SHA-256):** `962f82684d9dc58a67a57e6738d6d2ed457d7f30288cedb21fd46b5c655c1708`
