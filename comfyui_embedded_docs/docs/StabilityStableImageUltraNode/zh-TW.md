> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/zh-TW.md)

基於提示詞和解析度同步生成圖像。此節點使用 Stability AI 的 Stable Image Ultra 模型，處理您的文字提示詞，並根據指定的長寬比和風格生成對應的圖像。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 您希望在輸出圖像中看到的內容。一個強而有力、描述性強的提示詞，清楚定義元素、顏色和主體，將能獲得更好的結果。若要控制特定詞彙的權重，請使用 `(詞彙:權重)` 格式，其中 `詞彙` 是您想控制權重的詞，`權重` 是介於 0 到 1 之間的值。例如：`The sky was a crisp (blue:0.3) and (green:0.8)` 表示天空呈現藍色和綠色，但綠色多於藍色。 |
| `aspect_ratio` | COMBO | 是 | `"1:1"`<br>`"16:9"`<br>`"21:9"`<br>`"2:3"`<br>`"3:2"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"9:21"` | 生成圖像的長寬比（預設值："1:1"）。 |
| `style_preset` | COMBO | 否 | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` | 可選的生成圖像風格。選擇 "None" 則不套用任何風格預設。 |
| `seed` | INT | 是 | 0 - 4294967294 | 用於產生噪點的隨機種子。 |
| `image` | IMAGE | 否 | - | 用於圖像到圖像生成的可選輸入圖像。 |
| `negative_prompt` | STRING | 否 | - | 描述您不希望出現在輸出圖像中的內容的文字。這是一個進階功能。 |
| `image_denoise` | FLOAT | 否 | 0.0 - 1.0 | 輸入圖像的去噪強度；0.0 會產生與輸入完全相同的圖像，1.0 則如同完全未提供圖像（預設值：0.5）。 |

**注意：** 當未提供輸入圖像時，`image_denoise` 參數會自動停用並被忽略。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | IMAGE | 根據輸入參數生成的圖像。 |

---
**Source fingerprint (SHA-256):** `2fd9e106a3460a39c33ecc9a15ab6414dab1914fdc43e4f546827e02c889cf62`
