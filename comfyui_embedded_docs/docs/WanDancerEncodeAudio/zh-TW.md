# WanDancerEncodeAudio

## 概述

此節點處理音訊輸入以提取可用於引導影片生成模型的特徵。它分析音訊以偵測節奏、節拍和其他音樂特性，然後將這些資訊打包成適合條件化影片模型的格式，使生成的影片能夠與音訊同步。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要分析和編碼的音訊輸入。 | AUDIO | 是 | - |
| `video_frames` | 目標影片的幀數。用於計算同步所需的幀率（預設值：149）。 | INT | 是 | 最小值：1，最大值：268435456 (MAX_RESOLUTION)，步長：4 |
| `audio_inject_scale` | 音訊特徵注入影片模型時的縮放比例（預設值：1.0）。 | FLOAT | 是 | 最小值：0.0，最大值：10.0，步長：0.01 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio_encoder_output` | 一個字典，包含處理後的音訊特徵、計算出的幀率 (fps) 以及音訊注入縮放比例。此輸出用於條件化影片生成模型。 | AUDIO_ENCODER_OUTPUT |
| `fps_string` | 基於音訊長度和影片幀數計算出的幀率 (fps) 文字描述。此字串旨在用於影片模型的提示詞中。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ef230c92b23a04369708041b2e5d03c1b2928edf746dc43020bae777f9f0b589`
