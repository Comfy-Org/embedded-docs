# Runway Aleph2 影片轉影片節點

此節點使用 Runway 的 Aleph2 模型，透過文字提示來編輯影片。它能重新風格化、重新打光、新增或移除元素，或改變視角，同時保留原始動作與時間節奏，從而轉換您的影片素材。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 描述輸出中應出現的內容（1-1000 個字元）。 | STRING | 是 | 1-1000 個字元 |
| `video` | 要編輯的輸入影片。必須為 2-30 秒，且幀率為 30 fps 或更低。 | VIDEO | 是 | 2-30 秒長度，最大 30 fps |
| `seed` | 生成用的隨機種子（預設值：0）。 | INT | 是 | 0 到 4294967295 |
| `public_figure_threshold` | 針對可辨識公眾人物的內容審查（預設值："low"）。 | COMBO | 是 | "auto"<br>"low" |
| `keyframes` | 錨定於輸入影片的引導影像，來自 Aleph2 關鍵影格節點（最多 5 個）。請使用關鍵影格或提示影像，不可同時使用兩者。 | KEYFRAME | 否 | 最多 5 個項目 |
| `prompt_images` | 錨定於輸出影片的引導影像，來自 Aleph2 提示影像節點（最多 5 個）。請使用關鍵影格或提示影像，不可同時使用兩者。 | PROMPT_IMAGE | 否 | 最多 5 個項目 |

**重要限制：**
- 輸入影片長度必須在 2 到 30 秒之間，且幀率為 30 fps 或更低。
- 您只能使用 `keyframes` 或 `prompt_images` 其中一種作為引導，不可同時使用兩者。
- 每個引導輸入（關鍵影格或提示影像）最多支援 5 個項目。
- 關鍵影格時間戳記與提示影像時間戳記不得超過輸入影片的長度。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 由 Aleph2 模型生成的編輯後影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2VideoToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bda4d0f49843c1a8f311ddbce5911a2a157cae798a26f7a183b31fe41686d0b7`
