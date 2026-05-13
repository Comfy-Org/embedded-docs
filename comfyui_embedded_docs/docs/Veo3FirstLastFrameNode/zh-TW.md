> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3FirstLastFrameNode/zh-TW.md)

## 概述

Veo3FirstLastFrameNode 使用 Google 的 Veo 3 模型，根據文字提示以及提供的首幀和尾幀來生成影片，這些幀定義了影片序列的開始與結束。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | 無 | 影片的文字描述（預設：空字串）。 |
| `negative_prompt` | STRING | 否 | 無 | 負面文字提示，用於引導影片中應避免的內容（預設：空字串）。 |
| `resolution` | COMBO | 是 | `"720p"`<br>`"1080p"`<br>`"4k"` | 輸出影片的解析度。 |
| `aspect_ratio` | COMBO | 否 | `"16:9"`<br>`"9:16"` | 輸出影片的長寬比（預設："16:9"）。 |
| `duration` | INT | 否 | 4 到 8 | 輸出影片的時長（秒）（預設：8）。 |
| `seed` | INT | 否 | 0 到 4294967295 | 影片生成的種子（預設：0）。 |
| `first_frame` | IMAGE | 是 | 無 | 影片的起始幀。 |
| `last_frame` | IMAGE | 是 | 無 | 影片的結束幀。 |
| `model` | COMBO | 否 | `"veo-3.1-generate"`<br>`"veo-3.1-fast-generate"`<br>`"veo-3.1-lite"` | 用於生成的特定 Veo 3 模型（預設："veo-3.1-generate"）。 |
| `generate_audio` | BOOLEAN | 否 | 無 | 為影片生成音訊（預設：True）。 |

**注意：** `veo-3.1-lite` 模型不支援 4K 解析度。如果您選擇 `veo-3.1-lite` 和 `4k` 解析度，將會發生錯誤。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `b486b22e71a305172700760bb3eff256b0e571bba75e68f27e23a1e1a1319b5a`
