USOStyleReference 節點使用從 CLIP 視覺輸出編碼的圖像特徵，將樣式參考修補程式套用至模型。它透過納入從視覺輸入中提取的樣式資訊，建立輸入模型的修改版本，從而實現樣式轉換或基於參考的生成能力。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `模型` | 要套用樣式參考修補程式的基本模型 | MODEL | 是 | - |
| `模型修補` | 包含樣式參考資訊的模型修補程式 | MODEL_PATCH | 是 | - |
| `CLIP視覺輸出` | 從 CLIP 視覺處理中提取的編碼視覺特徵 | CLIP_VISION_OUTPUT | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `模型` | 已套用樣式參考修補程式的修改模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/USOStyleReference/zh-TW.md)

---
**Source fingerprint (SHA-256):** `fd800fb927677da29e148bfa1b287efed82895860ce4b0241d662579d2c07ff4`
