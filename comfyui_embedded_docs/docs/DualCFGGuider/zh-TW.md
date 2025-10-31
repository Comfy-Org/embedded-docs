> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCFGGuider/zh-TW.md)

DualCFGGuider 節點建立了一個用於雙重無分類器引導採樣的引導系統。它將兩個正向條件輸入與一個負向條件輸入相結合，對每個條件配對應用不同的引導縮放比例，以控制每個提示詞對生成輸出的影響程度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 參數說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | MODEL | 是 | - | 用於引導的模型 |
| `cond1` | CONDITIONING | 是 | - | 第一個正向條件輸入 |
| `cond2` | CONDITIONING | 是 | - | 第二個正向條件輸入 |
| `負面` | CONDITIONING | 是 | - | 負向條件輸入 |
| `cfg 條件` | FLOAT | 是 | 0.0 - 100.0 | 第一個正向條件的引導縮放比例（預設值：8.0） |
| `cfg cond2 負面` | FLOAT | 是 | 0.0 - 100.0 | 第二個正向條件和負向條件的引導縮放比例（預設值：8.0） |
| `style` | COMBO | 是 | "regular"<br>"nested" | 要套用的引導樣式（預設值："regular"） |

## 輸出結果

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `GUIDER` | GUIDER | 已配置完成的引導系統，準備好用於採樣過程 |