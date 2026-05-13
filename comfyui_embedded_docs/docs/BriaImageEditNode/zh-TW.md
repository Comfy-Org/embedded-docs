> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/zh-TW.md)

Bria FIBO 影像編輯節點允許您透過文字指令修改現有影像。它會將影像和提示詞發送至 Bria API，該 API 使用 FIBO 模型根據您的要求生成新的、編輯後的影像版本。您也可以提供遮罩來將編輯限制在特定區域。

## 輸入

| 參數 | 資料類型 | 必要 | 範圍 | 說明 |
|-----------|-----------|----------|-------|-------------|
| `model` | COMBO | 是 | `"FIBO"` | 用於影像編輯的模型版本。 |
| `image` | IMAGE | 是 | - | 您想要編輯的輸入影像。 |
| `prompt` | STRING | 否 | - | 描述如何編輯影像的文字指令（預設：空）。 |
| `negative_prompt` | STRING | 否 | - | 描述您不希望出現在編輯後影像中的文字（預設：空）。 |
| `structured_prompt` | STRING | 否 | - | 包含 JSON 格式結構化編輯提示詞的字串。使用此項代替一般提示詞以進行精確、程式化的控制（預設：空）。 |
| `seed` | INT | 是 | 1 到 2147483647 | 用於初始化隨機生成的數字，確保結果可重現（預設：1）。 |
| `guidance_scale` | FLOAT | 是 | 3.0 到 5.0 | 控制生成影像遵循提示詞的程度。數值越高，遵循程度越強（預設：3.0）。 |
| `steps` | INT | 是 | 20 到 50 | 模型將執行的去噪步驟數（預設：50）。 |
| `moderation` | DYNAMICCOMBO | 是 | `"false"`<br>`"true"` | 啟用或停用內容審核。選擇 `"true"` 會顯示針對提示詞內容、視覺輸入和視覺輸出的額外審核選項。 |
| `mask` | MASK | 否 | - | 可選的遮罩影像。若提供，編輯將僅應用於影像的遮罩區域。 |

**重要限制：**

* 您必須至少提供 `prompt` 或 `structured_prompt` 其中一個輸入。兩者不能同時為空。
* 需要且僅需要一個輸入 `image`。
* 當 `moderation` 參數設定為 `"true"` 時，會出現三個額外的布林輸入：`prompt_content_moderation`（預設：false）、`visual_input_moderation`（預設：false）和 `visual_output_moderation`（預設：true）。

## 輸出

| 輸出名稱 | 資料類型 | 說明 |
|-------------|-----------|-------------|
| `IMAGE` | IMAGE | Bria API 回傳的編輯後影像。 |
| `structured_prompt` | STRING | 在編輯過程中使用或生成的結構化提示詞。 |

---
**Source fingerprint (SHA-256):** `30148261f43f5bfd14339f5ff1ec250381a615cc05c67eee21b0a2423ebe349d`
