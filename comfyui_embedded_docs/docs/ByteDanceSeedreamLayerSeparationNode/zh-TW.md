# ByteDance Seedream 5.0 Pro 圖層分離

ByteDance Seedream 5.0 Pro 圖層分離可將影像分解為一個背景底片，加上最多 16 個透明圖層，每個圖層都有自己的堆疊順序、邊界框、名稱和描述。它會回傳背景、各圖層的影像與遮罩、放置框，以及一個可直接編輯的圖層堆疊。

## 輸入

| 參數 | 說明 | 資料型態 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖片` | 要分離的影像。必須剛好一張影像，至少 512x512 像素，長寬比介於 1:16 和 16:1 之間。大於約 4MP 的輸入會在上傳前縮小。 | IMAGE | 是 | 單一影像 |
| `提示詞` | 如何分離影像。留空將自動偵測並分離所有主要元素。以自然語言描述元素來控制分離，或使用 `<bbox>left top right bottom</bbox>` 標籤（0-1000 千分比座標）指定精確區域。預設：空字串。 | STRING | 是 | 多行文字 |
| `尺寸` | 輸出解析度等級。「auto」會跟隨輸入影像尺寸（限制在 1K-2K 範圍）。預設：「auto」。 | COMBO | 是 | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `種子` | 用於生成的隨機種子。預設：0。 | INT | 是 | 0 至 2147483647 |
| `提示詞優化` | 提示詞最佳化模式：「standard」提供較高品質，「fast」縮短生成時間。預設：「standard」。 | COMBO | 否 | "standard"<br>"fast" |
| `浮水印` | 是否在影像上新增「AI 生成」浮水印。預設：false。 | BOOLEAN | 否 | false<br>true |
| `裁切圖層` | 圖層/遮罩批次輸出的幾何形狀（layer_stack 不受影響，且始終為緊密裁切）。完整畫布：每個圖層位於其邊界框位置的基本尺寸畫布上 - 可直接使用 ImageCompositeMasked 重新合成。最小尺寸：每個圖層裁切至其邊界框（為批次處理填補至最大圖層）- 張量小得多；使用 bboxes 輸出，透過 Layers From Bounding Boxes 重建放置。預設：false（完整畫布）。 | BOOLEAN | 否 | false（完整畫布）<br>true（最小尺寸） |

注意：輸入的 `image` 必須為單一影像；不支援批次。影像必須至少為 512x512 像素，且長寬比介於 1:16 和 16:1 之間。

## 輸出

| 輸出名稱 | 說明 | 資料型態 |
|-------------|-------------|-----------|
| `基底圖片` | 圖層堆疊的基底影像（背景底片）。 | IMAGE |
| `基底遮罩` | 基底影像的透明度（1 = 透明，LoadImage 慣例）；目前一律為完全不透明。 | MASK |
| `圖層` | 透明圖層，由下至上排序。完整畫布模式：放置在黑色基本尺寸畫布上，位於其邊界框位置。最小尺寸模式：裁切至其邊界框，以左上角為基準，填補至最大圖層。 | IMAGE |
| `遮罩` | 每個圖層的透明度，與 layers 批次索引對齊（1 = 透明，LoadImage 慣例）。若要進行 ImageCompositeMasked 風格的合成，請先加入 InvertMask。 | MASK |
| `邊界框` | 每個圖層一個放置框，與 layers 批次索引對齊（將兩者連同 masks 一起饋入 Layers From Bounding Boxes，以重建每個圖層的放置）：`{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`。`content_rect = [left, top, width, height]` 是圖層在其自身框架內的內容區域；它會以框的位置加上該偏移量落在畫布上。 | BOUNDING_BOX |
| `圖層堆疊` | 適用於 Create Layered Image 的可直接編輯圖層文件：包含基底底片，以及每個元素作為獨立具名稱、緊密裁切的圖層，位於其實際位置和堆疊順序。可直接連接，或使用 Add Layer 延伸。 | LAYERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `5062760f2930333f8ed7d8b09dff2492c23fdf906ef71b111348687bef572821`
