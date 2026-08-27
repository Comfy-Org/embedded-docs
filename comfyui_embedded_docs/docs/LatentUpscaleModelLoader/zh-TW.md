# 載入 Latent 放大模型

LatentUpscaleModelLoader 節點會從 ComfyUI 的 `latent_upscale_models` 資料夾中的檔案載入一個專門用於放大潛在表示的模型。它會根據檔案內容自動偵測模型類型（720p、1080p 或其他潛在放大器），並配置相符的內部架構，使載入的模型可供其他節點使用。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的潛在放大模型檔案名稱。可用選項會根據 ComfyUI 的 `latent_upscale_models` 目錄中存在的檔案動態填入。 | COMBO | 是 | `latent_upscale_models` 資料夾中的所有檔案 |

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已載入的潛在放大模型，已配置並可供使用。 | LATENT_UPSCALE_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
