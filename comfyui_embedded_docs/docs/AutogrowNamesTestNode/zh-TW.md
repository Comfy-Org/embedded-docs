## 概述

此節點是自動增長輸入功能的測試節點。它接受動態數量的浮點數輸入，每個輸入都標有特定名稱，並將它們的值合併為一個以逗號分隔的單一字串。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `autogrow` | 動態輸入群組。您可以新增多個浮點數輸入，每個輸入都使用預先定義的名稱： "a"、"b" 或 "c"。此節點會接受這些命名輸入的任何組合。 | FLOAT | 是 | 不適用 |

**注意：** `autogrow` 輸入是動態的。您可以根據工作流程需求新增或移除個別的浮點數輸入（命名為 "a"、"b" 或 "c"）。此節點會處理所有提供的數值。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 包含所有提供的浮點數輸入值的單一字串，以逗號連接。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowNamesTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `33e8b2e2c369d06979415c31ef2623cff55d98ecf49137c5cafbeba7cc3b0451`
