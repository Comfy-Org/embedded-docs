# Video Deflicker

此節點可移除處理過影片中的時間性閃爍，使每一幀在跟隨鄰近幀運動的同時，仍保有自己的細節。它適用於在放大或逐幀處理後出現脈動現象的影片：連接光流模型與閃爍的影格，並可選擇性地連接來源的穩定副本作為引導。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | Range |
| --- | --- | --- | --- | --- |
| `optical_flow` | 來自 Load Optical Flow Model 節點的光流模型（torchvision RAFT-large）。 | OPTICAL_FLOW | 是 | - |
| `影像` | 需要穩定的閃爍影格，例如經過放大或逐幀處理的影片。 | IMAGE | 是 | - |
| `引導` | 任意解析度的穩定來源影格，用於跟隨其運動。預設為 `images`，此時移除的閃爍較少。其運動補償後的影格差異也參與平滑權重：當 `guide` 的變化無法由估計的運動解釋時，即使運動估計正確，平滑也會減弱。 | IMAGE | 否 | - |
| `強度` | 每一幀跟隨其鄰近幀的程度（預設：1.0）。數值越高，移除的閃爍越多，但也會使更多細節變得柔和；0 會回傳未經改變的影格。 | FLOAT | 是 | 0.0 至 100.0（步進值：0.1） |
| `方向` | 處理方向。`bidirectional` 會平均前向與後向的處理結果，可避免落後於運動；`forward` 僅執行單次處理。（預設：`bidirectional`） | COMBO | 是 | `"bidirectional"`<br>`"forward"` |
| `閾值` | 某一幀與其經運動補償的鄰近幀之間大於此值的變化，會被視為真實變化而較少被平滑（預設：0.1）。0 會對所有變化一視同仁地平滑。 | FLOAT | 是 | 0.0 至 1.0（步進值：0.01） |

**附註：**

- 光流在 `guide` 的縮小副本上計算，因此不必與 `images` 同尺寸；`guide` 的像素不會混入輸出。
- 超出 `images` 與 `guide` 中較短者的影格不會被去閃爍。`guide` 較短時，其餘影格原樣回傳。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 去閃爍後的影格，尺寸與影格數皆與 `images` 相同。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoDeflicker/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d9937a67b0ac33ef3b326017e7d7990474705917902f1097cfeb06d9f83322a1`
