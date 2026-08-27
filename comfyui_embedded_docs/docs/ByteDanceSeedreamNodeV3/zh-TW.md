# ByteDanceSeedreamNodeV3

ByteDance Seedream 4.5 與 5.0 可根據文字提示（text-to-image）生成圖片，或在可選參考圖片的引導下生成／編輯圖片，使用 ByteDance Seedream 4.0、4.5 與 5.0 模型，最高可達 4K 解析度。此節點會將提示詞及任何參考圖片傳送至 ByteDance API，等待生成任務完成，並回傳產生的圖片張量或張量集。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 用於建立或編輯圖片的文字提示詞。去除前後空白後不得為空。 | STRING | 是 | Multiline text |
| `模型` | 選擇要使用的 Seedream 模型。每個模型會在下方顯示各自的一組子參數與限制。 | DYNAMIC_COMBO | 是 | "seedream 5.0 pro"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Seedream 5.0 Pro 輸入 (seedream 5.0 pro)

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取「Custom」以使用下方的寬度與高度。預設：此模型的第一個建議預設值。 | COMBO | 否 | 依模型而定的建議尺寸預設值<br>"Custom" |
| `width` | 圖片的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 3136 (step 2) |
| `height` | 圖片的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 2496 (step 2) |
| `prompt_optimization` | 提供參考圖片時的提示詞最佳化模式：'standard' 提供較高品質，'fast' 則縮短生成時間。預設："standard"。 | COMBO | 否 | "standard"<br>"fast" |
| `seed` | 用於生成的種子值。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖片上加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以獲得更好的指令遵循效果。這可能大幅增加生成時間——尤其在 Seedream 5.0 Pro 上。此功能僅可在文字生成圖片模式中停用（當提供參考圖片時不可停用）。預設：true。 | BOOLEAN | 否 | true / false |

### Seedream 5.0 Lite 輸入 (seedream 5.0 lite)

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取「Custom」以使用下方的寬度與高度。預設：此模型的第一個建議預設值。 | COMBO | 否 | 依模型而定的建議尺寸預設值<br>"Custom" |
| `width` | 圖片的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 6240 (step 2) |
| `height` | 圖片的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4992 (step 2) |
| `max_images` | 要生成的圖片數量上限。設為 1 時，只會產生一張圖片。設為 >1 時，模型會生成 1 至 `max_images` 張相關圖片（例如故事場景、角色變化）。圖片總數（輸入 + 生成）不得超過 15。預設：1。 | INT | 否 | 1 至 14 |
| `fail_on_partial` | 若啟用，當任何要求的圖片缺失或回傳錯誤時，會中止執行。預設：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子值。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖片上加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以獲得更好的指令遵循效果。這可能大幅增加生成時間——尤其在 Seedream 5.0 Pro 上。此功能僅可在文字生成圖片模式中停用（當提供參考圖片時不可停用）。預設：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.5 輸入 (seedream-4-5-251128)

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取「Custom」以使用下方的寬度與高度。預設：此模型的第一個建議預設值。 | COMBO | 否 | 依模型而定的建議尺寸預設值<br>"Custom" |
| `width` | 圖片的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 6240 (step 2) |
| `height` | 圖片的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4992 (step 2) |
| `max_images` | 要生成的圖片數量上限。設為 1 時，只會產生一張圖片。設為 >1 時，模型會生成 1 至 `max_images` 張相關圖片（例如故事場景、角色變化）。圖片總數（輸入 + 生成）不得超過 15。預設：1。 | INT | 否 | 1 至 10 |
| `fail_on_partial` | 若啟用，當任何要求的圖片缺失或回傳錯誤時，會中止執行。預設：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子值。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖片上加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以獲得更好的指令遵循效果。這可能大幅增加生成時間——尤其在 Seedream 5.0 Pro 上。此功能僅可在文字生成圖片模式中停用（當提供參考圖片時不可停用）。預設：true。 | BOOLEAN | 否 | true / false |

