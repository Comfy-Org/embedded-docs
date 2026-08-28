# ModelComputeDtype

ModelComputeDtype 節點會變更模型在處理期間使用的計算資料型別（精確度）。它會建立輸入模型的副本，並套用所選的精確度設定，這有助於根據您的硬體最佳化記憶體使用量與效能。這對於偵錯和測試不同的精確度組態非常有用。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用新計算資料型別進行修改的輸入模型 | MODEL | 是 | - |
| `dtype` | 要套用至模型的計算資料型別（預設值："default"）。此參數標記為進階選項。 | COMBO | 是 | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## 輸出

| 輸出名 | 說明 | 資料型別 |
| --- | --- | --- |
| `model` | 已套用新計算資料型別的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`
