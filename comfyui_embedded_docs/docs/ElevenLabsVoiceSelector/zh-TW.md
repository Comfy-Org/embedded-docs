> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsVoiceSelector/zh-TW.md)

此節點允許您從預定義的 ElevenLabs 文字轉語音語音清單中選擇特定語音。它接收語音名稱作為輸入，並輸出音訊生成所需的對應語音識別碼。此節點簡化了為其他 ElevenLabs 音訊節點選擇相容語音的過程。

## 輸入參數

| 參數 | 資料類型 | 必填 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `voice` | STRING | 是 | `"Adam"`<br>`"Antoni"`<br>`"Arnold"`<br>`"Bella"`<br>`"Domi"`<br>`"Elli"`<br>`"Josh"`<br>`"Rachel"`<br>`"Sam"` | 從預定義的 ElevenLabs 語音中選擇一個語音。 |

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `voice` | STRING | 所選 ElevenLabs 語音的獨特識別碼，可傳遞給其他節點用於文字轉語音生成。 |