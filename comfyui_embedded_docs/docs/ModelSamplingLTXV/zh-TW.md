# 模型取樣 LTXV

ModelSamplingLTXV 節點會根據 token 數量，將進階取樣參數套用至模型。它會在 token 範圍內對 `base_shift` 與 `max_shift` 進行線性插值來計算 shift 值，然後以專門的取樣設定修補輸入模型。若有提供 `latent`，其維度會決定 token 數量；否則會使用 4096 個 token。

## 輸入

| 參數 | 說明 | 資料類型 | 必填 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用取樣參數的輸入模型。 | MODEL | 是 | - |
| `最大偏移` | 線性插值計算中使用的最大 shift 值（預設值：2.05）。 | FLOAT | 是 | 0.0 到 100.0（步長：0.01） |
| `基礎偏移` | 線性插值計算中使用的基礎 shift 值（預設值：0.95）。 | FLOAT | 是 | 0.0 到 100.0（步長：0.01） |
| `潛在空間` | 選用的 latent 輸入，用於決定 shift 計算的 token 數量。若未提供，則使用預設 token 數量 4096。 | LATENT | 否 | - |

shift 值的計算方式，是在 1024 個 token 時使用 `base_shift`，並在 4096 個 token 時使用 `max_shift`，於兩者之間進行插值。當提供 `latent` 時，token 數量是 latent 樣本中前兩個維度之後所有維度的乘積（空間／時間維度）。若未提供 `latent`，token 數量預設為 4096。

## 輸出

| 輸出名稱 | 說明 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用取樣參數的修改後模型。 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
