# ByteDance Seedream 4.5 與 5.0

ByteDance Seedream 4.5 與 5.0 可根據文字提示詞生成影像（文字轉圖像），或在可選參考影像引導下生成/編輯影像，使用 ByteDance Seedream 4.0、4.5 和 5.0 模型，解析度最高可達 4K。此節點會將提示詞與任何參考影像傳送至 ByteDance API，等待生成任務完成，並回傳產生的影像張量或張量。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 用於建立或編輯影像的文字提示詞。去除空白後不得為空。 | STRING | 是 | 多行文字 |
| `模型` | 選擇要使用的 Seedream 模型。每個模型會在下方公開其各自的子參數與限制。 | DYNAMIC_COMBO | 是 | "seedream 5.0 pro"<br>"seedream 5.0 flash"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro 輸入 (seedream 5.0 pro)

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇推薦尺寸。選擇 Custom 以使用下方的寬度與高度。預設：此模型的第一個推薦預設。 | COMBO | 否 | 模型專屬的推薦尺寸預設<br>"Custom" |
| `width` | 影像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4514 （步進值：2） |
| `height` | 影像的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4514 （步進值：2） |
| `prompt_optimization` | 提供參考影像時的提示詞優化模式：'standard' 可獲得更高品質，'fast' 可縮短生成時間。預設："standard"。 | COMBO | 否 | "standard"<br>"fast" |
| `seed` | 用於生成的種子。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在影像中加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞優化推理（「thinking」）以獲得更好的遵循度。可能大幅增加生成時間——尤其是在 Seedream 5.0 Pro 上。僅能在文字轉圖像時停用（提供參考影像時無法停用）。預設：true。 | BOOLEAN | 否 | true / false |

### Seedream 5.0 Flash 輸入 (seedream 5.0 flash)

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇推薦尺寸。選擇 Custom 以使用下方的寬度與高度。預設：此模型的第一個推薦預設。 | COMBO | 否 | 模型專屬的推薦尺寸預設<br>"Custom" |
| `width` | 影像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4514 （步進值：2） |
| `height` | 影像的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4514 （步進值：2） |
| `seed` | 用於生成的種子。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在影像中加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |

