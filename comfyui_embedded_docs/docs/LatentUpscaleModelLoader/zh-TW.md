## 概述

LatentUpscaleModelLoader 節點會載入一個專門設計用於放大潛在表示（latent representations）的模型。它從系統指定的資料夾中讀取模型檔案，並自動偵測其類型（720p、1080p 或其他），以實例化並設定正確的內部模型架構。載入後的模型即可供其他節點用於潛在空間的超解析度任務。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的潛在放大模型檔案名稱。可用選項會根據 ComfyUI 的 `latent_upscale_models` 目錄中存在的檔案動態產生。 | STRING | 是 | *`latent_upscale_models` 資料夾中的所有檔案* |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已載入的潛在放大模型，已設定完成並可供使用。 | LATENT_UPSCALE_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `bd97f3ec1422aaabbd60779aa4112be44791daddc6307de53ae0e4219a90ab0e`
