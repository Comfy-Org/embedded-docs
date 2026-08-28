# Sampler AR 視訊

Sampler AR Video 節點為自迴歸影片模型（例如使用 Causal Forcing 或 Self-Forcing 技術的模型）提供了一種專門的取樣方法。它直接在工作流程中管理與自迴歸（AR）迴圈相關的所有參數，讓您可以輕鬆設定模型如何一步步生成影片幀。

## 輸入
| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `每區塊影格數` | 每個自迴歸區塊的幀數。值為 1 表示模型一次生成一幀（逐幀模式），值為 3 表示模型一次生成三幀（分塊模式）。此設定必須與檢查點的訓練模式相符。預設值：1。 | INT | 是 | 1 到 64 |

## 輸出
| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 一個配置好的取樣器物件，使用「ar_video」取樣函數及指定的自迴歸參數。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
