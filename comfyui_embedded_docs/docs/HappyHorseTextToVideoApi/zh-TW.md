## 概述

使用 HappyHorse 模型根據文字提示生成影片。此節點會將您的提示和設定發送到 HappyHorse API，等待影片生成完成，然後下載結果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 包含模型選擇及其相關參數的字典。模型必須為 `"happyhorse-1.0-t2v"`。此字典包含以下子參數：<br><br>**`prompt`** (STRING)：您想要生成影片的文字描述。支援英文和中文。（預設值：""）。<br>**`resolution`** (COMBO)：輸出影片的解析度。選項：`"720P"`、`"1080P"`。<br>**`ratio`** (COMBO)：輸出影片的長寬比。選項：`"16:9"`、`"9:16"`、`"1:1"`、`"4:3"`、`"3:4"`。<br>**`duration`** (INT)：影片的長度，以秒為單位。（預設值：5，最小值：3，最大值：15，步長：1）。 | DICT | 是 | 請參閱說明 |
| `seed` | 用於生成的隨機種子。使用相同的種子和相同的輸入將產生相同的結果。（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `watermark` | 是否在結果中添加 AI 生成的水印。（預設值：False）。 | BOOLEAN | 否 | True / False |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `VIDEO` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseTextToVideoApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `8c6a7c0c2b10bbc65ca54abc991e1f12e8846b31701ed65b49c5d71f1b2a63ec`
