# ByteDance Seedream 4.5 & 5.0

此節點使用 ByteDance Seedream 模型（4.0、4.5、5.0 Lite 與 5.0 Pro）建立或編輯圖像。它可根據文字提示產生新圖像，並可依據參考圖像與單句指示編輯現有圖像，支援最高 4K 解析度。

## 輸入

`model` 選擇器決定可用的模型特定輸入。以下表格列出常見輸入、每個模型的輸入，以及可擴充的參考圖像插槽。

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要用於生成的 Seedream 模型版本。每個模型有不同的能力、限制與定價。 | DYNAMIC_COMBO | 是 | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | 用於建立或編輯圖像的文字提示。 | STRING | 是 | 任意文字（非空） |
| `seed` | 生成時使用的種子（預設：0）。 | INT | 是 | 0 to 2147483647 |
| `watermark` | 是否要為圖像加上「AI 生成」浮水印（預設：False）。 | BOOLEAN | 是 | True / False |
| `thinking` | 啟用模型的提示最佳化推理（「思考」）以提升指示遵循度。可能大幅增加生成時間——尤其在 Seedream 5.0 Pro 上。僅可在純文字生成圖像（text-to-image）時停用（提供參考圖像時不可停用）。（預設：True） | BOOLEAN | 否 | True / False |

### seedream 5.0 pro 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議尺寸。選擇 Custom 以使用下方的 width 與 height。 | COMBO | 是 | 模型專用預設（包含 Custom） |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 3136 (step 2) |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 2496 (step 2) |

### seedream 5.0 lite 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議尺寸。選擇 Custom 以使用下方的 width 與 height。 | COMBO | 是 | 模型專用預設（包含 Custom） |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 6240 (step 2) |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 4992 (step 2) |
| `max_images` | 要生成的最大圖像數量。設為 1 時，會剛好產生一張圖像。設為 >1 時，模型會產生 1 到 max_images 張相關圖像（例如故事場景、角色變化）。圖像總數（輸入 + 生成）不得超過 15。（預設：1） | INT | 是 | 1 to 14 |
| `fail_on_partial` | 啟用後，如果任何要求的圖像缺失或回傳錯誤，則中止執行。（預設：False） | BOOLEAN | 是 | True / False |

### seedream-4-5-251128 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議尺寸。選擇 Custom 以使用下方的 width 與 height。 | COMBO | 是 | 模型專用預設（包含 Custom） |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 6240 (step 2) |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 4992 (step 2) |
| `max_images` | 要生成的最大圖像數量。設為 1 時，會剛好產生一張圖像。設為 >1 時，模型會產生 1 到 max_images 張相關圖像（例如故事場景、角色變化）。圖像總數（輸入 + 生成）不得超過 15。（預設：1） | INT | 是 | 1 to 10 |
| `fail_on_partial` | 啟用後，如果任何要求的圖像缺失或回傳錯誤，則中止執行。（預設：False） | BOOLEAN | 是 | True / False |

### seedream-4-0-250828 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議尺寸。選擇 Custom 以使用下方的 width 與 height。 | COMBO | 是 | 模型專用預設（包含 Custom） |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 6240 (step 2) |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 Custom 時此值才生效（預設：2048）。 | INT | 是 | 1024 to 4992 (step 2) |
| `max_images` | 要生成的最大圖像數量。設為 1 時，會剛好產生一張圖像。設為 >1 時，模型會產生 1 到 max_images 張相關圖像（例如故事場景、角色變化）。圖像總數（輸入 + 生成）不得超過 15。（預設：1） | INT | 是 | 1 to 10 |
| `fail_on_partial` | 啟用後，如果任何要求的圖像缺失或回傳錯誤，則中止執行。（預設：False） | BOOLEAN | 是 | True / False |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可選的參考圖像，用於圖像到圖像或多參考生成。可擴充插槽：連接 1..N 個項目（`image_1`、`image_2`、...、`image_N`）；最大數量取決於所選模型（seedream 5.0 pro、seedream-4-5-251128 與 seedream-4-0-250828 為 10；seedream 5.0 lite 為 14）。 | IMAGE | 否 | 0 to 10<br>0 to 14 (seedream 5.0 lite) |

### 注意事項

- 自訂的 `width` 與 `height` 值只有在 `size_preset` 設為 Custom 時才會生效。
- 解析度限制（依 width × height）：
  - seedream 5.0 pro：最低 0.92 MP，最高 4.19 MP。
  - seedream 5.0 lite 與 seedream-4-5-251128：最低 3.68 MP。
  - seedream-4-0-250828：最低 0.92 MP。
  - seedream 5.0 lite、seedream-4-5-251128 與 seedream-4-0-250828：最高 16.78 MP。
- 參考圖像的長寬比必須介於 1:3 與 3:1 之間。
- 當 `max_images` 大於 1 時（適用於 seedream 5.0 lite、seedream-4-5-251128 與 seedream-4-0-250828），圖像總數（參考圖像加生成圖像）不得超過 15。
- `thinking` 僅可在純文字生成圖像時停用；提供參考圖像時必須啟用。
- seedream 5.0 pro 一律生成單張圖像，因此不會顯示 `max_images` 或 `fail_on_partial` 輸入。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成或編輯後的圖像。如果使用 `max_images` 要求多張圖像，則會將它們拼接成單一批次回傳。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b57e0d85a586aaeb7cf02ceaaddcd2d36cdac20f5251cba48de602a979420f1c`
