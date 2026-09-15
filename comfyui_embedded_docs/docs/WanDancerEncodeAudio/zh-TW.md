# WanDancerEncodeAudio

此節點會分析音訊片段，並將其轉換成一組可引導影片生成模型的特徵。它會估計速度與節拍，提取梅爾頻譜圖、MFCC、色度與起始特徵，然後將這些特徵與計算出的影格率一起封裝，以供同步使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `audio` | 要分析與編碼的音訊輸入。若音訊有多個聲道，在特徵提取前會將聲道平均為單聲道。 | AUDIO | 是 | - |
| `video_frames` | 目標影片的影格數。用於計算同步用的影格率（預設值：149）。 | INT | 是 | Min: 1, Max: 16384 (MAX_RESOLUTION), Step: 4 |
| `audio_inject_scale` | 音訊特徵注入影片模型時的縮放比例（預設值：1.0）。 | FLOAT | 是 | Min: 0.0, Max: 10.0, Step: 0.01 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `audio_encoder_output` | 包含處理後音訊特徵、計算出的影格率（fps）以及音訊注入縮放比例的字典。此輸出用於對影片生成模型進行條件控制。 | AUDIO_ENCODER_OUTPUT |
| `fps_string` | 根據音訊長度與影片影格數計算出的影格率（fps）的文字字串。此字串預期用於影片模型的提示詞中。其格式為中文，以符合參考流程。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
