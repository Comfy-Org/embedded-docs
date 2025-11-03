> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/zh-TW.md)

LatentComposite 節點旨在將兩個潛在表徵混合或合併為單一輸出。此過程對於透過受控方式結合輸入潛在表徵的特性來創建複合圖像或特徵至關重要。

## 輸入參數

| 參數名稱       | 資料類型    | 描述 |
|----------------|-------------|------|
| `samples_to`   | `LATENT`    | 作為合成操作基礎的 'samples_to' 潛在表徵，'samples_from' 將被合成到其上。 |
| `samples_from` | `LATENT`    | 將被合成到 'samples_to' 上的 'samples_from' 潛在表徵，其特徵或特性將貢獻給最終的複合輸出。 |
| `x`            | `INT`       | 'samples_from' 潛在表徵在 'samples_to' 上放置的 x 座標（水平位置），決定複合內容的水平對齊方式。 |
| `y`            | `INT`       | 'samples_from' 潛在表徵在 'samples_to' 上放置的 y 座標（垂直位置），決定複合內容的垂直對齊方式。 |
| `feather`      | `INT`       | 布林值，指示在合成前是否應調整 'samples_from' 潛在表徵的大小以匹配 'samples_to'，這會影響複合結果的尺度和比例。 |

## 輸出參數

| 參數名稱 | 資料類型 | 描述 |
|----------|----------|------|
| `latent` | `LATENT` | 輸出為複合潛在表徵，根據指定的座標和調整大小選項，混合了 'samples_to' 和 'samples_from' 潛在表徵的特徵。 |