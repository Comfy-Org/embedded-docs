# Grok 圖像編輯

根據文字提示修改一個或多個現有影像。此節點會使用所選模型，將已連接的參考影像與提示傳送至 Grok 影像編輯 API，然後傳回編輯後的影像。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `模型` | 要使用的 Grok 影像模型。下方顯示的子參數會依所選模型而有所不同。 | DYNAMIC_COMBO | 是 | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `提示詞` | 用於產生影像的文字提示。（預設值：""） | STRING | 是 | N/A |
| `種子` | 用於判斷節點是否應重新執行的種子；無論種子為何，實際結果皆為非確定性。（預設值：0） | INT | 是 | 0 到 2147483647 |

### grok-imagine-image-2.0 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `resolution` | 編輯後影像的輸出解析度。 | COMBO | 是 | "1K"<br>"2K" |
| `number_of_images` | 要產生的編輯後影像數量。（預設值：1） | INT | 是 | 1 到 10 |
| `quality` | 產生影像的品質等級。 | COMBO | 是 | "medium"<br>"low" |
| `aspect_ratio` | 編輯後影像的長寬比。（預設值："auto"） | COMBO | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-quality 與 grok-imagine-image 輸入

由 grok-imagine-image-quality 與 grok-imagine-image 共用。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `resolution` | 編輯後影像的輸出解析度。 | COMBO | 是 | "1K"<br>"2K" |
| `number_of_images` | 要產生的編輯後影像數量。（預設值：1） | INT | 是 | 1 到 10 |
| `aspect_ratio` | 僅在連接多張影像時允許使用。（預設值："auto"） | COMBO | 是 | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### grok-imagine-image-pro 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `resolution` | 編輯後影像的輸出解析度。 | COMBO | 是 | "1K"<br>"2K" |
| `number_of_images` | 要產生的編輯後影像數量。（預設值：1） | INT | 是 | 1 到 10 |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可擴充插槽：連接 1 到 N 張要編輯的參考影像。插槽使用範本名稱 `image_1`、`image_2`、`image_3`；插槽數量上限取決於所選模型。 | IMAGE | 是 | 1 張影像，適用於 `grok-imagine-image-pro`<br>1 到 3 張影像，適用於 `grok-imagine-image-2.0`、`grok-imagine-image-quality` 與 `grok-imagine-image` |

**限制注意事項：**
- `prompt` 必須包含至少 1 個非空白字元。
- 編輯時至少需要一張參考影像；若未連接任何影像，節點會引發錯誤。
- 輸入影像數量上限為：`grok-imagine-image-pro` 為 1，`grok-imagine-image-2.0`、`grok-imagine-image-quality` 與 `grok-imagine-image` 為 3。連接超過模型支援數量的影像會引發錯誤。
- 影像限制會計算已連接輸入中的每一張影像，因此包含多張影像的批次會以多張影像計入限制。
- 對於 `grok-imagine-image-quality` 與 `grok-imagine-image`，僅在連接多張影像時才允許自訂 `aspect_ratio`（任何非 "auto" 的值）。只有一張影像時，`aspect_ratio` 必須為 "auto"。
- 對於 `grok-imagine-image-2.0`，即使只有一張影像，也可以自由設定 `aspect_ratio`。
- `quality` 子參數僅適用於 `grok-imagine-image-2.0`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Grok API 傳回的編輯後影像。若產生單一影像，會直接傳回該影像。若產生多張影像，則會串接成單一批次張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
