# AutogrowNamesTestNode

此節點是 Autogrow 輸入功能的測試。它接受一組動態的 FLOAT 輸入，每個輸入都有預先定義的名稱，並將其值結合成單一以逗號分隔的字串。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `autogrow` | 一個動態輸入群組。你可以新增多個 FLOAT 輸入，每個輸入都有預先定義的名稱，可從清單中選擇："a"、"b" 或 "c"。節點接受這些具名輸入的任意組合。 | FLOAT | 是 | 具名槽位：`a`, `b`, `c` |

**注意：** `autogrow` 輸入是動態的。名為 "a"、"b" 和 "c" 的個別 FLOAT 輸入可以視需要新增或移除。節點會處理所有提供的值。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 單一字串，包含所有提供之 FLOAT 輸入的值，並以逗號連接。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
