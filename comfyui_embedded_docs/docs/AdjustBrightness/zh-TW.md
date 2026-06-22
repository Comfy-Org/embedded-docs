# 調整亮度

## 概述

調整亮度節點用於修改輸入圖像的亮度。其運作方式是將每個像素的值乘以指定的係數，然後將結果值限制在有效範圍內。係數為 1.0 時圖像保持不變，低於 1.0 時圖像變暗，高於 1.0 時圖像變亮。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要調整的輸入圖像。 | IMAGE | 是 | - |
| `亮度係數` | 亮度係數。1.0 = 不變，<1.0 = 變暗，>1.0 = 變亮。（預設值：1.0） | FLOAT | 否 | 0.0 - 2.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 調整亮度後的輸出圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c8f2fbb5fa149812a2ecd1ff9fce7bd6d29bf4c48b929e9ebc0a95c9e46ec65e`
