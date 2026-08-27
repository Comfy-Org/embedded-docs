# AutogrowNamesTestNode

此節點是為了測試自動增長（Autogrow）輸入功能。它接受動態數量的浮點數輸入，每個輸入都有指定的名稱，並將它們的值組合成單一以逗號分隔的字串。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `autogrow` | 動態輸入群組。您可以新增多個浮點數輸入，每個輸入使用預先定義的名稱：「a」、「b」或「c」。此節點會接受這些具名輸入的任何組合。 | FLOAT | 是 | N/A |

**注意：** `autogrow` 輸入是動態的。您可以依工作流程需求，新增或移除個別的浮點數輸入（名為「a」、「b」或「c」）。此節點會處理所有提供的值。

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `output` | 包含所有提供的浮點數輸入值的單一字串，以逗號連接。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
