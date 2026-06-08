## 概述

使用 HappyHorse 模型，透過文字指令或參考圖片來編輯影片。輸出時長為 3-15 秒，並與輸入影片匹配；超過 15 秒的輸入將被截斷。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 模型配置，包含模型選擇、提示詞、解析度、畫面比例以及可選的參考圖片。 | DICT | 是 | 見下方 |
| `video` | 要編輯的影片。 | VIDEO | 是 | - |
| `seed` | 用於生成的隨機種子（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `watermark` | 是否在結果中添加 AI 生成的水印（預設值：False）。 | BOOLEAN | 否 | True / False |

### `model` 參數詳細說明

`model` 參數是一個包含以下欄位的字典：

| 欄位 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要使用的 HappyHorse 影片編輯模型。 | STRING | 是 | `"happyhorse-1.0-video-edit"` |
| `prompt` | 編輯指令或風格轉換需求。長度必須至少為 1 個字元。 | STRING | 是 | - |
| `resolution` | 輸出解析度。 | STRING | 是 | `"720P"`<br>`"1080P"` |
| `ratio` | 畫面比例。若未更改，則會近似輸入影片的比例。 | STRING | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `reference_images` | 可選的參考圖片（image1、image2、image3、image4、image5），用於引導編輯。 | DICT | 否 | 0 至 5 張圖片 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 編輯後的影片輸出。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/zh-TW.md)

---
**Source fingerprint (SHA-256):** `af6747efbea1c65e4909d35dad009cbc2ffaad787d0f2031581c227deb9bf53c`
