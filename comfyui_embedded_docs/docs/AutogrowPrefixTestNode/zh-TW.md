# AutogrowPrefixTestNode

AutogrowPrefixTestNode 是一個邏輯節點，用於測試 autogrow 輸入功能。它接受動態數量的浮點數輸入，將每個值轉換為文字，組合成以逗號分隔的字串，然後輸出該字串。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | Range |
| --- | --- | --- | --- | --- |
| `autogrow` | 一個動態輸入群組，接受 1 到 10 個浮點數值。每個值皆為浮點數，生成的輸入以 `float` 為前綴命名。 | AUTOGROW | 是 | 1 至 10 inputs |

**注意：** `autogrow` 輸入是一個特殊的動態輸入。您可以在此群組中新增多個浮點數輸入，最少 1 個，最多 10 個。節點會處理所有提供的值，並將每個已連接的輸入納入輸出字串中。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 包含所有輸入浮點數值（以逗號分隔）的單一字串。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9b815f59961a4c661815f44b9c78e15e9084db1e4be89d502b9d92438f18e70b`
