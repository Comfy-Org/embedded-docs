# Sampler AR 視訊

Sampler AR Video 節點為自迴歸影片模型（例如使用 Causal Forcing 或 Self-Forcing 技術的模型）提供了一種專門的取樣方法。它直接在工作流程中管理與自迴歸（AR）循環相關的所有參數，讓您可以輕鬆配置模型逐步生成影片幀的方式。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `num_frame_per_block` | 每個自迴歸區塊的幀數。值為 1 表示模型一次生成一個幀（逐幀），值為 3 表示一次生成三個幀（分塊）。此設定必須與檢查點的訓練模式相符。預設值：1。 | INT | 是 | 1 to 64 |

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `SAMPLER` | 一個已配置的取樣器物件，使用帶有指定自迴歸參數的「ar_video」取樣函數。 | SAMPLER |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerARVideo/zh-TW.md)

---
**Source fingerprint (SHA-256):** `9ec72f52f5b77746f1587e64966bfa6cfd80ce8bb40a4fcb267f5197d09189fc`
