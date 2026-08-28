# Grok 影片編輯

此節點使用 Grok API，根據文字提示詞編輯現有影片。它會上傳您的影片，將修改請求傳送給 AI 模型以依您的描述進行調整，然後回傳新生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片編輯的 AI 模型（預設值："grok-imagine-video"）。 | COMBO | 是 | "grok-imagine-video" |
| `prompt` | 目標影片的文字描述。 | STRING | 是 | N/A |
| `video` | 要編輯的輸入影片。支援的最大持續時間為 8.7 秒，檔案大小上限為 50MB。 | VIDEO | 是 | N/A |
| `seed` | 決定節點是否應重新執行的種子；無論種子為何，實際結果皆具非確定性（預設值：0）。 | INT | 否 | 0 至 2147483647 |

**限制條件：**

* `prompt` 不可為空白。
* 輸入的 `video` 持續時間必須介於 1 到 8.7 秒之間。
* 輸入的 `video` 檔案大小不得超過 50MB。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 由 AI 模型生成的編輯後影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`
