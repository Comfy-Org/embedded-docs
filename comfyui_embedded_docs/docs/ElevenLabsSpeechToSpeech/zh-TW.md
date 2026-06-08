## 概述

ElevenLabs 語音轉語音節點可將輸入的音訊檔案從一種聲音轉換為另一種聲音。它使用 ElevenLabs API 進行語音轉換，同時保留原始音訊的內容和情感語調。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `目標語音` | 轉換的目標聲音。從語音選擇器或即時語音克隆連接。 | CUSTOM | 是 | - |
| `音訊` | 要轉換的來源音訊。 | AUDIO | 是 | - |
| `穩定性` | 語音穩定性。較低的值提供更廣泛的情感範圍，較高的值產生更一致但可能單調的語音（預設值：0.5）。 | FLOAT | 否 | 0.0 - 1.0 |
| `模型` | 用於語音轉語音轉換的模型。每個選項提供一組特定的語音設定（相似度增強、風格、使用說話者增強、速度）。 | DYNAMICCOMBO | 否 | `eleven_multilingual_sts_v2`<br>`eleven_english_sts_v2` |
| `輸出格式` | 音訊輸出格式（預設值："mp3_44100_192"）。 | COMBO | 否 | `"mp3_44100_192"`<br>`"opus_48000_192"` |
| `種子` | 用於可重現性的種子（預設值：0）。 | INT | 否 | 0 - 4294967295 |
| `移除背景噪音` | 使用音訊隔離技術從輸入音訊中移除背景噪音（預設值：False）。 | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `音訊` | 以指定輸出格式轉換後的音訊檔案。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ElevenLabsSpeechToSpeech/zh-TW.md)

---
**Source fingerprint (SHA-256):** `118fe6e85b146d0649b104d814abb518d37f69ade2e53becac365a0ec90146fd`
