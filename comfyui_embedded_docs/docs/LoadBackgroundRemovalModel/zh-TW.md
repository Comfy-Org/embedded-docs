# 載入背景移除模型

從檔案載入背景移除模型。此節點會準備模型，讓其他節點可用來從影像中移除背景。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | 用於從影像中移除背景的模型。請從可用的背景移除模型檔案清單中選取。 | COMBO | 是 | List of available model files (sorted alphabetically) |

注意：若選取的檔案不包含有效的背景移除模型，節點會引發 RuntimeError。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `bg_model` | 已載入的背景移除模型，可供其他節點用於處理影像。 | BACKGROUND_REMOVAL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