### Seedream 4.0 輸入 (seedream-4-0-250828)

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `size_preset` | 選擇建議的尺寸。選取「Custom」以使用下方的寬度與高度。預設：此模型的第一個建議預設值。 | COMBO | 否 | 依模型而定的建議尺寸預設值<br>"Custom" |
| `width` | 圖片的自訂寬度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 6240 (step 2) |
| `height` | 圖片的自訂高度。僅當 `size_preset` 設為 `Custom` 時此值才有效。預設：2048。 | INT | 否 | 1024 至 4992 (step 2) |
| `max_images` | 要生成的圖片數量上限。設為 1 時，只會產生一張圖片。設為 >1 時，模型會生成 1 至 `max_images` 張相關圖片（例如故事場景、角色變化）。圖片總數（輸入 + 生成）不得超過 15。預設：1。 | INT | 否 | 1 至 10 |
| `fail_on_partial` | 若啟用，當任何要求的圖片缺失或回傳錯誤時，會中止執行。預設：false。 | BOOLEAN | 否 | true / false |
| `seed` | 用於生成的種子值。預設：42。 | INT | 否 | 0 至 2147483647 |
| `watermark` | 是否在圖片上加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | true / false |
| `thinking` | 啟用模型的提示詞最佳化推理（'thinking'）以獲得更好的指令遵循效果。這可能大幅增加生成時間——尤其在 Seedream 5.0 Pro 上。此功能僅可在文字生成圖片模式中停用（當提供參考圖片時不可停用）。預設：true。 | BOOLEAN | 否 | true / false |

### 參考輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `images` | 可擴充插槽：用於圖生圖（image-to-image）或多參考生成的選用參考圖片。可連接 1..N 張圖片（例如 `image_1`、`image_2`……）；數量限制依模型而定（請參閱下方注意事項）。如果連接的圖片包含一批圖片，批次中的每張圖片都會計入限制。 | IMAGE | 否 | 0 至 10 (Seedream 5.0 Pro, Seedream 4.5, Seedream 4.0)<br>0 至 14 (Seedream 5.0 Lite) |

**注意事項：**

- `prompt` 去除前後空白後不得為空。
- 參考圖片數量上限：Seedream 5.0 Pro、Seedream 4.5 與 Seedream 4.0 為 10 張；Seedream 5.0 Lite 為 14 張。
- 每張參考圖片的長寬比必須介於 1:3 與 3:1 之間。
- 當 `max_images` 大於 1 時（Seedream 5.0 Pro 不提供此功能），參考圖片加上生成圖片的總數不得超過 15。
- `thinking` 僅可在文字生成圖片的模式中停用。當提供參考圖片時，`thinking` 必須啟用。
- `width` 與 `height` 僅在 `size_preset` 設為 "Custom" 時才會使用。
- `prompt_optimization` 僅適用於 Seedream 5.0 Pro。
- `max_images` 與 `fail_on_partial` 僅適用於 Seedream 5.0 Lite、Seedream 4.5 與 Seedream 4.0；Seedream 5.0 Pro 一律只要求生成單張圖片。
- 解析度要求（寬 x 高）：
  - Seedream 5.0 Pro：介於 0.92MP（921,600 像素）與 4.19MP（4,194,304 像素）之間。
  - Seedream 5.0 Lite 與 Seedream 4.5：至少 3.68MP（3,686,400 像素）。
  - Seedream 4.0：至少 0.92MP（921,600 像素）。
  - 所有非 Pro 型號：最多 16.78MP（16,777,216 像素）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 生成的圖片張量。當生成多張圖片時，會將其串接為單一批次的 IMAGE 張量。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/zh-TW.md)

---
**Source fingerprint (SHA-256):** `68dd23afdb5720491cef784b22ad66ff0baf80984ea652ea4c13e6c264c029ac`
