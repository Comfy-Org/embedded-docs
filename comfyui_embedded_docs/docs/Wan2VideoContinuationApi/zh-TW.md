> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/zh-TW.md)

## 概述

Wan 2.7 影片延續節點會生成一個新的影片片段，從輸入影片剪輯的結尾無縫銜接。它使用 Wan 2.7 模型根據文字提示合成延續內容，並可選擇性地引導結尾朝向特定的目標影格。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| `model` | COMBO | 是 | `"wan2.7-i2v"` | 要使用的影片生成模型。 |
| `model.prompt` | STRING | 是 | - | 描述元素和視覺特徵的提示。支援英文和中文。（預設：空字串） |
| `model.negative_prompt` | STRING | 是 | - | 描述應避免內容的負面提示。（預設：空字串） |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 輸出影片的解析度。 |
| `model.duration` | INT | 是 | 2 至 15 | 總輸出時長（秒）。模型會生成延續內容，以填補輸入剪輯之後的剩餘時間。（預設：5） |
| `first_clip` | VIDEO | 是 | - | 要從其延續的輸入影片。時長：2 秒至 10 秒。輸出影片的長寬比由此影片決定。 |
| `last_frame` | IMAGE | 否 | - | 最後影格影像。延續內容將過渡至此影格。 |
| `seed` | INT | 是 | 0 至 2147483647 | 用於生成的隨機種子。（預設：0） |
| `prompt_extend` | BOOLEAN | 是 | - | 是否使用 AI 輔助增強提示。（預設：True） |
| `watermark` | BOOLEAN | 是 | - | 是否在結果中添加 AI 生成浮水印。（預設：False） |

**注意：** `first_clip` 輸入影片的時長必須在 2 到 10 秒之間。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
| :--- | :--- | :--- |
| `output` | VIDEO | 生成的影片延續內容。 |

---
**Source fingerprint (SHA-256):** `5e9d2c7800603660f5f994d125e1e32f2b310234c4b6a24d502c764d91be49e8`
