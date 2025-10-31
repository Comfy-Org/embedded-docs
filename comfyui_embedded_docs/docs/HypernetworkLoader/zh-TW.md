> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HypernetworkLoader/zh-TW.md)

此節點會偵測位於 `ComfyUI/models/hypernetworks` 資料夾中的模型，同時也會從 extra_model_paths.yaml 檔案中設定的其他路徑讀取模型。有時您可能需要**重新整理 ComfyUI 介面**，才能讓它從相應的資料夾讀取模型檔案。

HypernetworkLoader 節點旨在透過應用超網路來增強或修改給定模型的能力。它會載入指定的超網路並將其應用於模型，根據強度參數可能改變其行為或效能。這個過程允許對模型的架構或參數進行動態調整，實現更靈活和自適應的 AI 系統。

## 輸入參數

| 欄位名稱 | Comfy 資料類型 | 描述 |
|---------|---------------|------|
| `model` | `MODEL` | 將應用超網路的基礎模型，決定要被增強或修改的架構。 |
| `hypernetwork_name` | `COMBO[STRING]` | 要載入並應用至模型的超網路名稱，會影響模型修改後的行為或效能。 |
| `強度` | `FLOAT` | 調整超網路對模型影響強度的標量值，允許對修改進行微調。 |

## 輸出結果

| 欄位名稱 | 資料類型 | 描述 |
|---------|---------|------|
| `model` | `MODEL` | 應用超網路後的修改模型，展示超網路對原始模型的影響效果。 |