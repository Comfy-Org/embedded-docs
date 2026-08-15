# BriaGenFill

此節點使用 Bria API 在影像的遮罩區域內生成物件或場景。它會上傳影像與遮罩，將提示詞傳送至 Bria 生成式填補服務，等待操作完成，然後回傳編輯後的影像。此為付費 API 操作（每次請求 US$0.0429）。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要編輯的輸入影像。 | IMAGE | 是 | - |
| `mask` | 白色區域會被生成的內容填滿，黑色區域則保留。遮罩在傳送前會進行二值化處理，因此部分塗繪的區域會被視為白色。必須與影像具有相同的長寬比。 | MASK | 是 | - |
| `prompt` | 描述要在遮罩區域內生成內容的文字。至少需包含 1 個字元。（預設值：""） | STRING | 是 | - |
| `negative_prompt` | 描述應避免出現在生成結果中的內容的提示詞。若留空，則不會傳送至 API。（預設值：""） | STRING | 是 | - |
| `refine_prompt` | 自動調整提示詞以獲得更好的結果；停用則完全按照原樣使用提示詞。（預設值：true） | BOOLEAN | 是 | true<br>false |
| `seed` | 生成過程的種子值。（預設值：42） | INT | 是 | 1 至 2147483647 |
| `moderation` | 審核設定。設為 "true" 時，會套用下方的審核選項。（預設值："false"） | DYNAMIC_COMBO | 是 | "false"<br>"true" |

### 審核輸入（當 `moderation` = "true" 時）

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | 對提示詞套用內容審核。（預設值：false） | BOOLEAN | 否 | true<br>false |
| `visual_input_moderation` | 對輸入影像套用內容審核。（預設值：false） | BOOLEAN | 否 | true<br>false |
| `visual_output_moderation` | 對輸出影像套用內容審核。（預設值：false） | BOOLEAN | 否 | true<br>false |

**注意：** `prompt` 不得為空。`mask` 必須與 `image` 具有相同的長寬比。遮罩會以 50% 不透明度進行二值化，因此塗繪不透明度低於一半的區域會被忽略；若二值化後遮罩中沒有白色區域，節點會拋出錯誤。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 遮罩區域由生成的內容填補後的結果影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
