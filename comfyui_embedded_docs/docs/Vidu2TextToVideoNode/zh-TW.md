# Vidu2 文字轉影片生成

## 概述

Vidu2 文字轉影片生成節點可根據文字描述建立影片。此節點會連接外部 API，根據您的提示詞生成影片內容，讓您能夠控制影片的長度、視覺風格與格式。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的 AI 模型。目前僅提供一個模型可供使用。 | COMBO | 是 | `"viduq2"` |
| `prompt` | 用於影片生成的文字描述，最大長度為 2000 個字元。 | STRING | 是 | - |
| `duration` | 生成影片的長度（以秒為單位）。可使用滑桿調整數值（預設值：5）。 | INT | 否 | 1 到 10 |
| `seed` | 用於控制生成隨機性的數值，可產生可重現的結果。可在生成後進行控制（預設值：1）。 | INT | 否 | 0 到 2147483647 |
| `aspect_ratio` | 影片寬度與高度之間的比例關係。 | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"3:4"`<br>`"4:3"`<br>`"1:1"` |
| `resolution` | 生成影片的像素尺寸。此為進階參數。 | COMBO | 否 | `"720p"`<br>`"1080p"` |
| `background_music` | 是否為生成的影片添加背景音樂（預設值：False）。此為進階參數。 | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu2TextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1e9e3629806e9b5a66d8f830d8ec33ef208a7a27b53caf43b44f7b746a85014b`
