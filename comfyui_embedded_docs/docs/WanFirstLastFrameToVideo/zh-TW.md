# Wan 首尾影格轉影片

The WanFirstLastFrameToVideo 節點透過結合起始幀與結束幀以及文字提示來建立影片條件化。它透過編碼第一幀和最後一幀、套用遮罩以引導生成過程，並在可用時納入 CLIP 視覺特徵，為影片生成建立潛在表示。此節點為影片模型準備正向與負向條件化，以在指定的起點與終點之間生成連貫的序列。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | Range |
| --- | --- | --- | --- | --- |
| `positive` | 用於引導影片生成的正向文字條件化 | CONDITIONING | 是 | - |
| `negative` | 用於引導影片生成的負向文字條件化 | CONDITIONING | 是 | - |
| `vae` | 用於將影像編碼至潛在空間的 VAE 模型 | VAE | 是 | - |
| `width` | 輸出影片寬度（預設：832，步進：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `height` | 輸出影片高度（預設：480，步進：16） | INT | 是 | 16 to MAX_RESOLUTION |
| `length` | 影片序列中的幀數（預設：81，步進：4） | INT | 是 | 1 to MAX_RESOLUTION |
| `batch_size` | 同時生成的影片數量（預設：1） | INT | 是 | 1 to 4096 |
| `clip_vision_start_image` | 從起始影像提取的 CLIP 視覺特徵 | CLIP_VISION_OUTPUT | 否 | - |
| `clip_vision_end_image` | 從結束影像提取的 CLIP 視覺特徵 | CLIP_VISION_OUTPUT | 否 | - |
| `start_image` | 影片序列的起始幀影像 | IMAGE | 否 | - |
| `end_image` | 影片序列的結束幀影像 | IMAGE | 否 | - |

**注意：** 當同時提供 `start_image` 與 `end_image` 時，節點會建立在此兩個幀之間轉場的影片序列。處理前，`start_image` 會被裁剪為前 `length` 幀，`end_image` 則被裁剪為後 `length` 幀。如果只提供其中一個，缺少的一側會以中性灰色幀填補。遮罩會在起始幀與結束幀存在的區域設為 0，其餘區域設為 1。`clip_vision_start_image` 與 `clip_vision_end_image` 參數為選用；當兩者都提供時，其 CLIP 視覺特徵會被串接並套用至正向與負向條件化。若僅提供其中一個，則單獨使用其特徵。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `positive` | 已套用影片幀編碼與 CLIP 視覺特徵的正向條件化 | CONDITIONING |
| `negative` | 已套用影片幀編碼與 CLIP 視覺特徵的負向條件化 | CONDITIONING |
| `latent` | 具有與指定影片參數相符維度的空潛在張量 | LATENT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
