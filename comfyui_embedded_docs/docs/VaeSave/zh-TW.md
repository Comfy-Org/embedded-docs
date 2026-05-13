> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAESave/zh-TW.md)

## 概述

VAESave 節點專為將 VAE 模型及其元數據（包括提示詞和額外的 PNG 資訊）儲存到指定輸出目錄而設計。它封裝了將模型狀態及相關資訊序列化為檔案的功能，有助於保存和分享訓練好的模型。

## 輸入

| 參數 | 資料類型 | 說明 |
|-----------|-------------|-------------|
| `vae`     | VAE       | 要儲存的 VAE 模型。此參數至關重要，因為它代表要序列化並儲存其狀態的模型。 |
| `filename_prefix` | STRING   | 儲存模型及其元數據的檔案名稱前綴。這有助於組織化儲存並方便模型的檢索。 |

## 輸出

此節點沒有輸出類型。