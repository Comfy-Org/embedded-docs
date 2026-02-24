> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/zh-TW.md)

此節點可根據文字描述生成音效。它使用 ElevenLabs API 來根據您的提示創建音效，讓您可以控制音效的持續時間、循環行為以及音效與文字描述的貼合程度。

## 輸入參數

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `text` | STRING | 是 | N/A | 要生成的音效的文字描述。此為必填欄位。 |
| `model` | COMBO | 是 | `"eleven_sfx_v2"` | 用於生成音效的模型。選擇此模型會顯示額外參數：`duration`（預設值：5.0，範圍：0.5 至 30.0 秒）、`loop`（預設值：False）和 `prompt_influence`（預設值：0.3，範圍：0.0 至 1.0）。 |
| `output_format` | COMBO | 是 | `"mp3_44100_192"`<br>`"opus_48000_192"` | 音訊輸出格式。 |

**參數詳情：**
*   **`model["duration"]`**：生成音效的持續時間（單位：秒）。預設值為 5.0，最小值為 0.5，最大值為 30.0。
*   **`model["loop"]`**：啟用時，會創建一個平滑循環的音效。預設值為 False。
*   **`model["prompt_influence"]`**：控制生成結果與文字提示的貼合程度。數值越高，音效越貼近文字描述。預設值為 0.3，範圍從 0.0 到 1.0。

## 輸出結果

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 生成的音效音訊檔案。 |