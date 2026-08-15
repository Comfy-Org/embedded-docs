# Grok 圖像編輯

Modify an existing image based on a text prompt. This node sends your images and a text description to the Grok API, which edits the images according to your instructions and returns the result.

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的 Grok 影像模型。下方顯示的子參數會依所選模型而變更。 | MODEL | 是 | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `提示詞` | 用於產生影像的文字提示。(預設值："") | STRING | 是 | N/A |
| `種子` | 用於決定節點是否重新執行的種子；無論種子為何，實際結果皆為非確定性。(預設值：0) | INT | 是 | 0 至 2147483647 |

### grok-imagine-image-2.0 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要編輯的參考影像。最多 3 張影像。 | IMAGE | 是 | 1 至 3 張影像 |
| `resolution` | 編輯後影像的輸出解析度。 | STRING | 是 | "1K"<br>"2K" |
| `number_of_images` | 要產生的編輯後影像數量。(預設值：1) | INT | 是 | 1 至 10 |
| `quality` | 產生影像的品質等級。 | STRING | 是 | "medium"<br>"low" |
| `aspect_ratio` | 編輯後影像的外觀比例。(預設值："auto") | STRING | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality 與 grok-imagine-image 輸入

由 grok-imagine-image-quality 與 grok-imagine-image 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要編輯的參考影像。最多 3 張影像。 | IMAGE | 是 | 1 至 3 張影像 |
| `resolution` | 編輯後影像的輸出解析度。 | STRING | 是 | "1K"<br>"2K" |
| `number_of_images` | 要產生的編輯後影像數量。(預設值：1) | INT | 是 | 1 至 10 |
| `aspect_ratio` | 僅在連接多張影像時允許使用。(預設值："auto") | STRING | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 要編輯的參考影像。 | IMAGE | 是 | 1 張影像 |
| `resolution` | 編輯後影像的輸出解析度。 | STRING | 是 | "1K"<br>"2K" |
| `number_of_images` | 要產生的編輯後影像數量。(預設值：1) | INT | 是 | 1 至 10 |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可擴充插槽：連接 1 張或多張要編輯的參考影像。可以新增編號插槽，例如 `image_1`、`image_2`、`image_3`。影像數量上限取決於所選模型（請參閱上方模型區段）。 | IMAGE | 是 | 1 至 3 張影像，依模型而定 |

**限制說明：**
- `prompt` 必須至少包含 1 個非空白字元。
- 編輯至少需要一張參考影像；若未連接任何影像，節點會回報錯誤。
- 輸入影像數量上限：`grok-imagine-image-pro` 為 1 張；`grok-imagine-image-2.0`、`grok-imagine-image-quality` 與 `grok-imagine-image` 為 3 張。連接超過模型支援的影像數量會回報錯誤。
- 對於 `grok-imagine-image-quality` 與 `grok-imagine-image`，僅在連接多張影像時允許使用自訂的 `aspect_ratio`（非 "auto" 的值）。使用單張影像時，`aspect_ratio` 必須為 "auto"。
- 對於 `grok-imagine-image-2.0`，即使使用單張影像，也可以自由設定 `aspect_ratio`。
- `quality` 子參數僅在 `grok-imagine-image-2.0` 中可用。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | 由 Grok API 回傳的編輯後影像。若產生單張影像，會直接回傳。若產生多張影像，則會串接成單一批量張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
