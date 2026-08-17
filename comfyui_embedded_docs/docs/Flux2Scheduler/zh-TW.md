# Flux2Scheduler

以下為翻譯結果：

Flux2Scheduler 節點會為去噪過程生成一系列雜訊等級（sigmas），特別針對 Flux2 模型量身打造。它會根據去噪步驟數與目標影像的尺寸來計算排程，進而影響影像生成期間雜訊移除的進程。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `steps` | 要執行的去噪步驟數。數值越高通常會產生更精細的結果，但處理時間也更長（預設：20）。 | INT | 是 | 1 到 4096 |
| `width` | 要生成影像的寬度（像素）。此數值會影響雜訊排程的計算（預設：1024）。 | INT | 是 | 16 到 16384（MAX_RESOLUTION） |
| `height` | 要生成影像的高度（像素）。此數值會影響雜訊排程的計算（預設：1024）。 | INT | 是 | 16 到 16384（MAX_RESOLUTION） |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `sigmas` | 一系列定義取樣器去噪排程的雜訊等級值（sigmas）。輸出包含的值數量會比步驟數多一個（`steps + 1`）。 | SIGMAS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2Scheduler/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9606177f37f7bc03aef524623f03b7f24bcdc3d9327dcdf74863fe2befeb2b65`
