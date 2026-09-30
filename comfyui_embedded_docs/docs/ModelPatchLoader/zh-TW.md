# 模型修補載入器

ModelPatchLoader 節點會從 `model_patches` 資料夾載入模型修補檔案，並準備好在工作流程中使用。它會自動偵測檔案中包含的修補類型、建立相符的架構、載入已儲存的權重，並將所有內容包裝在模型修補器中，以便套用到其他模型。它支援多種特殊修補格式，包括額外的 ControlNet 分支、特徵嵌入器模型、適配器、動畫/LLLite 引導模組及類似模組。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `名稱` | 要從 `model_patches` 資料夾載入的模型修補檔案名稱。從清單中選擇一個可用的修補檔案。 | COMBO | 是 | 動態產生的清單，包含在 `model_patches` 資料夾中找到的所有模型修補檔案 |

注意：此節點標示為實驗性。修補類型會自動從檔案內容偵測，因此不需要手動選擇類型。此節點會讀取 checkpoint 中繼資料並檢查權重鍵，以決定要建立哪種架構（例如 Qwen Image block-wise ControlNet、Qwen Image 2.1 Fun ControlNet、Z-Image ControlNet、Wan Uni3C ControlNet、MiniMax H3 Fun ControlNet、SigLIP feature projection、Lightricks duration head、Anima LLLite、MultiTalk 或 SUPIR）。權重載入時會啟用安全載入，且模型會放在 `CoreModelPatcher` 內的卸載裝置上，以便之後套用到另一個模型。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `MODEL_PATCH` | 已載入的模型修補，包裝在模型修補器中，準備好可套用到工作流程中的模型 | MODEL_PATCH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`
