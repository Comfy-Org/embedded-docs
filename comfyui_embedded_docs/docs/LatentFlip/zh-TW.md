> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/zh-TW.md)

LatentFlip 節點旨在透過垂直或水平翻轉來操作潛在表徵。此操作可對潛在空間進行轉換，有可能在資料中發掘新的變化或視角。

## 輸入參數

| 參數名稱      | 資料類型       | 描述 |
|---------------|----------------|------|
| `samples`     | `LATENT`       | 此參數代表將被翻轉的潛在表徵。翻轉操作會根據 'flip_method' 參數垂直或水平地改變這些表徵，從而轉換潛在空間中的資料。 |
| `flip_method` | COMBO[STRING] | 此參數指定潛在樣本將沿哪個軸進行翻轉。可選 'x-axis: vertically'（垂直）或 'y-axis: horizontally'（水平），決定了翻轉方向以及對潛在表徵施加的轉換性質。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `latent` | `LATENT` | 輸出是輸入潛在表徵的修改版本，已根據指定方法進行翻轉。此轉換可在潛在空間中引入新的變化。 |