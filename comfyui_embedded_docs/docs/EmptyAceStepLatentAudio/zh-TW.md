> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/zh-TW.md)

## 概述

EmptyAceStepLatentAudio 節點會建立指定時長的空潛在音訊樣本。它會生成一批充滿零值的靜音音訊潛在表示，其長度是根據輸入秒數和音訊處理參數計算得出的。此節點適用於初始化需要潛在表示的音訊處理工作流程。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `seconds` | FLOAT | 是 | 1.0 - 1000.0 | 音訊的持續時間（秒），預設值：120.0 |
| `batch_size` | INT | 是 | 1 - 4096 | 批次中的潛在影像數量，預設值：1 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | LATENT | 傳回充滿零值的空潛在音訊樣本。輸出包含一個 `samples` 張量，以及一個設為 "audio" 的 `type` 欄位。 |

---
**Source fingerprint (SHA-256):** `79fcfb3cb26db8a2ef4480455a44255e0d1a16f122a762d7608a78b2330cc637`
