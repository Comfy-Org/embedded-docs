# Bria FIBO 圖像編輯

Bria FIBO 影像編輯節點可讓您透過文字指令修改現有影像。它將影像和提示詞傳送至 Bria API，由 API 使用 FIBO 模型根據您的要求生成新的編輯後影像。您也可以提供遮罩，將編輯限制在特定區域。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 用於影像編輯的模型版本。 | COMBO | 是 | `"FIBO"` |
| `圖像` | 您想要編輯的輸入影像。 | IMAGE | 是 | - |
| `提示詞` | 編輯影像的指令（預設為空）。 | STRING | 是 | - |
| `負面提示詞` | 描述您不希望出現在編輯後影像中的內容的文字（預設為空）。 | STRING | 是 | - |
| `結構化提示詞` | 包含 JSON 格式的結構化編輯提示詞的字串。請使用此參數取代一般提示詞，以進行精確的程式化控制（預設為空）。 | STRING | 是 | - |
| `種子` | 用於初始化隨機生成過程的數字，以確保結果可重現（預設為 1）。 | INT | 是 | 1 到 2147483647 |
| `指引強度` | 數值越高，影像越貼近提示詞（預設為 3.0）。 | FLOAT | 是 | 3.0 到 5.0 |
| `步數` | 模型將執行的去噪步驟數（預設為 50）。 | INT | 是 | 20 到 50 |
| `審核` | 審核設定。選擇 `"true"` 會顯示更多針對提示詞內容、視覺輸入和視覺輸出的審核選項。 | DYNAMIC_COMBO | 是 | `"false"`<br>`"true"` |
| `遮罩` | 若省略，編輯將套用至整個影像。 | MASK | 否 | - |

**重要限制：**

- 您必須至少提供 `prompt` 或 `structured_prompt` 其中一個輸入。兩者不能同時為空。
- 當 `moderation` 參數設為 `"true"` 時，會出現三個額外的布林輸入：`prompt_content_moderation`（預設：false）、`visual_input_moderation`（預設：false）和 `visual_output_moderation`（預設：true）。

## 輸出

| 輸出名 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `IMAGE` | Bria API 回傳的編輯後影像。 | IMAGE |
| `結構化提示詞` | 編輯過程中所使用或產生的結構化提示詞。 | STRING |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`
