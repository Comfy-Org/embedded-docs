## 概述

此節點用於在較長影片生成過程中，為特定片段準備關鍵影格序列。它接收一批輸入影像與一條音軌，根據音訊長度計算完整影片應有的總影格數，然後將輸入影像作為關鍵影格分配到所選片段中，其餘部分以空白影格填充。同時，它也會提取該片段對應的音訊部分。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `images` | 要作為關鍵影格分配的輸入影像。 | IMAGE | 是 | 影像批次 |
| `segment_length` | 此片段的影格長度（預設值：149）。 | INT | 是 | 1 至 10000 |
| `segment_index` | 此片段為第幾個片段（0 表示第一個，1 表示第二個，依此類推，預設值：0）。 | INT | 是 | 0 至 100 |
| `audio` | 用於計算總輸出影格數並提取片段音訊的音軌。 | AUDIO | 是 | 音訊資料 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `keyframes_sequence` | 指定片段的填充後關鍵影格序列。 | IMAGE |
| `keyframes_mask` | 遮罩，標示有效影格（1 表示關鍵影格位置，0 表示填充位置）。 | MASK |
| `audio_segment` | 此影片片段對應的音訊片段。 | AUDIO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5a104b45faaa870727d4c45e6327e7233110b40dc5a13515a29e5f14de2050e0`
