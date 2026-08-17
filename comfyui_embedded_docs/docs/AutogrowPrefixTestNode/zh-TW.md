# AutogrowPrefixTestNode

AutogrowPrefixTestNode 是一個邏輯節點，用於測試 autogrow 輸入功能。它接受動態數量的浮點數輸入，將所有值組合成逗號分隔的字串，並輸出該字串。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `autogrow` | 一個動態輸入群組，接受浮點數值。該群組可容納 1 到 10 個浮點數輸入，節點會處理所有提供的值。 | FLOAT | 是 | 1 to 10 inputs |

**注意：** `autogrow` 輸入是一種特殊的動態輸入，可擴充以新增更多浮點數輸入，最多 10 個。最小值為 1 個輸入。此節點中的 `min` 和 `max` 值定義的是群組中允許的輸入數量，而非每個單獨浮點數的數值範圍。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 包含所有輸入浮點數值並以逗號分隔的單一字串。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
