# EmptyAceStepLatentAudio

Empty Ace Step 1.0 Latent Audio 節點會建立指定時長的空白潛在音訊樣本。它會填入一批靜音（全零）的音訊潛在樣本，其長度會根據 `seconds` 輸入並使用音訊處理參數計算得出。這通常用於初始化需要潛在表示作為起點的音訊工作流程。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `秒數` | 音訊時長（秒）（預設：120.0，步長：0.1） | FLOAT | 是 | 1.0 - 1000.0 |
| `批次大小` | 批次中的潛在影像數量（預設：1） | INT | 是 | 1 - 4096 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 傳回以零填充的空白潛在音訊樣本。輸出包含 `samples` 張量，以及設為 "audio" 的 `type` 欄位。 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
