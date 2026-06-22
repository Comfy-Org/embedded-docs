# Google Veo 3 首尾影格生成影片

## 概述

Veo3FirstLastFrameNode 使用 Google 的 Veo 3 模型，根據文字提示以及提供的首幀和尾幀來生成影片，這些幀定義了影片序列的開始與結束。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `提示詞` | 影片的文字描述（預設：空字串）。 | STRING | 是 | 無 |
| `反向提示詞` | 負面文字提示，用於引導影片中應避免的內容（預設：空字串）。 | STRING | 否 | 無 |
| `解析度` | 輸出影片的解析度。 | COMBO | 是 | `"720p"`<br>`"1080p"`<br>`"4k"` |
| `長寬比` | 輸出影片的長寬比（預設："16:9"）。 | COMBO | 否 | `"16:9"`<br>`"9:16"` |
| `時長` | 輸出影片的時長（秒）（預設：8）。 | INT | 否 | 4 到 8 |
| `種子` | 影片生成的種子（預設：0）。 | INT | 否 | 0 到 4294967295 |
| `起始影格` | 影片的起始幀。 | IMAGE | 是 | 無 |
| `結束影格` | 影片的結束幀。 | IMAGE | 是 | 無 |
| `模型` | 用於生成的特定 Veo 3 模型（預設："veo-3.1-generate"）。 | COMBO | 否 | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` |
| `生成音訊` | 為影片生成音訊（預設：True）。 | BOOLEAN | 否 | 無 |

**注意：** `veo-3.1-lite` 模型不支援 4K 解析度。如果您選擇 `veo-3.1-lite` 和 `4k` 解析度，將會發生錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
