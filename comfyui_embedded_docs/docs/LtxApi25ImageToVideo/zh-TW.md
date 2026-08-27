# LtxApi25ImageToVideo

此節點根據起始圖片生成專業品質的影片。您可以選擇 LTX 2.5 模型變體、用文字提示描述影片、調整時長、解析度、幀率和音訊生成，並可選擇提供最終幀。輸出為從提供的圖片開始的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 用於影片的第一幀。 | IMAGE | 是 | Exactly one image |
| `模型` | 模型設定群組。選擇要使用的 LTX 2.5 模型變體。 | COMBO | 是 | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `時長` | 生成影片的長度（以秒為單位）。 | INT | 是 | Integer |
| `解析度` | 生成影片的解析度。可用選項可能取決於所選模型。 | COMBO | 是 | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `幀率` | 生成影片的幀率。 | INT | 是 | Integer (default: 25) |
| `生成音訊` | 是否為影片生成音訊。 | BOOLEAN | 是 | True<br>False |
| `提示詞` | 要生成的影片內容的文字描述。必須介於 1 到 10000 個字元之間。 | STRING | 是 | 1 至 10000 characters |
| `種子` | 用於可重現生成的種子值。使用相同的種子和設定會產生相同的結果。 | INT | 是 | Integer (default: 42) |
| `最後幀` | 用於影片的最終幀。 | IMAGE | 否 | Exactly one image |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 根據提供的起始圖片和生成設定所生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
