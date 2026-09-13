# ByteDanceImageEditNode

ByteDance Image Edit 節點可讓您透過 API 使用 ByteDance 的 AI 模型修改影像。您提供輸入影像與描述所需變更的文字提示詞，節點便會依照您的指示處理影像。此節點會自動處理 API 通訊並回傳編輯後的影像。

## 輸入

| 參數 | 描述 | 資料類型 | 輸入類型 | 預設值 | 範圍 |
| --- | --- | --- | --- | --- | --- |
| `model` | 模型名稱 | MODEL | COMBO | seededit_3 | Image2ImageModelName options |
| `image` | 要編輯的基礎影像 | IMAGE | IMAGE | - | - |
| `prompt` | 編輯影像的指令 | STRING | STRING | "" | - |
| `seed` | 用於生成的種子 | INT | INT | 0 | 0-2147483647 |
| `guidance_scale` | 數值越高，影像會越緊密地遵循提示詞 | FLOAT | FLOAT | 5.5 | 1.0-10.0 |
| `watermark` | 是否在影像中加入「AI generated」浮水印 | BOOLEAN | BOOLEAN | True | - |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `IMAGE` | 從 ByteDance API 回傳的編輯後影像 | IMAGE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceImageEditNode/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9dc13d89f84756b545120efb5535e08ada163d4534975809f5056bdf7d8bfb73`
