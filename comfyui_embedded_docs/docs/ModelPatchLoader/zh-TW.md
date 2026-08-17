# 模型修補載入器

ModelPatchLoader 節點從 `model_patches` 資料夾載入專業的模型修補檔。它會自動偵測修補檔的類型並載入對應的模型架構，然後將其包裝在 `ModelPatcher` 中以供工作流程使用。此節點支援不同的修補類型，包括 ControlNet 區塊、特徵嵌入器模型，以及其他專門的架構。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `name` | 要從 `model_patches` 目錄載入的模型修補檔檔案名稱 | STRING | 是 | `model_patches` 資料夾中所有可用的模型修補檔 |

注意：此節點在 ComfyUI 中被標記為實驗性功能。修補檔類型會從檔案內容中自動偵測，因此單一節點可以處理多種修補檔。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `MODEL_PATCH` | 已載入的模型修補檔，包裝在 `ModelPatcher` 中以供工作流程使用 | MODEL_PATCH |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh-TW.md)

---
**Source fingerprint (SHA-256):** `7f5225521b82b39b85183ccc7957fc4172e64aed9289f66d53969ea4a2e81b7f`
