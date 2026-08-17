# 模型取樣 LTXV

ModelSamplingLTXV 節點根據 token 數量對模型套用進階取樣參數。它透過基線與最大偏移值之間的線性插值來計算偏移值，計算結果取決於輸入 latent 中的 token 數量。該節點隨後建立一個專門的模型取樣配置，並將其套用至輸入模型。

## 輸入

| 參數 | 描述 | 資料類型 | 必要 | 範圍 |
| --- | --- | --- | --- | --- |
| `model` | 要套用取樣參數的輸入模型 | MODEL | 是 | - |
| `max_shift` | 線性插值計算中使用的最大偏移值。在 4096 tokens 時，偏移值等於此最大值（預設：2.05） | FLOAT | 是 | 0.0 to 100.0 |
| `base_shift` | 線性插值計算中使用的基線偏移值。在 1024 tokens 時，偏移值等於此基線（預設：0.95） | FLOAT | 是 | 0.0 to 100.0 |
| `latent` | 可選的 latent 輸入，用於決定偏移計算的 token 數。token 數是 latent 樣本空間維度的乘積。若未提供，則使用預設 token 數 4096 | LATENT | 否 | - |

注意：偏移值是透過在 1024 tokens 時的 `base_shift` 與 4096 tokens 時的 `max_shift` 之間進行線性插值計算。當未提供 `latent` 時，預設 token 數為 4096，使偏移值等於 `max_shift`。

## 輸出

| 輸出名稱 | 描述 | 資料類型 |
| --- | --- | --- |
| `model` | 已套用取樣參數的修改後模型 | MODEL |

> 本文檔由 AI 生成。如果您發現任何錯誤或有改進建議，歡迎貢獻！ [在 GitHub 上編輯](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/zh-TW.md)

---
**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`
