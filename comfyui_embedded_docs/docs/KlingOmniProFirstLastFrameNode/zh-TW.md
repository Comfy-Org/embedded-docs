# Kling Omni 首末影格轉影片 (Pro)

此節點使用最新的 Kling AI 模型，從起始幀、可選的結束幀或參考影像生成影片。它可以建立單一影片，或包含多個片段（每個片段有獨立提示詞和時長）的多鏡頭分鏡腳本。此節點處理這些輸入，以產生指定長度和解析度的影片，並可選擇生成音訊。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 用於影片生成的特定 Kling AI 模型。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `提示詞` | 描述影片內容的文字提示詞。可包含正面和負面描述。啟用分鏡腳本時忽略此項。 | STRING | 是 | - |
| `時長` | 生成影片的所需長度，單位為秒（預設值：5）。 | INT | 是 | 3 至 15 |
| `起始影格` | 影片序列的起始影像。 | IMAGE | 是 | - |
| `結束影格` | 可選的影片結束幀。不能與 `參考圖片` 同時使用。不適用於分鏡腳本。 | IMAGE | 否 | - |
| `參考圖片` | 最多 6 張額外的參考影像。 | IMAGE | 否 | - |
| `解析度` | 生成影片的輸出解析度（預設值："1080p"）。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `分鏡腳本` | 生成一系列具有獨立提示詞和時長的影片片段。僅 `kling-v3-omni` 模型支援。啟用時，每個分鏡腳本都需要輸入提示詞和時長。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `產生音訊` | 為影片生成音訊（預設值：False）。僅 `kling-v3-omni` 模型支援。 | BOOLEAN | 否 | True / False |
| `種子` | 種子控制節點是否應重新執行；無論種子為何，結果皆非確定性（預設值：0）。 | INT | 否 | 0 至 2147483647 |

**重要限制：**

* `end_frame` 輸入不能與 `reference_images` 輸入同時使用。
* `end_frame` 輸入不能與分鏡腳本同時使用。
* `kling-video-o1` 模型不支援超過 10 秒的時長、音訊生成、4k 解析度或分鏡腳本。
* 如果您未提供 `end_frame` 或任何 `reference_images`，且使用 `kling-video-o1` 模型，則 `duration` 只能設定為 5 或 10 秒。
* 所有輸入影像（`first_frame`、`end_frame` 及任何 `reference_images`）的寬度和高度最小尺寸必須為 300 像素。
* 所有輸入影像的長寬比必須在 1:2.5 至 2.5:1 之間。
* 透過 `reference_images` 輸入最多可提供 6 張影像。
* `prompt` 文字長度必須在 1 到 2500 個字元之間（啟用分鏡腳本時允許 0 個字元）。
* 啟用分鏡腳本時，所有分鏡片段時長的總和必須等於全域 `duration` 值。
* 每個分鏡腳本提示詞的長度必須在 1 到 512 個字元之間。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `output` | 生成的影片檔案。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProFirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bd0fb11242b7f79062079b1aa48c3524abf59ecf06a90f013e57b6910cd8e224`
