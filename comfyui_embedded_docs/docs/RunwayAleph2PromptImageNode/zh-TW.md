# Runway Aleph2 提示圖像

此節點將引導圖像錨定到輸出影片中的特定時刻，控制編輯後的影片在該時間點的外觀。將此節點連接到 Runway Aleph2 影片轉影片節點的 `prompt_images` 輸入，並使用可選的 `prompt_images` 輸入將多個節點串聯在一起（最多 5 個）。

## ## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `圖片` | 放置在輸出影片所選時刻的引導圖像。 | IMAGE | 是 | - |
| `位置` | 如何將此圖像放置在輸出影片的時間軸上。選擇絕對時間（從開始的秒數）或分數時間（影片持續時間的百分比）。 | COMBO | 是 | `Absolute (seconds)`<br>`Fraction (0.0 to 1.0)` |
| `prompt_images` | 可選的先前提示圖像，用於與此圖像串聯。在此處連接另一個 Runway Aleph2 提示圖像節點的輸出，以建立最多 5 個引導圖像的鏈。 | PROMPT_IMAGE_CHAIN | 否 | - |

**位置模式詳細說明：**

當 `position` 設定為 `Absolute (seconds)` 時，您必須提供一個 `seconds` 值（預設值：0.0，範圍：0.0 到 30.0，步長：0.1）。這指定了此圖像在輸出影片中從開始起的精確時間（以秒為單位）。

當 `position` 設定為 `Fraction (0.0 to 1.0)` 時，您必須提供一個 `fraction` 值（預設值：0.0，範圍：0.0 到 1.0，步長：0.01）。這指定了此圖像在輸出影片中作為其總持續時間的分數所適用的位置（0.0 = 開始，1.0 = 結束）。

## ## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `prompt_images` | 提示圖像鏈，可連接到 Runway Aleph2 影片轉影片節點的 `prompt_images` 輸入。 | PROMPT_IMAGE_CHAIN |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2PromptImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `a8b86fb5d73d27cc58aa59c195ca058eec8a5c9433ea09522ff3e905f6b88193`
