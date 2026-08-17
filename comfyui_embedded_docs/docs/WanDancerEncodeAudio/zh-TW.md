# WanDancerEncodeAudio

此節點處理音頻輸入以提取可用於引導視頻生成模型的特徵。它分析音頻以偵測節奏、拍子及其他音樂特性，然後將此資訊打包成適合對視頻模型進行條件化的格式，使生成的視頻能與音頻同步。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要分析並編碼的音頻輸入。 | AUDIO | 是 | - |
| `video_frames` | 目標視頻的幀數。用於計算同步的幀率（預設值：149）。 | INT | 是 | Min: 1, Max: 268435456 (MAX_RESOLUTION), Step: 4 |
| `audio_inject_scale` | 將音頻特徵注入視頻模型時的縮放比例（預設值：1.0）。 | FLOAT | 是 | Min: 0.0, Max: 10.0, Step: 0.01 |

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `audio_encoder_output` | 包含處理後音頻特徵、計算出的幀率（fps）及音頻注入比例的字典。此輸出用於對視頻生成模型進行條件化。 | AUDIO_ENCODER_OUTPUT |
| `fps_string` | 描述根據音頻長度和視頻幀數計算出的幀率（fps）的文字字串。此字串旨在用於視頻模型的提示詞中。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
