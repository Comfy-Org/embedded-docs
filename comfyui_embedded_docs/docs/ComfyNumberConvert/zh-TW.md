# 數值轉換

Number Convert 節點可將各種輸入資料型別轉換為數值。它接受單一輸入，型別可為整數、浮點數、字串或布林值，並產生兩個輸出：一個浮點數和一個整數。此功能可用於將文字或邏輯值轉換為工作流程中其他數學或處理節點可使用的格式。

## Inputs

| Parameter | Description | Data Type | Required | Range |
| --- | --- | --- | --- | --- |
| `value` | 要轉換為數值輸出的值。接受整數、浮點數、文字字串或真/假布林值。 | INT, FLOAT, STRING, BOOLEAN | Yes | N/A |

**注意：** 當輸入為字串時，它不能為空，且必須包含有效的數字表示（例如 `"123"`、`"3.14"`）。若輸入為空字串、無法解析為數字的文字，或非有限值（如 `"inf"` 或 `"nan"`），節點會產生錯誤。對於布林值輸入，`true` 會轉換為 1.0（FLOAT）和 1（INT），而 `false` 則轉換為 0.0（FLOAT）和 0（INT）。對於浮點數輸入，整數輸出是透過截斷小數部分來取得。

## Outputs

| Output Name | Description | Data Type |
| --- | --- | --- |
| `FLOAT` | 輸入值轉換為浮點數。 | FLOAT |
| `INT` | 輸入值轉換為整數。對於浮點數輸入，這會執行截斷。 | INT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyNumberConvert/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d6a774bf7c3ad9482b2275adc6ccc9e47c82b1f35f11c5a241b00efd29526f94`
