# 數學運算式

ComfyMathExpression 節點會評估你以文字撰寫的數學公式。該公式可以使用字母名稱（例如 `a`、`b`、`c`）來參照節點的輸入值，而你可以透過可增長的 `values` 群組新增任意數量的輸入值。計算結果會同時以浮點數、整數和布林值傳回。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `運算式` | 要評估的數學公式，以文字撰寫（例如 `a + b`），並使用輸入值的字母名稱作為變數。多行輸入。（預設值："a + b"） | STRING | 是 | N/A |
| `數值` | 可增長的輸入值群組，提供運算式的變數。新增至群組的每個值會自動取得下一個小寫字母名稱，從 `a` 開始（`a`、`b`、`c`、...），然後該名稱即可在 `expression` 內使用。每個項目接受數字（INT 或 FLOAT）或布林值（TRUE/FALSE）。 | FLOAT, INT, BOOLEAN | 是 | 1 至 26 個值，命名為 `a` 至 `z` |

### 注意事項與限制

- `expression` 不能為空，也不能只包含空白字元。
- 運算式必須評估為數值結果（INT 或 FLOAT）或布林結果（TRUE/FALSE）。布林結果在 TRUE 時視為 1，在 FALSE 時視為 0。如果結果是不同類型，例如文字，節點會引發錯誤。
- 數值結果必須是有限值，且可轉換為浮點數。結果過大或非有限值會導致錯誤。
- 整組輸入值也可在運算式內以變數名稱 `values`（作為清單）取得，因此可以使用例如 `sum(values)` 的運算式。
- 運算式內可使用以下數學函式：`sum`、`min`、`max`、`abs`、`round`、`pow`、`sqrt`、`ceil`、`floor`、`log`、`log2`、`log10`、`sin`、`cos`、`tan`、`int`、`float`。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `FLOAT` | 運算式結果，以浮點數表示。 | FLOAT |
| `INT` | 運算式結果轉換為整數，小數部分會截斷。 | INT |
| `BOOL` | 結果轉換為布林值：數值結果不為零時為 TRUE，為零時為 FALSE。 | BOOLEAN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyMathExpression/zh-TW.md)

---
**Source fingerprint (SHA-256):** `4c77e9834fe7341143352f95ed8808dc81def3361b197c67e33a531bb3696d71`
