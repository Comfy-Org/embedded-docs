# Recraft V4 建立風格

此節點可從 1 到 10 張參考圖像建立可重複使用的 Recraft V4 樣式。傳回的樣式 ID 可與相同輸出類型的每個 Recraft V4 和 V4.1 模型搭配使用，並可在後續的圖像生成步驟中重複使用。所有參考圖像的總大小限制為 10 MB。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 建立樣式所針對的輸出類型：`recraftv4_styles` 用於點陣圖，`recraftv4_styles_vector` 用於 SVG。 | COMBO | 是 | "recraftv4_styles"<br>"recraftv4_styles_vector" |
| `images` | 定義樣式的參考圖像。相似的參考圖像可強化匹配，多樣化的參考圖像可擴大匹配範圍。可擴展槽位：連接 1 至 10 張圖像（`image_1` 至 `image_10`）。 | IMAGE | 是 | 1 至 10 images |

### 備註

- 至少需要一張參考圖像；若未提供任何圖像，節點會報錯。
- 最多允許 10 張參考圖像。
- 所有參考圖像的編碼後總大小不得超過 10 MB；若超過限制，節點會報錯。
- 每張參考圖像在傳送至 Recraft API 前會縮小至最多 2048×2048 像素，並編碼為 WebP 格式。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `style_id` | 所建立樣式的唯一識別碼，可與相同輸出類型的所有 Recraft V4 和 V4.1 模型搭配使用。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `63b31ff08d5cfe7c0d4de6987f2ee5a34bd491237ed0fb4c93c225e33b7cede3`
