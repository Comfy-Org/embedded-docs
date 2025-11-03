> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/zh-TW.md)

{heading_overview}

LatentBatchSeedBehavior 節點旨在修改潛在樣本批次的種子行為。它允許在整個批次中隨機化或固定種子，從而透過在生成輸出中引入變異性或保持一致性來影響生成過程。

{heading_inputs}

| 參數名稱       | 資料類型      | 描述 |
|-----------------|--------------|-------------|
| `samples`       | `LATENT`     | 此 'samples' 參數代表要處理的潛在樣本批次。其修改取決於所選的種子行為，會影響生成輸出的一致性或多樣性。 |
| `seed_behavior`  | COMBO[STRING] | 此 'seed_behavior' 參數決定潛在樣本批次的種子應該被隨機化還是固定。這個選擇會透過在整個批次中引入變異性或確保一致性，顯著影響生成過程。 |

{heading_outputs}

| 參數名稱 | 資料類型   | 描述 |
|-----------|-------------|-------------|
| `latent`  | `LATENT`    | 輸出是輸入潛在樣本的修改版本，根據指定的種子行為進行了調整。它會維持或改變批次索引以反映所選的種子行為。 |