# AutogrowPrefixTestNode

## 概述

AutogrowPrefixTestNode 是一個邏輯節點，旨在測試自動增長輸入功能。它接受動態數量的浮點數輸入，將其值組合成逗號分隔的字串，並輸出該字串。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `autogrow` | 一個動態輸入群組，可接受 1 到 10 個浮點數值。群組中的每個輸入都是 FLOAT 類型，最小值為 1，最大值為 10。 | AUTOGROW | 是 | 1 到 10 個輸入 |

**注意：** `autogrow` 輸入是一個特殊的動態輸入。您可以在此群組中新增多個浮點數輸入，最多可達 10 個。節點將處理所有提供的值。每個單獨的浮點數輸入都限制在 1 到 10 的範圍內。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 包含所有輸入浮點數值的單一字串，以逗號分隔。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AutogrowPrefixTestNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7ae65365f77399a2ad8358b5a1eab3f2caa39331e53dec474cdd7f2751bfff4b`
