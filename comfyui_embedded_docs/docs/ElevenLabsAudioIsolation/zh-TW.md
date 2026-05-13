> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/zh-TW.md)

ElevenLabs 語音隔離節點可從音訊檔案中移除背景噪音，隔離出人聲或語音。它會將音訊傳送至 ElevenLabs API 進行處理，並返回清理後的音訊。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `音訊` | AUDIO | 是 | | 要進行背景噪音移除處理的音訊。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `音訊` | AUDIO | 已移除背景噪音的處理後音訊。 |

---
**Source fingerprint (SHA-256):** `eca7919ff853fe48f8419a4135a99589e350d3d113631e27f6e7cb3cbb3faa3b`
