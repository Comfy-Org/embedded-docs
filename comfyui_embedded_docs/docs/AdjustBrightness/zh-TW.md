# 調整亮度

Adjust Brightness 節點會調整輸入影像的亮度。其運作方式是將每個像素的值乘以指定係數，然後將結果值限制在有效範圍內。係數為 1.0 時影像維持不變，低於 1.0 會變暗，高於 1.0 會變亮。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要調整的輸入影像。 | IMAGE | 是 | - |
| `factor` | 亮度係數。1.0 = 不變，<1.0 = 變暗，>1.0 = 變亮。（預設值：1.0） | FLOAT | 否 | 0.0 - 2.0 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `image` | 亮度調整後的輸出影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AdjustBrightness/zh-TW.md)

---
**Source fingerprint (SHA-256):** `696fb3c0bfc8edccc2049dad8f44b4b056fe1caa95b0cc0126164269cb65ab1a`
