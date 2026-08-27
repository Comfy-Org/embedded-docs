# Kling Omni 首末影格轉影片 (Pro)

此節點使用最新的 Kling AI 模型，從起始幀、可選的結束幀或參考圖像生成影片。它可建立單一影片，或具有每個片段個別提示詞和時長的多鏡頭故事板。此節點處理這些輸入，以產生指定長度和解析度的影片，並可選地生成音訊。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 用於影片生成的特定 Kling AI 模型。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `提示詞` | 描述影片內容的文字提示詞。可包含正面和負面描述。啟用故事板時忽略此項。 | STRING | 是 | - |
| `時長` | 生成影片的所需長度（秒）（預設值：5）。 | INT | 是 | 3 至 15 |
| `起始影格` | 影片序列的起始圖像。 | IMAGE | 是 | - |
| `結束影格` | 影片的選用結束幀。無法與 `reference_images` 同時使用。不適用於故事板。 | IMAGE | 否 | - |
| `參考圖片` | 最多 6 張額外的參考圖像。 | IMAGE | 否 | - |
| `解析度` | 生成影片的輸出解析度（預設值："1080p"）。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `分鏡腳本` | 生成一系列具有個別提示詞和時長的影片片段。僅支援 `kling-v3-omni`。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `產生音訊` | 為影片生成音訊（預設值：False）。僅支援 `kling-v3-omni`。 | BOOLEAN | 否 | True / False |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果都是非確定性的（預設值：0）。 | INT | 否 | 0 至 2147483647 |

### 故事板輸入

當 `storyboards` 設定為 `"disabled"` 以外的值時，下列輸入會為每個選取的片段新增（N 範圍從 1 到所選故事板數量）：

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `storyboard_N_prompt` | 故事板片段 N 的提示詞。最多 512 個字元。（預設值：""） | STRING | 是 | - |
| `storyboard_N_duration` | 故事板片段 N 的時長（秒）（預設值：4）。 | INT | 是 | 1 至 15 |

**重要約束：**

* `end_frame` 輸入無法與 `reference_images` 輸入同時使用。
* `end_frame` 輸入不能與故事板同時使用。
* `kling-video-o1` 模型不支援超過 10 秒的時長、音訊生成、4k 解析度或故事板。
* 若使用 `kling-video-o1` 模型時未提供 `end_frame` 或任何 `reference_images`，則 `duration` 只能設定為 5 或 10 秒。
* 所有輸入圖像（`first_frame`、`end_frame` 及任何 `reference_images`）的寬度和高度都必須至少為 300 像素。
* 所有輸入圖像的縱橫比必須介於 1:2.5 和 2.5:1 之間。
* 透過 `reference_images` 輸入最多可提供 6 張圖像。
* `prompt` 文字長度必須介於 1 到 2500 個字元之間（啟用故事板時允許 0 個字元）。
* 提示詞可以使用佔位符 `@image`、`@image1`、`@image2` 等來引用輸入圖像；這些佔位符會自動轉換為與 API 相容的圖像引用格式。
* 啟用故事板時，所有故事板片段的總時長必須等於全域 `duration` 值。
* 每個故事板提示詞的長度必須介於 1 到 512 個字元之間。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2b26914ba29c3d877a981e41acb44d15dfacc604d86d7cc232ebfa7fda0ae3b8`
