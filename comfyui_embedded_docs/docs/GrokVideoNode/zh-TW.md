# Grok 影片

Grok Video 節點可從文字描述生成短片。它能使用提示詞從零建立影片，或從單張輸入影像生成影片。此節點會將請求傳送至外部 API，並回傳生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型。 | COMBO | 是 | `"grok-imagine-video"`<br>`"grok-imagine-video-1.5"` |
| `prompt` | 目標影片的文字描述。當提供輸入影像時，對 grok-imagine-video-1.5 為可選。 | STRING | 是 | - |
| `resolution` | 輸出影片的解析度。1080p 僅適用於 grok-imagine-video-1.5。 | COMBO | 是 | `"480p"`<br>`"720p"`<br>`"1080p"` |
| `aspect_ratio` | 輸出影片的長寬比。 | COMBO | 是 | `"auto"`<br>`"16:9"`<br>`"4:3"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"3:4"`<br>`"9:16"` |
| `duration` | 輸出影片的時長（秒）（預設值：6）。 | INT | 是 | 1 至 15 |
| `seed` | 種子，用於決定節點是否應重新執行；無論種子值為何，實際結果皆不具確定性（預設值：0）。 | INT | 是 | 0 至 2147483647 |
| `image` | 可選的起始影像。若省略，則僅根據文字提示詞生成影片。 | IMAGE | 否 | - |

**注意：** 提供 `image` 時，僅支援單張輸入影像；提供多張影像將導致錯誤。當未提供影像時，或使用 `grok-imagine-video` 即使有提供影像時，`prompt` 在去除空白字元後必須為非空字串。對於 `grok-imagine-video-1.5`，只有在提供輸入影像時，`prompt` 才是可選的。`1080p` 解析度僅適用於 `grok-imagine-video-1.5`。當 `aspect_ratio` 設定為 `"auto"` 時，長寬比將由服務自動選擇。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `c7d07b7bf9a776892873698abb97c7d936c7770aab397d031a287b7ecfad0b71`
