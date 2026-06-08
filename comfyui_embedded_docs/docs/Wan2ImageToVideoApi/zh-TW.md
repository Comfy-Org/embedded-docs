## 概述

Wan 2.7 圖像轉影片節點可從首幀圖像生成影片。您可以選擇性地提供末幀圖像來建立兩者之間的過渡效果，或提供音訊檔案來引導影片的動作與節奏。此節點會根據您的文字描述，使用 AI 模型為場景製作動畫。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 AI 模型。 | COMBO | 是 | `"wan2.7-i2v"` |
| `model.prompt` | 您希望在影片中呈現的元素與視覺特徵的文字描述。支援英文與中文。 | STRING | 是 | - |
| `model.negative_prompt` | 您希望模型避免出現的元素或特徵的文字描述。 | STRING | 是 | - |
| `model.resolution` | 輸出影片的解析度。 | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `model.duration` | 生成影片的長度（秒），預設值為 5。 | INT | 是 | 2 至 15 |
| `first_frame` | 作為影片首幀的圖像。輸出影片的長寬比將由此圖像決定。 | IMAGE | 是 | - |
| `last_frame` | 可選的末幀圖像。提供後，模型將生成從首幀過渡到此末幀的影片。 | IMAGE | 否 | - |
| `audio` | 可選的音訊檔案，用於驅動影片生成，適用於唇形同步或節奏匹配的動作。時長必須在 2 到 30 秒之間。若未提供，模型將生成匹配的背景音樂或音效。 | AUDIO | 否 | - |
| `seed` | 控制生成隨機性的種子值，預設值為 0。 | INT | 是 | 0 至 2147483647 |
| `prompt_extend` | 啟用後，節點將使用 AI 輔助來增強您的文字提示（預設值：True）。此為進階設定。 | BOOLEAN | 是 | - |
| `watermark` | 啟用後，AI 生成的水印將添加到最終影片中（預設值：False）。此為進階設定。 | BOOLEAN | 是 | - |

**注意：** `audio` 輸入有時長限制。若提供音訊檔案，其時長必須在 2 到 30 秒之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ccd18dca3b191f2cbe64b6c2b941a7efcf281e4f327329d932cec27fd8234133`
