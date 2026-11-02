# Pruna P-Video Upscale

Pruna P-Video Upscale 可將影片放大至 720p、1080p、2K 或 4K，同時保留其長寬比與音軌。影片片段會傳送至 Pruna，接著輪詢預測結果，最後回傳放大後的影片。若來源本身的尺寸已達到或超過目標尺寸，則會維持原有尺寸，僅進行畫質增強。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `video` | 要放大的影片，最大 512 MiB。超過 1000 萬像素的影片僅能傳送至 2K 或 4K 目標。 | VIDEO | 是 | 最高 512 MiB |
| `target` | 輸出像素面積：720p 約為 0.9 百萬像素，1080p 為 2.1，2K 為 3.7，4K 為 8.3。影片長度上限受目標限制：分別為 2400、1200、600 或 300 幀，在 24 fps 下約為 100、50、25 或 12.5 秒（預設值："1080p"）。 | COMBO | 是 | "720p"<br>"1080p"<br>"2K"<br>"4K" |
| `fps` | 輸出影格率（預設值："source"）。"source" 會保留影片原有的影格率，最高 60；更高的影格率則以插值方式產生。輸出高於 30 fps 的費用為兩倍。 | COMBO | 是 | "source"<br>"16"<br>"24"<br>"25"<br>"30"<br>"48"<br>"50"<br>"60" |
| `turbo` | 更快速的放大，細節較為柔和，價格相同（預設值：false）。 | BOOLEAN | 否 | true<br>false |

### 參數限制

- 影片片段必須為 512 MiB 或更小，此限制以重新編碼為 H.264 MP4 後的大小為準。
- 影格上限以最高 30 fps 計算：720p 為 2400 幀、1080p 為 1200 幀、2K 為 600 幀、4K 為 300 幀。較長的影片片段需要較低的目標、較低的 `fps`，或更短的剪輯長度。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 放大後的影片，附帶原始音訊。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaPVideoUpscaleNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e8fc88b6177085e0852d17ff92b0a22a26c9914c012a9a244b19da9b2c0e38c2`
