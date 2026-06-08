# Kling 圖片（首幀）轉影片含音頻節點

Kling 圖片（首幀）轉影片含音頻節點使用 Kling AI 模型，從單張起始圖片和文字提示生成短影片。它會建立一個以提供的圖片為開頭的影片序列，並可選擇性地包含 AI 生成的音頻來配合視覺效果。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 用於影片生成的 Kling AI 模型特定版本。 | COMBO | 是 | `"kling-v2-6"` |
| `起始幀` | 將作為生成影片第一幀的圖片。圖片必須至少為 300x300 像素，且長寬比介於 1:2.5 到 2.5:1 之間。 | IMAGE | 是 | - |
| `提示詞` | 正向文字提示。描述您想要生成的影片內容。提示長度必須在 1 到 2500 個字元之間。 | STRING | 是 | - |
| `模式` | 影片生成的操作模式。 | COMBO | 是 | `"pro"` |
| `時長` | 要生成的影片長度，以秒為單位。 | COMBO | 是 | `5`<br>`10` |
| `產生音訊` | 啟用時，節點將生成音頻來配合影片。停用時，影片將為無聲狀態。（預設值：True） | BOOLEAN | 否 | - |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `video` | 生成的影片檔案，根據 `產生音訊` 輸入的設定，可能包含音頻。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageToVideoWithAudio/zh-TW.md)

---
**Source fingerprint (SHA-256):** `f161eedbc5d780805e3d0ca32b6be94cc78afcd2749e065c032ea20991b782fc`
