# Breeze Text to Speech

使用 Breeze TTS 2 將文字轉換為語音。挑選一個 Breeze 聲音、選擇文字所用的語言，並可選擇性地指示這句台詞的演出方式。英文與中文可使用任一 Breeze TTS 2 模型；其他所有語言則使用 Breeze TTS 2 Multilingual。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `voice` | 用於朗讀的 Breeze 聲音，來自 Breeze Voice Selector 或其中一個 Breeze 聲音建立節點。 | BREEZE_VOICE | 是 | - |
| `text` | 要朗讀的文字，1 至 1000 個字元。音訊標籤如 `(laughs)` 或 `(sighs)` 會被演出而非朗讀。預設：空。 | STRING | 是 | 1 至 1000 個字元 |
| `language` | 文字所用的語言。英文與中文可使用任一模型；其他語言則使用 Breeze TTS 2 Multilingual。聲音在其自身語言中聽起來最好，因此若要使用其他語言，請使用以 Breeze Voice Localize 製作的副本。 | DYNAMIC_COMBO | 是 | 提供多個選項 |
| `delivery` | 這句台詞的演出方式：`neutral` 保持聲音原樣，`directed` 依照書面指示。預設：`"neutral"`。 | DYNAMIC_COMBO | 是 | `"neutral"`<br>`"directed"` |
| `speed` | 速度倍率，不會改變音高。預設：1.0。 | FLOAT | 否 | 0.5 至 2.0（步進值：0.05） |
| `seed` | 控制節點是否重新執行；無論種子為何，結果都是非確定性的。預設：42。 | INT | 否 | 0 至 2147483647 |

### Language "English" and "Chinese" 輸入

這些參數僅在 `language` 為英文或中文時出現。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | `Breeze TTS 2` 或 `Breeze TTS 2 Multilingual`。預設：`"Breeze TTS 2"`。 | COMBO | 是 | `"Breeze TTS 2"`<br>`"Breeze TTS 2 Multilingual"` |

### Delivery "neutral" 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `speaker_boost` | 讓聲音更接近其原始音色。預設：false。 | BOOLEAN | 否 | true<br>false |

### Delivery "directed" 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `instructions` | 文字該如何演出，以與文字相同的語言撰寫。預設：空。 | STRING | 否 | 多行文字 |
| `strength` | 聲音遵循指示的程度。預設：4.0。 | FLOAT | 否 | 1.0 至 10.0（步進值：0.1） |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `audio` | 產生的語音，為 WAV 音訊。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BreezeTextToSpeech/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e5e5201e8c951a878ef9e764db31e494285ddded6ec66d8e818ec132342bbe5c`
