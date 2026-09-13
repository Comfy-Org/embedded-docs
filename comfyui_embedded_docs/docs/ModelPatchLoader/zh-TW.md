# 模型修補載入器

ModelPatchLoader 節點會從 `model_patches` 資料夾載入模型修補檔案，並準備好在工作流程中使用。它會自動偵測檔案中包含的修補類型，建構對應的架構，載入已儲存的權重，並將所有內容包裝在模型修補器中，以便套用到其他模型。它支援許多專門的修補格式，包括額外的 ControlNet 分支、特徵嵌入器模型、適配器、動畫/LLLite 引導模組，以及類似模組。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `名稱` | 要從 `model_patches` 資料夾載入的模型修補檔案名稱。從清單中選擇其中一個可用的修補檔案。 | COMBO | 是 | 動態產生的清單，包含在 `model_patches` 資料夾中找到的所有模型修補檔案 |

注意：此節點標記為實驗性。修補類型會從檔案內容自動偵測，因此不需要手動選擇類型。此節點會讀取檢查點中繼資料，並檢查權重鍵，以決定要建構哪種架構（例如 Qwen Image block-wise ControlNet、Z-Image ControlNet、Wan Uni3C ControlNet、MiniMax H3 Fun ControlNet、SigLIP feature projection、Lightricks duration head、Anima LLLite、MultiTalk 或 SUPIR）。權重會以啟用安全載入的方式載入，模型會放置在 `CoreModelPatcher` 內的卸載裝置上，以便之後套用到另一個模型。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL_PATCH` | 已載入的模型修補，包裝在模型修補器中，準備好可套用到工作流程中的模型 | MODEL_PATCH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `069f40b1f108ecd74fc58c12aa2f74edff07f743aa1ed6352ff7bcf0c39341d4`
