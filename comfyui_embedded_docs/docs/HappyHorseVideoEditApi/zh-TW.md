> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/zh-TW.md)

## 概述

使用 HappyHorse 模型，透過文字指令或參考圖片來編輯影片。輸出時長與輸入影片相符（3-15 秒），超過 15 秒的輸入會自動截斷。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | DICT | 是 | 見下方 | 模型配置，包含模型選擇、提示詞、解析度、畫面比例及可選的參考圖片。 |
| `video` | VIDEO | 是 | - | 要編輯的影片。 |
| `seed` | INT | 是 | 0 至 2147483647 | 用於生成的隨機種子（預設值：0）。 |
| `watermark` | BOOLEAN | 否 | True / False | 是否在結果中加入 AI 生成浮水印（預設值：False）。 |

### `model` 參數詳細說明

`model` 參數是一個字典，包含以下欄位：

| 欄位 | 資料類型 | 必要 | 範圍 | 說明 |
|-------|-----------|----------|-------|-------------|
| `model` | STRING | 是 | `"happyhorse-1.0-video-edit"` | 要使用的 HappyHorse 影片編輯模型。 |
| `prompt` | STRING | 是 | - | 編輯指令或風格轉換需求。長度至少需為 1 個字元。 |
| `resolution` | STRING | 是 | `"720P"`<br>`"1080P"` | 輸出解析度。 |
| `ratio` | STRING | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 畫面比例。若未更改，則會近似輸入影片的比例。 |
| `reference_images` | DICT | 否 | 0 至 5 張圖片 | 可選的參考圖片（image1、image2、image3、image4、image5），用於引導編輯。 |

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `video` | VIDEO | 編輯後的影片輸出。 |