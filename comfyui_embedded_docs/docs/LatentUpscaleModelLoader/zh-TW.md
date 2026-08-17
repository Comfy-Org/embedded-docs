# 載入 Latent 放大模型

LatentUpscaleModelLoader 節點載入專門設計用於放大潛在表示（latent representations）的模型。它會從系統指定資料夾讀取模型檔案，並自動偵測其類型（720p、1080p 或其他），以實例化並設定正確的內部模型架構。載入後的模型即可供其他節點用於潛在空間超解析度（super-resolution）任務。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model_name` | 要載入的潛在放大模型檔案名稱。可用選項會從 ComfyUI 的 `latent_upscale_models` 目錄中存在的檔案動態填入。 | COMBO | 是 | `latent_upscale_models` 資料夾中的所有檔案 |

注意：節點會根據檔案內容自動偵測模型架構。包含 720p HunyuanVideo 超解析度層的模型會以 720p 模型載入，具有 1080p 樣式上採樣層的模型會以 1080p 模型載入，而具有其他層結構的模型則會以 LatentUpsampler 模型載入。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已載入的潛在放大模型，已設定並可供使用。 | LATENT_UPSCALE_MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7e23214b1b1fc11be84910a5a209c7990a5199120cb0e6b6c61302a442dcf153`
