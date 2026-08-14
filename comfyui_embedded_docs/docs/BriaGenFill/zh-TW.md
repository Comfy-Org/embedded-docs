# BriaGenFill

此節點使用 Bria API 在影像的遮罩區域內生成物體或場景。它會上傳影像與遮罩，將提示詞傳送至 Bria 生成式填充服務，等待操作完成，然後回傳編輯後的影像。這是一項付費 API 操作（每次請求 US$0.0429）。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `image` | 要編輯的輸入影像。 | IMAGE | 是 | - |
| `mask` | 白色區域會填入生成的內容，黑色區域則保留。遮罩在傳送前會先進行二值化處理，因此部分繪製的區域會被視為白色。必須與影像具有相同的長寬比。 | MASK | 是 | - |
| `prompt` | 描述要在遮罩區域內生成什麼內容。至少須包含 1 個字元。 | STRING | 是 | - |
| `negative_prompt` | 描述要在生成結果中避免的內容。若留空，則不會傳送至 API。 | STRING | 是 | - |
| `refine_prompt` | 自動調整提示詞以獲得更好的結果；停用後則會完全按照撰寫的提示詞使用。（預設值：true） | BOOLEAN | 是 | true<br>false |
| `seed` | 生成過程的種子。（預設值：42） | INT | 是 | 1 至 2147483647 |
| `moderation` | 請求的審核設定。設為 "true" 時，會套用下列巢狀審核選項。（預設值："false"） | COMBO | 是 | "false"<br>"true" |

注意：`prompt` 不能為空，且 `mask` 必須與 `image` 具有相同的長寬比。

當 `moderation` 設為 "true" 時，可使用下列巢狀布林選項：
- `prompt_content_moderation`（預設值：false）：對提示詞套用內容審核。
- `visual_input_moderation`（預設值：false）：對輸入影像套用內容審核。
- `visual_output_moderation`（預設值：false）：對輸出影像套用內容審核。

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `image` | 生成的內容填入遮罩區域後所得的結果影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/zh-TW.md)

---
**Source fingerprint (SHA-256):** `0d9babfa5e14c03f73d2b5befbd1c5cd1f5ffc685a0d7ccb3db09cfec51ba4fa`
