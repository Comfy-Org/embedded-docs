> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/zh-TW.md)

{heading_overview}

ModelPatchLoader 節點從 model_patches 資料夾載入專門的模型修補檔案。它會自動偵測修補檔案的類型並載入適當的模型架構，然後將其封裝在 ModelPatcher 中以供工作流程使用。此節點支援不同的修補類型，包括 controlnet 區塊和特徵嵌入器模型。

{heading_inputs}

| 參數名稱 | 資料類型 | 必填 | 數值範圍 | 描述 |
|-----------|-----------|----------|-------|-------------|
| `name` | STRING | 是 | 來自 model_patches 資料夾的所有可用模型修補檔案 | 要從 model_patches 目錄載入的模型修補檔案名稱 |

{heading_outputs}

| 輸出名稱 | 資料類型 | 描述 |
|-------------|-----------|-------------|
| `MODEL_PATCH` | MODEL_PATCH | 已載入的模型修補，封裝在 ModelPatcher 中以供工作流程使用 |