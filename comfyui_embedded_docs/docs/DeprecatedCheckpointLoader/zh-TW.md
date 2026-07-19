# DeprecatedCheckpointLoader

CheckpointLoader 節點專為進階載入操作而設計，具體用於載入模型檢查點及其配置。它協助檢索初始化與執行生成模型所需的模型組件，包括來自指定目錄的配置與檢查點。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `config_name` | 指定要使用的配置文件名稱。這對於決定模型的參數與設定至關重要，會影響模型的行為與效能。 | COMBO[STRING] |
| `ckpt_name` | 指示要載入的檢查點文件名稱。這直接影響正在初始化的模型狀態，進而影響其初始權重與偏差。 | COMBO[STRING] |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 代表從檢查點載入的主要模型，可供進一步操作或推論使用。 | MODEL |
| `clip` | 提供從檢查點載入的 CLIP 模型組件（若可用且已請求）。 | CLIP |
| `vae` | 提供從檢查點載入的 VAE 模型組件（若可用且已請求）。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/zh-TW.md)
