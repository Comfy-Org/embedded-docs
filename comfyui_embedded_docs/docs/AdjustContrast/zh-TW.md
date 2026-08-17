# 調整對比度

「調整對比度」節點會修改輸入圖片的對比度等級。其運作方式是調整圖片中亮部與暗部之間的差異。當 `factor` 為 1.0 時，圖片保持不變；數值低於 1.0 會降低對比度；數值高於 1.0 則會提高對比度。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要調整對比度的輸入圖片。 | IMAGE | 是 | - |
| `factor` | 對比度係數。1.0 = 不變，<1.0 = 降低對比度，>1.0 = 提高對比度。（預設值：1.0） | FLOAT | 否 | 0.0 - 2.0 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `image` | 調整對比度後產生的圖片。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustContrast/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1f5fbd0f0b739492bc171d3c43ea2150a3ca76dc3ede9bf63cb97c45a90b9e44`
