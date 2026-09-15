# ByteDance Seed Audio 1.0

使用 ByteDance Seed Audio 1.0，從單一提示詞產生語音、音樂、音效與多說話者對話。在提示詞中描述語音、情緒、環境音、背景音樂與音效，並包含要說出的台詞。可選用內建預設語音、從最多 3 個參考片段複製語音（在提示詞中以 @Audio1-3 標註），或從角色圖像衍生語音。每次執行最多可產生 2 分鐘音訊。此多語言模型支援 20 種語言，以及以時間戳為基礎的時間控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text_prompt` | 描述語音、情緒、節奏、環境音、背景音樂與音效，並包含要說出的台詞（若為對話，可在行內標註角色名稱）。在「audio reference」模式中，依連接順序以 @Audio1、@Audio2、@Audio3 參照連接的片段。使用多語言模型時，引號中的台詞可以時間戳範圍開頭，以控制其開始說話的時間與持續長度，例如 `[5.5s:8.0s] Wait for me!`。請以與要說台詞相同的語言撰寫提示詞。最少 1 個字元，最多 3000 個字元。 | STRING | 是 | 1 到 3000 個字元 |
| `reference_mode` | 如何調節語音：「text only」（在提示詞中描述所有內容）、「audio reference」（複製最多 3 個語音，以 @Audio1-3 標註）、「image reference」（從單一角色圖像衍生語音），或「preset voice」（選擇內建的具名語音來朗讀提示詞）。 | COMBO | 是 | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | 用於語音複製的參考片段，在提示詞中以 @Audio1 標註。最多 30 秒。僅當 `reference_mode` 為「audio reference」時可用。 | AUDIO | 否 | 最多 30 秒 |
| `reference_audio_2` | 在提示詞中以 @Audio2 標註的參考片段。最多 30 秒。僅當 `reference_mode` 為「audio reference」時可用。 | AUDIO | 否 | 最多 30 秒 |
| `reference_audio_3` | 在提示詞中以 @Audio3 標註的參考片段。最多 30 秒。僅當 `reference_mode` 為「audio reference」時可用。 | AUDIO | 否 | 最多 30 秒 |
| `reference_image` | 單一角色圖像；模型會從中衍生語音。不能與參考音訊合併使用。僅當 `reference_mode` 為「image reference」時可用。 | IMAGE | 否 | - |
| `preset_voice` | 內建的 TTS 2.0 語音，會朗讀提示詞。此模式不需要參考片段，且不使用 @AudioN 標籤。當 `reference_mode` 為「preset voice」時為必填。 | COMBO | 否 | 多個內建預設語音選項（預設選取第一個選項） |
| `sample_rate` | 輸出取樣率，單位為 Hz。（預設值："24000"） | COMBO | 是 | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | 說話速度。0 = 正常，100 = 2.0x，-50 = 0.5x。（預設值：0） | INT | 是 | -50 到 100 |
| `loudness_rate` | 音量。0 = 正常，100 = 2.0x，-50 = 0.5x。（預設值：0） | INT | 是 | -50 到 100 |
| `pitch_rate` | 音高位移，單位為半音（-12 到 12）。（預設值：0） | INT | 是 | -12 到 12 |
| `seed` | 種子碼控制節點是否應重新執行；無論種子碼為何，結果皆不具確定性。（預設值：42） | INT | 是 | 0 到 2147483647 |
| `model` | 模型版本。`seed-audio-1.0-multilingual` 支援 20 種語言，並可透過 `[5.5s:8.0s]` 時間戳進行逐句時間控制。`seed-audio-1.0` 僅支援英語與中文，且不支援時間控制。（預設值："seed-audio-1.0-multilingual"） | COMBO | 否 | `"seed-audio-1.0-multilingual"`<br>`"seed-audio-1.0"` |

### 參數限制

- **參考模式相依性**：`reference_mode` 參數決定哪些其他輸入為必填：
  - **"text only"**：無需其他輸入。提示詞不得包含 @AudioN 標籤。
  - **"audio reference"**：需要連接 `reference_audio_1`、`reference_audio_2` 或 `reference_audio_3` 其中至少一個。參考片段必須依序連接且不得有缺口。每個片段最長限制為 30 秒。若提示詞中使用 @AudioN 標籤，最高標籤編號不得超過已連接的參考片段數量。
  - **"image reference"**：需要連接 `reference_image`。不使用 @AudioN 標籤；提示詞應只包含要合成的文字。
  - **"preset voice"**：需要選擇一個預設語音。整個提示詞會以所選語音朗讀；@AudioN 標籤不會用作參考，且會拒絕 @Audio2 或更高編號的標籤。

- **音訊參考排序**：在「audio reference」模式中，參考音訊輸入必須從 `reference_audio_1` 開始依序連接，且不得跳過。例如，可以連接 `reference_audio_1` 與 `reference_audio_2`，但不能在沒有 `reference_audio_2` 的情況下連接 `reference_audio_1` 與 `reference_audio_3`。

- **最大音訊標籤數**：在「audio reference」模式中，最多可連接 3 個參考片段（@Audio1、@Audio2、@Audio3），且提示詞中最高 @AudioN 標籤不得超過已連接的參考音訊輸入數量。

- **模型差異**：`seed-audio-1.0-multilingual` 模型支援 20 種語言（英語、中文、日語、韓語、墨西哥西班牙語與卡斯提亞西班牙語、印尼語、德語、巴西葡萄牙語、法語、泰語、越南語、馬來語、菲律賓語、義大利語、俄語、荷蘭語、波蘭語、土耳其語、瑞典語），並支援使用 `[5.5s:8.0s]` 格式的時間戳進行逐句時間控制。`seed-audio-1.0` 模型僅支援英語與中文，且不支援時間控制。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `AUDIO` | 由 ByteDance Seed Audio 1.0 產生的音訊輸出，包含提示詞中所述的語音、音樂、音效或多說話者對話。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e86e4edde424b4427d864350a9d3b082e271fbd2b1e335175637a9cc3ad51163`
