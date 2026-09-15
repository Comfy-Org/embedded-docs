# MiniMax H3 首末幀生成影片

此節點使用 MiniMax H3 模型，從第一幀圖像以及（可選的）最後一幀圖像生成影片。`model` 選擇器會變更適用的生成設定與限制條件，而生成影片的長寬比會遵循所提供的圖像。

## 輸入

### 通用輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影片生成的模型。選擇模型後，下方會顯示該模型專屬的設定。 | DYNAMIC_COMBO | 是 | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | 影片的第一幀圖像。生成影片的長寬比會遵循此圖像。 | IMAGE | 是 | - |
| `last_frame` | 影片可選的最後一幀圖像。提供時，影片會從第一幀朝向此最後一幀生成。 | IMAGE | 否 | - |
| `seed` | 隨機種子。相同請求搭配相同種子會產生相似但不保證完全相同的結果。包含「control after generate」選項。預設：42。 | INT | 是 | 0 至 4294967295 |
| `watermark` | 是否在影片中加入 AIGC 浮水印。這是進階參數。僅 `MiniMax H3` 模型支援。預設：False。 | BOOLEAN | 是 | True<br>False |

### MiniMax H3 輸入

當在 `model` 選擇器中選擇 `MiniMax H3` 時，會顯示這些設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。必須包含至少一個非空白字元。 | STRING | 是 | Multiline text |
| `resolution` | 輸出影片的解析度。 | COMBO | 是 | "768P"<br>"2K" |
| `duration` | 輸出影片的時長（秒）。預設：5。 | INT | 是 | 4 至 15 |

### MiniMax H3 Max 與 MiniMax H3 Max Turbo 輸入

這些設定由 `MiniMax H3 Max` 與 `MiniMax H3 Max Turbo` 共用。選擇任一模型都會顯示相同的設定。

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 用於影片生成的文字提示。不得為空或僅含空白，且限制為 50,000 個字元。 | STRING | 是 | Multiline text |
| `resolution` | 輸出影片的解析度。預設：768P。 | COMBO | 是 | "480P"<br>"768P" |
| `duration` | 輸出影片的時長（秒）。預設：5。 | INT | 是 | 5 至 15 |
| `prompt_expansion_mode` | 生成前改寫提示所投入的程度。預設：balanced。 | COMBO | 是 | "balanced"<br>"quality" |

**限制條件說明：**

- 提示必須包含文字：空白或僅含空白的提示會被拒絕。
- 任何提供的幀圖像必須至少 256 像素寬且 256 像素高，且寬高比介於 0.4 與 2.5 之間（約 2:5 至 5:2）。此要求適用於 `first_frame`，以及提供時的 `last_frame`。
- 省略 `last_frame` 時，影片僅從第一幀生成。
- 輸出影片會遵循所提供圖像的長寬比。
- `watermark` 僅由 `MiniMax H3` 支援。在 `MiniMax H3 Max` 或 `MiniMax H3 Max Turbo` 中啟用會引發錯誤。
- `MiniMax H3` 的時長範圍為 4 至 15 秒，而 `MiniMax H3 Max` 與 `MiniMax H3 Max Turbo` 的時長範圍為 5 至 15 秒。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `video` | 使用所選 MiniMax H3 模型，從第一幀及可選的最後一幀生成的影片。 | VIDEO |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
