# 取得影片元件

Get Video Components 節點會從影片檔案中擷取所有主要元素。它將影片分離為單獨的幀、擷取音訊軌，並提供影片的幀率、位元深度和色彩空間資訊。這讓您可以獨立處理每個元件，以進行進一步的處理或分析。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要從中擷取元件的影片。 | VIDEO | 是 | - |

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `影像` | 從影片中擷取為單獨影像的各個幀。 | IMAGE |
| `音訊` | 從影片中擷取的音訊軌。 | AUDIO |
| `每秒影格數` | 影片的幀率（每秒幀數）。 | FLOAT |
| `bit_depth` | 影片的位元深度。 | INT |
| `color_space` | 影片的色彩空間。 | COMBO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/zh-TW.md)

---
**Source fingerprint (SHA-256):** `ffe8b6c698cb9a855b8796768f068d403448cf56188ce4c5ead21bff30baff6e`
