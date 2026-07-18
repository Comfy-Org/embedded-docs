# ByteDance Seed Audio 1.0

## 概述
透過 ByteDance Seed Audio 1.0，從單一提示詞生成語音、音樂、音效及多人對話。在提示詞中描述聲音、情緒、氛圍、背景音樂和音效，並包含要說出的台詞。可選擇內建預設聲音、從最多 3 個參考片段（在提示詞中標記為 @Audio1-3）複製聲音，或從角色圖片衍生聲音。每次執行最多可生成 2 分鐘的音頻。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `text_prompt` | 描述聲音、情緒、節奏、氛圍、背景音樂和音效，並包含要說出的台詞（對話中內嵌角色名稱）。在「音頻參考」模式下，依序以 @Audio1、@Audio2、@Audio3 引用連接的片段。最多 3000 個字元。 | STRING | 是 | 1 至 3000 個字元 |
| `reference_mode` | 如何設定聲音條件：「僅文字」（在提示詞中描述所有內容）、「音頻參考」（複製最多 3 個聲音，標記為 @Audio1-3）、「圖片參考」（從單一角色圖片衍生聲音），或「預設聲音」（選擇一個內建命名聲音來朗讀提示詞）。 | COMBO | 是 | `"text only"`<br>`"audio reference"`<br>`"image reference"`<br>`"preset voice"` |
| `reference_audio_1` | 用於聲音複製的參考片段，在提示詞中標記為 @Audio1。最長 30 秒。 | AUDIO | 否 | 最長 30 秒 |
| `reference_audio_2` | 在提示詞中標記為 @Audio2 的參考片段。最長 30 秒。 | AUDIO | 否 | 最長 30 秒 |
| `reference_audio_3` | 在提示詞中標記為 @Audio3 的參考片段。最長 30 秒。 | AUDIO | 否 | 最長 30 秒 |
| `reference_image` | 單一角色圖片；模型從中衍生聲音。不能與參考音頻結合使用。 | IMAGE | 否 | 單張圖片 |
| `preset_voice` | 一個內建 TTS 2.0 聲音，用於朗讀提示詞。無需參考片段，且在此模式下不使用 @AudioN 標籤。 | COMBO | 否 | 多個預設聲音選項可用 |
| `sample_rate` | 輸出採樣率（Hz）。（預設值："24000"） | COMBO | 是 | `"8000"`<br>`"16000"`<br>`"24000"`<br>`"32000"`<br>`"44100"`<br>`"48000"` |
| `speech_rate` | 說話速度。0 = 正常，100 = 2.0 倍，-50 = 0.5 倍。（預設值：0） | INT | 是 | -50 至 100 |
| `loudness_rate` | 音量。0 = 正常，100 = 2.0 倍，-50 = 0.5 倍。（預設值：0） | INT | 是 | -50 至 100 |
| `pitch_rate` | 音高偏移（半音），範圍 -12 至 12。（預設值：0） | INT | 是 | -12 至 12 |
| `seed` | 種子碼控制節點是否應重新執行；無論種子碼為何，結果均非確定性。（預設值：42） | INT | 是 | 0 至 2147483647 |

**參數約束與依賴關係：**

- `reference_mode` 的選擇決定了哪些額外參數是必要的：
  - **"text only"**：無需參考輸入。提示詞不得包含 @AudioN 標籤。
  - **"audio reference"**：需要至少連接 `reference_audio_1`、`reference_audio_2` 或 `reference_audio_3` 中的一個。參考片段必須依序連接且無間隔（例如，若使用兩個片段，請連接 `reference_audio_1` 和 `reference_audio_2`）。每個參考音頻片段限制為 30 秒。提示詞必須依序使用 @Audio1、@Audio2、@Audio3 標籤引用已連接的片段。
  - **"image reference"**：需要連接 `reference_image`。不能與任何參考音頻輸入結合使用。提示詞不得包含 @AudioN 標籤。
  - **"preset voice"**：需要選擇 `preset_voice`。無需參考片段。提示詞不得包含 @Audio1 以外的 @AudioN 標籤。

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `audio` | 生成的音頻輸出，作為音頻信號。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `cefd5fca496b02c35022d25be3d99d3911c1304b6e3a751751b58841d5895ef7`
