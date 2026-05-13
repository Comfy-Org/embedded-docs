> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseImageToVideoApi/zh-TW.md)

## 概述

此節點使用 HappyHorse 模型從單張起始圖片生成短影片。您需要提供第一幀圖像以及描述所需動作和場景的文字提示，節點會根據該圖像生成後續的影片內容。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"happyhorse-1.0-i2v"` | 用於影片生成的 HappyHorse 模型。 |
| `model.prompt` | STRING | 否 | 不適用 | 描述元素和視覺特徵的提示詞。支援英文和中文。（預設值：""） |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 輸出影片的解析度。（預設值："720P"） |
| `model.duration` | INT | 是 | 3 至 15 | 生成影片的時長，單位為秒。（預設值：5） |
| `first_frame` | IMAGE | 是 | 不適用 | 第一幀圖像。輸出影片的長寬比將由此圖像決定。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用於生成的隨機種子。（預設值：0） |
| `watermark` | BOOLEAN | 否 | True / False | 是否在結果中添加 AI 生成浮水印。（預設值：False） |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 生成的影片檔案。 |

---
**Source fingerprint (SHA-256):** `e10ad61abd92df7ad6dd3ac70cc6af35faf0413798f4cff32c81194695bb0bed`
