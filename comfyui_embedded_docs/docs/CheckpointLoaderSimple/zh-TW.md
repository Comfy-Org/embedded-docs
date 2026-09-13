# 載入檢查點

載入擴散模型檢查點（checkpoint）檔案，並將其拆分為三個核心元件：用於對 latents 進行去噪的主要模型、CLIP 文字編碼器，以及 VAE 影像編碼器/解碼器。此節點會自動偵測 `ComfyUI/models/checkpoints` 資料夾中的所有模型檔案，以及你的 `extra_model_paths.yaml` 檔案中設定的任何其他路徑。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 要載入的檢查點（模型）名稱。選擇檢查點模型檔案名稱，這會決定後續影像生成所使用的 AI 模型。 | COMBO | 是 | 在 checkpoints 資料夾中找到的所有模型檔案 |

**注意：** 如果在 ComfyUI 執行期間新增模型檔案，你需要重新整理瀏覽器（Ctrl+R），才能在向下式清單中看到新檔案。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 用於對 latents 進行去噪的模型。這是用於影像生成的核心擴散模型。 | MODEL |
| `CLIP` | 用於編碼文字提示的 CLIP 模型，會將文字描述轉換成 AI 能理解的資訊。 | CLIP |
| `VAE` | 用於在影像與潛在空間之間進行編碼與解碼的 VAE 模型。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/zh-TW.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
