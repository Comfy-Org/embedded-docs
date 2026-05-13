> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoEditApi/zh-TW.md)

## 概述

Wan2VideoEditApi 節點使用 Wan 2.7 模型，根據文字指令、參考圖片或風格轉換來編輯影片。它會處理輸入的影片，並根據指定的參數（如解析度、時長和長寬比）生成新的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"wan2.7-videoedit"` | 用於影片編輯的模型。 |
| `model.prompt` | STRING | 是 | - | 編輯指令或風格轉換需求。（預設值：空字串） |
| `model.resolution` | COMBO | 是 | `"720P"`<br>`"1080P"` | 輸出影片的解析度。 |
| `model.ratio` | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` | 輸出影片的長寬比。若未更改，則會近似於輸入影片的長寬比。 |
| `model.duration` | COMBO | 是 | `"auto"`<br>`"2"`<br>`"3"`<br>`"4"`<br>`"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"` | 輸出時長（秒）。'auto' 會匹配輸入影片的時長。指定特定數值則會從影片開頭截取。（預設值："auto"） |
| `model.reference_images` | IMAGE | 否 | - | 最多 4 張參考圖片，用於引導編輯。 |
| `video` | VIDEO | 是 | - | 要編輯的影片。 |
| `seed` | INT | 否 | 0 至 2147483647 | 用於生成的隨機種子。（預設值：0） |
| `audio_setting` | COMBO | 否 | `"auto"`<br>`"origin"` | 'auto'：模型根據提示詞決定是否重新生成音訊。'origin'：保留輸入影片的原始音訊。（預設值："auto"） |
| `watermark` | BOOLEAN | 否 | - | 是否在結果中添加 AI 生成的水印。（預設值：False） |

**限制條件：**
*   `model.prompt` 的長度必須至少為 1 個字元。
*   輸入的 `video` 時長必須在 2 到 10 秒之間。
*   `model.reference_images` 輸入最多可接受 4 張圖片。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 模型生成的編輯後影片。 |

---
**Source fingerprint (SHA-256):** `d2dd65d743358c6a357e75076774e93c52c39893fbb376da2f4395446f440a20`
