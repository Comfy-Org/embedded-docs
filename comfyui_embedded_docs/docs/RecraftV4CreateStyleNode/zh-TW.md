# Recraft V4 建立風格

此節點會從 1 到 10 張參考影像建立可重複使用的 Recraft V4 風格。傳回的風格 ID 可搭配相同輸出類型（點陣或向量）的每個 Recraft V4 和 V4.1 模型使用，並且可在後續影像生成步驟中重複使用。所有參考影像的總大小限制為 10 MB。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要為其建立風格的模型。Standard 和 Pro 共用同一個風格池：點陣風格可搭配每個 Recraft V4 和 V4.1 點陣模型，向量風格（`*_vector`）可搭配每個 V4 和 V4.1 向量模型。 | COMBO | 是 | "recraftv4_styles"<br>"recraftv4_styles_vector"<br>"recraftv4_styles_pro"<br>"recraftv4_styles_pro_vector" |
| `images` | 定義風格的參考影像。相似的參考影像會使匹配更精準，多樣的參考影像則會擴大匹配範圍。可擴充插槽：連接 1 到 10 張影像（`image_1` 到 `image_10`）。 | IMAGE | 是 | 1 至 10 images |

### 備註

- 至少需要一張參考影像；若未提供任何參考影像，節點會引發錯誤。
- 最多允許 10 張參考影像；若提供超過 10 張，節點會引發錯誤。
- 所有參考影像的編碼後總大小不得超過 10 MB；若超過限制，節點會引發錯誤。
- 每張參考影像在傳送至 Recraft API 前，會先縮小至最多 2048×2048 像素，並編碼為 WebP。
- 結尾為 `_vector` 的模型會建立向量風格；其他選項則建立點陣風格。Standard 和 Pro 模型在每種輸出類型中會共用相同的風格池。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `style_id` | 所建立風格的唯一識別碼，可搭配相同輸出類型的每個 Recraft V4 和 V4.1 模型使用。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`
