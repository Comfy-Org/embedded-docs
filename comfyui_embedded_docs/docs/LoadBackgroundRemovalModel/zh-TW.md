## 概述

從檔案載入背景移除模型。此節點準備模型，以便用於從影像中移除背景。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | 用於從影像中移除背景的模型。從可用的背景移除模型檔案清單中選擇。 | STRING | 是 | 可用模型檔案清單 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `bg_model` | 已載入的背景移除模型，可供其他節點用於處理影像。 | BACKGROUND_REMOVAL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `63a1ffb37ea8581e3ba29f7dc4f871612d7ec458e6d36f5e2244201941d48f9d`
