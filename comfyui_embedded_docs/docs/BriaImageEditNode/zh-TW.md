# Bria FIBO 圖像編輯

Bria FIBO 影像編輯節點可讓您透過文字指令編輯現有影像。它會將影像和您的提示詞傳送至 Bria API，由 Bria API 使用 FIBO 模型建立編輯後的影像版本。您也可以提供遮罩，將變更限制在特定區域。

## 輸入

### 通用輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影像編輯的模型版本。 | COMBO | 是 | `"FIBO"` |
| `image` | 您想要編輯的輸入影像。 | IMAGE | 是 | - |
| `prompt` | 編輯影像的指示（預設：空白）。 | STRING | 是 | - |
| `negative_prompt` | 描述您不希望出現在編輯後影像中的文字（預設：空白）。 | STRING | 是 | - |
| `structured_prompt` | 包含 JSON 格式結構化編輯提示詞的字串。若需要精確、程式化的控制，請使用此參數取代一般提示詞（預設：空白）。 | STRING | 是 | - |
| `seed` | 用於初始化隨機生成的數字，確保結果可重現（預設：1）。 | INT | 是 | 1 to 2147483647 |
| `guidance_scale` | 數值越高，影像越貼近提示詞（預設：3）。 | FLOAT | 是 | 3.0 to 5.0 |
| `steps` | 模型執行的去噪步驟數（預設：50）。 | INT | 是 | 20 to 50 |
| `moderation` | 審核設定。選取 `"true"` 會顯示額外的審核選項。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |
| `mask` | 若未提供，編輯將套用至整個影像。 | MASK | 否 | - |

### 審核輸入

當 `moderation` 設為 `"true"` 時，可使用下列額外輸入：

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt_content_moderation` | 是否審核提示詞文字中的不當內容（預設：false）。 | BOOLEAN | 否 | `true`<br>`false` |
| `visual_input_moderation` | 是否審核輸入影像中的不當內容（預設：false）。 | BOOLEAN | 否 | `true`<br>`false` |
| `visual_output_moderation` | 是否審核編輯後輸出影像中的不當內容（預設：true）。 | BOOLEAN | 否 | `true`<br>`false` |

**重要限制：**

- `prompt` 或 `structured_prompt` 至少其中一個必須非空。若兩者皆為空，節點會觸發錯誤。
- 當 `moderation` 設為 `"true"` 時，便會顯示上述三個審核輸入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria API 回傳的編輯後影像。 | IMAGE |
| `structured_prompt` | 在編輯過程中使用或產生的結構化提示詞。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
