# ByteDance Seedream 5.0 Layer Separation

ByteDance Seedream 5.0 Layer Separation 會將一張影像分解成一個背景底圖，以及最多 16 個可重新定位的透明圖層；每個圖層都包含堆疊順序、邊界框、名稱與描述。它會回傳背景、帶遮罩的各圖層影像、放置框，以及可直接編輯的圖層堆疊。`model` 選擇器可在 Seedream 5.0 Pro 與更快速的 Seedream 5.0 Flash 之間選擇。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於分離的 Seedream 模型。"seedream 5.0 pro"（預設）可提供最高的分離品質，並且會額外提供 `prompt_optimization` 控制項；"seedream 5.0 flash" 則更快速、成本更低，且沒有提示詞最佳化控制項。 | DYNAMIC_COMBO | 是 | "seedream 5.0 pro"<br>"seedream 5.0 flash" |

### Seedream 5.0 Pro 與 5.0 Flash 輸入

這些輸入在兩個模型中都可用。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要進行分離的影像。必須恰好一張影像，至少 512x512 像素，長寬比介於 1:16 與 16:1 之間。大於約 4MP 的輸入會在上傳前先縮小。 | IMAGE | 是 | 單張圖像 |
| `prompt` | 如何分離影像。留空可自動偵測並分離所有主要元素。以自然語言描述元素來控制分離結果，或使用 `<bbox>left top right bottom</bbox>` 標籤指定精確區域（0-1000 千分比座標）。預設值：空字串。 | STRING | 是 | 多行文字 |
| `size` | 輸出解析度等級。"auto" 會跟隨輸入影像尺寸（限制在 1K-2K 範圍內）。預設值："auto"。 | COMBO | 是 | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | 用於生成的種子。預設值：42。 | INT | 是 | 0 至 2147483647 |
| `watermark` | 是否在影像上加入 "AI generated" 浮水印。預設值：false。 | BOOLEAN | 是 | false<br>true |
| `crop_layers` | 圖層/遮罩批次輸出的幾何配置（`layer_stack` 不受影響，且一律保持緊密裁切）。完整畫布：每個圖層位於其邊界框位置的基礎尺寸畫布上——可直接使用 ImageCompositeMasked 重新合成。最小尺寸：每個圖層裁切至其邊界框（為了批次處理而填充至最大圖層）——張量小得多；使用 `bboxes` 輸出，透過 Layers From Bounding Boxes 重建放置位置。預設值：false（完整畫布）。 | BOOLEAN | 是 | false（完整畫布）<br>true（最小尺寸） |

### 僅限 Seedream 5.0 Pro 的輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt_optimization` | 提示詞最佳化模式："standard" 可提供更高品質，"fast" 則縮短生成時間。僅適用於 Seedream 5.0 Pro。預設值："standard"。 | COMBO | 是 | "standard"<br>"fast" |

**注意：** 輸入 `image` 必須是單一影像；不支援批次。影像必須至少 512x512 像素，且長寬比介於 1:16 與 16:1 之間。Seedream 5.0 Flash 一律使用標準提示詞最佳化。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `base_image` | 圖層堆疊所依據的基礎影像（背景底圖）。 | IMAGE |
| `base_mask` | 基礎影像的透明度（1 = 透明，LoadImage 慣例）；目前一律為完全不透明。 | MASK |
| `layers` | 由下到上排序的透明圖層。完整畫布模式：置於黑色、與基礎影像同尺寸的畫布上，並位於其邊界框位置。最小尺寸模式：裁切至其邊界框，錨定於左上角，並填充至最大圖層尺寸。 | IMAGE |
| `masks` | 各圖層的透明度，索引與 `layers` 批次對齊（1 = 透明，LoadImage 慣例）。若要進行 ImageCompositeMasked 類型的合成，請先加上 InvertMask。 | MASK |
| `bboxes` | 每個圖層一個放置框，索引與 `layers` 批次對齊（將 `bboxes` 與 `layers`，再加上 `masks`，饋入 Layers From Bounding Boxes，即可重建各圖層的放置位置）：`{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`。`content_rect = [left, top, width, height]` 是該圖層在其自身框架內的內容區域；它會落在畫布上，位置為放置框位置加上該偏移量。 | BOUNDING_BOX |
| `layer_stack` | 可直接編輯的圖層文件，供 Create Layered Image 使用：包含基礎底圖，以及每個元素各自作為具名、緊密裁切的圖層，並位於其真實位置與堆疊順序。可直接連接，或使用 Add Layer 擴充。 | LAYERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNodeV2/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b106ca63d37aea68079f0032a1f7dfeefee9f759c71bb1605bbfe66c3d9dad62`
