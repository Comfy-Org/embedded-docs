# 條件設定（時間步範圍）

此節點旨在透過設定特定的時間步長範圍來調整條件化的時間面向。它允許精確控制條件化過程的起始與結束點，從而實現更具針對性且更高效的生成。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 條件化輸入代表生成過程的當前狀態，此節點透過設定特定的時間步長範圍來修改該狀態。 | CONDITIONING |
| `開始` | start 參數以佔總生成過程的百分比形式指定時間步長範圍的起點，可對條件化效果的開始時間進行精細調整。 | `FLOAT` |
| `結束` | end 參數以百分比形式定義時間步長範圍的終點，可精確控制條件化效果的持續時間與結束時機。 | `FLOAT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `CONDITIONING` | 輸出為已套用指定時間步長範圍的修改後條件化結果，可供後續處理或生成使用。 | CONDITIONING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetTimestepRange/zh-TW.md)
