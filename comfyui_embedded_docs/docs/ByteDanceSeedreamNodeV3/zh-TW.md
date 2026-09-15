# ByteDance Seedream 4.5 與 5.0

ByteDance Seedream 4.5 & 5.0 可依據文字提示詞生成圖像（文字轉圖像），或依據選用的參考圖像來生成／編輯圖像，並使用 ByteDance Seedream 4.0、4.5 與 5.0 模型，解析度最高可達 4K。此節點會將提示詞與任何參考圖像傳送至 ByteDance API，等待生成任務完成，並傳回生成的圖像張量。

## Inputs

### 通用輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 用於建立或編輯圖像的文字提示詞。去除空白字元後不得為空。 | STRING | 是 | Multiline text |
| `模型` | 選擇要使用的 Seedream 模型。每個模型在下方各自擁有專屬的子參數與限制。 | DYNAMIC_COMBO | 是 | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro 輸入（seedream 5.0 pro）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選擇 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議預設尺寸。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 3136 （步進值：2） |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 2496 （步進值：2） |
| `prompt_optimization` | 提供參考圖像時的提示詞最佳化模式：'standard' 可獲得較高品質，'fast' 則縮短生成時間。預設值："standard"。 | COMBO | 否 | "standard"<br>"fast" |
| `seed` | 用於生成的種子。預設值：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖像上加入「AI generated」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以提升遵循度。可能大幅增加生成時間——在 Seedream 5.0 Pro 上尤其明顯。僅能在文字轉圖像時停用（提供參考圖像時無法停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### Seedream 5.0 Lite 輸入（seedream 5.0 lite）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選擇 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議預設尺寸。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 6240 （步進值：2） |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 4992 （步進值：2） |
| `max_images` | 要生成的圖像數量上限。設為 1 時，只會產生恰好一張圖像。設為 >1 時，模型會生成 1 到 max_images 張相關圖像（例如故事場景、角色變化）。圖像總數（輸入 + 生成）不得超過 15。預設值：1。 | INT | 否 | 1 至 14 |
| `fail_on_partial` | 若啟用，當任何要求的圖像缺失或傳回錯誤時，即中止執行。預設值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子。預設值：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖像上加入「AI generated」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以提升遵循度。可能大幅增加生成時間——在 Seedream 5.0 Pro 上尤其明顯。僅能在文字轉圖像時停用（提供參考圖像時無法停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.5 輸入（seedream-4-5-251128）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選擇 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議預設尺寸。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 6240 （步進值：2） |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 4992 （步進值：2） |
| `max_images` | 要生成的圖像數量上限。設為 1 時，只會產生恰好一張圖像。設為 >1 時，模型會生成 1 到 max_images 張相關圖像（例如故事場景、角色變化）。圖像總數（輸入 + 生成）不得超過 15。預設值：1。 | INT | 否 | 1 至 10 |
| `fail_on_partial` | 若啟用，當任何要求的圖像缺失或傳回錯誤時，即中止執行。預設值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子。預設值：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖像上加入「AI generated」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以提升遵循度。可能大幅增加生成時間——在 Seedream 5.0 Pro 上尤其明顯。僅能在文字轉圖像時停用（提供參考圖像時無法停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.0 輸入（seedream-4-0-250828）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選擇 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議預設尺寸。 | COMBO | 否 | Model-specific recommended size presets<br>"Custom" |
| `width` | 圖像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 6240 （步進值：2） |
| `height` | 圖像的自訂高度。僅當 `size_preset` 設為 `Custom` 時才會生效。預設值：2048。 | INT | 否 | 1024 至 4992 （步進值：2） |
| `max_images` | 要生成的圖像數量上限。設為 1 時，只會產生恰好一張圖像。設為 >1 時，模型會生成 1 到 max_images 張相關圖像（例如故事場景、角色變化）。圖像總數（輸入 + 生成）不得超過 15。預設值：1。 | INT | 否 | 1 至 10 |
| `fail_on_partial` | 若啟用，當任何要求的圖像缺失或傳回錯誤時，即中止執行。預設值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子。預設值：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖像上加入「AI generated」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以提升遵循度。可能大幅增加生成時間——在 Seedream 5.0 Pro 上尤其明顯。僅能在文字轉圖像時停用（提供參考圖像時無法停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### 參考輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | 可增長的插槽：用於圖像轉圖像或多參考生成的選用參考圖像。可連接 1..N 張圖像（例如 `image_1`、`image_2`、……）；數量上限依模型而定（請見下方備註）。若連接的圖像包含一個批次的多張圖像，該批次中的每張圖像都會計入上限。 | IMAGE | 否 | 0 至 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 至 14 (Seedream 5.0 Lite) |

**備註：**

- `prompt` 去除空白字元後不得為空。
- 參考圖像數量上限：Seedream 5.0 Pro、Seedream 4.5 與 Seedream 4.0 為 10 張；Seedream 5.0 Lite 為 14 張。
- 每張參考圖像的長寬比必須介於 1:3 與 3:1 之間。
- 當 `max_images` 大於 1 時（Seedream 5.0 Pro 不支援），參考圖像加上生成圖像的總數不得超過 15。
- `thinking` 僅能在文字轉圖像生成時停用。提供參考圖像時，`thinking` 必須保持啟用。
- `width` 與 `height` 僅在 `size_preset` 設為 "Custom" 時才會使用。
- `prompt_optimization` 僅在 Seedream 5.0 Pro 上提供。
- `max_images` 與 `fail_on_partial` 僅在 Seedream 5.0 Lite、Seedream 4.5 與 Seedream 4.0 上提供；Seedream 5.0 Pro 一律只請求單張圖像。
- 解析度要求（寬 x 高）：
  - Seedream 5.0 Pro：介於 0.92MP（921,600 像素）與 4.19MP（4,194,304 像素）之間。
  - Seedream 5.0 Lite 與 Seedream 4.5：至少 3.68MP（3,686,400 像素）。
  - Seedream 4.0：至少 0.92MP（921,600 像素）。
  - 所有非 Pro 模型：最多 16.78MP（16,777,216 像素）。

## Outputs

| Output Name | Description | Data Type |
|-------------|-------------|-----------|
| `image` | 生成的圖像張量。當生成多張圖像時，它們會串接成單一批次化的 IMAGE 張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
