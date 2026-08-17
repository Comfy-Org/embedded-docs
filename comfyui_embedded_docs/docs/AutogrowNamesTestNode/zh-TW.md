# AutogrowNamesTestNode

此節點是針對 Autogrow 輸入功能的測試。它接受動態數量的浮點數輸入，每個輸入都標有特定名稱，並將它們的值合併為單一以逗號分隔的字串。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `autogrow` | 動態輸入群組。您可以新增多個浮點數輸入，每個輸入都可以從清單「a」、「b」或「c」中選取預先定義的名稱。此節點會接受這些具名輸入的任何組合。 | FLOAT | 是 | N/A |

**注意：** `autogrow` 輸入是動態的。您可以根據工作流程的需求，新增或移除個別的浮點數輸入（名為「a」、「b」或「c」）。此節點會處理所有提供的值。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 單一字串，包含所有提供的浮點數輸入的值，並以逗號連接。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `dac384c9486ac645d0d292fc891603cbfa6d362baa0a1e939c43257bbc0b06a0`
