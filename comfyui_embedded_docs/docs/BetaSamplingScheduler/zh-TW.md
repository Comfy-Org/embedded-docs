> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BetaSamplingScheduler/zh-TW.md)

BetaSamplingScheduler 節點使用 beta 排程演算法為取樣過程生成一系列雜訊等級（sigmas）。它接收模型和配置參數，創建一個自定義的雜訊排程，用於控制圖像生成過程中的去雜訊處理。此排程器允許透過 alpha 和 beta 參數微調雜訊降低軌跡。

## 輸入參數

| 參數名稱 | 資料類型 | 輸入類型 | 預設值 | 數值範圍 | 描述 |
|-----------|-----------|------------|---------|-------|-------------|
| `model` | MODEL | 必填 | - | - | 用於取樣的模型，提供模型取樣物件 |
| `步驟數` | INT | 必填 | 20 | 1-10000 | 要生成 sigmas 的取樣步驟數量 |
| `alpha` | FLOAT | 必填 | 0.6 | 0.0-50.0 | Beta 排程器的 alpha 參數，控制排程曲線 |
| `beta` | FLOAT | 必填 | 0.6 | 0.0-50.0 | Beta 排程器的 beta 參數，控制排程曲線 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `SIGMAS` | SIGMAS | 用於取樣過程的一系列雜訊等級（sigmas） |