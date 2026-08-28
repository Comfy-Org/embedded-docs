# WanDancerEncodeAudio

此節點處理音訊輸入以提取可用於引導影片生成模型的特徵。它會分析音訊以偵測節奏、節拍及其他音樂特性，然後將這些資訊包裝成適合對影片模型進行條件化的格式，使生成的影片能與音訊同步。

## 輸入

| 參數 | 說明 | 資料型別 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要分析和編碼的音訊輸入。若音訊有多個聲道，會在特徵提取前將聲道平均為單聲道。 | AUDIO | 是 | - |
| `video_frames` | 目標影片中的幀數。用於計算同步的幀率（預設值：149）。 | INT | 是 | 最小值：1，最大值：268435456（MAX_RESOLUTION），步長：4 |
| `audio_inject_scale` | 注入影片模型時的音訊特徵縮放比例（預設值：1.0）。 | FLOAT | 是 | 最小值：0.0，最大值：10.0，步長：0.01 |

## 輸出

| 輸出名稱 | 說明 | 資料型別 |
| --- | --- | --- |
| `audio_encoder_output` | 包含處理後音訊特徵、計算出的幀率（fps）及音訊注入比例的字典。此輸出用於對影片生成模型進行條件化。 | AUDIO_ENCODER_OUTPUT |
| `fps_string` | 描述根據音訊長度和影片幀數計算出的幀率（fps）的文字字串。此字串預期用於影片模型的提示詞中。其格式為中文，以符合參考管線。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
