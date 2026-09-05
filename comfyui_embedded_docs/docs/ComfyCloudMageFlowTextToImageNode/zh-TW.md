# ComfyCloudMageFlowTextToImageNode

此節點透過將請求傳送至 Comfy Cloud 中的 Mage-Flow 文字轉圖像工作流程，從文字提示生成圖像。它執行完整的 30 步生成流程，而非較快的蒸餾 turbo 流程，並且接受負面提示詞，讓您可以描述不希望出現在最終圖像中的內容。在此 30 步模式中支援負面提示詞；根據節點摘要，蒸餾 turbo 變體無法妥善利用它。

## 輸入

| 參數 | 描述 | 資料型別 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `prompt` | 要生成圖像的文字描述。 | STRING | 是 | Free-form text |
| `negative_prompt` | 描述不應出現在生成圖像中的內容的文字。此輸入用於標準的 30 步生成流程，但蒸餾 turbo 變體無法良好地利用負面提示詞。 | STRING | 否 | Free-form text |

## 輸出

| 輸出名稱 | 描述 | 資料型別 |
|-------------|-------------|-----------|
| `image` | 從提供的文字提示和負面提示詞生成的圖像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