### Seedream 5.0 Lite 輸入 (seedream 5.0 lite)

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇推薦尺寸。選擇 Custom 以使用下方的寬度與高度。預設：此模型的第一個推薦預設。 | COMBO | 否 | 模型專屬的推薦尺寸預設<br>"Custom" |
| `width` | 影像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 6240 （步進值：2） |
| `height` | 影像的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4992 （步進值：2） |
| `max_images` | 要生成的最大影像數量。設為 1 時，會精確產生一張影像。設為 >1 時，模型會產生 1 到 `max_images` 張相關影像（例如故事場景、角色變化）。總影像數（輸入 + 生成）不得超過 15。預設：1。 | INT | 否 | 1 至 14 |
| `fail_on_partial` | 若啟用，當任何要求的影像缺失或回傳錯誤時，會中止執行。預設：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在影像中加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞優化推理（「thinking」）以獲得更好的遵循度。可能大幅增加生成時間——尤其是在 Seedream 5.0 Pro 上。僅能在文字轉圖像時停用（提供參考影像時無法停用）。預設：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.5 輸入 (seedream-4-5-251128)

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇推薦尺寸。選擇 Custom 以使用下方的寬度與高度。預設：此模型的第一個推薦預設。 | COMBO | 否 | 模型專屬的推薦尺寸預設<br>"Custom" |
| `width` | 影像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 6240 （步進值：2） |
| `height` | 影像的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4992 （步進值：2） |
| `max_images` | 要生成的最大影像數量。設為 1 時，會精確產生一張影像。設為 >1 時，模型會產生 1 到 `max_images` 張相關影像（例如故事場景、角色變化）。總影像數（輸入 + 生成）不得超過 15。預設：1。 | INT | 否 | 1 至 10 |
| `fail_on_partial` | 若啟用，當任何要求的影像缺失或回傳錯誤時，會中止執行。預設：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在影像中加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞優化推理（「thinking」）以獲得更好的遵循度。可能大幅增加生成時間——尤其是在 Seedream 5.0 Pro 上。僅能在文字轉圖像時停用（提供參考影像時無法停用）。預設：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.0 輸入 (seedream-4-0-250828)

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇推薦尺寸。選擇 Custom 以使用下方的寬度與高度。預設：此模型的第一個推薦預設。 | COMBO | 否 | 模型專屬的推薦尺寸預設<br>"Custom" |
| `width` | 影像的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 6240 （步進值：2） |
| `height` | 影像的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4992 （步進值：2） |
| `max_images` | 要生成的最大影像數量。設為 1 時，會精確產生一張影像。設為 >1 時，模型會產生 1 到 `max_images` 張相關影像（例如故事場景、角色變化）。總影像數（輸入 + 生成）不得超過 15。預設：1。 | INT | 否 | 1 至 10 |
| `fail_on_partial` | 若啟用，當任何要求的影像缺失或回傳錯誤時，會中止執行。預設：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在影像中加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞優化推理（「thinking」）以獲得更好的遵循度。可能大幅增加生成時間——尤其是在 Seedream 5.0 Pro 上。僅能在文字轉圖像時停用（提供參考影像時無法停用）。預設：true。 | BOOLEAN | 否 | true / false |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可擴充插槽：用於圖像轉圖像或多參考生成的選用參考影像。連接 1..N 張影像（例如 `image_1`、`image_2`、...）；數量限制因模型而異（請參閱下方附註）。若連接的影像包含一批影像，該批次中的每張影像都會計入限制。 | IMAGE | 否 | 0 至 10 (Seedream 5.0 Pro, Seedream 5.0 Flash, Seedream 4.5, Seedream 4.0)<br>0 至 14 (Seedream 5.0 Lite) |

**附註：**

- `prompt` 去除空白後不得為空。
- 參考影像數量上限：Seedream 5.0 Pro、Seedream 5.0 Flash、Seedream 4.5 和 Seedream 4.0 為 10 張；Seedream 5.0 Lite 為 14 張。
- 每張參考影像的長寬比必須介於 1:16 與 16:1 之間。
- 當 `max_images` 大於 1 時（Seedream 5.0 Pro 或 Seedream 5.0 Flash 不支援），參考影像加生成影像的總數不得超過 15。
- `thinking` 僅能在文字轉圖像生成時停用。提供參考影像時，必須啟用 `thinking`。Seedream 5.0 Flash 沒有 `thinking` 輸入。
- `width` 與 `height` 僅會在 `size_preset` 設為 "Custom" 時使用。
- `prompt_optimization` 僅適用於 Seedream 5.0 Pro。
- `max_images` 與 `fail_on_partial` 僅適用於 Seedream 5.0 Lite、Seedream 4.5 和 Seedream 4.0；Seedream 5.0 Pro 與 Seedream 5.0 Flash 一律只要求一張影像。
- 解析度要求（寬 x 高）：
  - Seedream 5.0 Pro 與 Seedream 5.0 Flash：介於 0.92MP（921,600 像素）與 4.62MP（4,624,220 像素）之間。
  - Seedream 5.0 Lite 與 Seedream 4.5：至少 3.68MP（3,686,400 像素）。
  - Seedream 4.0：至少 0.92MP（921,600 像素）。
  - Seedream 5.0 Lite、Seedream 4.5 和 Seedream 4.0：最多 16.78MP（16,777,216 像素）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成的影像張量。當生成多張影像時，它們會串接成單一批次的 IMAGE 張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `1c1f40b202ccbb3e0f73cd072170e1c16b833e007f26e63505b54c42b004a8a6`
