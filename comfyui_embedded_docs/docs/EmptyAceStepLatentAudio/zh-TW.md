# EmptyAceStepLatentAudio

EmptyAceStepLatentAudio 節點會建立指定時長的空白潛在音訊樣本。它會產生一批充滿零值的靜音音訊潛在表示，其長度是根據輸入的秒數與音訊處理參數計算而得。此節點對於初始化需要潛在表示的音訊處理工作流程非常有用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `seconds` | 音訊的持續時間（秒）（預設值：120.0） | FLOAT | 是 | 1.0 - 1000.0 (step 0.1) |
| `batch_size` | 批次中的潛在影像數量（預設值：1） | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 傳回以零填充的空白潛在音訊樣本。輸出包含一個 `samples` 張量，以及一個設為 `"audio"` 的 `type` 欄位。 | LATENT |

注意：潛在長度是根據 `seconds` 值，使用內部取樣率 44100 Hz 計算，公式為 `int(seconds × 44100 / 512 / 8)` 幀。產生的潛在張量完全以零填充。

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
