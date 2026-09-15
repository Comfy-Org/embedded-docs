# 取得影片元件

`Get Video Components` 節點會從視訊檔案中擷取所有主要元素。它會將視訊拆分為個別影格、擷取音訊軌，並提供視訊的影格率、位元深度和色彩空間。這讓您可以獨立處理每個元件，以進行後續處理或分析。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影片` | 要從中擷取元件的視訊。 | VIDEO | 是 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `images` | 從視訊中擷取出的個別影格，作為獨立影像。 | IMAGE |
| `audio` | 從視訊中擷取出的音訊軌。 | AUDIO |
| `fps` | 視訊的影格率，以每秒影格數表示。 | FLOAT |
| `bit_depth` | 視訊的位元深度。 | COMBO |
| `color_space` | 視訊的色彩空間。 | COMBO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetVideoComponents/zh-TW.md)

---
**Source fingerprint (SHA-256):** `b57dbf1120105885d17361f07ec96c078aac9ae9a84beb63319885df679e4f81`
