此節點旨在透過對特定區域應用具有指定強度的遮罩，來修改生成模型的條件設定（conditioning）。它允許在條件設定中進行有針對性的調整，從而實現對生成過程更精確的控制。

## 輸入

### 必要輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 要修改的條件設定資料。這是應用遮罩和強度調整的基礎。 | CONDITIONING |
| `遮罩` | 一個遮罩張量，用於指定條件設定中要修改的區域。 | `MASK` |
| `強度` | 遮罩對條件設定效果的強度，可對所應用的修改進行微調。 | `FLOAT` |
| `設定條件區域` | 決定遮罩效果是應用於預設區域，還是受遮罩本身邊界限制，為鎖定特定區域提供靈活性。 | COMBO[STRING] |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 已修改的條件設定資料，已套用遮罩和強度調整。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/zh-TW.md)
