# 模型取樣 LTXV

ModelSamplingLTXV 節點會根據 token 數量，將進階取樣參數套用至模型。它會使用線性內插在基礎偏移值與最大偏移值之間計算出偏移值，而計算方式取決於輸入 latent 中的 token 數量。接著，此節點會建立專門的模型取樣設定，並將其套用至輸入模型。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用取樣參數的輸入模型 | MODEL | 是 | - |
| `最大偏移` | 線性內插計算中使用的最大偏移值（預設值：2.05） | FLOAT | 是 | 0.0 至 100.0 (step: 0.01) |
| `基礎偏移` | 線性內插計算中使用的基礎偏移值（預設值：0.95） | FLOAT | 是 | 0.0 至 100.0 (step: 0.01) |
| `潛在空間` | 選用，用於決定偏移計算中 token 數量的 latent 輸入。若未提供，則使用預設 token 數量 4096 | LATENT | 否 | - |

偏移值的計算是透過在 1024 至 4096 的 token 範圍內，於 `base_shift` 與 `max_shift` 之間進行內插。當提供 `latent` 時，token 數量會由其空間維度（例如高度與寬度）的乘積計算得出。若未提供 `latent`，token 數量則預設為 4096。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用取樣參數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
