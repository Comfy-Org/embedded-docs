# 取得影片元件

Get Video Components 節點會從影片檔案中提取所有主要元件。它將影片分離為個別影格、提取音訊軌道，並提供影片的幀率、位元深度和色彩空間資訊。這讓您能夠獨立處理每個元件，進行進一步的處理或分析。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要從中提取元件的影片。 | VIDEO | 是 | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `影像` | 從影片中提取的個別影格，作為獨立影像。 | IMAGE |
| `音訊` | 從影片中提取的音訊軌道。 | AUDIO |
| `每秒影格數` | 影片的幀率（每秒影格數）。 | FLOAT |
| `bit_depth` | 影片的位元深度。 | COMBO |
| `color_space` | 影片的色彩空間。 | COMBO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`
