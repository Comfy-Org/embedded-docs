## 概述

此節點使用 Wan 2.7 模型，根據文字描述生成影片。它將您的請求發送到外部 API，該 API 會處理提示詞並回傳影片檔案。您可以選擇性地提供音訊片段，以影響影片的動作和時間節奏。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的特定模型。 | COMBO | 是 | `"wan2.7-t2v"` |
| `model.prompt` | 描述您希望在影片中出現的元素和視覺特徵。支援英文和中文。 | STRING | 是 | - |
| `model.negative_prompt` | 描述您希望在生成的影片中避免出現的元素或特徵。 | STRING | 否 | - |
| `model.resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `model.ratio` | 輸出影片的長寬比。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `model.duration` | 影片的長度，單位為秒（預設值：5）。 | INT | 是 | 2 到 15 |
| `audio` | 用於驅動影片生成的音訊檔案，例如用於唇形同步或使動作配合節拍。如果未提供，模型將自動生成匹配的背景音樂或音效。音訊長度必須在 1.5 到 60 秒之間。 | AUDIO | 否 | - |
| `seed` | 用於控制生成隨機性的數字，確保結果可重現（預設值：0）。 | INT | 否 | 0 到 2147483647 |
| `prompt_extend` | 啟用後，提示詞將透過 AI 輔助進行增強（預設值：True）。 | BOOLEAN | 否 | - |
| `watermark` | 啟用後，AI 生成的水印將添加到結果中（預設值：False）。 | BOOLEAN | 否 | - |

**注意：** `audio` 參數為可選項。如果提供，其長度必須在 1.5 到 60 秒之間。如果省略，模型將自動生成音訊。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ce8a2f4e53b2bce879f143c66f6078fd81c6308e2822cb486b1cf8e178a6f58c`
