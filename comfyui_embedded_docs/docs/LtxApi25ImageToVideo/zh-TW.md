# LTX 2.5 圖像轉影片

此節點使用 LTX 2.5 模型從起始圖片產生專業品質的影片。您可以使用文字提示描述影片內容，選擇模型變體，並調整持續時間、解析度、幀率與音訊生成。可選擇提供最終幀來定義影片的結尾。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `影像` | 用於影片的第一幀。 | IMAGE | 是 | Exactly one image |
| `模型` | 模型設定群組。選擇要使用的 LTX 2.5 模型變體。 | COMBO | 是 | "LTX-2.5 (Fast)"<br>"LTX-2.5 (Pro)" |
| `時長` | 產生影片的長度（秒）。 | INT | 是 | Integer |
| `解析度` | 產生影片的解析度。可用選項可能取決於所選的模型。 | COMBO | 是 | "1280x720"<br>"720x1280"<br>"1920x1080"<br>"1080x1920"<br>"2560x1440"<br>"1440x2560"<br>"3840x2160"<br>"2160x3840" |
| `幀率` | 產生影片的幀率。 | INT | 是 | Integer (default: 25) |
| `生成音訊` | 是否為影片產生音訊。 | BOOLEAN | 是 | True<br>False (default: True) |
| `提示詞` | 要產生的影片內容的文字描述。必須介於 1 到 10000 個字元之間。 | STRING | 是 | 1 至 10000 characters |
| `種子` | 用於可重現生成的種子值。使用相同的種子與相同設定會產生相同的結果。 | INT | 是 | Integer (default: 42) |
| `最後幀` | 用於影片的最後一幀。 | IMAGE | 否 | Exactly one image |

**注意：** `image` 僅支援一張圖片。如果提供了 `last_frame`，它也必須恰好包含一張圖片。可用的 `model.resolution` 選項可能因所選的 `model` 變體而異。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 根據提供的起始圖片與生成設定所產生的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`
