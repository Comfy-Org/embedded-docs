> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/zh-TW.md)

## 概述

CheckpointLoader 節點專為進階載入操作設計，主要用於載入模型檢查點及其配置檔案。它能夠從指定目錄中擷取初始化與執行生成模型所需的模型元件，包括配置檔案和檢查點。

## 輸入

| 參數名稱       | 資料類型        | 描述 |
|----------------|-----------------|------|
| `config_name`  | COMBO[STRING] | 指定要使用的配置檔案名稱。這對於決定模型的參數和設定至關重要，會影響模型的行為和效能。 |
| `ckpt_name`    | COMBO[STRING] | 指定要載入的檢查點檔案名稱。這直接影響初始化模型的狀態，包括其初始權重和偏差。 |

## 輸出

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `model`  | MODEL    | 代表從檢查點載入的主要模型，已準備好進行後續操作或推理。 |
| `clip`   | CLIP     | 提供從檢查點載入的 CLIP 模型元件（如果可用且被請求）。 |
| `vae`    | VAE      | 提供從檢查點載入的 VAE 模型元件（如果可用且被請求）。 |