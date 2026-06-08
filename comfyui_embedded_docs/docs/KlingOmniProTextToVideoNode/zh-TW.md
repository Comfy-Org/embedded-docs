此節點使用最新的 Kling AI 模型，根據文字描述生成影片。它會將您的提示詞發送到遠端 API，並返回生成的影片。此節點讓您能夠控制影片的長度、形狀、品質，甚至建立多鏡頭故事板。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 用於影片生成的特定 Kling 模型（預設值：`"kling-v3-omni"`）。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `提示詞` | 描述影片內容的文字提示詞。可包含正面和負面描述。啟用故事板時忽略此參數。 | STRING | 是 | 0 到 2500 個字元 |
| `長寬比` | 要生成影片的形狀或尺寸。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `時長` | 影片的長度，以秒為單位（預設值：5）。 | INT | 是 | 3 到 15 秒 |
| `解析度` | 影片的品質或像素解析度（預設值：`"1080p"`）。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `分鏡腳本` | 生成一系列帶有各自提示詞和時長的影片片段。o1 模型不支援此功能。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `產生音訊` | 是否為影片生成音訊（預設值：False）。 | BOOLEAN | 否 | True / False |
| `種子` | 種子值控制節點是否應重新執行；無論種子值為何，結果皆非確定性（預設值：0）。 | INT | 否 | 0 到 2147483647 |

### 參數限制與注意事項

- **模型特定限制：**
  - `kling-video-o1` 模型僅支援 **5 或 10 秒** 的時長。
  - `kling-video-o1` 模型**不**支援音訊生成。
  - `kling-video-o1` 模型**不**支援 4k 解析度。
  - `kling-video-o1` 模型**不**支援故事板。
- **故事板限制：**
  - 啟用故事板時，`prompt` 欄位將被忽略。
  - 每個故事板需要自己的提示詞（1 到 512 個字元）和時長。
  - 所有故事板的總時長必須完全等於全域 `duration` 參數。
- **提示詞要求：**
  - 當故事板**停用**時，`prompt` 欄位為必填（至少 1 個字元）。
  - 當故事板**啟用**時，`prompt` 欄位可以為空（0 個字元）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `output` | 根據提供的文字提示詞和設定生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2f867e0bd2e7b0ec901a9ad8d2adcfe712ed479c1613b80f86af3a20863e9f4c`
