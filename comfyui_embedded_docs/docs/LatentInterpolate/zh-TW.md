LatentInterpolate 節點旨在根據指定的比例對兩組潛在樣本進行插值，融合兩組樣本的特徵，以產生新的中間潛在樣本集。

## 輸入

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `samples1` | 第一組待插值的潛在樣本，作為插值過程的起點。 | `LATENT` |
| `samples2` | 第二組待插值的潛在樣本，作為插值過程的終點。 | `LATENT` |
| `比例` | 一個浮點數值，決定插值輸出中每組樣本的權重。比例為 0 時產生第一組樣本的副本，比例為 1 時則產生第二組樣本的副本。 | `FLOAT` |

## 輸出

| 參數 | 說明 | 資料類型 |
| --- | --- | --- |
| `latent` | 輸出為一組新的潛在樣本，代表根據指定比例在兩組輸入樣本之間的插值狀態。 | `LATENT` |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/zh-TW.md)
