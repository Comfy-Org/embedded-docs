# ByteDance Seedream 5.0 Pro 圖層分離

ByteDance Seedream 5.0 Pro Layer Separation 會將影像分解為一個背景底板，以及最多 16 個可重新定位的透明圖層；每個圖層都有堆疊順序、邊界框、名稱與描述。它會傳回背景、帶遮罩的各圖層影像、放置框，以及可直接編輯的圖層堆疊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖片` | 要分離的影像。僅限一張影像，至少 512x512 像素，長寬比介於 1:16 與 16:1 之間。大約超過 4MP 的輸入會在的上傳前被縮小。 | IMAGE | 是 | Single image |
| `提示詞` | 如何分離影像。留空以自動偵測並分離所有主要元素。以自然語言描述元素以控制分離，或使用 `<bbox>left top right bottom</bbox>` 標籤指定精確區域（0-1000 千分比座標）。預設：空字串。 | STRING | 是 | Multiline text |
| `尺寸` | 輸出解析度等級。"auto" 會跟隨輸入影像大小（限制在 1K-2K 範圍內）。預設："auto"。 | COMBO | 是 | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `種子` | 生成時使用的種子。預設：0。 | INT | 是 | 0 至 2147483647 |
| `提示詞優化` | 提示詞最佳化模式："standard" 提供較高品質，"fast" 縮短生成時間。預設："standard"。 | COMBO | 否 | "standard"<br>"fast" |
| `浮水印` | 是否在影像中加入「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | false<br>true |
| `裁切圖層` | `layers`/`masks` 批次輸出的幾何形式（`layer_stack` 不受影響，且一律為緊密裁切）。完整畫布：每個圖層位於與基礎影像同尺寸的畫布上，並置於其邊界框位置——可直接搭配 ImageCompositeMasked 重新合成。最小尺寸：每個圖層裁切至其邊界框（為批次處理而補齊至最大圖層）——張量小得多；使用 bboxes 輸出，透過 Layers From Bounding Boxes 重建放置位置。預設：false（完整畫布）。 | BOOLEAN | 否 | false (full canvas)<br>true (minimal size) |

注意：輸入 `image` 必須是單一影像；不支援批次。影像必須至少 512x512 像素，且長寬比介於 1:16 與 16:1 之間。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `base_image` | 圖層堆疊其上的基礎影像（背景底板）。 | IMAGE |
| `base_mask` | 基礎影像的透明度（1 = 透明，LoadImage 慣例）；目前一律為完全不透明。 | MASK |
| `layers` | 透明圖層，依由下到上排序。完整畫布模式：置於黑色且與基礎影像同尺寸的畫布上，並位於其邊界框位置。最小尺寸模式：裁切至其邊界框、錨定於左上角，並補齊至最大圖層。 | IMAGE |
| `masks` | 各圖層的透明度，索引對齊 layers 批次（1 = 透明，LoadImage 慣例）。若要進行 ImageCompositeMasked 風格的合成，請先加入 InvertMask。 | MASK |
| `bboxes` | 每個圖層一個放置框，索引對齊 layers 批次（將兩者加上 masks 一起饋入 Layers From Bounding Boxes，以重建各圖層放置位置）：`{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`。`content_rect = [left, top, width, height]` 是圖層在其自身框架內的內容區域；它會落在畫布上，位置為框位置加上該偏移量。 | BOUNDING_BOX |
| `layer_stack` | 可直接編輯的圖層文件，用於 Create Layered Image：基礎底板加上每個元素作為各自具名、緊密裁切的圖層，並位於其真實位置與堆疊順序。可直接連接，或使用 Add Layer 擴充。 | LAYERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
