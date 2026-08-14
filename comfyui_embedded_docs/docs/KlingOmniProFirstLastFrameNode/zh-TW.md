# Kling Omni 首末影格轉影片 (Pro)

此節點使用最新的 Kling AI 模型，從起始幀、可選的結束幀或參考圖像生成影片。它可以建立單一影片或包含多個片段的多鏡頭分鏡，每個片段都有各自的提示詞和持續時間。此節點處理這些輸入，以產生指定長度和解析度的影片，並可選擇生成音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 用於影片生成的特定 Kling AI 模型。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `prompt` | 描述影片內容的文字提示詞。可包含正面和負面描述。啟用分鏡時忽略。 | STRING | 是 | - |
| `duration` | 生成影片的所需長度（以秒為單位，預設：5）。 | INT | 是 | 3 到 15 |
| `first_frame` | 影片序列的起始圖像。 | IMAGE | 是 | - |
| `end_frame` | 影片的可選結束幀。不能與 `reference_images` 同時使用。不適用於分鏡。 | IMAGE | 否 | - |
| `reference_images` | 最多 6 張額外的參考圖像。 | IMAGE | 否 | - |
| `resolution` | 生成影片的輸出解析度（預設："1080p"）。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `storyboards` | 生成一系列具有各自提示詞和持續時間的影片片段。僅支援 `kling-v3-omni`。啟用時，每個分鏡都需要提示詞和持續時間輸入。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `generate_audio` | 為影片生成音訊（預設：False）。僅支援 `kling-v3-omni`。 | BOOLEAN | 否 | True / False |
| `seed` | 種子控制節點是否應重新執行；無論種子為何，結果都是非確定性的（預設：0）。 | INT | 否 | 0 到 2147483647 |

### 分鏡輸入

當 `storyboards` 設定為 `"disabled"` 以外的值時，會為每個選取的片段新增以下輸入（N 從 1 到所選的分鏡數量）：

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | 分鏡片段 N 的提示詞。最多 512 個字元。（預設：""） | STRING | 是 | - |
| `storyboard_N_duration` | 分鏡片段 N 的持續時間（以秒為單位，預設：4）。 | INT | 是 | 1 到 15 |

**重要限制：**

* `end_frame` 輸入不能與 `reference_images` 輸入同時使用。
* `end_frame` 輸入不能與分鏡同時使用。
* `kling-video-o1` 模型不支援超過 10 秒的持續時間、音訊生成、4k 解析度或分鏡。
* 如果使用 `kling-video-o1` 模型且未提供 `end_frame` 或任何 `reference_images`，則 `duration` 只能設定為 5 或 10 秒。
* 所有輸入圖像（`first_frame`、`end_frame` 以及任何 `reference_images`）的寬度和高度都必須至少為 300 像素。
* 所有輸入圖像的長寬比必須介於 1:2.5 和 2.5:1 之間。
* 透過 `reference_images` 輸入最多可提供 6 張圖像。
* `prompt` 文字長度必須介於 1 到 2500 個字元之間（啟用分鏡時允許 0 個字元）。
* 提示詞可以使用佔位符 `@image`、`@image1`、`@image2` 等來參考輸入圖像；這些佔位符會自動轉換為 API 相容的圖像參考格式。
* 啟用分鏡時，所有分鏡片段的總持續時間必須等於整體 `duration` 值。
* 每個分鏡提示詞的長度必須介於 1 到 512 個字元之間。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`
