# LayersFromBoundingBoxes

此節點將影像批次及其邊界框轉換為圖層堆疊，為每個影格建立一個圖層，並根據對應的框放置每個圖層。當某個節點以批次形式輸出圖層時，請使用此節點，因為批次僅為每個影格攜帶單一放置資訊，否則個別位置會遺失。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 影像批次；每個影格會成為一個圖層。 | IMAGE | 是 | — |
| `bboxes` | 放置框，與影像批次索引對齊。接受邊界框（x, y, width, height）、正規化元素（帶有 "bbox" —— 這些需要 canvas_width/canvas_height 才能解析為像素），或任一形式的 JSON 字串。沒有匹配框的影格會被放置在原點。框的 width/height 會縮放圖層以符合該框。存在 metadata.name（或 desc）與 metadata.z_index 時會使用這些值，而 metadata.content_rect（相對於影格）會將影格裁切至其實際內容。 | BOUNDING_BOX、ARRAY 或 STRING | 是 | — |
| `mask` | 逐幀透明度，與影像批次索引對齊（1 = 透明，LoadImage 慣例）。 | MASK | 否 | — |
| `layers` | 要附加到的圖層堆疊。保持未連接以建立新的堆疊。 | LAYERS | 否 | — |
| `crop_to_content` | 若存在 metadata.content_rect，將每個影格裁切至該範圍，並將內容放置在框位置加上矩形偏移處。對於影格具有填補（padded）的批次，請保持啟用——這樣只會將真實內容保留在其實際位置。（預設值：true） | BOOLEAN | 否 | true<br>false |
| `canvas_width` | 文件畫布寬度。0 表示從已放置的圖層推導。（預設值：0） | INT | 否 | 0 至 MAX_RESOLUTION |
| `canvas_height` | 文件畫布高度。0 表示從已放置的圖層推導。（預設值：0） | INT | 否 | 0 至 MAX_RESOLUTION |

注意事項：

- `bboxes` 與 `mask` 必須與 `image` 索引對齊：第 n 個框與第 n 個遮罩幀對應第 n 個影像幀。沒有匹配框的影格會被放置在原點。
- 當 `bboxes` 包含正規化元素（帶有 "bbox"）時，必須提供 `canvas_width` 和 `canvas_height`，以便將這些正規化位置解析為像素。
- 若要明確設定文件畫布，`canvas_width` 和 `canvas_height` 都必須大於 0。若任一值為 0，畫布會從已放置的圖層推導，或從已連接的 `layers` 堆疊繼承。
- 當 `layers` 已連接時，新圖層會被附加到其中，並取得堆疊中既有最高 z-index 以上的值。
- 當啟用 `crop_to_content` 且影格帶有 metadata.content_rect 時，該影格會被裁切至該矩形，且不套用框的寬度/高度縮放；而是將矩形的偏移加到框位置。

## 輸出
| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `LAYERS` | 圖層堆疊，準備用於 Create Layered Image。 | LAYERS |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LayersFromBoundingBoxes/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a70956bf0d7ea8bdbd16767ed8b19600b274a6eeb745728f95219578adc73712`
