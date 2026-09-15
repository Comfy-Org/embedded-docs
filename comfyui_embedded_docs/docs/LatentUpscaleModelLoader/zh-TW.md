# 載入 Latent 放大模型

`LatentUpscaleModelLoader` 節點會從儲存在 ComfyUI `latent_upscale_models` 資料夾中的檔案載入專門用於放大潛在表徵的模型。它會自動從檔案內容偵測模型架構（Hunyuan Video 720p、Hunyuan Video 1080p 或 Latent Upsampler），並設定相符的內部模型，因此結果可直接供其他節點使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的 Latent 放大模型檔案名稱。可用選項會根據 ComfyUI 的 `latent_upscale_models` 目錄中現有的檔案動態填入。 | COMBO | 是 | `latent_upscale_models` 資料夾中的所有檔案 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已載入的 Latent 放大模型，已完成設定並可供使用。視偵測到的檔案內容而定，這會是 720p Hunyuan Video 放大器、1080p Hunyuan Video 放大器，或包裝後的 Latent Upsampler 模型。 | LATENT_UPSCALE_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
