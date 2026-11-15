# Split Image Channels

將影像拆分為紅色、綠色與藍色通道，並將 Alpha 通道作為遮罩傳回。每個顏色輸出都是三通道灰階影像，因此能像一般影像一樣預覽與儲存。可用於檢視或編輯單一通道，或從帶有 Alpha 通道的影像中取出透明度：使用 Load Image 載入的影像沒有 Alpha 通道，因為其 Alpha 會作為獨立的 `MASK` 輸出提供。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `image` | 要拆分的影像。單通道（灰階）輸入會被擴展，使三個顏色輸出都攜帶相同的資料。 | IMAGE | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| red | 紅色通道，為三通道灰階影像。 | IMAGE |
| green | 綠色通道，為三通道灰階影像。 | IMAGE |
| blue | 藍色通道，為三通道灰階影像。 | IMAGE |
| alpha | Alpha 作為遮罩，反轉方式與 Load Image 相同，因此 1 表示完全透明的像素。沒有 Alpha 通道的影像會傳回全零遮罩。 | MASK |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageChannels/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0f300d2e86c74e856001eb82da26c871c94c1dae5ec73a4504ca258420fbcf52`
