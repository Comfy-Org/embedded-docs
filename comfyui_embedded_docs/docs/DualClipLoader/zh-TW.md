DualCLIPLoader 節點專為同時載入兩個 CLIP 模型而設計，便於執行需要整合或比較兩個模型特徵的操作。

此節點會偵測位於 `ComfyUI/models/text_encoders` 資料夾中的模型。

## 輸入

| 參數 | 描述 | Comfy 資料類型 |
| --- | --- | --- |
| `clip_name1` | 指定要載入的第一個 CLIP 模型名稱。此參數對於從預定義的可用 CLIP 模型清單中識別並檢索正確模型至關重要。 | COMBO[STRING] |
| `clip_name2` | 指定要載入的第二個 CLIP 模型名稱。此參數允許載入第二個不同的 CLIP 模型，以便與第一個模型進行比較或整合分析。 | COMBO[STRING] |
| `type` | 從 "sdxl"、"sd3"、"flux" 中選擇，以適應不同的模型。 | `option` |

* 載入順序不影響輸出效果

## 輸出

| 參數 | 描述 | 資料類型 |
| --- | --- | --- |
| `clip` | 輸出為一個組合後的 CLIP 模型，該模型整合了兩個指定 CLIP 模型的特徵或功能。 | CLIP |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/zh-TW.md)
