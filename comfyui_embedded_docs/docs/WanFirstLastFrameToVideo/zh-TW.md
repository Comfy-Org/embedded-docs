> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/zh-TW.md)

WanFirstLastFrameToVideo 節點透過結合起始與結束影格及文字提示來建立影片條件設定。它透過編碼第一個和最後一個影格、應用遮罩來引導生成過程，並在可用時整合 CLIP 視覺特徵，從而為影片生成產生潛在表徵。此節點為影片模型準備正面和負面條件設定，以在指定的起點和終點之間生成連貫的序列。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `正向` | CONDITIONING | 是 | - | 用於引導影片生成的正面文字條件設定 |
| `負向` | CONDITIONING | 是 | - | 用於引導影片生成的負面文字條件設定 |
| `vae` | VAE | 是 | - | 用於將影像編碼至潛在空間的 VAE 模型 |
| `寬度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片寬度（預設值：832，步長：16） |
| `高度` | INT | 是 | 16 至 MAX_RESOLUTION | 輸出影片高度（預設值：480，步長：16） |
| `長度` | INT | 是 | 1 至 MAX_RESOLUTION | 影片序列中的影格數量（預設值：81，步長：4） |
| `批次大小` | INT | 是 | 1 至 4096 | 同時生成的影片數量（預設值：1） |
| `clip 視覺起始影像` | CLIP_VISION_OUTPUT | 否 | - | 從起始影像提取的 CLIP 視覺特徵 |
| `clip 視覺結束影像` | CLIP_VISION_OUTPUT | 否 | - | 從結束影像提取的 CLIP 視覺特徵 |
| `起始影像` | IMAGE | 否 | - | 影片序列的起始影格影像 |
| `結束影像` | IMAGE | 否 | - | 影片序列的結束影格影像 |

**注意：** 當同時提供 `start_image` 和 `end_image` 時，此節點會建立一個在這兩個影格之間過渡的影片序列。`clip_vision_start_image` 和 `clip_vision_end_image` 參數為選用，但若提供，其 CLIP 視覺特徵將被串聯並應用於正面和負面條件設定。`start_image` 會被裁切至前 `length` 個影格，而 `end_image` 則在處理前被裁切至最後 `length` 個影格。

## 輸出

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `負向` | CONDITIONING | 已套用影片影格編碼和 CLIP 視覺特徵的正面條件設定 |
| `潛在空間` | CONDITIONING | 已套用影片影格編碼和 CLIP 視覺特徵的負面條件設定 |
| `latent` | LATENT | 空白的潛在張量，其維度與指定的影片參數相符 |

---
**Source fingerprint (SHA-256):** `8cfca692fc4975bb5238ce749d2102fad4b6cd84e96ef74c3eff2b297ee60c3c`
