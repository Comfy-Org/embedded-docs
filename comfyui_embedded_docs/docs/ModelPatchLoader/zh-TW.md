# 模型修補載入器

ModelPatchLoader 節點從 `model_patches` 資料夾載入專門的模型補丁檔案。它會自動從檔案內容偵測補丁類型，並載入對應的模型架構，然後將其包裝在 ModelPatcher 中以供工作流程使用。此節點支援不同的補丁類型，包括 controlnet 區塊、特徵嵌入模型，以及其他專門的架構。

## 輸入

| 參數 | 描述 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `名稱` | 要從 `model_patches` 資料夾載入的模型補丁檔案名稱 | STRING | 是 | `model_patches` 資料夾中所有可用的模型補丁檔案 |

注意：此節點標記為實驗性。補丁類型會從檔案內容自動偵測，因此無需手動選擇類型。

## 輸出

| 輸出名 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL_PATCH` | 已載入的模型補丁，包裝在 ModelPatcher 中以供工作流程使用 | MODEL_PATCH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
