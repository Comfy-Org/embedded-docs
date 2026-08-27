# ByteDanceSeedreamNodeV3

ByteDance Seedream 4.5 & 5.0 可根據文字提示（文字轉影像）生成影像，或在可選參考影像的引導下生成／編輯影像，使用 ByteDance Seedream 4.0、4.5 和 5.0 模型，最高可達 4K 解析度。此節點會將提示與任何參考影像傳送至 ByteDance API，等待生成任務完成，並回傳產生的影像張量（或張量群）。

## 輸入

### 通用輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於建立或編輯影像的文字提示。去除前後空白後不得為空。 | STRING | 是 | 多行文字 |
| `model` | 選擇要使用的 Seedream 模型。每個模型都會在下方顯示各自的子參數與限制。 | DYNAMIC_COMBO | 是 | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro 輸入（seedream 5.0 pro）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議尺寸預設。 | COMBO | 否 | 模型專屬的建議尺寸預設<br>"Custom" |
| `width` | 自訂影像寬度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 3136 (step 2) |
| `height` | 自訂影像高度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 2496 (step 2) |
| `prompt_optimization` | 提供參考影像時的提示最佳化模式：「standard」提供較高品質，「fast」縮短生成時間。預設值："standard"。 | COMBO | 否 | "standard"<br>"fast" |
| `seed` | 用於生成的種子（seed）。預設值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在影像上加入「AI 生成」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示最佳化推理（「thinking」）以提升指令遵循度。可能會大幅增加生成時間——尤其是 Seedream 5.0 Pro。僅在文字轉影像時可停用（提供參考影像時不可停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### Seedream 5.0 Lite 輸入（seedream 5.0 lite）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議尺寸預設。 | COMBO | 否 | 模型專屬的建議尺寸預設<br>"Custom" |
| `width` | 自訂影像寬度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 6240 (step 2) |
| `height` | 自訂影像高度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 4992 (step 2) |
| `max_images` | 要生成的影像數量上限。設為 1 時，恰好生成一張影像。設為 >1 時，模型會生成 1 到 `max_images` 張相關影像（例如故事場景、角色變化）。總影像數（輸入 + 生成）不得超過 15。預設值：1。 | INT | 否 | 1 to 14 |
| `fail_on_partial` | 若啟用，當任何要求的影像缺失或回傳錯誤時，中止執行。預設值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子（seed）。預設值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在影像上加入「AI 生成」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示最佳化推理（「thinking」）以提升指令遵循度。可能會大幅增加生成時間——尤其是 Seedream 5.0 Pro。僅在文字轉影像時可停用（提供參考影像時不可停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.5 輸入（seedream-4-5-251128）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議尺寸預設。 | COMBO | 否 | 模型專屬的建議尺寸預設<br>"Custom" |
| `width` | 自訂影像寬度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 6240 (step 2) |
| `height` | 自訂影像高度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 4992 (step 2) |
| `max_images` | 要生成的影像數量上限。設為 1 時，恰好生成一張影像。設為 >1 時，模型會生成 1 到 `max_images` 張相關影像（例如故事場景、角色變化）。總影像數（輸入 + 生成）不得超過 15。預設值：1。 | INT | 否 | 1 to 10 |
| `fail_on_partial` | 若啟用，當任何要求的影像缺失或回傳錯誤時，中止執行。預設值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子（seed）。預設值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在影像上加入「AI 生成」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示最佳化推理（「thinking」）以提升指令遵循度。可能會大幅增加生成時間——尤其是 Seedream 5.0 Pro。僅在文字轉影像時可停用（提供參考影像時不可停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.0 輸入（seedream-4-0-250828）

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取 Custom 以使用下方的寬度與高度。預設值：此模型的第一個建議尺寸預設。 | COMBO | 否 | 模型專屬的建議尺寸預設<br>"Custom" |
| `width` | 自訂影像寬度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 6240 (step 2) |
| `height` | 自訂影像高度。僅當 `size_preset` 設為 `Custom` 時此值才生效。預設值：2048。 | INT | 否 | 1024 to 4992 (step 2) |
| `max_images` | 要生成的影像數量上限。設為 1 時，恰好生成一張影像。設為 >1 時，模型會生成 1 到 `max_images` 張相關影像（例如故事場景、角色變化）。總影像數（輸入 + 生成）不得超過 15。預設值：1。 | INT | 否 | 1 to 10 |
| `fail_on_partial` | 若啟用，當任何要求的影像缺失或回傳錯誤時，中止執行。預設值：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子（seed）。預設值：42。 | INT | 否 | 0 to 2147483647 |
| `watermark` | 是否在影像上加入「AI 生成」浮水印。預設值：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示最佳化推理（「thinking」）以提升指令遵循度。可能會大幅增加生成時間——尤其是 Seedream 5.0 Pro。僅在文字轉影像時可停用（提供參考影像時不可停用）。預設值：true。 | BOOLEAN | 否 | true / false |

### 參考輸入

| Parameter | Description | Data Type | Required | Range |
|-----------|-------------|-----------|----------|-------|
| `images` | 可擴充插槽（Growable slot）：用於影像轉影像或多參考影像生成的可選參考影像。可連接 1..N 張影像（例如 `image_1`、`image_2`……）；數量限制依模型而定（見下方注意事項）。若連接的影像包含一批影像，則該批次中的每一張影像都會計入限制。 | IMAGE | 否 | 0 to 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 to 14 (Seedream 5.0 Lite) |

**注意事項：**

- `prompt` 去除前後空白後不得為空。
- 參考影像數量上限：Seedream 5.0 Pro、Seedream 4.5 和 Seedream 4.0 為 10 張；Seedream 5.0 Lite 為 14 張。
- 每張參考影像的長寬比必須介於 1:3 和 3:1 之間。
- 當 `max_images` 大於 1 時（Seedream 5.0 Pro 不支援此選項），參考影像加上生成影像的總數不得超過 15。
- `thinking` 僅可在文字轉影像生成時停用。提供參考影像時，必須啟用 `thinking`。
- `width` 和 `height` 僅在 `size_preset` 設為 "Custom" 時使用。
- `prompt_optimization` 僅適用於 Seedream 5.0 Pro。
- `max_images` 和 `fail_on_partial` 僅適用於 Seedream 5.0 Lite、Seedream 4.5 和 Seedream 4.0；Seedream 5.0 Pro 一律只請求單張影像。
- 解析度要求（寬度 x 高度）：
  - Seedream 5.0 Pro：介於 0.92MP（921,600 像素）與 4.19MP（4,194,304 像素）之間。
  - Seedream 5.0 Lite 和 Seedream 4.5：至少 3.68MP（3,686,400 像素）。
  - Seedream 4.0：至少 0.92MP（921,600 像素）。
  - 所有非 Pro 模型：最多 16.78MP（16,777,216 像素）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成的影像張量。當生成多張影像時，會將其串接成單一批次（batched）的 IMAGE 張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
