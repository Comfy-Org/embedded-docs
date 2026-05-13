> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/zh-TW.md)

LatentComposite 節點旨在將兩個潛在表示混合或合併為單一輸出。此過程對於透過以受控方式結合輸入潛在特徵來建立合成影像或特徵至關重要。

## 輸入

| 參數 | 資料類型 | 描述 |
|--------------|-------------|-------------|
| `samples_to` | `LATENT` | `samples_to` 潛在表示，`samples_from` 將合成到其上。它作為合成操作的基礎。 |
| `samples_from` | `LATENT` | `samples_from` 潛在表示，將合成到 `samples_to` 上。它將其特徵或特性貢獻給最終的合成輸出。 |
| `x` | `INT` | `samples_from` 潛在將放置在 `samples_to` 上的 x 座標（水平位置）。它決定了合成的水平對齊方式。 |
| `y` | `INT` | `samples_from` 潛在將放置在 `samples_to` 上的 y 座標（垂直位置）。它決定了合成的垂直對齊方式。 |
| `feather` | `INT` | 一個布林值，指示在合成前是否應調整 `samples_from` 潛在的大小以匹配 `samples_to`。這會影響合成結果的比例和尺寸。 |

## 輸出

| 參數 | 資料類型 | 描述 |
|-----------|-------------|-------------|
| `latent` | `LATENT` | 輸出是一個合成的潛在表示，根據指定的座標和調整大小選項，融合了 `samples_to` 和 `samples_from` 潛在的特徵。 |