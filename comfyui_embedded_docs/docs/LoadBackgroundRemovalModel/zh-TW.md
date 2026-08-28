# 載入背景移除模型

從檔案載入背景移除模型。此節點準備模型以供從圖像中移除背景時使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | 用於從圖像中移除背景的模型。從可用的背景移除模型檔案清單中選擇。 | COMBO | 是 | 可用的模型檔案清單（依字母順序排序） |

注意：如果所選檔案不包含有效的背景移除模型，此節點會拋出 RuntimeError。

## 輸出

| 輸出名 | 說明 | 資料類型 |
| --- | --- | --- |
| `bg_model` | 已載入的背景移除模型，可供其他節點用來處理圖像。 | BACKGROUND_REMOVAL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
