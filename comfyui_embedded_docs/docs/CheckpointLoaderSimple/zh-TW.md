## 概述

載入擴散模型檢查點檔案，並將其分解為三個核心組件：用於對潛在空間進行去噪的主模型、CLIP 文字編碼器以及 VAE 影像編碼器/解碼器。此節點會自動偵測 `ComfyUI/models/checkpoints` 資料夾以及您在 `extra_model_paths.yaml` 檔案中設定的任何其他路徑中的所有模型檔案。

## 輸入

| 參數 | 說明 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `ckpt_name` | 要載入的檢查點（模型）名稱。選擇檢查點模型檔案名稱，此名稱決定了後續影像生成所使用的 AI 模型。 | STRING | 是 | checkpoints 資料夾中的所有模型檔案 |

**注意：** 如果在 ComfyUI 運行時新增了模型檔案，您需要重新整理瀏覽器（Ctrl+R）才能在下拉清單中看到新檔案。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL` | 用於對潛在空間進行去噪的模型。這是用於影像生成的核心擴散模型。 | MODEL |
| `CLIP` | 用於編碼文字提示的 CLIP 模型，將文字描述轉換為 AI 可以理解的資訊。 | CLIP |
| `VAE` | 用於在影像與潛在空間之間進行編碼和解碼的 VAE 模型。 | VAE |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/zh-TW.md)

---
**Source fingerprint (SHA-256):** `2fd8866ae659f8080f46c16d3a9864fa563d2090815d897ea2f42ba8d66d9b39`
