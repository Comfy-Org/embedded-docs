# 潛空間批次種子行為

LatentBatchSeedBehavior 節點旨在修改一批潛在樣本的種子行為。它允許在整個批次中隨機化或固定種子，從而透過引入變異性或維持生成輸出的一致性來影響生成過程。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `樣本` | 'samples' 參數代表要處理的潛在樣本批次。其修改取決於所選的種子行為，影響生成輸出的一致性或變異性。 | `LATENT` |
| `種子行為` | 'seed_behavior' 參數決定一批潛在樣本的種子應隨機化還是固定。此選擇透過引入變異性或確保整個批次的一致性，顯著影響生成過程。 | COMBO[STRING] |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 輸出是輸入潛在樣本的修改版本，根據指定的種子行為進行調整。它會維持或更改批次索引，以反映所選的種子行為。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/zh-TW.md)
