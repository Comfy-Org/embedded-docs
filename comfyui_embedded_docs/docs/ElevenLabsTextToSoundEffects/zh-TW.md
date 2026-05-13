> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsTextToSoundEffects/zh-TW.md)

## 概述

ElevenLabs 文字轉音效節點可根據文字描述生成音效。它使用 ElevenLabs API 根據您的提示詞創建音效，讓您能夠控制持續時間、循環行為以及音效與文字的貼合程度。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `文字` | STRING | 是 | 不適用 | 要生成音效的文字描述。此為必填欄位。 |
| `模型` | COMBO | 是 | `"eleven_sfx_v2"` | 用於音效生成的模型。選擇此模型會顯示額外參數：`duration`（預設值：5.0，範圍：0.5 至 30.0 秒）、`loop`（預設值：False）和 `prompt_influence`（預設值：0.3，範圍：0.0 至 1.0）。 |
| `輸出格式` | COMBO | 是 | `"mp3_44100_192"`<br>`"opus_48000_192"` | 音頻輸出格式。 |

**參數詳細說明：**

* **`model["duration"]`**：生成音效的持續時間（以秒為單位）。預設值為 5.0，最小值為 0.5，最大值為 30.0。
* **`model["loop"]`**：啟用後可創建平滑循環的音效。預設值為 False。
* **`model["prompt_influence"]`**：控制生成結果與文字提示的貼合程度。數值越高，音效越貼近文字描述。預設值為 0.3，範圍從 0.0 到 1.0。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `audio` | AUDIO | 生成的音效音頻檔案。 |

---
**Source fingerprint (SHA-256):** `c23c4dd3c9c12f0e891d40683265c5b74b5c6320601aaadb686489510db9f107`
