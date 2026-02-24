> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsAudioIsolation/zh-TW.md)

此節點可從音訊檔案中移除背景噪音，隔離人聲或語音。它會將音訊發送至 ElevenLabs API 進行處理，並返回處理後的乾淨音訊。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `audio` | AUDIO | 是 | | 需要進行背景噪音移除處理的音訊。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 已移除背景噪音的處理後音訊。 |