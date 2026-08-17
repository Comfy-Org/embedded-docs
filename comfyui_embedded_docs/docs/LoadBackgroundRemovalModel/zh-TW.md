# 載入背景移除模型

從檔案載入背景移除模型，並使其可供其他節點在移除影像背景時使用。模型檔案會從 `background_removal` 資料夾中的可用檔案中選取。

## 輸入
| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | 用於從影像中移除背景的模型。 | COMBO | Yes | 可用的模型檔案列表（`background_removal` 資料夾中檔案的排序列表） |

**注意：** 如果選取的檔案不包含有效的背景移除模型，節點會引發錯誤。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `bg_model` | 已載入的背景移除模型，可供其他節點用於處理影像。 | BACKGROUND_REMOVAL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/zh-TW.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
