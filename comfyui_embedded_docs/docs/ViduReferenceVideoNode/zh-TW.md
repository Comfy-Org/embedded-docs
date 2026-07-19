# Vidu 參考圖像轉影片生成

Vidu 參考影片節點可從多張參考圖片和文字提示生成影片。它使用 AI 模型根據提供的圖片和描述建立一致的影片內容。此節點支援多種影片設定，包括時長、長寬比、解析度和動態控制。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 用於影片生成的模型名稱（預設值："viduq1"） | COMBO | 是 | `"viduq1"` |
| `images` | 用作參考的圖片，以生成具有一致主體的影片（最多 7 張圖片） | IMAGE | 是 | - |
| `prompt` | 用於影片生成的文字描述 | STRING | 是 | - |
| `duration` | 輸出影片的時長（秒）（預設值：5） | INT | 否 | 5-5 |
| `seed` | 影片生成的隨機種子（0 表示隨機）（預設值：0） | INT | 否 | 0-2147483647 |
| `aspect_ratio` | 輸出影片的長寬比（預設值："16:9"） | COMBO | 否 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `resolution` | 支援的數值可能因模型和時長而異（預設值："1080p"） | COMBO | 否 | `"1080p"` |
| `movement_amplitude` | 畫面中物體的動態幅度（預設值："auto"） | COMBO | 否 | `"auto"`<br>`"small"`<br>`"medium"`<br>`"large"` |

**限制與約束：**

- `prompt` 欄位為必填，不可為空
- 最多允許 7 張參考圖片
- 每張圖片的長寬比必須介於 1:4 和 4:1 之間
- 每張圖片的最小尺寸必須為 128x128 像素
- 時長固定為 5 秒

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 根據參考圖片和提示生成的影片 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduReferenceVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `11a7de2f50658467f63d284ef6b95d91dcdd39b4e6e5cea3b8d2f2a5d63a3020`
