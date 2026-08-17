# ByteDance Seedream 5.0 Pro 圖層分離

ByteDance Seedream 5.0 Pro Layer Separation 將圖片分解為一個背景圖層，加上最多 16 個透明圖層，每個圖層都有自己的堆疊順序、邊界框、名稱與描述。它會傳回背景、各圖層的影像與遮罩、放置方框，以及可直接編輯的圖層堆疊。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要分離的圖片。必須是單一張圖片，至少 512x512 像素，長寬比介於 1:16 與 16:1 之間。若輸入超過約 4MP，上傳前會先縮小。 | IMAGE | 是 | Single image |
| `prompt` | 如何分離圖片。留空以自動偵測並分離所有主要元素。使用自然語言描述元素以控制分離，或使用 `<bbox>left top right bottom</bbox>` 標籤指定確切區域（0-1000 千分比座標）。預設為空字串。 | STRING | 是 | Multiline text |
| `size` | 輸出解析度等級。「auto」會依循輸入圖片尺寸（限制在 1K-2K 範圍內）。預設：「auto」。 | COMBO | 是 | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | 用於生成所使用的種子。預設：0。 | INT | 是 | 0 to 2147483647 |
| `prompt_optimization` | 提示詞最佳化模式：「standard」提供較高品質，「fast」縮短生成時間。預設：「standard」。 | COMBO | 否 | "standard"<br>"fast" |
| `watermark` | 是否在圖片上添加「AI generated」浮水印。預設：false。 | BOOLEAN | 否 | false<br>true |
| `crop_layers` | 圖層/遮罩批次輸出的幾何形狀（layer_stack 不受影響，且永遠是緊密裁切）。完整畫布：每個圖層在其邊界框位置上放置於基礎尺寸畫布上——可直接使用 ImageCompositeMasked 重新合成。最小尺寸：每個圖層裁切至其邊界框（為批次處理而填補至最大圖層）——張量小得多；使用 bboxes 輸出，透過 Layers From Bounding Boxes 重建放置位置。預設：false（完整畫布）。 | BOOLEAN | 否 | false (full canvas)<br>true (minimal size) |

注意：輸入圖片必須是單一張圖片；不支援批次。圖片必須至少 512x512 像素，長寬比介於 1:16 與 16:1 之間。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `base_image` | 圖層堆疊於其上的基礎圖片（背景圖層）。 | IMAGE |
| `base_mask` | 基礎圖片的透明度（1 = 透明，遵循 LoadImage 慣例）；目前永遠是完全不透明。 | MASK |
| `layers` | 透明圖層，依由下至上的順序排列。完整畫布模式：以基礎尺寸黑色畫布放置在各自邊界框位置。最小尺寸模式：裁切至其邊界框，以左上角為錨點，並填補至最大圖層。 | IMAGE |
| `masks` | 每個圖層的透明度，與 layers 批次索引對齊（1 = 透明，遵循 LoadImage 慣例）。若要進行 ImageCompositeMasked 風格的合成，請先加入 InvertMask。 | MASK |
| `bboxes` | 每個圖層一個放置框，與 layers 批次索引對齊（將兩者及 masks 輸入 Layers From Bounding Boxes，以重建每個圖層的放置位置）：`{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`。`content_rect = [left, top, width, height]` 是圖層在其自身影格內的內容區域；其會以該框位置加上該偏移量落在畫布上。 | BOUNDING_BOX |
| `layer_stack` | 可供 Create Layered Image 直接編輯的圖層文件：包含基礎圖板，以及每個元素以自己名稱、緊密裁切圖層形式，位於其真實位置與堆疊順序。可直接連接，或使用 Add Layer 擴充。 | LAYERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
