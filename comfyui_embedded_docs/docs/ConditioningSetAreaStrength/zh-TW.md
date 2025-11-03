> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaStrength/zh-TW.md)

此節點旨在修改指定條件設定集的強度屬性，允許調整條件對生成過程的影響程度或強度。

## 輸入參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | 要修改的條件設定集，代表影響生成過程的當前條件狀態。 |
| `強度` | `FLOAT` | 要應用於條件設定集的強度值，決定其影響的強度。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | 具有更新後強度值的修改條件設定集。 |