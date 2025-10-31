> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/zh-TW.md)

此節點旨在透過對特定區域應用具有指定強度的遮罩來修改生成模型的條件設定。它允許在條件設定中進行針對性調整，從而實現對生成過程更精確的控制。

## 輸入參數

### 必要參數

| 參數名稱       | 資料類型       | 描述 |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | 將被修改的條件設定資料，作為應用遮罩和強度調整的基礎。 |
| `mask`        | `MASK`       | 用於指定條件設定中將被修改區域的遮罩張量。 |
| `strength`    | `FLOAT`      | 遮罩對條件設定影響的強度，允許對應用的修改進行微調。 |
| `set_cond_area` | COMBO[STRING] | 決定遮罩效果是應用於預設區域還是受遮罩本身限制，提供在定位特定區域時的靈活性。 |

## 輸出參數

| 參數名稱       | 資料類型       | 描述 |
|---------------|--------------|-------------|
| `CONDITIONING` | CONDITIONING | 已應用遮罩和強度調整的修改後條件設定資料。 |