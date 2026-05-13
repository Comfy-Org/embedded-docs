> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/zh-TW.md)

# IdeogramV1 節點

此文件由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！[在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/en.md)

IdeogramV1 節點透過 API 使用 Ideogram V1 模型生成圖像。它接收文字提示和各種生成設定，根據您的輸入創建一個或多個圖像。該節點支援不同的寬高比和生成模式，以自訂輸出結果。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `prompt` | STRING | 是 | - | 圖像生成的提示詞（預設：空） |
| `turbo` | BOOLEAN | 是 | - | 是否使用 turbo 模式（生成速度更快，但品質可能較低）（預設：False） |
| `aspect_ratio` | COMBO | 否 | "1:1"<br>"16:9"<br>"9:16"<br>"4:3"<br>"3:4"<br>"3:2"<br>"2:3" | 圖像生成的寬高比（預設："1:1"） |
| `magic_prompt_option` | COMBO | 否 | "AUTO"<br>"ON"<br>"OFF" | 決定生成時是否使用 MagicPrompt（預設："AUTO"） |
| `seed` | INT | 否 | 0-2147483647 | 用於生成的隨機種子值（預設：0） |
| `negative_prompt` | STRING | 否 | - | 描述應從圖像中排除的內容（預設：空） |
| `num_images` | INT | 否 | 1-8 | 要生成的圖像數量（預設：1） |

**注意：** `num_images` 參數每次生成請求最多限制為 8 張圖像。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `output` | IMAGE | 從 Ideogram V1 模型生成的圖像 |

---
**Source fingerprint (SHA-256):** `7e453cd54b5db48588ed899b0754e0d06fdcfbaed248d13fb74b7049f0f25b8f`
