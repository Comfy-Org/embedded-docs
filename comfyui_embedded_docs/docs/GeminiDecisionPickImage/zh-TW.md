# Google Gemini Decision (Pick Image)

從一批影像中挑選最佳影像。將 `index` 連接到 Get Image from Batch，以保留所選影像，讓工作流程其餘部分只針對所選影像執行。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `model` | 要使用的模型（預設：`"gemini-decision-1"`）。 | COMBO | 是 | `"gemini-decision-1"` |
| `question` | 要挑選哪張影像（預設："Which image best matches the prompt in text? If there is no text, which image has the best quality?"）。 | STRING | 是 | 1 至 5000 個字元 |
| `images` | 可供選擇的影像，形式為一批影像或單一批次的影格。 | IMAGE | 是 | 2 至 64 張影像 |
| `text` | 問題所針對的文字，例如用來生成這些影像的提示詞，最多 20000 個字元。 | STRING | 否 | 最多 20000 個字元 |

此節點需要 2 至 64 張影像，若只有單張影像會引發錯誤。當選擇應依據提示詞而非僅依影像品質時，請連接 `text`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
|-------------|-------------|-----------|
| `index` | 所選影像在批次中的位置，從 0 開始。 | INT |
| `confidence` | 對所選結果的信心程度，介於 0 與 1 之間。 | FLOAT |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionPickImage/zh-TW.md)

---
**Source fingerprint (SHA-256):** `55eb604923cb66b42f23f37d0c710a97033cc2c5d95880d45397bba10e44dab0`
