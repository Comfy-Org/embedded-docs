# WanDancerPadKeyframesList

## 概述

此節點接收一系列影像與可選的音軌，並將其分割成指定數量的填充片段。其設計目的是為影片生成準備關鍵幀序列，其中每個片段會被填充至一致的長度，並建立相應的遮罩以標示哪些影格是有效的。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要分割成片段的輸入影像序列。 | IMAGE | 是 | 不適用 |
| `segment_length` | 每個片段的影格長度（預設值：149）。 | INT | 是 | 1 至 10000 |
| `num_segments` | 要輸出為列表的填充片段數量（預設值：1）。 | INT | 是 | 1 至 100 |
| `audio` | 要為每個輸出片段進行裁剪的音訊。 | AUDIO | 否 | 不適用 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `keyframes_mask` | 填充後的關鍵幀序列列表，每個片段對應一個序列。 | IMAGE |
| `audio_segment` | 遮罩列表，標示每個片段中有效的影格。 | MASK |
| `audio_segment` | 音訊片段列表，每個影片片段對應一個音訊片段。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c6a3ddca3fd61fcdb287fecb6969796eebd65e70f1174abdab57912586d27d00`
