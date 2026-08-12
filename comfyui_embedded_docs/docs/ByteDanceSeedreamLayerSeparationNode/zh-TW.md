# ByteDanceSeedreamLayerSeparationNode

ByteDance Seedream 5.0 Pro 圖層分離會將影像分解為一個背景圖層以及最多 16 個透明圖層，每個圖層都有自己的堆疊順序、邊界框、名稱和描述。它會回傳背景、各圖層影像與遮罩、放置方框，以及可直接編輯的圖層堆疊。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要分離的影像。必須是單一影像，至少 512x512 像素，長寬比介於 1:16 和 16:1 之間。大於約 4MP 的輸入會在上傳前縮小。 | IMAGE | 是 | 單一影像 |
| `prompt` | 影像分離的方式。留空則自動偵測並分離所有主要元素。以自然語言描述元素來控制分離，或使用 `<bbox>left top right bottom</bbox>` 標記（0-1000 千分比座標）鎖定特定區域。預設值：空字串。 | STRING | 是 | 多行文字 |
| `size` | 輸出解析度等級。"auto" 會跟隨輸入影像尺寸（限制在 1K-2K 範圍內）。預設值："auto"。 | STRING | 是 | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | 用於生成隨機種子。預設值：0。 | INT | 是 | 0 到 2147483647 |
| `prompt_optimization` | 提示詞最佳化模式："standard" 提供較高品質，"fast" 縮短生成時間。預設值："standard"。 | STRING | 否 | "standard"<br>"fast" |
| `watermark` | 是否在影像上加入「AI 生成」浮水印。預設值：false。 | BOOLEAN | 否 | false<br>true |
| `crop_layers` | 圖層/遮罩批次輸出的幾何形狀（layer_stack 不受影響，永遠是緊密裁切）。完整畫布：每個圖層位於基底尺寸畫布上其邊界框位置——可直接使用 ImageCompositeMasked 重新合成。最小尺寸：每個圖層裁切至其邊界框（為了批次統一而補邊至最大圖層）——張量小得多；使用 Layers From Bounding Boxes 搭配 bboxes 輸出重建放置。預設值：false（完整畫布）。 | BOOLEAN | 否 | false (full canvas)<br>true (minimal size) |

注意：輸入影像必須是單一影像；不支援批次。影像至少需為 512x512 像素，且長寬比介於 1:16 和 16:1 之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `base_image` | 圖層堆疊所在的基底影像（背景圖層）。 | IMAGE |
| `base_mask` | 基底影像的透明度（1 = 透明，採用 LoadImage 慣例）；目前永遠是完全不透明。 | MASK |
| `layers` | 由下到上排序的透明圖層。完整畫布模式：放置在黑色基底尺寸畫布上的邊界框位置。最小尺寸模式：裁切至其邊界框，錨定於左上角，並補邊至最大圖層。 | IMAGE |
| `masks` | 每個圖層的透明度，與 layers 批次索引對齊（1 = 透明，採用 LoadImage 慣例）。若要使用 ImageCompositeMasked 風格合成，請先加入 InvertMask。 | MASK |
| `bboxes` | 每個圖層的放置方框，與 layers 批次索引對齊（將兩者及 masks 一起送入 Layers From Bounding Boxes 以重建每個圖層的放置）：`{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`。`content_rect = [left, top, width, height]` 是圖層在其自身框架內的內容區域；它會落在畫布上，位置為方框座標加上該偏移量。 | BOUNDING_BOX |
| `layer_stack` | 可供 Create Layered Image 直接編輯的圖層文件：基底圖層加上每個元素作為獨立、具名稱、緊密裁切的圖層，位於其真實位置與堆疊順序。可直接連接，或使用 Add Layer 擴充。 | LAYERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `059d0a1a5f5793aadda72f50b549b8b10e2ecae3ce003f82c0c28191c3460954`
