# 預覽任意

PreviewAny 會將任何輸入值轉換為可讀文字，以便您檢視。字串會原樣傳遞，數字與布林值會變成純文字，其他資料類型則會在可能時序列化為 JSON（若序列化失敗，則退回其純字串形式）。產生的文字會顯示於使用者介面，也會以字串輸出傳回，供後續處理使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `來源` | 接受任何輸入資料類型以進行預覽顯示。若未提供值，預覽會顯示 'None'。 | ANY | 是 | Any data type |

**轉換行為**

- STRING 類型的值會完全依照提供的內容顯示。
- INT、FLOAT 或 BOOLEAN 類型的值會轉換為純文字。
- 任何其他非空值會轉換為縮排 4 個空格的 JSON 文字；若該轉換失敗，節點會退回該值的純文字形式。若此方式也失敗，預覽會顯示訊息 'source exists, but could not be serialized.'。
- 若未連接任何值，或值為空，預覽會顯示 'None'。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `result` | 轉換為文字格式的輸入值。相同文字也會顯示於使用者介面。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/zh-TW.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
