# EmptyAceStepLatentAudio

Empty Ace Step 1.0 Latent Audio 節點會建立指定時長的空白潛在音訊樣本。它會產生一批以零填充的靜音音訊潛在表示，其長度是根據輸入的秒數和音訊處理參數計算而來。此節點適用於初始化需要潛在表示的音訊處理工作流程。

## 輸入

| 參數 | 描述 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `秒數` | 音訊的持續時間（以秒為單位）（預設值：120.0，步長：0.1） | FLOAT | 是 | 1.0 - 1000.0 |
| `批次大小` | 批次中的潛在影像數量（預設值：1） | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名 | 描述 | 資料型別 |
| --- | --- | --- |
| `output` | 傳回以零填充的空潛在音訊樣本。輸出包含一個 `samples` 張量以及一個設定為「audio」的 `type` 欄位。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
