# 曲線編輯器

曲線編輯器節點提供一個視覺化介面，用於調整和微調曲線。它允許您修改輸入曲線的形狀，並可選擇以直方圖視覺化其分佈。此節點輸出修改後的曲線，供工作流程中的其他部分使用。

## 輸入

| 參數 | 說明 | 資料型別 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `curve` | 要編輯的輸入曲線。 | CURVE | 是 | N/A |
| `histogram` | 可選的直方圖，用於與曲線並排顯示作為視覺參考。 | HISTOGRAM | 否 | N/A |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `curve` | 在節點介面中進行調整後所得到的已編輯曲線。 | CURVE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CurveEditor/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6c4459998b1a3dd3a53f84cb1c231c448c64aa55b96444bc4ac7470556a3b915`
