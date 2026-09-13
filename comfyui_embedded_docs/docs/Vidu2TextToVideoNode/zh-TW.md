# Vidu2 文字轉影片生成

Vidu2 文字轉影片生成節點可根據文字描述建立影片。它會連接至外部 API，依據你的提示詞生成影片內容，讓你能控制影片的長度、視覺風格與格式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 AI 模型。目前僅有一個模型可供使用。 | COMBO | 是 | `"viduq2"` |
| `prompt` | 用於影片生成的文字描述，長度上限為 2000 個字元。 | STRING | 是 | - |
| `duration` | 生成影片的長度，以秒為單位。此數值可使用滑桿調整（預設：5）。 | INT | 否 | 1 至 10 |
| `seed` | 用於控制生成隨機性的數值，可讓結果重現。生成後仍可進行控制（預設：1）。 | INT | 否 | 0 至 2147483647 |
| `aspect_ratio` | 影片寬度與高度之間的比例關係。 | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | 生成影片的像素尺寸。此為進階參數。 | COMBO | 否 | `"720p"`<br>`"1080p"` |
| `background_music` | 是否為生成的影片加入背景音樂（預設：False）。此為進階參數。 | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `27b7c05ae1b3b23d07e775f67474ecef1ffc0bd8240f4aa2219e15949d854f27`
