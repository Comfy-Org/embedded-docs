# Flux 影片放大（舊版）

Flux Video Upscale 使用 FLUX 超解析度將影片片段放大 1.5 到 3 倍。在 creative 模式下，它會還原並創造精細細節；在 precise 模式下，它會銳化來源而不改變它。

**注意：** 此節點在原始碼中標記為已棄用。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `video` | 長度 1 到 20 秒、長寬比介於 1:4 與 4:1 之間的來源片段。輸出以 24 fps 渲染，且每幀上限約為 14.4 百萬像素。 | VIDEO | 是 | 1 至 20 seconds duration; aspect ratio between 1:4 and 4:1; minimum 64x64 pixels |
| `upscale_factor` | 相對於來源的輸出尺寸。由於每幀上限，非常大的來源會以低於所要求倍率的幅度放大。（預設：2.0） | FLOAT | 是 | 1.5 至 3.0 （步進值：0.1） |
| `mode` | 'creative' 會還原並創造精細細節，最適合生成式素材、紋理和風景。'precise' 會銳化來源而不改變它，適用於臉部、產品和真實影片素材。（預設："creative"） | COMBO | 是 | "creative"<br>"precise" |
| `prompt` | 選填的片段描述，用來引導增強的細節。留空則進行中性放大。（預設：空） | STRING | 是 | Multiline text |
| `auto_downscale` | 自動將面積大於 2560x1440 像素的來源縮小，以符合輸入限制。長寬比會保留；較小的影片不受影響。（預設：true） | BOOLEAN | 是 | true<br>false |
| `safety_tolerance` | 審核容忍度，0 最嚴格。（預設：2，進階參數） | INT | 是 | 0 至 4 |
| `seed` | 用來判斷節點是否應重新執行的種子；FLUX 會自行選擇種子，因此無論此值為何，實際結果都是不確定的。（預設：42） | INT | 是 | 0 至 4294967295 |

注意：來源影片長度必須介於 1 到 20 秒之間，尺寸至少 64x64 像素，且長寬比介於 1:4 與 4:1 之間。若停用 `auto_downscale` 且影片面積超過 2560x1440 像素，節點會引發錯誤。輸出影片以 24 fps 渲染，且每幀上限約為 14.4 百萬像素，因此非常大的來源可能以低於所要求倍率的幅度放大。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 放大後的影片片段。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVideoUpscaleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2eeac17c04b4a2cde76a7e0d58b42ba5622cc22119b7ddc3c730463b2eb5d8c1`
