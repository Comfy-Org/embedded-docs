> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetAreaStrength/zh-TW.md)

此節點旨在修改指定條件集的強度屬性，允許調整條件對生成過程的影響力或強度。

## 輸入

| 參數 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | 要修改的條件集，代表影響生成過程的當前條件狀態。 |
| `強度` | `FLOAT` | 應用於條件集的強度值，決定其影響力的強度。 |

## 輸出

| 參數 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `CONDITIONING` | CONDITIONING | 已修改的條件集，每個元素都具有更新後的強度值。 |