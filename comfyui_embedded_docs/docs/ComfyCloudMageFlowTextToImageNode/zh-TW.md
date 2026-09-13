# Comfy Cloud Mage Flow 文字轉影像 [測試版]

此節點會將請求傳送至 Comfy Cloud 中的 Mage-Flow 文字轉圖像工作流程，以根據文字提示生成影像。它會執行完整的 30 步生成流程，而非較快速的蒸餾 turbo 流程，並且接受負向提示，讓你可以描述不希望出現在最終影像中的內容。此 30 步模式支援負向提示；根據節點摘要，蒸餾 turbo 變體無法妥善利用負向提示。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
|-----------|-------------|-----------|----------|-------|
| `提示詞` | 要生成之影像的文字描述。 | STRING | 是 | 自由格式文字 |
| `負面提示詞` | 描述不應出現在生成影像中的內容之文字。此輸入會用於標準 30 步生成流程，但蒸餾 turbo 變體無法妥善利用負向提示。 | STRING | 否 | 自由格式文字 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
|-------------|-------------|-----------|
| `image` | 根據提供的文字提示與負向提示所生成的影像。 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
