# Kling Omni 文字轉影片 (Pro)

此節點使用最新的 Kling AI 模型，根據文字描述生成影片。它會將你的提示詞傳送至遠端 API，並傳回生成的影片。你可以控制影片的長度、形狀與品質，並可選擇建立多鏡頭分鏡。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model_name` | 用於影片生成的特定 Kling 模型（預設：`"kling-v3-omni"`）。 | COMBO | 是 | `"kling-v3-omni"`<br>`"kling-video-o1"` |
| `提示詞` | 描述影片內容的文字提示詞。這可以包含正面與負面描述。當分鏡啟用時會被忽略。 | STRING | 是 | 0 至 2500 characters |
| `長寬比` | 要生成影片的長寬比或尺寸。 | COMBO | 是 | `"16:9"`<br>`"9:16"`<br>`"1:1"` |
| `時長` | 影片長度，以秒為單位（預設：5）。 | INT | 是 | 3 至 15 seconds |
| `解析度` | 影片的品質或像素解析度（預設：`"1080p"`）。在內部對應至 standard、pro 或 4k 品質。 | COMBO | 否 | `"4k"`<br>`"1080p"`<br>`"720p"` |
| `分鏡腳本` | 生成一系列具有個別提示詞與時長的影片片段。o1 模型會忽略此項。 | DYNAMIC_COMBO | 否 | `"disabled"`<br>`"1 storyboard"`<br>`"2 storyboards"`<br>`"3 storyboards"`<br>`"4 storyboards"`<br>`"5 storyboards"`<br>`"6 storyboards"` |
| `產生音訊` | 是否為影片生成音訊（預設：False）。 | BOOLEAN | 否 | True / False |
| `種子` | `seed` 控制節點是否應重新執行；無論 `seed` 為何，結果皆為非確定性（預設：0）。 | INT | 否 | 0 至 2147483647 |

### 分鏡子輸入

當 `storyboards` 設定為 `"disabled"` 以外的值時，每個分鏡片段都會顯示以下輸入。在下列參數名稱中，`{i}` 是片段編號，從 1 到所選分鏡數量。

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `storyboard_{i}_prompt` | 分鏡片段 {i} 的提示詞。最多 512 個字元。 | STRING | 是 | 1 至 512 characters |
| `storyboard_{i}_duration` | 分鏡片段 {i} 的時長，以秒為單位（預設：4）。 | INT | 是 | 1 至 15 seconds |

### 參數限制與限制條件

- **模型特定限制：**
  - `kling-video-o1` 模型僅支援 **5 或 10 秒**的時長。
  - `kling-video-o1` 模型**不**支援音訊生成。
  - `kling-video-o1` 模型**不**支援 4k 解析度。
  - `kling-video-o1` 模型**不**支援分鏡。
- **分鏡限制：**
  - 當分鏡啟用時，`prompt` 欄位會被忽略。
  - 每個分鏡都需要自己的提示詞（1 到 512 個字元）與時長。
  - 所有分鏡的總時長必須完全等於全域 `duration` 參數。
- **提示詞要求：**
  - 當分鏡**停用**時，`prompt` 欄位為必填（最少 1 個字元）。
  - 當分鏡**啟用**時，`prompt` 欄位可以為空（0 個字元）。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `output` | 根據提供的文字提示詞與設定所生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`
