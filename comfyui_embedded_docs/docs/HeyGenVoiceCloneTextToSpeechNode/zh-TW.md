# HeyGen Voice 1.0 Instant Clone Text to Speech

使用 HeyGen Voice 1.0，從單一講者的錄音中複製聲音，並以該聲音朗讀文字。此節點會上傳錄音、合成語音並以音訊形式回傳，因此單一節點即可從語音樣本產出完成的語音。

選擇 `model` 後會顯示其專屬參數：`audio`、`text`、`language`、`expressiveness_boost`、`recording_language`、`similarity`、`remove_background_noise` 與 `seed`。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的模型。`heygen-voice-1-turbo` 速度更快且成本更低（預設：`"heygen-voice-1"`）。 | DYNAMIC_COMBO | 是 | `"heygen-voice-1"`<br>`"heygen-voice-1-turbo"` |
| `audio` | 要複製的單一講者錄音。請使用至少 10 秒清晰的語音；僅使用前 3 分鐘。 | AUDIO | 是 | - |
| `text` | 要朗讀的文字，最多 5000 個字元。超過約 12 分鐘的語音會失敗，因此請將極長的中文或日文文字分段（預設：空）。 | STRING | 是 | 1 至 5000 個字元 |
| `language` | 文字的語言。對於塞爾維亞語或馬來語等密切相關的語言，請自行設定，因為自動偵測可能會混淆（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>多種語言預設集 |
| `expressiveness_boost` | 數值越高表現力越強；數值越低則越接近原始聲音（預設：0.5）。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.05） |
| `recording_language` | 錄音中使用的語言，可將複製的聲音限定為該語言（預設：`"auto"`）。 | COMBO | 是 | `"auto"`<br>多種語言預設集 |
| `similarity` | 聲音與錄音的接近程度（預設：`"max"`）。 | COMBO | 是 | `"medium"`<br>`"high"`<br>`"extra_high"`<br>`"max"` |
| `remove_background_noise` | 在複製前清除錄音中的背景雜訊（預設：True）。 | BOOLEAN | 是 | `True`<br>`False` |
| `seed` | `seed` 控制節點是否重新執行；無論 `seed` 為何，結果皆不具確定性（預設：42）。 | INT | 是 | 0 至 2147483647 |

`text` 必須至少包含一個字元，且 `audio` 為必填：若錄音包含多位講者，或雜訊過多而無法複製，將得到品質不佳的聲音。當樣本的語言不明顯時，請設定 `recording_language`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `AUDIO` | 以複製的聲音朗讀的文字。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVoiceCloneTextToSpeechNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ea18e2abce687e106ed0b37eb7afd723fbe72a3b4d58124a143c00b66d2fe7c9`
