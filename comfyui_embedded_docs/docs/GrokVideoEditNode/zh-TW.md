# Grok 影片編輯

此節點使用 Grok API 根據文字提示編輯現有影片。它會上傳你的影片，向 AI 模型發送請求以依照你的描述進行修改，並回傳新生成的影片。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片編輯的 AI 模型（預設值："grok-imagine-video"）。 | COMBO | 是 | "grok-imagine-video" |
| `prompt` | 所需影片的文字描述。 | STRING | 是 | N/A |
| `video` | 要編輯的輸入影片。支援的最大長度為 8.7 秒，檔案大小為 50MB。 | VIDEO | 是 | N/A |
| `seed` | 用於決定節點是否重新執行的種子；無論種子為何，實際結果皆不確定（預設值：0）。 | INT | 否 | 0 至 2147483647 |

**限制條件：**

* `prompt` 不得為空。
* 輸入 `video` 的長度必須介於 1 到 8.7 秒之間。
* 輸入 `video` 的檔案大小不得超過 50MB。

**注意：** 此節點為 API 節點，需要 Comfy.org 帳戶和 API 金鑰才能執行。使用費用約為每秒影片 $0.06。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 由 AI 模型生成的編輯後影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokVideoEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7ceedff2f858bc0849b5e0d92d10ed51e7fdccd1391c6a6966561cb05999b4b1`
