# HappyHorse 圖像轉影片

## 概述

此節點使用 HappyHorse 模型從單張起始圖片生成短影片。您需要提供第一幀圖像以及描述所需動作和場景的文字提示，節點會根據該圖像生成後續的影片內容。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 HappyHorse 模型。 | COMBO | 是 | `"happyhorse-1.0-i2v"` |
| `model.prompt` | 描述元素和視覺特徵的提示詞。支援英文和中文。（預設值：""） | STRING | 否 | 不適用 |
| `model.resolution` | 輸出影片的解析度。（預設值："720P"） | COMBO | 是 | `"720P"`<br>`"1080P"` |
| `model.duration` | 生成影片的時長，單位為秒。（預設值：5） | INT | 是 | 3 至 15 |
| `first_frame` | 第一幀圖像。輸出影片的長寬比將由此圖像決定。 | IMAGE | 是 | 不適用 |
| `seed` | 用於生成的隨機種子。（預設值：0） | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在結果中添加 AI 生成浮水印。（預設值：False） | BOOLEAN | 否 | True / False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
