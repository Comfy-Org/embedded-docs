> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/zh-TW.md)

# Grok 影片節點

Grok 影片節點可根據文字描述生成短影片。它能透過提示詞從頭開始建立影片，或根據提示詞對單張輸入圖片進行動畫處理。此節點會向外部 API 發送請求，並返回生成的影片。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"grok-imagine-video"`<br>`"grok-imagine-video-beta"` | 用於影片生成的模型。 |
| `prompt` | STRING | 是 | - | 所需影片的文字描述。 |
| `resolution` | COMBO | 是 | `"480p"`<br>`"720p"` | 輸出影片的解析度。 |
| `aspect_ratio` | COMBO | 是 | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` | 輸出影片的長寬比（預設值："auto"）。 |
| `duration` | INT | 是 | 1 至 15 | 輸出影片的時長（秒）（預設值：6）。 |
| `seed` | INT | 是 | 0 至 2147483647 | 用於決定節點是否應重新執行的種子；實際結果無論種子為何皆為非確定性（預設值：0）。 |
| `image` | IMAGE | 否 | - | 可選的輸入圖片，用於進行動畫處理。 |

**注意：** 如果提供了 `image`，則僅支援單張圖片。提供多張圖片將會導致錯誤。`prompt` 在去除空白字元後必須至少包含 1 個字元。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | VIDEO | 生成的影片。 |

---
**Source fingerprint (SHA-256):** `d48049fafbe4dbf50eb5a42495d445fa4c7fc590a1d70267e220ccedc2f5328a`
