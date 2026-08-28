# 調整對比度

Adjust Contrast 節點會修改輸入影像的對比度等級。其運作方式是調整影像中亮部與暗部之間的差異。係數為 1.0 時影像保持不變，低於 1.0 的值會降低對比度，高於 1.0 的值則會增加對比度。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要調整對比度的輸入影像。 | IMAGE | 是 | - |
| `對比度係數` | 對比度係數。1.0 = 不變，<1.0 = 降低對比度，>1.0 = 增加對比度。（預設值：1.0） | FLOAT | 否 | 0.0 - 2.0 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `影像` | 調整對比度後產生的影像。像素值會限制在 0.0–1.0 範圍內。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1f5fbd0f0b739492bc171d3c43ea2150a3ca76dc3ede9bf63cb97c45a90b9e44`
